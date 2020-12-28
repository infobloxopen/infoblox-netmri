from ..broker import Broker


class IfGroupDefnBroker(Broker):
    controller = "if_group_defns"

    def show(self, **kwargs):
        """Shows the details for the specified if group defn.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_group_defn: The if group defn identified by the specified GroupID.
             :rtype if_group_defn: IfGroupDefn

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available if group defns. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface.
             :type GroupName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface.
             :type GroupName: Array of String

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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt.
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

             :param select: The list of attributes to return for each IfGroupDefn. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt. If empty or omitted, all attributes will be returned.
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

             :return if_group_defns: An array of the IfGroupDefn objects that match the specified input criteria.
             :rtype if_group_defns: Array of IfGroupDefn

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available if group defns matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The group belongs to defined criteria in an interface group.
             :type Criteria: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The group belongs to defined criteria in an interface group.
             :type Criteria: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The level of flow collection in an interface group.
             :type FlowCollection: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The level of flow collection in an interface group.
             :type FlowCollection: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface.
             :type GroupName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface.
             :type GroupName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The total number of member in an interface group.
             :type MemberCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The total number of member in an interface group.
             :type MemberCount: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The performance frequency level in an interface group.
             :type PerfFrequency: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The performance frequency level in an interface group.
             :type PerfFrequency: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The rank specified for the group in an interface.
             :type Rank: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The rank specified for the group in an interface.
             :type Rank: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP polling state in an interface group definition.
             :type SNMPPolling: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP polling state in an interface group definition.
             :type SNMPPolling: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected.
             :type Timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected.
             :type Timestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UpdatedAt: The date and time this record was last modified.
             :type UpdatedAt: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UpdatedAt: The date and time this record was last modified.
             :type UpdatedAt: Array of DateTime

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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt.
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

             :param select: The list of attributes to return for each IfGroupDefn. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if group defns, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: Criteria, FlowCollection, GroupID, GroupName, MemberCount, PerfFrequency, Rank, SNMPPolling, Timestamp, UpdatedAt.
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

             :return if_group_defns: An array of the IfGroupDefn objects that match the specified input criteria.
             :rtype if_group_defns: Array of IfGroupDefn

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if group defns matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: Criteria, FlowCollection, GroupID, GroupName, MemberCount, PerfFrequency, Rank, SNMPPolling, Timestamp, UpdatedAt.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Criteria: The operator to apply to the field Criteria. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Criteria: The group belongs to defined criteria in an interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_FlowCollection: The operator to apply to the field FlowCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FlowCollection: The level of flow collection in an interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_GroupID: The operator to apply to the field GroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupID: The internal NetMRI identifier of an interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_GroupName: The operator to apply to the field GroupName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupName: The name of the group in the Interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_MemberCount: The operator to apply to the field MemberCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemberCount: The total number of member in an interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PerfFrequency: The operator to apply to the field PerfFrequency. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PerfFrequency: The performance frequency level in an interface group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Rank: The operator to apply to the field Rank. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Rank: The rank specified for the group in an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SNMPPolling: The operator to apply to the field SNMPPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPolling: The SNMP polling state in an interface group definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Timestamp: The operator to apply to the field Timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Timestamp: The date and time this record was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_UpdatedAt: The operator to apply to the field UpdatedAt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UpdatedAt: The date and time this record was last modified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UpdatedAt: If op_UpdatedAt is specified, the field named in this input will be compared to the value in UpdatedAt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UpdatedAt must be specified if op_UpdatedAt is specified.
             :type val_f_UpdatedAt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UpdatedAt: If op_UpdatedAt is specified, this value will be compared to the value in UpdatedAt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UpdatedAt must be specified if op_UpdatedAt is specified.
             :type val_c_UpdatedAt: String

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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt.
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

             :param select: The list of attributes to return for each IfGroupDefn. Valid values are GroupID, GroupName, Criteria, Rank, SNMPPolling, FlowCollection, PerfFrequency, Timestamp, MemberCount, UpdatedAt. If empty or omitted, all attributes will be returned.
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

             :return if_group_defns: An array of the IfGroupDefn objects that match the specified input criteria.
             :rtype if_group_defns: Array of IfGroupDefn

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a new if group defn.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Criteria: The group belongs to defined criteria in an interface group.
             :type Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The level of flow collection in an interface group.
             :type FlowCollection: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface.
             :type GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The total number of member in an interface group.
             :type MemberCount: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The performance frequency level in an interface group.
             :type PerfFrequency: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Rank: The rank specified for the group in an interface.
             :type Rank: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP polling state in an interface group definition.
             :type SNMPPolling: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected.
             :type Timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UpdatedAt: The date and time this record was last modified.
             :type UpdatedAt: DateTime

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created if group defn.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created if group defn.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created if group defn.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_group_defn: The newly created if group defn.
             :rtype if_group_defn: IfGroupDefn

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified if group defn from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Interface group identity which identifies each definition.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def update(self, **kwargs):
        """Updates an existing if group defn.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier of an interface group.
             :type GroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The group belongs to defined criteria in an interface group. If omitted, this field will not be updated.
             :type Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FlowCollection: The level of flow collection in an interface group. If omitted, this field will not be updated.
             :type FlowCollection: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of the group in the Interface. If omitted, this field will not be updated.
             :type GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The total number of member in an interface group. If omitted, this field will not be updated.
             :type MemberCount: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PerfFrequency: The performance frequency level in an interface group. If omitted, this field will not be updated.
             :type PerfFrequency: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The rank specified for the group in an interface. If omitted, this field will not be updated.
             :type Rank: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: The SNMP polling state in an interface group definition. If omitted, this field will not be updated.
             :type SNMPPolling: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected. If omitted, this field will not be updated.
             :type Timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UpdatedAt: The date and time this record was last modified. If omitted, this field will not be updated.
             :type UpdatedAt: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Interface group identity which identifies each definition.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated if group defn.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated if group defn.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated if group defn.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_group_defn: The updated if group defn.
             :rtype if_group_defn: IfGroupDefn

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)
