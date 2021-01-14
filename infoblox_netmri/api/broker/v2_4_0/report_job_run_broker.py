from ..broker import Broker


class ReportJobRunBroker(Broker):
    controller = "report_job_runs"

    def index(self, **kwargs):
        """Lists the available report job runs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the report job.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the report job.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size.
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

             :param select: The list of attributes to return for each ReportJobRun. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size. If empty or omitted, all attributes will be returned.
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

             :return report_job_runs: An array of the ReportJobRun objects that match the specified input criteria.
             :rtype report_job_runs: Array of ReportJobRun

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified report job run from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the report job.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def search(self, **kwargs):
        """Lists the available report job runs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param auth_user_id: The internal NetMRI user id that created the Report Job.
             :type auth_user_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_user_id: The internal NetMRI user id that created the Report Job.
             :type auth_user_id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param cancel_time: The date and time the report job was canceled.
             :type cancel_time: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cancel_time: The date and time the report job was canceled.
             :type cancel_time: Array of DateTime

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the report job was created.
             :type created_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the report job was created.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ext_job_id: The system process id for the report job.
             :type ext_job_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ext_job_id: The system process id for the report job.
             :type ext_job_id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the report job.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the report job.
             :type id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param is_foreground: Value to indicate the report is being run in the NetMRI GUI.
             :type is_foreground: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param is_foreground: Value to indicate the report is being run in the NetMRI GUI.
             :type is_foreground: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param job_priority: The report job priority, lower priority are processed first.
             :type job_priority: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_priority: The report job priority, lower priority are processed first.
             :type job_priority: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_checkin: The date and time the report job last changed status.
             :type last_checkin: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_checkin: The date and time the report job last changed status.
             :type last_checkin: Array of DateTime

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param report_id: The internal NetMRI identifier for a specific report.
             :type report_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param report_id: The internal NetMRI identifier for a specific report.
             :type report_id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param report_job_specification_id: The internal NetMRI identifier for the associated Report Job Specification.
             :type report_job_specification_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param report_job_specification_id: The internal NetMRI identifier for the associated Report Job Specification.
             :type report_job_specification_id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param report_type: The report job type to indicate if a report was scheduled or run on demand.
             :type report_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param report_type: The report job type to indicate if a report was scheduled or run on demand.
             :type report_type: Array of String

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param size: The file size of a completed report.
             :type size: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param size: The file size of a completed report.
             :type size: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param start_time: The date and time the report job started running.
             :type start_time: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_time: The date and time the report job started running.
             :type start_time: Array of DateTime

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param status: The report running status.
             :type status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The report running status.
             :type status: Array of String

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the report job was updated.
             :type updated_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the report job was updated.
             :type updated_at: Array of DateTime

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size.
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

             :param select: The list of attributes to return for each ReportJobRun. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against report job runs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: auth_user_id, cancel_time, created_at, ext_job_id, id, is_foreground, job_priority, last_checkin, report_id, report_job_specification_id, report_type, size, start_time, status, updated_at.
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

             :return report_job_runs: An array of the ReportJobRun objects that match the specified input criteria.
             :rtype report_job_runs: Array of ReportJobRun

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available report job runs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: auth_user_id, cancel_time, created_at, ext_job_id, id, is_foreground, job_priority, last_checkin, report_id, report_job_specification_id, report_type, size, start_time, status, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_user_id: The operator to apply to the field auth_user_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_user_id: The internal NetMRI user id that created the Report Job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_user_id: If op_auth_user_id is specified, the field named in this input will be compared to the value in auth_user_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_user_id must be specified if op_auth_user_id is specified.
             :type val_f_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_user_id: If op_auth_user_id is specified, this value will be compared to the value in auth_user_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_user_id must be specified if op_auth_user_id is specified.
             :type val_c_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cancel_time: The operator to apply to the field cancel_time. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cancel_time: The date and time the report job was canceled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cancel_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cancel_time: If op_cancel_time is specified, the field named in this input will be compared to the value in cancel_time using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cancel_time must be specified if op_cancel_time is specified.
             :type val_f_cancel_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cancel_time: If op_cancel_time is specified, this value will be compared to the value in cancel_time using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cancel_time must be specified if op_cancel_time is specified.
             :type val_c_cancel_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the report job was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ext_job_id: The operator to apply to the field ext_job_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ext_job_id: The system process id for the report job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ext_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ext_job_id: If op_ext_job_id is specified, the field named in this input will be compared to the value in ext_job_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ext_job_id must be specified if op_ext_job_id is specified.
             :type val_f_ext_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ext_job_id: If op_ext_job_id is specified, this value will be compared to the value in ext_job_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ext_job_id must be specified if op_ext_job_id is specified.
             :type val_c_ext_job_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the report job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_is_foreground: The operator to apply to the field is_foreground. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. is_foreground: Value to indicate the report is being run in the NetMRI GUI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_is_foreground: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_is_foreground: If op_is_foreground is specified, the field named in this input will be compared to the value in is_foreground using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_is_foreground must be specified if op_is_foreground is specified.
             :type val_f_is_foreground: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_is_foreground: If op_is_foreground is specified, this value will be compared to the value in is_foreground using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_is_foreground must be specified if op_is_foreground is specified.
             :type val_c_is_foreground: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_priority: The operator to apply to the field job_priority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_priority: The report job priority, lower priority are processed first. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_job_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_job_priority: If op_job_priority is specified, the field named in this input will be compared to the value in job_priority using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_job_priority must be specified if op_job_priority is specified.
             :type val_f_job_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_job_priority: If op_job_priority is specified, this value will be compared to the value in job_priority using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_job_priority must be specified if op_job_priority is specified.
             :type val_c_job_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_last_checkin: The operator to apply to the field last_checkin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_checkin: The date and time the report job last changed status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_checkin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_checkin: If op_last_checkin is specified, the field named in this input will be compared to the value in last_checkin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_checkin must be specified if op_last_checkin is specified.
             :type val_f_last_checkin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_checkin: If op_last_checkin is specified, this value will be compared to the value in last_checkin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_checkin must be specified if op_last_checkin is specified.
             :type val_c_last_checkin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_report_id: The operator to apply to the field report_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. report_id: The internal NetMRI identifier for a specific report. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_report_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_report_id: If op_report_id is specified, the field named in this input will be compared to the value in report_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_report_id must be specified if op_report_id is specified.
             :type val_f_report_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_report_id: If op_report_id is specified, this value will be compared to the value in report_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_report_id must be specified if op_report_id is specified.
             :type val_c_report_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_report_job_specification_id: The operator to apply to the field report_job_specification_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. report_job_specification_id: The internal NetMRI identifier for the associated Report Job Specification. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_report_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_report_job_specification_id: If op_report_job_specification_id is specified, the field named in this input will be compared to the value in report_job_specification_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_report_job_specification_id must be specified if op_report_job_specification_id is specified.
             :type val_f_report_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_report_job_specification_id: If op_report_job_specification_id is specified, this value will be compared to the value in report_job_specification_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_report_job_specification_id must be specified if op_report_job_specification_id is specified.
             :type val_c_report_job_specification_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_report_type: The operator to apply to the field report_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. report_type: The report job type to indicate if a report was scheduled or run on demand. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_report_type: If op_report_type is specified, the field named in this input will be compared to the value in report_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_report_type must be specified if op_report_type is specified.
             :type val_f_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_report_type: If op_report_type is specified, this value will be compared to the value in report_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_report_type must be specified if op_report_type is specified.
             :type val_c_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_size: The operator to apply to the field size. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. size: The file size of a completed report. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_size: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_size: If op_size is specified, the field named in this input will be compared to the value in size using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_size must be specified if op_size is specified.
             :type val_f_size: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_size: If op_size is specified, this value will be compared to the value in size using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_size must be specified if op_size is specified.
             :type val_c_size: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_start_time: The operator to apply to the field start_time. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. start_time: The date and time the report job started running. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_start_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_start_time: If op_start_time is specified, the field named in this input will be compared to the value in start_time using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_start_time must be specified if op_start_time is specified.
             :type val_f_start_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_start_time: If op_start_time is specified, this value will be compared to the value in start_time using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_start_time must be specified if op_start_time is specified.
             :type val_c_start_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The report running status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the report job was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size.
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

             :param select: The list of attributes to return for each ReportJobRun. Valid values are id, report_id, ext_job_id, auth_user_id, status, start_time, is_foreground, last_checkin, cancel_time, created_at, updated_at, report_type, job_priority, report_job_specification_id, size. If empty or omitted, all attributes will be returned.
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

             :return report_job_runs: An array of the ReportJobRun objects that match the specified input criteria.
             :rtype report_job_runs: Array of ReportJobRun

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def cancel(self, **kwargs):
        """Cancels running or pending reports.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: One or more ReportJobID values indicating the reports to cancel
             :type id: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel"), kwargs)

    def run_in_background(self, **kwargs):
        """Run reports in background.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: One or more ReportJobID values indicating the reports to run in the background.
             :type id: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("run_in_background"), kwargs)

    def delete(self, **kwargs):
        """Deletes reports that have been canceled or completed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: One or more ReportJobID values indicating the reports to cancel
             :type id: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)

    def run_next(self, **kwargs):
        """Increases a report jobs priority to the highest pending job

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: One or more ReportJobID values indicating the reports to run next
             :type id: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("run_next"), kwargs)

    def show(self, **kwargs):
        """Shows ReportJob details

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: ReportJobID value indicating the report
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job: A Report Job object that matches the specified input criteria.
             :rtype job: Array of ReportJobRun

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return queue_size: Total number of active report jobs
             :rtype queue_size: Integer

            """

        return self.api_list_request(self._get_method_fullname("show"), kwargs)
