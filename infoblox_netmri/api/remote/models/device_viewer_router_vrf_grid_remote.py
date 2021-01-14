from ..remote import RemoteModel


class DeviceViewerRouterVrfGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberID:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberDescription:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``RouteLimit:`` none
    |  ``attribute type:`` string

    |  ``WarningLimit:`` none
    |  ``attribute type:`` string

    |  ``CurrentCount:`` none
    |  ``attribute type:`` string

    |  ``Timestamp:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VirtualNetworkMemberID",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkMemberDescription",
                  "VirtualNetworkID",
                  "Network",
                  "RouteDistinguisher",
                  "DeviceID",
                  "RouteLimit",
                  "WarningLimit",
                  "CurrentCount",
                  "Timestamp",
                  )
