from ..remote import RemoteModel


class IssueSummaryByTypeNetworkAnalysisExt3GridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``SeverityName:`` none
    |  ``attribute type:`` string

    |  ``SeverityID:`` none
    |  ``attribute type:`` string

    |  ``Timestamp:`` none
    |  ``attribute type:`` string

    |  ``EndTime:`` none
    |  ``attribute type:`` string

    |  ``Title:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    |  ``Component:`` none
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

    |  ``Description:`` none
    |  ``attribute type:`` string

    |  ``Stability:`` none
    |  ``attribute type:`` string

    |  ``Correctness:`` none
    |  ``attribute type:`` string

    |  ``IssueTypeID:`` none
    |  ``attribute type:`` string

    |  ``FirstSeen:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "SeverityName",
                  "SeverityID",
                  "Timestamp",
                  "EndTime",
                  "Title",
                  "Status",
                  "Component",
                  "Count",
                  "Adds",
                  "Same",
                  "Deletes",
                  "Suppressed",
                  "Description",
                  "Stability",
                  "Correctness",
                  "IssueTypeID",
                  "FirstSeen",
                  )
