from ..remote import RemoteModel


class AuthServiceGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``priority:`` none
    |  ``attribute type:`` string

    |  ``service_name:`` none
    |  ``attribute type:`` string

    |  ``auth_method:`` none
    |  ``attribute type:`` string

    |  ``timeout:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``auth_status:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``context_params_json:`` none
    |  ``attribute type:`` string

    |  ``enabled_ind:`` none
    |  ``attribute type:`` string

    |  ``enabled_authz_ind:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "priority",
                  "service_name",
                  "auth_method",
                  "timeout",
                  "status",
                  "auth_status",
                  "description",
                  "context_params_json",
                  "enabled_ind",
                  "enabled_authz_ind",
                  )
