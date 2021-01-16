from ..remote import RemoteModel


class DeviceViewerSwitchFwdGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``LocalInterface:`` none
    |  ``attribute type:`` string

    |  ``LocalInterfaceName:`` none
    |  ``attribute type:`` string

    |  ``LocalInterfaceNameSort:`` none
    |  ``attribute type:`` string

    |  ``LocalInterfaceDescription:`` none
    |  ``attribute type:`` string

    |  ``LocalInterfaceID:`` none
    |  ``attribute type:`` string

    |  ``LocalIfIndex:`` none
    |  ``attribute type:`` string

    |  ``LocalDeviceID:`` none
    |  ``attribute type:`` string

    |  ``LocalIfPortControlInd:`` none
    |  ``attribute type:`` string

    |  ``SwitchPortFwdStatus:`` none
    |  ``attribute type:`` string

    |  ``MacAddress:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    |  ``Interface:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``InterfaceName:`` none
    |  ``attribute type:`` string

    |  ``InterfaceNameSort:`` none
    |  ``attribute type:`` string

    |  ``InterfaceDescription:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``RootBridgeAddress:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VlanIndex",
                  "VlanName",
                  "VlanID",
                  "LocalInterface",
                  "LocalInterfaceName",
                  "LocalInterfaceNameSort",
                  "LocalInterfaceDescription",
                  "LocalInterfaceID",
                  "LocalIfIndex",
                  "LocalDeviceID",
                  "LocalIfPortControlInd",
                  "SwitchPortFwdStatus",
                  "MacAddress",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceID",
                  "DeviceName",
                  "DeviceType",
                  "DeviceAssurance",
                  "Interface",
                  "ifIndex",
                  "InterfaceName",
                  "InterfaceNameSort",
                  "InterfaceDescription",
                  "InterfaceID",
                  "RootBridgeAddress",
                  "RootVlanMemberID",
                  "ifPortControlInd",
                  )
