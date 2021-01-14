from ..remote import RemoteModel


class VlanNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``VlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``BridgeMemberInd:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
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

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VlanMemberTimestamp:`` none
    |  ``attribute type:`` string

    |  ``StpPriority:`` none
    |  ``attribute type:`` string

    |  ``BaseBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeMaxAge:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeHelloTime:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeForwardDelay:`` none
    |  ``attribute type:`` string

    |  ``Timers:`` none
    |  ``attribute type:`` string

    """

    properties = ("VlanID",
                  "VlanMemberID",
                  "BridgeMemberInd",
                  "RootVlanMemberID",
                  "DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "VlanIndex",
                  "VlanName",
                  "VlanMemberTimestamp",
                  "StpPriority",
                  "BaseBridgeAddress",
                  "StpBridgeMaxAge",
                  "StpBridgeHelloTime",
                  "StpBridgeForwardDelay",
                  "Timers",
                  )
