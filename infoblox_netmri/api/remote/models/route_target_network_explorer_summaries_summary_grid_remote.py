from ..remote import RemoteModel


class RouteTargetNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``VrfDirection:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VrfNetworkViewID:`` none
    |  ``attribute type:`` string

    |  ``VrfNetworkView:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    |  ``VrfRouteTargetName:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "VrfDirection",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "VirtualNetworkMemberName",
                  "VrfNetworkViewID",
                  "VrfNetworkView",
                  "RouteDistinguisher",
                  "VrfRouteTargetName",
                  )
