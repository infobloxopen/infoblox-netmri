from ..remote import RemoteModel


class DeviceSectionGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``RoutingInd:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "DeviceName",
                  "DeviceType",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceIPNumeric",
                  "RoutingInd",
                  "DeviceAssurance",
                  )
