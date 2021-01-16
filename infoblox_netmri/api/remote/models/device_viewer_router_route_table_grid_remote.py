from ..remote import RemoteModel


class DeviceViewerRouterRouteTableGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``RouteProto:`` none
    |  ``attribute type:`` string

    |  ``RouteType:`` none
    |  ``attribute type:`` string

    |  ``RouteCIDR:`` none
    |  ``attribute type:`` string

    |  ``RouteSubnetIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberDescription:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    |  ``RouteNextHopIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RouteNextHopIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``RouteNextHopDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RouteMetric1:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceID",
                  "InterfaceID",
                  "RouteProto",
                  "RouteType",
                  "RouteCIDR",
                  "RouteSubnetIPNumeric",
                  "ifName",
                  "ifNameSort",
                  "ifDescr",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkMemberDescription",
                  "RouteDistinguisher",
                  "RouteNextHopIPDotted",
                  "RouteNextHopIPNumeric",
                  "RouteNextHopDeviceID",
                  "RouteMetric1",
                  "ifIndex",
                  "ifPortControlInd",
                  )
