from ..broker import Broker


class VlanBroker(Broker):
    controller = "vlans"

    def show(self, **kwargs):
        """Shows the details for the specified vlan.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan methods. The listed methods will be called on each vlan returned and included in the output. Available methods are: data_source, root_member, root_device, root_bridge.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, root_member.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return vlan: The vlan identified by the specified VlanID.
             :rtype vlan: Vlan

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available vlans. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The bridge address of the root bridge.
             :type RootBridgeAddress: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The bridge address of the root bridge.
             :type RootBridgeAddress: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RootVlanMemberID: The internal NetMRI identifier for the VlanMember record of the VLAN root bridge.
             :type RootVlanMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RootVlanMemberID: The internal NetMRI identifier for the VlanMember record of the VLAN root bridge.
             :type RootVlanMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Array of Integer

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

             :param timestamp: The data returned will represent the vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan methods. The listed methods will be called on each vlan returned and included in the output. Available methods are: data_source, root_member, root_device, root_bridge.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, root_member.
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
            |  ``default:`` VlanID

             :param sort: The data field(s) to use for sorting the output. Default is VlanID. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain.
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

             :param select: The list of attributes to return for each Vlan. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain. If empty or omitted, all attributes will be returned.
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

             :return vlans: An array of the Vlan objects that match the specified input criteria.
             :rtype vlans: Array of Vlan

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available vlans matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector assigned to this VLAN (members may come from more than one collector).
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector assigned to this VLAN (members may come from more than one collector).
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The bridge address of the root bridge.
             :type RootBridgeAddress: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The bridge address of the root bridge.
             :type RootBridgeAddress: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RootVlanMemberID: The internal NetMRI identifier for the VlanMember record of the VLAN root bridge.
             :type RootVlanMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RootVlanMemberID: The internal NetMRI identifier for the VlanMember record of the VLAN root bridge.
             :type RootVlanMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpEnabledInd: A flag indicating whether this VLAN is participating in Spanning Tree.
             :type StpEnabledInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpEnabledInd: A flag indicating whether this VLAN is participating in Spanning Tree.
             :type StpEnabledInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VTPDomain: Management domain name if VLAN is VTP managed.
             :type VTPDomain: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VTPDomain: Management domain name if VLAN is VTP managed.
             :type VTPDomain: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type VlanChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type VlanChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type VlanEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type VlanEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanIndex: The numerical VLAN number (VLAN ID).
             :type VlanIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanIndex: The numerical VLAN number (VLAN ID).
             :type VlanIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanName: The name of the VLAN on the root bridge.
             :type VlanName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanName: The name of the VLAN on the root bridge.
             :type VlanName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanStartTime: The starting effective time of this revision of the record.
             :type VlanStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanStartTime: The starting effective time of this revision of the record.
             :type VlanStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanTimestamp: The date and time this record was collected or calculated.
             :type VlanTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanTimestamp: The date and time this record was collected or calculated.
             :type VlanTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan methods. The listed methods will be called on each vlan returned and included in the output. Available methods are: data_source, root_member, root_device, root_bridge.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, root_member.
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
            |  ``default:`` VlanID

             :param sort: The data field(s) to use for sorting the output. Default is VlanID. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain.
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

             :param select: The list of attributes to return for each Vlan. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against vlans, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, RootBridgeAddress, RootVlanMemberID, StpEnabledInd, VTPDomain, VlanChangedCols, VlanEndTime, VlanID, VlanIndex, VlanName, VlanStartTime, VlanTimestamp.
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

             :return vlans: An array of the Vlan objects that match the specified input criteria.
             :rtype vlans: Array of Vlan

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available vlans matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, RootBridgeAddress, RootVlanMemberID, StpEnabledInd, VTPDomain, VlanChangedCols, VlanEndTime, VlanID, VlanIndex, VlanName, VlanStartTime, VlanTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector assigned to this VLAN (members may come from more than one collector). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RootBridgeAddress: The operator to apply to the field RootBridgeAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RootBridgeAddress: The bridge address of the root bridge. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RootBridgeAddress: If op_RootBridgeAddress is specified, the field named in this input will be compared to the value in RootBridgeAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RootBridgeAddress must be specified if op_RootBridgeAddress is specified.
             :type val_f_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RootBridgeAddress: If op_RootBridgeAddress is specified, this value will be compared to the value in RootBridgeAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RootBridgeAddress must be specified if op_RootBridgeAddress is specified.
             :type val_c_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RootVlanMemberID: The operator to apply to the field RootVlanMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RootVlanMemberID: The internal NetMRI identifier for the VlanMember record of the VLAN root bridge. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RootVlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RootVlanMemberID: If op_RootVlanMemberID is specified, the field named in this input will be compared to the value in RootVlanMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RootVlanMemberID must be specified if op_RootVlanMemberID is specified.
             :type val_f_RootVlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RootVlanMemberID: If op_RootVlanMemberID is specified, this value will be compared to the value in RootVlanMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RootVlanMemberID must be specified if op_RootVlanMemberID is specified.
             :type val_c_RootVlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpEnabledInd: The operator to apply to the field StpEnabledInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpEnabledInd: A flag indicating whether this VLAN is participating in Spanning Tree. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpEnabledInd: If op_StpEnabledInd is specified, the field named in this input will be compared to the value in StpEnabledInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpEnabledInd must be specified if op_StpEnabledInd is specified.
             :type val_f_StpEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpEnabledInd: If op_StpEnabledInd is specified, this value will be compared to the value in StpEnabledInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpEnabledInd must be specified if op_StpEnabledInd is specified.
             :type val_c_StpEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VTPDomain: The operator to apply to the field VTPDomain. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VTPDomain: Management domain name if VLAN is VTP managed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VTPDomain: If op_VTPDomain is specified, the field named in this input will be compared to the value in VTPDomain using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VTPDomain must be specified if op_VTPDomain is specified.
             :type val_f_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VTPDomain: If op_VTPDomain is specified, this value will be compared to the value in VTPDomain using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VTPDomain must be specified if op_VTPDomain is specified.
             :type val_c_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanChangedCols: The operator to apply to the field VlanChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanChangedCols: If op_VlanChangedCols is specified, the field named in this input will be compared to the value in VlanChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanChangedCols must be specified if op_VlanChangedCols is specified.
             :type val_f_VlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanChangedCols: If op_VlanChangedCols is specified, this value will be compared to the value in VlanChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanChangedCols must be specified if op_VlanChangedCols is specified.
             :type val_c_VlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanEndTime: The operator to apply to the field VlanEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanEndTime: If op_VlanEndTime is specified, the field named in this input will be compared to the value in VlanEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanEndTime must be specified if op_VlanEndTime is specified.
             :type val_f_VlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanEndTime: If op_VlanEndTime is specified, this value will be compared to the value in VlanEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanEndTime must be specified if op_VlanEndTime is specified.
             :type val_c_VlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanID: If op_VlanID is specified, the field named in this input will be compared to the value in VlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanID must be specified if op_VlanID is specified.
             :type val_f_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanID: If op_VlanID is specified, this value will be compared to the value in VlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanID must be specified if op_VlanID is specified.
             :type val_c_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanIndex: The operator to apply to the field VlanIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanIndex: The numerical VLAN number (VLAN ID). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanIndex: If op_VlanIndex is specified, the field named in this input will be compared to the value in VlanIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanIndex must be specified if op_VlanIndex is specified.
             :type val_f_VlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanIndex: If op_VlanIndex is specified, this value will be compared to the value in VlanIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanIndex must be specified if op_VlanIndex is specified.
             :type val_c_VlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanName: The operator to apply to the field VlanName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanName: The name of the VLAN on the root bridge. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanName: If op_VlanName is specified, the field named in this input will be compared to the value in VlanName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanName must be specified if op_VlanName is specified.
             :type val_f_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanName: If op_VlanName is specified, this value will be compared to the value in VlanName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanName must be specified if op_VlanName is specified.
             :type val_c_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanStartTime: The operator to apply to the field VlanStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanStartTime: If op_VlanStartTime is specified, the field named in this input will be compared to the value in VlanStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanStartTime must be specified if op_VlanStartTime is specified.
             :type val_f_VlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanStartTime: If op_VlanStartTime is specified, this value will be compared to the value in VlanStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanStartTime must be specified if op_VlanStartTime is specified.
             :type val_c_VlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanTimestamp: The operator to apply to the field VlanTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanTimestamp: If op_VlanTimestamp is specified, the field named in this input will be compared to the value in VlanTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanTimestamp must be specified if op_VlanTimestamp is specified.
             :type val_f_VlanTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanTimestamp: If op_VlanTimestamp is specified, this value will be compared to the value in VlanTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanTimestamp must be specified if op_VlanTimestamp is specified.
             :type val_c_VlanTimestamp: String

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

             :param timestamp: The data returned will represent the vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan methods. The listed methods will be called on each vlan returned and included in the output. Available methods are: data_source, root_member, root_device, root_bridge.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, root_member.
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
            |  ``default:`` VlanID

             :param sort: The data field(s) to use for sorting the output. Default is VlanID. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain.
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

             :param select: The list of attributes to return for each Vlan. Valid values are VlanID, VlanStartTime, VlanEndTime, VlanChangedCols, VlanTimestamp, DataSourceID, RootVlanMemberID, VlanIndex, VlanName, RootBridgeAddress, StpEnabledInd, VTPDomain. If empty or omitted, all attributes will be returned.
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

             :return vlans: An array of the Vlan objects that match the specified input criteria.
             :rtype vlans: Array of Vlan

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def root_member(self, **kwargs):
        """The VLAN membership record of the VLAN root bridge.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VLAN membership record of the VLAN root bridge.
             :rtype : VlanMember

            """

        return self.api_request(self._get_method_fullname("root_member"), kwargs)

    def root_device(self, **kwargs):
        """The Device object for the root bridge, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Device object for the root bridge, if available.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("root_device"), kwargs)

    def root_bridge(self, **kwargs):
        """The name of the root bridge, if available; otherwise, the root bridge address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
             :type VlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The name of the root bridge, if available; otherwise, the root bridge address.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("root_bridge"), kwargs)
