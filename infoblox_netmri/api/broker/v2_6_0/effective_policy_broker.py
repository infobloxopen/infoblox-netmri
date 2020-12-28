from ..broker import Broker


class EffectivePolicyBroker(Broker):
    controller = "effective_policies"

    def show(self, **kwargs):
        """Shows the details for the specified effective policy.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy methods. The listed methods will be called on each effective policy returned and included in the output. Available methods are: policy_set_filter_text, data_source, device_policies, devices, device_group_policies.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device_policies, devices, device_group_policies.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return effective_policy: The effective policy identified by the specified PolicyID.
             :rtype effective_policy: EffectivePolicy

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available effective policies. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyShortName: The short name of the policy, as entered in the policy design center at the time of policy creation.
             :type PolicyShortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyShortName: The short name of the policy, as entered in the policy design center at the time of policy creation.
             :type PolicyShortName: Array of String

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

             :param timestamp: The data returned will represent the effective policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy methods. The listed methods will be called on each effective policy returned and included in the output. Available methods are: policy_set_filter_text, data_source, device_policies, devices, device_group_policies.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device_policies, devices, device_group_policies.
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
            |  ``default:`` PolicyID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyID. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicy. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :return effective_policies: An array of the EffectivePolicy objects that match the specified input criteria.
             :rtype effective_policies: Array of EffectivePolicy

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available effective policies matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param PolicyAuthor: The policy author name.
             :type PolicyAuthor: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyAuthor: The policy author name.
             :type PolicyAuthor: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PolicyChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type PolicyChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyCreatedAt: The date and time at which this policy was first created in NetMRI.
             :type PolicyCreatedAt: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyCreatedAt: The date and time at which this policy was first created in NetMRI.
             :type PolicyCreatedAt: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyDescription: The policy description, as entered at the time of policy execution.
             :type PolicyDescription: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyDescription: The policy description, as entered at the time of policy execution.
             :type PolicyDescription: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyEndTime: The ending effective time of this record, or empty if still in effect.
             :type PolicyEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyEndTime: The ending effective time of this record, or empty if still in effect.
             :type PolicyEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyFirstSeenTime: The data and time this policy was first seen (as identified by the policy short name).
             :type PolicyFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyFirstSeenTime: The data and time this policy was first seen (as identified by the policy short name).
             :type PolicyFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyName: The long name of the policy.
             :type PolicyName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyName: The long name of the policy.
             :type PolicyName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyReadOnlyInd: A flag indicating whether this policy was a read-only policy at the time of execution.
             :type PolicyReadOnlyInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyReadOnlyInd: A flag indicating whether this policy was a read-only policy at the time of execution.
             :type PolicyReadOnlyInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyScheduleMode: Not used.
             :type PolicyScheduleMode: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyScheduleMode: Not used.
             :type PolicyScheduleMode: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicySetFilter: The XML SetFilter used to define whether this policy applies to a given device.
             :type PolicySetFilter: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicySetFilter: The XML SetFilter used to define whether this policy applies to a given device.
             :type PolicySetFilter: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyShortName: The short name of the policy, as entered in the policy design center at the time of policy creation.
             :type PolicyShortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyShortName: The short name of the policy, as entered in the policy design center at the time of policy creation.
             :type PolicyShortName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStartTime: The starting effective time of this record.
             :type PolicyStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyStartTime: The starting effective time of this record.
             :type PolicyStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyTimestamp: The date and time this record was collected or calculated.
             :type PolicyTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyTimestamp: The date and time this record was collected or calculated.
             :type PolicyTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyUpdatedAt: The date and time at which this policy was last modified.
             :type PolicyUpdatedAt: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyUpdatedAt: The date and time at which this policy was last modified.
             :type PolicyUpdatedAt: Array of DateTime

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

             :param timestamp: The data returned will represent the effective policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy methods. The listed methods will be called on each effective policy returned and included in the output. Available methods are: policy_set_filter_text, data_source, device_policies, devices, device_group_policies.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device_policies, devices, device_group_policies.
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
            |  ``default:`` PolicyID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyID. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicy. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against effective policies, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, PolicyAuthor, PolicyChangedCols, PolicyCreatedAt, PolicyDescription, PolicyEndTime, PolicyFirstSeenTime, PolicyID, PolicyName, PolicyReadOnlyInd, PolicyScheduleMode, PolicySetFilter, PolicyShortName, PolicyStartTime, PolicyTimestamp, PolicyUpdatedAt.
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

             :return effective_policies: An array of the EffectivePolicy objects that match the specified input criteria.
             :rtype effective_policies: Array of EffectivePolicy

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available effective policies matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, PolicyAuthor, PolicyChangedCols, PolicyCreatedAt, PolicyDescription, PolicyEndTime, PolicyFirstSeenTime, PolicyID, PolicyName, PolicyReadOnlyInd, PolicyScheduleMode, PolicySetFilter, PolicyShortName, PolicyStartTime, PolicyTimestamp, PolicyUpdatedAt.

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

             :param op_PolicyAuthor: The operator to apply to the field PolicyAuthor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyAuthor: The policy author name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyAuthor: If op_PolicyAuthor is specified, the field named in this input will be compared to the value in PolicyAuthor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyAuthor must be specified if op_PolicyAuthor is specified.
             :type val_f_PolicyAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyAuthor: If op_PolicyAuthor is specified, this value will be compared to the value in PolicyAuthor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyAuthor must be specified if op_PolicyAuthor is specified.
             :type val_c_PolicyAuthor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyChangedCols: The operator to apply to the field PolicyChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyChangedCols: If op_PolicyChangedCols is specified, the field named in this input will be compared to the value in PolicyChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyChangedCols must be specified if op_PolicyChangedCols is specified.
             :type val_f_PolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyChangedCols: If op_PolicyChangedCols is specified, this value will be compared to the value in PolicyChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyChangedCols must be specified if op_PolicyChangedCols is specified.
             :type val_c_PolicyChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyCreatedAt: The operator to apply to the field PolicyCreatedAt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyCreatedAt: The date and time at which this policy was first created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyCreatedAt: If op_PolicyCreatedAt is specified, the field named in this input will be compared to the value in PolicyCreatedAt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyCreatedAt must be specified if op_PolicyCreatedAt is specified.
             :type val_f_PolicyCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyCreatedAt: If op_PolicyCreatedAt is specified, this value will be compared to the value in PolicyCreatedAt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyCreatedAt must be specified if op_PolicyCreatedAt is specified.
             :type val_c_PolicyCreatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyDescription: The operator to apply to the field PolicyDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyDescription: The policy description, as entered at the time of policy execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyDescription: If op_PolicyDescription is specified, the field named in this input will be compared to the value in PolicyDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyDescription must be specified if op_PolicyDescription is specified.
             :type val_f_PolicyDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyDescription: If op_PolicyDescription is specified, this value will be compared to the value in PolicyDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyDescription must be specified if op_PolicyDescription is specified.
             :type val_c_PolicyDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyEndTime: The operator to apply to the field PolicyEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyEndTime: If op_PolicyEndTime is specified, the field named in this input will be compared to the value in PolicyEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyEndTime must be specified if op_PolicyEndTime is specified.
             :type val_f_PolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyEndTime: If op_PolicyEndTime is specified, this value will be compared to the value in PolicyEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyEndTime must be specified if op_PolicyEndTime is specified.
             :type val_c_PolicyEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyFirstSeenTime: The operator to apply to the field PolicyFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyFirstSeenTime: The data and time this policy was first seen (as identified by the policy short name). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyFirstSeenTime: If op_PolicyFirstSeenTime is specified, the field named in this input will be compared to the value in PolicyFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyFirstSeenTime must be specified if op_PolicyFirstSeenTime is specified.
             :type val_f_PolicyFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyFirstSeenTime: If op_PolicyFirstSeenTime is specified, this value will be compared to the value in PolicyFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyFirstSeenTime must be specified if op_PolicyFirstSeenTime is specified.
             :type val_c_PolicyFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyID: The operator to apply to the field PolicyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyID: The internal NetMRI identifier for this effective policy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PolicyName: The operator to apply to the field PolicyName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyName: The long name of the policy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyName: If op_PolicyName is specified, the field named in this input will be compared to the value in PolicyName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyName must be specified if op_PolicyName is specified.
             :type val_f_PolicyName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyName: If op_PolicyName is specified, this value will be compared to the value in PolicyName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyName must be specified if op_PolicyName is specified.
             :type val_c_PolicyName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyReadOnlyInd: The operator to apply to the field PolicyReadOnlyInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyReadOnlyInd: A flag indicating whether this policy was a read-only policy at the time of execution. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyReadOnlyInd: If op_PolicyReadOnlyInd is specified, the field named in this input will be compared to the value in PolicyReadOnlyInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyReadOnlyInd must be specified if op_PolicyReadOnlyInd is specified.
             :type val_f_PolicyReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyReadOnlyInd: If op_PolicyReadOnlyInd is specified, this value will be compared to the value in PolicyReadOnlyInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyReadOnlyInd must be specified if op_PolicyReadOnlyInd is specified.
             :type val_c_PolicyReadOnlyInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyScheduleMode: The operator to apply to the field PolicyScheduleMode. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyScheduleMode: Not used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyScheduleMode: If op_PolicyScheduleMode is specified, the field named in this input will be compared to the value in PolicyScheduleMode using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyScheduleMode must be specified if op_PolicyScheduleMode is specified.
             :type val_f_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyScheduleMode: If op_PolicyScheduleMode is specified, this value will be compared to the value in PolicyScheduleMode using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyScheduleMode must be specified if op_PolicyScheduleMode is specified.
             :type val_c_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicySetFilter: The operator to apply to the field PolicySetFilter. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicySetFilter: The XML SetFilter used to define whether this policy applies to a given device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicySetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicySetFilter: If op_PolicySetFilter is specified, the field named in this input will be compared to the value in PolicySetFilter using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicySetFilter must be specified if op_PolicySetFilter is specified.
             :type val_f_PolicySetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicySetFilter: If op_PolicySetFilter is specified, this value will be compared to the value in PolicySetFilter using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicySetFilter must be specified if op_PolicySetFilter is specified.
             :type val_c_PolicySetFilter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyShortName: The operator to apply to the field PolicyShortName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyShortName: The short name of the policy, as entered in the policy design center at the time of policy creation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyShortName: If op_PolicyShortName is specified, the field named in this input will be compared to the value in PolicyShortName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyShortName must be specified if op_PolicyShortName is specified.
             :type val_f_PolicyShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyShortName: If op_PolicyShortName is specified, this value will be compared to the value in PolicyShortName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyShortName must be specified if op_PolicyShortName is specified.
             :type val_c_PolicyShortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyStartTime: The operator to apply to the field PolicyStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyStartTime: If op_PolicyStartTime is specified, the field named in this input will be compared to the value in PolicyStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyStartTime must be specified if op_PolicyStartTime is specified.
             :type val_f_PolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyStartTime: If op_PolicyStartTime is specified, this value will be compared to the value in PolicyStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyStartTime must be specified if op_PolicyStartTime is specified.
             :type val_c_PolicyStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyTimestamp: The operator to apply to the field PolicyTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyTimestamp: If op_PolicyTimestamp is specified, the field named in this input will be compared to the value in PolicyTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyTimestamp must be specified if op_PolicyTimestamp is specified.
             :type val_f_PolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyTimestamp: If op_PolicyTimestamp is specified, this value will be compared to the value in PolicyTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyTimestamp must be specified if op_PolicyTimestamp is specified.
             :type val_c_PolicyTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyUpdatedAt: The operator to apply to the field PolicyUpdatedAt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyUpdatedAt: The date and time at which this policy was last modified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyUpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyUpdatedAt: If op_PolicyUpdatedAt is specified, the field named in this input will be compared to the value in PolicyUpdatedAt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyUpdatedAt must be specified if op_PolicyUpdatedAt is specified.
             :type val_f_PolicyUpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyUpdatedAt: If op_PolicyUpdatedAt is specified, this value will be compared to the value in PolicyUpdatedAt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyUpdatedAt must be specified if op_PolicyUpdatedAt is specified.
             :type val_c_PolicyUpdatedAt: String

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

             :param timestamp: The data returned will represent the effective policies as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of effective policy methods. The listed methods will be called on each effective policy returned and included in the output. Available methods are: policy_set_filter_text, data_source, device_policies, devices, device_group_policies.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device_policies, devices, device_group_policies.
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
            |  ``default:`` PolicyID

             :param sort: The data field(s) to use for sorting the output. Default is PolicyID. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd.
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

             :param select: The list of attributes to return for each EffectivePolicy. Valid values are DataSourceID, PolicyID, PolicyStartTime, PolicyEndTime, PolicyChangedCols, PolicyTimestamp, PolicyFirstSeenTime, PolicyName, PolicyDescription, PolicyAuthor, PolicySetFilter, PolicyCreatedAt, PolicyUpdatedAt, PolicyScheduleMode, PolicyShortName, PolicyReadOnlyInd. If empty or omitted, all attributes will be returned.
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

             :return effective_policies: An array of the EffectivePolicy objects that match the specified input criteria.
             :rtype effective_policies: Array of EffectivePolicy

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def policy_set_filter_text(self, **kwargs):
        """Returns a human-readable text version of the policy set filter.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PolicyID: The internal NetMRI identifier for this effective policy.
             :type PolicyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Returns a human-readable text version of the policy set filter.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("policy_set_filter_text"), kwargs)
