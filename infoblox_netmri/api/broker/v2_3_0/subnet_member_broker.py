from ..broker import Broker


class SubnetMemberBroker(Broker):
    controller = "subnet_members"

    def show(self, **kwargs):
        """Shows the details for the specified subnet member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet member methods. The listed methods will be called on each subnet member returned and included in the output. Available methods are: data_source, device, subnet, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, subnet.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return subnet_member: The subnet member identified by the specified SubnetMemberID.
             :rtype subnet_member: SubnetMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available subnet members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this subnet membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this subnet membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for the subnet associated with this subnet membership.
             :type SubnetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for the subnet associated with this subnet membership.
             :type SubnetID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the subnet members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet member methods. The listed methods will be called on each subnet member returned and included in the output. Available methods are: data_source, device, subnet, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, subnet.
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
            |  ``default:`` SubnetMemberID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetMemberID. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp.
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

             :param select: The list of attributes to return for each SubnetMember. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp. If empty or omitted, all attributes will be returned.
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

             :return subnet_members: An array of the SubnetMember objects that match the specified input criteria.
             :rtype subnet_members: Array of SubnetMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available subnet members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AciBdID: ID of ACI bridge domain subnet member is assigned to
             :type AciBdID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AciBdID: ID of ACI bridge domain subnet member is assigned to
             :type AciBdID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AciEpgID: ID of ACI EPG subnet member is assigned to
             :type AciEpgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AciEpgID: ID of ACI EPG subnet member is assigned to
             :type AciEpgID: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device associated with this subnet membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this subnet membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for the interface address associated with this subnet membership, if available.
             :type IfAddrID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for the interface address associated with this subnet membership, if available.
             :type IfAddrID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for the subnet associated with this subnet membership.
             :type SubnetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for the subnet associated with this subnet membership.
             :type SubnetID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubnetMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubnetMemberChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SubnetMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SubnetMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberSource: Internal tracking information for NetMRI algorithms.
             :type SubnetMemberSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberSource: Internal tracking information for NetMRI algorithms.
             :type SubnetMemberSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberStartTime: The starting effective time of this revision of the record.
             :type SubnetMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberStartTime: The starting effective time of this revision of the record.
             :type SubnetMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberTimestamp: The date and time this record was collected or calculated.
             :type SubnetMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetMemberTimestamp: The date and time this record was collected or calculated.
             :type SubnetMemberTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the subnet members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet member methods. The listed methods will be called on each subnet member returned and included in the output. Available methods are: data_source, device, subnet, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, subnet.
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
            |  ``default:`` SubnetMemberID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetMemberID. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp.
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

             :param select: The list of attributes to return for each SubnetMember. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against subnet members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: AciBdID, AciEpgID, DataSourceID, DeviceID, IfAddrID, SubnetID, SubnetMemberChangedCols, SubnetMemberEndTime, SubnetMemberID, SubnetMemberSource, SubnetMemberStartTime, SubnetMemberTimestamp.
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

             :return subnet_members: An array of the SubnetMember objects that match the specified input criteria.
             :rtype subnet_members: Array of SubnetMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available subnet members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: AciBdID, AciEpgID, DataSourceID, DeviceID, IfAddrID, SubnetID, SubnetMemberChangedCols, SubnetMemberEndTime, SubnetMemberID, SubnetMemberSource, SubnetMemberStartTime, SubnetMemberTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AciBdID: The operator to apply to the field AciBdID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AciBdID: ID of ACI bridge domain subnet member is assigned to For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AciBdID: If op_AciBdID is specified, the field named in this input will be compared to the value in AciBdID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AciBdID must be specified if op_AciBdID is specified.
             :type val_f_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AciBdID: If op_AciBdID is specified, this value will be compared to the value in AciBdID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AciBdID must be specified if op_AciBdID is specified.
             :type val_c_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AciEpgID: The operator to apply to the field AciEpgID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AciEpgID: ID of ACI EPG subnet member is assigned to For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AciEpgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AciEpgID: If op_AciEpgID is specified, the field named in this input will be compared to the value in AciEpgID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AciEpgID must be specified if op_AciEpgID is specified.
             :type val_f_AciEpgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AciEpgID: If op_AciEpgID is specified, this value will be compared to the value in AciEpgID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AciEpgID must be specified if op_AciEpgID is specified.
             :type val_c_AciEpgID: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device associated with this subnet membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfAddrID: The operator to apply to the field IfAddrID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfAddrID: The internal NetMRI identifier for the interface address associated with this subnet membership, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfAddrID: If op_IfAddrID is specified, the field named in this input will be compared to the value in IfAddrID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_f_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfAddrID: If op_IfAddrID is specified, this value will be compared to the value in IfAddrID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_c_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetID: The operator to apply to the field SubnetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetID: The internal NetMRI identifier for the subnet associated with this subnet membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetID: If op_SubnetID is specified, the field named in this input will be compared to the value in SubnetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetID must be specified if op_SubnetID is specified.
             :type val_f_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetID: If op_SubnetID is specified, this value will be compared to the value in SubnetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetID must be specified if op_SubnetID is specified.
             :type val_c_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberChangedCols: The operator to apply to the field SubnetMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberChangedCols: If op_SubnetMemberChangedCols is specified, the field named in this input will be compared to the value in SubnetMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberChangedCols must be specified if op_SubnetMemberChangedCols is specified.
             :type val_f_SubnetMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberChangedCols: If op_SubnetMemberChangedCols is specified, this value will be compared to the value in SubnetMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberChangedCols must be specified if op_SubnetMemberChangedCols is specified.
             :type val_c_SubnetMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberEndTime: The operator to apply to the field SubnetMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberEndTime: If op_SubnetMemberEndTime is specified, the field named in this input will be compared to the value in SubnetMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberEndTime must be specified if op_SubnetMemberEndTime is specified.
             :type val_f_SubnetMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberEndTime: If op_SubnetMemberEndTime is specified, this value will be compared to the value in SubnetMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberEndTime must be specified if op_SubnetMemberEndTime is specified.
             :type val_c_SubnetMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberID: The operator to apply to the field SubnetMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberID: The internal NetMRI identifier for this subnet membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberID: If op_SubnetMemberID is specified, the field named in this input will be compared to the value in SubnetMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberID must be specified if op_SubnetMemberID is specified.
             :type val_f_SubnetMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberID: If op_SubnetMemberID is specified, this value will be compared to the value in SubnetMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberID must be specified if op_SubnetMemberID is specified.
             :type val_c_SubnetMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberSource: The operator to apply to the field SubnetMemberSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberSource: If op_SubnetMemberSource is specified, the field named in this input will be compared to the value in SubnetMemberSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberSource must be specified if op_SubnetMemberSource is specified.
             :type val_f_SubnetMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberSource: If op_SubnetMemberSource is specified, this value will be compared to the value in SubnetMemberSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberSource must be specified if op_SubnetMemberSource is specified.
             :type val_c_SubnetMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberStartTime: The operator to apply to the field SubnetMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberStartTime: If op_SubnetMemberStartTime is specified, the field named in this input will be compared to the value in SubnetMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberStartTime must be specified if op_SubnetMemberStartTime is specified.
             :type val_f_SubnetMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberStartTime: If op_SubnetMemberStartTime is specified, this value will be compared to the value in SubnetMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberStartTime must be specified if op_SubnetMemberStartTime is specified.
             :type val_c_SubnetMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetMemberTimestamp: The operator to apply to the field SubnetMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetMemberTimestamp: If op_SubnetMemberTimestamp is specified, the field named in this input will be compared to the value in SubnetMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetMemberTimestamp must be specified if op_SubnetMemberTimestamp is specified.
             :type val_f_SubnetMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetMemberTimestamp: If op_SubnetMemberTimestamp is specified, this value will be compared to the value in SubnetMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetMemberTimestamp must be specified if op_SubnetMemberTimestamp is specified.
             :type val_c_SubnetMemberTimestamp: String

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

             :param timestamp: The data returned will represent the subnet members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet member methods. The listed methods will be called on each subnet member returned and included in the output. Available methods are: data_source, device, subnet, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, subnet.
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
            |  ``default:`` SubnetMemberID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetMemberID. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp.
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

             :param select: The list of attributes to return for each SubnetMember. Valid values are SubnetMemberID, SubnetID, DeviceID, IfAddrID, DataSourceID, SubnetMemberSource, AciBdID, AciEpgID, SubnetMemberStartTime, SubnetMemberEndTime, SubnetMemberChangedCols, SubnetMemberTimestamp. If empty or omitted, all attributes will be returned.
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

             :return subnet_members: An array of the SubnetMember objects that match the specified input criteria.
             :rtype subnet_members: Array of SubnetMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def subnet(self, **kwargs):
        """Returns the associated Subnet object for this subnet member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Returns the associated Subnet object for this subnet member.
             :rtype : Subnet

            """

        return self.api_request(self._get_method_fullname("subnet"), kwargs)

    def infradevice(self, **kwargs):
        """The device associated with this subnet membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device associated with this subnet membership.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device associated with this subnet membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetMemberID: The internal NetMRI identifier for this subnet membership.
             :type SubnetMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device associated with this subnet membership.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
