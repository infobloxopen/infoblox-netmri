from ..remote import RemoteModel


class SpmHistoryInterfaceHistoryGridRemote(RemoteModel):
    """
    This table lists the SPM interface history within the user specified period of time for a given interface.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this interface.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this interface.
    |  ``attribute type:`` datetime

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

    |  ``ifName:`` The name of this interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` string

    |  ``ifDescr:`` The description of the interface, as set in the device's configuration file.
    |  ``attribute type:`` string

    |  ``ifAlias:`` Interface alias of this interface.
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

    |  ``Errors:`` Total inbound and outbound errors on this interface.
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal identifier for the network which the interface is associated to.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "FirstSeen",
                  "LastSeen",
                  "DeviceID",
                  "DeviceType",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "InterfaceID",
                  "ifName",
                  "ifIndex",
                  "ifDescr",
                  "ifAlias",
                  "ifMAC",
                  "ifOperStatus",
                  "ifAdminStatus",
                  "ifSpeed",
                  "ifDuplex",
                  "ifAdminDuplex",
                  "Errors",
                  "VirtualNetworkID",
                  "Network",
                  )
