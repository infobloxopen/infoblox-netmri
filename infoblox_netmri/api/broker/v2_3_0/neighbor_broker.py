from ..broker import Broker


class NeighborBroker(Broker):
    controller = "neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of neighbor methods. The listed methods will be called on each neighbor returned and included in the output. Available methods are: network_id, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, neighbor_device, neighbor_interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return neighbor: The neighbor identified by the specified NeighborID.
             :rtype neighbor: Neighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

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

             :param DeviceID: The internal NetMRI identifier for the source device in this neighbor relationship.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the source device in this neighbor relationship.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the source interface in this neighbor relationship.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the source interface in this neighbor relationship.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborDeviceID: The internal NetMRI identifier for the destination device in this neighbor relationship.
             :type NeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborDeviceID: The internal NetMRI identifier for the destination device in this neighbor relationship.
             :type NeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborInterfaceID: The internal NetMRI identifier for the destination interface in this neighbor relationship.
             :type NeighborInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborInterfaceID: The internal NetMRI identifier for the destination interface in this neighbor relationship.
             :type NeighborInterfaceID: Array of Integer

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

             :param timestamp: The data returned will represent the neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of neighbor methods. The listed methods will be called on each neighbor returned and included in the output. Available methods are: network_id, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, neighbor_device, neighbor_interface.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID.
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

             :param select: The list of attributes to return for each Neighbor. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID. If empty or omitted, all attributes will be returned.
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

             :return neighbors: An array of the Neighbor objects that match the specified input criteria.
             :rtype neighbors: Array of Neighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BGPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a BGP route.
             :type BGPRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BGPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a BGP route.
             :type BGPRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's CDP entries.
             :type CDPInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's CDP entries.
             :type CDPInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for the CdpNeighbor object associated with this neighbor entry (if any).
             :type CDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for the CdpNeighbor object associated with this neighbor entry (if any).
             :type CDPNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CombinedInd: A flag indicating that these devices have basic layer 1/2 connectivity.
             :type CombinedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CombinedInd: A flag indicating that these devices have basic layer 1/2 connectivity.
             :type CombinedInd: Array of Boolean

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

             :param DeviceID: The internal NetMRI identifier for the source device in this neighbor relationship.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the source device in this neighbor relationship.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DirectEthernetInd: A flag indicating that this neighbor relationship was derived using the NetMRI direct Ethernet neighbor detection algorithm (for example, two routers directly connected via Ethernet, without any switches between them).
             :type DirectEthernetInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DirectEthernetInd: A flag indicating that this neighbor relationship was derived using the NetMRI direct Ethernet neighbor detection algorithm (for example, two routers directly connected via Ethernet, without any switches between them).
             :type DirectEthernetInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IGRPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an IGRP or EIGRP route.
             :type IGRPRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IGRPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an IGRP or EIGRP route.
             :type IGRPRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship; that is, the destination device is a next hop for at least one route on the source device.
             :type IPRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship; that is, the destination device is a next hop for at least one route on the source device.
             :type IPRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the source interface in this neighbor relationship.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the source interface in this neighbor relationship.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's LLDP entries.
             :type LLDPInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's LLDP entries.
             :type LLDPInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LocalRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a local route.
             :type LocalRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LocalRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a local route.
             :type LocalRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborDeviceID: The internal NetMRI identifier for the destination device in this neighbor relationship.
             :type NeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborDeviceID: The internal NetMRI identifier for the destination device in this neighbor relationship.
             :type NeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type NeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type NeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborFirstSeenTime: The date and time this neighbor was first seen on the network, and since which it has been continuously present.
             :type NeighborFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborFirstSeenTime: The date and time this neighbor was first seen on the network, and since which it has been continuously present.
             :type NeighborFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborIfIndex: The SNMP interface index of the destination device interface.
             :type NeighborIfIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborIfIndex: The SNMP interface index of the destination device interface.
             :type NeighborIfIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborInterfaceID: The internal NetMRI identifier for the destination interface in this neighbor relationship.
             :type NeighborInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborInterfaceID: The internal NetMRI identifier for the destination interface in this neighbor relationship.
             :type NeighborInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborNetworkDeviceInd: A flag indicating if the destination device is a network device or an end host.
             :type NeighborNetworkDeviceInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborNetworkDeviceInd: A flag indicating if the destination device is a network device or an end host.
             :type NeighborNetworkDeviceInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborStartTime: The starting effective time of this revision of the record.
             :type NeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborStartTime: The starting effective time of this revision of the record.
             :type NeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborTimestamp: The date and time this record was collected or calculated.
             :type NeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborTimestamp: The date and time this record was collected or calculated.
             :type NeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkDeviceInd: A flag indicating if the source device is a network device or an end host.
             :type NetworkDeviceInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkDeviceInd: A flag indicating if the source device is a network device or an end host.
             :type NetworkDeviceInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OSPFRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an OSPF route.
             :type OSPFRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OSPFRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an OSPF route.
             :type OSPFRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ProtoRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a dynamic protocol defined route.
             :type ProtoRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ProtoRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a dynamic protocol defined route.
             :type ProtoRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdInd: A flag indicating that this neighbor relationship was derived by reversing a switch forwarding neighbor relationship.
             :type RevSwitchFwdInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdInd: A flag indicating that this neighbor relationship was derived by reversing a switch forwarding neighbor relationship.
             :type RevSwitchFwdInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialInd: A flag indicating that this neighbor relationship was derived using the NetMRI point-to-point neighbor detection algorithm. Despite the name this may include point-to-point relationships on interfaces other than serial interfaces.
             :type SerialInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialInd: A flag indicating that this neighbor relationship was derived using the NetMRI point-to-point neighbor detection algorithm. Despite the name this may include point-to-point relationships on interfaces other than serial interfaces.
             :type SerialInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StaticRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a static route.
             :type StaticRoutedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StaticRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a static route.
             :type StaticRoutedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdInd: A flag indicating that this neighbor relationship was derived using the NetMRI switch forwarding neighbor detection algorithm.
             :type SwitchFwdInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdInd: A flag indicating that this neighbor relationship was derived using the NetMRI switch forwarding neighbor detection algorithm.
             :type SwitchFwdInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP interface index of the source device interface.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP interface index of the source device interface.
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

             :param timestamp: The data returned will represent the neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of neighbor methods. The listed methods will be called on each neighbor returned and included in the output. Available methods are: network_id, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, neighbor_device, neighbor_interface.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID.
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

             :param select: The list of attributes to return for each Neighbor. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: BGPRoutedInd, CDPInd, CDPNeighborID, CombinedInd, DataSourceID, DeviceID, DirectEthernetInd, IGRPRoutedInd, IPRoutedInd, InterfaceID, LLDPInd, LLDPNeighborID, LocalRoutedInd, NeighborChangedCols, NeighborDeviceID, NeighborEndTime, NeighborFirstSeenTime, NeighborID, NeighborIfIndex, NeighborInterfaceID, NeighborNetworkDeviceInd, NeighborStartTime, NeighborTimestamp, NetworkDeviceInd, OSPFRoutedInd, ProtoRoutedInd, RevSwitchFwdInd, SerialInd, StaticRoutedInd, SwitchFwdInd, ifIndex.
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

             :return neighbors: An array of the Neighbor objects that match the specified input criteria.
             :rtype neighbors: Array of Neighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: BGPRoutedInd, CDPInd, CDPNeighborID, CombinedInd, DataSourceID, DeviceID, DirectEthernetInd, IGRPRoutedInd, IPRoutedInd, InterfaceID, LLDPInd, LLDPNeighborID, LocalRoutedInd, NeighborChangedCols, NeighborDeviceID, NeighborEndTime, NeighborFirstSeenTime, NeighborID, NeighborIfIndex, NeighborInterfaceID, NeighborNetworkDeviceInd, NeighborStartTime, NeighborTimestamp, NetworkDeviceInd, OSPFRoutedInd, ProtoRoutedInd, RevSwitchFwdInd, SerialInd, StaticRoutedInd, SwitchFwdInd, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BGPRoutedInd: The operator to apply to the field BGPRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BGPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a BGP route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BGPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BGPRoutedInd: If op_BGPRoutedInd is specified, the field named in this input will be compared to the value in BGPRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BGPRoutedInd must be specified if op_BGPRoutedInd is specified.
             :type val_f_BGPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BGPRoutedInd: If op_BGPRoutedInd is specified, this value will be compared to the value in BGPRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BGPRoutedInd must be specified if op_BGPRoutedInd is specified.
             :type val_c_BGPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPInd: The operator to apply to the field CDPInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's CDP entries. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPInd: If op_CDPInd is specified, the field named in this input will be compared to the value in CDPInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPInd must be specified if op_CDPInd is specified.
             :type val_f_CDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPInd: If op_CDPInd is specified, this value will be compared to the value in CDPInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPInd must be specified if op_CDPInd is specified.
             :type val_c_CDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborID: The operator to apply to the field CDPNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborID: The internal NetMRI identifier for the CdpNeighbor object associated with this neighbor entry (if any). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborID: If op_CDPNeighborID is specified, the field named in this input will be compared to the value in CDPNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborID must be specified if op_CDPNeighborID is specified.
             :type val_f_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborID: If op_CDPNeighborID is specified, this value will be compared to the value in CDPNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborID must be specified if op_CDPNeighborID is specified.
             :type val_c_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CombinedInd: The operator to apply to the field CombinedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CombinedInd: A flag indicating that these devices have basic layer 1/2 connectivity. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CombinedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CombinedInd: If op_CombinedInd is specified, the field named in this input will be compared to the value in CombinedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CombinedInd must be specified if op_CombinedInd is specified.
             :type val_f_CombinedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CombinedInd: If op_CombinedInd is specified, this value will be compared to the value in CombinedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CombinedInd must be specified if op_CombinedInd is specified.
             :type val_c_CombinedInd: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the source device in this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DirectEthernetInd: The operator to apply to the field DirectEthernetInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DirectEthernetInd: A flag indicating that this neighbor relationship was derived using the NetMRI direct Ethernet neighbor detection algorithm (for example, two routers directly connected via Ethernet, without any switches between them). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DirectEthernetInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DirectEthernetInd: If op_DirectEthernetInd is specified, the field named in this input will be compared to the value in DirectEthernetInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DirectEthernetInd must be specified if op_DirectEthernetInd is specified.
             :type val_f_DirectEthernetInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DirectEthernetInd: If op_DirectEthernetInd is specified, this value will be compared to the value in DirectEthernetInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DirectEthernetInd must be specified if op_DirectEthernetInd is specified.
             :type val_c_DirectEthernetInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IGRPRoutedInd: The operator to apply to the field IGRPRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IGRPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an IGRP or EIGRP route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IGRPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IGRPRoutedInd: If op_IGRPRoutedInd is specified, the field named in this input will be compared to the value in IGRPRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IGRPRoutedInd must be specified if op_IGRPRoutedInd is specified.
             :type val_f_IGRPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IGRPRoutedInd: If op_IGRPRoutedInd is specified, this value will be compared to the value in IGRPRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IGRPRoutedInd must be specified if op_IGRPRoutedInd is specified.
             :type val_c_IGRPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedInd: The operator to apply to the field IPRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship; that is, the destination device is a next hop for at least one route on the source device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedInd: If op_IPRoutedInd is specified, the field named in this input will be compared to the value in IPRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedInd must be specified if op_IPRoutedInd is specified.
             :type val_f_IPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedInd: If op_IPRoutedInd is specified, this value will be compared to the value in IPRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedInd must be specified if op_IPRoutedInd is specified.
             :type val_c_IPRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the source interface in this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_LLDPInd: The operator to apply to the field LLDPInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPInd: A flag indicating that this neighbor relationship was derived based upon the source device's LLDP entries. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPInd: If op_LLDPInd is specified, the field named in this input will be compared to the value in LLDPInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPInd must be specified if op_LLDPInd is specified.
             :type val_f_LLDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPInd: If op_LLDPInd is specified, this value will be compared to the value in LLDPInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPInd must be specified if op_LLDPInd is specified.
             :type val_c_LLDPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborID: The operator to apply to the field LLDPNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborID: If op_LLDPNeighborID is specified, the field named in this input will be compared to the value in LLDPNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborID must be specified if op_LLDPNeighborID is specified.
             :type val_f_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborID: If op_LLDPNeighborID is specified, this value will be compared to the value in LLDPNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborID must be specified if op_LLDPNeighborID is specified.
             :type val_c_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LocalRoutedInd: The operator to apply to the field LocalRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LocalRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a local route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LocalRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LocalRoutedInd: If op_LocalRoutedInd is specified, the field named in this input will be compared to the value in LocalRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LocalRoutedInd must be specified if op_LocalRoutedInd is specified.
             :type val_f_LocalRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LocalRoutedInd: If op_LocalRoutedInd is specified, this value will be compared to the value in LocalRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LocalRoutedInd must be specified if op_LocalRoutedInd is specified.
             :type val_c_LocalRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborChangedCols: The operator to apply to the field NeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborChangedCols: If op_NeighborChangedCols is specified, the field named in this input will be compared to the value in NeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborChangedCols must be specified if op_NeighborChangedCols is specified.
             :type val_f_NeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborChangedCols: If op_NeighborChangedCols is specified, this value will be compared to the value in NeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborChangedCols must be specified if op_NeighborChangedCols is specified.
             :type val_c_NeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborDeviceID: The operator to apply to the field NeighborDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborDeviceID: The internal NetMRI identifier for the destination device in this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborDeviceID: If op_NeighborDeviceID is specified, the field named in this input will be compared to the value in NeighborDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborDeviceID must be specified if op_NeighborDeviceID is specified.
             :type val_f_NeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborDeviceID: If op_NeighborDeviceID is specified, this value will be compared to the value in NeighborDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborDeviceID must be specified if op_NeighborDeviceID is specified.
             :type val_c_NeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborEndTime: The operator to apply to the field NeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborEndTime: If op_NeighborEndTime is specified, the field named in this input will be compared to the value in NeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborEndTime must be specified if op_NeighborEndTime is specified.
             :type val_f_NeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborEndTime: If op_NeighborEndTime is specified, this value will be compared to the value in NeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborEndTime must be specified if op_NeighborEndTime is specified.
             :type val_c_NeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborFirstSeenTime: The operator to apply to the field NeighborFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborFirstSeenTime: The date and time this neighbor was first seen on the network, and since which it has been continuously present. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborFirstSeenTime: If op_NeighborFirstSeenTime is specified, the field named in this input will be compared to the value in NeighborFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborFirstSeenTime must be specified if op_NeighborFirstSeenTime is specified.
             :type val_f_NeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborFirstSeenTime: If op_NeighborFirstSeenTime is specified, this value will be compared to the value in NeighborFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborFirstSeenTime must be specified if op_NeighborFirstSeenTime is specified.
             :type val_c_NeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborID: The operator to apply to the field NeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborID: The internal NetMRI identifier for this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_NeighborIfIndex: The operator to apply to the field NeighborIfIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborIfIndex: The SNMP interface index of the destination device interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborIfIndex: If op_NeighborIfIndex is specified, the field named in this input will be compared to the value in NeighborIfIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborIfIndex must be specified if op_NeighborIfIndex is specified.
             :type val_f_NeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborIfIndex: If op_NeighborIfIndex is specified, this value will be compared to the value in NeighborIfIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborIfIndex must be specified if op_NeighborIfIndex is specified.
             :type val_c_NeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborInterfaceID: The operator to apply to the field NeighborInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborInterfaceID: The internal NetMRI identifier for the destination interface in this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborInterfaceID: If op_NeighborInterfaceID is specified, the field named in this input will be compared to the value in NeighborInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborInterfaceID must be specified if op_NeighborInterfaceID is specified.
             :type val_f_NeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborInterfaceID: If op_NeighborInterfaceID is specified, this value will be compared to the value in NeighborInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborInterfaceID must be specified if op_NeighborInterfaceID is specified.
             :type val_c_NeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborNetworkDeviceInd: The operator to apply to the field NeighborNetworkDeviceInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborNetworkDeviceInd: A flag indicating if the destination device is a network device or an end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborNetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborNetworkDeviceInd: If op_NeighborNetworkDeviceInd is specified, the field named in this input will be compared to the value in NeighborNetworkDeviceInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborNetworkDeviceInd must be specified if op_NeighborNetworkDeviceInd is specified.
             :type val_f_NeighborNetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborNetworkDeviceInd: If op_NeighborNetworkDeviceInd is specified, this value will be compared to the value in NeighborNetworkDeviceInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborNetworkDeviceInd must be specified if op_NeighborNetworkDeviceInd is specified.
             :type val_c_NeighborNetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborStartTime: The operator to apply to the field NeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborStartTime: If op_NeighborStartTime is specified, the field named in this input will be compared to the value in NeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborStartTime must be specified if op_NeighborStartTime is specified.
             :type val_f_NeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborStartTime: If op_NeighborStartTime is specified, this value will be compared to the value in NeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborStartTime must be specified if op_NeighborStartTime is specified.
             :type val_c_NeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborTimestamp: The operator to apply to the field NeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborTimestamp: If op_NeighborTimestamp is specified, the field named in this input will be compared to the value in NeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborTimestamp must be specified if op_NeighborTimestamp is specified.
             :type val_f_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborTimestamp: If op_NeighborTimestamp is specified, this value will be compared to the value in NeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborTimestamp must be specified if op_NeighborTimestamp is specified.
             :type val_c_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NetworkDeviceInd: The operator to apply to the field NetworkDeviceInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NetworkDeviceInd: A flag indicating if the source device is a network device or an end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NetworkDeviceInd: If op_NetworkDeviceInd is specified, the field named in this input will be compared to the value in NetworkDeviceInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NetworkDeviceInd must be specified if op_NetworkDeviceInd is specified.
             :type val_f_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NetworkDeviceInd: If op_NetworkDeviceInd is specified, this value will be compared to the value in NetworkDeviceInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NetworkDeviceInd must be specified if op_NetworkDeviceInd is specified.
             :type val_c_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OSPFRoutedInd: The operator to apply to the field OSPFRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OSPFRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon an OSPF route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OSPFRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OSPFRoutedInd: If op_OSPFRoutedInd is specified, the field named in this input will be compared to the value in OSPFRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OSPFRoutedInd must be specified if op_OSPFRoutedInd is specified.
             :type val_f_OSPFRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OSPFRoutedInd: If op_OSPFRoutedInd is specified, this value will be compared to the value in OSPFRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OSPFRoutedInd must be specified if op_OSPFRoutedInd is specified.
             :type val_c_OSPFRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ProtoRoutedInd: The operator to apply to the field ProtoRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ProtoRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a dynamic protocol defined route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ProtoRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ProtoRoutedInd: If op_ProtoRoutedInd is specified, the field named in this input will be compared to the value in ProtoRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ProtoRoutedInd must be specified if op_ProtoRoutedInd is specified.
             :type val_f_ProtoRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ProtoRoutedInd: If op_ProtoRoutedInd is specified, this value will be compared to the value in ProtoRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ProtoRoutedInd must be specified if op_ProtoRoutedInd is specified.
             :type val_c_ProtoRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RevSwitchFwdInd: The operator to apply to the field RevSwitchFwdInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdInd: A flag indicating that this neighbor relationship was derived by reversing a switch forwarding neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdInd: If op_RevSwitchFwdInd is specified, the field named in this input will be compared to the value in RevSwitchFwdInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdInd must be specified if op_RevSwitchFwdInd is specified.
             :type val_f_RevSwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdInd: If op_RevSwitchFwdInd is specified, this value will be compared to the value in RevSwitchFwdInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdInd must be specified if op_RevSwitchFwdInd is specified.
             :type val_c_RevSwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialInd: The operator to apply to the field SerialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialInd: A flag indicating that this neighbor relationship was derived using the NetMRI point-to-point neighbor detection algorithm. Despite the name this may include point-to-point relationships on interfaces other than serial interfaces. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialInd: If op_SerialInd is specified, the field named in this input will be compared to the value in SerialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialInd must be specified if op_SerialInd is specified.
             :type val_f_SerialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialInd: If op_SerialInd is specified, this value will be compared to the value in SerialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialInd must be specified if op_SerialInd is specified.
             :type val_c_SerialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StaticRoutedInd: The operator to apply to the field StaticRoutedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StaticRoutedInd: A flag indicating that this neighbor relationship represents an IP routing relationship based upon a static route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StaticRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StaticRoutedInd: If op_StaticRoutedInd is specified, the field named in this input will be compared to the value in StaticRoutedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StaticRoutedInd must be specified if op_StaticRoutedInd is specified.
             :type val_f_StaticRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StaticRoutedInd: If op_StaticRoutedInd is specified, this value will be compared to the value in StaticRoutedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StaticRoutedInd must be specified if op_StaticRoutedInd is specified.
             :type val_c_StaticRoutedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdInd: The operator to apply to the field SwitchFwdInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdInd: A flag indicating that this neighbor relationship was derived using the NetMRI switch forwarding neighbor detection algorithm. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdInd: If op_SwitchFwdInd is specified, the field named in this input will be compared to the value in SwitchFwdInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdInd must be specified if op_SwitchFwdInd is specified.
             :type val_f_SwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdInd: If op_SwitchFwdInd is specified, this value will be compared to the value in SwitchFwdInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdInd must be specified if op_SwitchFwdInd is specified.
             :type val_c_SwitchFwdInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP interface index of the source device interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_network_id: The operator to apply to the field network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. network_id: The Network View ID assigned to this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_network_id: If op_network_id is specified, the field named in this input will be compared to the value in network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_network_id must be specified if op_network_id is specified.
             :type val_f_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_network_id: If op_network_id is specified, this value will be compared to the value in network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_network_id must be specified if op_network_id is specified.
             :type val_c_network_id: String

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

             :param timestamp: The data returned will represent the neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of neighbor methods. The listed methods will be called on each neighbor returned and included in the output. Available methods are: network_id, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, neighbor_device, neighbor_interface.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID.
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

             :param select: The list of attributes to return for each Neighbor. Valid values are DataSourceID, NeighborID, DeviceID, InterfaceID, ifIndex, NeighborDeviceID, NeighborInterfaceID, NeighborIfIndex, NeighborFirstSeenTime, NeighborStartTime, NeighborEndTime, NeighborChangedCols, NeighborTimestamp, CombinedInd, CDPInd, LLDPInd, SerialInd, SwitchFwdInd, RevSwitchFwdInd, DirectEthernetInd, IPRoutedInd, StaticRoutedInd, LocalRoutedInd, ProtoRoutedInd, BGPRoutedInd, OSPFRoutedInd, IGRPRoutedInd, NetworkDeviceInd, NeighborNetworkDeviceInd, CDPNeighborID, LLDPNeighborID. If empty or omitted, all attributes will be returned.
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

             :return neighbors: An array of the Neighbor objects that match the specified input criteria.
             :rtype neighbors: Array of Neighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def interface(self, **kwargs):
        """The source interface in this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The source interface in this neighbor relationship.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def neighbor_device(self, **kwargs):
        """The destination device in this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The destination device in this neighbor relationship.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("neighbor_device"), kwargs)

    def neighbor_interface(self, **kwargs):
        """The destination interface in this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The destination interface in this neighbor relationship.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("neighbor_interface"), kwargs)

    def infradevice(self, **kwargs):
        """The source device in this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The source device in this neighbor relationship.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def network_id(self, **kwargs):
        """The Network View ID assigned to this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Network View ID assigned to this neighbor relationship.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("network_id"), kwargs)

    def device(self, **kwargs):
        """The source device in this neighbor relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for this neighbor relationship.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The source device in this neighbor relationship.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
