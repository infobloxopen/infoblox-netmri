from ..remote import RemoteModel


class BackgroundTasksSubtaskRemote(RemoteModel):
    """
    This table list out the subtasks of background tasks.


    |  ``background_task_id:`` The internal NetMRI identifier for background task this subtask belong to.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``detail:`` Detailed description of subtask.
    |  ``attribute type:`` string

    |  ``id:`` The internal NetMRI identifier for this subtask.
    |  ``attribute type:`` number

    |  ``name:`` The name of subtask.
    |  ``attribute type:`` string

    |  ``status:`` The status of subtask.
    |  ``attribute type:`` string

    """

    properties = ("background_task_id",
                  "created_at",
                  "updated_at",
                  "detail",
                  "id",
                  "name",
                  "status",
                  )
