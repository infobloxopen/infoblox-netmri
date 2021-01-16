from ..remote import RemoteModel


class NetworkViewViwerAssociatedVrfsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``RouteDistinguisher:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceName",
                  "VirtualNetworkMemberName",
                  "RouteDistinguisher",
                  )
