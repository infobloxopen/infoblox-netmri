from ..remote import RemoteModel


class JobManagementScriptsGridRemote(RemoteModel):
    """



    |  ``script_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``language:`` none
    |  ``attribute type:`` string

    |  ``run_level:`` none
    |  ``attribute type:`` string

    |  ``risk_level:`` none
    |  ``attribute type:`` string

    |  ``category:`` none
    |  ``attribute type:`` string

    |  ``taskflow:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``last_run_start:`` none
    |  ``attribute type:`` string

    |  ``last_run_BatchID:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``job_specification_ids:`` none
    |  ``attribute type:`` string

    |  ``job_specifications_count:`` none
    |  ``attribute type:`` string

    |  ``triggered_jobs_count:`` none
    |  ``attribute type:`` string

    |  ``visible:`` none
    |  ``attribute type:`` string

    """

    properties = ("script_id",
                  "name",
                  "language",
                  "run_level",
                  "risk_level",
                  "category",
                  "taskflow",
                  "created_by",
                  "updated_by",
                  "created_at",
                  "updated_at",
                  "last_run_start",
                  "last_run_BatchID",
                  "description",
                  "job_specification_ids",
                  "job_specifications_count",
                  "triggered_jobs_count",
                  "visible",
                  )
