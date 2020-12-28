from ..remote import RemoteModel


class SystemHealthSummaryRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``datasource_id:`` none
    |  ``attribute type:`` string

    |  ``timestamp:`` none
    |  ``attribute type:`` string

    |  ``category:`` none
    |  ``attribute type:`` string

    |  ``diagnostic:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``entry_type:`` none
    |  ``attribute type:`` string

    |  ``visibility:`` none
    |  ``attribute type:`` string

    |  ``message_code:`` none
    |  ``attribute type:`` string

    |  ``message:`` none
    |  ``attribute type:`` string

    |  ``silenceable_ind:`` none
    |  ``attribute type:`` string

    |  ``silenced_ind:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``subcategory:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "datasource_id",
                  "timestamp",
                  "category",
                  "diagnostic",
                  "status",
                  "entry_type",
                  "visibility",
                  "message_code",
                  "message",
                  "silenceable_ind",
                  "silenced_ind",
                  "updated_at",
                  "subcategory",
                  )
