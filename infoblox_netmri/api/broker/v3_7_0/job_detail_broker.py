from ..broker import Broker


class JobDetailBroker(Broker):
    controller = "job_details"

    def search(self, **kwargs):
        """Lists the available job details matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this job detail.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this job detail.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The time this job completed execution against this specific device.
             :type EndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The time this job completed execution against this specific device.
             :type EndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param JobDetailID: The internal NetMRI identifier for this job detail.
             :type JobDetailID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobDetailID: The internal NetMRI identifier for this job detail.
             :type JobDetailID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param JobID: The internal NetMRI identifier for the job associated with this job detail.
             :type JobID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobID: The internal NetMRI identifier for the job associated with this job detail.
             :type JobID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LastUpdate: The last time the status changed for this job detail.
             :type LastUpdate: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LastUpdate: The last time the status changed for this job detail.
             :type LastUpdate: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Module: The internal NetMRI subsystem that created this job detail record.
             :type Module: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Module: The internal NetMRI subsystem that created this job detail record.
             :type Module: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Script: The name of the script associated with this job detail.
             :type Script: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Script: The name of the script associated with this job detail.
             :type Script: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ScriptDisplayName: The title of the script.
             :type ScriptDisplayName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ScriptDisplayName: The title of the script.
             :type ScriptDisplayName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The time this job began execution against this specific device.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The time this job began execution against this specific device.
             :type StartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Status: The status of this job detail. That is, the status of this execution of the script against this device.
             :type Status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Status: The status of this job detail. That is, the status of this execution of the script against this device.
             :type Status: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Visible: Shows if this job detail record was user initiated.
             :type Visible: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Visible: Shows if this job detail record was user initiated.
             :type Visible: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal NetMRI identifier of corresponding JobSpecification
             :type job_specification_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_specification_id: The internal NetMRI identifier of corresponding JobSpecification
             :type job_specification_id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job detail methods. The listed methods will be called on each job detail returned and included in the output. Available methods are: infradevice, meta, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, device.
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
            |  ``default:`` JobDetailID

             :param sort: The data field(s) to use for sorting the output. Default is JobDetailID. Valid values are JobDetailID, JobID, Script, ScriptDisplayName, DeviceID, StartTime, EndTime, Status, LastUpdate, Module, Visible, job_specification_id.
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

             :param select: The list of attributes to return for each JobDetail. Valid values are JobDetailID, JobID, Script, ScriptDisplayName, DeviceID, StartTime, EndTime, Status, LastUpdate, Module, Visible, job_specification_id. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against job details, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DeviceID, EndTime, JobDetailID, JobID, LastUpdate, Module, Script, ScriptDisplayName, StartTime, Status, Visible, job_specification_id.
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

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available job details matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DeviceID, EndTime, JobDetailID, JobID, LastUpdate, Module, Script, ScriptDisplayName, StartTime, Status, Visible, job_specification_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device associated with this job detail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceID: If op_DeviceID is specified, the field named in this input will be compared to the value in DeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceID must be specified if op_DeviceID is specified.
             :type val_f_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceID: If op_DeviceID is specified, this value will be compared to the value in DeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceID must be specified if op_DeviceID is specified.
             :type val_c_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndTime: The operator to apply to the field EndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndTime: The time this job completed execution against this specific device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndTime: If op_EndTime is specified, the field named in this input will be compared to the value in EndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndTime must be specified if op_EndTime is specified.
             :type val_f_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndTime: If op_EndTime is specified, this value will be compared to the value in EndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndTime must be specified if op_EndTime is specified.
             :type val_c_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_JobDetailID: The operator to apply to the field JobDetailID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. JobDetailID: The internal NetMRI identifier for this job detail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_JobDetailID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_JobDetailID: If op_JobDetailID is specified, the field named in this input will be compared to the value in JobDetailID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_JobDetailID must be specified if op_JobDetailID is specified.
             :type val_f_JobDetailID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_JobDetailID: If op_JobDetailID is specified, this value will be compared to the value in JobDetailID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_JobDetailID must be specified if op_JobDetailID is specified.
             :type val_c_JobDetailID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_JobID: The operator to apply to the field JobID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. JobID: The internal NetMRI identifier for the job associated with this job detail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_JobID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_JobID: If op_JobID is specified, the field named in this input will be compared to the value in JobID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_JobID must be specified if op_JobID is specified.
             :type val_f_JobID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_JobID: If op_JobID is specified, this value will be compared to the value in JobID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_JobID must be specified if op_JobID is specified.
             :type val_c_JobID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LastUpdate: The operator to apply to the field LastUpdate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LastUpdate: The last time the status changed for this job detail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LastUpdate: If op_LastUpdate is specified, the field named in this input will be compared to the value in LastUpdate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LastUpdate must be specified if op_LastUpdate is specified.
             :type val_f_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LastUpdate: If op_LastUpdate is specified, this value will be compared to the value in LastUpdate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LastUpdate must be specified if op_LastUpdate is specified.
             :type val_c_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Module: The operator to apply to the field Module. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Module: The internal NetMRI subsystem that created this job detail record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Module: If op_Module is specified, the field named in this input will be compared to the value in Module using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Module must be specified if op_Module is specified.
             :type val_f_Module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Module: If op_Module is specified, this value will be compared to the value in Module using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Module must be specified if op_Module is specified.
             :type val_c_Module: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Script: The operator to apply to the field Script. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Script: The name of the script associated with this job detail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Script: If op_Script is specified, the field named in this input will be compared to the value in Script using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Script must be specified if op_Script is specified.
             :type val_f_Script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Script: If op_Script is specified, this value will be compared to the value in Script using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Script must be specified if op_Script is specified.
             :type val_c_Script: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ScriptDisplayName: The operator to apply to the field ScriptDisplayName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ScriptDisplayName: The title of the script. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ScriptDisplayName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ScriptDisplayName: If op_ScriptDisplayName is specified, the field named in this input will be compared to the value in ScriptDisplayName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ScriptDisplayName must be specified if op_ScriptDisplayName is specified.
             :type val_f_ScriptDisplayName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ScriptDisplayName: If op_ScriptDisplayName is specified, this value will be compared to the value in ScriptDisplayName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ScriptDisplayName must be specified if op_ScriptDisplayName is specified.
             :type val_c_ScriptDisplayName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The time this job began execution against this specific device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Status: The operator to apply to the field Status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Status: The status of this job detail. That is, the status of this execution of the script against this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Status: If op_Status is specified, the field named in this input will be compared to the value in Status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Status must be specified if op_Status is specified.
             :type val_f_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Status: If op_Status is specified, this value will be compared to the value in Status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Status must be specified if op_Status is specified.
             :type val_c_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Visible: The operator to apply to the field Visible. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Visible: Shows if this job detail record was user initiated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Visible: If op_Visible is specified, the field named in this input will be compared to the value in Visible using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Visible must be specified if op_Visible is specified.
             :type val_f_Visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Visible: If op_Visible is specified, this value will be compared to the value in Visible using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Visible must be specified if op_Visible is specified.
             :type val_c_Visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_job_specification_id: The operator to apply to the field job_specification_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. job_specification_id: The internal NetMRI identifier of corresponding JobSpecification For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of job detail methods. The listed methods will be called on each job detail returned and included in the output. Available methods are: infradevice, meta, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, device.
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
            |  ``default:`` JobDetailID

             :param sort: The data field(s) to use for sorting the output. Default is JobDetailID. Valid values are JobDetailID, JobID, Script, ScriptDisplayName, DeviceID, StartTime, EndTime, Status, LastUpdate, Module, Visible, job_specification_id.
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

             :param select: The list of attributes to return for each JobDetail. Valid values are JobDetailID, JobID, Script, ScriptDisplayName, DeviceID, StartTime, EndTime, Status, LastUpdate, Module, Visible, job_specification_id. If empty or omitted, all attributes will be returned.
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

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def index(self, **kwargs):
        """Lists per-device job details. You can filter the results by Job ID, Job Name, or by Device ID.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The job id to list details for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the job to list details for.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param deviceid: The Device ID to list details for.
             :type deviceid: Integer

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

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Lists the per-device details for the associated job id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to list details for.
             :type id: Integer

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

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("show"), kwargs)

    def device_files(self, **kwargs):
        """Lists/downloads the per-device files for a job. If no filename is given, a list of files for the job will be returned. If a filename is passed, and it exists, it will be downloaded as type "application/octet-stream". If the special filename "all.zip" is passed, a ZIP file containing all job files will be created and downloaded as type "application/zip"

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

             :param deviceid: The Device ID to list files for.
             :type deviceid: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: An optional filename to download.
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

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return filenames: An array of filenames that match the specified input criteria.
             :rtype filenames: Array of String

            """

        return self.api_mixed_request(self._get_method_fullname("device_files"), kwargs)

    def port_control_file(self, **kwargs):
        """Download a Port Control jobs log as type "application/octet-stream".

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

             :param deviceid: The Device ID to list files for.
             :type deviceid: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: An optional filename to download.
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

        return self.api_mixed_request(self._get_method_fullname("port_control_file"), kwargs)
