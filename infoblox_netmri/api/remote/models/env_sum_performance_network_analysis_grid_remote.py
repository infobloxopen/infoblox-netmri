from ..remote import RemoteModel


class EnvSumPerformanceNetworkAnalysisGridRemote(RemoteModel):
    """



    |  ``DevEnvMonId:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``DevEnvMonDescr:`` none
    |  ``attribute type:`` string

    |  ``DevEnvMonType:`` none
    |  ``attribute type:`` string

    |  ``DevEnvMonStatusMessage:`` none
    |  ``attribute type:`` string

    |  ``DevEnvMonStatusAlert:`` none
    |  ``attribute type:`` string

    |  ``DevEnvMonTimestamp:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    """

    properties = ("DevEnvMonId",
                  "DeviceID",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceIPNumeric",
                  "DeviceType",
                  "DeviceVendor",
                  "DevEnvMonDescr",
                  "DevEnvMonType",
                  "DevEnvMonStatusMessage",
                  "DevEnvMonStatusAlert",
                  "DevEnvMonTimestamp",
                  "DeviceAssurance",
                  )
