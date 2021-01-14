from ..remote import RemoteModel


class TaeJobLogViewerGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``start_time:`` none
    |  ``attribute type:`` string

    |  ``job_id:`` none
    |  ``attribute type:`` string

    |  ``job_name:`` none
    |  ``attribute type:`` string

    |  ``approved_by:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``devices_count:`` none
    |  ``attribute type:`` string

    |  ``first_job_details_id:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "start_time",
                  "job_id",
                  "job_name",
                  "approved_by",
                  "created_by",
                  "status",
                  "devices_count",
                  "first_job_details_id",
                  )
