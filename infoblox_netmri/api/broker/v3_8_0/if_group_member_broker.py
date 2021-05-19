from ..broker import Broker


class IfGroupMemberBroker(Broker):
    controller = "if_group_members"

    def index(self, **kwargs):
        """Lists the available if group members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Array of Integer

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

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The Interface ID.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The Interface ID.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if group members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group member methods. The listed methods will be called on each if group member returned and included in the output. Available methods are: interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: interface.
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
            |  ``default:`` IfGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupMemberID. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID.
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

             :param select: The list of attributes to return for each IfGroupMember. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return if_group_members: An array of the IfGroupMember objects that match the specified input criteria.
             :rtype if_group_members: Array of IfGroupMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified if group member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group member methods. The listed methods will be called on each if group member returned and included in the output. Available methods are: interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_group_member: The if group member identified by the specified IfGroupMemberID.
             :rtype if_group_member: IfGroupMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available if group members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

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

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Array of Integer

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

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The Interface ID.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The Interface ID.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifGroupMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifGroupMemberChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifGroupMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifGroupMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberStartTime: The starting effective time of this record.
             :type ifGroupMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberStartTime: The starting effective time of this record.
             :type ifGroupMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberTimestamp: The date and time this record was collected or calculated.
             :type ifGroupMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifGroupMemberTimestamp: The date and time this record was collected or calculated.
             :type ifGroupMemberTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The internal NetMRI identifier for the device from which this data was collected.
             :type ifIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The internal NetMRI identifier for the device from which this data was collected.
             :type ifIndex: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if group members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group member methods. The listed methods will be called on each if group member returned and included in the output. Available methods are: interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: interface.
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
            |  ``default:`` IfGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupMemberID. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID.
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

             :param select: The list of attributes to return for each IfGroupMember. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if group members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, GroupID, IfGroupMemberID, InterfaceID, ifGroupMemberChangedCols, ifGroupMemberEndTime, ifGroupMemberStartTime, ifGroupMemberTimestamp, ifIndex.
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

             :return if_group_members: An array of the IfGroupMember objects that match the specified input criteria.
             :rtype if_group_members: Array of IfGroupMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if group members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, GroupID, IfGroupMemberID, InterfaceID, ifGroupMemberChangedCols, ifGroupMemberEndTime, ifGroupMemberStartTime, ifGroupMemberTimestamp, ifIndex.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfGroupMemberID: The operator to apply to the field IfGroupMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfGroupMemberID: The internal NetMRI identifier for this interface group membership record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfGroupMemberID: If op_IfGroupMemberID is specified, the field named in this input will be compared to the value in IfGroupMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfGroupMemberID must be specified if op_IfGroupMemberID is specified.
             :type val_f_IfGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfGroupMemberID: If op_IfGroupMemberID is specified, this value will be compared to the value in IfGroupMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfGroupMemberID must be specified if op_IfGroupMemberID is specified.
             :type val_c_IfGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The Interface ID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupMemberChangedCols: The operator to apply to the field ifGroupMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupMemberChangedCols: If op_ifGroupMemberChangedCols is specified, the field named in this input will be compared to the value in ifGroupMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupMemberChangedCols must be specified if op_ifGroupMemberChangedCols is specified.
             :type val_f_ifGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupMemberChangedCols: If op_ifGroupMemberChangedCols is specified, this value will be compared to the value in ifGroupMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupMemberChangedCols must be specified if op_ifGroupMemberChangedCols is specified.
             :type val_c_ifGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupMemberEndTime: The operator to apply to the field ifGroupMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupMemberEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupMemberEndTime: If op_ifGroupMemberEndTime is specified, the field named in this input will be compared to the value in ifGroupMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupMemberEndTime must be specified if op_ifGroupMemberEndTime is specified.
             :type val_f_ifGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupMemberEndTime: If op_ifGroupMemberEndTime is specified, this value will be compared to the value in ifGroupMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupMemberEndTime must be specified if op_ifGroupMemberEndTime is specified.
             :type val_c_ifGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupMemberStartTime: The operator to apply to the field ifGroupMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupMemberStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupMemberStartTime: If op_ifGroupMemberStartTime is specified, the field named in this input will be compared to the value in ifGroupMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupMemberStartTime must be specified if op_ifGroupMemberStartTime is specified.
             :type val_f_ifGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupMemberStartTime: If op_ifGroupMemberStartTime is specified, this value will be compared to the value in ifGroupMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupMemberStartTime must be specified if op_ifGroupMemberStartTime is specified.
             :type val_c_ifGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifGroupMemberTimestamp: The operator to apply to the field ifGroupMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifGroupMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifGroupMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifGroupMemberTimestamp: If op_ifGroupMemberTimestamp is specified, the field named in this input will be compared to the value in ifGroupMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifGroupMemberTimestamp must be specified if op_ifGroupMemberTimestamp is specified.
             :type val_f_ifGroupMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifGroupMemberTimestamp: If op_ifGroupMemberTimestamp is specified, this value will be compared to the value in ifGroupMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifGroupMemberTimestamp must be specified if op_ifGroupMemberTimestamp is specified.
             :type val_c_ifGroupMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The internal NetMRI identifier for the device from which this data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the if group members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if group member methods. The listed methods will be called on each if group member returned and included in the output. Available methods are: interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: interface.
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
            |  ``default:`` IfGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IfGroupMemberID. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID.
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

             :param select: The list of attributes to return for each IfGroupMember. Valid values are IfGroupMemberID, GroupID, DeviceID, ifIndex, InterfaceID, ifGroupMemberStartTime, ifGroupMemberEndTime, ifGroupMemberChangedCols, ifGroupMemberTimestamp, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return if_group_members: An array of the IfGroupMember objects that match the specified input criteria.
             :rtype if_group_members: Array of IfGroupMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def interface(self, **kwargs):
        """IfGroup model access the interface method from API accessible.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfGroupMemberID: The internal NetMRI identifier for this interface group membership record.
             :type IfGroupMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : IfGroup model access the interface method from API accessible.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)
