from ..remote import RemoteModel


class ReportJobSpecificationRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``report_id:`` none
    |  ``attribute type:`` string

    |  ``schedule:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``last_run:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``schedule_json:`` none
    |  ``attribute type:`` string

    |  ``is_scheduled:`` none
    |  ``attribute type:`` string

    |  ``content_type:`` none
    |  ``attribute type:`` string

    |  ``recipients:`` none
    |  ``attribute type:`` string

    |  ``auth_user_id:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "description",
                  "report_id",
                  "schedule",
                  "created_by",
                  "last_run",
                  "created_at",
                  "updated_at",
                  "schedule_json",
                  "is_scheduled",
                  "content_type",
                  "recipients",
                  "auth_user_id",
                  )
