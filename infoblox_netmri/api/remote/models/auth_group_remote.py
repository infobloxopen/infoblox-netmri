from ..remote import RemoteModel


class AuthGroupRemote(RemoteModel):
    """
    The defined NetMRI users.


    |  ``id:`` The id of the authentication remote group
    |  ``attribute type:`` number

    |  ``group_name:`` The name of the authentication remote group
    |  ``attribute type:`` string

    |  ``auth_service_id:`` The id of the authentication service, where this group is defined.
    |  ``attribute type:`` number

    |  ``enabled_ind:`` A flag indicating whether this group mappings to NetMRI roles is enabled or disabled.
    |  ``attribute type:`` bool

    |  ``description:`` Description/comment about this remote group.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``last_logged_time:`` The last connection date and time of a user belonging to this AuthGroup.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "group_name",
                  "auth_service_id",
                  "enabled_ind",
                  "description",
                  "created_at",
                  "updated_at",
                  "last_logged_time",
                  )
