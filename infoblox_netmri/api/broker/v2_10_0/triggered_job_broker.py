from ..broker import Broker


class TriggeredJobBroker(Broker):
    controller = "triggered_jobs"

    def index(self, **kwargs):
        """Lists the available triggered jobs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by.
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

             :param select: The list of attributes to return for each TriggeredJob. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by. If empty or omitted, all attributes will be returned.
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

             :return triggered_jobs: An array of the TriggeredJob objects that match the specified input criteria.
             :rtype triggered_jobs: Array of TriggeredJob

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified triggered job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the triggered job.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return triggered_job: The triggered job identified by the specified id.
             :rtype triggered_job: TriggeredJob

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available triggered jobs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param action_auto: No description is available for action_auto.
             :type action_auto: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param action_preapprove: No description is available for action_preapprove.
             :type action_preapprove: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: No description is available for config_template_id.
             :type config_template_id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: No description is available for created_at.
             :type created_at: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: No description is available for created_by.
             :type created_by: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cron: No description is available for cron.
             :type cron: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: No description is available for description.
             :type description: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled: No description is available for enabled.
             :type enabled: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: No description is available for job_type.
             :type job_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_run: No description is available for last_run.
             :type last_run: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: No description is available for name.
             :type name: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: No description is available for script_id.
             :type script_id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source: No description is available for source.
             :type source: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: No description is available for updated_at.
             :type updated_at: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: No description is available for updated_by.
             :type updated_by: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by.
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

             :param select: The list of attributes to return for each TriggeredJob. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against triggered jobs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: action_auto, action_preapprove, config_template_id, created_at, created_by, cron, description, enabled, id, job_type, last_run, name, script_id, source, updated_at, updated_by.
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

             :return triggered_jobs: An array of the TriggeredJob objects that match the specified input criteria.
             :rtype triggered_jobs: Array of TriggeredJob

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available triggered jobs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: action_auto, action_preapprove, config_template_id, created_at, created_by, cron, description, enabled, id, job_type, last_run, name, script_id, source, updated_at, updated_by.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_action_auto: The operator to apply to the field action_auto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. action_auto: No description is available for action_auto. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_action_auto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_action_auto: If op_action_auto is specified, the field named in this input will be compared to the value in action_auto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_action_auto must be specified if op_action_auto is specified.
             :type val_f_action_auto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_action_auto: If op_action_auto is specified, this value will be compared to the value in action_auto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_action_auto must be specified if op_action_auto is specified.
             :type val_c_action_auto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_action_preapprove: The operator to apply to the field action_preapprove. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. action_preapprove: No description is available for action_preapprove. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_action_preapprove: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_action_preapprove: If op_action_preapprove is specified, the field named in this input will be compared to the value in action_preapprove using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_action_preapprove must be specified if op_action_preapprove is specified.
             :type val_f_action_preapprove: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_action_preapprove: If op_action_preapprove is specified, this value will be compared to the value in action_preapprove using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_action_preapprove must be specified if op_action_preapprove is specified.
             :type val_c_action_preapprove: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_config_template_id: The operator to apply to the field config_template_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. config_template_id: No description is available for config_template_id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_config_template_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_config_template_id: If op_config_template_id is specified, the field named in this input will be compared to the value in config_template_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_config_template_id must be specified if op_config_template_id is specified.
             :type val_f_config_template_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_config_template_id: If op_config_template_id is specified, this value will be compared to the value in config_template_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_config_template_id must be specified if op_config_template_id is specified.
             :type val_c_config_template_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: No description is available for created_at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: No description is available for created_by. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cron: The operator to apply to the field cron. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cron: No description is available for cron. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cron: If op_cron is specified, the field named in this input will be compared to the value in cron using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cron must be specified if op_cron is specified.
             :type val_f_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cron: If op_cron is specified, this value will be compared to the value in cron using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cron must be specified if op_cron is specified.
             :type val_c_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: No description is available for description. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_enabled: The operator to apply to the field enabled. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. enabled: No description is available for enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_enabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_enabled: If op_enabled is specified, the field named in this input will be compared to the value in enabled using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_enabled must be specified if op_enabled is specified.
             :type val_f_enabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_enabled: If op_enabled is specified, this value will be compared to the value in enabled using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_enabled must be specified if op_enabled is specified.
             :type val_c_enabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: No description is available for id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_type: The operator to apply to the field job_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_type: No description is available for job_type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_job_type: If op_job_type is specified, the field named in this input will be compared to the value in job_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_job_type must be specified if op_job_type is specified.
             :type val_f_job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_job_type: If op_job_type is specified, this value will be compared to the value in job_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_job_type must be specified if op_job_type is specified.
             :type val_c_job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_last_run: The operator to apply to the field last_run. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_run: No description is available for last_run. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_run: If op_last_run is specified, the field named in this input will be compared to the value in last_run using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_run must be specified if op_last_run is specified.
             :type val_f_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_run: If op_last_run is specified, this value will be compared to the value in last_run using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_run must be specified if op_last_run is specified.
             :type val_c_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: No description is available for name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_script_id: The operator to apply to the field script_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script_id: No description is available for script_id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_script_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_script_id: If op_script_id is specified, the field named in this input will be compared to the value in script_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_script_id must be specified if op_script_id is specified.
             :type val_f_script_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_script_id: If op_script_id is specified, this value will be compared to the value in script_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_script_id must be specified if op_script_id is specified.
             :type val_c_script_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_source: The operator to apply to the field source. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. source: No description is available for source. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_source: If op_source is specified, the field named in this input will be compared to the value in source using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_source must be specified if op_source is specified.
             :type val_f_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_source: If op_source is specified, this value will be compared to the value in source using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_source must be specified if op_source is specified.
             :type val_c_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: No description is available for updated_at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_by: The operator to apply to the field updated_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_by: No description is available for updated_by. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by.
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

             :param select: The list of attributes to return for each TriggeredJob. Valid values are id, name, description, enabled, script_id, source, action_auto, cron, action_preapprove, last_run, created_at, updated_at, config_template_id, job_type, created_by, updated_by. If empty or omitted, all attributes will be returned.
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

             :return triggered_jobs: An array of the TriggeredJob objects that match the specified input criteria.
             :rtype triggered_jobs: Array of TriggeredJob

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified triggered job from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the triggered job.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Create a triggered job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The triggered job name.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param job_type: The type of the job: script, template.
             :type job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param source: The ID of trigger source: 1 - Policy Rule, 2 - Issue, 3 - IFMAP Subscription.
             :type source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: The triggered job description to contain detailed information about the job.
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` on

             :param enabled: The flag to turn on/off the triggered job.
             :type enabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` false

             :param action_preapprove: Indicates whether or not this job is approved.
             :type action_preapprove: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param active_window_id: Active Time Window: 1 - "24/7", 2 - "Work Hours (M-F 8am-6pm)", 3 - "Off Hours (M-F 6pm-8am, Sat, Sun)", 4 - "First Shift (M-F 12am-8am)", 5 - "Second Shift (M-F 8am-4pm)", 6 - "Third Shift (M-F 4pm-12am)", 7 - "Weekends (Sat/Sun)"
             :type active_window_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param run_at_hour: The schedule time to run the job (Format: "6:00 AM").
             :type run_at_hour: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param run_at_day_id: The week day number (0-6).
             :type run_at_day_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` bulk

             :param push_mode: Defines the push mode (bulk or line_by_line) used for template based jobs.
             :type push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param action_auto: 0 - run by schedule, 1 - auto-run.
             :type action_auto: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` [u'0']

             :param device_group_ids: A comma delimited list of device groups against which to run the specified job.
             :type device_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` [u'0']

             :param interface_group_ids: A comma delimited list of interface groups against which to run the specified job.
             :type interface_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_name: The script name.
             :type script_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param template_id: The internal NetMRI identifier for the template.
             :type template_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script.
             :type script_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param rule_id: The internal NetMRI identifier for the Policy Rule.
             :type rule_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for the Issue type.
             :type IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 3

             :param severity_id: The severity of the issue.
             :type severity_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifmap_subscription_id: The internal NetMRI identifier for the ifmap subscription.
             :type ifmap_subscription_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Update a triggered job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the triggered job.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The triggered job name.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The type of the job: script, template.
             :type job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source: The ID of trigger source: 1 - Policy Rule, 2 - Issue, 3 - IFMAP Subscription.
             :type source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: The triggered job description to contain detailed information about the job.
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` on

             :param enabled: The flag to turn on/off the triggered job.
             :type enabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` false

             :param action_preapprove: Indicates whether or not this job is approved.
             :type action_preapprove: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param active_window_id: Active Time Window: 1 - "24/7", 2 - "Work Hours (M-F 8am-6pm)", 3 - "Off Hours (M-F 6pm-8am, Sat, Sun)", 4 - "First Shift (M-F 12am-8am)", 5 - "Second Shift (M-F 8am-4pm)", 6 - "Third Shift (M-F 4pm-12am)", 7 - "Weekends (Sat/Sun)"
             :type active_window_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param run_at_hour: The schedule time to run the job (Format: "6:00 AM").
             :type run_at_hour: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param run_at_day_id: The week day number (0-6).
             :type run_at_day_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param action_auto: 0 - run by schedule, 1 - auto-run.
             :type action_auto: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` bulk

             :param push_mode: Defines the push mode (bulk or line_by_line) used for template based jobs.
             :type push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A comma delimited list of device groups against which to run the specified job.
             :type device_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interface_group_ids: A comma delimited list of interface groups against which to run the specified job.
             :type interface_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_name: The script name.
             :type script_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param template_id: The internal NetMRI identifier for the template.
             :type template_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script.
             :type script_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param rule_id: The internal NetMRI identifier for the Policy Rule.
             :type rule_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for the Issue type.
             :type IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param severity_id: The severity of the issue.
             :type severity_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifmap_subscription_id: The internal NetMRI identifier for the ifmap subscription.
             :type ifmap_subscription_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)
