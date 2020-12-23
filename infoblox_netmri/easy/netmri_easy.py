###########################################################################
# Export of Script Module: netmri_easy
# Language: Python
# Category: Internal
# Description: Object oriented library for Python scripting support
###########################################################################
import datetime
import sys
import time
from urllib.parse import urlparse

from infoblox_netmri.client import InfobloxNetMRI


class NetMRIEasy(object):
    def __init__(self, debug=False, **kwargs):
        self.debug = debug
        self.api_version = kwargs.get('api_version') or "auto"
        self.host = urlparse(kwargs.get('api_url')).hostname
        self.username = kwargs.get('http_username')
        self.password = kwargs.get('http_password')
        self.job_id = kwargs.get('job_id')
        self.device_id = kwargs.get('device_id')
        self.batch_id = kwargs.get('batch_id')
        self.script_login = kwargs.get('script_login')

        if (not self.job_id) or (not self.device_id) or (not self.batch_id):
            raise RuntimeError('job_id or device_id or batch_id not initialized')

        self.client = InfobloxNetMRI(
            self.host,
            self.username,
            self.password,
            api_version=self.api_version
        )

        self.dis_session = self._open_dis_session()
        if not self.script_login == 'false':
            self.cli_connection = self._open_cli_connection()
        self._setup_logging()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close_session()

    def broker(self, name):
        return self.client.get_broker(name)

    def _setup_logging(self):
        broker = self.broker('Job')
        if hasattr(broker, 'log_custom_message'):
            def remote_log_message(self, severity, message):
                date = datetime.datetime.now()
                brkr = self.broker('Job')
                msg_formatted = "{} [{:<7}] {}".format(
                    date.strftime("%Y-%m-%d %H:%M:%S "),
                    str(severity).upper(),
                    message
                )
                brkr.log_custom_message(message=msg_formatted, id=self.batch_id,
                                        jobdetailid=self.job_id, severity=severity)

            setattr(self.__class__, "remote_log_message", remote_log_message)
        else:
            def remote_log_message(self, severity, message):
                if not hasattr(self, 'cli_connection'):
                    return

                brkr = self._get_cli_broker()
                return brkr.log_message(
                    id=self.dis_session.SessionID,
                    device_id=self.device_id,
                    severity=severity,
                    message=message
                )

            setattr(self.__class__, "remote_log_message", remote_log_message)

    def _open_cli_connection(self):
        if getattr(self, 'cli_connection', None) and self.cli_connection:
            return self.cli_connection
        return self._get_cli_broker().open(
            id=self.dis_session.SessionID,
            DeviceID=self.device_id
        )

    def _close_dis_session(self):
        return self.broker('DisSession').close(id=self.dis_session.SessionID)

    def _open_dis_session(self):
        return self.broker('DisSession').open(job_id=self.job_id)

    def send_command(self, command, regex=None):
        if not hasattr(self, 'cli_connection'):
            return

        regex = regex or ""
        result = self._get_cli_broker().send_command(
            id=self.dis_session.SessionID,
            device_id=self.device_id,
            command=command,
            regex=regex
        )
        if result:
            return result.get('command_response')
        return result

    def send_async_command(self, command, timeout, regex, wait_until_finished=True):
        if not hasattr(self, 'cli_connection'):
            return

        regex = regex or ""
        self._print("Sending asynchronous command ({})".format(command))
        try:
            async_command_result = self._get_cli_broker().send_async_command(
                id=self.dis_session.SessionID,
                device_id=self.device_id,
                command=command,
                timeout=timeout,
                debug=self.debug,
                regex=regex,
            )
            self._ok()
            async_command_id = async_command_result.get('command_response')

            if async_command_id:
                async_command_id = async_command_id.replace("async_command_id:", "")
            else:
                self._error("Invalid send_async_command response ({})".format(str(async_command_id)))

            if not async_command_id.isdigit():
                self._error("Invalid send_async_command response ({})".format(str(async_command_id)))

            self._print("Received async_command_id {}".format(str(async_command_id)))
            self._ok()
            if not wait_until_finished:
                return async_command_id

            delay = 30
            max_delay = 14400 + 900  # DIS max session time plus a little padding (4.25 hours)
            cur_delay = 0
            ok = "async_command_id_status:OK\n"
            error = "async_command_id_status:Error\n"
            while True:
                self._print("Getting the status of async_command_id {}".format(async_command_id))
                res = self._get_cli_broker().get_async_command_status(
                    id=self.dis_session.SessionID,
                    device_id=self.device_id,
                    async_command_id=async_command_id
                )

                if not res:
                    self._error("Invalid get_async_command_status response ({})".format(res))
                result = res.get('command_response')

                if ok in result:
                    return result.replace(ok, '')

                if error in result:
                    self._error("Asynchronous command failed {}".format(
                        result.replace(error, '')
                    ))

                if cur_delay >= max_delay:
                    self._error("Timeout waiting for asynchronous command to complete")
                time.sleep(delay)
                cur_delay += delay

        except AttributeError:
            raise RuntimeError("Api version {} not support async commands. Minimal version: 2.10".format(
                self.client.api_version
            ))

    def get_config(self, sync=True):
        if not hasattr(self, 'cli_connection'):
            return

        self._print("Requesting on demand configuration collection ({})".format(sync))
        traking_id = None
        try:
            res = self.broker('ConfigRevision').get_configs(
                DeviceID=self.device_id
            )
            traking_id = res.get('TrackingID')

        except RuntimeError:
            raise RuntimeError("Api version {} not support this command. Minimal version: 2.10".format(
                self.client.api_version
            ))
        self._print("Received TrackingID {}".format(traking_id))
        self._ok()
        if not sync:
            return traking_id

        delay = 30
        max_delay = 600
        cur_delay = 0
        while True:
            self._print("Getting the status of TrackingID {}".format(traking_id))
            status_resp = self.broker('ConfigRevision').get_configs_status(
                TrackingID=traking_id
            )
            if status_resp.get('Status') == "OK":
                return status_resp

            if status_resp.get('Status') == "Error":
                self._error("On demand configuration collection failed")

            if cur_delay >= max_delay:
                self._error("Timeout waiting for configuration collection to complete")

            time.sleep(delay)
            cur_delay += delay

            self._print("Sending 'Keep Alive CR/LF'")
            self.send_command("NOP:")
            self._ok()

    def set_variable(self, name, value):
        if not hasattr(self, 'cli_connection'):
            return

        command = '${name} ="{value}"'.format(name=name, value=value)
        result = self._get_cli_broker().set_variable(
            id=self.dis_session.SessionID,
            device_id=self.device_id,
            command=command
        )
        if result:
            return result.get('command_response')
        return result

    def get_template(self, template_name, stage):
        if not hasattr(self, 'cli_connection'):
            return

        result = self._get_cli_broker().get_template(
            id=self.dis_session.SessionID,
            device_id=self.device_id,
            template=template_name,
            stage=(stage or 0)
        )
        if result:
            return result.get('command_response')
        return result

    def get_list_value(self, list_name, key_column, key_value, value_column, default):
        if not hasattr(self, 'cli_connection'):
            return

        result = self._get_cli_broker().get_list_value(
            id=self.dis_session.SessionID,
            device_id=self.device_id,
            list_name=list_name,
            key_column=key_column,
            key_value=key_value,
            value_column=value_column,
            default_value=default
        )
        if result:
            return result.get('command_response')
        return result

    def generate_issue(self, issue_type_id, severity, **kwargs):
        result = self.broker('IssueAdhoc').generate_issue(
            DeviceID=self.device_id,
            BatchID=self.batch_id,
            Severity=severity,
            IssueTypeID=issue_type_id,
            **kwargs
        )
        if result:
            return result.get('IssueID')
        return result

    def close_session(self):
        brkr = self.broker('DisSession')
        return brkr.close(
            SessionID=self.dis_session.SessionID
        )

    def get_device(self):
        return self.broker('Device').show(
            DeviceID=self.device_id
        )

    def log_message(self, severity, message):
        self.remote_log_message(severity, message)

    def _get_cli_broker(self):
        return self.client.get_broker('CliConnection')

    def _print(self, msg):
        if self.debug:
            print(msg)

    def _print_status(self, status):
        if self.debug:
            print(status)

    def _ok(self):
        self._print("OK")

    def _error(self, message):
        print("\n*** ERROR: {} ***\n".format(message))
        sys.exit(-1)
