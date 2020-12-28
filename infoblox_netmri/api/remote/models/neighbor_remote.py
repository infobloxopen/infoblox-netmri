from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NeighborRemote(RemoteModel):
    """
     Summary of each neighbor relationship for a device.  This includes both L2 and L3 neighbor relationships.


    |  ``BGPRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon a BGP route.
    |  ``attribute type:`` bool

    |  ``CDPInd:`` A flag indicating that this neighbor relationship was derived based upon the source device's CDP entries.
    |  ``attribute type:`` bool

    |  ``CombinedInd:`` A flag indicating that these devices have basic layer 1/2 connectivity.
    |  ``attribute type:`` bool

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the source device in this neighbor relationship.
    |  ``attribute type:`` number

    |  ``DirectEthernetInd:`` A flag indicating that this neighbor relationship was derived using the NetMRI direct Ethernet neighbor detection algorithm (for example, two routers directly connected via Ethernet, without any switches between them).
    |  ``attribute type:`` bool

    |  ``ifIndex:`` The SNMP interface index of the source device interface.
    |  ``attribute type:`` number

    |  ``IGRPRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon an IGRP or EIGRP route.
    |  ``attribute type:`` bool

    |  ``InterfaceID:`` The internal NetMRI identifier for the source interface in this neighbor relationship.
    |  ``attribute type:`` number

    |  ``IPRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship; that is, the destination device is a next hop for at least one route on the source device.
    |  ``attribute type:`` bool

    |  ``LLDPInd:`` A flag indicating that this neighbor relationship was derived based upon the source device's LLDP entries.
    |  ``attribute type:`` bool

    |  ``LocalRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon a local route.
    |  ``attribute type:`` bool

    |  ``NeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``NeighborDeviceID:`` The internal NetMRI identifier for the destination device in this neighbor relationship.
    |  ``attribute type:`` number

    |  ``NeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``NeighborID:`` The internal NetMRI identifier for this neighbor relationship.
    |  ``attribute type:`` number

    |  ``NeighborIfIndex:`` The SNMP interface index of the destination device interface.
    |  ``attribute type:`` number

    |  ``NeighborInterfaceID:`` The internal NetMRI identifier for the destination interface in this neighbor relationship.
    |  ``attribute type:`` number

    |  ``NeighborNetworkDeviceInd:`` A flag indicating if the destination device is a network device or an end host.
    |  ``attribute type:`` bool

    |  ``NeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``NeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``NetworkDeviceInd:`` A flag indicating if the source device is a network device or an end host.
    |  ``attribute type:`` bool

    |  ``OSPFRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon an OSPF route.
    |  ``attribute type:`` bool

    |  ``ProtoRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon a dynamic protocol defined route.
    |  ``attribute type:`` bool

    |  ``RevSwitchFwdInd:`` A flag indicating that this neighbor relationship was derived by reversing a switch forwarding neighbor relationship.
    |  ``attribute type:`` bool

    |  ``SerialInd:`` A flag indicating that this neighbor relationship was derived using the NetMRI point-to-point neighbor detection algorithm. Despite the name this may include point-to-point relationships on interfaces other than serial interfaces.
    |  ``attribute type:`` bool

    |  ``StaticRoutedInd:`` A flag indicating that this neighbor relationship represents an IP routing relationship based upon a static route.
    |  ``attribute type:`` bool

    |  ``SwitchFwdInd:`` A flag indicating that this neighbor relationship was derived using the NetMRI switch forwarding neighbor detection algorithm.
    |  ``attribute type:`` bool

    |  ``CDPNeighborID:`` The internal NetMRI identifier for the CdpNeighbor object associated with this neighbor entry (if any).
    |  ``attribute type:`` number





    |  ``LLDPNeighborID:`` The internal NetMRI identifier for this LLDP table entry.
    |  ``attribute type:`` number

    |  ``NeighborFirstSeenTime:`` The date and time this neighbor was first seen on the network, and since which it has been continuously present.
    |  ``attribute type:`` datetime


    |  ``network_id:`` The Network View ID assigned to this neighbor relationship.
    |  ``attribute type:`` number

    """

    properties = ("BGPRoutedInd",
                  "CDPInd",
                  "CombinedInd",
                  "DataSourceID",
                  "DeviceID",
                  "DirectEthernetInd",
                  "ifIndex",
                  "IGRPRoutedInd",
                  "InterfaceID",
                  "IPRoutedInd",
                  "LLDPInd",
                  "LocalRoutedInd",
                  "NeighborChangedCols",
                  "NeighborDeviceID",
                  "NeighborEndTime",
                  "NeighborID",
                  "NeighborIfIndex",
                  "NeighborInterfaceID",
                  "NeighborNetworkDeviceInd",
                  "NeighborStartTime",
                  "NeighborTimestamp",
                  "NetworkDeviceInd",
                  "OSPFRoutedInd",
                  "ProtoRoutedInd",
                  "RevSwitchFwdInd",
                  "SerialInd",
                  "StaticRoutedInd",
                  "SwitchFwdInd",
                  "CDPNeighborID",
                  "LLDPNeighborID",
                  "NeighborFirstSeenTime",
                  "network_id",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The source device in this neighbor relationship.
        ``attribute type:`` model
        """
        return self.broker.device(**{"NeighborID": self.NeighborID})

    @property
    @check_api_availability
    def interface(self):
        """
        The source interface in this neighbor relationship.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"NeighborID": self.NeighborID})

    @property
    @check_api_availability
    def neighbor_device(self):
        """
        The destination device in this neighbor relationship.
        ``attribute type:`` model
        """
        return self.broker.neighbor_device(**{"NeighborID": self.NeighborID})

    @property
    @check_api_availability
    def neighbor_interface(self):
        """
        The destination interface in this neighbor relationship.
        ``attribute type:`` model
        """
        return self.broker.neighbor_interface(**{"NeighborID": self.NeighborID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The source device in this neighbor relationship.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"NeighborID": self.NeighborID})
