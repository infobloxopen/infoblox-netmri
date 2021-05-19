from ..broker import Broker


class AccessSearchIssueTypeBroker(Broker):
    controller = "access_search_issue_types"

    def show(self, **kwargs):
        """Shows the details for the specified access search issue type.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_search_issue_type: The access search issue type identified by the specified id.
             :rtype access_search_issue_type: AccessSearchIssueType

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available access search issue types. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id.
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

             :param select: The list of attributes to return for each AccessSearchIssueType. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id. If empty or omitted, all attributes will be returned.
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

             :return access_search_issue_types: An array of the AccessSearchIssueType objects that match the specified input criteria.
             :rtype access_search_issue_types: Array of AccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available access search issue types matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access: The allowance of rule used as criteria for this search alert. One if 'Allow', 'Deny' or 'Any.
             :type access: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param destinations: The list of destination network objects used as criteria for this search alert.
             :type destinations: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param exact_match: A flag indicating whether only rules that match exactly the criteria should be returned.
             :type exact_match: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
             :type id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param issue_meta_type_id: The name of meta type of issue associated with this alert. One of 'WhiteList' or 'BlackList'.
             :type issue_meta_type_id: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param issue_type_id: The internal NetMRI identifier computed for this search alert, which is also a type of issue.
             :type issue_type_id: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this alert..
             :type name: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param services: The list of source ports used as criteria for this search alert.
             :type services: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_ports: The list of service objects used as criteria for this search alert.
             :type source_ports: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sources: The list of source network objects used as criteria for this search alert.
             :type sources: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param workbook_id: The internal NetMRI identifier of the workbook of rule lists on which the searches for this alert should applied.
             :type workbook_id: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id.
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

             :param select: The list of attributes to return for each AccessSearchIssueType. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against access search issue types, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: access, created_at, destinations, exact_match, id, issue_meta_type_id, issue_type_id, name, services, source_ports, sources, updated_at, workbook_id.
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

             :return access_search_issue_types: An array of the AccessSearchIssueType objects that match the specified input criteria.
             :rtype access_search_issue_types: Array of AccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available access search issue types matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: access, created_at, destinations, exact_match, id, issue_meta_type_id, issue_type_id, name, services, source_ports, sources, updated_at, workbook_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_access: The operator to apply to the field access. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. access: The allowance of rule used as criteria for this search alert. One if 'Allow', 'Deny' or 'Any. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_access: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_access: If op_access is specified, the field named in this input will be compared to the value in access using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_access must be specified if op_access is specified.
             :type val_f_access: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_access: If op_access is specified, this value will be compared to the value in access using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_access must be specified if op_access is specified.
             :type val_c_access: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_destinations: The operator to apply to the field destinations. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. destinations: The list of destination network objects used as criteria for this search alert. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_destinations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_destinations: If op_destinations is specified, the field named in this input will be compared to the value in destinations using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_destinations must be specified if op_destinations is specified.
             :type val_f_destinations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_destinations: If op_destinations is specified, this value will be compared to the value in destinations using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_destinations must be specified if op_destinations is specified.
             :type val_c_destinations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_exact_match: The operator to apply to the field exact_match. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. exact_match: A flag indicating whether only rules that match exactly the criteria should be returned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_exact_match: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_exact_match: If op_exact_match is specified, the field named in this input will be compared to the value in exact_match using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_exact_match must be specified if op_exact_match is specified.
             :type val_f_exact_match: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_exact_match: If op_exact_match is specified, this value will be compared to the value in exact_match using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_exact_match must be specified if op_exact_match is specified.
             :type val_c_exact_match: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this access search alert. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_issue_meta_type_id: The operator to apply to the field issue_meta_type_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. issue_meta_type_id: The name of meta type of issue associated with this alert. One of 'WhiteList' or 'BlackList'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_issue_meta_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_issue_meta_type_id: If op_issue_meta_type_id is specified, the field named in this input will be compared to the value in issue_meta_type_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_issue_meta_type_id must be specified if op_issue_meta_type_id is specified.
             :type val_f_issue_meta_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_issue_meta_type_id: If op_issue_meta_type_id is specified, this value will be compared to the value in issue_meta_type_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_issue_meta_type_id must be specified if op_issue_meta_type_id is specified.
             :type val_c_issue_meta_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_issue_type_id: The operator to apply to the field issue_type_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. issue_type_id: The internal NetMRI identifier computed for this search alert, which is also a type of issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_issue_type_id: If op_issue_type_id is specified, the field named in this input will be compared to the value in issue_type_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_issue_type_id must be specified if op_issue_type_id is specified.
             :type val_f_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_issue_type_id: If op_issue_type_id is specified, this value will be compared to the value in issue_type_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_issue_type_id must be specified if op_issue_type_id is specified.
             :type val_c_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of this alert.. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_name: If op_name is specified, the field named in this input will be compared to the value in name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_name must be specified if op_name is specified.
             :type val_f_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_name: If op_name is specified, this value will be compared to the value in name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_name must be specified if op_name is specified.
             :type val_c_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_services: The operator to apply to the field services. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. services: The list of source ports used as criteria for this search alert. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_services: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_services: If op_services is specified, the field named in this input will be compared to the value in services using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_services must be specified if op_services is specified.
             :type val_f_services: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_services: If op_services is specified, this value will be compared to the value in services using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_services must be specified if op_services is specified.
             :type val_c_services: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_source_ports: The operator to apply to the field source_ports. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. source_ports: The list of service objects used as criteria for this search alert. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_source_ports: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_source_ports: If op_source_ports is specified, the field named in this input will be compared to the value in source_ports using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_source_ports must be specified if op_source_ports is specified.
             :type val_f_source_ports: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_source_ports: If op_source_ports is specified, this value will be compared to the value in source_ports using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_source_ports must be specified if op_source_ports is specified.
             :type val_c_source_ports: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sources: The operator to apply to the field sources. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sources: The list of source network objects used as criteria for this search alert. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sources: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sources: If op_sources is specified, the field named in this input will be compared to the value in sources using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sources must be specified if op_sources is specified.
             :type val_f_sources: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sources: If op_sources is specified, this value will be compared to the value in sources using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sources must be specified if op_sources is specified.
             :type val_c_sources: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_workbook_id: The operator to apply to the field workbook_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. workbook_id: The internal NetMRI identifier of the workbook of rule lists on which the searches for this alert should applied. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_workbook_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_workbook_id: If op_workbook_id is specified, the field named in this input will be compared to the value in workbook_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_workbook_id must be specified if op_workbook_id is specified.
             :type val_f_workbook_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_workbook_id: If op_workbook_id is specified, this value will be compared to the value in workbook_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_workbook_id must be specified if op_workbook_id is specified.
             :type val_c_workbook_id: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id.
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

             :param select: The list of attributes to return for each AccessSearchIssueType. Valid values are id, issue_meta_type_id, name, sources, destinations, source_ports, services, access, exact_match, workbook_id, created_at, updated_at, issue_type_id. If empty or omitted, all attributes will be returned.
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

             :return access_search_issue_types: An array of the AccessSearchIssueType objects that match the specified input criteria.
             :rtype access_search_issue_types: Array of AccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing access search issue type.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access: The allowance of rule used as criteria for this search alert. One if 'Allow', 'Deny' or 'Any. If omitted, this field will not be updated.
             :type access: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param destinations: The list of destination network objects used as criteria for this search alert. If omitted, this field will not be updated.
             :type destinations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param exact_match: A flag indicating whether only rules that match exactly the criteria should be returned. If omitted, this field will not be updated.
             :type exact_match: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param issue_meta_type_id: The name of meta type of issue associated with this alert. One of 'WhiteList' or 'BlackList'. If omitted, this field will not be updated.
             :type issue_meta_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param issue_type_id: The internal NetMRI identifier computed for this search alert, which is also a type of issue. If omitted, this field will not be updated.
             :type issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this alert.. If omitted, this field will not be updated.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param services: The list of source ports used as criteria for this search alert. If omitted, this field will not be updated.
             :type services: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_ports: The list of service objects used as criteria for this search alert. If omitted, this field will not be updated.
             :type source_ports: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sources: The list of source network objects used as criteria for this search alert. If omitted, this field will not be updated.
             :type sources: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param workbook_id: The internal NetMRI identifier of the workbook of rule lists on which the searches for this alert should applied. If omitted, this field will not be updated.
             :type workbook_id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated access search issue type.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated access search issue type.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated access search issue type.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_search_issue_type: The updated access search issue type.
             :rtype access_search_issue_type: AccessSearchIssueType

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified access search issue type from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Created a new issueType for search access checking. Note: This will only create Whitelist and Blacklist issue types. Updating AccessSearchIssueTypes is currently not permitted.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param issue_meta_type_id: Symbolic name of kind of list one of 'MandatoryFlow', 'ForbiddenFlow'.
             :type issue_meta_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Name of this new issueType.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param workbook_id: The internal identifier for the workbook to search.
             :type workbook_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param sources: The source address specifications.
             :type sources: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_ports: The source service specifications. Individual entries may be blank, but the ordering of the array must correspond to the ordering of the source address specification array.
             :type source_ports: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param destinations: The destination address specifications.
             :type destinations: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param services: The destination service specifications.
             :type services: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param access: The access type to search for: Allow, Deny, Any.
             :type access: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param exact_match: Only return results for exact matches.
             :type exact_match: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access search issue type.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access search issue type.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access search issue type.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_search_issue_type: The newly created access search issue type.
             :rtype access_search_issue_type: AccessSearchIssueType

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)
