from ..broker import Broker


class DevicePolicyBroker(Broker):
    controller = "device_policies"

    def show(self, **kwargs):
        """Shows the details for the specified device policy.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy methods. The listed methods will be called on each device policy returned and included in the output. Available methods are: policy_name, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_policy: The device policy identified by the specified DevicePolicyID.
             :rtype device_policy: DevicePolicy

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device policies. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device whose policy status this record represents.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device whose policy status this record represents.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for the policy whose status this record represents.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for the policy whose status this record represents.
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

             :param timestamp: The data returned will represent the device policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy methods. The listed methods will be called on each device policy returned and included in the output. Available methods are: policy_name, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyID. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown.
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

             :param select: The list of attributes to return for each DevicePolicy. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown. If empty or omitted, all attributes will be returned.
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

             :return device_policies: An array of the DevicePolicy objects that match the specified input criteria.
             :rtype device_policies: Array of DevicePolicy

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device policies matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device whose policy status this record represents.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device whose policy status this record represents.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevicePolicyChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevicePolicyChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DevicePolicyEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DevicePolicyEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyStartTime: The starting effective time of this revision of the record.
             :type DevicePolicyStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyStartTime: The starting effective time of this revision of the record.
             :type DevicePolicyStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyTimestamp: The date and time this record was collected or calculated.
             :type DevicePolicyTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyTimestamp: The date and time this record was collected or calculated.
             :type DevicePolicyTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for the policy whose status this record represents.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for the policy whose status this record represents.
             :type PolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesChecked: The total number of rules that were checked against this device for this policy. Invalid rules and rules that are skipped due to the device not matching the rule filter are not counted as 'checked' rules.
             :type PolicyRulesChecked: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesChecked: The total number of rules that were checked against this device for this policy. Invalid rules and rules that are skipped due to the device not matching the rule filter are not counted as 'checked' rules.
             :type PolicyRulesChecked: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesError: The total number of rules in this policy that the device failed with error status.
             :type PolicyRulesError: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesError: The total number of rules in this policy that the device failed with error status.
             :type PolicyRulesError: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesFailed: The total number of rules in this policy that the device failed with info, warning, or error status.
             :type PolicyRulesFailed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesFailed: The total number of rules in this policy that the device failed with info, warning, or error status.
             :type PolicyRulesFailed: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesInfo: The total number of rules in this policy that the device failed with info status.
             :type PolicyRulesInfo: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesInfo: The total number of rules in this policy that the device failed with info status.
             :type PolicyRulesInfo: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesInvalid: The total number of invalid rules that were in this policy at the time the policy was executed against this device.
             :type PolicyRulesInvalid: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesInvalid: The total number of invalid rules that were in this policy at the time the policy was executed against this device.
             :type PolicyRulesInvalid: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesPassed: The total number of rules in this policy that the device passed successfully.
             :type PolicyRulesPassed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesPassed: The total number of rules in this policy that the device passed successfully.
             :type PolicyRulesPassed: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesSkipped: The total number of rules in this policy that were skipped due to the device not matching the rule filters.
             :type PolicyRulesSkipped: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesSkipped: The total number of rules in this policy that were skipped due to the device not matching the rule filters.
             :type PolicyRulesSkipped: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesTotal: The total number of rules that in this policy at the time the policy was executed against this device.
             :type PolicyRulesTotal: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesTotal: The total number of rules that in this policy at the time the policy was executed against this device.
             :type PolicyRulesTotal: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesUnknown: The total number of rules that could not be fully evaluated because information needed for the rule was not available (for example, the configuration file has not been collected for the device).
             :type PolicyRulesUnknown: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesUnknown: The total number of rules that could not be fully evaluated because information needed for the rule was not available (for example, the configuration file has not been collected for the device).
             :type PolicyRulesUnknown: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesValid: The total number of valid rules that were in this policy at the time the policy was executed against this device. An invalid rule generally only occurs if the XML rule build has been used and an improper XML format has been specified.
             :type PolicyRulesValid: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesValid: The total number of valid rules that were in this policy at the time the policy was executed against this device. An invalid rule generally only occurs if the XML rule build has been used and an improper XML format has been specified.
             :type PolicyRulesValid: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesWarning: The total number of rules in this policy that the device failed with warning status.
             :type PolicyRulesWarning: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRulesWarning: The total number of rules in this policy that the device failed with warning status.
             :type PolicyRulesWarning: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStatus: The current status of this policy for this device.
             :type PolicyStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStatus: The current status of this policy for this device.
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

             :param timestamp: The data returned will represent the device policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy methods. The listed methods will be called on each device policy returned and included in the output. Available methods are: policy_name, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyID. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown.
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

             :param select: The list of attributes to return for each DevicePolicy. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device policies, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DevicePolicyChangedCols, DevicePolicyEndTime, DevicePolicyID, DevicePolicyStartTime, DevicePolicyTimestamp, PolicyID, PolicyRulesChecked, PolicyRulesError, PolicyRulesFailed, PolicyRulesInfo, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesSkipped, PolicyRulesTotal, PolicyRulesUnknown, PolicyRulesValid, PolicyRulesWarning, PolicyStatus.
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

             :return device_policies: An array of the DevicePolicy objects that match the specified input criteria.
             :rtype device_policies: Array of DevicePolicy

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device policies matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DevicePolicyChangedCols, DevicePolicyEndTime, DevicePolicyID, DevicePolicyStartTime, DevicePolicyTimestamp, PolicyID, PolicyRulesChecked, PolicyRulesError, PolicyRulesFailed, PolicyRulesInfo, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesSkipped, PolicyRulesTotal, PolicyRulesUnknown, PolicyRulesValid, PolicyRulesWarning, PolicyStatus.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device whose policy status this record represents. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DevicePolicyChangedCols: The operator to apply to the field DevicePolicyChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyChangedCols: If op_DevicePolicyChangedCols is specified, the field named in this input will be compared to the value in DevicePolicyChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyChangedCols must be specified if op_DevicePolicyChangedCols is specified.
             :type val_f_DevicePolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyChangedCols: If op_DevicePolicyChangedCols is specified, this value will be compared to the value in DevicePolicyChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyChangedCols must be specified if op_DevicePolicyChangedCols is specified.
             :type val_c_DevicePolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyEndTime: The operator to apply to the field DevicePolicyEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyEndTime: If op_DevicePolicyEndTime is specified, the field named in this input will be compared to the value in DevicePolicyEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyEndTime must be specified if op_DevicePolicyEndTime is specified.
             :type val_f_DevicePolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyEndTime: If op_DevicePolicyEndTime is specified, this value will be compared to the value in DevicePolicyEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyEndTime must be specified if op_DevicePolicyEndTime is specified.
             :type val_c_DevicePolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyID: The operator to apply to the field DevicePolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyID: The internal NetMRI identifier for this device policy status record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyID: If op_DevicePolicyID is specified, the field named in this input will be compared to the value in DevicePolicyID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyID must be specified if op_DevicePolicyID is specified.
             :type val_f_DevicePolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyID: If op_DevicePolicyID is specified, this value will be compared to the value in DevicePolicyID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyID must be specified if op_DevicePolicyID is specified.
             :type val_c_DevicePolicyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyStartTime: The operator to apply to the field DevicePolicyStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyStartTime: If op_DevicePolicyStartTime is specified, the field named in this input will be compared to the value in DevicePolicyStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyStartTime must be specified if op_DevicePolicyStartTime is specified.
             :type val_f_DevicePolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyStartTime: If op_DevicePolicyStartTime is specified, this value will be compared to the value in DevicePolicyStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyStartTime must be specified if op_DevicePolicyStartTime is specified.
             :type val_c_DevicePolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyTimestamp: The operator to apply to the field DevicePolicyTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyTimestamp: If op_DevicePolicyTimestamp is specified, the field named in this input will be compared to the value in DevicePolicyTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyTimestamp must be specified if op_DevicePolicyTimestamp is specified.
             :type val_f_DevicePolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyTimestamp: If op_DevicePolicyTimestamp is specified, this value will be compared to the value in DevicePolicyTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyTimestamp must be specified if op_DevicePolicyTimestamp is specified.
             :type val_c_DevicePolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyID: The operator to apply to the field PolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyID: The internal NetMRI identifier for the policy whose status this record represents. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PolicyRulesChecked: The operator to apply to the field PolicyRulesChecked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesChecked: The total number of rules that were checked against this device for this policy. Invalid rules and rules that are skipped due to the device not matching the rule filter are not counted as 'checked' rules. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesChecked: If op_PolicyRulesChecked is specified, the field named in this input will be compared to the value in PolicyRulesChecked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesChecked must be specified if op_PolicyRulesChecked is specified.
             :type val_f_PolicyRulesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesChecked: If op_PolicyRulesChecked is specified, this value will be compared to the value in PolicyRulesChecked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesChecked must be specified if op_PolicyRulesChecked is specified.
             :type val_c_PolicyRulesChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesError: The operator to apply to the field PolicyRulesError. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesError: The total number of rules in this policy that the device failed with error status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesError: If op_PolicyRulesError is specified, the field named in this input will be compared to the value in PolicyRulesError using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesError must be specified if op_PolicyRulesError is specified.
             :type val_f_PolicyRulesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesError: If op_PolicyRulesError is specified, this value will be compared to the value in PolicyRulesError using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesError must be specified if op_PolicyRulesError is specified.
             :type val_c_PolicyRulesError: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesFailed: The operator to apply to the field PolicyRulesFailed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesFailed: The total number of rules in this policy that the device failed with info, warning, or error status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesFailed: If op_PolicyRulesFailed is specified, the field named in this input will be compared to the value in PolicyRulesFailed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesFailed must be specified if op_PolicyRulesFailed is specified.
             :type val_f_PolicyRulesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesFailed: If op_PolicyRulesFailed is specified, this value will be compared to the value in PolicyRulesFailed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesFailed must be specified if op_PolicyRulesFailed is specified.
             :type val_c_PolicyRulesFailed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesInfo: The operator to apply to the field PolicyRulesInfo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesInfo: The total number of rules in this policy that the device failed with info status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesInfo: If op_PolicyRulesInfo is specified, the field named in this input will be compared to the value in PolicyRulesInfo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesInfo must be specified if op_PolicyRulesInfo is specified.
             :type val_f_PolicyRulesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesInfo: If op_PolicyRulesInfo is specified, this value will be compared to the value in PolicyRulesInfo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesInfo must be specified if op_PolicyRulesInfo is specified.
             :type val_c_PolicyRulesInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesInvalid: The operator to apply to the field PolicyRulesInvalid. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesInvalid: The total number of invalid rules that were in this policy at the time the policy was executed against this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesInvalid: If op_PolicyRulesInvalid is specified, the field named in this input will be compared to the value in PolicyRulesInvalid using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesInvalid must be specified if op_PolicyRulesInvalid is specified.
             :type val_f_PolicyRulesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesInvalid: If op_PolicyRulesInvalid is specified, this value will be compared to the value in PolicyRulesInvalid using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesInvalid must be specified if op_PolicyRulesInvalid is specified.
             :type val_c_PolicyRulesInvalid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesPassed: The operator to apply to the field PolicyRulesPassed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesPassed: The total number of rules in this policy that the device passed successfully. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesPassed: If op_PolicyRulesPassed is specified, the field named in this input will be compared to the value in PolicyRulesPassed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesPassed must be specified if op_PolicyRulesPassed is specified.
             :type val_f_PolicyRulesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesPassed: If op_PolicyRulesPassed is specified, this value will be compared to the value in PolicyRulesPassed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesPassed must be specified if op_PolicyRulesPassed is specified.
             :type val_c_PolicyRulesPassed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesSkipped: The operator to apply to the field PolicyRulesSkipped. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesSkipped: The total number of rules in this policy that were skipped due to the device not matching the rule filters. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesSkipped: If op_PolicyRulesSkipped is specified, the field named in this input will be compared to the value in PolicyRulesSkipped using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesSkipped must be specified if op_PolicyRulesSkipped is specified.
             :type val_f_PolicyRulesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesSkipped: If op_PolicyRulesSkipped is specified, this value will be compared to the value in PolicyRulesSkipped using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesSkipped must be specified if op_PolicyRulesSkipped is specified.
             :type val_c_PolicyRulesSkipped: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesTotal: The operator to apply to the field PolicyRulesTotal. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesTotal: The total number of rules that in this policy at the time the policy was executed against this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesTotal: If op_PolicyRulesTotal is specified, the field named in this input will be compared to the value in PolicyRulesTotal using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesTotal must be specified if op_PolicyRulesTotal is specified.
             :type val_f_PolicyRulesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesTotal: If op_PolicyRulesTotal is specified, this value will be compared to the value in PolicyRulesTotal using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesTotal must be specified if op_PolicyRulesTotal is specified.
             :type val_c_PolicyRulesTotal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesUnknown: The operator to apply to the field PolicyRulesUnknown. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesUnknown: The total number of rules that could not be fully evaluated because information needed for the rule was not available (for example, the configuration file has not been collected for the device). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesUnknown: If op_PolicyRulesUnknown is specified, the field named in this input will be compared to the value in PolicyRulesUnknown using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesUnknown must be specified if op_PolicyRulesUnknown is specified.
             :type val_f_PolicyRulesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesUnknown: If op_PolicyRulesUnknown is specified, this value will be compared to the value in PolicyRulesUnknown using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesUnknown must be specified if op_PolicyRulesUnknown is specified.
             :type val_c_PolicyRulesUnknown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesValid: The operator to apply to the field PolicyRulesValid. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesValid: The total number of valid rules that were in this policy at the time the policy was executed against this device. An invalid rule generally only occurs if the XML rule build has been used and an improper XML format has been specified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesValid: If op_PolicyRulesValid is specified, the field named in this input will be compared to the value in PolicyRulesValid using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesValid must be specified if op_PolicyRulesValid is specified.
             :type val_f_PolicyRulesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesValid: If op_PolicyRulesValid is specified, this value will be compared to the value in PolicyRulesValid using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesValid must be specified if op_PolicyRulesValid is specified.
             :type val_c_PolicyRulesValid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRulesWarning: The operator to apply to the field PolicyRulesWarning. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRulesWarning: The total number of rules in this policy that the device failed with warning status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRulesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRulesWarning: If op_PolicyRulesWarning is specified, the field named in this input will be compared to the value in PolicyRulesWarning using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRulesWarning must be specified if op_PolicyRulesWarning is specified.
             :type val_f_PolicyRulesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRulesWarning: If op_PolicyRulesWarning is specified, this value will be compared to the value in PolicyRulesWarning using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRulesWarning must be specified if op_PolicyRulesWarning is specified.
             :type val_c_PolicyRulesWarning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyStatus: The operator to apply to the field PolicyStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyStatus: The current status of this policy for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param timestamp: The data returned will represent the device policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy methods. The listed methods will be called on each device policy returned and included in the output. Available methods are: policy_name, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePolicyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyID. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown.
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

             :param select: The list of attributes to return for each DevicePolicy. Valid values are DevicePolicyID, DeviceID, PolicyID, DevicePolicyStartTime, DevicePolicyEndTime, DevicePolicyChangedCols, DevicePolicyTimestamp, DataSourceID, PolicyStatus, PolicyRulesTotal, PolicyRulesValid, PolicyRulesChecked, PolicyRulesInvalid, PolicyRulesPassed, PolicyRulesFailed, PolicyRulesError, PolicyRulesWarning, PolicyRulesInfo, PolicyRulesSkipped, PolicyRulesUnknown. If empty or omitted, all attributes will be returned.
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

             :return device_policies: An array of the DevicePolicy objects that match the specified input criteria.
             :rtype device_policies: Array of DevicePolicy

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def infradevice(self, **kwargs):
        """The device whose policy status this record represents.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device whose policy status this record represents.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def policy_name(self, **kwargs):
        """The policy name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The policy name.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_name"), kwargs)

    def device(self, **kwargs):
        """The device whose policy status this record represents.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for this device policy status record.
             :type DevicePolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device whose policy status this record represents.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def summary(self, **kwargs):
        """Provides a single method to retrieve policies, devices, and per-device, per-policy status summaries. The start/limit parameters apply to the devices, not to the policies. That is, if a device is returned, all of the policy status summaries for that device will be returned, regardless of the start/limit parameters.

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

             :return devices: The device information, as of the date and time specified in the timestamp parameter.
             :rtype devices: Array of Device

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_policies: The per-device, per-policy status.
             :rtype device_policies: Array of DevicePolicy

            """

        return self.api_list_request(self._get_method_fullname("summary"), kwargs)

    def count_statuses_by_device(self, **kwargs):
        """Returns a count of Policy Statuses for a specified device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal NetMRI identifier of the device.
             :type device_id: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` now

             :param timestamp: The date and time for which to retrieve the policy status.
             :type timestamp: DateTime

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return statuses_per_device: Array of hashes that contain a PoliciesTotal, PoliciesValid, PoliciesChecked, PoliciesInvalid, PoliciesPassed, PoliciesFailed, PoliciesError, PoliciesWarning, PoliciesInfo, PoliciesSkipped, PoliciesUnknown, DeviceID.
             :rtype statuses_per_device: Array

            """

        return self.api_request(self._get_method_fullname("count_statuses_by_device"), kwargs)
