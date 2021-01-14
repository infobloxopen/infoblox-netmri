from ..broker import Broker


class DiscoveryHintBroker(Broker):
    controller = "discovery_hints"

    def index(self, **kwargs):
        """Lists the available discovery hints. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure.
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

             :param select: The list of attributes to return for each DiscoveryHint. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure. If empty or omitted, all attributes will be returned.
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

             :return discovery_hints: An array of the DiscoveryHint objects that match the specified input criteria.
             :rtype discovery_hints: Array of DiscoveryHint

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available discovery hints matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure.
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

             :param select: The list of attributes to return for each DiscoveryHint. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against discovery hints, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: hint, device_type.
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

             :return discovery_hints: An array of the DiscoveryHint objects that match the specified input criteria.
             :rtype discovery_hints: Array of DiscoveryHint

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available discovery hints matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: UnitID, cli_enable_password_secure, cli_user_name_secure_ssh, cli_user_name_secure_telnet, cli_user_password_secure_ssh, cli_user_password_secure_telnet, created_at, created_by, device_type, hint, id, secure_version, snmp_auth_password_secure, snmp_auth_protocol, snmp_community_secure, snmp_private_password_secure, snmp_private_protocol, snmp_protocol, updated_at, updated_by.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier collector assigned to the discovery hint. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cli_enable_password_secure: The operator to apply to the field cli_enable_password_secure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_enable_password_secure: Device specific CLI enable password for all protocols. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_enable_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_enable_password_secure: If op_cli_enable_password_secure is specified, the field named in this input will be compared to the value in cli_enable_password_secure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_enable_password_secure must be specified if op_cli_enable_password_secure is specified.
             :type val_f_cli_enable_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_enable_password_secure: If op_cli_enable_password_secure is specified, this value will be compared to the value in cli_enable_password_secure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_enable_password_secure must be specified if op_cli_enable_password_secure is specified.
             :type val_c_cli_enable_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_user_name_secure_ssh: The operator to apply to the field cli_user_name_secure_ssh. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_user_name_secure_ssh: Device specific CLI username for ssh protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_user_name_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_user_name_secure_ssh: If op_cli_user_name_secure_ssh is specified, the field named in this input will be compared to the value in cli_user_name_secure_ssh using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_user_name_secure_ssh must be specified if op_cli_user_name_secure_ssh is specified.
             :type val_f_cli_user_name_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_user_name_secure_ssh: If op_cli_user_name_secure_ssh is specified, this value will be compared to the value in cli_user_name_secure_ssh using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_user_name_secure_ssh must be specified if op_cli_user_name_secure_ssh is specified.
             :type val_c_cli_user_name_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_user_name_secure_telnet: The operator to apply to the field cli_user_name_secure_telnet. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_user_name_secure_telnet: Device specific CLI username for telnet protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_user_name_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_user_name_secure_telnet: If op_cli_user_name_secure_telnet is specified, the field named in this input will be compared to the value in cli_user_name_secure_telnet using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_user_name_secure_telnet must be specified if op_cli_user_name_secure_telnet is specified.
             :type val_f_cli_user_name_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_user_name_secure_telnet: If op_cli_user_name_secure_telnet is specified, this value will be compared to the value in cli_user_name_secure_telnet using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_user_name_secure_telnet must be specified if op_cli_user_name_secure_telnet is specified.
             :type val_c_cli_user_name_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_user_password_secure_ssh: The operator to apply to the field cli_user_password_secure_ssh. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_user_password_secure_ssh: Device specific CLI password for ssh protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_user_password_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_user_password_secure_ssh: If op_cli_user_password_secure_ssh is specified, the field named in this input will be compared to the value in cli_user_password_secure_ssh using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_user_password_secure_ssh must be specified if op_cli_user_password_secure_ssh is specified.
             :type val_f_cli_user_password_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_user_password_secure_ssh: If op_cli_user_password_secure_ssh is specified, this value will be compared to the value in cli_user_password_secure_ssh using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_user_password_secure_ssh must be specified if op_cli_user_password_secure_ssh is specified.
             :type val_c_cli_user_password_secure_ssh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_user_password_secure_telnet: The operator to apply to the field cli_user_password_secure_telnet. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_user_password_secure_telnet: Device specific CLI password for telnet protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_user_password_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_user_password_secure_telnet: If op_cli_user_password_secure_telnet is specified, the field named in this input will be compared to the value in cli_user_password_secure_telnet using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_user_password_secure_telnet must be specified if op_cli_user_password_secure_telnet is specified.
             :type val_f_cli_user_password_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_user_password_secure_telnet: If op_cli_user_password_secure_telnet is specified, this value will be compared to the value in cli_user_password_secure_telnet using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_user_password_secure_telnet must be specified if op_cli_user_password_secure_telnet is specified.
             :type val_c_cli_user_password_secure_telnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the hint was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: The user that initially created the discovery hint. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_by: If op_created_by is specified, the field named in this input will be compared to the value in created_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_by must be specified if op_created_by is specified.
             :type val_f_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_by: If op_created_by is specified, this value will be compared to the value in created_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_by must be specified if op_created_by is specified.
             :type val_c_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_type: The operator to apply to the field device_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_type: The device type applied to the given discovery hint. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_hint: The operator to apply to the field hint. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. hint: The hint used the by discovery engine. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_hint: If op_hint is specified, the field named in this input will be compared to the value in hint using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_hint must be specified if op_hint is specified.
             :type val_f_hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_hint: If op_hint is specified, this value will be compared to the value in hint using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_hint must be specified if op_hint is specified.
             :type val_c_hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the discovery hint. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_secure_version: The operator to apply to the field secure_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. secure_version: The encryption version of the username and passwords. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_snmp_auth_password_secure: The operator to apply to the field snmp_auth_password_secure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_auth_password_secure: The SNMPv3 authentication protocol password For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_auth_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_auth_password_secure: If op_snmp_auth_password_secure is specified, the field named in this input will be compared to the value in snmp_auth_password_secure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_auth_password_secure must be specified if op_snmp_auth_password_secure is specified.
             :type val_f_snmp_auth_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_auth_password_secure: If op_snmp_auth_password_secure is specified, this value will be compared to the value in snmp_auth_password_secure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_auth_password_secure must be specified if op_snmp_auth_password_secure is specified.
             :type val_c_snmp_auth_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_auth_protocol: The operator to apply to the field snmp_auth_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_auth_protocol: The SNMPv3 authentication protocol to use with this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_snmp_community_secure: The operator to apply to the field snmp_community_secure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_community_secure: The SNMP community string. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_community_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_community_secure: If op_snmp_community_secure is specified, the field named in this input will be compared to the value in snmp_community_secure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_community_secure must be specified if op_snmp_community_secure is specified.
             :type val_f_snmp_community_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_community_secure: If op_snmp_community_secure is specified, this value will be compared to the value in snmp_community_secure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_community_secure must be specified if op_snmp_community_secure is specified.
             :type val_c_snmp_community_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_private_password_secure: The operator to apply to the field snmp_private_password_secure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_private_password_secure: The SNMPv3 privacy protocol password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_private_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_private_password_secure: If op_snmp_private_password_secure is specified, the field named in this input will be compared to the value in snmp_private_password_secure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_private_password_secure must be specified if op_snmp_private_password_secure is specified.
             :type val_f_snmp_private_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_private_password_secure: If op_snmp_private_password_secure is specified, this value will be compared to the value in snmp_private_password_secure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_private_password_secure must be specified if op_snmp_private_password_secure is specified.
             :type val_c_snmp_private_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_private_protocol: The operator to apply to the field snmp_private_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_private_protocol: The SNMPv3 privacy protocol to use with this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_private_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_private_protocol: If op_snmp_private_protocol is specified, the field named in this input will be compared to the value in snmp_private_protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_private_protocol must be specified if op_snmp_private_protocol is specified.
             :type val_f_snmp_private_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_private_protocol: If op_snmp_private_protocol is specified, this value will be compared to the value in snmp_private_protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_private_protocol must be specified if op_snmp_private_protocol is specified.
             :type val_c_snmp_private_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_snmp_protocol: The operator to apply to the field snmp_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. snmp_protocol: The SNMP protocol for which to use these credentials. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_snmp_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_snmp_protocol: If op_snmp_protocol is specified, the field named in this input will be compared to the value in snmp_protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_snmp_protocol must be specified if op_snmp_protocol is specified.
             :type val_f_snmp_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_snmp_protocol: If op_snmp_protocol is specified, this value will be compared to the value in snmp_protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_snmp_protocol must be specified if op_snmp_protocol is specified.
             :type val_c_snmp_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the hint was last modified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_by: The operator to apply to the field updated_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_by: The user that last updated the discovery hint. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_by: If op_updated_by is specified, the field named in this input will be compared to the value in updated_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_by must be specified if op_updated_by is specified.
             :type val_f_updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_by: If op_updated_by is specified, this value will be compared to the value in updated_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_by must be specified if op_updated_by is specified.
             :type val_c_updated_by: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure.
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

             :param select: The list of attributes to return for each DiscoveryHint. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure. If empty or omitted, all attributes will be returned.
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

             :return discovery_hints: An array of the DiscoveryHint objects that match the specified input criteria.
             :rtype discovery_hints: Array of DiscoveryHint

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The discovery hint identified by the specified id.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Creates a new discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param hint: The hint used the by discovery engine.
             :type hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_type: The device type applied to the given discovery hint.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created discovery hint.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created discovery hint.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created discovery hint.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The newly created discovery hint.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param hint: The hint used the by discovery engine. If omitted, this field will not be updated.
             :type hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_type: The device type applied to the given discovery hint. If omitted, this field will not be updated.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint. If omitted, this field will be updated to the default value.
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated discovery hint.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated discovery hint.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated discovery hint.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The updated discovery hint.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified discovery hint from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def destroy_many(self, **kwargs):
        """Remove several discovery hints

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ids: The IDs array of the discovery hints to delete.  When sending form encoded use ids[].
             :type ids: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy_many"), kwargs)
