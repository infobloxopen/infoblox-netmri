from ..remote import RemoteModel


class RouteTargetNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VrfRouteTargetID:`` none
    |  ``attribute type:`` string

    |  ``VrfRouteTargetName:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VrfRouteTargetID",
                  "VrfRouteTargetName",
                  )
