from ..remote import RemoteModel


class WorkbookHistoryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``workbook_history_id:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``user_name:`` none
    |  ``attribute type:`` string

    |  ``source:`` none
    |  ``attribute type:`` string

    |  ``summary:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "workbook_history_id",
                  "created_at",
                  "user_name",
                  "source",
                  "summary",
                  )
