from ..remote import RemoteModel


class DeviceRouteNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceRouteID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``Interface:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VrfNetworkViewID:`` none
    |  ``attribute type:`` string

    |  ``VrfNetworkView:`` none
    |  ``attribute type:`` string

    |  ``InterfaceName:`` none
    |  ``attribute type:`` string

    |  ``InterfaceNameSort:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``RouteNextHopIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RouteNextHopIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``RouteProto:`` none
    |  ``attribute type:`` string

    |  ``RouteCIDR:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    |  ``CIDRouteNumeric:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "InterfaceID",
                  "DeviceRouteID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "ifDescr",
                  "Interface",
                  "VirtualNetworkMemberName",
                  "VrfNetworkViewID",
                  "VrfNetworkView",
                  "InterfaceName",
                  "InterfaceNameSort",
                  "DeviceType",
                  "RouteNextHopIPDotted",
                  "RouteNextHopIPNumeric",
                  "ifIndex",
                  "RouteProto",
                  "RouteCIDR",
                  "RouteDistinguisher",
                  "DeviceAssurance",
                  "CIDRouteNumeric",
                  )
