from ..remote import RemoteModel


class IssueSummaryByDeviceNetworkAnalysisGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``SeverityName:`` none
    |  ``attribute type:`` string

    |  ``SeverityID:`` none
    |  ``attribute type:`` string

    |  ``IPAddress:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``Timestamp:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    |  ``Count:`` none
    |  ``attribute type:`` string

    |  ``Adds:`` none
    |  ``attribute type:`` string

    |  ``Same:`` none
    |  ``attribute type:`` string

    |  ``Deletes:`` none
    |  ``attribute type:`` string

    |  ``Suppressed:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "SeverityName",
                  "SeverityID",
                  "IPAddress",
                  "Network",
                  "VirtualNetworkID",
                  "DeviceID",
                  "Timestamp",
                  "DeviceName",
                  "DeviceType",
                  "DeviceAssurance",
                  "Status",
                  "Count",
                  "Adds",
                  "Same",
                  "Deletes",
                  "Suppressed",
                  "DeviceIPNumeric",
                  )
