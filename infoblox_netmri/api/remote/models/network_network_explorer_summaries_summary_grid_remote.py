from ..remote import RemoteModel


class NetworkNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``ifType:`` none
    |  ``attribute type:`` string

    |  ``ifIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceIPNumeric",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceType",
                  "ifIndex",
                  "ifName",
                  "VirtualNetworkMemberName",
                  "ifType",
                  "ifIPDotted",
                  "ifIPNumeric",
                  )
