from ..remote import RemoteModel


class JobHandlerRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``unit_id:`` none
    |  ``attribute type:`` string

    |  ``broker_user_name:`` none
    |  ``attribute type:`` string

    |  ``broker_password_secure:`` none
    |  ``attribute type:`` string

    |  ``broker_password_version:`` none
    |  ``attribute type:`` string

    |  ``broker_exchange:`` none
    |  ``attribute type:`` string

    |  ``broker_queue:`` none
    |  ``attribute type:`` string

    |  ``broker_admin_queue:`` none
    |  ``attribute type:`` string

    |  ``concurrent_limit:`` none
    |  ``attribute type:`` string

    |  ``current_bid:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``last_status_at:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "created_by",
                  "unit_id",
                  "broker_user_name",
                  "broker_password_secure",
                  "broker_password_version",
                  "broker_exchange",
                  "broker_queue",
                  "broker_admin_queue",
                  "concurrent_limit",
                  "current_bid",
                  "status",
                  "last_status_at",
                  "created_at",
                  "updated_at",
                  )
