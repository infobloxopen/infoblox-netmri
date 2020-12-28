from ..remote import RemoteModel


class DeviceViewerSwitchVlanConfigurationGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``StpMaxAge:`` none
    |  ``attribute type:`` string

    |  ``StpHelloTime:`` none
    |  ``attribute type:`` string

    |  ``StpForwardDelay:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeMaxAge:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeHelloTime:`` none
    |  ``attribute type:`` string

    |  ``StpBridgeForwardDelay:`` none
    |  ``attribute type:`` string

    |  ``red:`` none
    |  ``attribute type:`` string

    |  ``stpred:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DataSourceID",
                  "RootBridgeAddress",
                  "RootVlanMemberID",
                  "VlanIndex",
                  "VlanID",
                  "VlanName",
                  "StpMaxAge",
                  "StpHelloTime",
                  "StpForwardDelay",
                  "StpBridgeMaxAge",
                  "StpBridgeHelloTime",
                  "StpBridgeForwardDelay",
                  "red",
                  "stpred",
                  )
