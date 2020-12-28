from ..broker import Broker


class ScriptBroker(Broker):
    controller = "scripts"

    def index(self, **kwargs):
        """Lists the available scripts. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind.
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

             :param select: The list of attributes to return for each Script. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind. If empty or omitted, all attributes will be returned.
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

             :return scripts: An array of the Script objects that match the specified input criteria.
             :rtype scripts: Array of Script

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified script.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return script: The script identified by the specified id.
             :rtype script: Script

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available scripts matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param category: Currently unused.
             :type category: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: Currently unused.
             :type category: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the script was initially imported into NetMRI.
             :type created_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the script was initially imported into NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user that initially imported the script into NetMRI.
             :type created_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user that initially imported the script into NetMRI.
             :type created_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param description: Describes the purpose, function and usage of this script.
             :type description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Describes the purpose, function and usage of this script.
             :type description: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param language: The scripting language used; currently the only supported language is CCS.
             :type language: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param language: The scripting language used; currently the only supported language is CCS.
             :type language: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param module: Currently unused.
             :type module: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param module: Currently unused.
             :type module: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param read_only: Read-only scripts are not user modifiable.
             :type read_only: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read_only: Read-only scripts are not user modifiable.
             :type read_only: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param risk_level: The user-specified risk level for the script. Possible levels are 1 (low), 2 (medium), and 3 (high). To run higher risk scripts, higher privileges are required.
             :type risk_level: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param risk_level: The user-specified risk level for the script. Possible levels are 1 (low), 2 (medium), and 3 (high). To run higher risk scripts, higher privileges are required.
             :type risk_level: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param target_mapping: Kind of mapping used for this script : 'device' ...
             :type target_mapping: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param target_mapping: Kind of mapping used for this script : 'device' ...
             :type target_mapping: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_create: Internal workflow name for job creation using this script.
             :type taskflow_create: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_create: Internal workflow name for job creation using this script.
             :type taskflow_create: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_edit: Internal workflow name for job edition using this script.
             :type taskflow_edit: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_edit: Internal workflow name for job edition using this script.
             :type taskflow_edit: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_revert: Internal workflow name for job reversion using this script.
             :type taskflow_revert: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_revert: Internal workflow name for job reversion using this script.
             :type taskflow_revert: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating if devices should be reserved during execution of this script.
             :type transactional_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating if devices should be reserved during execution of this script.
             :type transactional_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the script was last modified.
             :type updated_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the script was last modified.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: The user that last modified this script.
             :type updated_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: The user that last modified this script.
             :type updated_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param visible: Indicates whether this script is visible on the user interface.
             :type visible: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param visible: Indicates whether this script is visible on the user interface.
             :type visible: Array of Boolean

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind.
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

             :param select: The list of attributes to return for each Script. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against scripts, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: category, created_at, created_by, description, id, language, module, name, read_only, risk_level, target_mapping, taskflow_create, taskflow_edit, taskflow_revert, transactional_ind, updated_at, updated_by, visible.
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

             :return scripts: An array of the Script objects that match the specified input criteria.
             :rtype scripts: Array of Script

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available scripts matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: category, created_at, created_by, description, id, language, module, name, read_only, risk_level, target_mapping, taskflow_create, taskflow_edit, taskflow_revert, transactional_ind, updated_at, updated_by, visible.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: Currently unused. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_category: If op_category is specified, the field named in this input will be compared to the value in category using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_category must be specified if op_category is specified.
             :type val_f_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_category: If op_category is specified, this value will be compared to the value in category using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_category must be specified if op_category is specified.
             :type val_c_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the script was initially imported into NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: The user that initially imported the script into NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: Describes the purpose, function and usage of this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_description: If op_description is specified, the field named in this input will be compared to the value in description using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_description must be specified if op_description is specified.
             :type val_f_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_description: If op_description is specified, this value will be compared to the value in description using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_description must be specified if op_description is specified.
             :type val_c_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_language: The operator to apply to the field language. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. language: The scripting language used; currently the only supported language is CCS. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_language: If op_language is specified, the field named in this input will be compared to the value in language using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_language must be specified if op_language is specified.
             :type val_f_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_language: If op_language is specified, this value will be compared to the value in language using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_language must be specified if op_language is specified.
             :type val_c_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_module: The operator to apply to the field module. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. module: Currently unused. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_module: If op_module is specified, the field named in this input will be compared to the value in module using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_module must be specified if op_module is specified.
             :type val_f_module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_module: If op_module is specified, this value will be compared to the value in module using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_module must be specified if op_module is specified.
             :type val_c_module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_read_only: The operator to apply to the field read_only. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. read_only: Read-only scripts are not user modifiable. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_read_only: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_read_only: If op_read_only is specified, the field named in this input will be compared to the value in read_only using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_read_only must be specified if op_read_only is specified.
             :type val_f_read_only: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_read_only: If op_read_only is specified, this value will be compared to the value in read_only using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_read_only must be specified if op_read_only is specified.
             :type val_c_read_only: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_risk_level: The operator to apply to the field risk_level. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. risk_level: The user-specified risk level for the script. Possible levels are 1 (low), 2 (medium), and 3 (high). To run higher risk scripts, higher privileges are required. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_risk_level: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_risk_level: If op_risk_level is specified, the field named in this input will be compared to the value in risk_level using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_risk_level must be specified if op_risk_level is specified.
             :type val_f_risk_level: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_risk_level: If op_risk_level is specified, this value will be compared to the value in risk_level using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_risk_level must be specified if op_risk_level is specified.
             :type val_c_risk_level: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_target_mapping: The operator to apply to the field target_mapping. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. target_mapping: Kind of mapping used for this script : 'device' ... For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_target_mapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_target_mapping: If op_target_mapping is specified, the field named in this input will be compared to the value in target_mapping using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_target_mapping must be specified if op_target_mapping is specified.
             :type val_f_target_mapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_target_mapping: If op_target_mapping is specified, this value will be compared to the value in target_mapping using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_target_mapping must be specified if op_target_mapping is specified.
             :type val_c_target_mapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_taskflow_create: The operator to apply to the field taskflow_create. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. taskflow_create: Internal workflow name for job creation using this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_taskflow_create: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_taskflow_create: If op_taskflow_create is specified, the field named in this input will be compared to the value in taskflow_create using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_taskflow_create must be specified if op_taskflow_create is specified.
             :type val_f_taskflow_create: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_taskflow_create: If op_taskflow_create is specified, this value will be compared to the value in taskflow_create using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_taskflow_create must be specified if op_taskflow_create is specified.
             :type val_c_taskflow_create: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_taskflow_edit: The operator to apply to the field taskflow_edit. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. taskflow_edit: Internal workflow name for job edition using this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_taskflow_edit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_taskflow_edit: If op_taskflow_edit is specified, the field named in this input will be compared to the value in taskflow_edit using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_taskflow_edit must be specified if op_taskflow_edit is specified.
             :type val_f_taskflow_edit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_taskflow_edit: If op_taskflow_edit is specified, this value will be compared to the value in taskflow_edit using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_taskflow_edit must be specified if op_taskflow_edit is specified.
             :type val_c_taskflow_edit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_taskflow_revert: The operator to apply to the field taskflow_revert. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. taskflow_revert: Internal workflow name for job reversion using this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_taskflow_revert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_taskflow_revert: If op_taskflow_revert is specified, the field named in this input will be compared to the value in taskflow_revert using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_taskflow_revert must be specified if op_taskflow_revert is specified.
             :type val_f_taskflow_revert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_taskflow_revert: If op_taskflow_revert is specified, this value will be compared to the value in taskflow_revert using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_taskflow_revert must be specified if op_taskflow_revert is specified.
             :type val_c_taskflow_revert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_transactional_ind: The operator to apply to the field transactional_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. transactional_ind: Flag indicating if devices should be reserved during execution of this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_transactional_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_transactional_ind: If op_transactional_ind is specified, the field named in this input will be compared to the value in transactional_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_transactional_ind must be specified if op_transactional_ind is specified.
             :type val_f_transactional_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_transactional_ind: If op_transactional_ind is specified, this value will be compared to the value in transactional_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_transactional_ind must be specified if op_transactional_ind is specified.
             :type val_c_transactional_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the script was last modified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_by: The operator to apply to the field updated_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_by: The user that last modified this script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_visible: The operator to apply to the field visible. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. visible: Indicates whether this script is visible on the user interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_visible: If op_visible is specified, the field named in this input will be compared to the value in visible using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_visible must be specified if op_visible is specified.
             :type val_f_visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_visible: If op_visible is specified, this value will be compared to the value in visible using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_visible must be specified if op_visible is specified.
             :type val_c_visible: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind.
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

             :param select: The list of attributes to return for each Script. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind. If empty or omitted, all attributes will be returned.
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

             :return scripts: An array of the Script objects that match the specified input criteria.
             :rtype scripts: Array of Script

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def export_file(self, **kwargs):
        """Export a CCS/Perl/Python script from the server.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to export.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return content: The content of the script.
             :rtype content: String

            """

        return self.api_request(self._get_method_fullname("export_file"), kwargs)

    def import_file(self, **kwargs):
        """Import a CCS/Perl/Python script into the server.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to update.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param content: The content of the script.
             :type content: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import_file"), kwargs)

    def create(self, **kwargs):
        """Create a CCS/Perl/Python script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param script_file: The script file contents.
             :type script_file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param overwrite: Overwrite any existing version of the script with the same name.
             :type overwrite: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` CCS

             :param language: The language the script is written in (CCS, Perl, Python).
             :type language: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Update a CCS/Perl/Python script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to update.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param script_file: The script file contents.
             :type script_file: String

            |  ``api version min:`` 2.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` CCS

             :param language: The language the script is written in (CCS, Perl, Python).
             :type language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param overwrite: Overwrite any existing version of the script with the same name.
             :type overwrite: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Delete a CCS script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to delete.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def run(self, **kwargs):
        """Run a script immediately with specified input. In addition to the listed parameters, optional parameters can be passed. Any parameter name starting with \$ will be passed as Script-Variable to the script.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.1
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to run.
             :type id: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The ID of the script to run. Required unless name is specified.
             :type id: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the script to run. Required unless ID is specified.
             :type name: String

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param wait: Maximum number of seconds to wait for script completion before returning the job result. Using a value of 0 will cause the call to schedule the job and return immediately. Requires that the target is one single device.
             :type wait: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: An array of device group ids. Can be blank if not using device groups.
             :type device_group_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: An array of device ids. Can be blank if ONLY using device groups.
             :type device_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` requestor

             :param credential_mode: If user credentials are required, they may be set from additional inputs (credential_mode = 'manual'). The credentials may be looked up using requestor stored credentials (credential_mode = 'requestor').
             :type credential_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: Username to be used if the job requires user credentials.
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: Password to be used if the job requires user credentials.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enable_password: Enable password to be used if the job requires user credentials.
             :type enable_password: String

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_name: Optional name for this run of a job.
             :type job_name: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return JobID: The JobID of the running script.
             :rtype JobID: Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the job, if the call input wait parameter had a non zero value. Status Pending or Running indicates the call timed out and the job is still in processing.
             :rtype status: String

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return payload: The JSON payload of the script output, if any. Only set if Status is set and its value is OK.
             :rtype payload: String

            """

        return self.api_request(self._get_method_fullname("run"), kwargs)
