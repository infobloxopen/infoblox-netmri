from ..remote import RemoteModel


class DeviceViewerSwitchActiveVlansGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeName:`` none
    |  ``attribute type:`` string

    |  ``RootPriority:`` none
    |  ``attribute type:`` string

    |  ``StpPriority:`` none
    |  ``attribute type:`` string

    |  ``StpRootCost:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``StpProtocolSpecification:`` none
    |  ``attribute type:`` string

    |  ``red:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DataSourceID",
                  "VlanIndex",
                  "VlanID",
                  "VlanName",
                  "RootVlanMemberID",
                  "RootBridgeAddress",
                  "RootID",
                  "RootBridgeName",
                  "RootPriority",
                  "StpPriority",
                  "StpRootCost",
                  "ifName",
                  "ifNameSort",
                  "ifIndex",
                  "StpProtocolSpecification",
                  "red",
                  "ifPortControlInd",
                  )
