from ..broker import Broker


class JobSpecificationBroker(Broker):
    controller = "job_specifications"

    def index(self, **kwargs):
        """Lists the available job specifications. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
             :type name: Array of String

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user id of the user that approved this job.
             :type approved_by: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user id of the user that approved this job.
             :type approved_by: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job specification methods. The listed methods will be called on each job specification returned and included in the output. Available methods are: meta.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script.
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

             :param select: The list of attributes to return for each JobSpecification. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script. If empty or omitted, all attributes will be returned.
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

             :return job_specifications: An array of the JobSpecification objects that match the specified input criteria.
             :rtype job_specifications: Array of JobSpecification

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified job specification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job specification methods. The listed methods will be called on each job specification returned and included in the output. Available methods are: meta.
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

             :return job_specification: The job specification identified by the specified id.
             :rtype job_specification: JobSpecification

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available job specifications matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approval_note: The comment associated to the approval.
             :type approval_note: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approval_note: The comment associated to the approval.
             :type approval_note: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user id of the user that approved this job.
             :type approved_by: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by: The user id of the user that approved this job.
             :type approved_by: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by_name: Name of the approver for this job.
             :type approved_by_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_by_name: Name of the approver for this job.
             :type approved_by_name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param approved_timestamp: The date/time of the approval.
             :type approved_timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved_timestamp: The date/time of the approval.
             :type approved_timestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param category: The category of this job.
             :type category: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: The category of this job.
             :type category: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: The internal NetMRI identifier for the associated Configuration Template.
             :type config_template_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: The internal NetMRI identifier for the associated Configuration Template.
             :type config_template_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date/time that this job specification was created.
             :type created_at: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date/time that this job specification was created.
             :type created_at: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user name of the user that created this job.
             :type created_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user name of the user that created this job.
             :type created_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param deployable_ind: Flag indicating that job must deploy the uploaded rules on firewalls.
             :type deployable_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param deployable_ind: Flag indicating that job must deploy the uploaded rules on firewalls.
             :type deployable_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param description: The description of the job as entered when creating the job.
             :type description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: The description of the job as entered when creating the job.
             :type description: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The base type of the job ('script' or 'template').
             :type job_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The base type of the job ('script' or 'template').
             :type job_type: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_run: Last run start time
             :type last_run: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_run: Last run start time
             :type last_run: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
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

             :param push_mode: Defines the push mode (bulk or line by line) used for template based jobs.
             :type push_mode: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param push_mode: Defines the push mode (bulk or line by line) used for template based jobs.
             :type push_mode: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param revertable_ind: Flag indicating that when failed, job must revert the already processed operations.
             :type revertable_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param revertable_ind: Flag indicating that when failed, job must revert the already processed operations.
             :type revertable_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param schedule: The job schedule, in cron format.
             :type schedule: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule: The job schedule, in cron format.
             :type schedule: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param script: Script name used in netmri.details_from_jobs view
             :type script: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script: Script name used in netmri.details_from_jobs view
             :type script: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script associated with this job.
             :type script_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script associated with this job.
             :type script_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating that the job needs to be executed in a transaction.
             :type transactional_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param transactional_ind: Flag indicating that the job needs to be executed in a transaction.
             :type transactional_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param unapproved_notification_trigger: Flag that defines if approval status has changed.
             :type unapproved_notification_trigger: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unapproved_notification_trigger: Flag that defines if approval status has changed.
             :type unapproved_notification_trigger: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date/time that this job specification was last updated.
             :type updated_at: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date/time that this job specification was last updated.
             :type updated_at: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job specification methods. The listed methods will be called on each job specification returned and included in the output. Available methods are: meta.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script.
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

             :param select: The list of attributes to return for each JobSpecification. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against job specifications, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: approval_note, approved_by, approved_by_name, approved_timestamp, category, config_template_id, created_at, created_by, deployable_ind, description, id, job_type, last_run, name, provision_data, push_mode, revertable_ind, schedule, script, script_id, transactional_ind, unapproved_notification_trigger, updated_at.
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

             :return job_specifications: An array of the JobSpecification objects that match the specified input criteria.
             :rtype job_specifications: Array of JobSpecification

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available job specifications matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: approval_note, approved_by, approved_by_name, approved_timestamp, category, config_template_id, created_at, created_by, deployable_ind, description, id, job_type, last_run, name, provision_data, push_mode, revertable_ind, schedule, script, script_id, transactional_ind, unapproved_notification_trigger, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_approval_note: The operator to apply to the field approval_note. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approval_note: The comment associated to the approval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_approved_by: The operator to apply to the field approved_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approved_by: The user id of the user that approved this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_approved_by_name: The operator to apply to the field approved_by_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approved_by_name: Name of the approver for this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_approved_by_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_approved_by_name: If op_approved_by_name is specified, the field named in this input will be compared to the value in approved_by_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_approved_by_name must be specified if op_approved_by_name is specified.
             :type val_f_approved_by_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_approved_by_name: If op_approved_by_name is specified, this value will be compared to the value in approved_by_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_approved_by_name must be specified if op_approved_by_name is specified.
             :type val_c_approved_by_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_approved_timestamp: The operator to apply to the field approved_timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. approved_timestamp: The date/time of the approval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_approved_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_approved_timestamp: If op_approved_timestamp is specified, the field named in this input will be compared to the value in approved_timestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_approved_timestamp must be specified if op_approved_timestamp is specified.
             :type val_f_approved_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_approved_timestamp: If op_approved_timestamp is specified, this value will be compared to the value in approved_timestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_approved_timestamp must be specified if op_approved_timestamp is specified.
             :type val_c_approved_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: The category of this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_config_template_id: The operator to apply to the field config_template_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. config_template_id: The internal NetMRI identifier for the associated Configuration Template. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date/time that this job specification was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: The user name of the user that created this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_deployable_ind: The operator to apply to the field deployable_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. deployable_ind: Flag indicating that job must deploy the uploaded rules on firewalls. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_deployable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_deployable_ind: If op_deployable_ind is specified, the field named in this input will be compared to the value in deployable_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_deployable_ind must be specified if op_deployable_ind is specified.
             :type val_f_deployable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_deployable_ind: If op_deployable_ind is specified, this value will be compared to the value in deployable_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_deployable_ind must be specified if op_deployable_ind is specified.
             :type val_c_deployable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: The description of the job as entered when creating the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the job specification. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_type: The operator to apply to the field job_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_type: The base type of the job ('script' or 'template'). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_last_run: The operator to apply to the field last_run. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_run: Last run start time For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The job name as entered when creating the job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_push_mode: The operator to apply to the field push_mode. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. push_mode: Defines the push mode (bulk or line by line) used for template based jobs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_push_mode: If op_push_mode is specified, the field named in this input will be compared to the value in push_mode using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_push_mode must be specified if op_push_mode is specified.
             :type val_f_push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_push_mode: If op_push_mode is specified, this value will be compared to the value in push_mode using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_push_mode must be specified if op_push_mode is specified.
             :type val_c_push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_revertable_ind: The operator to apply to the field revertable_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. revertable_ind: Flag indicating that when failed, job must revert the already processed operations. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_revertable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_revertable_ind: If op_revertable_ind is specified, the field named in this input will be compared to the value in revertable_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_revertable_ind must be specified if op_revertable_ind is specified.
             :type val_f_revertable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_revertable_ind: If op_revertable_ind is specified, this value will be compared to the value in revertable_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_revertable_ind must be specified if op_revertable_ind is specified.
             :type val_c_revertable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_schedule: The operator to apply to the field schedule. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. schedule: The job schedule, in cron format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_schedule: If op_schedule is specified, the field named in this input will be compared to the value in schedule using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_schedule must be specified if op_schedule is specified.
             :type val_f_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_schedule: If op_schedule is specified, this value will be compared to the value in schedule using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_schedule must be specified if op_schedule is specified.
             :type val_c_schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_script: The operator to apply to the field script. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script: Script name used in netmri.details_from_jobs view For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_script: If op_script is specified, the field named in this input will be compared to the value in script using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_script must be specified if op_script is specified.
             :type val_f_script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_script: If op_script is specified, this value will be compared to the value in script using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_script must be specified if op_script is specified.
             :type val_c_script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_script_id: The operator to apply to the field script_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. script_id: The internal NetMRI identifier for the script associated with this job. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_transactional_ind: The operator to apply to the field transactional_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. transactional_ind: Flag indicating that the job needs to be executed in a transaction. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_unapproved_notification_trigger: The operator to apply to the field unapproved_notification_trigger. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. unapproved_notification_trigger: Flag that defines if approval status has changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_unapproved_notification_trigger: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_unapproved_notification_trigger: If op_unapproved_notification_trigger is specified, the field named in this input will be compared to the value in unapproved_notification_trigger using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_unapproved_notification_trigger must be specified if op_unapproved_notification_trigger is specified.
             :type val_f_unapproved_notification_trigger: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_unapproved_notification_trigger: If op_unapproved_notification_trigger is specified, this value will be compared to the value in unapproved_notification_trigger using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_unapproved_notification_trigger must be specified if op_unapproved_notification_trigger is specified.
             :type val_c_unapproved_notification_trigger: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date/time that this job specification was last updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param methods: A list of job specification methods. The listed methods will be called on each job specification returned and included in the output. Available methods are: meta.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script.
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

             :param select: The list of attributes to return for each JobSpecification. Valid values are id, name, description, script_id, schedule, created_by, approved_by, approved_by_name, approved_timestamp, created_at, updated_at, config_template_id, job_type, category, provision_data, transactional_ind, approval_note, revertable_ind, last_run, push_mode, unapproved_notification_trigger, deployable_ind, script. If empty or omitted, all attributes will be returned.
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

             :return job_specifications: An array of the JobSpecification objects that match the specified input criteria.
             :rtype job_specifications: Array of JobSpecification

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified job specification from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Creates a new job specification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The job name as entered when creating the job.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param schedule: The job schedule, in cron format.
             :type schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script associated with this job.
             :type script_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A comma delimited list of device groups against which to run the specified job. Either this or the device_ids parameter is required.
             :type device_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: A comma delimited list of device ids against which to run the specified job. Either this or the device_group_ids parameter is required.
             :type device_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved: Indicates whether or not this job is approved.
             :type approved: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_variables: Optional variables to be passed to the script. Any variable name starting with $ will be passed through as input to the script.
             :type script_variables: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` requestor

             :param credential_mode: If user credentials are required, they may be set from additional inputs (credential_mode = 'manual'). The credentials may be looked up using requestor stored credentials (credential_mode = 'requestor'). The credentials may be looked up using the approver stored credentials (credential_mode = 'approver').
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

             :param enable_password: Enable Password to be used if the job requires user credentials.
             :type enable_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Overview of the job functionality.
             :type description: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created job specification.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created job specification.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created job specification.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_specification: The newly created job specification.
             :rtype job_specification: JobSpecification

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing job specification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the job specification.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The job name as entered when creating the job. If omitted, this field will not be updated.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule: The job schedule, in cron format. If omitted, this field will not be updated.
             :type schedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_type: The base type of the job ('script' or 'template'). If omitted, this field will not be updated.
             :type job_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_id: The internal NetMRI identifier for the script associated with this job. If omitted, this field will not be updated.
             :type script_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_template_id: The internal NetMRI identifier for the associated Configuration Template. If omitted, this field will not be updated.
             :type config_template_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param push_mode: Defines the push mode (bulk or line by line) used for template based jobs. If omitted, this field will not be updated.
             :type push_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A comma delimited list of device groups against which to run the specified job. Either this or the device_ids parameter is required.
             :type device_group_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: A comma delimited list of device ids against which to run the specified job. Either this or the device_group_ids parameter is required.
             :type device_ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param approved: Indicates whether or not this job is approved.
             :type approved: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param script_variables: Optional variables to be passed to the script. Any variable name starting with $ will be passed through as input to the script.
             :type script_variables: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` requestor

             :param credential_mode: If user credentials are required, they may be set from additional inputs (credential_mode = 'manual'). The credentials may be looked up using requestor stored credentials (credential_mode = 'requestor'). The credentials may be looked up using the approver stored credentials (credential_mode = 'approver').
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

             :param enable_password: Enable Password to be used if the job requires user credentials.
             :type enable_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Overview of the job functionality.
             :type description: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated job specification.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated job specification.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated job specification.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_specification: The updated job specification.
             :rtype job_specification: JobSpecification

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def run(self, **kwargs):
        """Runs the specified job specification immediately.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the job specification to run.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param dry_run: Do not run an actual job; marke it skipped immediately after processing
             :type dry_run: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: ID of the running job specification or any error code.
             :rtype id: Integer

            """

        return self.api_request(self._get_method_fullname("run"), kwargs)

    def approve(self, **kwargs):
        """Approves the specified job specification immediately.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the job specification to approve.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_specification: The job specification that has been approved.
             :rtype job_specification: JobSpecification

            """

        return self.api_request(self._get_method_fullname("approve"), kwargs)

    def unapprove(self, **kwargs):
        """Unapproves the specified job specification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the job specification to unapprove.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_specification: The job specification that has been unapproved.
             :rtype job_specification: JobSpecification

            """

        return self.api_request(self._get_method_fullname("unapprove"), kwargs)
