from ..remote import RemoteModel


class DeviceWirelessGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceWirelessTimestamp:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``StationID:`` none
    |  ``attribute type:`` string

    |  ``DesiredSSID:`` none
    |  ``attribute type:`` string

    |  ``StationRole:`` none
    |  ``attribute type:`` string

    |  ``WEPEnabledInd:`` none
    |  ``attribute type:`` string

    |  ``WEPAllowedInd:`` none
    |  ``attribute type:`` string

    |  ``WEPOnlyTrafficInd:`` none
    |  ``attribute type:`` string

    |  ``WEPICVErrorCount:`` none
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen1:`` none
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen2:`` none
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen3:`` none
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen4:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceWirelessTimestamp",
                  "DeviceID",
                  "ifIndex",
                  "ifName",
                  "ifNameSort",
                  "StationID",
                  "DesiredSSID",
                  "StationRole",
                  "WEPEnabledInd",
                  "WEPAllowedInd",
                  "WEPOnlyTrafficInd",
                  "WEPICVErrorCount",
                  "WEPDefaultKeyLen1",
                  "WEPDefaultKeyLen2",
                  "WEPDefaultKeyLen3",
                  "WEPDefaultKeyLen4",
                  )
