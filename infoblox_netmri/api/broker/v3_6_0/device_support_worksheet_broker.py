from ..broker import Broker


class DeviceSupportWorksheetBroker(Broker):
    controller = "device_support_worksheets"

    def index(self, **kwargs):
        """Lists the available device support worksheets. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal system identifier of the associated device support request worksheet.
             :type id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DeviceSupportWorksheet. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_worksheets: An array of the DeviceSupportWorksheet objects that match the specified input criteria.
             :rtype device_support_worksheets: Array of DeviceSupportWorksheet

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device support worksheets matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access_to_device: Information about how Infoblox will access the device for site testing.
             :type access_to_device: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access_to_device_other: Other information about how Infoblox will access the device.
             :type access_to_device_other: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param admin_guide_collected_ind: Flag indicating that the admin guide was collected.
             :type admin_guide_collected_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_password: The CLI Password of the device.
             :type cli_password: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_session_collected_ind: Flag indicating that CLI data was collected.
             :type cli_session_collected_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_username: The CLI Username of the device.
             :type cli_username: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param contact_method: How the customer should be contacted (valid values are 'Email' and 'Phone').
             :type contact_method: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param contact_name: A name of a person to contact.
             :type contact_name: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param contact_value: E-mail address or phone that can be used to contact the customer.
             :type contact_value: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in the system.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param customer_name: Customer name.
             :type customer_name: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param delivery_addl_email: Additional email addresses to which the device support data bundle is sent.
             :type delivery_addl_email: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param delivery_method: The method of delivery (sftp, email, or download) for the device support data bundle.
             :type delivery_method: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_discovered_ind: A flag indicating that the device has been discovered by the system.
             :type device_discovered_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal system identifier of the associated device.
             :type device_id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ip_dotted: The IP address of the associated device.
             :type device_ip_dotted: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_model: The device model of the associated device as determined by the system.
             :type device_model: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_type: The device type of the associated device as determined by system.
             :type device_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_vendor: The vendor of the associated device as determined by the system.
             :type device_vendor: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param discovery_diagnostic_collected_ind: Flag indicating that discovery diagnostics were collected.
             :type discovery_diagnostic_collected_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal system identifier of the associated device support request worksheet.
             :type id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param license_expiration: The expiration of the NetMRI license
             :type license_expiration: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param license_id: The NetMRI license identifier.
             :type license_id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param license_type: The NetMRI license type.
             :type license_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param manual_data_entry_ind: Flag indicating that device data is being collected in manual mode.
             :type manual_data_entry_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param netmri_version: The NetMRI version.
             :type netmri_version: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param os_version: The OS version of the associated device as determined by the system.
             :type os_version: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param package_name: The name of the compressed, encrypted device support data package.
             :type package_name: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param preferred_cli: The preferred CLI method (SSH, Telnet, or Other).
             :type preferred_cli: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param priv_mode_info: Privileged mode information.
             :type priv_mode_info: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secure_version: The encryption secure version of the credentials.
             :type secure_version: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_auth_password: The SNMP authorized password of the device (SNMPv3 only).
             :type snmp_auth_password: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_auth_protocol: The SNMP authorized protocol of the device (SNMPv3 only).
             :type snmp_auth_protocol: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_auth_username: The SNMP authorized username of the device (SNMPv3 only).
             :type snmp_auth_username: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_community_string: The SNMP community string of the device.
             :type snmp_community_string: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_data_collected_ind: Flag indicating that SNMP data was collected.
             :type snmp_data_collected_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_port: The SNMP port of the device.
             :type snmp_port: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_privacy_password: The SNMP privacy password of the device (SNMPv3 only).
             :type snmp_privacy_password: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_privacy_protocol: The SNMP privacy protocol of the device (SNMPv3 only).
             :type snmp_privacy_protocol: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_version: The SNMP version of the device (SNMPv1, SNMPv2, or SNMPv3).
             :type snmp_version: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The overall status of the device support request worksheet.
             :type status: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status_msg: Error message associated with worksheet status. Currently, only contain error messages for "Transfer Failed" status.
             :type status_msg: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param step_number: The last step which the worksheet was saved at.
             :type step_number: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param syslogs_collected_ind: Flag indicating that the syslogs were collected.
             :type syslogs_collected_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: The internal identifier for the collector that is used to collect the device support data. Used in an OC only.
             :type unit_id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in the system.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_in_device_capabilities: The device capabilities as determined by the user.
             :type user_in_device_capabilities: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_in_device_model: The device model as determined by the user.
             :type user_in_device_model: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_in_device_type: The device type as determined by the user.
             :type user_in_device_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_in_device_vendor: The device vendor as determined by the user.
             :type user_in_device_vendor: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_in_os_version: The os version as determined by the user.
             :type user_in_os_version: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal identifier for the network which the device is associated to.
             :type virtual_network_id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DeviceSupportWorksheet. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against device support worksheets, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: access_to_device, access_to_device_other, admin_guide_collected_ind, cli_password, cli_session_collected_ind, cli_username, contact_method, contact_name, contact_value, created_at, customer_name, delivery_addl_email, delivery_method, device_discovered_ind, device_id, device_ip_dotted, device_model, device_type, device_vendor, discovery_diagnostic_collected_ind, id, license_expiration, license_id, license_type, manual_data_entry_ind, netmri_version, os_version, package_name, preferred_cli, priv_mode_info, secure_version, snmp_auth_password, snmp_auth_protocol, snmp_auth_username, snmp_community_string, snmp_data_collected_ind, snmp_port, snmp_privacy_password, snmp_privacy_protocol, snmp_version, status, status_msg, step_number, syslogs_collected_ind, unit_id, updated_at, user_in_device_capabilities, user_in_device_model, user_in_device_type, user_in_device_vendor, user_in_os_version, virtual_network_id.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_worksheets: An array of the DeviceSupportWorksheet objects that match the specified input criteria.
             :rtype device_support_worksheets: Array of DeviceSupportWorksheet

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device support worksheets matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: access_to_device, access_to_device_other, admin_guide_collected_ind, cli_password, cli_session_collected_ind, cli_username, contact_method, contact_name, contact_value, created_at, customer_name, delivery_addl_email, delivery_method, device_discovered_ind, device_id, device_ip_dotted, device_model, device_type, device_vendor, discovery_diagnostic_collected_ind, id, license_expiration, license_id, license_type, manual_data_entry_ind, netmri_version, os_version, package_name, preferred_cli, priv_mode_info, secure_version, snmp_auth_password, snmp_auth_protocol, snmp_auth_username, snmp_community_string, snmp_data_collected_ind, snmp_port, snmp_privacy_password, snmp_privacy_protocol, snmp_version, status, status_msg, step_number, syslogs_collected_ind, unit_id, updated_at, user_in_device_capabilities, user_in_device_model, user_in_device_type, user_in_device_vendor, user_in_os_version, virtual_network_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_access_to_device: The operator to apply to the field access_to_device. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. access_to_device: Information about how Infoblox will access the device for site testing. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_access_to_device: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_access_to_device: If op_access_to_device is specified, the field named in this input will be compared to the value in access_to_device using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_access_to_device must be specified if op_access_to_device is specified.
             :type val_f_access_to_device: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_access_to_device: If op_access_to_device is specified, this value will be compared to the value in access_to_device using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_access_to_device must be specified if op_access_to_device is specified.
             :type val_c_access_to_device: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_access_to_device_other: The operator to apply to the field access_to_device_other. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. access_to_device_other: Other information about how Infoblox will access the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_access_to_device_other: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_access_to_device_other: If op_access_to_device_other is specified, the field named in this input will be compared to the value in access_to_device_other using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_access_to_device_other must be specified if op_access_to_device_other is specified.
             :type val_f_access_to_device_other: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_access_to_device_other: If op_access_to_device_other is specified, this value will be compared to the value in access_to_device_other using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_access_to_device_other must be specified if op_access_to_device_other is specified.
             :type val_c_access_to_device_other: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_admin_guide_collected_ind: The operator to apply to the field admin_guide_collected_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. admin_guide_collected_ind: Flag indicating that the admin guide was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_admin_guide_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_admin_guide_collected_ind: If op_admin_guide_collected_ind is specified, the field named in this input will be compared to the value in admin_guide_collected_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_admin_guide_collected_ind must be specified if op_admin_guide_collected_ind is specified.
             :type val_f_admin_guide_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_admin_guide_collected_ind: If op_admin_guide_collected_ind is specified, this value will be compared to the value in admin_guide_collected_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_admin_guide_collected_ind must be specified if op_admin_guide_collected_ind is specified.
             :type val_c_admin_guide_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_password: The operator to apply to the field cli_password. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_password: The CLI Password of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_password: If op_cli_password is specified, the field named in this input will be compared to the value in cli_password using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_password must be specified if op_cli_password is specified.
             :type val_f_cli_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_password: If op_cli_password is specified, this value will be compared to the value in cli_password using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_password must be specified if op_cli_password is specified.
             :type val_c_cli_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_session_collected_ind: The operator to apply to the field cli_session_collected_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_session_collected_ind: Flag indicating that CLI data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_session_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_session_collected_ind: If op_cli_session_collected_ind is specified, the field named in this input will be compared to the value in cli_session_collected_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_session_collected_ind must be specified if op_cli_session_collected_ind is specified.
             :type val_f_cli_session_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_session_collected_ind: If op_cli_session_collected_ind is specified, this value will be compared to the value in cli_session_collected_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_session_collected_ind must be specified if op_cli_session_collected_ind is specified.
             :type val_c_cli_session_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_username: The operator to apply to the field cli_username. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_username: The CLI Username of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_username: If op_cli_username is specified, the field named in this input will be compared to the value in cli_username using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_username must be specified if op_cli_username is specified.
             :type val_f_cli_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_username: If op_cli_username is specified, this value will be compared to the value in cli_username using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_username must be specified if op_cli_username is specified.
             :type val_c_cli_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_contact_method: The operator to apply to the field contact_method. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. contact_method: How the customer should be contacted (valid values are 'Email' and 'Phone'). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_contact_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_contact_method: If op_contact_method is specified, the field named in this input will be compared to the value in contact_method using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_contact_method must be specified if op_contact_method is specified.
             :type val_f_contact_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_contact_method: If op_contact_method is specified, this value will be compared to the value in contact_method using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_contact_method must be specified if op_contact_method is specified.
             :type val_c_contact_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_contact_name: The operator to apply to the field contact_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. contact_name: A name of a person to contact. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_contact_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_contact_name: If op_contact_name is specified, the field named in this input will be compared to the value in contact_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_contact_name must be specified if op_contact_name is specified.
             :type val_f_contact_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_contact_name: If op_contact_name is specified, this value will be compared to the value in contact_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_contact_name must be specified if op_contact_name is specified.
             :type val_c_contact_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_contact_value: The operator to apply to the field contact_value. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. contact_value: E-mail address or phone that can be used to contact the customer. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_contact_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_contact_value: If op_contact_value is specified, the field named in this input will be compared to the value in contact_value using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_contact_value must be specified if op_contact_value is specified.
             :type val_f_contact_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_contact_value: If op_contact_value is specified, this value will be compared to the value in contact_value using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_contact_value must be specified if op_contact_value is specified.
             :type val_c_contact_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the record was initially created in the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_at: If op_created_at is specified, the field named in this input will be compared to the value in created_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_at must be specified if op_created_at is specified.
             :type val_f_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_at: If op_created_at is specified, this value will be compared to the value in created_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_at must be specified if op_created_at is specified.
             :type val_c_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_customer_name: The operator to apply to the field customer_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. customer_name: Customer name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_customer_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_customer_name: If op_customer_name is specified, the field named in this input will be compared to the value in customer_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_customer_name must be specified if op_customer_name is specified.
             :type val_f_customer_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_customer_name: If op_customer_name is specified, this value will be compared to the value in customer_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_customer_name must be specified if op_customer_name is specified.
             :type val_c_customer_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_delivery_addl_email: The operator to apply to the field delivery_addl_email. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. delivery_addl_email: Additional email addresses to which the device support data bundle is sent. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_delivery_addl_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_delivery_addl_email: If op_delivery_addl_email is specified, the field named in this input will be compared to the value in delivery_addl_email using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_delivery_addl_email must be specified if op_delivery_addl_email is specified.
             :type val_f_delivery_addl_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_delivery_addl_email: If op_delivery_addl_email is specified, this value will be compared to the value in delivery_addl_email using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_delivery_addl_email must be specified if op_delivery_addl_email is specified.
             :type val_c_delivery_addl_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_delivery_method: The operator to apply to the field delivery_method. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. delivery_method: The method of delivery (sftp, email, or download) for the device support data bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_delivery_method: If op_delivery_method is specified, the field named in this input will be compared to the value in delivery_method using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_delivery_method must be specified if op_delivery_method is specified.
             :type val_f_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_delivery_method: If op_delivery_method is specified, this value will be compared to the value in delivery_method using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_delivery_method must be specified if op_delivery_method is specified.
             :type val_c_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_discovered_ind: The operator to apply to the field device_discovered_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_discovered_ind: A flag indicating that the device has been discovered by the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_discovered_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_discovered_ind: If op_device_discovered_ind is specified, the field named in this input will be compared to the value in device_discovered_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_discovered_ind must be specified if op_device_discovered_ind is specified.
             :type val_f_device_discovered_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_discovered_ind: If op_device_discovered_ind is specified, this value will be compared to the value in device_discovered_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_discovered_ind must be specified if op_device_discovered_ind is specified.
             :type val_c_device_discovered_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_id: The operator to apply to the field device_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_id: The internal system identifier of the associated device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_id: If op_device_id is specified, the field named in this input will be compared to the value in device_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_id must be specified if op_device_id is specified.
             :type val_f_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_id: If op_device_id is specified, this value will be compared to the value in device_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_id must be specified if op_device_id is specified.
             :type val_c_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_ip_dotted: The operator to apply to the field device_ip_dotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_ip_dotted: The IP address of the associated device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_ip_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_ip_dotted: If op_device_ip_dotted is specified, the field named in this input will be compared to the value in device_ip_dotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_ip_dotted must be specified if op_device_ip_dotted is specified.
             :type val_f_device_ip_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_ip_dotted: If op_device_ip_dotted is specified, this value will be compared to the value in device_ip_dotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_ip_dotted must be specified if op_device_ip_dotted is specified.
             :type val_c_device_ip_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_model: The operator to apply to the field device_model. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_model: The device model of the associated device as determined by the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_model: If op_device_model is specified, the field named in this input will be compared to the value in device_model using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_model must be specified if op_device_model is specified.
             :type val_f_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_model: If op_device_model is specified, this value will be compared to the value in device_model using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_model must be specified if op_device_model is specified.
             :type val_c_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_type: The operator to apply to the field device_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_type: The device type of the associated device as determined by system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_type: If op_device_type is specified, the field named in this input will be compared to the value in device_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_type must be specified if op_device_type is specified.
             :type val_f_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_type: If op_device_type is specified, this value will be compared to the value in device_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_type must be specified if op_device_type is specified.
             :type val_c_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_vendor: The operator to apply to the field device_vendor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_vendor: The vendor of the associated device as determined by the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_vendor: If op_device_vendor is specified, the field named in this input will be compared to the value in device_vendor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_vendor must be specified if op_device_vendor is specified.
             :type val_f_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_vendor: If op_device_vendor is specified, this value will be compared to the value in device_vendor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_vendor must be specified if op_device_vendor is specified.
             :type val_c_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_discovery_diagnostic_collected_ind: The operator to apply to the field discovery_diagnostic_collected_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. discovery_diagnostic_collected_ind: Flag indicating that discovery diagnostics were collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_discovery_diagnostic_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_discovery_diagnostic_collected_ind: If op_discovery_diagnostic_collected_ind is specified, the field named in this input will be compared to the value in discovery_diagnostic_collected_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_discovery_diagnostic_collected_ind must be specified if op_discovery_diagnostic_collected_ind is specified.
             :type val_f_discovery_diagnostic_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_discovery_diagnostic_collected_ind: If op_discovery_diagnostic_collected_ind is specified, this value will be compared to the value in discovery_diagnostic_collected_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_discovery_diagnostic_collected_ind must be specified if op_discovery_diagnostic_collected_ind is specified.
             :type val_c_discovery_diagnostic_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal system identifier of the associated device support request worksheet. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_id: If op_id is specified, the field named in this input will be compared to the value in id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_id must be specified if op_id is specified.
             :type val_f_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_id: If op_id is specified, this value will be compared to the value in id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_id must be specified if op_id is specified.
             :type val_c_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_license_expiration: The operator to apply to the field license_expiration. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. license_expiration: The expiration of the NetMRI license For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_license_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_license_expiration: If op_license_expiration is specified, the field named in this input will be compared to the value in license_expiration using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_license_expiration must be specified if op_license_expiration is specified.
             :type val_f_license_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_license_expiration: If op_license_expiration is specified, this value will be compared to the value in license_expiration using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_license_expiration must be specified if op_license_expiration is specified.
             :type val_c_license_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_license_id: The operator to apply to the field license_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. license_id: The NetMRI license identifier. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_license_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_license_id: If op_license_id is specified, the field named in this input will be compared to the value in license_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_license_id must be specified if op_license_id is specified.
             :type val_f_license_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_license_id: If op_license_id is specified, this value will be compared to the value in license_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_license_id must be specified if op_license_id is specified.
             :type val_c_license_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_license_type: The operator to apply to the field license_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. license_type: The NetMRI license type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_license_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_license_type: If op_license_type is specified, the field named in this input will be compared to the value in license_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_license_type must be specified if op_license_type is specified.
             :type val_f_license_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_license_type: If op_license_type is specified, this value will be compared to the value in license_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_license_type must be specified if op_license_type is specified.
             :type val_c_license_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_manual_data_entry_ind: The operator to apply to the field manual_data_entry_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. manual_data_entry_ind: Flag indicating that device data is being collected in manual mode. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_manual_data_entry_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_manual_data_entry_ind: If op_manual_data_entry_ind is specified, the field named in this input will be compared to the value in manual_data_entry_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_manual_data_entry_ind must be specified if op_manual_data_entry_ind is specified.
             :type val_f_manual_data_entry_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_manual_data_entry_ind: If op_manual_data_entry_ind is specified, this value will be compared to the value in manual_data_entry_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_manual_data_entry_ind must be specified if op_manual_data_entry_ind is specified.
             :type val_c_manual_data_entry_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_netmri_version: The operator to apply to the field netmri_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. netmri_version: The NetMRI version. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_netmri_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_netmri_version: If op_netmri_version is specified, the field named in this input will be compared to the value in netmri_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_netmri_version must be specified if op_netmri_version is specified.
             :type val_f_netmri_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_netmri_version: If op_netmri_version is specified, this value will be compared to the value in netmri_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_netmri_version must be specified if op_netmri_version is specified.
             :type val_c_netmri_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_os_version: The operator to apply to the field os_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. os_version: The OS version of the associated device as determined by the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_os_version: If op_os_version is specified, the field named in this input will be compared to the value in os_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_os_version must be specified if op_os_version is specified.
             :type val_f_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_os_version: If op_os_version is specified, this value will be compared to the value in os_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_os_version must be specified if op_os_version is specified.
             :type val_c_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_package_name: The operator to apply to the field package_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. package_name: The name of the compressed, encrypted device support data package. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_package_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_package_name: If op_package_name is specified, the field named in this input will be compared to the value in package_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_package_name must be specified if op_package_name is specified.
             :type val_f_package_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_package_name: If op_package_name is specified, this value will be compared to the value in package_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_package_name must be specified if op_package_name is specified.
             :type val_c_package_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_preferred_cli: The operator to apply to the field preferred_cli. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. preferred_cli: The preferred CLI method (SSH, Telnet, or Other). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_preferred_cli: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_preferred_cli: If op_preferred_cli is specified, the field named in this input will be compared to the value in preferred_cli using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_preferred_cli must be specified if op_preferred_cli is specified.
             :type val_f_preferred_cli: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_preferred_cli: If op_preferred_cli is specified, this value will be compared to the value in preferred_cli using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_preferred_cli must be specified if op_preferred_cli is specified.
             :type val_c_preferred_cli: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_priv_mode_info: The operator to apply to the field priv_mode_info. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. priv_mode_info: Privileged mode information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_priv_mode_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_priv_mode_info: If op_priv_mode_info is specified, the field named in this input will be compared to the value in priv_mode_info using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_priv_mode_info must be specified if op_priv_mode_info is specified.
             :type val_f_priv_mode_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_priv_mode_info: If op_priv_mode_info is specified, this value will be compared to the value in priv_mode_info using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_priv_mode_info must be specified if op_priv_mode_info is specified.
             :type val_c_priv_mode_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_secure_version: The operator to apply to the field secure_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. secure_version: The encryption secure version of the credentials. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_secure_version: If op_secure_version is specified, the field named in this input will be compared to the value in secure_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_secure_version must be specified if op_secure_version is specified.
             :type val_f_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_secure_version: If op_secure_version is specified, this value will be compared to the value in secure_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_secure_version must be specified if op_secure_version is specified.
             :type val_c_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_auth_password: The operator to apply to the field snmp_auth_password. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_auth_password: The SNMP authorized password of the device (SNMPv3 only). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_auth_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_auth_password: If op_snmp_auth_password is specified, the field named in this input will be compared to the value in snmp_auth_password using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_auth_password must be specified if op_snmp_auth_password is specified.
             :type val_f_snmp_auth_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_auth_password: If op_snmp_auth_password is specified, this value will be compared to the value in snmp_auth_password using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_auth_password must be specified if op_snmp_auth_password is specified.
             :type val_c_snmp_auth_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_auth_protocol: The operator to apply to the field snmp_auth_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_auth_protocol: The SNMP authorized protocol of the device (SNMPv3 only). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_auth_protocol: If op_snmp_auth_protocol is specified, the field named in this input will be compared to the value in snmp_auth_protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_auth_protocol must be specified if op_snmp_auth_protocol is specified.
             :type val_f_snmp_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_auth_protocol: If op_snmp_auth_protocol is specified, this value will be compared to the value in snmp_auth_protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_auth_protocol must be specified if op_snmp_auth_protocol is specified.
             :type val_c_snmp_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_auth_username: The operator to apply to the field snmp_auth_username. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_auth_username: The SNMP authorized username of the device (SNMPv3 only). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_auth_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_auth_username: If op_snmp_auth_username is specified, the field named in this input will be compared to the value in snmp_auth_username using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_auth_username must be specified if op_snmp_auth_username is specified.
             :type val_f_snmp_auth_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_auth_username: If op_snmp_auth_username is specified, this value will be compared to the value in snmp_auth_username using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_auth_username must be specified if op_snmp_auth_username is specified.
             :type val_c_snmp_auth_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_community_string: The operator to apply to the field snmp_community_string. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_community_string: The SNMP community string of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_community_string: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_community_string: If op_snmp_community_string is specified, the field named in this input will be compared to the value in snmp_community_string using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_community_string must be specified if op_snmp_community_string is specified.
             :type val_f_snmp_community_string: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_community_string: If op_snmp_community_string is specified, this value will be compared to the value in snmp_community_string using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_community_string must be specified if op_snmp_community_string is specified.
             :type val_c_snmp_community_string: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_data_collected_ind: The operator to apply to the field snmp_data_collected_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_data_collected_ind: Flag indicating that SNMP data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_data_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_data_collected_ind: If op_snmp_data_collected_ind is specified, the field named in this input will be compared to the value in snmp_data_collected_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_data_collected_ind must be specified if op_snmp_data_collected_ind is specified.
             :type val_f_snmp_data_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_data_collected_ind: If op_snmp_data_collected_ind is specified, this value will be compared to the value in snmp_data_collected_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_data_collected_ind must be specified if op_snmp_data_collected_ind is specified.
             :type val_c_snmp_data_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_port: The operator to apply to the field snmp_port. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_port: The SNMP port of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_port: If op_snmp_port is specified, the field named in this input will be compared to the value in snmp_port using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_port must be specified if op_snmp_port is specified.
             :type val_f_snmp_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_port: If op_snmp_port is specified, this value will be compared to the value in snmp_port using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_port must be specified if op_snmp_port is specified.
             :type val_c_snmp_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_privacy_password: The operator to apply to the field snmp_privacy_password. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_privacy_password: The SNMP privacy password of the device (SNMPv3 only). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_privacy_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_privacy_password: If op_snmp_privacy_password is specified, the field named in this input will be compared to the value in snmp_privacy_password using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_privacy_password must be specified if op_snmp_privacy_password is specified.
             :type val_f_snmp_privacy_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_privacy_password: If op_snmp_privacy_password is specified, this value will be compared to the value in snmp_privacy_password using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_privacy_password must be specified if op_snmp_privacy_password is specified.
             :type val_c_snmp_privacy_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_privacy_protocol: The operator to apply to the field snmp_privacy_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_privacy_protocol: The SNMP privacy protocol of the device (SNMPv3 only). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_privacy_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_privacy_protocol: If op_snmp_privacy_protocol is specified, the field named in this input will be compared to the value in snmp_privacy_protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_privacy_protocol must be specified if op_snmp_privacy_protocol is specified.
             :type val_f_snmp_privacy_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_privacy_protocol: If op_snmp_privacy_protocol is specified, this value will be compared to the value in snmp_privacy_protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_privacy_protocol must be specified if op_snmp_privacy_protocol is specified.
             :type val_c_snmp_privacy_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_version: The operator to apply to the field snmp_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_version: The SNMP version of the device (SNMPv1, SNMPv2, or SNMPv3). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_version: If op_snmp_version is specified, the field named in this input will be compared to the value in snmp_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_version must be specified if op_snmp_version is specified.
             :type val_f_snmp_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_version: If op_snmp_version is specified, this value will be compared to the value in snmp_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_version must be specified if op_snmp_version is specified.
             :type val_c_snmp_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The overall status of the device support request worksheet. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_status: If op_status is specified, the field named in this input will be compared to the value in status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_status must be specified if op_status is specified.
             :type val_f_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_status: If op_status is specified, this value will be compared to the value in status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_status must be specified if op_status is specified.
             :type val_c_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status_msg: The operator to apply to the field status_msg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status_msg: Error message associated with worksheet status. Currently, only contain error messages for "Transfer Failed" status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_status_msg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_status_msg: If op_status_msg is specified, the field named in this input will be compared to the value in status_msg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_status_msg must be specified if op_status_msg is specified.
             :type val_f_status_msg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_status_msg: If op_status_msg is specified, this value will be compared to the value in status_msg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_status_msg must be specified if op_status_msg is specified.
             :type val_c_status_msg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_step_number: The operator to apply to the field step_number. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. step_number: The last step which the worksheet was saved at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_step_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_step_number: If op_step_number is specified, the field named in this input will be compared to the value in step_number using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_step_number must be specified if op_step_number is specified.
             :type val_f_step_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_step_number: If op_step_number is specified, this value will be compared to the value in step_number using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_step_number must be specified if op_step_number is specified.
             :type val_c_step_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_syslogs_collected_ind: The operator to apply to the field syslogs_collected_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. syslogs_collected_ind: Flag indicating that the syslogs were collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_syslogs_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_syslogs_collected_ind: If op_syslogs_collected_ind is specified, the field named in this input will be compared to the value in syslogs_collected_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_syslogs_collected_ind must be specified if op_syslogs_collected_ind is specified.
             :type val_f_syslogs_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_syslogs_collected_ind: If op_syslogs_collected_ind is specified, this value will be compared to the value in syslogs_collected_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_syslogs_collected_ind must be specified if op_syslogs_collected_ind is specified.
             :type val_c_syslogs_collected_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_unit_id: The operator to apply to the field unit_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. unit_id: The internal identifier for the collector that is used to collect the device support data. Used in an OC only. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_unit_id: If op_unit_id is specified, the field named in this input will be compared to the value in unit_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_unit_id must be specified if op_unit_id is specified.
             :type val_f_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_unit_id: If op_unit_id is specified, this value will be compared to the value in unit_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_unit_id must be specified if op_unit_id is specified.
             :type val_c_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the record was last modified in the system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_at: If op_updated_at is specified, the field named in this input will be compared to the value in updated_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_at must be specified if op_updated_at is specified.
             :type val_f_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_at: If op_updated_at is specified, this value will be compared to the value in updated_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_at must be specified if op_updated_at is specified.
             :type val_c_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_in_device_capabilities: The operator to apply to the field user_in_device_capabilities. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_in_device_capabilities: The device capabilities as determined by the user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_in_device_capabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_in_device_capabilities: If op_user_in_device_capabilities is specified, the field named in this input will be compared to the value in user_in_device_capabilities using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_in_device_capabilities must be specified if op_user_in_device_capabilities is specified.
             :type val_f_user_in_device_capabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_in_device_capabilities: If op_user_in_device_capabilities is specified, this value will be compared to the value in user_in_device_capabilities using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_in_device_capabilities must be specified if op_user_in_device_capabilities is specified.
             :type val_c_user_in_device_capabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_in_device_model: The operator to apply to the field user_in_device_model. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_in_device_model: The device model as determined by the user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_in_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_in_device_model: If op_user_in_device_model is specified, the field named in this input will be compared to the value in user_in_device_model using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_in_device_model must be specified if op_user_in_device_model is specified.
             :type val_f_user_in_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_in_device_model: If op_user_in_device_model is specified, this value will be compared to the value in user_in_device_model using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_in_device_model must be specified if op_user_in_device_model is specified.
             :type val_c_user_in_device_model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_in_device_type: The operator to apply to the field user_in_device_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_in_device_type: The device type as determined by the user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_in_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_in_device_type: If op_user_in_device_type is specified, the field named in this input will be compared to the value in user_in_device_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_in_device_type must be specified if op_user_in_device_type is specified.
             :type val_f_user_in_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_in_device_type: If op_user_in_device_type is specified, this value will be compared to the value in user_in_device_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_in_device_type must be specified if op_user_in_device_type is specified.
             :type val_c_user_in_device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_in_device_vendor: The operator to apply to the field user_in_device_vendor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_in_device_vendor: The device vendor as determined by the user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_in_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_in_device_vendor: If op_user_in_device_vendor is specified, the field named in this input will be compared to the value in user_in_device_vendor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_in_device_vendor must be specified if op_user_in_device_vendor is specified.
             :type val_f_user_in_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_in_device_vendor: If op_user_in_device_vendor is specified, this value will be compared to the value in user_in_device_vendor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_in_device_vendor must be specified if op_user_in_device_vendor is specified.
             :type val_c_user_in_device_vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_in_os_version: The operator to apply to the field user_in_os_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_in_os_version: The os version as determined by the user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_in_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_in_os_version: If op_user_in_os_version is specified, the field named in this input will be compared to the value in user_in_os_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_in_os_version must be specified if op_user_in_os_version is specified.
             :type val_f_user_in_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_in_os_version: If op_user_in_os_version is specified, this value will be compared to the value in user_in_os_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_in_os_version must be specified if op_user_in_os_version is specified.
             :type val_c_user_in_os_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_virtual_network_id: The operator to apply to the field virtual_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. virtual_network_id: The internal identifier for the network which the device is associated to. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_virtual_network_id: If op_virtual_network_id is specified, the field named in this input will be compared to the value in virtual_network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_virtual_network_id must be specified if op_virtual_network_id is specified.
             :type val_f_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_virtual_network_id: If op_virtual_network_id is specified, this value will be compared to the value in virtual_network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_virtual_network_id must be specified if op_virtual_network_id is specified.
             :type val_c_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DeviceSupportWorksheet. Valid values are id, device_id, device_ip_dotted, netmri_version, license_id, license_type, license_expiration, device_vendor, device_model, os_version, device_type, discovery_diagnostic_collected_ind, snmp_data_collected_ind, cli_session_collected_ind, priv_mode_info, syslogs_collected_ind, admin_guide_collected_ind, access_to_device, access_to_device_other, created_at, updated_at, user_in_device_type, user_in_device_vendor, user_in_device_model, user_in_os_version, user_in_device_capabilities, snmp_version, snmp_community_string, snmp_port, snmp_auth_username, snmp_auth_password, snmp_auth_protocol, snmp_privacy_password, snmp_privacy_protocol, preferred_cli, cli_username, cli_password, secure_version, package_name, device_discovered_ind, delivery_method, unit_id, status, step_number, delivery_addl_email, manual_data_entry_ind, status_msg, virtual_network_id, contact_method, customer_name, contact_name, contact_value. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_worksheets: An array of the DeviceSupportWorksheet objects that match the specified input criteria.
             :rtype device_support_worksheets: Array of DeviceSupportWorksheet

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device support worksheet.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal system identifier of the associated device support request worksheet.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_worksheet: The device support worksheet identified by the specified id.
             :rtype device_support_worksheet: DeviceSupportWorksheet

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)
