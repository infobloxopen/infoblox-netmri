from ..remote import RemoteModel


class JobSpecsConfigManageJobManageGridRemote(RemoteModel):
    """



    |  ``job_id:`` none
    |  ``attribute type:`` string

    |  ``script_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``script_name:`` none
    |  ``attribute type:`` string

    |  ``script_risk:`` none
    |  ``attribute type:`` string

    |  ``risk_level:`` none
    |  ``attribute type:`` string

    |  ``taskflowCreate:`` none
    |  ``attribute type:`` string

    |  ``approved_by_name:`` none
    |  ``attribute type:`` string

    |  ``schedule_hash:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``last_run:`` none
    |  ``attribute type:`` string

    |  ``last_run_status:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``approved_by:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``approved_timestamp:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``last_run_BatchID:`` none
    |  ``attribute type:`` string

    |  ``config_template_id:`` none
    |  ``attribute type:`` string

    |  ``job_type:`` none
    |  ``attribute type:`` string

    """

    properties = ("job_id",
                  "script_id",
                  "name",
                  "script_name",
                  "script_risk",
                  "risk_level",
                  "taskflowCreate",
                  "approved_by_name",
                  "schedule_hash",
                  "status",
                  "last_run",
                  "last_run_status",
                  "description",
                  "approved_by",
                  "created_by",
                  "approved_timestamp",
                  "created_at",
                  "updated_at",
                  "last_run_BatchID",
                  "config_template_id",
                  "job_type",
                  )
