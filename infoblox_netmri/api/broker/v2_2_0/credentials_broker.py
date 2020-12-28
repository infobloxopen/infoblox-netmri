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

             :param VirtualNetworkID: VirtualNetwork ID to use with DeviceIPDotted if DeviceID is not set
             :type VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead: SNMPv1/2 Community string credential
             :type SNMPRead: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead2: SNMPv3 Community string credential
             :type SNMPRead2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPW: SNMP authorization Password
             :type SNMPAuthPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: SNMP authorization password
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPW: SNMP privacy password
             :type SNMPPrivPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: SNMP privacy protocol
             :type SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPVersion: SNMP Version
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
        """Executes a cli credential test against a supplied device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: Device ID to specify what device to test cli credentials on (takes precedence over IP address)
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: Device IP to specify what device to test cli credentials on
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
