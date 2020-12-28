from ..remote import RemoteModel


class AuthServerRemote(RemoteModel):
    """
    This table list out the entries of Authentication Servers.


    |  ``id:`` The authentication server identifier.
    |  ``attribute type:`` number

    |  ``priority:`` Priority assigned to an authentication server.
    |  ``attribute type:`` number

    |  ``enabled_ind:`` A flag indicating whether the authentication server settings is enabled or disabled.
    |  ``attribute type:`` bool

    |  ``auth_server:`` Authentication Server Name (required for Radius, Tacacs, LDAP and Active Directory methods).
    |  ``attribute type:`` string

    |  ``auth_port:`` Authentication Port (required for Active Directory method).
    |  ``attribute type:`` number

    |  ``auth_shared_secret:`` The shared secret of an authentication server (required for Radius and Tacacs methods).
    |  ``attribute type:`` string

    |  ``auth_encryption:`` The Encryption method (none or SSL) (required for Active Directory method).
    |  ``attribute type:`` string

    |  ``auth_cert:`` The SSL certificate of an Authentication Server. (Required for Active Directory method).
    |  ``attribute type:`` string

    |  ``auth_timeout:`` The timeout interval of an authentication server settings (Required for Active Directory method).
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``secure_version:`` Internal encrypt version used for any auth_shared_secret
    |  ``attribute type:`` number

    |  ``auth_service_id:`` The id of the authentication service, this server is member of.
    |  ``attribute type:`` number

    |  ``auth_protocol:`` The password exchange protocol to use for authentication. One of (PAP, CHAP)
    |  ``attribute type:`` string

    |  ``source_interface_id:`` The NetMRI interface to use as source of the packets sent to the authentication server.
    |  ``attribute type:`` number

    |  ``auth_version:`` The version use for the authentication (LDAP).
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "priority",
                  "enabled_ind",
                  "auth_server",
                  "auth_port",
                  "auth_shared_secret",
                  "auth_encryption",
                  "auth_cert",
                  "auth_timeout",
                  "created_at",
                  "updated_at",
                  "secure_version",
                  "auth_service_id",
                  "auth_protocol",
                  "source_interface_id",
                  "auth_version",
                  )
