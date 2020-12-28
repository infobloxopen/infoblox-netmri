from ..remote import RemoteModel


class IfWirelessSsidGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDTimestamp:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDStartTime:`` none
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDEndTime:`` none
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDChangedCols:`` none
    |  ``attribute type:`` string

    |  ``SSIDIndex:`` none
    |  ``attribute type:`` string

    |  ``SSID:`` none
    |  ``attribute type:`` string

    |  ``SSIDMaxAssociations:`` none
    |  ``attribute type:`` string

    |  ``WEPMICAlgorithm:`` none
    |  ``attribute type:`` string

    |  ``WEPPermuteAlgorithm:`` none
    |  ``attribute type:`` string

    |  ``SSIDDefaultVlanIndex:`` none
    |  ``attribute type:`` string

    |  ``SSIDBroadcastInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "ifWirelessSSIDTimestamp",
                  "DeviceID",
                  "ifIndex",
                  "ifName",
                  "ifNameSort",
                  "ifWirelessSSIDStartTime",
                  "ifWirelessSSIDEndTime",
                  "ifWirelessSSIDChangedCols",
                  "SSIDIndex",
                  "SSID",
                  "SSIDMaxAssociations",
                  "WEPMICAlgorithm",
                  "WEPPermuteAlgorithm",
                  "SSIDDefaultVlanIndex",
                  "SSIDBroadcastInd",
                  )
