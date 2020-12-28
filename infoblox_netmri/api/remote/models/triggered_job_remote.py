from ..remote import RemoteModel


class TriggeredJobRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``enabled:`` none
    |  ``attribute type:`` string

    |  ``script_id:`` none
    |  ``attribute type:`` string

    |  ``source:`` none
    |  ``attribute type:`` string

    |  ``action_auto:`` none
    |  ``attribute type:`` string

    |  ``cron:`` none
    |  ``attribute type:`` string

    |  ``action_preapprove:`` none
    |  ``attribute type:`` string

    |  ``last_run:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``config_template_id:`` none
    |  ``attribute type:`` string

    |  ``job_type:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "description",
                  "enabled",
                  "script_id",
                  "source",
                  "action_auto",
                  "cron",
                  "action_preapprove",
                  "last_run",
                  "created_at",
                  "updated_at",
                  "config_template_id",
                  "job_type",
                  "created_by",
                  "updated_by",
                  )
