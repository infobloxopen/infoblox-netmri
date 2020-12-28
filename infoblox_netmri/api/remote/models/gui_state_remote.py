from ..remote import RemoteModel


class GuiStateRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``object_name:`` none
    |  ``attribute type:`` string

    |  ``view_name:`` none
    |  ``attribute type:`` string

    |  ``auth_user_id:`` none
    |  ``attribute type:`` string

    |  ``object_state:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``shared:`` none
    |  ``attribute type:`` string

    |  ``desc:`` none
    |  ``attribute type:`` string

    |  ``default:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "object_name",
                  "view_name",
                  "auth_user_id",
                  "object_state",
                  "created_at",
                  "updated_at",
                  "shared",
                  "desc",
                  "default",
                  )
