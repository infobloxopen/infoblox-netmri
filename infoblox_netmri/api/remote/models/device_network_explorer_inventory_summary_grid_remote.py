from ..remote import RemoteModel


class DeviceNetworkExplorerInventorySummaryGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``Collector:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``DeviceModel:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceAssurance",
                  )
