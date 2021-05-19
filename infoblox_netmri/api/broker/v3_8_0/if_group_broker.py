from ..broker import Broker


class IfGroupBroker(Broker):
    controller = "if_groups"

    def index(self, **kwargs):
        """Lists the available if groups. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group methods. The listed methods will be called on each if group returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` IfGroupID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupID. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount.
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

             :param select: The list of attributes to return for each IfGroup. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount. If empty or omitted, all attributes will be returned.
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

             :return if_groups: An array of the IfGroup objects that match the specified input criteria.
             :rtype if_groups: Array of IfGroup

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified if group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group methods. The listed methods will be called on each if group returned and included in the output. Available methods are: data_source.
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

             :return if_group: The if group identified by the specified IfGroupID.
             :rtype if_group: IfGroup

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available if groups matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The interface group criteria, which define the group memberships.
             :type Criteria: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The interface group criteria, which define the group memberships.
             :type Criteria: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The Flow Collection indicator of the Group.
             :type FlowCollection: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The Flow Collection indicator of the Group.
             :type FlowCollection: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for the interface group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for the interface group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The interface group name.
             :type GroupName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The interface group name.
             :type GroupName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The number of interfaces in this interface group.
             :type MemberCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The number of interfaces in this interface group.
             :type MemberCount: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The Group performance data gathering frequency indicator.
             :type PerfFrequency: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The Group performance data gathering frequency indicator.
             :type PerfFrequency: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The Group rank.
             :type Rank: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The Group rank.
             :type Rank: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP Polling indicator of the Group.
             :type SNMPPolling: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP Polling indicator of the Group.
             :type SNMPPolling: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifGroupChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifGroupChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifGroupEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifGroupEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupStartTime: The starting effective time of this record.
             :type ifGroupStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupStartTime: The starting effective time of this record.
             :type ifGroupStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupTimestamp: The date and time this record was collected or calculated.
             :type ifGroupTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupTimestamp: The date and time this record was collected or calculated.
             :type ifGroupTimestamp: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group methods. The listed methods will be called on each if group returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` IfGroupID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupID. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount.
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

             :param select: The list of attributes to return for each IfGroup. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if groups, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: Criteria, DataSourceID, FlowCollection, GroupID, GroupName, IfGroupID, MemberCount, PerfFrequency, Rank, SNMPPolling, Timestamp, ifGroupChangedCols, ifGroupEndTime, ifGroupStartTime, ifGroupTimestamp.
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

             :return if_groups: An array of the IfGroup objects that match the specified input criteria.
             :rtype if_groups: Array of IfGroup

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if groups matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: Criteria, DataSourceID, FlowCollection, GroupID, GroupName, IfGroupID, MemberCount, PerfFrequency, Rank, SNMPPolling, Timestamp, ifGroupChangedCols, ifGroupEndTime, ifGroupStartTime, ifGroupTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Criteria: The operator to apply to the field Criteria. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Criteria: The interface group criteria, which define the group memberships. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Criteria: If op_Criteria is specified, the field named in this input will be compared to the value in Criteria using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Criteria must be specified if op_Criteria is specified.
             :type val_f_Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Criteria: If op_Criteria is specified, this value will be compared to the value in Criteria using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Criteria must be specified if op_Criteria is specified.
             :type val_c_Criteria: String

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

             :param op_FlowCollection: The operator to apply to the field FlowCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FlowCollection: The Flow Collection indicator of the Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FlowCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FlowCollection: If op_FlowCollection is specified, the field named in this input will be compared to the value in FlowCollection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FlowCollection must be specified if op_FlowCollection is specified.
             :type val_f_FlowCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FlowCollection: If op_FlowCollection is specified, this value will be compared to the value in FlowCollection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FlowCollection must be specified if op_FlowCollection is specified.
             :type val_c_FlowCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GroupID: The operator to apply to the field GroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupID: The internal NetMRI identifier for the interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_GroupName: The operator to apply to the field GroupName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupName: The interface group name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GroupName: If op_GroupName is specified, the field named in this input will be compared to the value in GroupName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GroupName must be specified if op_GroupName is specified.
             :type val_f_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GroupName: If op_GroupName is specified, this value will be compared to the value in GroupName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GroupName must be specified if op_GroupName is specified.
             :type val_c_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IfGroupID: The operator to apply to the field IfGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfGroupID: The internal NetMRI identifier for the interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfGroupID: If op_IfGroupID is specified, the field named in this input will be compared to the value in IfGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfGroupID must be specified if op_IfGroupID is specified.
             :type val_f_IfGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfGroupID: If op_IfGroupID is specified, this value will be compared to the value in IfGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfGroupID must be specified if op_IfGroupID is specified.
             :type val_c_IfGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemberCount: The operator to apply to the field MemberCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemberCount: The number of interfaces in this interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemberCount: If op_MemberCount is specified, the field named in this input will be compared to the value in MemberCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemberCount must be specified if op_MemberCount is specified.
             :type val_f_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemberCount: If op_MemberCount is specified, this value will be compared to the value in MemberCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemberCount must be specified if op_MemberCount is specified.
             :type val_c_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PerfFrequency: The operator to apply to the field PerfFrequency. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PerfFrequency: The Group performance data gathering frequency indicator. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PerfFrequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PerfFrequency: If op_PerfFrequency is specified, the field named in this input will be compared to the value in PerfFrequency using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PerfFrequency must be specified if op_PerfFrequency is specified.
             :type val_f_PerfFrequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PerfFrequency: If op_PerfFrequency is specified, this value will be compared to the value in PerfFrequency using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PerfFrequency must be specified if op_PerfFrequency is specified.
             :type val_c_PerfFrequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Rank: The operator to apply to the field Rank. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Rank: The Group rank. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Rank: If op_Rank is specified, the field named in this input will be compared to the value in Rank using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Rank must be specified if op_Rank is specified.
             :type val_f_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Rank: If op_Rank is specified, this value will be compared to the value in Rank using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Rank must be specified if op_Rank is specified.
             :type val_c_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPPolling: The operator to apply to the field SNMPPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPolling: The SNMP Polling indicator of the Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPPolling: If op_SNMPPolling is specified, the field named in this input will be compared to the value in SNMPPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPPolling must be specified if op_SNMPPolling is specified.
             :type val_f_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPPolling: If op_SNMPPolling is specified, this value will be compared to the value in SNMPPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPPolling must be specified if op_SNMPPolling is specified.
             :type val_c_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Timestamp: The operator to apply to the field Timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Timestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Timestamp: If op_Timestamp is specified, the field named in this input will be compared to the value in Timestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Timestamp must be specified if op_Timestamp is specified.
             :type val_f_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Timestamp: If op_Timestamp is specified, this value will be compared to the value in Timestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Timestamp must be specified if op_Timestamp is specified.
             :type val_c_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupChangedCols: The operator to apply to the field ifGroupChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupChangedCols: If op_ifGroupChangedCols is specified, the field named in this input will be compared to the value in ifGroupChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupChangedCols must be specified if op_ifGroupChangedCols is specified.
             :type val_f_ifGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupChangedCols: If op_ifGroupChangedCols is specified, this value will be compared to the value in ifGroupChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupChangedCols must be specified if op_ifGroupChangedCols is specified.
             :type val_c_ifGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupEndTime: The operator to apply to the field ifGroupEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupEndTime: If op_ifGroupEndTime is specified, the field named in this input will be compared to the value in ifGroupEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupEndTime must be specified if op_ifGroupEndTime is specified.
             :type val_f_ifGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupEndTime: If op_ifGroupEndTime is specified, this value will be compared to the value in ifGroupEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupEndTime must be specified if op_ifGroupEndTime is specified.
             :type val_c_ifGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupStartTime: The operator to apply to the field ifGroupStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupStartTime: If op_ifGroupStartTime is specified, the field named in this input will be compared to the value in ifGroupStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupStartTime must be specified if op_ifGroupStartTime is specified.
             :type val_f_ifGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupStartTime: If op_ifGroupStartTime is specified, this value will be compared to the value in ifGroupStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupStartTime must be specified if op_ifGroupStartTime is specified.
             :type val_c_ifGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupTimestamp: The operator to apply to the field ifGroupTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupTimestamp: If op_ifGroupTimestamp is specified, the field named in this input will be compared to the value in ifGroupTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupTimestamp must be specified if op_ifGroupTimestamp is specified.
             :type val_f_ifGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupTimestamp: If op_ifGroupTimestamp is specified, this value will be compared to the value in ifGroupTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupTimestamp must be specified if op_ifGroupTimestamp is specified.
             :type val_c_ifGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group methods. The listed methods will be called on each if group returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` IfGroupID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupID. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount.
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

             :param select: The list of attributes to return for each IfGroup. Valid values are IfGroupID, ifGroupStartTime, ifGroupEndTime, ifGroupChangedCols, ifGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount. If empty or omitted, all attributes will be returned.
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

             :return if_groups: An array of the IfGroup objects that match the specified input criteria.
             :rtype if_groups: Array of IfGroup

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfGroupID: The internal NetMRI identifier for the interface group.
             :type IfGroupID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)
