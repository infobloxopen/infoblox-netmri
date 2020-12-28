from ..remote import RemoteModel


class VrfNetworkGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberID:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberDescription:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``VrfStatus:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VirtualNetworkMemberID",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkMemberDescription",
                  "DeviceID",
                  "DeviceName",
                  "DeviceType",
                  "DeviceIPNumeric",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "VrfStatus",
                  )
