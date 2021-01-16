from ..broker import Broker


class EndHostMacAddressBroker(Broker):
    controller = "end_host_mac_addresses"

    def index(self, **kwargs):
        """Lists the available end host mac addresses. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the associated Device record.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressID: The internal NetMRI identifier for the End Host MAC Address entry.
             :type EndHostMACAddressID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddress: The IP address of the end host.
             :type IPAddress: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceID: The internal NetMRI identifier for the InfraDevice on which the end host was found.
             :type InfraDeviceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which the end host was found.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MACAddress: The MAC address of the end host.
             :type MACAddress: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the associated Neighbor record.
             :type NeighborID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` EndHostMACAddressID

             :param sort: The data field(s) to use for sorting the output. Default is EndHostMACAddressID. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols.
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

             :param select: The list of attributes to return for each EndHostMacAddress. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols. If empty or omitted, all attributes will be returned.
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

             :return end_host_mac_addresses: An array of the EndHostMacAddress objects that match the specified input criteria.
             :rtype end_host_mac_addresses: Array of EndHostMacAddress

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified end host mac address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param EndHostMACAddressID: The internal NetMRI identifier for the End Host MAC Address entry.
             :type EndHostMACAddressID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return end_host_mac_address: The end host mac address identified by the specified EndHostMACAddressID.
             :rtype end_host_mac_address: EndHostMacAddress

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available end host mac addresses matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the associated Device record.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceName: The determined name of the end host.
             :type DeviceName: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceNetBIOSName: The NetBIOS name of the end host.
             :type DeviceNetBIOSName: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceType: The determined type of the end host.
             :type DeviceType: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type EndHostMACAddressChangedCols: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressEndTime: The ending effective time of this record, or empty if still in effect.
             :type EndHostMACAddressEndTime: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressID: The internal NetMRI identifier for the End Host MAC Address entry.
             :type EndHostMACAddressID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressStartTime: The starting effective time of this record.
             :type EndHostMACAddressStartTime: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndHostMACAddressTimestamp: The date and time this record was collected or calculated.
             :type EndHostMACAddressTimestamp: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FirstSeenTime: The date and time this record was first seen.
             :type FirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddress: The IP address of the end host.
             :type IPAddress: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddressNumeric: The IP address of the end host, in numerical form.
             :type IPAddressNumeric: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceID: The internal NetMRI identifier for the InfraDevice on which the end host was found.
             :type InfraDeviceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which the end host was found.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MACAddress: The MAC address of the end host.
             :type MACAddress: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the associated Neighbor record.
             :type NeighborID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Network: The name of the Network View associated.
             :type Network: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkID: The internal NetMRI identifier of the associated network.
             :type NetworkID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The interface index on which the end host was found.
             :type ifIndex: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` EndHostMACAddressID

             :param sort: The data field(s) to use for sorting the output. Default is EndHostMACAddressID. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols.
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

             :param select: The list of attributes to return for each EndHostMacAddress. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against end host mac addresses, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DeviceName, DeviceNetBIOSName, DeviceType, EndHostMACAddressChangedCols, EndHostMACAddressEndTime, EndHostMACAddressID, EndHostMACAddressStartTime, EndHostMACAddressTimestamp, FirstSeenTime, IPAddress, IPAddressNumeric, InfraDeviceID, InterfaceID, MACAddress, NeighborID, Network, NetworkID, ifIndex.
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

             :return end_host_mac_addresses: An array of the EndHostMacAddress objects that match the specified input criteria.
             :rtype end_host_mac_addresses: Array of EndHostMacAddress

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available end host mac addresses matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DeviceName, DeviceNetBIOSName, DeviceType, EndHostMACAddressChangedCols, EndHostMACAddressEndTime, EndHostMACAddressID, EndHostMACAddressStartTime, EndHostMACAddressTimestamp, FirstSeenTime, IPAddress, IPAddressNumeric, InfraDeviceID, InterfaceID, MACAddress, NeighborID, Network, NetworkID, ifIndex.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the associated Device record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceName: The operator to apply to the field DeviceName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceName: The determined name of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceName: If op_DeviceName is specified, the field named in this input will be compared to the value in DeviceName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceName must be specified if op_DeviceName is specified.
             :type val_f_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceName: If op_DeviceName is specified, this value will be compared to the value in DeviceName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceName must be specified if op_DeviceName is specified.
             :type val_c_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceNetBIOSName: The operator to apply to the field DeviceNetBIOSName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceNetBIOSName: The NetBIOS name of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceNetBIOSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceNetBIOSName: If op_DeviceNetBIOSName is specified, the field named in this input will be compared to the value in DeviceNetBIOSName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceNetBIOSName must be specified if op_DeviceNetBIOSName is specified.
             :type val_f_DeviceNetBIOSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceNetBIOSName: If op_DeviceNetBIOSName is specified, this value will be compared to the value in DeviceNetBIOSName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceNetBIOSName must be specified if op_DeviceNetBIOSName is specified.
             :type val_c_DeviceNetBIOSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceType: The operator to apply to the field DeviceType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceType: The determined type of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceType: If op_DeviceType is specified, the field named in this input will be compared to the value in DeviceType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceType must be specified if op_DeviceType is specified.
             :type val_f_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceType: If op_DeviceType is specified, this value will be compared to the value in DeviceType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceType must be specified if op_DeviceType is specified.
             :type val_c_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndHostMACAddressChangedCols: The operator to apply to the field EndHostMACAddressChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndHostMACAddressChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndHostMACAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndHostMACAddressChangedCols: If op_EndHostMACAddressChangedCols is specified, the field named in this input will be compared to the value in EndHostMACAddressChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndHostMACAddressChangedCols must be specified if op_EndHostMACAddressChangedCols is specified.
             :type val_f_EndHostMACAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndHostMACAddressChangedCols: If op_EndHostMACAddressChangedCols is specified, this value will be compared to the value in EndHostMACAddressChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndHostMACAddressChangedCols must be specified if op_EndHostMACAddressChangedCols is specified.
             :type val_c_EndHostMACAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndHostMACAddressEndTime: The operator to apply to the field EndHostMACAddressEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndHostMACAddressEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndHostMACAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndHostMACAddressEndTime: If op_EndHostMACAddressEndTime is specified, the field named in this input will be compared to the value in EndHostMACAddressEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndHostMACAddressEndTime must be specified if op_EndHostMACAddressEndTime is specified.
             :type val_f_EndHostMACAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndHostMACAddressEndTime: If op_EndHostMACAddressEndTime is specified, this value will be compared to the value in EndHostMACAddressEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndHostMACAddressEndTime must be specified if op_EndHostMACAddressEndTime is specified.
             :type val_c_EndHostMACAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndHostMACAddressID: The operator to apply to the field EndHostMACAddressID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndHostMACAddressID: The internal NetMRI identifier for the End Host MAC Address entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndHostMACAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndHostMACAddressID: If op_EndHostMACAddressID is specified, the field named in this input will be compared to the value in EndHostMACAddressID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndHostMACAddressID must be specified if op_EndHostMACAddressID is specified.
             :type val_f_EndHostMACAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndHostMACAddressID: If op_EndHostMACAddressID is specified, this value will be compared to the value in EndHostMACAddressID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndHostMACAddressID must be specified if op_EndHostMACAddressID is specified.
             :type val_c_EndHostMACAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndHostMACAddressStartTime: The operator to apply to the field EndHostMACAddressStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndHostMACAddressStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndHostMACAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndHostMACAddressStartTime: If op_EndHostMACAddressStartTime is specified, the field named in this input will be compared to the value in EndHostMACAddressStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndHostMACAddressStartTime must be specified if op_EndHostMACAddressStartTime is specified.
             :type val_f_EndHostMACAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndHostMACAddressStartTime: If op_EndHostMACAddressStartTime is specified, this value will be compared to the value in EndHostMACAddressStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndHostMACAddressStartTime must be specified if op_EndHostMACAddressStartTime is specified.
             :type val_c_EndHostMACAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndHostMACAddressTimestamp: The operator to apply to the field EndHostMACAddressTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndHostMACAddressTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndHostMACAddressTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndHostMACAddressTimestamp: If op_EndHostMACAddressTimestamp is specified, the field named in this input will be compared to the value in EndHostMACAddressTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndHostMACAddressTimestamp must be specified if op_EndHostMACAddressTimestamp is specified.
             :type val_f_EndHostMACAddressTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndHostMACAddressTimestamp: If op_EndHostMACAddressTimestamp is specified, this value will be compared to the value in EndHostMACAddressTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndHostMACAddressTimestamp must be specified if op_EndHostMACAddressTimestamp is specified.
             :type val_c_EndHostMACAddressTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FirstSeenTime: The operator to apply to the field FirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FirstSeenTime: The date and time this record was first seen. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FirstSeenTime: If op_FirstSeenTime is specified, the field named in this input will be compared to the value in FirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FirstSeenTime must be specified if op_FirstSeenTime is specified.
             :type val_f_FirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FirstSeenTime: If op_FirstSeenTime is specified, this value will be compared to the value in FirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FirstSeenTime must be specified if op_FirstSeenTime is specified.
             :type val_c_FirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPAddress: The operator to apply to the field IPAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPAddress: The IP address of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPAddress: If op_IPAddress is specified, the field named in this input will be compared to the value in IPAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPAddress must be specified if op_IPAddress is specified.
             :type val_f_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddress: If op_IPAddress is specified, this value will be compared to the value in IPAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPAddress must be specified if op_IPAddress is specified.
             :type val_c_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPAddressNumeric: The operator to apply to the field IPAddressNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPAddressNumeric: The IP address of the end host, in numerical form. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPAddressNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPAddressNumeric: If op_IPAddressNumeric is specified, the field named in this input will be compared to the value in IPAddressNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPAddressNumeric must be specified if op_IPAddressNumeric is specified.
             :type val_f_IPAddressNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddressNumeric: If op_IPAddressNumeric is specified, this value will be compared to the value in IPAddressNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPAddressNumeric must be specified if op_IPAddressNumeric is specified.
             :type val_c_IPAddressNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InfraDeviceID: The operator to apply to the field InfraDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfraDeviceID: The internal NetMRI identifier for the InfraDevice on which the end host was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfraDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfraDeviceID: If op_InfraDeviceID is specified, the field named in this input will be compared to the value in InfraDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfraDeviceID must be specified if op_InfraDeviceID is specified.
             :type val_f_InfraDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfraDeviceID: If op_InfraDeviceID is specified, this value will be compared to the value in InfraDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfraDeviceID must be specified if op_InfraDeviceID is specified.
             :type val_c_InfraDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the interface on which the end host was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_MACAddress: The operator to apply to the field MACAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MACAddress: The MAC address of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MACAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MACAddress: If op_MACAddress is specified, the field named in this input will be compared to the value in MACAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MACAddress must be specified if op_MACAddress is specified.
             :type val_f_MACAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MACAddress: If op_MACAddress is specified, this value will be compared to the value in MACAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MACAddress must be specified if op_MACAddress is specified.
             :type val_c_MACAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborID: The operator to apply to the field NeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborID: The internal NetMRI identifier for the associated Neighbor record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborID: If op_NeighborID is specified, the field named in this input will be compared to the value in NeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborID must be specified if op_NeighborID is specified.
             :type val_f_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborID: If op_NeighborID is specified, this value will be compared to the value in NeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborID must be specified if op_NeighborID is specified.
             :type val_c_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Network: The operator to apply to the field Network. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Network: The name of the Network View associated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Network: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Network: If op_Network is specified, the field named in this input will be compared to the value in Network using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Network must be specified if op_Network is specified.
             :type val_f_Network: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Network: If op_Network is specified, this value will be compared to the value in Network using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Network must be specified if op_Network is specified.
             :type val_c_Network: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NetworkID: The operator to apply to the field NetworkID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NetworkID: The internal NetMRI identifier of the associated network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NetworkID: If op_NetworkID is specified, the field named in this input will be compared to the value in NetworkID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NetworkID must be specified if op_NetworkID is specified.
             :type val_f_NetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NetworkID: If op_NetworkID is specified, this value will be compared to the value in NetworkID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NetworkID must be specified if op_NetworkID is specified.
             :type val_c_NetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The interface index on which the end host was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` EndHostMACAddressID

             :param sort: The data field(s) to use for sorting the output. Default is EndHostMACAddressID. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols.
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

             :param select: The list of attributes to return for each EndHostMacAddress. Valid values are EndHostMACAddressID, NetworkID, Network, MACAddress, IPAddress, IPAddressNumeric, DataSourceID, DeviceType, DeviceName, DeviceNetBIOSName, DeviceID, ifIndex, InterfaceID, InfraDeviceID, NeighborID, EndHostMACAddressTimestamp, FirstSeenTime, EndHostMACAddressStartTime, EndHostMACAddressEndTime, EndHostMACAddressChangedCols. If empty or omitted, all attributes will be returned.
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

             :return end_host_mac_addresses: An array of the EndHostMacAddress objects that match the specified input criteria.
             :rtype end_host_mac_addresses: Array of EndHostMacAddress

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
