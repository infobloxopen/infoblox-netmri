from ..remote import RemoteModel


class AuthRoleRemote(RemoteModel):
    """
    The defined NetMRI user roles. A role is a collection of user privileges.


    |  ``id:`` The internal NetMRI identifier for this role definition.
    |  ``attribute type:`` number

    |  ``role_name:`` The name of the role, as displayed in the user interface.
    |  ``attribute type:`` string

    |  ``description:`` The description of the role, as displayed in the user interface.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``is_system:`` A flag indicating whether or not this is a build-in role. Built-in roles may not be modified.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "role_name",
                  "description",
                  "created_at",
                  "updated_at",
                  "is_system",
                  )
