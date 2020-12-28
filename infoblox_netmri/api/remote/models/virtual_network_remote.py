from ..remote import RemoteModel


class VirtualNetworkRemote(RemoteModel):
    """
    Distinct Virtual Routing and Forwarding based VPNs in the network.


    |  ``VirtualNetworkName:`` The name of the Network View.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal NetMRI identifier for this Network View.
    |  ``attribute type:`` number

    |  ``VirtualNetworkDescription:`` A description of this Virtual Network.
    |  ``attribute type:`` string

    |  ``VirtualNetworkDeleteInd:`` Indicates if this Virtual Network has been deleted.
    |  ``attribute type:`` bool

    """

    properties = ("VirtualNetworkName",
                  "VirtualNetworkID",
                  "VirtualNetworkDescription",
                  "VirtualNetworkDeleteInd",
                  )
