from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SettingsNetworksGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkDescription:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberIDs:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VirtualNetworkID",
                  "VirtualNetworkName",
                  "VirtualNetworkDescription",
                  "VirtualNetworkMemberIDs",
                  )
