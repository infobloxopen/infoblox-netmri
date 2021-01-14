from ..remote import RemoteModel


class DeviceViewerRouterOspfAreaGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``RoutingAreaNumber:`` none
    |  ``attribute type:`` string

    |  ``RoutingAreaName:`` none
    |  ``attribute type:`` string

    |  ``OspfAuthType:`` none
    |  ``attribute type:`` string

    |  ``OspfImportAsExtern:`` none
    |  ``attribute type:`` string

    |  ``OspfAreaBdrRtrCount:`` none
    |  ``attribute type:`` string

    |  ``OspfSpfRunsDelta:`` none
    |  ``attribute type:`` string

    |  ``OspfAsBdrRtrCount:`` none
    |  ``attribute type:`` string

    |  ``OspfAreaLsaCount:`` none
    |  ``attribute type:`` string

    |  ``OspfAreaLsaCksumSum:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "RoutingAreaNumber",
                  "RoutingAreaName",
                  "OspfAuthType",
                  "OspfImportAsExtern",
                  "OspfAreaBdrRtrCount",
                  "OspfSpfRunsDelta",
                  "OspfAsBdrRtrCount",
                  "OspfAreaLsaCount",
                  "OspfAreaLsaCksumSum",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  )
