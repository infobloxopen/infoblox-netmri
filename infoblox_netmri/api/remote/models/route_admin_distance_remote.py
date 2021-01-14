from ..remote import RemoteModel


class RouteAdminDistanceRemote(RemoteModel):
    """
    This table list out the route admin distances.


    |  ``id:`` The internal NetMRI identifier for this route admin distance.
    |  ``attribute type:`` number

    |  ``route_protocol:`` The route protocol name.
    |  ``attribute type:`` string

    |  ``admin_distance:`` The admin distance.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "route_protocol",
                  "admin_distance",
                  )
