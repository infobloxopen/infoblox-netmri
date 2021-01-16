from ..remote import RemoteModel


class PathAnalysisGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``PathAnalysisID:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    |  ``Source:`` none
    |  ``attribute type:`` string

    |  ``SourceDeviceID:`` none
    |  ``attribute type:`` string

    |  ``Destination:`` none
    |  ``attribute type:`` string

    |  ``DestinationDeviceID:`` none
    |  ``attribute type:`` string

    |  ``ErrorMsg:`` none
    |  ``attribute type:`` string

    |  ``RuleListInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "PathAnalysisID",
                  "Status",
                  "Source",
                  "SourceDeviceID",
                  "Destination",
                  "DestinationDeviceID",
                  "ErrorMsg",
                  "RuleListInd",
                  )
