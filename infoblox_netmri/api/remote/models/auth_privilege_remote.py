from ..remote import RemoteModel


class AuthPrivilegeRemote(RemoteModel):
    """
    The user privileges defined within NetMRI.


    |  ``id:`` The internal NetMRI identifier for this user privilege.
    |  ``attribute type:`` number

    |  ``privilege_name:`` The name of this user privilege, as shown in the user interface.
    |  ``attribute type:`` string

    |  ``sequence:`` Not used.
    |  ``attribute type:`` string

    |  ``description:`` The description of this user privilege, as shown in the user interface.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``reference:`` The internal key used to identify this privilege; this is the value shown in the API documentation page for those methods requiring a privilege.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "privilege_name",
                  "sequence",
                  "description",
                  "created_at",
                  "updated_at",
                  "reference",
                  )
