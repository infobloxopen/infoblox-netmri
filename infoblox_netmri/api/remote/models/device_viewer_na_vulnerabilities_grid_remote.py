from ..remote import RemoteModel


class DeviceViewerNaVulnerabilitiesGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    |  ``SeverityName:`` none
    |  ``attribute type:`` string

    |  ``SeveritySort:`` none
    |  ``attribute type:`` string

    |  ``SeverityID:`` none
    |  ``attribute type:`` string

    |  ``CVESeverity:`` none
    |  ``attribute type:`` string

    |  ``CVEID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``Timestamp:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Name:`` none
    |  ``attribute type:`` string

    |  ``Summary:`` none
    |  ``attribute type:`` string

    |  ``StatusInd:`` none
    |  ``attribute type:`` string

    |  ``VulnerabilityID:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "Status",
                  "SeverityName",
                  "SeveritySort",
                  "SeverityID",
                  "CVESeverity",
                  "CVEID",
                  "DeviceID",
                  "Timestamp",
                  "Network",
                  "Name",
                  "Summary",
                  "StatusInd",
                  "VulnerabilityID",
                  )
