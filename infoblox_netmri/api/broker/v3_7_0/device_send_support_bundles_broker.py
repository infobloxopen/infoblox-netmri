from ..broker import Broker


class DeviceSendSupportBundlesBroker(Broker):
    controller = "device_send_support_bundles"

    def groups_and_definitions(self, **kwargs):
        """Returns set of Log files groupings and definitions of them

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return debug_groups: List of debug group objects
             :rtype debug_groups: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return definitions: List of debug definition objects
             :rtype definitions: Array

            """

        return self.api_request(self._get_method_fullname("groups_and_definitions"), kwargs)

    def support_bundle_statuses(self, **kwargs):
        """Returns set of Support Bundle statuses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: Offset for the Support Bundle statuses to be returned.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param limit: Limit of rows of Support Bundle statuses to be returned.
             :type limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return rows: List of support bundle status objects
             :rtype rows: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return total: Total amount of support bundle statuses
             :rtype total: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return updated: Timestamp for last request update
             :rtype updated: DateTime

            """

        return self.api_request(self._get_method_fullname("support_bundle_statuses"), kwargs)

    def create(self, **kwargs):
        """Initiates a Device Support Bundle Request

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param support_case_number: The identifier for Support Bundle Request
             :type support_case_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param definitions: Set of debug definitions ids to enable
             :type definitions: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param debug_groups: Set of debug groups ids to enable
             :type debug_groups: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_ip_range: Set of ip addresses for SNMP debugging
             :type snmp_ip_range: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ip_address: The IP address of the device.
             :type device_ip_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` SNMPv2

             :param snmp_version: The SNMP Version.
             :type snmp_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_community_string: The SNMP community string associated with the device.
             :type snmp_community_string: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_oid: The SNMP OID identifier
             :type snmp_oid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_auth_username: The SNMP username associated with the device. Used only for SNMP Version 3.
             :type snmp_auth_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` md5

             :param snmp_auth_protocol: The SNMP authenticationprotocol associated with the device. Used only for SNMP Version 3.
             :type snmp_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_auth_password: The SNMP authentication password associated with the device. Used only for SNMP Version 3.
             :type snmp_auth_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` aes-128

             :param snmp_privacy_protocol: The SNMP privacy protocol associated with the device. Used only for SNMP Version 3.
             :type snmp_privacy_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_privacy_password: The SNMP privacy password associated with the device. Used only for SNMP Version 3.
             :type snmp_privacy_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` sftp

             :param delivery_method: The final delivery method of the device Support Bundle Request.
             :type delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param notification_email: The email address that used for notifications
             :type notification_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param duration_time: Time in hours for how long debugging process will be enabled
             :type duration_time: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The unique identifier for Support Bundle Request initialized
             :rtype id: Integer

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def delete_log_file(self, **kwargs):
        """Delete the Support Bundle log file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file_id: The identifier of log filename being deleted
             :type file_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete_log_file"), kwargs)

    def resend_log_file(self, **kwargs):
        """Resend the Support Bundle log file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file_id: The identifier of log filename being resent
             :type file_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("resend_log_file"), kwargs)

    def download_status_log(self, **kwargs):
        """Download log file associated with the Support Bundle status

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param support_case_number: The identifier for Support Bundle Request
             :type support_case_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param filename: Name for status log file
             :type filename: String

            **Outputs**

            """

        return self.api_mixed_request(self._get_method_fullname("download_status_log"), kwargs)
