from ..remote import RemoteModel


class HubLocatorNetworkExplorerInventorySummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifSpeed:`` none
    |  ``attribute type:`` string

    |  ``ifState:`` none
    |  ``attribute type:`` string

    |  ``ifLastChange:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    |  ``NeighborCnt:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "InterfaceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceType",
                  "ifIndex",
                  "ifName",
                  "ifSpeed",
                  "ifState",
                  "ifLastChange",
                  "ifPortControlInd",
                  "NeighborCnt",
                  "DeviceAssurance",
                  )
