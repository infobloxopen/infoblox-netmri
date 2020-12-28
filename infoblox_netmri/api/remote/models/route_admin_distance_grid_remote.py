from ..remote import RemoteModel


class RouteAdminDistanceGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``RouteDistanceID:`` none
    |  ``attribute type:`` string

    |  ``RouteProtocol:`` none
    |  ``attribute type:`` string

    |  ``AdminDistance:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "RouteDistanceID",
                  "RouteProtocol",
                  "AdminDistance",
                  )
