from ..broker import Broker


class JobTargetBroker(Broker):
    controller = "job_targets"

    def show(self, **kwargs):
        """Shows the details for the specified job target.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal identifier of this target.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_target: The job target identified by the specified id.
             :rtype job_target: JobTarget

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available job targets. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal identifier of this target.
             :type id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal identifier of the job specification that issued this target.
             :type job_specification_id: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data.
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

             :param select: The list of attributes to return for each JobTarget. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data. If empty or omitted, all attributes will be returned.
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

             :return job_targets: An array of the JobTarget objects that match the specified input criteria.
             :rtype job_targets: Array of JobTarget

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available job targets matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param completed_at: The date and time this target was completed in the script execution.
             :type completed_at: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_filter_set_id: The internal identifier of DevicFilterSet that target is of type TargetDeviceFilterSet.
             :type device_filter_set_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_id: The internal identifier of device-group if that target is of type TargetdeviceGroup.
             :type device_group_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal identifier of device if that target denotes a Device.
             :type device_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dis_session_id: Unused.
             :type dis_session_id: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal identifier of this target.
             :type id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param input_data: Target specific input data.
             :type input_data: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interface_group_id: The internal identifier of interface-group if that target is of type TargetInterfaceGroup.
             :type interface_group_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interface_id: The internal identifier of interface if that target is of type TargetInterface.
             :type interface_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The internal identifier of the job this target belongs to.
             :type job_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal identifier of the job specification that issued this target.
             :type job_specification_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_status_at: The date and time the status was updated.
             :type last_status_at: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param managed_process_id: The internal identifier of JobProcess that runs this target.
             :type managed_process_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The last known execution status for this target.
             :type status: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status_info: Extra information on the execution status for this target.
             :type status_info: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param target_type: Type of Target.
             :type target_type: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data.
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

             :param select: The list of attributes to return for each JobTarget. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against job targets, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: completed_at, created_at, device_filter_set_id, device_group_id, device_id, dis_session_id, id, input_data, interface_group_id, interface_id, job_id, job_specification_id, last_status_at, managed_process_id, status, status_info, target_type, updated_at.
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

             :return job_targets: An array of the JobTarget objects that match the specified input criteria.
             :rtype job_targets: Array of JobTarget

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available job targets matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: completed_at, created_at, device_filter_set_id, device_group_id, device_id, dis_session_id, id, input_data, interface_group_id, interface_id, job_id, job_specification_id, last_status_at, managed_process_id, status, status_info, target_type, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_completed_at: The operator to apply to the field completed_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. completed_at: The date and time this target was completed in the script execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_device_filter_set_id: The operator to apply to the field device_filter_set_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_filter_set_id: The internal identifier of DevicFilterSet that target is of type TargetDeviceFilterSet. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_filter_set_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_filter_set_id: If op_device_filter_set_id is specified, the field named in this input will be compared to the value in device_filter_set_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_filter_set_id must be specified if op_device_filter_set_id is specified.
             :type val_f_device_filter_set_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_filter_set_id: If op_device_filter_set_id is specified, this value will be compared to the value in device_filter_set_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_filter_set_id must be specified if op_device_filter_set_id is specified.
             :type val_c_device_filter_set_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_group_id: The operator to apply to the field device_group_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_group_id: The internal identifier of device-group if that target is of type TargetdeviceGroup. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_device_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_device_group_id: If op_device_group_id is specified, the field named in this input will be compared to the value in device_group_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_device_group_id must be specified if op_device_group_id is specified.
             :type val_f_device_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_device_group_id: If op_device_group_id is specified, this value will be compared to the value in device_group_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_device_group_id must be specified if op_device_group_id is specified.
             :type val_c_device_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_device_id: The operator to apply to the field device_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. device_id: The internal identifier of device if that target denotes a Device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_dis_session_id: The operator to apply to the field dis_session_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. dis_session_id: Unused. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_dis_session_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_dis_session_id: If op_dis_session_id is specified, the field named in this input will be compared to the value in dis_session_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_dis_session_id must be specified if op_dis_session_id is specified.
             :type val_f_dis_session_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_dis_session_id: If op_dis_session_id is specified, this value will be compared to the value in dis_session_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_dis_session_id must be specified if op_dis_session_id is specified.
             :type val_c_dis_session_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal identifier of this target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_input_data: The operator to apply to the field input_data. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. input_data: Target specific input data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_interface_group_id: The operator to apply to the field interface_group_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. interface_group_id: The internal identifier of interface-group if that target is of type TargetInterfaceGroup. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_interface_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_interface_group_id: If op_interface_group_id is specified, the field named in this input will be compared to the value in interface_group_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_interface_group_id must be specified if op_interface_group_id is specified.
             :type val_f_interface_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_interface_group_id: If op_interface_group_id is specified, this value will be compared to the value in interface_group_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_interface_group_id must be specified if op_interface_group_id is specified.
             :type val_c_interface_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_interface_id: The operator to apply to the field interface_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. interface_id: The internal identifier of interface if that target is of type TargetInterface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_interface_id: If op_interface_id is specified, the field named in this input will be compared to the value in interface_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_interface_id must be specified if op_interface_id is specified.
             :type val_f_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_interface_id: If op_interface_id is specified, this value will be compared to the value in interface_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_interface_id must be specified if op_interface_id is specified.
             :type val_c_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_id: The operator to apply to the field job_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_id: The internal identifier of the job this target belongs to. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_job_specification_id: The operator to apply to the field job_specification_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_specification_id: The internal identifier of the job specification that issued this target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_managed_process_id: The operator to apply to the field managed_process_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. managed_process_id: The internal identifier of JobProcess that runs this target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_managed_process_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_managed_process_id: If op_managed_process_id is specified, the field named in this input will be compared to the value in managed_process_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_managed_process_id must be specified if op_managed_process_id is specified.
             :type val_f_managed_process_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_managed_process_id: If op_managed_process_id is specified, this value will be compared to the value in managed_process_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_managed_process_id must be specified if op_managed_process_id is specified.
             :type val_c_managed_process_id: String

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

             :param op_status_info: The operator to apply to the field status_info. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status_info: Extra information on the execution status for this target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_status_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_status_info: If op_status_info is specified, the field named in this input will be compared to the value in status_info using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_status_info must be specified if op_status_info is specified.
             :type val_f_status_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_status_info: If op_status_info is specified, this value will be compared to the value in status_info using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_status_info must be specified if op_status_info is specified.
             :type val_c_status_info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_target_type: The operator to apply to the field target_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. target_type: Type of Target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_target_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_target_type: If op_target_type is specified, the field named in this input will be compared to the value in target_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_target_type must be specified if op_target_type is specified.
             :type val_f_target_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_target_type: If op_target_type is specified, this value will be compared to the value in target_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_target_type must be specified if op_target_type is specified.
             :type val_c_target_type: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data.
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

             :param select: The list of attributes to return for each JobTarget. Valid values are id, job_id, managed_process_id, dis_session_id, target_type, device_id, device_group_id, interface_group_id, interface_id, device_filter_set_id, created_at, updated_at, job_specification_id, status, last_status_at, completed_at, status_info, input_data. If empty or omitted, all attributes will be returned.
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

             :return job_targets: An array of the JobTarget objects that match the specified input criteria.
             :rtype job_targets: Array of JobTarget

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
