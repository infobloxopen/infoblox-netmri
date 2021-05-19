from ..broker import Broker


class DevicePolicyRuleBroker(Broker):
    controller = "device_policy_rules"

    def show(self, **kwargs):
        """Shows the details for the specified device policy rule.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy rule methods. The listed methods will be called on each device policy rule returned and included in the output. Available methods are: policy_name, policy_rule_name, policy_rule_short_name, policy_rule_severity, data_source, device.
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

             :return device_policy_rule: The device policy rule identified by the specified DevicePolicyRuleID.
             :rtype device_policy_rule: DevicePolicyRule

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device policy rules. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for the corresponding device policy status.
             :type DevicePolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for the corresponding device policy status.
             :type DevicePolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Array of Integer

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

             :param timestamp: The data returned will represent the device policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy rule methods. The listed methods will be called on each device policy rule returned and included in the output. Available methods are: policy_name, policy_rule_name, policy_rule_short_name, policy_rule_severity, data_source, device.
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
            |  ``default:`` DevicePolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyRuleID. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext.
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

             :param select: The list of attributes to return for each DevicePolicyRule. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext. If empty or omitted, all attributes will be returned.
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

             :return device_policy_rules: An array of the DevicePolicyRule objects that match the specified input criteria.
             :rtype device_policy_rules: Array of DevicePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device policy rules matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DevicePolicyID: The internal NetMRI identifier for the corresponding device policy status.
             :type DevicePolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyID: The internal NetMRI identifier for the corresponding device policy status.
             :type DevicePolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevicePolicyRuleChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevicePolicyRuleChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevicePolicyRuleEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevicePolicyRuleEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleStartTime: The starting effective time of this record.
             :type DevicePolicyRuleStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleStartTime: The starting effective time of this record.
             :type DevicePolicyRuleStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleTimestamp: The date and time this record was collected or calculated.
             :type DevicePolicyRuleTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyRuleTimestamp: The date and time this record was collected or calculated.
             :type DevicePolicyRuleTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleContext: The specific lines within the device configuration file that surround and include the line in violation.
             :type PolicyRuleContext: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleContext: The specific lines within the device configuration file that surround and include the line in violation.
             :type PolicyRuleContext: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for the effective Policy Rule object.
             :type PolicyRuleID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for the effective Policy Rule object.
             :type PolicyRuleID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleLineNo: For configuration file rule violations, the line number in the device configuration file on which the violation occurs.
             :type PolicyRuleLineNo: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleLineNo: For configuration file rule violations, the line number in the device configuration file on which the violation occurs.
             :type PolicyRuleLineNo: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleMessage: The textual message associated with this policy rule status.
             :type PolicyRuleMessage: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleMessage: The textual message associated with this policy rule status.
             :type PolicyRuleMessage: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleStatus: The policy rule status result for the evaluation of the specified rule against the corresponding device (see DevicePolicy to retrieve the device).
             :type PolicyRuleStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleStatus: The policy rule status result for the evaluation of the specified rule against the corresponding device (see DevicePolicy to retrieve the device).
             :type PolicyRuleStatus: Array of String

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

             :param timestamp: The data returned will represent the device policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy rule methods. The listed methods will be called on each device policy rule returned and included in the output. Available methods are: policy_name, policy_rule_name, policy_rule_short_name, policy_rule_severity, data_source, device.
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
            |  ``default:`` DevicePolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyRuleID. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext.
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

             :param select: The list of attributes to return for each DevicePolicyRule. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device policy rules, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DevicePolicyID, DevicePolicyRuleChangedCols, DevicePolicyRuleEndTime, DevicePolicyRuleID, DevicePolicyRuleStartTime, DevicePolicyRuleTimestamp, PolicyRuleContext, PolicyRuleID, PolicyRuleLineNo, PolicyRuleMessage, PolicyRuleStatus.
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

             :return device_policy_rules: An array of the DevicePolicyRule objects that match the specified input criteria.
             :rtype device_policy_rules: Array of DevicePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device policy rules matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DevicePolicyID, DevicePolicyRuleChangedCols, DevicePolicyRuleEndTime, DevicePolicyRuleID, DevicePolicyRuleStartTime, DevicePolicyRuleTimestamp, PolicyRuleContext, PolicyRuleID, PolicyRuleLineNo, PolicyRuleMessage, PolicyRuleStatus.

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

             :param op_DevicePolicyID: The operator to apply to the field DevicePolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyID: The internal NetMRI identifier for the corresponding device policy status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DevicePolicyRuleChangedCols: The operator to apply to the field DevicePolicyRuleChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyRuleChangedCols: If op_DevicePolicyRuleChangedCols is specified, the field named in this input will be compared to the value in DevicePolicyRuleChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyRuleChangedCols must be specified if op_DevicePolicyRuleChangedCols is specified.
             :type val_f_DevicePolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyRuleChangedCols: If op_DevicePolicyRuleChangedCols is specified, this value will be compared to the value in DevicePolicyRuleChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyRuleChangedCols must be specified if op_DevicePolicyRuleChangedCols is specified.
             :type val_c_DevicePolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyRuleEndTime: The operator to apply to the field DevicePolicyRuleEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyRuleEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyRuleEndTime: If op_DevicePolicyRuleEndTime is specified, the field named in this input will be compared to the value in DevicePolicyRuleEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyRuleEndTime must be specified if op_DevicePolicyRuleEndTime is specified.
             :type val_f_DevicePolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyRuleEndTime: If op_DevicePolicyRuleEndTime is specified, this value will be compared to the value in DevicePolicyRuleEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyRuleEndTime must be specified if op_DevicePolicyRuleEndTime is specified.
             :type val_c_DevicePolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyRuleID: The operator to apply to the field DevicePolicyRuleID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyRuleID: If op_DevicePolicyRuleID is specified, the field named in this input will be compared to the value in DevicePolicyRuleID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyRuleID must be specified if op_DevicePolicyRuleID is specified.
             :type val_f_DevicePolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyRuleID: If op_DevicePolicyRuleID is specified, this value will be compared to the value in DevicePolicyRuleID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyRuleID must be specified if op_DevicePolicyRuleID is specified.
             :type val_c_DevicePolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyRuleStartTime: The operator to apply to the field DevicePolicyRuleStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyRuleStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyRuleStartTime: If op_DevicePolicyRuleStartTime is specified, the field named in this input will be compared to the value in DevicePolicyRuleStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyRuleStartTime must be specified if op_DevicePolicyRuleStartTime is specified.
             :type val_f_DevicePolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyRuleStartTime: If op_DevicePolicyRuleStartTime is specified, this value will be compared to the value in DevicePolicyRuleStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyRuleStartTime must be specified if op_DevicePolicyRuleStartTime is specified.
             :type val_c_DevicePolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyRuleTimestamp: The operator to apply to the field DevicePolicyRuleTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyRuleTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyRuleTimestamp: If op_DevicePolicyRuleTimestamp is specified, the field named in this input will be compared to the value in DevicePolicyRuleTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyRuleTimestamp must be specified if op_DevicePolicyRuleTimestamp is specified.
             :type val_f_DevicePolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyRuleTimestamp: If op_DevicePolicyRuleTimestamp is specified, this value will be compared to the value in DevicePolicyRuleTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyRuleTimestamp must be specified if op_DevicePolicyRuleTimestamp is specified.
             :type val_c_DevicePolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleContext: The operator to apply to the field PolicyRuleContext. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleContext: The specific lines within the device configuration file that surround and include the line in violation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleContext: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleContext: If op_PolicyRuleContext is specified, the field named in this input will be compared to the value in PolicyRuleContext using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleContext must be specified if op_PolicyRuleContext is specified.
             :type val_f_PolicyRuleContext: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleContext: If op_PolicyRuleContext is specified, this value will be compared to the value in PolicyRuleContext using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleContext must be specified if op_PolicyRuleContext is specified.
             :type val_c_PolicyRuleContext: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleID: The operator to apply to the field PolicyRuleID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleID: The internal NetMRI identifier for the effective Policy Rule object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleID: If op_PolicyRuleID is specified, the field named in this input will be compared to the value in PolicyRuleID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleID must be specified if op_PolicyRuleID is specified.
             :type val_f_PolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleID: If op_PolicyRuleID is specified, this value will be compared to the value in PolicyRuleID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleID must be specified if op_PolicyRuleID is specified.
             :type val_c_PolicyRuleID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleLineNo: The operator to apply to the field PolicyRuleLineNo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleLineNo: For configuration file rule violations, the line number in the device configuration file on which the violation occurs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleLineNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleLineNo: If op_PolicyRuleLineNo is specified, the field named in this input will be compared to the value in PolicyRuleLineNo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleLineNo must be specified if op_PolicyRuleLineNo is specified.
             :type val_f_PolicyRuleLineNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleLineNo: If op_PolicyRuleLineNo is specified, this value will be compared to the value in PolicyRuleLineNo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleLineNo must be specified if op_PolicyRuleLineNo is specified.
             :type val_c_PolicyRuleLineNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleMessage: The operator to apply to the field PolicyRuleMessage. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleMessage: The textual message associated with this policy rule status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleMessage: If op_PolicyRuleMessage is specified, the field named in this input will be compared to the value in PolicyRuleMessage using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleMessage must be specified if op_PolicyRuleMessage is specified.
             :type val_f_PolicyRuleMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleMessage: If op_PolicyRuleMessage is specified, this value will be compared to the value in PolicyRuleMessage using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleMessage must be specified if op_PolicyRuleMessage is specified.
             :type val_c_PolicyRuleMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleStatus: The operator to apply to the field PolicyRuleStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleStatus: The policy rule status result for the evaluation of the specified rule against the corresponding device (see DevicePolicy to retrieve the device). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleStatus: If op_PolicyRuleStatus is specified, the field named in this input will be compared to the value in PolicyRuleStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleStatus must be specified if op_PolicyRuleStatus is specified.
             :type val_f_PolicyRuleStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleStatus: If op_PolicyRuleStatus is specified, this value will be compared to the value in PolicyRuleStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleStatus must be specified if op_PolicyRuleStatus is specified.
             :type val_c_PolicyRuleStatus: String

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

             :param timestamp: The data returned will represent the device policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device policy rule methods. The listed methods will be called on each device policy rule returned and included in the output. Available methods are: policy_name, policy_rule_name, policy_rule_short_name, policy_rule_severity, data_source, device.
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
            |  ``default:`` DevicePolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePolicyRuleID. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext.
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

             :param select: The list of attributes to return for each DevicePolicyRule. Valid values are DevicePolicyRuleID, DevicePolicyID, DevicePolicyRuleStartTime, DevicePolicyRuleEndTime, DevicePolicyRuleChangedCols, DevicePolicyRuleTimestamp, DataSourceID, PolicyRuleID, PolicyRuleStatus, PolicyRuleMessage, PolicyRuleLineNo, PolicyRuleContext. If empty or omitted, all attributes will be returned.
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

             :return device_policy_rules: An array of the DevicePolicyRule objects that match the specified input criteria.
             :rtype device_policy_rules: Array of DevicePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

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
        """The policy name associated with this usage of the rulelist.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The policy name associated with this usage of the rulelist.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_name"), kwargs)

    def policy_rule_name(self, **kwargs):
        """The rule name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The rule name.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_rule_name"), kwargs)

    def policy_rule_short_name(self, **kwargs):
        """The short rule name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The short rule name.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_rule_short_name"), kwargs)

    def policy_rule_severity(self, **kwargs):
        """The rule severity.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The rule severity.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_rule_severity"), kwargs)

    def device(self, **kwargs):
        """The device to which this policy rule is attached.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePolicyRuleID: The internal NetMRI identifier for this device policy rule status.
             :type DevicePolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device to which this policy rule is attached.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def policy_summary(self, **kwargs):
        """Provides a single method to retrieve a policy, it's rules, devices, and per-device, per-policy rule status records. The start/limit parameters apply to the devices, not to the policy rules. That is, if a device is returned, all of the policy rule status records for that device and policy will be returned, regardless of the start/limit parameters.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param policy_id: The internal NetMRI Effective Policy identifiers for the policy of interest.
             :type policy_id: Integer

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

             :param show_skipped_ind: If true, the results will include devices with policy rule status 'Skipped'.
             :type show_skipped_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The date and time for which to retrieve the policy rule status. The current status will be returned if omitted.
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

             :return effective_policy: The policy as it was defined at the date and time specified in the timestamp parameter.
             :rtype effective_policy: EffectivePolicy

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return effective_policy_rules: The policy rules for the specified policy, as they were defined at the date and time specified in the timestamp parameter.
             :rtype effective_policy_rules: Array of EffectivePolicyRule

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

             :return device_policy_rules: The per-device, per-policy rule status.
             :rtype device_policy_rules: Array of DevicePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("policy_summary"), kwargs)
