from ..remote import RemoteModel


class DeviceViewerSwitchVlanTrunksGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``TrunkState:`` none
    |  ``attribute type:`` string

    |  ``TrunkStatus:`` none
    |  ``attribute type:`` string

    |  ``TrunkEncapsulationType:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``peer:`` none
    |  ``attribute type:`` string

    |  ``peerid:`` none
    |  ``attribute type:`` string

    |  ``peerintf:`` none
    |  ``attribute type:`` string

    |  ``peerintfSort:`` none
    |  ``attribute type:`` string

    |  ``peerintfindex:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "ifNameSort",
                  "ifIndex",
                  "TrunkState",
                  "TrunkStatus",
                  "TrunkEncapsulationType",
                  "VlanName",
                  "VlanIndex",
                  "VlanID",
                  "RootBridgeAddress",
                  "RootVlanMemberID",
                  "peer",
                  "peerid",
                  "peerintf",
                  "peerintfSort",
                  "peerintfindex",
                  "ifPortControlInd",
                  )
