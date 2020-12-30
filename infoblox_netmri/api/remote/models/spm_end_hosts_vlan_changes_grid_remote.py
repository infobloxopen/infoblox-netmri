from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SpmEndHostsVlanChangesGridRemote(RemoteModel):
    """
    This table lists end hosts that have moved to a different VLAN within the user specified period of time.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``NeighborDeviceID:`` The internal NetMRI identifier for the end host in this neighbor relationship.
    |  ``attribute type:`` number

    |  ``NeighborType:`` The NetMRI-determined device type for this end host.
    |  ``attribute type:`` string

    |  ``NeighborIPDotted:`` The management IP address of this end host, in dotted, or colon-delimited for IPv6, format.
    |  ``attribute type:`` string

    |  ``NeighborIPNumeric:`` The numerical value of the end host IP address.
    |  ``attribute type:`` number

    |  ``NeighborName:`` The NetMRI name of the end host; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``NeighborMAC:`` The Media Access Controller (MAC) address of the end host.
    |  ``attribute type:`` string

    |  ``NeighborIfIndex:`` The SNMP interface index of the end host interface.
    |  ``attribute type:`` string

    |  ``OrgUniqueId:`` Organizational unique identifier of the end host.
    |  ``attribute type:`` string

    |  ``NetBIOSName:`` The NetBIOS name of the end host.
    |  ``attribute type:`` string

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this end host.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this end host.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The NetMRI internal identifier for the switch.
    |  ``attribute type:`` number

    |  ``DeviceType:`` The NetMRI-determined device type of the switch.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the switch; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the switch IP address.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface on the switch configured with this address.
    |  ``attribute type:`` number

    |  ``Interface:`` The interface on the switch configured with this address.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface on the switch configured with this address.
    |  ``attribute type:`` string

    |  ``ifDescr:`` The description of the interface, as set in the switch's configuration file.
    |  ``attribute type:`` string

    |  ``ifAlias:`` Interface alias for this interface.
    |  ``attribute type:`` string

    |  ``ifMAC:`` The interface Media Access Controller (MAC) address for this interface.
    |  ``attribute type:`` string

    |  ``ifOperStatus:`` The operational status (up/down) of this interface.
    |  ``attribute type:`` string

    |  ``ifAdminStatus:`` The configured status (up/down) of this interface.
    |  ``attribute type:`` string

    |  ``ifSpeed:`` The operational speed, in bps, of this interface.
    |  ``attribute type:`` number

    |  ``ifDuplex:`` The operational duplex of this interface.
    |  ``attribute type:`` string

    |  ``ifAdminDuplex:`` Admin setting of duplex, Auto indicates the device will try to negotiate with the other end to determine.
    |  ``attribute type:`` string

    |  ``VlanIndex:`` The numerical VLAN number (VLAN ID).
    |  ``attribute type:`` number

    |  ``VlanName:`` The name of the VLAN on the root bridge.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``VTPDomain:`` Management domain name if VLAN is VTP managed.
    |  ``attribute type:`` string

    |  ``Packets:`` Total inbound and outbound packets on this interface.
    |  ``attribute type:`` number

    |  ``Errors:`` Total inbound and outbound errors on this interface.
    |  ``attribute type:`` number

    |  ``ErrorPercentage:`` Percentage of errors on this interface.
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberName:`` The name of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``TenantDn:`` DN of the tenant that owns the EPG the end host is assigned to
    |  ``attribute type:`` string

    |  ``BridgeDomainDn:`` DN of bridge domain the end host is connected to
    |  ``attribute type:`` string

    |  ``EPGDn:`` DN of a EPG the end host is assigned to
    |  ``attribute type:`` string

    |  ``ApName:`` Name of the access point
    |  ``attribute type:`` string

    |  ``ApIpAddress:`` IP address of the access point
    |  ``attribute type:`` string

    |  ``ApSsid:`` SSID of the access point
    |  ``attribute type:`` string



    """

    properties = ("id",
                  "Network",
                  "NeighborDeviceID",
                  "NeighborType",
                  "NeighborIPDotted",
                  "NeighborIPNumeric",
                  "NeighborName",
                  "NeighborMAC",
                  "NeighborIfIndex",
                  "OrgUniqueId",
                  "NetBIOSName",
                  "FirstSeen",
                  "LastSeen",
                  "DeviceID",
                  "DeviceType",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "InterfaceID",
                  "Interface",
                  "ifIndex",
                  "ifDescr",
                  "ifAlias",
                  "ifMAC",
                  "ifOperStatus",
                  "ifAdminStatus",
                  "ifSpeed",
                  "ifDuplex",
                  "ifAdminDuplex",
                  "VlanIndex",
                  "VlanName",
                  "VlanID",
                  "VTPDomain",
                  "Packets",
                  "Errors",
                  "ErrorPercentage",
                  "VirtualNetworkID",
                  "VirtualNetworkMemberName",
                  "TenantDn",
                  "BridgeDomainDn",
                  "EPGDn",
                  "ApName",
                  "ApIpAddress",
                  "ApSsid",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"id": self.id})
