from ..remote import RemoteModel


class PortListGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``Protocol:`` none
    |  ``attribute type:`` string

    |  ``Port:`` none
    |  ``attribute type:`` string

    |  ``Service:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "Protocol",
                  "Port",
                  "Service",
                  )
