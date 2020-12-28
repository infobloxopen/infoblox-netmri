from ..remote import RemoteModel


class DeviceViewerRouterOspfNeighborGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceName:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceType:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``OspfPeerRouterIdentDotted:`` none
    |  ``attribute type:`` string

    |  ``OspfPeerRouterIdentNumeric:`` none
    |  ``attribute type:`` string

    |  ``RPPeerState:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "RPPeerDeviceName",
                  "RPPeerDeviceID",
                  "RPPeerDeviceType",
                  "RPPeerIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "RPPeerIPNumeric",
                  "OspfPeerRouterIdentDotted",
                  "OspfPeerRouterIdentNumeric",
                  "RPPeerState",
                  )
