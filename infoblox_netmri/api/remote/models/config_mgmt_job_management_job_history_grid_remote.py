from ..remote import RemoteModel


class ConfigMgmtJobManagementJobHistoryGridRemote(RemoteModel):
    """



    |  ``Status:`` none
    |  ``attribute type:`` string

    |  ``BatchID:`` none
    |  ``attribute type:`` string

    |  ``Name:`` none
    |  ``attribute type:`` string

    |  ``Script:`` none
    |  ``attribute type:`` string

    |  ``IsJobDeleted:`` none
    |  ``attribute type:`` string

    |  ``Initiator:`` none
    |  ``attribute type:`` string

    |  ``Approver:`` none
    |  ``attribute type:`` string

    |  ``StartTime:`` none
    |  ``attribute type:`` string

    |  ``EndTime:`` none
    |  ``attribute type:`` string

    |  ``JobCount:`` none
    |  ``attribute type:`` string

    |  ``MinJobID:`` none
    |  ``attribute type:`` string

    |  ``OkCount:`` none
    |  ``attribute type:`` string

    |  ``ErrorCount:`` none
    |  ``attribute type:`` string

    |  ``PendingCount:`` none
    |  ``attribute type:`` string

    |  ``OtherCount:`` none
    |  ``attribute type:`` string

    |  ``SummaryCount:`` none
    |  ``attribute type:`` string

    |  ``taskflowCreate:`` none
    |  ``attribute type:`` string

    """

    properties = ("Status",
                  "BatchID",
                  "Name",
                  "Script",
                  "IsJobDeleted",
                  "Initiator",
                  "Approver",
                  "StartTime",
                  "EndTime",
                  "JobCount",
                  "MinJobID",
                  "OkCount",
                  "ErrorCount",
                  "PendingCount",
                  "OtherCount",
                  "SummaryCount",
                  "taskflowCreate",
                  )
