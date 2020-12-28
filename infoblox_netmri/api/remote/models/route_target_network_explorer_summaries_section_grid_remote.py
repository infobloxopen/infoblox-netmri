from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


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
