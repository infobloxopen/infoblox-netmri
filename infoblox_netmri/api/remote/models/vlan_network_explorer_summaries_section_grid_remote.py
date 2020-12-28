from ..remote import RemoteModel


class VlanNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeDeviceName:`` none
    |  ``attribute type:`` string

    |  ``VlanCount:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeDeviceID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeDeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeDeviceIPNumeric:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VlanID",
                  "DeviceID",
                  "VlanIndex",
                  "VlanName",
                  "VirtualNetworkID",
                  "Network",
                  "RootBridgeDeviceName",
                  "VlanCount",
                  "RootVlanMemberID",
                  "RootBridgeDeviceID",
                  "RootBridgeDeviceIPDotted",
                  "RootBridgeDeviceIPNumeric",
                  )
