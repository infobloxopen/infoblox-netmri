from ..remote import RemoteModel


class ConfigMgmtJobManagementTemplateGridRemote(RemoteModel):
    """



    |  ``template_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``run_level:`` none
    |  ``attribute type:`` string

    |  ``risk_level:`` none
    |  ``attribute type:`` string

    |  ``vendor:`` none
    |  ``attribute type:`` string

    |  ``model:`` none
    |  ``attribute type:`` string

    |  ``version:`` none
    |  ``attribute type:`` string

    |  ``device_type:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``last_run_start:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``variables_count:`` none
    |  ``attribute type:`` string

    |  ``last_run_BatchID:`` none
    |  ``attribute type:`` string

    |  ``job_specifications_count:`` none
    |  ``attribute type:`` string

    |  ``triggered_jobs_count:`` none
    |  ``attribute type:`` string

    """

    properties = ("template_id",
                  "name",
                  "run_level",
                  "risk_level",
                  "vendor",
                  "model",
                  "version",
                  "device_type",
                  "created_by",
                  "created_at",
                  "updated_by",
                  "updated_at",
                  "last_run_start",
                  "description",
                  "variables_count",
                  "last_run_BatchID",
                  "job_specifications_count",
                  "triggered_jobs_count",
                  )
