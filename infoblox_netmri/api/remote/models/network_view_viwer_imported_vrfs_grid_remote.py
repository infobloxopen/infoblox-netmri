from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NetworkViewViwerImportedVrfsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``RouteTarget:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "RouteTarget",
                  "DeviceName",
                  "VirtualNetworkMemberName",
                  "RouteDistinguisher",
                  )
