from ..remote import RemoteModel


class SNMPCredentialRemote(RemoteModel):
    """
    The SNMP credentials to use when accessing devices.


    |  ``PasswordID:`` The internal NetMRI identifier for this credential.
    |  ``attribute type:`` number

    |  ``UnitID:`` The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
    |  ``attribute type:`` number

    |  ``Protocol:`` The protocol for which to use this password: 'SNMP' or 'SNMPv3'.
    |  ``attribute type:`` string

    |  ``Type:`` Whether this is a read-only 'RO' or read/write 'RW' community.
    |  ``attribute type:`` string

    |  ``Origination:`` Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential.
    |  ``attribute type:`` string

    |  ``Vendor:`` The vendor devices against which to try this credential.
    |  ``attribute type:`` string

    |  ``SNMPAuthProto:`` The SNMPv3 authentication protocol to use with this credential.
    |  ``attribute type:`` string

    |  ``SNMPPrivProto:`` The SNMPv3 privacy protocol to use with this credential.
    |  ``attribute type:`` string

    |  ``Priority:`` The priority order in which to attempt this credential.
    |  ``attribute type:`` number

    |  ``PasswordSecure:`` (alias Password) The community string.
    |  ``attribute type:`` string

    |  ``SNMPAuthPWSecure:`` (alias SNMPAuthPW) The SNMPv3 authentication protocol password.
    |  ``attribute type:`` string

    |  ``SNMPPrivPWSecure:`` (alias SNMPPrivPW) The SNMPv3 privacy protocol password.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number

    |  ``CredentialGroupID:`` The unique identifier of the credential group.
    |  ``attribute type:`` number

    """

    properties = ("PasswordID",
                  "UnitID",
                  "Protocol",
                  "Type",
                  "Origination",
                  "Vendor",
                  "SNMPAuthProto",
                  "SNMPPrivProto",
                  "Priority",
                  "PasswordSecure",
                  "SNMPAuthPWSecure",
                  "SNMPPrivPWSecure",
                  "SecureVersion",
                  "CredentialGroupID",
                  )
