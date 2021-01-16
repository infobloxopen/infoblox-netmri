from ..remote import RemoteModel


class DeviceViewerDeviceLocationSwitchPortGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
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

    |  ``macaddress:`` none
    |  ``attribute type:`` string

    |  ``switchname:`` none
    |  ``attribute type:`` string

    |  ``switchip:`` none
    |  ``attribute type:`` string

    |  ``peerid:`` none
    |  ``attribute type:`` string

    |  ``switchiface:`` none
    |  ``attribute type:`` string

    |  ``switchifaceSort:`` none
    |  ``attribute type:`` string

    |  ``peerintfindex:`` none
    |  ``attribute type:`` string

    |  ``peerDeviceType:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    |  ``ifTrunkStatus:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``ifAdminStatus:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkID",
                  "Network",
                  "ifNameSort",
                  "ifIndex",
                  "macaddress",
                  "switchname",
                  "switchip",
                  "peerid",
                  "switchiface",
                  "switchifaceSort",
                  "peerintfindex",
                  "peerDeviceType",
                  "ifPortControlInd",
                  "ifTrunkStatus",
                  "ifDescr",
                  "ifAdminStatus",
                  "VlanIndex",
                  "VlanName",
                  )
