from ..remote import RemoteModel


class NetworkNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Count:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VirtualNetworkID",
                  "Network",
                  "Count",
                  )
