from ..remote import RemoteModel


class SpmHistoryEndHostHistoryGridRemote(RemoteModel):
    """
    This table lists the end host history within the user specified period of time for a given end host.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this end host.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this end host.
    |  ``attribute type:`` datetime

    |  ``HostIPNumeric:`` The numerical value of the end host IP address.
    |  ``attribute type:`` number

    |  ``HostIPAddress:`` The management IP address of the end host, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``HostName:`` The NetMRI name of the end host; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The NetMRI internal identifier for the switch.
    |  ``attribute type:`` number

    |  ``DeviceType:`` The NetMRI-determined device type of the switch.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the switch; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface on the switch configured with this address.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP interface index of the interface on the switch configured with this address.
    |  ``attribute type:`` string

    |  ``Interface:`` The interface on the switch configured with this address.
    |  ``attribute type:`` string

    |  ``ifMAC:`` The interface Media Access Controller (MAC) address of this interface.
    |  ``attribute type:`` string

    |  ``ifOperStatus:`` The operational status (up/down) of this interface.
    |  ``attribute type:`` string

    |  ``VlanIndex:`` The numerical VLAN number (VLAN ID).
    |  ``attribute type:`` number

    |  ``VlanName:`` The name of the VLAN on the root bridge.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``VTPDomain:`` Management domain name if VLAN is VTP managed.
    |  ``attribute type:`` string

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` Internal identifier for the network view.
    |  ``attribute type:`` number

    |  ``HostMAC:`` The MAC Address of the end host.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "FirstSeen",
                  "LastSeen",
                  "HostIPNumeric",
                  "HostIPAddress",
                  "HostName",
                  "DeviceID",
                  "DeviceType",
                  "DeviceName",
                  "InterfaceID",
                  "ifIndex",
                  "Interface",
                  "ifMAC",
                  "ifOperStatus",
                  "VlanIndex",
                  "VlanName",
                  "VlanID",
                  "VTPDomain",
                  "Network",
                  "VirtualNetworkID",
                  "HostMAC",
                  )
