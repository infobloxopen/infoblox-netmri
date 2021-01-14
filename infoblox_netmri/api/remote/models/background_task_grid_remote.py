from ..remote import RemoteModel


class BackgroundTaskGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``progress_value:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``detail:`` none
    |  ``attribute type:`` string

    |  ``subtasks_ind:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "progress_value",
                  "status",
                  "detail",
                  "subtasks_ind",
                  "created_at",
                  "updated_at",
                  )
