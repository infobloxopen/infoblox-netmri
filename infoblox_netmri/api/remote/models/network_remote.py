from ..remote import RemoteModel


class NetworkRemote(RemoteModel):
    """
    This table list out the entries of network system.


    |  ``id:`` The internal NetMRI identifier of a network.
    |  ``attribute type:`` number

    |  ``name:`` The name of a network.
    |  ``attribute type:`` string

    |  ``description:`` The description of a network.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "name",
                  "description",
                  "created_at",
                  "updated_at",
                  )
