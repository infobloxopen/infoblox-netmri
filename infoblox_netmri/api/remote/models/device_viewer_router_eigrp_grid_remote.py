from ..remote import RemoteModel


class DeviceViewerRouterEigrpGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``RPPeerDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RPPeerIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``RoutingAreaName:`` none
    |  ``attribute type:`` string

    |  ``RPPeerUpSince:`` none
    |  ``attribute type:`` string

    |  ``EigrpRetransCount:`` none
    |  ``attribute type:`` string

    |  ``EigrpRetriesCount:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "InterfaceID",
                  "ifName",
                  "ifNameSort",
                  "VirtualNetworkID",
                  "Network",
                  "ifIndex",
                  "RPPeerDeviceID",
                  "RPPeerIPDotted",
                  "RPPeerIPNumeric",
                  "RoutingAreaName",
                  "RPPeerUpSince",
                  "EigrpRetransCount",
                  "EigrpRetriesCount",
                  "ifPortControlInd",
                  )
