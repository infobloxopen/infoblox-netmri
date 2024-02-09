from ..broker import Broker


class CredentialsBroker(Broker):
    controller = "credentials"

    def snmp_test(self, **kwargs):
        """Executes SNMP Test and returns results

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: Device ID to specify what device to test SNMP credentials on (takes precedence over IP address)
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: Device IP to specify what device to test SNMP credentials on
             :type DeviceIPDotted: String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: Unit ID to start polling from. Mutually exclusive to DeviceID
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The VirtualNetwork ID to use with DeviceIPDotted if DeviceID is not set
             :type VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead: The SNMPv1/2 Community string credential
             :type SNMPRead: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead2: The SNMPv3 Community string credential
             :type SNMPRead2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPW: The SNMPv3 authentication protocol password
             :type SNMPAuthPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMPv3 authentication protocol. Valid values are: 'md5', 'sha'
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPW: The SNMPv3 privacy protocol password
             :type SNMPPrivPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMPv3 privacy protocol. Valid values are: 'des', '3des', 'aes-128', 'aes-192', 'aes-256', 'aes-192c', 'aes-256c'
             :type SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param SNMPVersion: The SNMP version. Valid values are: 1, 2 or 3
             :type SNMPVersion: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the session output file to display.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param read: Offset from the start of the file.
             :type read: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the session output file.
             :rtype id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return read: Offset in bytes from the start of the file, to be used in the next snmp_test call, in order to retrieve the next lines of the output.
             :rtype read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return output: Result of the credential test.
             :rtype output: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the remaining output data to dump:
        <br><dd> 0: if the dump of the credential test output is completed.
        <br><dd> 1: if there is still output data to dump.
             :rtype status: Integer

            """

        return self.api_request(self._get_method_fullname("snmp_test"), kwargs)

    def cli_test(self, **kwargs):
        """Executes a CLI credential test against a supplied device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: Device ID to specify what device to test CLI credentials on (takes precedence over IP address)
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: Device IP to specify what device to test CLI credentials on
             :type DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: VirtualNetwork ID to use with DeviceIPDotted if DeviceID is not set
             :type VirtualNetworkID: Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: Unit ID to execute polling from. Mutually exclusive to DeviceID
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Username: CLI SSH username
             :type config.SSH.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Password: CLI SSH password
             :type config.SSH.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Username: CLI Telnet username
             :type config.Telnet.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Password: CLI Telnet password
             :type config.Telnet.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Username: CLI HTTP username
             :type config.HTTP.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Password: CLI HTTP password
             :type config.HTTP.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.EnablePassword: CLI enable password
             :type config.EnablePassword: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 22

             :param config.SSH.Port: CLI SSH Port
             :type config.SSH.Port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 23

             :param config.Telnet.Port: CLI Telnet Port
             :type config.Telnet.Port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param DoPostLogin: Flag to indicate if test should just attempt log in or log in and attempt to access enable mode
             :type DoPostLogin: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the session output file to display.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param read: Offset in bytes from the start of the file.
             :type read: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the session output file.
             :rtype id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return read: Offset in bytes from the start of the file, to be used in the next cli_test call, in order to retrieve the next lines of the output.
             :rtype read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return output: Result of the credential test.
             :rtype output: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the remaining output data to dump:
        <br><dd> 0: if the dump of the credential test output is completed.
        <br><dd> 1: if there is still output data to dump.
             :rtype status: Integer

            """

        return self.api_request(self._get_method_fullname("cli_test"), kwargs)

    def import_file(self, **kwargs):
        """Imports credentials from a file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file: The contents of the CSV file with the list of credentials to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param protocol: The protocol type of the credential. Valid values are: 'CLI', 'SNMP' or 'SNMPv3'
             :type protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param scope: The scope of the credential. Valid values are: 'User' or 'Vendor'
             :type scope: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The UnitID of the collector to which the credentials should be imported. 0 means all
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return success_count: The number of successfully imported credentials
             :rtype success_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return failure_count: The number of failed imported credentials
             :rtype failure_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return message: Information message
             :rtype message: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return errors: Error message, if exists
             :rtype errors: String

            """

        return self.api_request(self._get_method_fullname("import_file"), kwargs)
