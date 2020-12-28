from ..broker import Broker


class AccessChangeBroker(Broker):
    controller = "access_changes"

    def show(self, **kwargs):
        """Shows the details for the specified access change.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this provisioning operation.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of access change methods. The listed methods will be called on each access change returned and included in the output. Available methods are: summary.
             :type methods: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The access change identified by the specified id.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available access changes. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this provisioning operation.
             :type id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of access change methods. The listed methods will be called on each access change returned and included in the output. Available methods are: summary.
             :type methods: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable.
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

             :param select: The list of attributes to return for each AccessChange. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable. If empty or omitted, all attributes will be returned.
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

             :return access_changes: An array of the AccessChange objects that match the specified input criteria.
             :rtype access_changes: Array of AccessChange

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available access changes matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param change_set_key: The random generated key that identify this provisioning operation.
             :type change_set_key: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param change_status: The status of workflow of this provisioning, one of : 'Init', 'Edit', 'JobRunning', 'JobAchieved'.
             :type change_status: Array of String

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

             :param deployable: String containing list of firewalls on which new rules can be deployed.
             :type deployable: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param edit_status: The status of edition for this provisioning : one of 'Starting', 'Running', 'Cancelled', 'Done', 'Error'.
             :type edit_status: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param error_count: The total number of errors raised in last analysis.
             :type error_count: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param former_proposal_json: The one level history of the proposals, aka proposals of the former analysis - json format.
             :type former_proposal_json: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param general_errors: The list of all errors computed at last analysis - pipe separated.
             :type general_errors: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param history_json: The history of the whole workflow for this provisioning - json format.
             :type history_json: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this provisioning operation.
             :type id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The internal NetMRI identifier of execution of job.
             :type job_id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal NetMRI identifier of the job that hold the provisioning.
             :type job_specification_id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proposal_json: The proposals for provisioning (at the last edition) - json format.
             :type proposal_json: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param reversible: The state of reversibility of the current provisioning, one of : 'full', 'partial', 'none'.
             :type reversible: Array of String

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

             :param user_name: The name of the user that created this provisioning operation.
             :type user_name: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_proposal_json: The proposals accepted and modified by user, last sent to analysis - json format.
             :type user_proposal_json: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param warning_count: The total number of warning raised in the last analysis.
             :type warning_count: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of access change methods. The listed methods will be called on each access change returned and included in the output. Available methods are: summary.
             :type methods: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable.
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

             :param select: The list of attributes to return for each AccessChange. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against access changes, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: change_set_key, change_status, created_at, deployable, edit_status, error_count, former_proposal_json, general_errors, history_json, id, job_id, job_specification_id, proposal_json, reversible, updated_at, user_name, user_proposal_json, warning_count.
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

             :return access_changes: An array of the AccessChange objects that match the specified input criteria.
             :rtype access_changes: Array of AccessChange

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available access changes matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: change_set_key, change_status, created_at, deployable, edit_status, error_count, former_proposal_json, general_errors, history_json, id, job_id, job_specification_id, proposal_json, reversible, updated_at, user_name, user_proposal_json, warning_count.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_change_set_key: The operator to apply to the field change_set_key. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. change_set_key: The random generated key that identify this provisioning operation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_change_set_key: If op_change_set_key is specified, the field named in this input will be compared to the value in change_set_key using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_change_set_key must be specified if op_change_set_key is specified.
             :type val_f_change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_change_set_key: If op_change_set_key is specified, this value will be compared to the value in change_set_key using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_change_set_key must be specified if op_change_set_key is specified.
             :type val_c_change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_change_status: The operator to apply to the field change_status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. change_status: The status of workflow of this provisioning, one of : 'Init', 'Edit', 'JobRunning', 'JobAchieved'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_change_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_change_status: If op_change_status is specified, the field named in this input will be compared to the value in change_status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_change_status must be specified if op_change_status is specified.
             :type val_f_change_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_change_status: If op_change_status is specified, this value will be compared to the value in change_status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_change_status must be specified if op_change_status is specified.
             :type val_c_change_status: String

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

             :param op_deployable: The operator to apply to the field deployable. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. deployable: String containing list of firewalls on which new rules can be deployed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_deployable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_deployable: If op_deployable is specified, the field named in this input will be compared to the value in deployable using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_deployable must be specified if op_deployable is specified.
             :type val_f_deployable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_deployable: If op_deployable is specified, this value will be compared to the value in deployable using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_deployable must be specified if op_deployable is specified.
             :type val_c_deployable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_edit_status: The operator to apply to the field edit_status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. edit_status: The status of edition for this provisioning : one of 'Starting', 'Running', 'Cancelled', 'Done', 'Error'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_edit_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_edit_status: If op_edit_status is specified, the field named in this input will be compared to the value in edit_status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_edit_status must be specified if op_edit_status is specified.
             :type val_f_edit_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_edit_status: If op_edit_status is specified, this value will be compared to the value in edit_status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_edit_status must be specified if op_edit_status is specified.
             :type val_c_edit_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_error_count: The operator to apply to the field error_count. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. error_count: The total number of errors raised in last analysis. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_error_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_error_count: If op_error_count is specified, the field named in this input will be compared to the value in error_count using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_error_count must be specified if op_error_count is specified.
             :type val_f_error_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_error_count: If op_error_count is specified, this value will be compared to the value in error_count using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_error_count must be specified if op_error_count is specified.
             :type val_c_error_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_former_proposal_json: The operator to apply to the field former_proposal_json. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. former_proposal_json: The one level history of the proposals, aka proposals of the former analysis - json format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_former_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_former_proposal_json: If op_former_proposal_json is specified, the field named in this input will be compared to the value in former_proposal_json using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_former_proposal_json must be specified if op_former_proposal_json is specified.
             :type val_f_former_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_former_proposal_json: If op_former_proposal_json is specified, this value will be compared to the value in former_proposal_json using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_former_proposal_json must be specified if op_former_proposal_json is specified.
             :type val_c_former_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_general_errors: The operator to apply to the field general_errors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. general_errors: The list of all errors computed at last analysis - pipe separated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_general_errors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_general_errors: If op_general_errors is specified, the field named in this input will be compared to the value in general_errors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_general_errors must be specified if op_general_errors is specified.
             :type val_f_general_errors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_general_errors: If op_general_errors is specified, this value will be compared to the value in general_errors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_general_errors must be specified if op_general_errors is specified.
             :type val_c_general_errors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_history_json: The operator to apply to the field history_json. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. history_json: The history of the whole workflow for this provisioning - json format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_history_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_history_json: If op_history_json is specified, the field named in this input will be compared to the value in history_json using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_history_json must be specified if op_history_json is specified.
             :type val_f_history_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_history_json: If op_history_json is specified, this value will be compared to the value in history_json using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_history_json must be specified if op_history_json is specified.
             :type val_c_history_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this provisioning operation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_id: The operator to apply to the field job_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_id: The internal NetMRI identifier of execution of job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_job_id: If op_job_id is specified, the field named in this input will be compared to the value in job_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_job_id must be specified if op_job_id is specified.
             :type val_f_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_job_id: If op_job_id is specified, this value will be compared to the value in job_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_job_id must be specified if op_job_id is specified.
             :type val_c_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_specification_id: The operator to apply to the field job_specification_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_specification_id: The internal NetMRI identifier of the job that hold the provisioning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_job_specification_id: If op_job_specification_id is specified, the field named in this input will be compared to the value in job_specification_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_job_specification_id must be specified if op_job_specification_id is specified.
             :type val_f_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_job_specification_id: If op_job_specification_id is specified, this value will be compared to the value in job_specification_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_job_specification_id must be specified if op_job_specification_id is specified.
             :type val_c_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_proposal_json: The operator to apply to the field proposal_json. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. proposal_json: The proposals for provisioning (at the last edition) - json format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_proposal_json: If op_proposal_json is specified, the field named in this input will be compared to the value in proposal_json using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_proposal_json must be specified if op_proposal_json is specified.
             :type val_f_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_proposal_json: If op_proposal_json is specified, this value will be compared to the value in proposal_json using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_proposal_json must be specified if op_proposal_json is specified.
             :type val_c_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_reversible: The operator to apply to the field reversible. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. reversible: The state of reversibility of the current provisioning, one of : 'full', 'partial', 'none'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_reversible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_reversible: If op_reversible is specified, the field named in this input will be compared to the value in reversible using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_reversible must be specified if op_reversible is specified.
             :type val_f_reversible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_reversible: If op_reversible is specified, this value will be compared to the value in reversible using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_reversible must be specified if op_reversible is specified.
             :type val_c_reversible: String

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

             :param op_user_name: The operator to apply to the field user_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_name: The name of the user that created this provisioning operation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_name: If op_user_name is specified, the field named in this input will be compared to the value in user_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_name must be specified if op_user_name is specified.
             :type val_f_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_name: If op_user_name is specified, this value will be compared to the value in user_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_name must be specified if op_user_name is specified.
             :type val_c_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_user_proposal_json: The operator to apply to the field user_proposal_json. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_proposal_json: The proposals accepted and modified by user, last sent to analysis - json format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_proposal_json: If op_user_proposal_json is specified, the field named in this input will be compared to the value in user_proposal_json using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_proposal_json must be specified if op_user_proposal_json is specified.
             :type val_f_user_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_proposal_json: If op_user_proposal_json is specified, this value will be compared to the value in user_proposal_json using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_proposal_json must be specified if op_user_proposal_json is specified.
             :type val_c_user_proposal_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_warning_count: The operator to apply to the field warning_count. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. warning_count: The total number of warning raised in the last analysis. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_warning_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_warning_count: If op_warning_count is specified, the field named in this input will be compared to the value in warning_count using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_warning_count must be specified if op_warning_count is specified.
             :type val_f_warning_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_warning_count: If op_warning_count is specified, this value will be compared to the value in warning_count using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_warning_count must be specified if op_warning_count is specified.
             :type val_c_warning_count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of access change methods. The listed methods will be called on each access change returned and included in the output. Available methods are: summary.
             :type methods: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable.
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

             :param select: The list of attributes to return for each AccessChange. Valid values are id, user_name, change_set_key, edit_status, proposal_json, created_at, updated_at, change_status, general_errors, history_json, user_proposal_json, warning_count, error_count, job_specification_id, job_id, former_proposal_json, reversible, deployable. If empty or omitted, all attributes will be returned.
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

             :return access_changes: An array of the AccessChange objects that match the specified input criteria.
             :rtype access_changes: Array of AccessChange

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create_from_search(self, **kwargs):
        """Creates a proposed set of changes from selected search results.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param search_set_key: The identifier for the originating search set as returned by the Access Search create method.
             :type search_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_rules_to_provision: The list of search elements ids for provisioning - from primary table.
             :type search_rules_to_provision: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_filters_to_remove: The list of search result rules ids to delete in the provisioning - from secondary table.
             :type search_filters_to_remove: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The newly created access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("create_from_search"), kwargs)

    def create_by_searching(self, **kwargs):
        """Initiates a network access search, and uses the results to propose a set of changes.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param workbook_id: The internal identifier for the workbook to search. If omitted, the active set will be searched.
             :type workbook_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param source: The source address specifications.
             :type source: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_service: The source service specifications. Individual entries may be blank, but the ordering of the array must correspond to the ordering of the source address specification array.
             :type source_service: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param destination: The destination address specifications.
             :type destination: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param destination_service: The destination service specifications.
             :type destination_service: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` Allow

             :param access_type: The access type to search for: Allow, Deny, Any.
             :type access_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param exact_match_ind: Only return results for exact matches.
             :type exact_match_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The newly created access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("create_by_searching"), kwargs)

    def create_from_job(self, **kwargs):
        """Creates a proposed set of changes to repeat or rollback a specified job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param job_id: The identifier of the job to repeat or rollback.
             :type job_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param for: Specifies if the proposed changes are for repeating or rolling back the job. Valid are 'repeat' and 'rollback'.
             :type for: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` none

             :param restriction: Specifies if the set of proposed changes to re-analyze is restricted.
             :type restriction: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The newly created access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("create_from_job"), kwargs)

    def create_from_job_specification(self, **kwargs):
        """Recreates a proposed set of changes associated with a specific job specification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param job_specification_id: The identifier of the job specification to edit.
             :type job_specification_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The newly created access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("create_from_job_specification"), kwargs)

    def create_from_issue(self, **kwargs):
        """Creates a set of changes to remediate a specific issue or set of issues.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param issue_ids: An array of IssueID values for issues to remediate.
             :type issue_ids: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The newly created access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("create_from_issue"), kwargs)

    def reset(self, **kwargs):
        """Resets a modified proposal to the original proposal.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The internal NetMRI identifier of the access change.
             :type change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` clean

             :param kind: Specify if we reset ALL the proposals to the former analysis, or only partials: we keep last proposals add unselected proposals from the former analysis.
             :type kind: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The updated access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("reset"), kwargs)

    def update(self, **kwargs):
        """Updates the access change proposal.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The internal NetMRI identifier of the access change.
             :type change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param rejected_proposals: The list of proposals (ProposalID values) that are not kept for provisioning.
             :type rejected_proposals: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param accepted_proposals: The list of proposals (ProposalID values) to accept as is for provisioning. 'action : in ['allow', 'deny'],
                        rule_nb : integer, source_id : string, source_name : string,
                        destination_id : string, destination_id : string,
                        service_id : string, service_name : string
             :type accepted_proposals: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_proposals: The list of proposals (ProposalID values) that have been updated.
             :type updated_proposals: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param delete_proposals: A list of types of objects for which to proposal deletions. This enables the client to propose changes that were not suggested by the system. The specific object IDs should be listed in the delete_object_ids array in the same order as this array. Each element must be one of ['network_object', 'service', 'filter_set', 'filter']
             :type delete_proposals: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param delete_object_ids: The list of object ID values corresponding to the object types listed in delete_proposals. The ordering and types must match that of the delete_proposals list.
             :type delete_object_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_actions: A list of allow/deny actions to propose as a new rule. This enables the client to propose the addition of rules that were not suggested by the system. The specific rule parameters will be specified in the add_filter_sources, add_filter_destinations, add_filter_services, and add_filter_source_services arrays. Each element mus be one of  ['Allow', 'Deny']
             :type add_filter_actions: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_sources: A list of new names for ip-objects sources corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_sources: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_source_ids: A list of selected id for sources corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_source_ids: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_destinations: A list new names for ip-objects as destinations corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_destinations: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_destination_ids: A list of selected id of destinations corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_destination_ids: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_services: A list of new names for services corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_services: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_service_ids: A list of selected id of services corresponding to the allow/deny actions in add_filter_actions.
             :type add_filter_service_ids: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param add_filter_rule_numbers: A list of rules position for each rule of add_filter_actions.
             :type add_filter_rule_numbers: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated access change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated access change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated access change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change: The updated access change.
             :rtype access_change: AccessChange

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def cancel(self, **kwargs):
        """Cancels a currently executing create_xxx request.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this change set as returned by the search_and_create method.
             :type change_set_key: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel"), kwargs)

    def status(self, **kwargs):
        """The status of the overall create_xxx set execution.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this change set as returned by the search_and_create method.
             :type change_set_key: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the set execution. If the status is Running, Done, or Error the proposed_changes call will return values.
             :rtype status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return error_count: When status Done, indicates the nb of errors raised by analysis of the proposals. -1 if status not Done
             :rtype error_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return warning_count: When status Done, indicates the nb of warnings raised by analysis of the proposals. -1 if status not Done
             :rtype warning_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return reversible: Global reversibility for the set of proposals.
             :rtype reversible: String

            """

        return self.api_request(self._get_method_fullname("status"), kwargs)

    def summary(self, **kwargs):
        """Returns a summary of a network access create_by_searching request.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this specific change set as returned by the create_from_search method.
             :type change_set_key: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the overall create_by_searching set execution. If the status is Running, Done, or Error the proposed_changes call will return values.
             :rtype status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return title: Title of summary for proposals of the change.
             :rtype title: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sub_title: Initial title and details of summary for proposals of the change.
             :rtype sub_title: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return details: Details of the summary - a list of line
             :rtype details: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return errors: Global errors retrieved while trying to provision - a list of line
             :rtype errors: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return search_count: The number of individual searches in the create_by_searching set.
             :rtype search_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return rule_count: The number of rules in the create_by_searching set.
             :rtype rule_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_count: The number of devices in the create_by_searching set.
             :rtype device_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_filter_set_count: The number of device rule lists in the create_by_searching set.
             :rtype device_filter_set_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return running_search_count: The number of individual searches from this create_by_searching set that are currently running.
             :rtype running_search_count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return reversible: Global reversibility for the set of proposals.
             :rtype reversible: String

            """

        return self.api_list_request(self._get_method_fullname("summary"), kwargs)

    def proposed_changes(self, **kwargs):
        """Returns the proposed changes for a change set.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this change set as returned by the create method.
             :type change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for the originating change set as returned by the Access Change Proposal create method.
             :type change_set_key: String

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
            |  ``default:`` None

             :param sort: The data field(s) to use for sorting the output. Default is . Valid values are id, DeviceID, ProposalID, DeviceType, DeviceAssurance, DeviceName, DeviceIPDotted, Network, VirtualNetworkID, DeviceIPNumeric, DeviceFilterSetID, DeviceFilterSetName, RuleNum, RuleNumEditableInd, SrcObjID, SrcObjName, SrcMatchedObjNames, SrcObjSummary, SrcObjEditableInd, SrcObjHasDetailInd, DestObjID, DestObjName, DestMatchedObjNames, DestObjSummary, DestObjEditableInd, DestObjHasDetailInd, SvcID, SvcName, SvcMatchedObjNames, SvcSummary, SvcEditableInd, SvcHasDetailInd, SrcSvcName, Action, Warning, WarningMsg, WarningMsgHasDetailInd, ConfigurationDetails, SrcGroupTag, DestGroupTag, SvcGroupTag.
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

             :param select: The list of attributes to return for each . Valid values are id, DeviceID, ProposalID, DeviceType, DeviceAssurance, DeviceName, DeviceIPDotted, Network, VirtualNetworkID, DeviceIPNumeric, DeviceFilterSetID, DeviceFilterSetName, RuleNum, RuleNumEditableInd, SrcObjID, SrcObjName, SrcMatchedObjNames, SrcObjSummary, SrcObjEditableInd, SrcObjHasDetailInd, DestObjID, DestObjName, DestMatchedObjNames, DestObjSummary, DestObjEditableInd, DestObjHasDetailInd, SvcID, SvcName, SvcMatchedObjNames, SvcSummary, SvcEditableInd, SvcHasDetailInd, SrcSvcName, Action, Warning, WarningMsg, WarningMsgHasDetailInd, ConfigurationDetails, SrcGroupTag, DestGroupTag, SvcGroupTag. If empty or omitted, all attributes will be returned.
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

             :return proposed_changes: The list of proposed changes in this change set.
             :rtype proposed_changes: Array of AccessChangeProposalGrid

            """

        return self.api_list_request(self._get_method_fullname("proposed_changes"), kwargs)

    def run(self, **kwargs):
        """Create job specification for provisioning and launch it.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this create_by_searching set as returned by the create method.
             :type change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param approved: Indicates whether or not this job is approved.
             :type approved: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule: If launched for later, the schedule information. nil for no schedule
             :type schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param revert_on_error: If true, all already succeeded sub-jobs will be revert on first failed sub-job, otherwise continue to end until all processes launched.
             :type revert_on_error: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param custom_field_names: Names of the filled custom fields for this job
             :type custom_field_names: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param custom_field_values: Corresponding values of the filled custom fields for this job
             :type custom_field_values: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param credential_mode: If user credentials are required, they may be set from additional inputs (credential_mode = 'manual').
                      The credentials may be looked up using requestor stored credentials (credential_mode = 'requestor').
                      The credentials may be looked up using the approver stored credentials (credential_mode = 'approver').
             :type credential_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enable_password: Enable Password to be used if the job requires user credentials
             :type enable_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: username part of the 'manual' credential, if required
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: password part of the 'manual' credential, if required
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_spec_id: The job specification id for editing job.
             :type job_spec_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_specification_id: The job specification id of the prepared job.
             :rtype job_specification_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_id: The job id of the launched exec. Available only for a runNow
             :rtype job_id: Integer

            """

        return self.api_request(self._get_method_fullname("run"), kwargs)

    def cancel_job(self, **kwargs):
        """Cancel any running or scheduled job for provisionning and launch it.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this set as returned by the create method.
             :type change_set_key: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel_job"), kwargs)

    def describe(self, **kwargs):
        """Returns tree-format information about this device rule based on description type.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param change_set_key: The identifier for this change set as returned by one of the create methods.
             :type change_set_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param proposal_id: The line in the grid.
             :type proposal_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description_type: The description type for a specific device rule property: Source, Destination, Service
             :type description_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param choice_id: ID selected in the corresponding column
             :type choice_id: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("describe"), kwargs)
