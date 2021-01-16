from ..remote import RemoteModel


class CLICredentialRemote(RemoteModel):
    """
    The CLI credentials to use when accessing devices.


    |  ``UnitID:`` The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
    |  ``attribute type:`` number

    |  ``Protocol:`` The protocol for which to use this credential.
    |  ``attribute type:`` string

    |  ``Origination:`` Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential.
    |  ``attribute type:`` string

    |  ``UPWUse:`` Determines the function of the credential. 'GUESS' indicates that this will only be used if vendor default credential collection is enabled, whereas 'LOCAL' means that this credential will be used in all guessing.
    |  ``attribute type:`` string

    |  ``HitCount:`` The number of successful uses of this credential.
    |  ``attribute type:`` number

    |  ``Vendor:`` The vendor devices against which to try this credential.
    |  ``attribute type:`` string

    |  ``id:`` The internal NetMRI identifier for this credential.
    |  ``attribute type:`` number

    |  ``Priority:`` The priority order in which to attempt this credential.
    |  ``attribute type:`` string

    |  ``UsernameSecure:`` The username portion of the credential.
    |  ``attribute type:`` string

    |  ``PasswordSecure:`` The password portion of the credential.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The encryption version of the username and password.
    |  ``attribute type:`` number

    |  ``CredentialGroupID:`` The unique identifier of the credential group.
    |  ``attribute type:`` number

    """

    properties = ("UnitID",
                  "Protocol",
                  "Origination",
                  "UPWUse",
                  "HitCount",
                  "Vendor",
                  "id",
                  "Priority",
                  "UsernameSecure",
                  "PasswordSecure",
                  "SecureVersion",
                  "CredentialGroupID",
                  )
