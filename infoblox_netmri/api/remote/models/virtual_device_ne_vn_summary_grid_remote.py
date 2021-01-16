from ..remote import RemoteModel


class VirtualDeviceNeVnSummaryGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostDeviceID:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostDeviceName:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostDeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostDeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostNetwork:`` none
    |  ``attribute type:`` string

    |  ``VirtualHostDeviceType:`` none
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

    |  ``DeviceMAC:`` none
    |  ``attribute type:`` string

    |  ``DeviceContextName:`` none
    |  ``attribute type:`` string

    |  ``AssetType:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "VirtualHostDeviceID",
                  "VirtualHostDeviceName",
                  "VirtualHostDeviceIPDotted",
                  "VirtualHostDeviceIPNumeric",
                  "VirtualHostNetwork",
                  "VirtualHostDeviceType",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceMAC",
                  "DeviceContextName",
                  "AssetType",
                  )
