from ..remote import RemoteModel


class DeviceViewerRouterBgpGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``BGPLocalIPDotted:`` none
    |  ``attribute type:`` string

    |  ``BGPLocalIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``BGPLocalPort:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``BGPPeerPort:`` none
    |  ``attribute type:`` string

    |  ``RoutingAreaNumber:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceName:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceType:`` none
    |  ``attribute type:`` string

    |  ``RPPeerState:`` none
    |  ``attribute type:`` string

    |  ``RPPeerUpSince:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "BGPLocalIPDotted",
                  "BGPLocalIPNumeric",
                  "BGPLocalPort",
                  "VirtualNetworkID",
                  "Network",
                  "RPPeerIPDotted",
                  "RPPeerIPNumeric",
                  "BGPPeerPort",
                  "RoutingAreaNumber",
                  "RPPeerDeviceName",
                  "RPPeerDeviceID",
                  "RPPeerDeviceType",
                  "RPPeerState",
                  "RPPeerUpSince",
                  )
