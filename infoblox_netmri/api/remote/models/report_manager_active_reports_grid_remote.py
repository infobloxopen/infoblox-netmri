from ..remote import RemoteModel


class ReportManagerActiveReportsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``report_run_id:`` none
    |  ``attribute type:`` string

    |  ``report_name:`` none
    |  ``attribute type:`` string

    |  ``report_type:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``column_to_sort_by:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``priority:`` none
    |  ``attribute type:`` string

    |  ``last_action_timestamp:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "report_run_id",
                  "report_name",
                  "report_type",
                  "created_by",
                  "column_to_sort_by",
                  "status",
                  "priority",
                  "last_action_timestamp",
                  )
