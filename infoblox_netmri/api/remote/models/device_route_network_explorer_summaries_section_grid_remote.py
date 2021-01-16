from ..remote import RemoteModel


class DeviceRouteNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``DeviceRouteID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``RouteProto:`` none
    |  ``attribute type:`` string

    |  ``RouteCIDR:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``route_count:`` none
    |  ``attribute type:`` string

    |  ``route_numeric:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceRouteID",
                  "DeviceID",
                  "RouteProto",
                  "RouteCIDR",
                  "VirtualNetworkID",
                  "Network",
                  "route_count",
                  "route_numeric",
                  )
