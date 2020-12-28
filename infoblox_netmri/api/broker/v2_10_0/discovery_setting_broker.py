from ..broker import Broker


class DiscoverySettingBroker(Broker):
    controller = "discovery_settings"

    def index(self, **kwargs):
        """Lists the available discovery settings. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery setting.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery setting.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery setting.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery setting.
             :type UnitID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD).
             :type range_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD).
             :type range_type: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count.
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

             :param select: The list of attributes to return for each DiscoverySetting. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count. If empty or omitted, all attributes will be returned.
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

             :return discovery_settings: An array of the DiscoverySetting objects that match the specified input criteria.
             :rtype discovery_settings: Array of DiscoverySetting

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available discovery settings matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD).
             :type range_type: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery setting.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count.
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

             :param select: The list of attributes to return for each DiscoverySetting. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against discovery settings, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: range_value, range_type, {"ping_sweep_ind"=>{1=>"Enable", 0=>"Disable"}}, {"discovery_status"=>{"INCLUDE"=>"Include in discovery", "EXCLUDE"=>"Exclude from discovery", "IGNORE"=>"Exclude from management"}}, VirtualNetworkName.
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

             :return discovery_settings: An array of the DiscoverySetting objects that match the specified input criteria.
             :rtype discovery_settings: Array of DiscoverySetting

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available discovery settings matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: UnitID, blackout_duration, cidr_count, created_at, created_by, discovery_status, id, ping_sweep_ind, port_control_blackout_duration, range_end, range_end_numeric, range_mask, range_start, range_start_numeric, range_type, range_value, smart_ping_sweep_ind, start_blackout_schedule, start_port_control_blackout_schedule, updated_at, updated_by, virtual_network_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier collector assigned to the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cidr_count: The operator to apply to the field cidr_count. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cidr_count: Number of CIDRs in discovery range. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cidr_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cidr_count: If op_cidr_count is specified, the field named in this input will be compared to the value in cidr_count using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cidr_count must be specified if op_cidr_count is specified.
             :type val_f_cidr_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cidr_count: If op_cidr_count is specified, this value will be compared to the value in cidr_count using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cidr_count must be specified if op_cidr_count is specified.
             :type val_c_cidr_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the discovery setting was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: The user that created the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_discovery_status: The operator to apply to the field discovery_status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. discovery_status: The discovery mode of the discovery setting (INCLUDE, EXCLUDE, IGNORE). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_discovery_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_discovery_status: If op_discovery_status is specified, the field named in this input will be compared to the value in discovery_status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_discovery_status must be specified if op_discovery_status is specified.
             :type val_f_discovery_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_discovery_status: If op_discovery_status is specified, this value will be compared to the value in discovery_status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_discovery_status must be specified if op_discovery_status is specified.
             :type val_c_discovery_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ping_sweep_ind: The operator to apply to the field ping_sweep_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ping_sweep_ind: A flag indicating if ping sweeps are used on the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ping_sweep_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ping_sweep_ind: If op_ping_sweep_ind is specified, the field named in this input will be compared to the value in ping_sweep_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ping_sweep_ind must be specified if op_ping_sweep_ind is specified.
             :type val_f_ping_sweep_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ping_sweep_ind: If op_ping_sweep_ind is specified, this value will be compared to the value in ping_sweep_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ping_sweep_ind must be specified if op_ping_sweep_ind is specified.
             :type val_c_ping_sweep_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_port_control_blackout_duration: The operator to apply to the field port_control_blackout_duration. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. port_control_blackout_duration: Port Control Blackout duration in minutes For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_port_control_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_port_control_blackout_duration: If op_port_control_blackout_duration is specified, the field named in this input will be compared to the value in port_control_blackout_duration using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_port_control_blackout_duration must be specified if op_port_control_blackout_duration is specified.
             :type val_f_port_control_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_port_control_blackout_duration: If op_port_control_blackout_duration is specified, this value will be compared to the value in port_control_blackout_duration using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_port_control_blackout_duration must be specified if op_port_control_blackout_duration is specified.
             :type val_c_port_control_blackout_duration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_end: The operator to apply to the field range_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_end: The ending IP address for the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_end: If op_range_end is specified, the field named in this input will be compared to the value in range_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_end must be specified if op_range_end is specified.
             :type val_f_range_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_end: If op_range_end is specified, this value will be compared to the value in range_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_end must be specified if op_range_end is specified.
             :type val_c_range_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_end_numeric: The operator to apply to the field range_end_numeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_end_numeric: The ending IP address numeric value for the discovery setting.ange_end_numeric. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_end_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_end_numeric: If op_range_end_numeric is specified, the field named in this input will be compared to the value in range_end_numeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_end_numeric must be specified if op_range_end_numeric is specified.
             :type val_f_range_end_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_end_numeric: If op_range_end_numeric is specified, this value will be compared to the value in range_end_numeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_end_numeric must be specified if op_range_end_numeric is specified.
             :type val_c_range_end_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_mask: The operator to apply to the field range_mask. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_mask: The CIDR mask for the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_mask: If op_range_mask is specified, the field named in this input will be compared to the value in range_mask using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_mask must be specified if op_range_mask is specified.
             :type val_f_range_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_mask: If op_range_mask is specified, this value will be compared to the value in range_mask using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_mask must be specified if op_range_mask is specified.
             :type val_c_range_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_start: The operator to apply to the field range_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_start: The starting IP address for the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_start: If op_range_start is specified, the field named in this input will be compared to the value in range_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_start must be specified if op_range_start is specified.
             :type val_f_range_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_start: If op_range_start is specified, this value will be compared to the value in range_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_start must be specified if op_range_start is specified.
             :type val_c_range_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_start_numeric: The operator to apply to the field range_start_numeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_start_numeric: The starting IP address numeric value for the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_start_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_start_numeric: If op_range_start_numeric is specified, the field named in this input will be compared to the value in range_start_numeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_start_numeric must be specified if op_range_start_numeric is specified.
             :type val_f_range_start_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_start_numeric: If op_range_start_numeric is specified, this value will be compared to the value in range_start_numeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_start_numeric must be specified if op_range_start_numeric is specified.
             :type val_c_range_start_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_type: The operator to apply to the field range_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_type: If op_range_type is specified, the field named in this input will be compared to the value in range_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_type must be specified if op_range_type is specified.
             :type val_f_range_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_type: If op_range_type is specified, this value will be compared to the value in range_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_type must be specified if op_range_type is specified.
             :type val_c_range_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_range_value: The operator to apply to the field range_value. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. range_value: The discovery setting value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_range_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_range_value: If op_range_value is specified, the field named in this input will be compared to the value in range_value using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_range_value must be specified if op_range_value is specified.
             :type val_f_range_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_range_value: If op_range_value is specified, this value will be compared to the value in range_value using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_range_value must be specified if op_range_value is specified.
             :type val_c_range_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_smart_ping_sweep_ind: The operator to apply to the field smart_ping_sweep_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. smart_ping_sweep_ind: A flag indicating if smart ping sweep should be used on the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_smart_ping_sweep_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_smart_ping_sweep_ind: If op_smart_ping_sweep_ind is specified, the field named in this input will be compared to the value in smart_ping_sweep_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_smart_ping_sweep_ind must be specified if op_smart_ping_sweep_ind is specified.
             :type val_f_smart_ping_sweep_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_smart_ping_sweep_ind: If op_smart_ping_sweep_ind is specified, this value will be compared to the value in smart_ping_sweep_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_smart_ping_sweep_ind must be specified if op_smart_ping_sweep_ind is specified.
             :type val_c_smart_ping_sweep_ind: String

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

             :param op_start_port_control_blackout_schedule: The operator to apply to the field start_port_control_blackout_schedule. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. start_port_control_blackout_schedule: Port Control Blackout schedule in CRON format For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_start_port_control_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_start_port_control_blackout_schedule: If op_start_port_control_blackout_schedule is specified, the field named in this input will be compared to the value in start_port_control_blackout_schedule using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_start_port_control_blackout_schedule must be specified if op_start_port_control_blackout_schedule is specified.
             :type val_f_start_port_control_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_start_port_control_blackout_schedule: If op_start_port_control_blackout_schedule is specified, this value will be compared to the value in start_port_control_blackout_schedule using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_start_port_control_blackout_schedule must be specified if op_start_port_control_blackout_schedule is specified.
             :type val_c_start_port_control_blackout_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the discovery setting was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_by: The operator to apply to the field updated_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_by: The user that last updated the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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
            |  ``default:`` None

             :param op_virtual_network_id: The operator to apply to the field virtual_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. virtual_network_id: A Virtual Network identifier assigned to the discovery setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count.
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

             :param select: The list of attributes to return for each DiscoverySetting. Valid values are id, range_value, range_start, range_end, range_start_numeric, range_end_numeric, range_mask, range_type, discovery_status, created_at, updated_at, UnitID, created_by, updated_by, ping_sweep_ind, smart_ping_sweep_ind, start_blackout_schedule, blackout_duration, virtual_network_id, start_port_control_blackout_schedule, port_control_blackout_duration, cidr_count. If empty or omitted, all attributes will be returned.
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

             :return discovery_settings: An array of the DiscoverySetting objects that match the specified input criteria.
             :rtype discovery_settings: Array of DiscoverySetting

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified discovery setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery setting.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_setting: The discovery setting identified by the specified id.
             :rtype discovery_setting: DiscoverySetting

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Creates a new discovery setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param range_value: The discovery setting value.
             :type range_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD).
             :type range_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param discovery_status: The discovery mode of the discovery setting (INCLUDE, EXCLUDE, IGNORE).
             :type discovery_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery setting.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param ping_sweep_ind: A flag indicating if ping sweeps are used on the discovery setting.
             :type ping_sweep_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param virtual_network_id: A Virtual Network identifier assigned to the discovery setting.
             :type virtual_network_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created discovery setting.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created discovery setting.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created discovery setting.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_setting: The newly created discovery setting.
             :rtype discovery_setting: DiscoverySetting

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing discovery setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery setting.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param range_value: The discovery setting value. If omitted, this field will not be updated.
             :type range_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param range_type: The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD). If omitted, this field will not be updated.
             :type range_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param discovery_status: The discovery mode of the discovery setting (INCLUDE, EXCLUDE, IGNORE). If omitted, this field will not be updated.
             :type discovery_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery setting. If omitted, this field will be updated to the default value.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param ping_sweep_ind: A flag indicating if ping sweeps are used on the discovery setting. If omitted, this field will be updated to the default value.
             :type ping_sweep_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param virtual_network_id: A Virtual Network identifier assigned to the discovery setting. If omitted, this field will be updated to the default value.
             :type virtual_network_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated discovery setting.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated discovery setting.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated discovery setting.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_setting: The updated discovery setting.
             :rtype discovery_setting: DiscoverySetting

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified discovery setting from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery setting.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def destroy_many(self, **kwargs):
        """Remove several discovery settings

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ids: The IDs array of the discovery settings to delete.  When sending form encoded use ids[].
             :type ids: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy_many"), kwargs)

    def import_settings(self, **kwargs):
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
            |  ``required:`` True
            |  ``default:`` None

             :param import_type: The type of discovery settings to import. Valid values are: range, static, seed
             :type import_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The UnitID of the collector
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import_settings"), kwargs)

    def seed_information(self, **kwargs):
        """Returns the following information: if at least one seed exists, if at least one seed has been discovered, if any IPv6 range is missing a seed

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("seed_information"), kwargs)

    def seed_status(self, **kwargs):
        """List of all Device Seeds and the entire Discovery Status for each one.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` range_start_numeric

             :param sort: The data field to use for sorting the output. Default is range_start_numeric.
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

             :param query: This value will be matched against attribute "range_value" and "VirtualNetworkName". Any DiscoverySetting objects with the passed value contained within one or more of those attributes will be returned.
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

        return self.api_request(self._get_method_fullname("seed_status"), kwargs)
