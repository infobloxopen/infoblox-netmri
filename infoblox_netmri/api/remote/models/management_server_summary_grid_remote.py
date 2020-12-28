from ..remote import RemoteModel


class ManagementServerSummaryGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ManagementServerID:`` none
    |  ``attribute type:`` string

    |  ``ManagementServerName:`` none
    |  ``attribute type:`` string

    |  ``ManagementServerIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ManagementServerIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``ManagementServerType:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Collector:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceMAC:`` none
    |  ``attribute type:`` string

    |  ``AssetType:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "ManagementServerID",
                  "ManagementServerName",
                  "ManagementServerIPDotted",
                  "ManagementServerIPNumeric",
                  "ManagementServerType",
                  "Network",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceMAC",
                  "AssetType",
                  )
