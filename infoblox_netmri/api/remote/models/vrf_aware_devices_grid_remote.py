from ..remote import RemoteModel


class VrfAwareDevicesGridRemote(RemoteModel):
    """
    list of VRF aware devices


    |  ``id:`` The internal system identifier for the worksheet.
    |  ``attribute type:`` number

    |  ``DeviceID:`` DeviceID.
    |  ``attribute type:`` number

    |  ``DeviceName:`` Device Name.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` Device Ip Address.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` Device Ip Numeric Address.
    |  ``attribute type:`` string

    |  ``DeviceNetwork:`` Indicates the network view which the device is associated to.
    |  ``attribute type:`` string

    |  ``DeviceVirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` string

    |  ``ifIndex:`` Interface ID.
    |  ``attribute type:`` string

    |  ``ifName:`` Interface Name.
    |  ``attribute type:`` string

    |  ``ifNameSort:`` Interface Name Sort.
    |  ``attribute type:`` string

    |  ``ifIPDotted:`` Interface IP.
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` Interface IP Numeric.
    |  ``attribute type:`` string

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` Name of the Local VRF instance.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal identifier for the network.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberDescription:`` The description of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` Route Distinguisher.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceNetwork",
                  "DeviceVirtualNetworkID",
                  "ifIndex",
                  "ifName",
                  "ifNameSort",
                  "ifIPDotted",
                  "ifIPNumeric",
                  "Network",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkID",
                  "VirtualNetworkMemberDescription",
                  "RouteDistinguisher",
                  )
