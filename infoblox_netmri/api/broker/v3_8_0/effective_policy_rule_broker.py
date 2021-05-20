from ..broker import Broker


class EffectivePolicyRuleBroker(Broker):
    controller = "effective_policy_rules"

    def show(self, **kwargs):
        """Shows the details for the specified effective policy rule.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy rule methods. The listed methods will be called on each effective policy rule returned and included in the output. Available methods are: policy_rule_set_filter_text, policy_rule_rule_logic_text, devices, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return effective_policy_rule: The effective policy rule identified by the specified PolicyRuleID.
             :rtype effective_policy_rule: EffectivePolicyRule

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available effective policy rules. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleShortName: The policy rule short name, used on the policy status display.
             :type PolicyRuleShortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleShortName: The policy rule short name, used on the policy status display.
             :type PolicyRuleShortName: Array of String

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

             :param timestamp: The data returned will represent the effective policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy rule methods. The listed methods will be called on each effective policy rule returned and included in the output. Available methods are: policy_rule_set_filter_text, policy_rule_rule_logic_text, devices, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` PolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyRuleID. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicyRule. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :return effective_policy_rules: An array of the EffectivePolicyRule objects that match the specified input criteria.
             :rtype effective_policy_rules: Array of EffectivePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available effective policy rules matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param PolicyRuleActionAfterExec: Not used.
             :type PolicyRuleActionAfterExec: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleActionAfterExec: Not used.
             :type PolicyRuleActionAfterExec: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleAuthor: The author of the policy rule at the time of evaluation.
             :type PolicyRuleAuthor: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleAuthor: The author of the policy rule at the time of evaluation.
             :type PolicyRuleAuthor: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PolicyRuleChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PolicyRuleChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleCreatedAt: The date and time the policy rule was first added to NetMRI.
             :type PolicyRuleCreatedAt: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleCreatedAt: The date and time the policy rule was first added to NetMRI.
             :type PolicyRuleCreatedAt: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleDescription: The description of the policy rule at the time of evaluation.
             :type PolicyRuleDescription: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleDescription: The description of the policy rule at the time of evaluation.
             :type PolicyRuleDescription: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleEndTime: The ending effective time of this record, or empty if still in effect.
             :type PolicyRuleEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleEndTime: The ending effective time of this record, or empty if still in effect.
             :type PolicyRuleEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleFirstSeenTime: The date and time when this policy rule was first seen on the NetMRI.
             :type PolicyRuleFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleFirstSeenTime: The date and time when this policy rule was first seen on the NetMRI.
             :type PolicyRuleFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleName: The long name of the policy rule.
             :type PolicyRuleName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleName: The long name of the policy rule.
             :type PolicyRuleName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleReadOnlyInd: A flag indicating whether this is a read-only policy rule.
             :type PolicyRuleReadOnlyInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleReadOnlyInd: A flag indicating whether this is a read-only policy rule.
             :type PolicyRuleReadOnlyInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleRemediation: The textual remediation description associated with the rule.
             :type PolicyRuleRemediation: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleRemediation: The textual remediation description associated with the rule.
             :type PolicyRuleRemediation: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleRuleLogic: The XML policy rule logic.
             :type PolicyRuleRuleLogic: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleRuleLogic: The XML policy rule logic.
             :type PolicyRuleRuleLogic: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleSetFilter: The XML SetFilter used to determine if this rule applies to a specific device.
             :type PolicyRuleSetFilter: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleSetFilter: The XML SetFilter used to determine if this rule applies to a specific device.
             :type PolicyRuleSetFilter: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleSeverity: The severity level (info, warning, or error) for a violation of this rule.
             :type PolicyRuleSeverity: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleSeverity: The severity level (info, warning, or error) for a violation of this rule.
             :type PolicyRuleSeverity: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleShortName: The policy rule short name, used on the policy status display.
             :type PolicyRuleShortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleShortName: The policy rule short name, used on the policy status display.
             :type PolicyRuleShortName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleStartTime: The starting effective time of this record.
             :type PolicyRuleStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleStartTime: The starting effective time of this record.
             :type PolicyRuleStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleTimestamp: The date and time this record was collected or calculated.
             :type PolicyRuleTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleTimestamp: The date and time this record was collected or calculated.
             :type PolicyRuleTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleUpdatedAt: The date and time the policy rule was last updated in NetMRI.
             :type PolicyRuleUpdatedAt: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyRuleUpdatedAt: The date and time the policy rule was last updated in NetMRI.
             :type PolicyRuleUpdatedAt: Array of String

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

             :param timestamp: The data returned will represent the effective policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy rule methods. The listed methods will be called on each effective policy rule returned and included in the output. Available methods are: policy_rule_set_filter_text, policy_rule_rule_logic_text, devices, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` PolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyRuleID. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicyRule. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against effective policy rules, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, PolicyRuleActionAfterExec, PolicyRuleAuthor, PolicyRuleChangedCols, PolicyRuleCreatedAt, PolicyRuleDescription, PolicyRuleEndTime, PolicyRuleFirstSeenTime, PolicyRuleID, PolicyRuleName, PolicyRuleReadOnlyInd, PolicyRuleRemediation, PolicyRuleRuleLogic, PolicyRuleSetFilter, PolicyRuleSeverity, PolicyRuleShortName, PolicyRuleStartTime, PolicyRuleTimestamp, PolicyRuleUpdatedAt.
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

             :return effective_policy_rules: An array of the EffectivePolicyRule objects that match the specified input criteria.
             :rtype effective_policy_rules: Array of EffectivePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available effective policy rules matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, PolicyRuleActionAfterExec, PolicyRuleAuthor, PolicyRuleChangedCols, PolicyRuleCreatedAt, PolicyRuleDescription, PolicyRuleEndTime, PolicyRuleFirstSeenTime, PolicyRuleID, PolicyRuleName, PolicyRuleReadOnlyInd, PolicyRuleRemediation, PolicyRuleRuleLogic, PolicyRuleSetFilter, PolicyRuleSeverity, PolicyRuleShortName, PolicyRuleStartTime, PolicyRuleTimestamp, PolicyRuleUpdatedAt.

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

             :param op_PolicyRuleActionAfterExec: The operator to apply to the field PolicyRuleActionAfterExec. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleActionAfterExec: Not used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleActionAfterExec: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleActionAfterExec: If op_PolicyRuleActionAfterExec is specified, the field named in this input will be compared to the value in PolicyRuleActionAfterExec using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleActionAfterExec must be specified if op_PolicyRuleActionAfterExec is specified.
             :type val_f_PolicyRuleActionAfterExec: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleActionAfterExec: If op_PolicyRuleActionAfterExec is specified, this value will be compared to the value in PolicyRuleActionAfterExec using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleActionAfterExec must be specified if op_PolicyRuleActionAfterExec is specified.
             :type val_c_PolicyRuleActionAfterExec: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleAuthor: The operator to apply to the field PolicyRuleAuthor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleAuthor: The author of the policy rule at the time of evaluation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleAuthor: If op_PolicyRuleAuthor is specified, the field named in this input will be compared to the value in PolicyRuleAuthor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleAuthor must be specified if op_PolicyRuleAuthor is specified.
             :type val_f_PolicyRuleAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleAuthor: If op_PolicyRuleAuthor is specified, this value will be compared to the value in PolicyRuleAuthor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleAuthor must be specified if op_PolicyRuleAuthor is specified.
             :type val_c_PolicyRuleAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleChangedCols: The operator to apply to the field PolicyRuleChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleChangedCols: If op_PolicyRuleChangedCols is specified, the field named in this input will be compared to the value in PolicyRuleChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleChangedCols must be specified if op_PolicyRuleChangedCols is specified.
             :type val_f_PolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleChangedCols: If op_PolicyRuleChangedCols is specified, this value will be compared to the value in PolicyRuleChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleChangedCols must be specified if op_PolicyRuleChangedCols is specified.
             :type val_c_PolicyRuleChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleCreatedAt: The operator to apply to the field PolicyRuleCreatedAt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleCreatedAt: The date and time the policy rule was first added to NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleCreatedAt: If op_PolicyRuleCreatedAt is specified, the field named in this input will be compared to the value in PolicyRuleCreatedAt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleCreatedAt must be specified if op_PolicyRuleCreatedAt is specified.
             :type val_f_PolicyRuleCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleCreatedAt: If op_PolicyRuleCreatedAt is specified, this value will be compared to the value in PolicyRuleCreatedAt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleCreatedAt must be specified if op_PolicyRuleCreatedAt is specified.
             :type val_c_PolicyRuleCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleDescription: The operator to apply to the field PolicyRuleDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleDescription: The description of the policy rule at the time of evaluation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleDescription: If op_PolicyRuleDescription is specified, the field named in this input will be compared to the value in PolicyRuleDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleDescription must be specified if op_PolicyRuleDescription is specified.
             :type val_f_PolicyRuleDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleDescription: If op_PolicyRuleDescription is specified, this value will be compared to the value in PolicyRuleDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleDescription must be specified if op_PolicyRuleDescription is specified.
             :type val_c_PolicyRuleDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleEndTime: The operator to apply to the field PolicyRuleEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleEndTime: If op_PolicyRuleEndTime is specified, the field named in this input will be compared to the value in PolicyRuleEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleEndTime must be specified if op_PolicyRuleEndTime is specified.
             :type val_f_PolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleEndTime: If op_PolicyRuleEndTime is specified, this value will be compared to the value in PolicyRuleEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleEndTime must be specified if op_PolicyRuleEndTime is specified.
             :type val_c_PolicyRuleEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleFirstSeenTime: The operator to apply to the field PolicyRuleFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleFirstSeenTime: The date and time when this policy rule was first seen on the NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleFirstSeenTime: If op_PolicyRuleFirstSeenTime is specified, the field named in this input will be compared to the value in PolicyRuleFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleFirstSeenTime must be specified if op_PolicyRuleFirstSeenTime is specified.
             :type val_f_PolicyRuleFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleFirstSeenTime: If op_PolicyRuleFirstSeenTime is specified, this value will be compared to the value in PolicyRuleFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleFirstSeenTime must be specified if op_PolicyRuleFirstSeenTime is specified.
             :type val_c_PolicyRuleFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleID: The operator to apply to the field PolicyRuleID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleID: The internal NetMRI identifier for this effective policy rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PolicyRuleName: The operator to apply to the field PolicyRuleName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleName: The long name of the policy rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleName: If op_PolicyRuleName is specified, the field named in this input will be compared to the value in PolicyRuleName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleName must be specified if op_PolicyRuleName is specified.
             :type val_f_PolicyRuleName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleName: If op_PolicyRuleName is specified, this value will be compared to the value in PolicyRuleName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleName must be specified if op_PolicyRuleName is specified.
             :type val_c_PolicyRuleName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleReadOnlyInd: The operator to apply to the field PolicyRuleReadOnlyInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleReadOnlyInd: A flag indicating whether this is a read-only policy rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleReadOnlyInd: If op_PolicyRuleReadOnlyInd is specified, the field named in this input will be compared to the value in PolicyRuleReadOnlyInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleReadOnlyInd must be specified if op_PolicyRuleReadOnlyInd is specified.
             :type val_f_PolicyRuleReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleReadOnlyInd: If op_PolicyRuleReadOnlyInd is specified, this value will be compared to the value in PolicyRuleReadOnlyInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleReadOnlyInd must be specified if op_PolicyRuleReadOnlyInd is specified.
             :type val_c_PolicyRuleReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleRemediation: The operator to apply to the field PolicyRuleRemediation. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleRemediation: The textual remediation description associated with the rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleRemediation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleRemediation: If op_PolicyRuleRemediation is specified, the field named in this input will be compared to the value in PolicyRuleRemediation using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleRemediation must be specified if op_PolicyRuleRemediation is specified.
             :type val_f_PolicyRuleRemediation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleRemediation: If op_PolicyRuleRemediation is specified, this value will be compared to the value in PolicyRuleRemediation using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleRemediation must be specified if op_PolicyRuleRemediation is specified.
             :type val_c_PolicyRuleRemediation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleRuleLogic: The operator to apply to the field PolicyRuleRuleLogic. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleRuleLogic: The XML policy rule logic. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleRuleLogic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleRuleLogic: If op_PolicyRuleRuleLogic is specified, the field named in this input will be compared to the value in PolicyRuleRuleLogic using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleRuleLogic must be specified if op_PolicyRuleRuleLogic is specified.
             :type val_f_PolicyRuleRuleLogic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleRuleLogic: If op_PolicyRuleRuleLogic is specified, this value will be compared to the value in PolicyRuleRuleLogic using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleRuleLogic must be specified if op_PolicyRuleRuleLogic is specified.
             :type val_c_PolicyRuleRuleLogic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleSetFilter: The operator to apply to the field PolicyRuleSetFilter. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleSetFilter: The XML SetFilter used to determine if this rule applies to a specific device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleSetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleSetFilter: If op_PolicyRuleSetFilter is specified, the field named in this input will be compared to the value in PolicyRuleSetFilter using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleSetFilter must be specified if op_PolicyRuleSetFilter is specified.
             :type val_f_PolicyRuleSetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleSetFilter: If op_PolicyRuleSetFilter is specified, this value will be compared to the value in PolicyRuleSetFilter using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleSetFilter must be specified if op_PolicyRuleSetFilter is specified.
             :type val_c_PolicyRuleSetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleSeverity: The operator to apply to the field PolicyRuleSeverity. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleSeverity: The severity level (info, warning, or error) for a violation of this rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleSeverity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleSeverity: If op_PolicyRuleSeverity is specified, the field named in this input will be compared to the value in PolicyRuleSeverity using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleSeverity must be specified if op_PolicyRuleSeverity is specified.
             :type val_f_PolicyRuleSeverity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleSeverity: If op_PolicyRuleSeverity is specified, this value will be compared to the value in PolicyRuleSeverity using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleSeverity must be specified if op_PolicyRuleSeverity is specified.
             :type val_c_PolicyRuleSeverity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleShortName: The operator to apply to the field PolicyRuleShortName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleShortName: The policy rule short name, used on the policy status display. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleShortName: If op_PolicyRuleShortName is specified, the field named in this input will be compared to the value in PolicyRuleShortName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleShortName must be specified if op_PolicyRuleShortName is specified.
             :type val_f_PolicyRuleShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleShortName: If op_PolicyRuleShortName is specified, this value will be compared to the value in PolicyRuleShortName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleShortName must be specified if op_PolicyRuleShortName is specified.
             :type val_c_PolicyRuleShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleStartTime: The operator to apply to the field PolicyRuleStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleStartTime: If op_PolicyRuleStartTime is specified, the field named in this input will be compared to the value in PolicyRuleStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleStartTime must be specified if op_PolicyRuleStartTime is specified.
             :type val_f_PolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleStartTime: If op_PolicyRuleStartTime is specified, this value will be compared to the value in PolicyRuleStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleStartTime must be specified if op_PolicyRuleStartTime is specified.
             :type val_c_PolicyRuleStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleTimestamp: The operator to apply to the field PolicyRuleTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleTimestamp: If op_PolicyRuleTimestamp is specified, the field named in this input will be compared to the value in PolicyRuleTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleTimestamp must be specified if op_PolicyRuleTimestamp is specified.
             :type val_f_PolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleTimestamp: If op_PolicyRuleTimestamp is specified, this value will be compared to the value in PolicyRuleTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleTimestamp must be specified if op_PolicyRuleTimestamp is specified.
             :type val_c_PolicyRuleTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyRuleUpdatedAt: The operator to apply to the field PolicyRuleUpdatedAt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyRuleUpdatedAt: The date and time the policy rule was last updated in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyRuleUpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyRuleUpdatedAt: If op_PolicyRuleUpdatedAt is specified, the field named in this input will be compared to the value in PolicyRuleUpdatedAt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyRuleUpdatedAt must be specified if op_PolicyRuleUpdatedAt is specified.
             :type val_f_PolicyRuleUpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyRuleUpdatedAt: If op_PolicyRuleUpdatedAt is specified, this value will be compared to the value in PolicyRuleUpdatedAt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyRuleUpdatedAt must be specified if op_PolicyRuleUpdatedAt is specified.
             :type val_c_PolicyRuleUpdatedAt: String

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

             :param timestamp: The data returned will represent the effective policy rules as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy rule methods. The listed methods will be called on each effective policy rule returned and included in the output. Available methods are: policy_rule_set_filter_text, policy_rule_rule_logic_text, devices, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` PolicyRuleID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyRuleID. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicyRule. Valid values are DataSourceID, PolicyRuleID, PolicyRuleStartTime, PolicyRuleEndTime, PolicyRuleChangedCols, PolicyRuleTimestamp, PolicyRuleFirstSeenTime, PolicyRuleName, PolicyRuleDescription, PolicyRuleAuthor, PolicyRuleSetFilter, PolicyRuleRuleLogic, PolicyRuleSeverity, PolicyRuleActionAfterExec, PolicyRuleCreatedAt, PolicyRuleUpdatedAt, PolicyRuleRemediation, PolicyRuleShortName, PolicyRuleReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :return effective_policy_rules: An array of the EffectivePolicyRule objects that match the specified input criteria.
             :rtype effective_policy_rules: Array of EffectivePolicyRule

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def devices(self, **kwargs):
        """The devices against which this rule was evaluated.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The devices against which this rule was evaluated.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("devices"), kwargs)

    def policy_rule_set_filter_text(self, **kwargs):
        """Returns a human-readable text version of the policy rule set filter.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Returns a human-readable text version of the policy rule set filter.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_rule_set_filter_text"), kwargs)

    def policy_rule_rule_logic_text(self, **kwargs):
        """Returns a human readable text version of the policy rule logic.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyRuleID: The internal NetMRI identifier for this effective policy rule.
             :type PolicyRuleID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Returns a human readable text version of the policy rule logic.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_rule_rule_logic_text"), kwargs)
