from ..remote import RemoteModel


class DeviceByVlannameOrVlanindexGridRemote(RemoteModel):
    """
    This table lists devices that a VlanName or VlanIndex exists on.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The NetMRI internal identifier for the device associated with this interface.
    |  ``attribute type:`` number

    |  ``DeviceIPDotted:`` The management IP address of the device associated with this interface, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the device associated with this interface; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type for the device associated with this interface.
    |  ``attribute type:`` string

    |  ``VlanName:`` The name of the VLAN on the root bridge.
    |  ``attribute type:`` string

    |  ``VlanIndex:`` The numerical VLAN number (VLAN ID).
    |  ``attribute type:`` number

    |  ``Network:`` A Network View assigned to the device.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` Internal identifier for the network view.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceIPDotted",
                  "DeviceName",
                  "DeviceType",
                  "VlanName",
                  "VlanIndex",
                  "Network",
                  "VirtualNetworkID",
                  )
