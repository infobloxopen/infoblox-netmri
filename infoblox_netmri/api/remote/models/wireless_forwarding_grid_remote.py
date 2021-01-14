from ..remote import RemoteModel


class WirelessForwardingGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``WirelessFwdTimestamp:`` none
    |  ``attribute type:`` string

    |  ``RemoteDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RemoteDeviceType:`` none
    |  ``attribute type:`` string

    |  ``RemoteMAC:`` none
    |  ``attribute type:`` string

    |  ``RemoteIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RemoteDevice:`` none
    |  ``attribute type:`` string

    |  ``RemoteIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``RemoteStatus:`` none
    |  ``attribute type:`` string

    |  ``RemoteUsername:`` none
    |  ``attribute type:`` string

    |  ``RemoteClass:`` none
    |  ``attribute type:`` string

    |  ``AssociatedSSID:`` none
    |  ``attribute type:`` string

    |  ``AssociatedVlan:`` none
    |  ``attribute type:`` string

    |  ``BSSDevice:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "WirelessFwdTimestamp",
                  "RemoteDeviceID",
                  "RemoteDeviceType",
                  "RemoteMAC",
                  "RemoteIPDotted",
                  "RemoteDevice",
                  "RemoteIPNumeric",
                  "RemoteStatus",
                  "RemoteUsername",
                  "RemoteClass",
                  "AssociatedSSID",
                  "AssociatedVlan",
                  "BSSDevice",
                  )
