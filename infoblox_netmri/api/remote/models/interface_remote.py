from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class InterfaceRemote(RemoteModel):
    """
    Interfaces on devices discovered by NetMRI.


    |  ``AggrInterfaceID:`` The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device containing this interface.
    |  ``attribute type:`` number

    |  ``ifAdminStatus:`` The configured status (up/down) of the interface.
    |  ``attribute type:`` string

    |  ``ifAggrMemberInd:`` A flag indicating whether or not this is a member interface in a link aggregation.
    |  ``attribute type:`` bool

    |  ``ifArtificialInd:`` Not currently used.
    |  ``attribute type:`` bool

    |  ``ifChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifConnector:`` If "true" or "1", then this interface has a physical connector.
    |  ``attribute type:`` string

    |  ``ifDescr:`` The description of the interface, as set in the device's configuration file.
    |  ``attribute type:`` string

    |  ``ifDuplex:`` The operational duplex of this interface.
    |  ``attribute type:`` string

    |  ``ifEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifIndex:`` The SNMP index value of the interface.
    |  ``attribute type:`` number

    |  ``ifLastChange:`` The date/time of the last status change for this interface.
    |  ``attribute type:`` datetime

    |  ``ifLinkAggrInd:`` A flag indicating whether or not this is a link aggregation (port channel, etherchannel, LACP, etc.) interface.
    |  ``attribute type:`` bool

    |  ``ifLinkAggrIndex:`` The port group or port channel number for link aggregations interface or their member interfaces.
    |  ``attribute type:`` number

    |  ``ifLinkTrap:`` If "enabled", this device is configured to send link up/down traps.
    |  ``attribute type:`` string

    |  ``ifLowerLayer:`` The SNMP interface index of the lower-layer interface on which this interface is constructed.
    |  ``attribute type:`` number

    |  ``ifMAC:`` The interface Media Access Controller (MAC) address.
    |  ``attribute type:`` string

    |  ``ifMtu:`` The size of the largest packet or datagram which can be sent/received on the interface, specified in octets.
    |  ``attribute type:`` number

    |  ``ifName:`` The name of this interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``ifOperStatus:`` The operational status (up/down) of the interface.
    |  ``attribute type:`` string

    |  ``ifPortFast:`` If "enabled" then port fast is active on the interface.
    |  ``attribute type:`` string

    |  ``ifSpeed:`` The operational speed, in bps, of this interface.
    |  ``attribute type:`` number

    |  ``ifStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``ifTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``ifTrunkStatus:`` If "on", then this interface is a VLAN trunk port.
    |  ``attribute type:`` string

    |  ``ifTunnelInd:`` A flag indicating whether or not this is a tunnel interface.
    |  ``attribute type:`` bool

    |  ``ifType:`` The interface type.
    |  ``attribute type:`` string

    |  ``ifVirtualInd:`` A flag indicating whether or not this is a virtual interface.
    |  ``attribute type:`` bool

    |  ``InterfaceID:`` The internal NetMRI identifier for this interface.
    |  ``attribute type:`` number

    |  ``SwitchPortNumber:`` The switch port number from the dot1d bridge MIB for this interface.
    |  ``attribute type:`` number




    |  ``ifAlias:`` Interface alias.
    |  ``attribute type:`` string

    |  ``ifDescrRaw:`` The raw description of the interface before any NetMRI processing.
    |  ``attribute type:`` string

    |  ``ifAdminDuplex:`` Admin setting of duplex, Auto indicates the device will try to negotiate with the other end to determine.
    |  ``attribute type:`` string

    |  ``Slot:`` The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
    |  ``attribute type:`` string

    |  ``Port:`` The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
    |  ``attribute type:`` string

    |  ``PoEPower:`` Power draw of the supplied device in millivolts.
    |  ``attribute type:`` string

    |  ``PoEStatus:`` Status of the PoE connection.
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` A flag indicating whether or not this interface is available for port control actions.
    |  ``attribute type:`` bool

    |  ``ifSwitchPortMgmtInd:`` A flag indicating whether or not this interface is available in switch port management views.
    |  ``attribute type:`` bool

    |  ``ifFirstSeenTime:`` The date and time this interface was first seen on the network, and since which it has been continuously present.
    |  ``attribute type:`` datetime



    |  ``ifphysaddress:`` The interface Media Access Controller (MAC) address.
    |  ``attribute type:`` string

    |  ``ifOperStatusChange:`` The date/time of the last operational status change (e.g. free or used) for this interface.
    |  ``attribute type:`` datetime

    |  ``ifNameSort:`` The internal NetMRI name of this interface for sorting purpose.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberID:`` The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined.
    |  ``attribute type:`` number

    |  ``ifEncapsulationType:`` Indicates the encapsulation Type for this interface.
    |  ``attribute type:`` string

    |  ``ifEncapsulationTag:`` Indicates the encapsulation Tag for this interface.
    |  ``attribute type:`` string

    |  ``network_name:`` A Network View assigned to the device.
    |  ``attribute type:`` string

    |  ``ifLowerLayerInterfaceID:`` The internal NetMRI identifier for the lower-layer interface on which this interface is constructed.
    |  ``attribute type:`` number

    |  ``DownstreamSwitchCount:`` The number of downstream switches for this interface (only available for switch ports).
    |  ``attribute type:`` number

    |  ``network_id:`` The Network View ID assigned to the interface.
    |  ``attribute type:`` number

    |  ``vrf_name:`` The VRF name assigned to the interface.
    |  ``attribute type:`` string

    |  ``vrf_description:`` The VRF description of the vrf assigned to the interface.
    |  ``attribute type:`` string

    |  ``vrf_rd:`` The VRF route distinguisher of the vrf  assigned to the interface.
    |  ``attribute type:`` string

    |  ``cap_if_description_ind:`` Capability of changing the description of this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_admin_status_ind:`` Capability of changing the Admin Status of this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_vlan_assignment_ind:`` Capability of assigning a regular data VLAN to this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_voice_vlan_ind:`` Capability of assigning a voice VLAN to this interface.
    |  ``attribute type:`` bool

    |  ``control_capabilities:`` Configuration capabilities for this interface, related to Port Control.
    |  ``attribute type:`` string

    |  ``cap_itf_net_deprovisioning_ind:`` Capability of de-provisioning a network from this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_description_na_reason:`` Reason of non ability of changing the description of this interface.
    |  ``attribute type:`` string

    |  ``cap_if_admin_status_na_reason:`` Reason of non ability of changing the Admin Status of this interface.
    |  ``attribute type:`` string

    |  ``cap_if_vlan_assignment_na_reason:`` Reason of non ability of assigning a regular data VLAN to this interface.
    |  ``attribute type:`` string

    |  ``cap_if_voice_vlan_na_reason:`` Reason of non ability of assigning a voice VLAN to this interface.
    |  ``attribute type:`` string

    |  ``cap_if_net_provisioning_ipv4_ind:`` Capability to provision an ipv4 network on this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_provisioning_ipv4_na_reason:`` Reason of non ability to provision an ipv4 network on this interface.
    |  ``attribute type:`` string

    |  ``cap_if_net_provisioning_ipv6_ind:`` Capability to provision an ipv6 network on this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_provisioning_ipv6_na_reason:`` Reason of non ability to provision an ipv6 network on this interface.i
    |  ``attribute type:`` string

    |  ``cap_if_net_deprovisioning_ipv4_ind:`` Capability of de-provisioning an ipv4 network from this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_deprovisioning_ipv4_na_reason:`` Reason of non ability of de-provisioning an ipv4 network from this interface.
    |  ``attribute type:`` string

    |  ``cap_if_net_deprovisioning_ipv6_ind:`` Capability of de-provisioning an ipv6 network from this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_deprovisioning_ipv6_na_reason:`` Reason of non ability of de-provisioning an ipv6 network from this interface.
    |  ``attribute type:`` string

    |  ``cap_itf_net_deprovisioning_na_reason:`` The reason a network from this interface was unable to be deprovisioned.
    |  ``attribute type:`` string

    |  ``aggr_interface_name:`` The name of aggregated interface.
    |  ``attribute type:`` string

    |  ``vpc_peer_ifname:`` The name of peer interface of VPC pair.
    |  ``attribute type:`` string

    |  ``vpc_peer_device_id:`` DeviceID of VPC peer device.
    |  ``attribute type:`` number


    """

    properties = ("AggrInterfaceID",
                  "DataSourceID",
                  "DeviceID",
                  "ifAdminStatus",
                  "ifAggrMemberInd",
                  "ifArtificialInd",
                  "ifChangedCols",
                  "ifConnector",
                  "ifDescr",
                  "ifDuplex",
                  "ifEndTime",
                  "ifIndex",
                  "ifLastChange",
                  "ifLinkAggrInd",
                  "ifLinkAggrIndex",
                  "ifLinkTrap",
                  "ifLowerLayer",
                  "ifMAC",
                  "ifMtu",
                  "ifName",
                  "ifOperStatus",
                  "ifPortFast",
                  "ifSpeed",
                  "ifStartTime",
                  "ifTimestamp",
                  "ifTrunkStatus",
                  "ifTunnelInd",
                  "ifType",
                  "ifVirtualInd",
                  "InterfaceID",
                  "SwitchPortNumber",
                  "ifAlias",
                  "ifDescrRaw",
                  "ifAdminDuplex",
                  "Slot",
                  "Port",
                  "PoEPower",
                  "PoEStatus",
                  "ifPortControlInd",
                  "ifSwitchPortMgmtInd",
                  "ifFirstSeenTime",
                  "ifphysaddress",
                  "ifOperStatusChange",
                  "ifNameSort",
                  "VirtualNetworkMemberID",
                  "ifEncapsulationType",
                  "ifEncapsulationTag",
                  "network_name",
                  "ifLowerLayerInterfaceID",
                  "DownstreamSwitchCount",
                  "network_id",
                  "vrf_name",
                  "vrf_description",
                  "vrf_rd",
                  "cap_if_description_ind",
                  "cap_if_admin_status_ind",
                  "cap_if_vlan_assignment_ind",
                  "cap_if_voice_vlan_ind",
                  "control_capabilities",
                  "cap_itf_net_deprovisioning_ind",
                  "cap_if_description_na_reason",
                  "cap_if_admin_status_na_reason",
                  "cap_if_vlan_assignment_na_reason",
                  "cap_if_voice_vlan_na_reason",
                  "cap_if_net_provisioning_ipv4_ind",
                  "cap_if_net_provisioning_ipv4_na_reason",
                  "cap_if_net_provisioning_ipv6_ind",
                  "cap_if_net_provisioning_ipv6_na_reason",
                  "cap_if_net_deprovisioning_ipv4_ind",
                  "cap_if_net_deprovisioning_ipv4_na_reason",
                  "cap_if_net_deprovisioning_ipv6_ind",
                  "cap_if_net_deprovisioning_ipv6_na_reason",
                  "cap_itf_net_deprovisioning_na_reason",
                  "aggr_interface_name",
                  "vpc_peer_ifname",
                  "vpc_peer_device_id",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device containing this interface.
        ``attribute type:`` model
        """
        return self.broker.device(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def aggr_interface(self):
        """
        The 'owning' link aggregation interface for link aggregate members (refers back to self for link aggregates).
        ``attribute type:`` model
        """
        return self.broker.aggr_interface(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device containing this interface.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The first virtual LAN attached to that interface
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"InterfaceID": self.InterfaceID})
