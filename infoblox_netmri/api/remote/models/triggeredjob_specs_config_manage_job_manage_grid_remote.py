from ..remote import RemoteModel


class TriggeredjobSpecsConfigManageJobManageGridRemote(RemoteModel):
    """



    |  ``job_id:`` none
    |  ``attribute type:`` string

    |  ``script_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``script_name:`` none
    |  ``attribute type:`` string

    |  ``script_risk:`` none
    |  ``attribute type:`` string

    |  ``risk_level:`` none
    |  ``attribute type:`` string

    |  ``enabled:`` none
    |  ``attribute type:`` string

    |  ``active_window:`` none
    |  ``attribute type:`` string

    |  ``cron:`` none
    |  ``attribute type:`` string

    |  ``source:`` none
    |  ``attribute type:`` string

    |  ``trigger_event:`` none
    |  ``attribute type:`` string

    |  ``device_group:`` none
    |  ``attribute type:`` string

    |  ``action_auto:`` none
    |  ``attribute type:`` string

    |  ``action_preapprove:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``last_run:`` none
    |  ``attribute type:`` string

    |  ``job_type:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    """

    properties = ("job_id",
                  "script_id",
                  "name",
                  "description",
                  "script_name",
                  "script_risk",
                  "risk_level",
                  "enabled",
                  "active_window",
                  "cron",
                  "source",
                  "trigger_event",
                  "device_group",
                  "action_auto",
                  "action_preapprove",
                  "created_at",
                  "updated_at",
                  "last_run",
                  "job_type",
                  "created_by",
                  "updated_by",
                  )
