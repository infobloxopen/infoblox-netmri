from ..remote import RemoteModel


class IfWirelessSsidAuthGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDAuthTimestamp:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``SSIDAlgorithmIndex:`` none
    |  ``attribute type:`` string

    |  ``SSIDAuthEnabledInd:`` none
    |  ``attribute type:`` string

    |  ``SSIDEAPRequiredInd:`` none
    |  ``attribute type:`` string

    |  ``SSIDEAPMethod:`` none
    |  ``attribute type:`` string

    |  ``SSIDMACAuthRequiredInd:`` none
    |  ``attribute type:`` string

    |  ``SSIDMACAuthMethod:`` none
    |  ``attribute type:`` string

    |  ``SSIDDefaultVlanIndex:`` none
    |  ``attribute type:`` string

    |  ``SSIDAuthAlgorithm:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "ifWirelessSSIDAuthTimestamp",
                  "DeviceID",
                  "ifIndex",
                  "ifName",
                  "ifNameSort",
                  "SSIDAlgorithmIndex",
                  "SSIDAuthEnabledInd",
                  "SSIDEAPRequiredInd",
                  "SSIDEAPMethod",
                  "SSIDMACAuthRequiredInd",
                  "SSIDMACAuthMethod",
                  "SSIDDefaultVlanIndex",
                  "SSIDAuthAlgorithm",
                  )
