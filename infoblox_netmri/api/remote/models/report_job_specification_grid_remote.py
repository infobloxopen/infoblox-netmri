from ..remote import RemoteModel


class ReportJobSpecificationGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``reportname:`` none
    |  ``attribute type:`` string

    |  ``file_name:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``schedule_json:`` none
    |  ``attribute type:`` string

    |  ``schedule:`` none
    |  ``attribute type:`` string

    |  ``recipients:`` none
    |  ``attribute type:`` string

    |  ``last_run:`` none
    |  ``attribute type:`` string

    |  ``is_removed:`` none
    |  ``attribute type:`` string

    |  ``origid:`` none
    |  ``attribute type:`` string

    |  ``auth_users:`` none
    |  ``attribute type:`` string

    |  ``report_id:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "reportname",
                  "file_name",
                  "created_by",
                  "schedule_json",
                  "schedule",
                  "recipients",
                  "last_run",
                  "is_removed",
                  "origid",
                  "auth_users",
                  "report_id",
                  )
