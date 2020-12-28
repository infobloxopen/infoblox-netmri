from ..remote import RemoteModel


class SettingsAuthAuditLogGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``user_name:`` none
    |  ``attribute type:`` string

    |  ``event_type:`` none
    |  ``attribute type:`` string

    |  ``message:`` none
    |  ``attribute type:`` string

    |  ``field_changes:`` none
    |  ``attribute type:`` string

    |  ``field_changes_exportable:`` none
    |  ``attribute type:`` string

    |  ``client_ip:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "created_at",
                  "user_name",
                  "event_type",
                  "message",
                  "field_changes",
                  "field_changes_exportable",
                  "client_ip",
                  "DeviceID",
                  )
