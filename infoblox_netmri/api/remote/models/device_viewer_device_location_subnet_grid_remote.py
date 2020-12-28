from ..remote import RemoteModel


class DeviceViewerDeviceLocationSubnetGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``IPDotted:`` none
    |  ``attribute type:`` string

    |  ``IPNumeric:`` none
    |  ``attribute type:`` string

    |  ``subnet:`` none
    |  ``attribute type:`` string

    |  ``subnetlocation:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkID",
                  "Network",
                  "ifNameSort",
                  "ifIndex",
                  "IPDotted",
                  "IPNumeric",
                  "subnet",
                  "subnetlocation",
                  )
