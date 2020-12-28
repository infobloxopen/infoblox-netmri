from ..remote import RemoteModel


class BackgroundTaskRemote(RemoteModel):
    """
    This table list out the background tasks.


    |  ``id:`` The internal NetMRI identifier for this background task.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``detail:`` Detailed description of task.
    |  ``attribute type:`` string

    |  ``name:`` The name of background task.
    |  ``attribute type:`` string

    |  ``progress_value:`` The value of background task progress in percents.
    |  ``attribute type:`` number

    |  ``status:`` The status of background task.
    |  ``attribute type:`` string

    |  ``subtasks_ind:`` A flag indicating if task has subtasks.
    |  ``attribute type:`` bool

    |  ``background_tasks_subtasks:`` Method to access this task subtasks.
    |  ``attribute type:`` model

    """

    properties = ("id",
                  "created_at",
                  "updated_at",
                  "detail",
                  "name",
                  "progress_value",
                  "status",
                  "subtasks_ind",
                  "background_tasks_subtasks",
                  )
