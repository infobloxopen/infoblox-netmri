from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VlanMemberRemote(RemoteModel):
    """
    Device memberships in VLANs, along with their STP configurations.  This includes switch members (BridgeMemberInd = 1) and devices attached to access ports (BridgeMemberInd = 0).


    |  ``BaseBridgeAddress:`` The spanning tree protocol base bridge address of this bridge. Empty for non-bridge members.
    |  ``attribute type:`` string

    |  ``BaseNumPorts:`` The number of ports on this bridge. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``BridgeMemberInd:`` A flag indicating that this VLAN membership record represents a bridge device's configuration entry for the VLAN; that is, that this membership record is for a bridge participating in the VLAN, as opposed to a device attached to an access port.
    |  ``attribute type:`` bool

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device associated with this VLAN membership.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the switched virtual interface for this VLAN on this device.
    |  ``attribute type:`` number

    |  ``RootBridgeAddress:`` The spanning tree protocol root bridge address; this is the designated root with the STP priority portion removed. Empty for non-bridge members.
    |  ``attribute type:`` string

    |  ``StpBridgeForwardDelay:`` The value that all bridges use for ForwardDelay when this bridge is acting as the root. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpBridgeHelloTime:`` The value that all bridges use for HelloTime when this bridge is acting as the root. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpBridgeMaxAge:`` The value that all bridges use for MaxAge when this bridge is acting as the root. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpDesignatedRoot:`` The bridge identifier for this bridge. Empty for non-bridge members.
    |  ``attribute type:`` string

    |  ``StpForwardDelay:`` This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state. The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state. This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. This is the value currently in use on this bridge. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpHelloTime:`` The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second. This is the actual value that this bridge is currently using.
    |  ``attribute type:`` number

    |  ``StpHoldTime:`` This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second.
    |  ``attribute type:`` number

    |  ``StpMaxAge:`` The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second. This is the actual value that this bridge is currently using. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpPriority:`` The spanning tree protocol priority for this bridge in this VLAN. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpProtocolSpecification:`` The protocol of spanning tree running for this VLAN. Empty for non-bridge members.
    |  ``attribute type:`` string

    |  ``StpRootCost:`` The cost of the path to the root bridge as seen from this bridge. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``StpRootPort:`` The port number (i.e., the SwitchPortNumber attribute value of the interface) of the port that offers the lowest cost path from this bridge to the root bridge.
    |  ``attribute type:`` number

    |  ``StpTopChanges:`` The total number of topology changes detected by this bridge since the last reset. Empty for non-bridge members.
    |  ``attribute type:`` number

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN associated with this VLAN membership.
    |  ``attribute type:`` number

    |  ``VlanMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``VlanMemberEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``VlanMemberID:`` The internal NetMRI identifier for this VLAN membership.
    |  ``attribute type:`` number

    |  ``VlanMemberStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``VlanMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``VlanName:`` The name of this VLAN as configured on this device. Empty for non-bridge members.
    |  ``attribute type:`` string

    |  ``VlanState:`` The state of this VLAN on this device. Empty for non-bridge members.

The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.

The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports.
    |  ``attribute type:`` string

    |  ``VlanType:`` The type of this VLAN (1:ethernet, 2:fddi, 3:tokenRing, 4:fddiNet, 5:trNet, 6:deprecated) as configured on this device. Empty for non-bridge members.
    |  ``attribute type:`` string





    |  ``VTPDomain:`` Management domain name if VLAN is VTP managed.
    |  ``attribute type:`` string


    |  ``network_id:`` The Network View ID assigned to the Vlan membership.
    |  ``attribute type:`` number

    """

    properties = ("BaseBridgeAddress",
                  "BaseNumPorts",
                  "BridgeMemberInd",
                  "DataSourceID",
                  "DeviceID",
                  "InterfaceID",
                  "RootBridgeAddress",
                  "StpBridgeForwardDelay",
                  "StpBridgeHelloTime",
                  "StpBridgeMaxAge",
                  "StpDesignatedRoot",
                  "StpForwardDelay",
                  "StpHelloTime",
                  "StpHoldTime",
                  "StpMaxAge",
                  "StpPriority",
                  "StpProtocolSpecification",
                  "StpRootCost",
                  "StpRootPort",
                  "StpTopChanges",
                  "VlanID",
                  "VlanMemberChangedCols",
                  "VlanMemberEndTime",
                  "VlanMemberID",
                  "VlanMemberStartTime",
                  "VlanMemberTimestamp",
                  "VlanName",
                  "VlanState",
                  "VlanType",
                  "VTPDomain",
                  "network_id",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"VlanMemberID": self.VlanMemberID})

    @property
    @check_api_availability
    def device(self):
        """
        The device associated with this VLAN membership.
        ``attribute type:`` model
        """
        return self.broker.device(**{"VlanMemberID": self.VlanMemberID})

    @property
    @check_api_availability
    def interface(self):
        """
        The switched virtual interface for this VLAN on this device.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"VlanMemberID": self.VlanMemberID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The VLAN associated with this VLAN membership.
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"VlanMemberID": self.VlanMemberID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device associated with this VLAN membership.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"VlanMemberID": self.VlanMemberID})
