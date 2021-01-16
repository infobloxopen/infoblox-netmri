from ..broker import Broker


class JobProcessBroker(Broker):
    controller = "job_processes"

    def index(self, **kwargs):
        """Lists the available job processes. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal identifier of this process.
             :type id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job process methods. The listed methods will be called on each job process returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id.
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

             :param select: The list of attributes to return for each JobProcess. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id. If empty or omitted, all attributes will be returned.
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

             :return job_processes: An array of the JobProcess objects that match the specified input criteria.
             :rtype job_processes: Array of JobProcess

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified job process.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal identifier of this process.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job process methods. The listed methods will be called on each job process returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_process: The job process identified by the specified id.
             :rtype job_process: JobProcess

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available job processes matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param completed_at: The date and time the execution of this process was completed.
             :type completed_at: Array of DateTime

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

             :param deploy_ind: Indication that this process must be re-executed for post-deploy operation when completed with success.
             :type deploy_ind: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal identifier of the device that this process is running against.
             :type device_id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal identifier of this process.
             :type id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param input_data: Data parameters for the execution.
             :type input_data: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_handler_id: The internal identifier of the Runner that handled the execution of this process.
             :type job_handler_id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The internal identifier of job that process belongs to.
             :type job_id: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_status_at: The date and time the status was updated.
             :type last_status_at: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param process_type: The kind of process_type.
             :type process_type: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param revert_ind: Indication that this process must be re-executed for reversion if it is completed with an error.
             :type revert_ind: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param started_at: The date and time the execution of this process was started.
             :type started_at: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The last known execution status for this target.
             :type status: Array of String

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

             :param user_name: The name of the user that ran this execution.
             :type user_name: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job process methods. The listed methods will be called on each job process returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id.
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

             :param select: The list of attributes to return for each JobProcess. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against job processes, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: completed_at, created_at, deploy_ind, device_id, id, input_data, job_handler_id, job_id, last_status_at, process_type, revert_ind, started_at, status, updated_at, user_name.
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

             :return job_processes: An array of the JobProcess objects that match the specified input criteria.
             :rtype job_processes: Array of JobProcess

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available job processes matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: completed_at, created_at, deploy_ind, device_id, id, input_data, job_handler_id, job_id, last_status_at, process_type, revert_ind, started_at, status, updated_at, user_name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_completed_at: The operator to apply to the field completed_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. completed_at: The date and time the execution of this process was completed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_deploy_ind: The operator to apply to the field deploy_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. deploy_ind: Indication that this process must be re-executed for post-deploy operation when completed with success. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_deploy_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_deploy_ind: If op_deploy_ind is specified, the field named in this input will be compared to the value in deploy_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_deploy_ind must be specified if op_deploy_ind is specified.
             :type val_f_deploy_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_deploy_ind: If op_deploy_ind is specified, this value will be compared to the value in deploy_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_deploy_ind must be specified if op_deploy_ind is specified.
             :type val_c_deploy_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_id: The operator to apply to the field device_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_id: The internal identifier of the device that this process is running against. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_id: If op_device_id is specified, the field named in this input will be compared to the value in device_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_id must be specified if op_device_id is specified.
             :type val_f_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_id: If op_device_id is specified, this value will be compared to the value in device_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_id must be specified if op_device_id is specified.
             :type val_c_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal identifier of this process. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_input_data: The operator to apply to the field input_data. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. input_data: Data parameters for the execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_handler_id: The operator to apply to the field job_handler_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_handler_id: The internal identifier of the Runner that handled the execution of this process. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_job_handler_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_job_handler_id: If op_job_handler_id is specified, the field named in this input will be compared to the value in job_handler_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_job_handler_id must be specified if op_job_handler_id is specified.
             :type val_f_job_handler_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_job_handler_id: If op_job_handler_id is specified, this value will be compared to the value in job_handler_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_job_handler_id must be specified if op_job_handler_id is specified.
             :type val_c_job_handler_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_id: The operator to apply to the field job_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_id: The internal identifier of job that process belongs to. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_last_status_at: The operator to apply to the field last_status_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_status_at: The date and time the status was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_process_type: The operator to apply to the field process_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. process_type: The kind of process_type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_process_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_process_type: If op_process_type is specified, the field named in this input will be compared to the value in process_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_process_type must be specified if op_process_type is specified.
             :type val_f_process_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_process_type: If op_process_type is specified, this value will be compared to the value in process_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_process_type must be specified if op_process_type is specified.
             :type val_c_process_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_revert_ind: The operator to apply to the field revert_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. revert_ind: Indication that this process must be re-executed for reversion if it is completed with an error. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_revert_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_revert_ind: If op_revert_ind is specified, the field named in this input will be compared to the value in revert_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_revert_ind must be specified if op_revert_ind is specified.
             :type val_f_revert_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_revert_ind: If op_revert_ind is specified, this value will be compared to the value in revert_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_revert_ind must be specified if op_revert_ind is specified.
             :type val_c_revert_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_started_at: The operator to apply to the field started_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. started_at: The date and time the execution of this process was started. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The last known execution status for this target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_user_name: The operator to apply to the field user_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_name: The name of the user that ran this execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param methods: A list of job process methods. The listed methods will be called on each job process returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id.
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

             :param select: The list of attributes to return for each JobProcess. Valid values are id, process_type, user_name, job_handler_id, job_id, input_data, status, last_status_at, started_at, completed_at, created_at, updated_at, revert_ind, deploy_ind, device_id. If empty or omitted, all attributes will be returned.
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

             :return job_processes: An array of the JobProcess objects that match the specified input criteria.
             :rtype job_processes: Array of JobProcess

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device(self, **kwargs):
        """The device against which this Process will be executed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal identifier of this process.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device against which this Process will be executed.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def stream_output(self, **kwargs):
        """Return log output stream.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The job id to list files for. Required unless job_process_id is specified.
             :type job_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_process_id: The job process id to list files for. Required unless job_id and device_id are specified.
             :type job_process_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The Device ID to list files for. Required unless job_process_id is specified.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` script-allout

             :param stream: Name of expected stream.
             :type stream: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param first: First line expected.
             :type first: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` -1

             :param end_line: Number of the end line to read, if -1, read all available.
             :type end_line: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` -1

             :param count: Number of lines to read, if -1, read all available.
             :type count: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param retry_limit: Number of seconds before stopping retry efforts, if 0 do not retry.
             :type retry_limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return stream: The log output stream.
             :rtype stream: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the job process.
             :rtype status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return completed_at: The date and time when the job process was completed. returned nil if it is not completed
             :rtype completed_at: DateTime

            """

        return self.api_request(self._get_method_fullname("stream_output"), kwargs)

    def execution_log_files(self, **kwargs):
        """Downloads the per-device files for a job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The job id to list files for. Required unless job_process_id is specified.
             :type job_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The Device ID to list files for. Required unless job_process_id is specified.
             :type device_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_process_id: The job process id to list files for. Required unless job_id and deviceid are specified.
             :type job_process_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: An optional filename to download. If the special filename "all.zip" is passed, a ZIP file containing all job files will be created
             :type filename: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read file from.
             :type read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start: A position in the file to start transmission from. Available for log files only.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param retry_limit: Number of seconds before stopping retry efforts. Usually used when viewing a log for a new job.
             :type retry_limit: Integer

            **Outputs**

            """

        return self.api_mixed_request(self._get_method_fullname("execution_log_files"), kwargs)

    def show_job_files(self, **kwargs):
        """Show files for a job.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The job id to list files for. Required unless job_process_id is specified.
             :type job_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_process_id: The job process id to list files for. Required unless job_id and device_id are specified.
             :type job_process_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The Device ID to list files for. Required unless job_process_id is specified.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return filenames: An array of filenames that match the specified input criteria.
             :rtype filenames: Array of String

            """

        return self.api_request(self._get_method_fullname("show_job_files"), kwargs)
