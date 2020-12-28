from ..remote import RemoteModel


class ProxyOsNetworkExplorerInventorySectionGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``os_label:`` none
    |  ``attribute type:`` string

    |  ``os_count:`` none
    |  ``attribute type:`` string

    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "os_label",
                  "os_count",
                  "DeviceVersion",
                  "DeviceVendor",
                  )
