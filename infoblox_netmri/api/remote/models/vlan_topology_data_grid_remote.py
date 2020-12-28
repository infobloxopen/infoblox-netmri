from ..remote import RemoteModel


class VlanTopologyDataGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``VlanMemberID:`` none
    |  ``attribute type:`` string

    |  ``StartDeviceID:`` none
    |  ``attribute type:`` string

    |  ``StpRootCost:`` none
    |  ``attribute type:`` string

    |  ``StpPortState:`` none
    |  ``attribute type:`` string

    |  ``NeighborID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``NeighborDeviceID:`` none
    |  ``attribute type:`` string

    |  ``NeighborIfIndex:`` none
    |  ``attribute type:`` string

    |  ``NeighborInterfaceID:`` none
    |  ``attribute type:`` string

    |  ``CDPInd:`` none
    |  ``attribute type:`` string

    |  ``LLDPInd:`` none
    |  ``attribute type:`` string

    |  ``RootMemberInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VlanID",
                  "VlanName",
                  "RootVlanMemberID",
                  "VlanMemberID",
                  "StartDeviceID",
                  "StpRootCost",
                  "StpPortState",
                  "NeighborID",
                  "InterfaceID",
                  "DeviceID",
                  "ifIndex",
                  "NeighborDeviceID",
                  "NeighborIfIndex",
                  "NeighborInterfaceID",
                  "CDPInd",
                  "LLDPInd",
                  "RootMemberInd",
                  )
