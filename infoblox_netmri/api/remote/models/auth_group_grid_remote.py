from ..remote import RemoteModel


class AuthGroupGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``auth_service_id:`` none
    |  ``attribute type:`` string

    |  ``group_name:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``enabled_ind:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``roles:`` none
    |  ``attribute type:`` string

    |  ``last_login:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "auth_service_id",
                  "group_name",
                  "description",
                  "enabled_ind",
                  "status",
                  "roles",
                  "last_login",
                  )
