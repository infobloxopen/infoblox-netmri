from ..broker import Broker


class CliConnectionBroker(Broker):
    controller = "cli_connections"

    def create(self, **kwargs):
        """Opens a CLI connection with the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_connection: The CLI connection object that represents a CLI connection with the device.
             :rtype cli_connection: CliConnection

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def open(self, **kwargs):
        """Opens a CLI connection with the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_connection: The CLI connection object that represents a CLI connection with the device.
             :rtype cli_connection: CliConnection

            """

        return self.api_request(self._get_method_fullname("open"), kwargs)

    def close(self, **kwargs):
        """Closes an open CLI connection with the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("close"), kwargs)

    def set_variable(self, **kwargs):
        """Set a local variable.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param command: The command to set a local variable.
             :type command: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("set_variable"), kwargs)

    def send_command(self, **kwargs):
        """Sends a command to the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param command: The command to send to the device.
             :type command: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param regex: Expected regex: prompt or question resulting of the command.
             :type regex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param debug: Option to test the command and not send to the device.
             :type debug: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("send_command"), kwargs)

    def send_async_command(self, **kwargs):
        """Sends a command to the device asynchronously.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param command: The command to send to the device.
             :type command: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param timeout: The command timeout.
             :type timeout: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param debug: Option to test the command and not send to the device.
             :type debug: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param regex: Expected regex: prompt or question resulting of the command.
             :type regex: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("send_async_command"), kwargs)

    def get_async_command_status(self, **kwargs):
        """Get the status of an asynchronously running command.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param async_command_id: The asynchronous command id.
             :type async_command_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("get_async_command_status"), kwargs)

    def get_template(self, **kwargs):
        """get template

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param template: The name of the template that contains commands to be evaluated.
             :type template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param stage: Option to stage the template.
             :type stage: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("get_template"), kwargs)

    def get_list_value(self, **kwargs):
        """Set local variables from a list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param list_name: Name or Short Name of the List
             :type list_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key_column: Key column for the search
             :type key_column: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key_value: Value which will be seached in the column
             :type key_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param value_column: Value of column which should be returned
             :type value_column: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param default_value: Value which will be returned if nothing was found
             :type default_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("get_list_value"), kwargs)

    def log_message(self, **kwargs):
        """Log a message of the given severity. The message will be written to the custom.log file.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param severity: The severity.
             :type severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param message: The message.
             :type message: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to sending the command.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("log_message"), kwargs)
