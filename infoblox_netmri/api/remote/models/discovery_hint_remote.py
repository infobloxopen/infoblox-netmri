from ..remote import RemoteModel


class DiscoveryHintRemote(RemoteModel):
    """
    Discovery hints used by the NetMRI discovery engine.


    |  ``id:`` The internal NetMRI identifier for the discovery hint.
    |  ``attribute type:`` number

    |  ``hint:`` The hint used the by discovery engine.
    |  ``attribute type:`` string

    |  ``device_type:`` The device type applied to the given discovery hint.
    |  ``attribute type:`` string

    |  ``UnitID:`` The internal NetMRI identifier collector assigned to the discovery hint.
    |  ``attribute type:`` number

    |  ``created_by:`` The user that initially created the discovery hint.
    |  ``attribute type:`` string

    |  ``updated_by:`` The user that last updated the discovery hint.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the hint was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the hint was last modified.
    |  ``attribute type:`` datetime

    |  ``cli_user_name_secure:`` The user name for the device.
    |  ``attribute type:`` string

    |  ``cli_user_password_secure:`` The password for the device.
    |  ``attribute type:`` string

    |  ``snmp_protocol:`` The SNMP protocol for which to use these credentials.
    |  ``attribute type:`` string

    |  ``snmp_community_secure:`` The SNMP community string.
    |  ``attribute type:`` string

    |  ``snmp_auth_protocol:`` The SNMPv3 authentication protocol to use with this credential.
    |  ``attribute type:`` string

    |  ``snmp_auth_password_secure:`` The SNMPv3 authentication protocol password
    |  ``attribute type:`` string

    |  ``snmp_private_protocol:`` The SNMPv3 privacy protocol to use with this credential.
    |  ``attribute type:`` string

    |  ``snmp_private_password_secure:`` The SNMPv3 privacy protocol password.
    |  ``attribute type:`` string

    |  ``secure_version:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number

    |  ``cli_user_name_secure_ssh:`` Device specific CLI username for ssh protocol.
    |  ``attribute type:`` string

    |  ``cli_user_password_secure_ssh:`` Device specific CLI password for ssh protocol.
    |  ``attribute type:`` string

    |  ``cli_user_name_secure_telnet:`` Device specific CLI username for telnet protocol.
    |  ``attribute type:`` string

    |  ``cli_user_password_secure_telnet:`` Device specific CLI password for telnet protocol.
    |  ``attribute type:`` string

    |  ``cli_enable_password_secure:`` Device specific CLI enable password for all protocols.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "hint",
                  "device_type",
                  "UnitID",
                  "created_by",
                  "updated_by",
                  "created_at",
                  "updated_at",
                  "cli_user_name_secure",
                  "cli_user_password_secure",
                  "snmp_protocol",
                  "snmp_community_secure",
                  "snmp_auth_protocol",
                  "snmp_auth_password_secure",
                  "snmp_private_protocol",
                  "snmp_private_password_secure",
                  "secure_version",
                  "cli_user_name_secure_ssh",
                  "cli_user_password_secure_ssh",
                  "cli_user_name_secure_telnet",
                  "cli_user_password_secure_telnet",
                  "cli_enable_password_secure",
                  )
