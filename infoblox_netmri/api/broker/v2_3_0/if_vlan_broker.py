from ..broker import Broker


class IfVlanBroker(Broker):
    controller = "if_vlans"

    def show(self, **kwargs):
        """Shows the details for the specified if vlan.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if vlan methods. The listed methods will be called on each if vlan returned and included in the output. Available methods are: meta, data_source, device, interface, vlan, vlan_member, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface, vlan, vlan_member.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_vlan: The if vlan identified by the specified IfVlanID.
             :rtype if_vlan: IfVlan

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available if vlans. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device to which the interface belongs.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device to which the interface belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface participating in the VLAN.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface participating in the VLAN.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
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

             :param timestamp: The data returned will represent the if vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if vlan methods. The listed methods will be called on each if vlan returned and included in the output. Available methods are: meta, data_source, device, interface, vlan, vlan_member, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface, vlan, vlan_member.
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
            |  ``default:`` IfVlanID

             :param sort: The data field(s) to use for sorting the output. Default is IfVlanID. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge.
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

             :param select: The list of attributes to return for each IfVlan. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge. If empty or omitted, all attributes will be returned.
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

             :return if_vlans: An array of the IfVlan objects that match the specified input criteria.
             :rtype if_vlans: Array of IfVlan

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available if vlans matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier of the device to which the interface belongs.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device to which the interface belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface participating in the VLAN.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface participating in the VLAN.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpPortDesignatedBridge: The Spanning Tree Protocol designated bridge address of this interface for this VLAN.
             :type StpPortDesignatedBridge: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpPortDesignatedBridge: The Spanning Tree Protocol designated bridge address of this interface for this VLAN.
             :type StpPortDesignatedBridge: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpPortState: The Spanning Tree Protocol state of this interface for this VLAN.
             :type StpPortState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpPortState: The Spanning Tree Protocol state of this interface for this VLAN.
             :type StpPortState: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanExtensionInd: A flag indicating if this record represents an interface attached to an access port rather than on a participating bridge.
             :type VlanExtensionInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanExtensionInd: A flag indicating if this record represents an interface attached to an access port rather than on a participating bridge.
             :type VlanExtensionInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanInterfaceInd: A flag indicating if this record represents the SVI for the VLAN on this device.
             :type VlanInterfaceInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanInterfaceInd: A flag indicating if this record represents the SVI for the VLAN on this device.
             :type VlanInterfaceInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for the VlanMember record of the device to which the interface belongs, for this VLAN.
             :type VlanMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for the VlanMember record of the device to which the interface belongs, for this VLAN.
             :type VlanMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifVlanChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifVlanChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type ifVlanEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type ifVlanEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanSource: Internal tracking information for NetMRI algorithms.
             :type ifVlanSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanSource: Internal tracking information for NetMRI algorithms.
             :type ifVlanSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanStartTime: The starting effective time of this revision of the record.
             :type ifVlanStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanStartTime: The starting effective time of this revision of the record.
             :type ifVlanStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanTimestamp: The date and time this record was collected or calculated.
             :type ifVlanTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVlanTimestamp: The date and time this record was collected or calculated.
             :type ifVlanTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the if vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if vlan methods. The listed methods will be called on each if vlan returned and included in the output. Available methods are: meta, data_source, device, interface, vlan, vlan_member, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface, vlan, vlan_member.
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
            |  ``default:`` IfVlanID

             :param sort: The data field(s) to use for sorting the output. Default is IfVlanID. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge.
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

             :param select: The list of attributes to return for each IfVlan. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if vlans, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, IfVlanID, InterfaceID, StpPortDesignatedBridge, StpPortState, VlanExtensionInd, VlanID, VlanInterfaceInd, VlanMemberID, ifVlanChangedCols, ifVlanEndTime, ifVlanSource, ifVlanStartTime, ifVlanTimestamp.
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

             :return if_vlans: An array of the IfVlan objects that match the specified input criteria.
             :rtype if_vlans: Array of IfVlan

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if vlans matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, IfVlanID, InterfaceID, StpPortDesignatedBridge, StpPortState, VlanExtensionInd, VlanID, VlanInterfaceInd, VlanMemberID, ifVlanChangedCols, ifVlanEndTime, ifVlanSource, ifVlanStartTime, ifVlanTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of the device to which the interface belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfVlanID: The operator to apply to the field IfVlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfVlanID: If op_IfVlanID is specified, the field named in this input will be compared to the value in IfVlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfVlanID must be specified if op_IfVlanID is specified.
             :type val_f_IfVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfVlanID: If op_IfVlanID is specified, this value will be compared to the value in IfVlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfVlanID must be specified if op_IfVlanID is specified.
             :type val_c_IfVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of the interface participating in the VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_StpPortDesignatedBridge: The operator to apply to the field StpPortDesignatedBridge. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpPortDesignatedBridge: The Spanning Tree Protocol designated bridge address of this interface for this VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpPortDesignatedBridge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpPortDesignatedBridge: If op_StpPortDesignatedBridge is specified, the field named in this input will be compared to the value in StpPortDesignatedBridge using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpPortDesignatedBridge must be specified if op_StpPortDesignatedBridge is specified.
             :type val_f_StpPortDesignatedBridge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpPortDesignatedBridge: If op_StpPortDesignatedBridge is specified, this value will be compared to the value in StpPortDesignatedBridge using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpPortDesignatedBridge must be specified if op_StpPortDesignatedBridge is specified.
             :type val_c_StpPortDesignatedBridge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpPortState: The operator to apply to the field StpPortState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpPortState: The Spanning Tree Protocol state of this interface for this VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpPortState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpPortState: If op_StpPortState is specified, the field named in this input will be compared to the value in StpPortState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpPortState must be specified if op_StpPortState is specified.
             :type val_f_StpPortState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpPortState: If op_StpPortState is specified, this value will be compared to the value in StpPortState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpPortState must be specified if op_StpPortState is specified.
             :type val_c_StpPortState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanExtensionInd: The operator to apply to the field VlanExtensionInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanExtensionInd: A flag indicating if this record represents an interface attached to an access port rather than on a participating bridge. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanExtensionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanExtensionInd: If op_VlanExtensionInd is specified, the field named in this input will be compared to the value in VlanExtensionInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanExtensionInd must be specified if op_VlanExtensionInd is specified.
             :type val_f_VlanExtensionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanExtensionInd: If op_VlanExtensionInd is specified, this value will be compared to the value in VlanExtensionInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanExtensionInd must be specified if op_VlanExtensionInd is specified.
             :type val_c_VlanExtensionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier of the VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VlanInterfaceInd: The operator to apply to the field VlanInterfaceInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanInterfaceInd: A flag indicating if this record represents the SVI for the VLAN on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanInterfaceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanInterfaceInd: If op_VlanInterfaceInd is specified, the field named in this input will be compared to the value in VlanInterfaceInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanInterfaceInd must be specified if op_VlanInterfaceInd is specified.
             :type val_f_VlanInterfaceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanInterfaceInd: If op_VlanInterfaceInd is specified, this value will be compared to the value in VlanInterfaceInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanInterfaceInd must be specified if op_VlanInterfaceInd is specified.
             :type val_c_VlanInterfaceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberID: The operator to apply to the field VlanMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberID: The internal NetMRI identifier for the VlanMember record of the device to which the interface belongs, for this VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberID: If op_VlanMemberID is specified, the field named in this input will be compared to the value in VlanMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberID must be specified if op_VlanMemberID is specified.
             :type val_f_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberID: If op_VlanMemberID is specified, this value will be compared to the value in VlanMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberID must be specified if op_VlanMemberID is specified.
             :type val_c_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVlanChangedCols: The operator to apply to the field ifVlanChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVlanChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVlanChangedCols: If op_ifVlanChangedCols is specified, the field named in this input will be compared to the value in ifVlanChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVlanChangedCols must be specified if op_ifVlanChangedCols is specified.
             :type val_f_ifVlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVlanChangedCols: If op_ifVlanChangedCols is specified, this value will be compared to the value in ifVlanChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVlanChangedCols must be specified if op_ifVlanChangedCols is specified.
             :type val_c_ifVlanChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVlanEndTime: The operator to apply to the field ifVlanEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVlanEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVlanEndTime: If op_ifVlanEndTime is specified, the field named in this input will be compared to the value in ifVlanEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVlanEndTime must be specified if op_ifVlanEndTime is specified.
             :type val_f_ifVlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVlanEndTime: If op_ifVlanEndTime is specified, this value will be compared to the value in ifVlanEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVlanEndTime must be specified if op_ifVlanEndTime is specified.
             :type val_c_ifVlanEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVlanSource: The operator to apply to the field ifVlanSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVlanSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVlanSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVlanSource: If op_ifVlanSource is specified, the field named in this input will be compared to the value in ifVlanSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVlanSource must be specified if op_ifVlanSource is specified.
             :type val_f_ifVlanSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVlanSource: If op_ifVlanSource is specified, this value will be compared to the value in ifVlanSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVlanSource must be specified if op_ifVlanSource is specified.
             :type val_c_ifVlanSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVlanStartTime: The operator to apply to the field ifVlanStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVlanStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVlanStartTime: If op_ifVlanStartTime is specified, the field named in this input will be compared to the value in ifVlanStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVlanStartTime must be specified if op_ifVlanStartTime is specified.
             :type val_f_ifVlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVlanStartTime: If op_ifVlanStartTime is specified, this value will be compared to the value in ifVlanStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVlanStartTime must be specified if op_ifVlanStartTime is specified.
             :type val_c_ifVlanStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVlanTimestamp: The operator to apply to the field ifVlanTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVlanTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVlanTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVlanTimestamp: If op_ifVlanTimestamp is specified, the field named in this input will be compared to the value in ifVlanTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVlanTimestamp must be specified if op_ifVlanTimestamp is specified.
             :type val_f_ifVlanTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVlanTimestamp: If op_ifVlanTimestamp is specified, this value will be compared to the value in ifVlanTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVlanTimestamp must be specified if op_ifVlanTimestamp is specified.
             :type val_c_ifVlanTimestamp: String

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

             :param timestamp: The data returned will represent the if vlans as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if vlan methods. The listed methods will be called on each if vlan returned and included in the output. Available methods are: meta, data_source, device, interface, vlan, vlan_member, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface, vlan, vlan_member.
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
            |  ``default:`` IfVlanID

             :param sort: The data field(s) to use for sorting the output. Default is IfVlanID. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge.
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

             :param select: The list of attributes to return for each IfVlan. Valid values are IfVlanID, DataSourceID, DeviceID, InterfaceID, VlanID, ifVlanStartTime, ifVlanEndTime, ifVlanChangedCols, ifVlanTimestamp, ifVlanSource, VlanMemberID, VlanInterfaceInd, VlanExtensionInd, StpPortState, StpPortDesignatedBridge. If empty or omitted, all attributes will be returned.
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

             :return if_vlans: An array of the IfVlan objects that match the specified input criteria.
             :rtype if_vlans: Array of IfVlan

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def interface(self, **kwargs):
        """The interface participating in the VLAN.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface participating in the VLAN.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def vlan(self, **kwargs):
        """The VLAN to which this interface VLAN membership belongs.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VLAN to which this interface VLAN membership belongs.
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def vlan_member(self, **kwargs):
        """The VLAN membership record of the device to which the interface belongs, for this VLAN.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VLAN membership record of the device to which the interface belongs, for this VLAN.
             :rtype : VlanMember

            """

        return self.api_request(self._get_method_fullname("vlan_member"), kwargs)

    def infradevice(self, **kwargs):
        """The device to which the interface belongs.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device to which the interface belongs.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device to which the interface belongs.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfVlanID: The internal NetMRI identifier for the interface-in-VLAN record.
             :type IfVlanID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device to which the interface belongs.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
