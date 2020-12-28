from ..remote import RemoteModel


class ConfigListRemote(RemoteModel):
    """
    Configuration lists as defined in the NetMRI and accessible to NetMRI scripts.


    |  ``id:`` The internal NetMRI identifier of this configuration list.
    |  ``attribute type:`` number

    |  ``auth_user_id:`` The internal NetMRI identifier of the user that created this list.
    |  ``attribute type:`` number

    |  ``name:`` The name of this list, as specified by the user.
    |  ``attribute type:`` string

    |  ``description:`` The description of this list, as specified by the user.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "auth_user_id",
                  "name",
                  "description",
                  "created_at",
                  "updated_at",
                  )
