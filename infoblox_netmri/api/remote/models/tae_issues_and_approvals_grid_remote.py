from ..remote import RemoteModel


class TaeIssuesAndApprovalsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``Time:`` none
    |  ``attribute type:`` string

    |  ``Type:`` none
    |  ``attribute type:`` string

    |  ``Severity:`` none
    |  ``attribute type:`` string

    |  ``SeverityID:`` none
    |  ``attribute type:`` string

    |  ``Name:`` none
    |  ``attribute type:`` string

    |  ``DeviceNumber:`` none
    |  ``attribute type:`` string

    |  ``Action:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "Time",
                  "Type",
                  "Severity",
                  "SeverityID",
                  "Name",
                  "DeviceNumber",
                  "Action",
                  )
