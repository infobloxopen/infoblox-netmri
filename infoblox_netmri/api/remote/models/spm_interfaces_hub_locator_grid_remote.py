from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SpmInterfacesHubLocatorGridRemote(RemoteModel):
    """
    This table lists all SPM interfaces on which multiple end hosts were connected within the user specified period of time.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The NetMRI internal identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface configured with this address.
    |  ``attribute type:`` number

    |  ``Interface:`` The name of this interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` string

    |  ``ifDescr:`` The description of the interface, as set in the device's configuration file.
    |  ``attribute type:`` string

    |  ``ifAlias:`` Interface alias of this interface.
    |  ``attribute type:`` string

    |  ``ifType:`` The interface type of this interface.
    |  ``attribute type:`` string

    |  ``ifMAC:`` The interface Media Access Controller (MAC) address of this interface.
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

    |  ``PoEPower:`` Power draw of the supplied device in millivolts.
    |  ``attribute type:`` number

    |  ``PoEStatus:`` Status of the PoE connection.
    |  ``attribute type:`` string

    |  ``VlanIndex:`` The numerical VLAN number (VLAN ID).
    |  ``attribute type:`` number

    |  ``VlanName:`` The name of the VLAN on the root bridge.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``VTPDomain:`` Management domain name if VLAN is VTP managed.
    |  ``attribute type:`` string

    |  ``EndHostCount:`` The number of end devices connected to this interface.
    |  ``attribute type:`` number

    |  ``PortStatus:`` Port Status. Valid values are "Used", "Free", or "Avail".
    |  ``attribute type:`` string

    |  ``Packets:`` Total inbound and outbound packets on this interface.
    |  ``attribute type:`` number

    |  ``Errors:`` Total inbound and outbound errors on this interface.
    |  ``attribute type:`` number

    |  ``ErrorPercentage:`` Percentage of errors on this interface.
    |  ``attribute type:`` number

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this interface.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this interface.
    |  ``attribute type:`` datetime

    |  ``ifPortControlInd:`` A flag indicating whether or not this interface is available for port control actions.
    |  ``attribute type:`` bool

    |  ``ifSwitchPortMgmtInd:`` A flag indicating whether or not this interface is available in switch port management views.
    |  ``attribute type:`` bool

    |  ``ifName:`` The name of the switch interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``ifIPDotted:`` The IP address in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` The numerical value of the IP address.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberName:`` The name of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``ifTrunkStatus:`` Trunk Status
    |  ``attribute type:`` string


    """

    properties = ("id",
                  "Network",
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
                  "ifType",
                  "ifMAC",
                  "ifOperStatus",
                  "ifAdminStatus",
                  "ifSpeed",
                  "ifDuplex",
                  "ifAdminDuplex",
                  "PoEPower",
                  "PoEStatus",
                  "VlanIndex",
                  "VlanName",
                  "VlanID",
                  "VTPDomain",
                  "EndHostCount",
                  "PortStatus",
                  "Packets",
                  "Errors",
                  "ErrorPercentage",
                  "FirstSeen",
                  "LastSeen",
                  "ifPortControlInd",
                  "ifSwitchPortMgmtInd",
                  "ifName",
                  "VirtualNetworkID",
                  "ifIPDotted",
                  "ifIPNumeric",
                  "VirtualNetworkMemberName",
                  "ifTrunkStatus",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"id": self.id})
