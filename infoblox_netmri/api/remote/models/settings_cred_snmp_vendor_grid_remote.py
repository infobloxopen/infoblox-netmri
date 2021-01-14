from ..remote import RemoteModel


class SettingsCredSnmpVendorGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Priority:`` none
    |  ``attribute type:`` string

    |  ``Protocol:`` none
    |  ``attribute type:`` string

    |  ``Password:`` none
    |  ``attribute type:`` string

    |  ``Origination:`` none
    |  ``attribute type:`` string

    |  ``Vendor:`` none
    |  ``attribute type:`` string

    |  ``Type:`` none
    |  ``attribute type:`` string

    |  ``PasswordID:`` none
    |  ``attribute type:`` string

    |  ``UnitID:`` none
    |  ``attribute type:`` string

    |  ``Successful:`` none
    |  ``attribute type:`` string

    |  ``Invalid:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "Network",
                  "Priority",
                  "Protocol",
                  "Password",
                  "Origination",
                  "Vendor",
                  "Type",
                  "PasswordID",
                  "UnitID",
                  "Successful",
                  "Invalid",
                  )
