from ..remote import RemoteModel


class SubnetNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``SubnetID:`` none
    |  ``attribute type:`` string

    |  ``SubnetCIDR:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``SubnetMemberCount:`` none
    |  ``attribute type:`` string

    """

    properties = ("SubnetID",
                  "SubnetCIDR",
                  "VirtualNetworkID",
                  "Network",
                  "VlanName",
                  "VlanIndex",
                  "VlanID",
                  "RootBridgeAddress",
                  "SubnetMemberCount",
                  )
