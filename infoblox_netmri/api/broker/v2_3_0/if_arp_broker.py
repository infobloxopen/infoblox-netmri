from ..broker import Broker


class IfArpBroker(Broker):
    controller = "if_arps"

    def show(self, **kwargs):
        """Shows the details for the specified if arp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if arp methods. The listed methods will be called on each if arp returned and included in the output. Available methods are: remote_device, remote_interface, data_source, device, interface, vrf, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: remote_device, remote_interface, data_source, device, interface, vrf.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_arp: The if arp identified by the specified IfArpID.
             :rtype if_arp: IfArp

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available if arps. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device from which this ARP entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device from which this ARP entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrDotted: The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format.
             :type IPAddrDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrDotted: The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format.
             :type IPAddrDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrNumeric: The numerical value of the IP address for this ARP entry.
             :type IPAddrNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrNumeric: The numerical value of the IP address for this ARP entry.
             :type IPAddrNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this ARP table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this ARP table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAddr: The physical address for this ARP entry.
             :type PhysicalAddr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAddr: The physical address for this ARP entry.
             :type PhysicalAddr: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrfID: The internal NetMRI identifier for the VRF to which this ARP entry applies, if available.
             :type VrfID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfID: The internal NetMRI identifier for the VRF to which this ARP entry applies, if available.
             :type VrfID: Array of Integer

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

             :param timestamp: The data returned will represent the if arps as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if arp methods. The listed methods will be called on each if arp returned and included in the output. Available methods are: remote_device, remote_interface, data_source, device, interface, vrf, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: remote_device, remote_interface, data_source, device, interface, vrf.
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
            |  ``default:`` IfArpID

             :param sort: The data field(s) to use for sorting the output. Default is IfArpID. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID.
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

             :param select: The list of attributes to return for each IfArp. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID. If empty or omitted, all attributes will be returned.
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

             :return if_arps: An array of the IfArp objects that match the specified input criteria.
             :rtype if_arps: Array of IfArp

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available if arps matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ArpChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ArpChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpDeviceID: The internal NetMRI identifier for the remote device to which the ARP entry refers, if available.
             :type ArpDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpDeviceID: The internal NetMRI identifier for the remote device to which the ARP entry refers, if available.
             :type ArpDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpEndTime: The ending effective time of this record, or empty if still in effect.
             :type ArpEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpEndTime: The ending effective time of this record, or empty if still in effect.
             :type ArpEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpInterfaceID: The internal NetMRI identifier for the remote interface to which the ARP entry refers, if available.
             :type ArpInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpInterfaceID: The internal NetMRI identifier for the remote interface to which the ARP entry refers, if available.
             :type ArpInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpStartTime: The starting effective time of this record.
             :type ArpStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpStartTime: The starting effective time of this record.
             :type ArpStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ArpTimestamp: The date and time this record was collected or calculated.
             :type ArpTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ArpTimestamp: The date and time this record was collected or calculated.
             :type ArpTimestamp: Array of DateTime

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

             :param DeviceID: The internal NetMRI identifier of the device from which this ARP entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device from which this ARP entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrDotted: The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format.
             :type IPAddrDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrDotted: The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format.
             :type IPAddrDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrNumeric: The numerical value of the IP address for this ARP entry.
             :type IPAddrNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddrNumeric: The numerical value of the IP address for this ARP entry.
             :type IPAddrNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this ARP table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this ARP table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAddr: The physical address for this ARP entry.
             :type PhysicalAddr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PhysicalAddr: The physical address for this ARP entry.
             :type PhysicalAddr: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrfID: The internal NetMRI identifier for the VRF to which this ARP entry applies, if available.
             :type VrfID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfID: The internal NetMRI identifier for the VRF to which this ARP entry applies, if available.
             :type VrfID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this ARP table entry.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this ARP table entry.
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
            |  ``default:`` None

             :param timestamp: The data returned will represent the if arps as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if arp methods. The listed methods will be called on each if arp returned and included in the output. Available methods are: remote_device, remote_interface, data_source, device, interface, vrf, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: remote_device, remote_interface, data_source, device, interface, vrf.
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
            |  ``default:`` IfArpID

             :param sort: The data field(s) to use for sorting the output. Default is IfArpID. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID.
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

             :param select: The list of attributes to return for each IfArp. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if arps, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ArpChangedCols, ArpDeviceID, ArpEndTime, ArpInterfaceID, ArpStartTime, ArpTimestamp, DataSourceID, DeviceID, IPAddrDotted, IPAddrNumeric, IfArpID, InterfaceID, PhysicalAddr, VrfID, ifIndex.
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

             :return if_arps: An array of the IfArp objects that match the specified input criteria.
             :rtype if_arps: Array of IfArp

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if arps matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ArpChangedCols, ArpDeviceID, ArpEndTime, ArpInterfaceID, ArpStartTime, ArpTimestamp, DataSourceID, DeviceID, IPAddrDotted, IPAddrNumeric, IfArpID, InterfaceID, PhysicalAddr, VrfID, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpChangedCols: The operator to apply to the field ArpChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpChangedCols: If op_ArpChangedCols is specified, the field named in this input will be compared to the value in ArpChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpChangedCols must be specified if op_ArpChangedCols is specified.
             :type val_f_ArpChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpChangedCols: If op_ArpChangedCols is specified, this value will be compared to the value in ArpChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpChangedCols must be specified if op_ArpChangedCols is specified.
             :type val_c_ArpChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpDeviceID: The operator to apply to the field ArpDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpDeviceID: The internal NetMRI identifier for the remote device to which the ARP entry refers, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpDeviceID: If op_ArpDeviceID is specified, the field named in this input will be compared to the value in ArpDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpDeviceID must be specified if op_ArpDeviceID is specified.
             :type val_f_ArpDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpDeviceID: If op_ArpDeviceID is specified, this value will be compared to the value in ArpDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpDeviceID must be specified if op_ArpDeviceID is specified.
             :type val_c_ArpDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpEndTime: The operator to apply to the field ArpEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpEndTime: If op_ArpEndTime is specified, the field named in this input will be compared to the value in ArpEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpEndTime must be specified if op_ArpEndTime is specified.
             :type val_f_ArpEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpEndTime: If op_ArpEndTime is specified, this value will be compared to the value in ArpEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpEndTime must be specified if op_ArpEndTime is specified.
             :type val_c_ArpEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpInterfaceID: The operator to apply to the field ArpInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpInterfaceID: The internal NetMRI identifier for the remote interface to which the ARP entry refers, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpInterfaceID: If op_ArpInterfaceID is specified, the field named in this input will be compared to the value in ArpInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpInterfaceID must be specified if op_ArpInterfaceID is specified.
             :type val_f_ArpInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpInterfaceID: If op_ArpInterfaceID is specified, this value will be compared to the value in ArpInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpInterfaceID must be specified if op_ArpInterfaceID is specified.
             :type val_c_ArpInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpStartTime: The operator to apply to the field ArpStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpStartTime: If op_ArpStartTime is specified, the field named in this input will be compared to the value in ArpStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpStartTime must be specified if op_ArpStartTime is specified.
             :type val_f_ArpStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpStartTime: If op_ArpStartTime is specified, this value will be compared to the value in ArpStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpStartTime must be specified if op_ArpStartTime is specified.
             :type val_c_ArpStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ArpTimestamp: The operator to apply to the field ArpTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ArpTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ArpTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ArpTimestamp: If op_ArpTimestamp is specified, the field named in this input will be compared to the value in ArpTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ArpTimestamp must be specified if op_ArpTimestamp is specified.
             :type val_f_ArpTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ArpTimestamp: If op_ArpTimestamp is specified, this value will be compared to the value in ArpTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ArpTimestamp must be specified if op_ArpTimestamp is specified.
             :type val_c_ArpTimestamp: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of the device from which this ARP entry was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IPAddrDotted: The operator to apply to the field IPAddrDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPAddrDotted: The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPAddrDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPAddrDotted: If op_IPAddrDotted is specified, the field named in this input will be compared to the value in IPAddrDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPAddrDotted must be specified if op_IPAddrDotted is specified.
             :type val_f_IPAddrDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddrDotted: If op_IPAddrDotted is specified, this value will be compared to the value in IPAddrDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPAddrDotted must be specified if op_IPAddrDotted is specified.
             :type val_c_IPAddrDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPAddrNumeric: The operator to apply to the field IPAddrNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPAddrNumeric: The numerical value of the IP address for this ARP entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPAddrNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPAddrNumeric: If op_IPAddrNumeric is specified, the field named in this input will be compared to the value in IPAddrNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPAddrNumeric must be specified if op_IPAddrNumeric is specified.
             :type val_f_IPAddrNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddrNumeric: If op_IPAddrNumeric is specified, this value will be compared to the value in IPAddrNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPAddrNumeric must be specified if op_IPAddrNumeric is specified.
             :type val_c_IPAddrNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IfArpID: The operator to apply to the field IfArpID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfArpID: The internal NetMRI identifier for this ARP entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfArpID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfArpID: If op_IfArpID is specified, the field named in this input will be compared to the value in IfArpID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfArpID must be specified if op_IfArpID is specified.
             :type val_f_IfArpID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfArpID: If op_IfArpID is specified, this value will be compared to the value in IfArpID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfArpID must be specified if op_IfArpID is specified.
             :type val_c_IfArpID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the local interface for this ARP table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PhysicalAddr: The operator to apply to the field PhysicalAddr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PhysicalAddr: The physical address for this ARP entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PhysicalAddr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PhysicalAddr: If op_PhysicalAddr is specified, the field named in this input will be compared to the value in PhysicalAddr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PhysicalAddr must be specified if op_PhysicalAddr is specified.
             :type val_f_PhysicalAddr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PhysicalAddr: If op_PhysicalAddr is specified, this value will be compared to the value in PhysicalAddr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PhysicalAddr must be specified if op_PhysicalAddr is specified.
             :type val_c_PhysicalAddr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfID: The operator to apply to the field VrfID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfID: The internal NetMRI identifier for the VRF to which this ARP entry applies, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfID: If op_VrfID is specified, the field named in this input will be compared to the value in VrfID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfID must be specified if op_VrfID is specified.
             :type val_f_VrfID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfID: If op_VrfID is specified, this value will be compared to the value in VrfID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfID must be specified if op_VrfID is specified.
             :type val_c_VrfID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index for the local interface for this ARP table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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
            |  ``default:`` None

             :param timestamp: The data returned will represent the if arps as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if arp methods. The listed methods will be called on each if arp returned and included in the output. Available methods are: remote_device, remote_interface, data_source, device, interface, vrf, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: remote_device, remote_interface, data_source, device, interface, vrf.
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
            |  ``default:`` IfArpID

             :param sort: The data field(s) to use for sorting the output. Default is IfArpID. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID.
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

             :param select: The list of attributes to return for each IfArp. Valid values are IfArpID, DataSourceID, InterfaceID, DeviceID, ifIndex, ArpStartTime, ArpEndTime, ArpChangedCols, ArpTimestamp, PhysicalAddr, IPAddrNumeric, IPAddrDotted, ArpDeviceID, ArpInterfaceID, VrfID. If empty or omitted, all attributes will be returned.
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

             :return if_arps: An array of the IfArp objects that match the specified input criteria.
             :rtype if_arps: Array of IfArp

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def interface(self, **kwargs):
        """The local interface for this ARP table entry.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The local interface for this ARP table entry.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def remote_device(self, **kwargs):
        """The remote device to which the ARP entry refers, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The remote device to which the ARP entry refers, if available.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("remote_device"), kwargs)

    def remote_interface(self, **kwargs):
        """The remote interface to which the ARP entry refers, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The remote interface to which the ARP entry refers, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("remote_interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this ARP entry was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this ARP entry was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this ARP entry was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfArpID: The internal NetMRI identifier for this ARP entry.
             :type IfArpID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device from which this ARP entry was collected.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
