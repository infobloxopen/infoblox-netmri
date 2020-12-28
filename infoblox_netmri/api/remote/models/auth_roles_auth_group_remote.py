from ..remote import RemoteModel


class AuthRolesAuthGroupRemote(RemoteModel):
    """
    The defined NetMRI remote group roles. A role is a collection of user privileges.


    |  ``id:`` The internal NetMRI identifier for this record.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``auth_role_id:`` The internal NetMRI identifier for role definition.
    |  ``attribute type:`` number

    |  ``auth_group_id:`` The internal NetMRI identifier for group definition.
    |  ``attribute type:`` number

    |  ``DeviceGroupID:`` The internal NetMRI identifier for device group definition.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "created_at",
                  "updated_at",
                  "auth_role_id",
                  "auth_group_id",
                  "DeviceGroupID",
                  )
