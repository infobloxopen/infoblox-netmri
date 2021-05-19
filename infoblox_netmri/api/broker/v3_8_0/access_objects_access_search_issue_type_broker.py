from ..broker import Broker


class AccessObjectsAccessSearchIssueTypeBroker(Broker):
    controller = "access_objects_access_search_issue_types"

    def show(self, **kwargs):
        """Shows the details for the specified access objects access search issue type.

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

             :return access_objects_access_search_issue_type: The access objects access search issue type identified by the specified id.
             :rtype access_objects_access_search_issue_type: AccessObjectsAccessSearchIssueType

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available access objects access search issue types. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.8
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value.
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

             :param select: The list of attributes to return for each AccessObjectsAccessSearchIssueType. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value. If empty or omitted, all attributes will be returned.
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

             :return access_objects_access_search_issue_types: An array of the AccessObjectsAccessSearchIssueType objects that match the specified input criteria.
             :rtype access_objects_access_search_issue_types: Array of AccessObjectsAccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available access objects access search issue types matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access_search_issue_type_field: The name of the issue type field.
             :type access_search_issue_type_field: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param access_search_issue_type_id: The internal NetMRI identifier for the access search issue type this record is associated with.
             :type access_search_issue_type_id: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param element_id: The internal NetMRI identifier for the related element_type, NULL for a direct value.
             :type element_id: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param element_type: The element type, DeviceObject, DeviceService, IPv4Value, or FlowValue.
             :type element_type: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this access search alert.
             :type id: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The global name of the object, NULL for a direct value.
             :type name: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param value: The value of the object or direct value. A list of ipv4 or flow value in csv format.
             :type value: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value.
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

             :param select: The list of attributes to return for each AccessObjectsAccessSearchIssueType. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against access objects access search issue types, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: access_search_issue_type_field, access_search_issue_type_id, element_id, element_type, id, name, value.
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

             :return access_objects_access_search_issue_types: An array of the AccessObjectsAccessSearchIssueType objects that match the specified input criteria.
             :rtype access_objects_access_search_issue_types: Array of AccessObjectsAccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available access objects access search issue types matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: access_search_issue_type_field, access_search_issue_type_id, element_id, element_type, id, name, value.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_access_search_issue_type_field: The operator to apply to the field access_search_issue_type_field. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. access_search_issue_type_field: The name of the issue type field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_access_search_issue_type_field: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_access_search_issue_type_field: If op_access_search_issue_type_field is specified, the field named in this input will be compared to the value in access_search_issue_type_field using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_access_search_issue_type_field must be specified if op_access_search_issue_type_field is specified.
             :type val_f_access_search_issue_type_field: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_access_search_issue_type_field: If op_access_search_issue_type_field is specified, this value will be compared to the value in access_search_issue_type_field using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_access_search_issue_type_field must be specified if op_access_search_issue_type_field is specified.
             :type val_c_access_search_issue_type_field: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_access_search_issue_type_id: The operator to apply to the field access_search_issue_type_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. access_search_issue_type_id: The internal NetMRI identifier for the access search issue type this record is associated with. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_access_search_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_access_search_issue_type_id: If op_access_search_issue_type_id is specified, the field named in this input will be compared to the value in access_search_issue_type_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_access_search_issue_type_id must be specified if op_access_search_issue_type_id is specified.
             :type val_f_access_search_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_access_search_issue_type_id: If op_access_search_issue_type_id is specified, this value will be compared to the value in access_search_issue_type_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_access_search_issue_type_id must be specified if op_access_search_issue_type_id is specified.
             :type val_c_access_search_issue_type_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_element_id: The operator to apply to the field element_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. element_id: The internal NetMRI identifier for the related element_type, NULL for a direct value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_element_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_element_id: If op_element_id is specified, the field named in this input will be compared to the value in element_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_element_id must be specified if op_element_id is specified.
             :type val_f_element_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_element_id: If op_element_id is specified, this value will be compared to the value in element_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_element_id must be specified if op_element_id is specified.
             :type val_c_element_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_element_type: The operator to apply to the field element_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. element_type: The element type, DeviceObject, DeviceService, IPv4Value, or FlowValue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_element_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_element_type: If op_element_type is specified, the field named in this input will be compared to the value in element_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_element_type must be specified if op_element_type is specified.
             :type val_f_element_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_element_type: If op_element_type is specified, this value will be compared to the value in element_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_element_type must be specified if op_element_type is specified.
             :type val_c_element_type: String

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

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The global name of the object, NULL for a direct value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_value: The operator to apply to the field value. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. value: The value of the object or direct value. A list of ipv4 or flow value in csv format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_value: If op_value is specified, the field named in this input will be compared to the value in value using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_value must be specified if op_value is specified.
             :type val_f_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_value: If op_value is specified, this value will be compared to the value in value using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_value must be specified if op_value is specified.
             :type val_c_value: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value.
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

             :param select: The list of attributes to return for each AccessObjectsAccessSearchIssueType. Valid values are id, access_search_issue_type_id, access_search_issue_type_field, element_type, element_id, name, value. If empty or omitted, all attributes will be returned.
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

             :return access_objects_access_search_issue_types: An array of the AccessObjectsAccessSearchIssueType objects that match the specified input criteria.
             :rtype access_objects_access_search_issue_types: Array of AccessObjectsAccessSearchIssueType

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
