from ..broker import Broker


class SdnSettingBroker(Broker):
    controller = "sdn_settings"

    def index(self, **kwargs):
        """Lists the available sdn settings. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content.
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

             :param select: The list of attributes to return for each SdnSetting. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content. If empty or omitted, all attributes will be returned.
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

             :return sdn_settings: An array of the SdnSetting objects that match the specified input criteria.
             :rtype sdn_settings: Array of SdnSetting

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available sdn settings matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: Internal version of the encryption method
             :type SecureVersion: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for collector assigned to the SDN Setting
             :type UnitID: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param api_key: API key to access the SDN controller (MERAKI)
             :type api_key: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param blackout_duration: The blackout duration in minutes.
             :type blackout_duration: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_content: Content of custom CA certificate.
             :type ca_cert_content: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_id: ID of custom CA certificate.
             :type ca_cert_id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param collect_offline_devices: Collect Devices In Offline Status
             :type collect_offline_devices: Array of Boolean

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param controller_address: Controller IP address or hostname.
             :type controller_address: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time when the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param handle: Unique handle for single configuration
             :type handle: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting.
             :type id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param max_requests_per_second: Maximum Requests per Second.
             :type max_requests_per_second: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param on_prem: True if controller is on premises. Otherwise we consider it is in cloud.
             :type on_prem: Array of Boolean

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param protocol: Protocol used to communicate with controller.
             :type protocol: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param scan_interface_id: ID of scan interface which used for controller connection
             :type scan_interface_id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_password: Password used to connect SDN controller.
             :type sdn_password: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_type: Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA
             :type sdn_type: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_username: Username used to connect SDN controller.
             :type sdn_username: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_blackout_schedule: The blackout start time in cron format.
             :type start_blackout_schedule: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time when the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param use_global_proxy: Use global proxy settings to access SDN controller.
             :type use_global_proxy: Array of Boolean

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the Virtual Network on which this controller is defined.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content.
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

             :param select: The list of attributes to return for each SdnSetting. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against sdn settings, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: SecureVersion, UnitID, api_key, blackout_duration, ca_cert_content, ca_cert_id, collect_offline_devices, controller_address, created_at, handle, id, max_requests_per_second, on_prem, protocol, scan_interface_id, sdn_password, sdn_type, sdn_username, start_blackout_schedule, updated_at, use_global_proxy, virtual_network_id.
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

             :return sdn_settings: An array of the SdnSetting objects that match the specified input criteria.
             :rtype sdn_settings: Array of SdnSetting

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available sdn settings matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: SecureVersion, UnitID, api_key, blackout_duration, ca_cert_content, ca_cert_id, collect_offline_devices, controller_address, created_at, handle, id, max_requests_per_second, on_prem, protocol, scan_interface_id, sdn_password, sdn_type, sdn_username, start_blackout_schedule, updated_at, use_global_proxy, virtual_network_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SecureVersion: The operator to apply to the field SecureVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SecureVersion: Internal version of the encryption method For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SecureVersion: If op_SecureVersion is specified, the field named in this input will be compared to the value in SecureVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_f_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SecureVersion: If op_SecureVersion is specified, this value will be compared to the value in SecureVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_c_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier for collector assigned to the SDN Setting For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UnitID: If op_UnitID is specified, the field named in this input will be compared to the value in UnitID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UnitID must be specified if op_UnitID is specified.
             :type val_f_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UnitID: If op_UnitID is specified, this value will be compared to the value in UnitID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UnitID must be specified if op_UnitID is specified.
             :type val_c_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_api_key: The operator to apply to the field api_key. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. api_key: API key to access the SDN controller (MERAKI) For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_api_key: If op_api_key is specified, the field named in this input will be compared to the value in api_key using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_api_key must be specified if op_api_key is specified.
             :type val_f_api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_api_key: If op_api_key is specified, this value will be compared to the value in api_key using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_api_key must be specified if op_api_key is specified.
             :type val_c_api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_blackout_duration: The operator to apply to the field blackout_duration. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. blackout_duration: The blackout duration in minutes. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_blackout_duration: If op_blackout_duration is specified, the field named in this input will be compared to the value in blackout_duration using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_blackout_duration must be specified if op_blackout_duration is specified.
             :type val_f_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_blackout_duration: If op_blackout_duration is specified, this value will be compared to the value in blackout_duration using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_blackout_duration must be specified if op_blackout_duration is specified.
             :type val_c_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ca_cert_content: The operator to apply to the field ca_cert_content. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ca_cert_content: Content of custom CA certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ca_cert_content: If op_ca_cert_content is specified, the field named in this input will be compared to the value in ca_cert_content using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ca_cert_content must be specified if op_ca_cert_content is specified.
             :type val_f_ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ca_cert_content: If op_ca_cert_content is specified, this value will be compared to the value in ca_cert_content using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ca_cert_content must be specified if op_ca_cert_content is specified.
             :type val_c_ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ca_cert_id: The operator to apply to the field ca_cert_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ca_cert_id: ID of custom CA certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ca_cert_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ca_cert_id: If op_ca_cert_id is specified, the field named in this input will be compared to the value in ca_cert_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ca_cert_id must be specified if op_ca_cert_id is specified.
             :type val_f_ca_cert_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ca_cert_id: If op_ca_cert_id is specified, this value will be compared to the value in ca_cert_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ca_cert_id must be specified if op_ca_cert_id is specified.
             :type val_c_ca_cert_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_collect_offline_devices: The operator to apply to the field collect_offline_devices. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. collect_offline_devices: Collect Devices In Offline Status For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_collect_offline_devices: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_collect_offline_devices: If op_collect_offline_devices is specified, the field named in this input will be compared to the value in collect_offline_devices using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_collect_offline_devices must be specified if op_collect_offline_devices is specified.
             :type val_f_collect_offline_devices: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_collect_offline_devices: If op_collect_offline_devices is specified, this value will be compared to the value in collect_offline_devices using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_collect_offline_devices must be specified if op_collect_offline_devices is specified.
             :type val_c_collect_offline_devices: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_controller_address: The operator to apply to the field controller_address. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. controller_address: Controller IP address or hostname. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_controller_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_controller_address: If op_controller_address is specified, the field named in this input will be compared to the value in controller_address using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_controller_address must be specified if op_controller_address is specified.
             :type val_f_controller_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_controller_address: If op_controller_address is specified, this value will be compared to the value in controller_address using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_controller_address must be specified if op_controller_address is specified.
             :type val_c_controller_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time when the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_handle: The operator to apply to the field handle. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. handle: Unique handle for single configuration For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_handle: If op_handle is specified, the field named in this input will be compared to the value in handle using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_handle must be specified if op_handle is specified.
             :type val_f_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_handle: If op_handle is specified, this value will be compared to the value in handle using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_handle must be specified if op_handle is specified.
             :type val_c_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_max_requests_per_second: The operator to apply to the field max_requests_per_second. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. max_requests_per_second: Maximum Requests per Second. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_max_requests_per_second: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_max_requests_per_second: If op_max_requests_per_second is specified, the field named in this input will be compared to the value in max_requests_per_second using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_max_requests_per_second must be specified if op_max_requests_per_second is specified.
             :type val_f_max_requests_per_second: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_max_requests_per_second: If op_max_requests_per_second is specified, this value will be compared to the value in max_requests_per_second using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_max_requests_per_second must be specified if op_max_requests_per_second is specified.
             :type val_c_max_requests_per_second: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_on_prem: The operator to apply to the field on_prem. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. on_prem: True if controller is on premises. Otherwise we consider it is in cloud. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_on_prem: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_on_prem: If op_on_prem is specified, the field named in this input will be compared to the value in on_prem using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_on_prem must be specified if op_on_prem is specified.
             :type val_f_on_prem: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_on_prem: If op_on_prem is specified, this value will be compared to the value in on_prem using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_on_prem must be specified if op_on_prem is specified.
             :type val_c_on_prem: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_protocol: The operator to apply to the field protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. protocol: Protocol used to communicate with controller. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_protocol: If op_protocol is specified, the field named in this input will be compared to the value in protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_protocol must be specified if op_protocol is specified.
             :type val_f_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_protocol: If op_protocol is specified, this value will be compared to the value in protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_protocol must be specified if op_protocol is specified.
             :type val_c_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_scan_interface_id: The operator to apply to the field scan_interface_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. scan_interface_id: ID of scan interface which used for controller connection For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_scan_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_scan_interface_id: If op_scan_interface_id is specified, the field named in this input will be compared to the value in scan_interface_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_scan_interface_id must be specified if op_scan_interface_id is specified.
             :type val_f_scan_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_scan_interface_id: If op_scan_interface_id is specified, this value will be compared to the value in scan_interface_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_scan_interface_id must be specified if op_scan_interface_id is specified.
             :type val_c_scan_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_password: The operator to apply to the field sdn_password. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_password: Password used to connect SDN controller. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_password: If op_sdn_password is specified, the field named in this input will be compared to the value in sdn_password using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_password must be specified if op_sdn_password is specified.
             :type val_f_sdn_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_password: If op_sdn_password is specified, this value will be compared to the value in sdn_password using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_password must be specified if op_sdn_password is specified.
             :type val_c_sdn_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_type: The operator to apply to the field sdn_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_type: Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_type: If op_sdn_type is specified, the field named in this input will be compared to the value in sdn_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_type must be specified if op_sdn_type is specified.
             :type val_f_sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_type: If op_sdn_type is specified, this value will be compared to the value in sdn_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_type must be specified if op_sdn_type is specified.
             :type val_c_sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_username: The operator to apply to the field sdn_username. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_username: Username used to connect SDN controller. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_username: If op_sdn_username is specified, the field named in this input will be compared to the value in sdn_username using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_username must be specified if op_sdn_username is specified.
             :type val_f_sdn_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_username: If op_sdn_username is specified, this value will be compared to the value in sdn_username using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_username must be specified if op_sdn_username is specified.
             :type val_c_sdn_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_start_blackout_schedule: The operator to apply to the field start_blackout_schedule. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. start_blackout_schedule: The blackout start time in cron format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_start_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_start_blackout_schedule: If op_start_blackout_schedule is specified, the field named in this input will be compared to the value in start_blackout_schedule using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_start_blackout_schedule must be specified if op_start_blackout_schedule is specified.
             :type val_f_start_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_start_blackout_schedule: If op_start_blackout_schedule is specified, this value will be compared to the value in start_blackout_schedule using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_start_blackout_schedule must be specified if op_start_blackout_schedule is specified.
             :type val_c_start_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time when the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_use_global_proxy: The operator to apply to the field use_global_proxy. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. use_global_proxy: Use global proxy settings to access SDN controller. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_use_global_proxy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_use_global_proxy: If op_use_global_proxy is specified, the field named in this input will be compared to the value in use_global_proxy using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_use_global_proxy must be specified if op_use_global_proxy is specified.
             :type val_f_use_global_proxy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_use_global_proxy: If op_use_global_proxy is specified, this value will be compared to the value in use_global_proxy using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_use_global_proxy must be specified if op_use_global_proxy is specified.
             :type val_c_use_global_proxy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_virtual_network_id: The operator to apply to the field virtual_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. virtual_network_id: The internal NetMRI identifier of the Virtual Network on which this controller is defined. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content.
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

             :param select: The list of attributes to return for each SdnSetting. Valid values are id, virtual_network_id, controller_address, protocol, sdn_username, sdn_password, SecureVersion, created_at, updated_at, UnitID, sdn_type, api_key, on_prem, use_global_proxy, handle, scan_interface_id, start_blackout_schedule, blackout_duration, max_requests_per_second, collect_offline_devices, ca_cert_id, ca_cert_content. If empty or omitted, all attributes will be returned.
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

             :return sdn_settings: An array of the SdnSetting objects that match the specified input criteria.
             :rtype sdn_settings: Array of SdnSetting

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified sdn setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_setting: The sdn setting identified by the specified id.
             :rtype sdn_setting: SdnSetting

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Creates a new sdn setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param SecureVersion: Internal version of the encryption method
             :type SecureVersion: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier for collector assigned to the SDN Setting
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param api_key: API key to access the SDN controller (MERAKI)
             :type api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param blackout_duration: The blackout duration in minutes.
             :type blackout_duration: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_content: Content of custom CA certificate.
             :type ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_id: ID of custom CA certificate.
             :type ca_cert_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param collect_offline_devices: Collect Devices In Offline Status
             :type collect_offline_devices: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param controller_address: Controller IP address or hostname.
             :type controller_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param handle: Unique handle for single configuration
             :type handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param max_requests_per_second: Maximum Requests per Second.
             :type max_requests_per_second: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param on_prem: True if controller is on premises. Otherwise we consider it is in cloud.
             :type on_prem: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param protocol: Protocol used to communicate with controller.
             :type protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param scan_interface_id: ID of scan interface which used for controller connection
             :type scan_interface_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_password: Password used to connect SDN controller.
             :type sdn_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param sdn_type: Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA
             :type sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_username: Username used to connect SDN controller.
             :type sdn_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param start_blackout_schedule: The blackout start time in cron format.
             :type start_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param use_global_proxy: Use global proxy settings to access SDN controller.
             :type use_global_proxy: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the Virtual Network on which this controller is defined.
             :type virtual_network_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created sdn setting.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created sdn setting.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created sdn setting.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_setting: The newly created sdn setting.
             :rtype sdn_setting: SdnSetting

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing sdn setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param SecureVersion: Internal version of the encryption method If omitted, this field will be updated to the default value.
             :type SecureVersion: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier for collector assigned to the SDN Setting If omitted, this field will be updated to the default value.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param api_key: API key to access the SDN controller (MERAKI) If omitted, this field will not be updated.
             :type api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param blackout_duration: The blackout duration in minutes. If omitted, this field will be updated to the default value.
             :type blackout_duration: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_content: Content of custom CA certificate. If omitted, this field will not be updated.
             :type ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_id: ID of custom CA certificate. If omitted, this field will not be updated.
             :type ca_cert_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param collect_offline_devices: Collect Devices In Offline Status If omitted, this field will be updated to the default value.
             :type collect_offline_devices: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param controller_address: Controller IP address or hostname. If omitted, this field will not be updated.
             :type controller_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param handle: Unique handle for single configuration If omitted, this field will not be updated.
             :type handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param max_requests_per_second: Maximum Requests per Second. If omitted, this field will be updated to the default value.
             :type max_requests_per_second: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param on_prem: True if controller is on premises. Otherwise we consider it is in cloud. If omitted, this field will not be updated.
             :type on_prem: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param protocol: Protocol used to communicate with controller. If omitted, this field will not be updated.
             :type protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param scan_interface_id: ID of scan interface which used for controller connection If omitted, this field will not be updated.
             :type scan_interface_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_password: Password used to connect SDN controller. If omitted, this field will not be updated.
             :type sdn_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_type: Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA If omitted, this field will not be updated.
             :type sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_username: Username used to connect SDN controller. If omitted, this field will not be updated.
             :type sdn_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param start_blackout_schedule: The blackout start time in cron format. If omitted, this field will be updated to the default value.
             :type start_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param use_global_proxy: Use global proxy settings to access SDN controller. If omitted, this field will not be updated.
             :type use_global_proxy: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the Virtual Network on which this controller is defined. If omitted, this field will not be updated.
             :type virtual_network_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated sdn setting.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated sdn setting.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated sdn setting.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_setting: The updated sdn setting.
             :rtype sdn_setting: SdnSetting

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified sdn setting from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def destroy_many(self, **kwargs):
        """Remove several configurations of SDN Controllers

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ids: The IDs array of the configurations.  When sending form encoded use ids[].
             :type ids: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy_many"), kwargs)

    def dump_sdn_controllers(self, **kwargs):
        """List all SDN Controllers

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` controller_address

             :param sort: The data field to use for sorting the output. Default is controller_address.
             :type sort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The UnitID of the collector
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against attribute "controller_address" and "VirtualNetworkName". Any SdnSetting objects with the passed value contained within one or more of those attributes will be returned.
             :type query: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19.
             :type limit: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("dump_sdn_controllers"), kwargs)

    def import_controllers(self, **kwargs):
        """Imports a list of discovery settings into the database

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file: The contents of the CSV file with the list of discovery settings to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The UnitID of the collector
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import_controllers"), kwargs)

    def check_credentials(self, **kwargs):
        """Performs connection to SDN/SDWAN controller, checks credentials and returns results or status id based on async_ind

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: ID of the collector to send the request to, OC only
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param sdn_type: Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA
             :type sdn_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param address: Comma-separated list of controller's IP Addresses/FQDNs
             :type address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: Username used to connect SDN controller
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: Password used to connect SDN controller
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param api_key: API key to access the SDN controller
             :type api_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` HTTP

             :param protocol: Protocol used to communicate with controller (HTTP or HTTPS)
             :type protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param use_global_proxy: Use global proxy settings to access SDN controller
             :type use_global_proxy: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ca_cert_content: CA certificate content to connect using HTTPS
             :type ca_cert_content: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param network_interface: Name of physical network interface which used for controller connection
             :type network_interface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: Virtual Network ID assigned for SDN controller discovery
             :type virtual_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_address: Address of the proxy server
             :type proxy_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 80

             :param proxy_port: Port number the proxy listens on
             :type proxy_port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_username: Proxy username
             :type proxy_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_password: Proxy password
             :type proxy_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param async_ind: When false, the credential check will be run synchronously, and the API call will block until it is complete. When true, credential check id will be returned to use for subsequent calls
             :type async_ind: Boolean

            |  ``api version min:`` 3.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param start_blackout_schedule: Blackout schedule
             :type start_blackout_schedule: String

            |  ``api version min:`` 3.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param blackout_duration: Blackout duration
             :type blackout_duration: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return text: When async_ind is false, credential check text will be returned upon completion.
             :rtype text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The internal identifier for previously initiated credential check.
             :rtype id: String

            """

        return self.api_request(self._get_method_fullname("check_credentials"), kwargs)

    def check_credentials_status(self, **kwargs):
        """Status of SDN/SDWAN controller credentials check

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: SDN credential check id needed to retrieve status
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param start: The starting index(inclusive) of the returned text of the SDN credential check
             :type start: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return text: Credential check result
             :rtype text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return start: The starting index(inclusive) of the returned text of the SDN credential check
             :rtype start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return end: The ending index (exclusive) of the returned text of the SDN credential check
             :rtype end: Integer

            """

        return self.api_request(self._get_method_fullname("check_credentials_status"), kwargs)
