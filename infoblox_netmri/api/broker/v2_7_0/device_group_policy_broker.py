from ..broker import Broker


class DeviceGroupPolicyBroker(Broker):
    controller = "device_group_policies"

    def show(self, **kwargs):
        """Shows the details for the specified device group policy.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group policy methods. The listed methods will be called on each device group policy returned and included in the output. Available methods are: policy_name, group_name.
             :type methods: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_group_policy: The device group policy identified by the specified DeviceGroupPolicyID.
             :rtype device_group_policy: DeviceGroupPolicy

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device group policies. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of the associated device group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of the associated device group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier of the associated effective policy.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier of the associated effective policy.
             :type PolicyID: Array of Integer

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

             :param timestamp: The data returned will represent the device group policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group policy methods. The listed methods will be called on each device group policy returned and included in the output. Available methods are: policy_name, group_name.
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
            |  ``default:`` DeviceGroupPolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceGroupPolicyID. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown.
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

             :param select: The list of attributes to return for each DeviceGroupPolicy. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown. If empty or omitted, all attributes will be returned.
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

             :return device_group_policies: An array of the DeviceGroupPolicy objects that match the specified input criteria.
             :rtype device_group_policies: Array of DeviceGroupPolicy

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device group policies matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceGroupPolicyChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceGroupPolicyChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceGroupPolicyEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceGroupPolicyEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyStartTime: The starting effective time of this record.
             :type DeviceGroupPolicyStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyStartTime: The starting effective time of this record.
             :type DeviceGroupPolicyStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyTimestamp: The date and time this record was collected or calculated.
             :type DeviceGroupPolicyTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupPolicyTimestamp: The date and time this record was collected or calculated.
             :type DeviceGroupPolicyTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesChecked: The number of devices in this device group for which the policy status was checked (this excludes devices that do not meet the policy filter criteria).
             :type DevicesChecked: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesChecked: The number of devices in this device group for which the policy status was checked (this excludes devices that do not meet the policy filter criteria).
             :type DevicesChecked: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesError: The number of devices in this device group for which the policy status result for this policy is Error.
             :type DevicesError: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesError: The number of devices in this device group for which the policy status result for this policy is Error.
             :type DevicesError: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesFailed: The number of devices in this device group for which the policy status result for this policy is Error, Warning, or Info.
             :type DevicesFailed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesFailed: The number of devices in this device group for which the policy status result for this policy is Error, Warning, or Info.
             :type DevicesFailed: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesInfo: The number of devices in this device group for which the policy status result for this policy is Info.
             :type DevicesInfo: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesInfo: The number of devices in this device group for which the policy status result for this policy is Info.
             :type DevicesInfo: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesInvalid: The number of devices in this device group for which the policy evaluation failed due to an invalid rule definition or internal error for this policy.
             :type DevicesInvalid: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesInvalid: The number of devices in this device group for which the policy evaluation failed due to an invalid rule definition or internal error for this policy.
             :type DevicesInvalid: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesPassed: The number of devices in this device group for which the policy status result for this policy is Passed.
             :type DevicesPassed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesPassed: The number of devices in this device group for which the policy status result for this policy is Passed.
             :type DevicesPassed: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesSkipped: The number of devices in this device group for which the policy status result for this policy is Skipped. This refers to devices that do not meet the policy filter criteria.
             :type DevicesSkipped: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesSkipped: The number of devices in this device group for which the policy status result for this policy is Skipped. This refers to devices that do not meet the policy filter criteria.
             :type DevicesSkipped: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesTotal: The number of devices in this device group against which this policy was deployed at the time of evaluation.
             :type DevicesTotal: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesTotal: The number of devices in this device group against which this policy was deployed at the time of evaluation.
             :type DevicesTotal: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesUnknown: The number of devices in this device group for which the policy status result for this policy is Unknown. This refers to devices for which a configuration file or other necessary data is not available.
             :type DevicesUnknown: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesUnknown: The number of devices in this device group for which the policy status result for this policy is Unknown. This refers to devices for which a configuration file or other necessary data is not available.
             :type DevicesUnknown: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesValid: The number of devices in this device group for which the policy was successfully evaluated (that is, without a failure such as an invalid XML-based rule).
             :type DevicesValid: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesValid: The number of devices in this device group for which the policy was successfully evaluated (that is, without a failure such as an invalid XML-based rule).
             :type DevicesValid: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesWarning: The number of devices in this device group for which the policy status result for this policy is Warning.
             :type DevicesWarning: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicesWarning: The number of devices in this device group for which the policy status result for this policy is Warning.
             :type DevicesWarning: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of the associated device group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of the associated device group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier of the associated effective policy.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier of the associated effective policy.
             :type PolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStatus: The overall status for this device group an policy.
             :type PolicyStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStatus: The overall status for this device group an policy.
             :type PolicyStatus: Array of String

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

             :param timestamp: The data returned will represent the device group policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group policy methods. The listed methods will be called on each device group policy returned and included in the output. Available methods are: policy_name, group_name.
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
            |  ``default:`` DeviceGroupPolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceGroupPolicyID. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown.
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

             :param select: The list of attributes to return for each DeviceGroupPolicy. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device group policies, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceGroupPolicyChangedCols, DeviceGroupPolicyEndTime, DeviceGroupPolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyTimestamp, DevicesChecked, DevicesError, DevicesFailed, DevicesInfo, DevicesInvalid, DevicesPassed, DevicesSkipped, DevicesTotal, DevicesUnknown, DevicesValid, DevicesWarning, GroupID, PolicyID, PolicyStatus.
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

             :return device_group_policies: An array of the DeviceGroupPolicy objects that match the specified input criteria.
             :rtype device_group_policies: Array of DeviceGroupPolicy

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device group policies matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceGroupPolicyChangedCols, DeviceGroupPolicyEndTime, DeviceGroupPolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyTimestamp, DevicesChecked, DevicesError, DevicesFailed, DevicesInfo, DevicesInvalid, DevicesPassed, DevicesSkipped, DevicesTotal, DevicesUnknown, DevicesValid, DevicesWarning, GroupID, PolicyID, PolicyStatus.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceID: If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_f_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceID: If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_c_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupPolicyChangedCols: The operator to apply to the field DeviceGroupPolicyChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupPolicyChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupPolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupPolicyChangedCols: If op_DeviceGroupPolicyChangedCols is specified, the field named in this input will be compared to the value in DeviceGroupPolicyChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupPolicyChangedCols must be specified if op_DeviceGroupPolicyChangedCols is specified.
             :type val_f_DeviceGroupPolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupPolicyChangedCols: If op_DeviceGroupPolicyChangedCols is specified, this value will be compared to the value in DeviceGroupPolicyChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupPolicyChangedCols must be specified if op_DeviceGroupPolicyChangedCols is specified.
             :type val_c_DeviceGroupPolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupPolicyEndTime: The operator to apply to the field DeviceGroupPolicyEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupPolicyEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupPolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupPolicyEndTime: If op_DeviceGroupPolicyEndTime is specified, the field named in this input will be compared to the value in DeviceGroupPolicyEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupPolicyEndTime must be specified if op_DeviceGroupPolicyEndTime is specified.
             :type val_f_DeviceGroupPolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupPolicyEndTime: If op_DeviceGroupPolicyEndTime is specified, this value will be compared to the value in DeviceGroupPolicyEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupPolicyEndTime must be specified if op_DeviceGroupPolicyEndTime is specified.
             :type val_c_DeviceGroupPolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupPolicyID: The operator to apply to the field DeviceGroupPolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupPolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupPolicyID: If op_DeviceGroupPolicyID is specified, the field named in this input will be compared to the value in DeviceGroupPolicyID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupPolicyID must be specified if op_DeviceGroupPolicyID is specified.
             :type val_f_DeviceGroupPolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupPolicyID: If op_DeviceGroupPolicyID is specified, this value will be compared to the value in DeviceGroupPolicyID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupPolicyID must be specified if op_DeviceGroupPolicyID is specified.
             :type val_c_DeviceGroupPolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupPolicyStartTime: The operator to apply to the field DeviceGroupPolicyStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupPolicyStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupPolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupPolicyStartTime: If op_DeviceGroupPolicyStartTime is specified, the field named in this input will be compared to the value in DeviceGroupPolicyStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupPolicyStartTime must be specified if op_DeviceGroupPolicyStartTime is specified.
             :type val_f_DeviceGroupPolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupPolicyStartTime: If op_DeviceGroupPolicyStartTime is specified, this value will be compared to the value in DeviceGroupPolicyStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupPolicyStartTime must be specified if op_DeviceGroupPolicyStartTime is specified.
             :type val_c_DeviceGroupPolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupPolicyTimestamp: The operator to apply to the field DeviceGroupPolicyTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupPolicyTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupPolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupPolicyTimestamp: If op_DeviceGroupPolicyTimestamp is specified, the field named in this input will be compared to the value in DeviceGroupPolicyTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupPolicyTimestamp must be specified if op_DeviceGroupPolicyTimestamp is specified.
             :type val_f_DeviceGroupPolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupPolicyTimestamp: If op_DeviceGroupPolicyTimestamp is specified, this value will be compared to the value in DeviceGroupPolicyTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupPolicyTimestamp must be specified if op_DeviceGroupPolicyTimestamp is specified.
             :type val_c_DeviceGroupPolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesChecked: The operator to apply to the field DevicesChecked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesChecked: The number of devices in this device group for which the policy status was checked (this excludes devices that do not meet the policy filter criteria). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesChecked: If op_DevicesChecked is specified, the field named in this input will be compared to the value in DevicesChecked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesChecked must be specified if op_DevicesChecked is specified.
             :type val_f_DevicesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesChecked: If op_DevicesChecked is specified, this value will be compared to the value in DevicesChecked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesChecked must be specified if op_DevicesChecked is specified.
             :type val_c_DevicesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesError: The operator to apply to the field DevicesError. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesError: The number of devices in this device group for which the policy status result for this policy is Error. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesError: If op_DevicesError is specified, the field named in this input will be compared to the value in DevicesError using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesError must be specified if op_DevicesError is specified.
             :type val_f_DevicesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesError: If op_DevicesError is specified, this value will be compared to the value in DevicesError using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesError must be specified if op_DevicesError is specified.
             :type val_c_DevicesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesFailed: The operator to apply to the field DevicesFailed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesFailed: The number of devices in this device group for which the policy status result for this policy is Error, Warning, or Info. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesFailed: If op_DevicesFailed is specified, the field named in this input will be compared to the value in DevicesFailed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesFailed must be specified if op_DevicesFailed is specified.
             :type val_f_DevicesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesFailed: If op_DevicesFailed is specified, this value will be compared to the value in DevicesFailed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesFailed must be specified if op_DevicesFailed is specified.
             :type val_c_DevicesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesInfo: The operator to apply to the field DevicesInfo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesInfo: The number of devices in this device group for which the policy status result for this policy is Info. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesInfo: If op_DevicesInfo is specified, the field named in this input will be compared to the value in DevicesInfo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesInfo must be specified if op_DevicesInfo is specified.
             :type val_f_DevicesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesInfo: If op_DevicesInfo is specified, this value will be compared to the value in DevicesInfo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesInfo must be specified if op_DevicesInfo is specified.
             :type val_c_DevicesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesInvalid: The operator to apply to the field DevicesInvalid. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesInvalid: The number of devices in this device group for which the policy evaluation failed due to an invalid rule definition or internal error for this policy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesInvalid: If op_DevicesInvalid is specified, the field named in this input will be compared to the value in DevicesInvalid using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesInvalid must be specified if op_DevicesInvalid is specified.
             :type val_f_DevicesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesInvalid: If op_DevicesInvalid is specified, this value will be compared to the value in DevicesInvalid using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesInvalid must be specified if op_DevicesInvalid is specified.
             :type val_c_DevicesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesPassed: The operator to apply to the field DevicesPassed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesPassed: The number of devices in this device group for which the policy status result for this policy is Passed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesPassed: If op_DevicesPassed is specified, the field named in this input will be compared to the value in DevicesPassed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesPassed must be specified if op_DevicesPassed is specified.
             :type val_f_DevicesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesPassed: If op_DevicesPassed is specified, this value will be compared to the value in DevicesPassed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesPassed must be specified if op_DevicesPassed is specified.
             :type val_c_DevicesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesSkipped: The operator to apply to the field DevicesSkipped. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesSkipped: The number of devices in this device group for which the policy status result for this policy is Skipped. This refers to devices that do not meet the policy filter criteria. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesSkipped: If op_DevicesSkipped is specified, the field named in this input will be compared to the value in DevicesSkipped using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesSkipped must be specified if op_DevicesSkipped is specified.
             :type val_f_DevicesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesSkipped: If op_DevicesSkipped is specified, this value will be compared to the value in DevicesSkipped using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesSkipped must be specified if op_DevicesSkipped is specified.
             :type val_c_DevicesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesTotal: The operator to apply to the field DevicesTotal. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesTotal: The number of devices in this device group against which this policy was deployed at the time of evaluation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesTotal: If op_DevicesTotal is specified, the field named in this input will be compared to the value in DevicesTotal using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesTotal must be specified if op_DevicesTotal is specified.
             :type val_f_DevicesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesTotal: If op_DevicesTotal is specified, this value will be compared to the value in DevicesTotal using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesTotal must be specified if op_DevicesTotal is specified.
             :type val_c_DevicesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesUnknown: The operator to apply to the field DevicesUnknown. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesUnknown: The number of devices in this device group for which the policy status result for this policy is Unknown. This refers to devices for which a configuration file or other necessary data is not available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesUnknown: If op_DevicesUnknown is specified, the field named in this input will be compared to the value in DevicesUnknown using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesUnknown must be specified if op_DevicesUnknown is specified.
             :type val_f_DevicesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesUnknown: If op_DevicesUnknown is specified, this value will be compared to the value in DevicesUnknown using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesUnknown must be specified if op_DevicesUnknown is specified.
             :type val_c_DevicesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesValid: The operator to apply to the field DevicesValid. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesValid: The number of devices in this device group for which the policy was successfully evaluated (that is, without a failure such as an invalid XML-based rule). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesValid: If op_DevicesValid is specified, the field named in this input will be compared to the value in DevicesValid using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesValid must be specified if op_DevicesValid is specified.
             :type val_f_DevicesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesValid: If op_DevicesValid is specified, this value will be compared to the value in DevicesValid using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesValid must be specified if op_DevicesValid is specified.
             :type val_c_DevicesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicesWarning: The operator to apply to the field DevicesWarning. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicesWarning: The number of devices in this device group for which the policy status result for this policy is Warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicesWarning: If op_DevicesWarning is specified, the field named in this input will be compared to the value in DevicesWarning using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicesWarning must be specified if op_DevicesWarning is specified.
             :type val_f_DevicesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicesWarning: If op_DevicesWarning is specified, this value will be compared to the value in DevicesWarning using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicesWarning must be specified if op_DevicesWarning is specified.
             :type val_c_DevicesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GroupID: The operator to apply to the field GroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupID: The internal NetMRI identifier of the associated device group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GroupID: If op_GroupID is specified, the field named in this input will be compared to the value in GroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GroupID must be specified if op_GroupID is specified.
             :type val_f_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GroupID: If op_GroupID is specified, this value will be compared to the value in GroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GroupID must be specified if op_GroupID is specified.
             :type val_c_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyID: The operator to apply to the field PolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyID: The internal NetMRI identifier of the associated effective policy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyID: If op_PolicyID is specified, the field named in this input will be compared to the value in PolicyID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyID must be specified if op_PolicyID is specified.
             :type val_f_PolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyID: If op_PolicyID is specified, this value will be compared to the value in PolicyID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyID must be specified if op_PolicyID is specified.
             :type val_c_PolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyStatus: The operator to apply to the field PolicyStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyStatus: The overall status for this device group an policy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyStatus: If op_PolicyStatus is specified, the field named in this input will be compared to the value in PolicyStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyStatus must be specified if op_PolicyStatus is specified.
             :type val_f_PolicyStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyStatus: If op_PolicyStatus is specified, this value will be compared to the value in PolicyStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyStatus must be specified if op_PolicyStatus is specified.
             :type val_c_PolicyStatus: String

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

             :param timestamp: The data returned will represent the device group policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group policy methods. The listed methods will be called on each device group policy returned and included in the output. Available methods are: policy_name, group_name.
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
            |  ``default:`` DeviceGroupPolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceGroupPolicyID. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown.
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

             :param select: The list of attributes to return for each DeviceGroupPolicy. Valid values are DeviceGroupPolicyID, GroupID, PolicyID, DeviceGroupPolicyStartTime, DeviceGroupPolicyEndTime, DeviceGroupPolicyChangedCols, DeviceGroupPolicyTimestamp, DataSourceID, PolicyStatus, DevicesTotal, DevicesValid, DevicesChecked, DevicesInvalid, DevicesPassed, DevicesFailed, DevicesError, DevicesWarning, DevicesInfo, DevicesSkipped, DevicesUnknown. If empty or omitted, all attributes will be returned.
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

             :return device_group_policies: An array of the DeviceGroupPolicy objects that match the specified input criteria.
             :rtype device_group_policies: Array of DeviceGroupPolicy

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def policy_name(self, **kwargs):
        """The policy name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The policy name.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_name"), kwargs)

    def group_name(self, **kwargs):
        """The group name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceGroupPolicyID: The internal NetMRI identifier for this device group policy status record.
             :type DeviceGroupPolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The group name.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("group_name"), kwargs)

    def summary(self, **kwargs):
        """Provides a single method to retrieve policies, device groups, and per-device-group, per-policy status summaries. The start/limit parameters apply to the device groups, not to the policies. That is, if a device group is returned, all of the policy status summaries for that device group will be returned, regardless of the start/limit parameters.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The device group or list of device groups for which to obtain status.
             :type GroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param show_skipped_ind: If true, the results will include devices with policy status 'Skipped'.
             :type show_skipped_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The date and time for which to retrieve the policy status. The current status will be returned if omitted.
             :type timestamp: DateTime

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

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19.
             :type limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return effective_policies: The policies, as they were defined at the date and time specified in the timestamp parameter.
             :rtype effective_policies: Array of EffectivePolicy

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_groups: The device group information, as of the date and time specified in the timestamp parameter.
             :rtype device_groups: Array of DeviceGroup

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_group_policies: The per-device-group, per-policy status.
             :rtype device_group_policies: Array of DeviceGroupPolicy

            """

        return self.api_list_request(self._get_method_fullname("summary"), kwargs)
