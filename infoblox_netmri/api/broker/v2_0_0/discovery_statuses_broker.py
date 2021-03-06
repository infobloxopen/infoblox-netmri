from ..broker import Broker


class DiscoveryStatusesBroker(Broker):
    controller = "discovery_statuses"

    def static(self, **kwargs):
        """Displays the current discovery statuses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` current

             :param view: Defined filters for displaying discovery statuses data. Valid values are "current", "licensed", "non_reached", "problems", "ok"
             :type view: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The index of the last row to display. Default value is 25
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: Search string
             :type query: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only. Specifying a UnitID will pull the most recent data from a specific collector while not specifying one will pull data directly from the OC.
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("static"), kwargs)

    def telnet_queue(self, **kwargs):
        """Displays the telnet queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("telnet_queue"), kwargs)

    def ssh_queue(self, **kwargs):
        """Displays the ssh queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("ssh_queue"), kwargs)

    def snmp_queue(self, **kwargs):
        """Displays the snmp queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("snmp_queue"), kwargs)

    def summary(self, **kwargs):
        """Summary data for discovery statuses

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("summary"), kwargs)

    def discover_next(self, **kwargs):
        """Set the given device ids to be discovered next

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: An array of device ids to be discovered next
             :type DeviceIDs: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discover_next"), kwargs)

    def discover_now(self, **kwargs):
        """Set the "DeviceID" of the given device to be discovered now and check the status of previously started discovery process. If the "id" parameter is not set, the method starts a new Discover Now process and returns its id for further tracking the process status. If the "id" parameter is set, the method returns a chunk of log output of the corresponding discovery process. The number of bytes to read is defined by the "read" parameter.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the previously started discovery process required to retrieve its status
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param DeviceID: ID of the device to re-discover now, if known
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address: Device IP address to be discovered now
             :type ip_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the discover now output
             :type read: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param ignore_history_ind: If true, NetMRI will not check for previous instances of this IP address, and therefore will not associate this IP address with the associated device history.
             :type ignore_history_ind: Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mac_address: Device MAC address to be discovered now
             :type mac_address: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discover_now"), kwargs)

    def abort_discovery(self, **kwargs):
        """Abort an outstanding discover now session

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: ID of the discover now request to abort
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("abort_discovery"), kwargs)

    def override_licenses(self, **kwargs):
        """Overrides a license for all or some devices

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: The list of devices to override licenses
             :type DeviceIDs: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Licensed: The state of the device license override. Valid values are 0 (unlicensed), 1 (licensed), 2 (automatic)
             :type Licensed: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortManagement: The state of the Switch Port Management license override. Valid values are on or off if exists. An empty string is passed if not present.
             :type SwitchPortManagement: String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessProvisioning: The state of the Security Device Controller license override. Valid values are on or off if exists. An empty string is passed if not present.
             :type AccessProvisioning: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("override_licenses"), kwargs)

    def unmanage(self, **kwargs):
        """Set one or more specified devices to unmanaged

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: The list of devices to set to unmanaged
             :type DeviceIDs: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("unmanage"), kwargs)

    def update_snmp(self, **kwargs):
        """Update the SNMP read credential for a device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to be updated
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPVersion: The SNMP Version
             :type SNMPVersion: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead: The SNMP read community
             :type SNMPRead: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPW: The SNMP auth password for SNMPv3
             :type SNMPAuthPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMP auth protocol for SNMPv3
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPW: The SNMP priv password for SNMPv3
             :type SNMPPrivPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMP priv protocol for SNMPv3
             :type SNMPPrivProto: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_snmp"), kwargs)

    def update_cli_credentials(self, **kwargs):
        """Update the CLI credential for a device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to be updated
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Username: SSH username
             :type config.SSH.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Password: SSH password
             :type config.SSH.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Username: Telnet username
             :type config.Telnet.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Password: Telnet password
             :type config.Telnet.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Username: HTTP username
             :type config.HTTP.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Password: HTTP password
             :type config.HTTP.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.EnablePassword: Enable password
             :type config.EnablePassword: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_cli_credentials"), kwargs)

    def cli_guesses(self, **kwargs):
        """Displays the status of all devices CLI guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cli_guesses"), kwargs)

    def snmp_guesses(self, **kwargs):
        """Displays the status of all devices SNMP guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("snmp_guesses"), kwargs)

    def show_opsec_certificate(self, **kwargs):
        """Return OPSEC device certificate

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show_opsec_certificate"), kwargs)

    def opsec_guesses(self, **kwargs):
        """Displays the status of all devices OPSEC guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("opsec_guesses"), kwargs)

    def status_management(self, **kwargs):
        """Returns a list of discovery statuses of the device with given id

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to get management status
             :type DeviceID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("status_management"), kwargs)

    def setup_summary(self, **kwargs):
        """Discovery Wizard setup summary information

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("setup_summary"), kwargs)
