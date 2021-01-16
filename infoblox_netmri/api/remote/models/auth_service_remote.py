from ..remote import RemoteModel


class AuthServiceRemote(RemoteModel):
    """
    This table list out the entries of Authentication Services.


    |  ``id:`` The id of the authentication service.
    |  ``attribute type:`` number

    |  ``service_name:`` The name of the Authentication Service.
    |  ``attribute type:`` string

    |  ``auth_method:`` The Authentication method of the service. One of (local, radius, tacacs, ldap, activedirectory).
    |  ``attribute type:`` string

    |  ``description:`` Description/comment about this authentication service
    |  ``attribute type:`` string

    |  ``priority:`` The priority assigned to this Authentication Service.
    |  ``attribute type:`` number

    |  ``context_params_json:`` Additional specific authentication method parameters are stored in this field using a json format. (such as 'base_dn' for LDAP method, Vendor Specific Attribute ID for Radius,...).
    |  ``attribute type:`` string

    |  ``enabled_ind:`` A flag indicating whether the authentication service settings is enabled or disabled.
    |  ``attribute type:`` bool

    |  ``enabled_authz_ind:`` A flag indicating whether this service is used for computing privileges for the remote users.
    |  ``attribute type:`` bool

    |  ``timeout:`` The timeout interval of the service authentication servers.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "service_name",
                  "auth_method",
                  "description",
                  "priority",
                  "context_params_json",
                  "enabled_ind",
                  "enabled_authz_ind",
                  "timeout",
                  "created_at",
                  "updated_at",
                  )
