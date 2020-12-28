from ..remote import RemoteModel


class DeviceViewerDeviceLocationNetworksGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``VRFNetworkName:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "ifNameSort",
                  "ifIndex",
                  "ifIPDotted",
                  "ifIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "VRFNetworkName",
                  )
