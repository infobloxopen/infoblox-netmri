from ..broker import Broker


class JobBroker(Broker):
    controller = "jobs"

    def index(self, **kwargs):
        """Lists the available jobs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobID: The internal NetMRI identifier for this job.
             :type JobID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this job.
             :type id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this job, as entered when the job specification was defined, or when the job was executed from a script.
             :type name: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param started_at: The time this job started execution.
             :type started_at: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job methods. The listed methods will be called on each job returned and included in the output. Available methods are: meta.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
             :type include: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id.
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

             :param select: The list of attributes to return for each Job. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id. If empty or omitted, all attributes will be returned.
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

             :return jobs: An array of the Job objects that match the specified input criteria.
             :rtype jobs: Array of Job

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this job.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job methods. The listed methods will be called on each job returned and included in the output. Available methods are: meta.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job: The job identified by the specified id.
             :rtype job: Job

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available jobs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approval_note: The approval note.
             :type approval_note: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approval_note: The approval note.
             :type approval_note: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_at: The time when the job was approved.
             :type approved_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_at: The time when the job was approved.
             :type approved_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user that approved the job.
             :type approved_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user that approved the job.
             :type approved_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param category: The job category.
             :type category: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: The job category.
             :type category: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param completed_at: The time this job completed execution against all devices.
             :type completed_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param completed_at: The time this job completed execution against all devices.
             :type completed_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: The internal identifier for the config template.
             :type config_template_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: The internal identifier for the config template.
             :type config_template_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_text: The content of the config template.
             :type config_template_text: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_text: The content of the config template.
             :type config_template_text: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The time when the job was created.
             :type created_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The time when the job was created.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user that created the job.
             :type created_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user that created the job.
             :type created_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param credential_source: The source of a device credential.
             :type credential_source: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param credential_source: The source of a device credential.
             :type credential_source: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param description: The description of the job.
             :type description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: The description of the job.
             :type description: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this job.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this job.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param input_data: The input data for the job.
             :type input_data: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param input_data: The input data for the job.
             :type input_data: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal identifier for the associated Job Specification.
             :type job_specification_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal identifier for the associated Job Specification.
             :type job_specification_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The type of job. This can be Scheduled, Ad Hoc, or Run Now.
             :type job_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The type of job. This can be Scheduled, Ad Hoc, or Run Now.
             :type job_type: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_status_at: The time when the job status was updated.
             :type last_status_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_status_at: The time when the job status was updated.
             :type last_status_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this job, as entered when the job specification was defined, or when the job was executed from a script.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this job, as entered when the job specification was defined, or when the job was executed from a script.
             :type name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param provision_data: Internal data for provisioning jobs.
             :type provision_data: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param provision_data: Internal data for provisioning jobs.
             :type provision_data: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param run_as: The user that run the job.
             :type run_as: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param run_as: The user that run the job.
             :type run_as: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal identifier for the script.
             :type script_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal identifier for the script.
             :type script_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param script_language: The language of the script.
             :type script_language: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_language: The language of the script.
             :type script_language: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param script_text: The content of the script.
             :type script_text: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_text: The content of the script.
             :type script_text: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param started_at: The time this job started execution.
             :type started_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param started_at: The time this job started execution.
             :type started_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param status: The current status of this job, based upon all of the statuses for each device in the job.
             :type status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The current status of this job, based upon all of the statuses for each device in the job.
             :type status: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_revert: The internal workflow name for job reversion using the script.
             :type taskflow_revert: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param taskflow_revert: The internal workflow name for job reversion using the script.
             :type taskflow_revert: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating if devices should be reserved during execution of this job.
             :type transactional_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating if devices should be reserved during execution of this job.
             :type transactional_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The time when the job was updated.
             :type updated_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The time when the job was updated.
             :type updated_at: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job methods. The listed methods will be called on each job returned and included in the output. Available methods are: meta.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
             :type include: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id.
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

             :param select: The list of attributes to return for each Job. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against jobs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: approval_note, approved_at, approved_by, category, completed_at, config_template_id, config_template_text, created_at, created_by, credential_source, description, id, input_data, job_specification_id, job_type, last_status_at, name, provision_data, run_as, script_id, script_language, script_text, started_at, status, taskflow_revert, transactional_ind, updated_at.
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

             :return jobs: An array of the Job objects that match the specified input criteria.
             :rtype jobs: Array of Job

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available jobs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: approval_note, approved_at, approved_by, category, completed_at, config_template_id, config_template_text, created_at, created_by, credential_source, description, id, input_data, job_specification_id, job_type, last_status_at, name, provision_data, run_as, script_id, script_language, script_text, started_at, status, taskflow_revert, transactional_ind, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_approval_note: The operator to apply to the field approval_note. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approval_note: The approval note. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_approval_note: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_approval_note: If op_approval_note is specified, the field named in this input will be compared to the value in approval_note using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_approval_note must be specified if op_approval_note is specified.
             :type val_f_approval_note: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_approval_note: If op_approval_note is specified, this value will be compared to the value in approval_note using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_approval_note must be specified if op_approval_note is specified.
             :type val_c_approval_note: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_approved_at: The operator to apply to the field approved_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approved_at: The time when the job was approved. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_approved_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_approved_at: If op_approved_at is specified, the field named in this input will be compared to the value in approved_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_approved_at must be specified if op_approved_at is specified.
             :type val_f_approved_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_approved_at: If op_approved_at is specified, this value will be compared to the value in approved_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_approved_at must be specified if op_approved_at is specified.
             :type val_c_approved_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_approved_by: The operator to apply to the field approved_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approved_by: The user that approved the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_approved_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_approved_by: If op_approved_by is specified, the field named in this input will be compared to the value in approved_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_approved_by must be specified if op_approved_by is specified.
             :type val_f_approved_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_approved_by: If op_approved_by is specified, this value will be compared to the value in approved_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_approved_by must be specified if op_approved_by is specified.
             :type val_c_approved_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: The job category. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_completed_at: The operator to apply to the field completed_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. completed_at: The time this job completed execution against all devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_completed_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_completed_at: If op_completed_at is specified, the field named in this input will be compared to the value in completed_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_completed_at must be specified if op_completed_at is specified.
             :type val_f_completed_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_completed_at: If op_completed_at is specified, this value will be compared to the value in completed_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_completed_at must be specified if op_completed_at is specified.
             :type val_c_completed_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_config_template_id: The operator to apply to the field config_template_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. config_template_id: The internal identifier for the config template. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_config_template_text: The operator to apply to the field config_template_text. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. config_template_text: The content of the config template. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_config_template_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_config_template_text: If op_config_template_text is specified, the field named in this input will be compared to the value in config_template_text using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_config_template_text must be specified if op_config_template_text is specified.
             :type val_f_config_template_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_config_template_text: If op_config_template_text is specified, this value will be compared to the value in config_template_text using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_config_template_text must be specified if op_config_template_text is specified.
             :type val_c_config_template_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The time when the job was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: The user that created the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_credential_source: The operator to apply to the field credential_source. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. credential_source: The source of a device credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_credential_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_credential_source: If op_credential_source is specified, the field named in this input will be compared to the value in credential_source using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_credential_source must be specified if op_credential_source is specified.
             :type val_f_credential_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_credential_source: If op_credential_source is specified, this value will be compared to the value in credential_source using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_credential_source must be specified if op_credential_source is specified.
             :type val_c_credential_source: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: The description of the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_input_data: The operator to apply to the field input_data. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. input_data: The input data for the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_input_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_input_data: If op_input_data is specified, the field named in this input will be compared to the value in input_data using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_input_data must be specified if op_input_data is specified.
             :type val_f_input_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_input_data: If op_input_data is specified, this value will be compared to the value in input_data using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_input_data must be specified if op_input_data is specified.
             :type val_c_input_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_specification_id: The operator to apply to the field job_specification_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_specification_id: The internal identifier for the associated Job Specification. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_type: The operator to apply to the field job_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_type: The type of job. This can be Scheduled, Ad Hoc, or Run Now. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_last_status_at: The operator to apply to the field last_status_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_status_at: The time when the job status was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_status_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_status_at: If op_last_status_at is specified, the field named in this input will be compared to the value in last_status_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_status_at must be specified if op_last_status_at is specified.
             :type val_f_last_status_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_status_at: If op_last_status_at is specified, this value will be compared to the value in last_status_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_status_at must be specified if op_last_status_at is specified.
             :type val_c_last_status_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of this job, as entered when the job specification was defined, or when the job was executed from a script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_provision_data: The operator to apply to the field provision_data. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. provision_data: Internal data for provisioning jobs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_provision_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_provision_data: If op_provision_data is specified, the field named in this input will be compared to the value in provision_data using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_provision_data must be specified if op_provision_data is specified.
             :type val_f_provision_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_provision_data: If op_provision_data is specified, this value will be compared to the value in provision_data using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_provision_data must be specified if op_provision_data is specified.
             :type val_c_provision_data: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_run_as: The operator to apply to the field run_as. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. run_as: The user that run the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_run_as: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_run_as: If op_run_as is specified, the field named in this input will be compared to the value in run_as using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_run_as must be specified if op_run_as is specified.
             :type val_f_run_as: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_run_as: If op_run_as is specified, this value will be compared to the value in run_as using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_run_as must be specified if op_run_as is specified.
             :type val_c_run_as: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_script_id: The operator to apply to the field script_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script_id: The internal identifier for the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_script_language: The operator to apply to the field script_language. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script_language: The language of the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_script_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_script_language: If op_script_language is specified, the field named in this input will be compared to the value in script_language using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_script_language must be specified if op_script_language is specified.
             :type val_f_script_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_script_language: If op_script_language is specified, this value will be compared to the value in script_language using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_script_language must be specified if op_script_language is specified.
             :type val_c_script_language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_script_text: The operator to apply to the field script_text. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script_text: The content of the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_script_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_script_text: If op_script_text is specified, the field named in this input will be compared to the value in script_text using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_script_text must be specified if op_script_text is specified.
             :type val_f_script_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_script_text: If op_script_text is specified, this value will be compared to the value in script_text using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_script_text must be specified if op_script_text is specified.
             :type val_c_script_text: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_started_at: The operator to apply to the field started_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. started_at: The time this job started execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_started_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_started_at: If op_started_at is specified, the field named in this input will be compared to the value in started_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_started_at must be specified if op_started_at is specified.
             :type val_f_started_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_started_at: If op_started_at is specified, this value will be compared to the value in started_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_started_at must be specified if op_started_at is specified.
             :type val_c_started_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The current status of this job, based upon all of the statuses for each device in the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_taskflow_revert: The operator to apply to the field taskflow_revert. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. taskflow_revert: The internal workflow name for job reversion using the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_transactional_ind: The operator to apply to the field transactional_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. transactional_ind: Flag indicating if devices should be reserved during execution of this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The time when the job was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param methods: A list of job methods. The listed methods will be called on each job returned and included in the output. Available methods are: meta.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
             :type include: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id.
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

             :param select: The list of attributes to return for each Job. Valid values are id, name, category, job_type, taskflow_revert, script_id, config_template_id, description, created_by, run_as, credential_source, approved_by, approval_note, provision_data, input_data, transactional_ind, status, last_status_at, started_at, completed_at, created_at, updated_at, approved_at, script_text, script_language, config_template_text, job_specification_id. If empty or omitted, all attributes will be returned.
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

             :return jobs: An array of the Job objects that match the specified input criteria.
             :rtype jobs: Array of Job

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def script(self, **kwargs):
        """Downloads the script that ran on each device in a job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to download the script file for.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return script: The script file contents ran on each device in a job. It will be presented as type "application/octet-stream".
             :rtype script: String

            """

        return self.api_mixed_request(self._get_method_fullname("script"), kwargs)

    def issues(self, **kwargs):
        """List any issues associated with the specified job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param JobID: The id of the job to list.
             :type JobID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return as the first record.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The maximum number of records to return.
             :type limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return issue_details: An array of the IssueDetail objects that match the specified input criteria.
             :rtype issue_details: Array of IssueDetail

            """

        return self.api_list_request(self._get_method_fullname("issues"), kwargs)

    def job_files(self, **kwargs):
        """Lists/downloads common files for a job. If no filename is given, a list of files for the job will be returned. If a filename is passed, and it exists, it will be downloaded as type "application/octet-stream".

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to list files for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: An optional filename to download.
             :type filename: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return filenames: An array of filenames that match the specified input criteria.
             :rtype filenames: Array of String

            """

        return self.api_mixed_request(self._get_method_fullname("job_files"), kwargs)

    def job_archive(self, **kwargs):
        """Downloads zip archive of whole job or job process.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to list files for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param started_at: The job started at date
             :type started_at: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param process_id: The job process id to list files for.
             :type process_id: Integer

            **Outputs**

            """

        return self.api_mixed_request(self._get_method_fullname("job_archive"), kwargs)

    def log_message(self, **kwargs):
        """Logs a message to custom log and session log

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobID: The id of the job.
             :type JobID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param process_id: The id of the job process.
             :type process_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param severity: The severity of the message.
             :type severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message: A message describing the results.
             :type message: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("log_message"), kwargs)

    def log_custom_message(self, **kwargs):
        """Logs a message to custom log

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobID: The id of the job.
             :type JobID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobDetailID: The id of the individual device job.
             :type JobDetailID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param severity: The severity of the message.
             :type severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message: A message describing the results.
             :type message: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("log_custom_message"), kwargs)

    def cancel(self, **kwargs):
        """Cancel the execution of a job or a process

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the job to cancel.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param process_id: The id of the process to cancel.
             :type process_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel"), kwargs)
