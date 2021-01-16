from ..broker import Broker


class IfWirelessSSIDBroker(Broker):
    controller = "if_wireless_ssids"

    def index(self, **kwargs):
        """Lists the available if wireless ssids. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Wireless SSID table entry was found.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Wireless SSID table entry was found.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of local interface for this wireless SSID table.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of local interface for this wireless SSID table.
             :type InterfaceID: Array of Integer

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

             :param timestamp: The data returned will represent the if wireless ssids as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid methods. The listed methods will be called on each if wireless ssid returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd.
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

             :param select: The list of attributes to return for each IfWirelessSSID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd. If empty or omitted, all attributes will be returned.
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

             :return if_wireless_ssi_ds: An array of the IfWirelessSSID objects that match the specified input criteria.
             :rtype if_wireless_ssi_ds: Array of IfWirelessSSID

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified if wireless ssid.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid methods. The listed methods will be called on each if wireless ssid returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_wireless_ssid: The if wireless ssid identified by the specified IfWirelessSSIDID.
             :rtype if_wireless_ssid: IfWirelessSSID

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available if wireless ssids matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier of each device from which Wireless SSID table entry was found.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Wireless SSID table entry was found.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of local interface for this wireless SSID table.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of local interface for this wireless SSID table.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSID: The unique number of service set identifier(SSID) in the wirelessSSID.
             :type SSID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSID: The unique number of service set identifier(SSID) in the wirelessSSID.
             :type SSID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDBroadcastInd: A flag indicates whether the broadcast index of the wireless SSID is enabled or not.
             :type SSIDBroadcastInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDBroadcastInd: A flag indicates whether the broadcast index of the wireless SSID is enabled or not.
             :type SSIDBroadcastInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDDefaultVlanIndex: The default VLAN Index of the wireless SSID.
             :type SSIDDefaultVlanIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDDefaultVlanIndex: The default VLAN Index of the wireless SSID.
             :type SSIDDefaultVlanIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDIndex: The service set identifier(SSID) index of the interface wirelessSSID.
             :type SSIDIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDIndex: The service set identifier(SSID) index of the interface wirelessSSID.
             :type SSIDIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMaxAssociations: The maximum associations formed by the wirelessSSID.
             :type SSIDMaxAssociations: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMaxAssociations: The maximum associations formed by the wirelessSSID.
             :type SSIDMaxAssociations: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPMICAlgorithm: The algorithm process of web equivalent privacy in the wirelessSSID.
             :type WEPMICAlgorithm: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPMICAlgorithm: The algorithm process of web equivalent privacy in the wirelessSSID.
             :type WEPMICAlgorithm: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPPermuteAlgorithm: The permutation algorithm of web equivalent privacy in the wirelessSSID.
             :type WEPPermuteAlgorithm: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPPermuteAlgorithm: The permutation algorithm of web equivalent privacy in the wirelessSSID.
             :type WEPPermuteAlgorithm: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index of the local interface for the wireless SSID.
             :type ifIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index of the local interface for the wireless SSID.
             :type ifIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifWirelessSSIDChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifWirelessSSIDChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifWirelessSSIDEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifWirelessSSIDEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDStartTime: The starting effective time of this record.
             :type ifWirelessSSIDStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDStartTime: The starting effective time of this record.
             :type ifWirelessSSIDStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDTimestamp: The date and time this record was collected or calculated.
             :type ifWirelessSSIDTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDTimestamp: The date and time this record was collected or calculated.
             :type ifWirelessSSIDTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the if wireless ssids as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid methods. The listed methods will be called on each if wireless ssid returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd.
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

             :param select: The list of attributes to return for each IfWirelessSSID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if wireless ssids, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, IfWirelessSSIDID, InterfaceID, SSID, SSIDBroadcastInd, SSIDDefaultVlanIndex, SSIDIndex, SSIDMaxAssociations, VlanID, WEPMICAlgorithm, WEPPermuteAlgorithm, ifIndex, ifWirelessSSIDChangedCols, ifWirelessSSIDEndTime, ifWirelessSSIDStartTime, ifWirelessSSIDTimestamp.
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

             :return if_wireless_ssi_ds: An array of the IfWirelessSSID objects that match the specified input criteria.
             :rtype if_wireless_ssi_ds: Array of IfWirelessSSID

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if wireless ssids matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, IfWirelessSSIDID, InterfaceID, SSID, SSIDBroadcastInd, SSIDDefaultVlanIndex, SSIDIndex, SSIDMaxAssociations, VlanID, WEPMICAlgorithm, WEPPermuteAlgorithm, ifIndex, ifWirelessSSIDChangedCols, ifWirelessSSIDEndTime, ifWirelessSSIDStartTime, ifWirelessSSIDTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which Wireless SSID table entry was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfWirelessSSIDID: The operator to apply to the field IfWirelessSSIDID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfWirelessSSIDID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfWirelessSSIDID: If op_IfWirelessSSIDID is specified, the field named in this input will be compared to the value in IfWirelessSSIDID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfWirelessSSIDID must be specified if op_IfWirelessSSIDID is specified.
             :type val_f_IfWirelessSSIDID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfWirelessSSIDID: If op_IfWirelessSSIDID is specified, this value will be compared to the value in IfWirelessSSIDID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfWirelessSSIDID must be specified if op_IfWirelessSSIDID is specified.
             :type val_c_IfWirelessSSIDID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of local interface for this wireless SSID table. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SSID: The operator to apply to the field SSID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSID: The unique number of service set identifier(SSID) in the wirelessSSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSID: If op_SSID is specified, the field named in this input will be compared to the value in SSID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSID must be specified if op_SSID is specified.
             :type val_f_SSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSID: If op_SSID is specified, this value will be compared to the value in SSID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSID must be specified if op_SSID is specified.
             :type val_c_SSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDBroadcastInd: The operator to apply to the field SSIDBroadcastInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDBroadcastInd: A flag indicates whether the broadcast index of the wireless SSID is enabled or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDBroadcastInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDBroadcastInd: If op_SSIDBroadcastInd is specified, the field named in this input will be compared to the value in SSIDBroadcastInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDBroadcastInd must be specified if op_SSIDBroadcastInd is specified.
             :type val_f_SSIDBroadcastInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDBroadcastInd: If op_SSIDBroadcastInd is specified, this value will be compared to the value in SSIDBroadcastInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDBroadcastInd must be specified if op_SSIDBroadcastInd is specified.
             :type val_c_SSIDBroadcastInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDDefaultVlanIndex: The operator to apply to the field SSIDDefaultVlanIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDDefaultVlanIndex: The default VLAN Index of the wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDDefaultVlanIndex: If op_SSIDDefaultVlanIndex is specified, the field named in this input will be compared to the value in SSIDDefaultVlanIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDDefaultVlanIndex must be specified if op_SSIDDefaultVlanIndex is specified.
             :type val_f_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDDefaultVlanIndex: If op_SSIDDefaultVlanIndex is specified, this value will be compared to the value in SSIDDefaultVlanIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDDefaultVlanIndex must be specified if op_SSIDDefaultVlanIndex is specified.
             :type val_c_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDIndex: The operator to apply to the field SSIDIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDIndex: The service set identifier(SSID) index of the interface wirelessSSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDIndex: If op_SSIDIndex is specified, the field named in this input will be compared to the value in SSIDIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDIndex must be specified if op_SSIDIndex is specified.
             :type val_f_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDIndex: If op_SSIDIndex is specified, this value will be compared to the value in SSIDIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDIndex must be specified if op_SSIDIndex is specified.
             :type val_c_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDMaxAssociations: The operator to apply to the field SSIDMaxAssociations. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDMaxAssociations: The maximum associations formed by the wirelessSSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDMaxAssociations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDMaxAssociations: If op_SSIDMaxAssociations is specified, the field named in this input will be compared to the value in SSIDMaxAssociations using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDMaxAssociations must be specified if op_SSIDMaxAssociations is specified.
             :type val_f_SSIDMaxAssociations: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDMaxAssociations: If op_SSIDMaxAssociations is specified, this value will be compared to the value in SSIDMaxAssociations using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDMaxAssociations must be specified if op_SSIDMaxAssociations is specified.
             :type val_c_SSIDMaxAssociations: String

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

             :param op_WEPMICAlgorithm: The operator to apply to the field WEPMICAlgorithm. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPMICAlgorithm: The algorithm process of web equivalent privacy in the wirelessSSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPMICAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPMICAlgorithm: If op_WEPMICAlgorithm is specified, the field named in this input will be compared to the value in WEPMICAlgorithm using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPMICAlgorithm must be specified if op_WEPMICAlgorithm is specified.
             :type val_f_WEPMICAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPMICAlgorithm: If op_WEPMICAlgorithm is specified, this value will be compared to the value in WEPMICAlgorithm using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPMICAlgorithm must be specified if op_WEPMICAlgorithm is specified.
             :type val_c_WEPMICAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPPermuteAlgorithm: The operator to apply to the field WEPPermuteAlgorithm. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPPermuteAlgorithm: The permutation algorithm of web equivalent privacy in the wirelessSSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPPermuteAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPPermuteAlgorithm: If op_WEPPermuteAlgorithm is specified, the field named in this input will be compared to the value in WEPPermuteAlgorithm using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPPermuteAlgorithm must be specified if op_WEPPermuteAlgorithm is specified.
             :type val_f_WEPPermuteAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPPermuteAlgorithm: If op_WEPPermuteAlgorithm is specified, this value will be compared to the value in WEPPermuteAlgorithm using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPPermuteAlgorithm must be specified if op_WEPPermuteAlgorithm is specified.
             :type val_c_WEPPermuteAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index of the local interface for the wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ifWirelessSSIDChangedCols: The operator to apply to the field ifWirelessSSIDChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDChangedCols: If op_ifWirelessSSIDChangedCols is specified, the field named in this input will be compared to the value in ifWirelessSSIDChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDChangedCols must be specified if op_ifWirelessSSIDChangedCols is specified.
             :type val_f_ifWirelessSSIDChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDChangedCols: If op_ifWirelessSSIDChangedCols is specified, this value will be compared to the value in ifWirelessSSIDChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDChangedCols must be specified if op_ifWirelessSSIDChangedCols is specified.
             :type val_c_ifWirelessSSIDChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDEndTime: The operator to apply to the field ifWirelessSSIDEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDEndTime: If op_ifWirelessSSIDEndTime is specified, the field named in this input will be compared to the value in ifWirelessSSIDEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDEndTime must be specified if op_ifWirelessSSIDEndTime is specified.
             :type val_f_ifWirelessSSIDEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDEndTime: If op_ifWirelessSSIDEndTime is specified, this value will be compared to the value in ifWirelessSSIDEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDEndTime must be specified if op_ifWirelessSSIDEndTime is specified.
             :type val_c_ifWirelessSSIDEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDStartTime: The operator to apply to the field ifWirelessSSIDStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDStartTime: If op_ifWirelessSSIDStartTime is specified, the field named in this input will be compared to the value in ifWirelessSSIDStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDStartTime must be specified if op_ifWirelessSSIDStartTime is specified.
             :type val_f_ifWirelessSSIDStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDStartTime: If op_ifWirelessSSIDStartTime is specified, this value will be compared to the value in ifWirelessSSIDStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDStartTime must be specified if op_ifWirelessSSIDStartTime is specified.
             :type val_c_ifWirelessSSIDStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDTimestamp: The operator to apply to the field ifWirelessSSIDTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDTimestamp: If op_ifWirelessSSIDTimestamp is specified, the field named in this input will be compared to the value in ifWirelessSSIDTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDTimestamp must be specified if op_ifWirelessSSIDTimestamp is specified.
             :type val_f_ifWirelessSSIDTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDTimestamp: If op_ifWirelessSSIDTimestamp is specified, this value will be compared to the value in ifWirelessSSIDTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDTimestamp must be specified if op_ifWirelessSSIDTimestamp is specified.
             :type val_c_ifWirelessSSIDTimestamp: String

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

             :param timestamp: The data returned will represent the if wireless ssids as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid methods. The listed methods will be called on each if wireless ssid returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd.
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

             :param select: The list of attributes to return for each IfWirelessSSID. Valid values are IfWirelessSSIDID, ifWirelessSSIDStartTime, ifWirelessSSIDEndTime, ifWirelessSSIDChangedCols, ifWirelessSSIDTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, SSIDIndex, SSID, SSIDMaxAssociations, WEPMICAlgorithm, WEPPermuteAlgorithm, SSIDDefaultVlanIndex, VlanID, SSIDBroadcastInd. If empty or omitted, all attributes will be returned.
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

             :return if_wireless_ssi_ds: An array of the IfWirelessSSID objects that match the specified input criteria.
             :rtype if_wireless_ssi_ds: Array of IfWirelessSSID

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def interface(self, **kwargs):
        """interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : interface
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def vlan(self, **kwargs):
        """vlan

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : vlan
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDID: The internal NetMRI identifier of wireless SSID in the interface.
             :type IfWirelessSSIDID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
