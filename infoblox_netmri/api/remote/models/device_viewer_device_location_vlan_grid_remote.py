from ..remote import RemoteModel


class DeviceViewerDeviceLocationVlanGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifMAC:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``RootBridge:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootID:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    |  ``ifTrunkStatus:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``ifAdminStatus:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceVendor",
                  "ifName",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkID",
                  "Network",
                  "ifNameSort",
                  "ifIndex",
                  "ifMAC",
                  "VlanName",
                  "VlanIndex",
                  "VlanID",
                  "RootBridge",
                  "RootBridgeAddress",
                  "RootID",
                  "RootVlanMemberID",
                  "ifPortControlInd",
                  "ifTrunkStatus",
                  "ifDescr",
                  "ifAdminStatus",
                  )
