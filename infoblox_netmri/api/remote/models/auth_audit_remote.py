from ..remote import RemoteModel


class AuthAuditRemote(RemoteModel):
    """
    The user audit log information defined within NetMRI.


    |  ``id:`` The internal NetMRI identifier of this user audit log information.
    |  ``attribute type:`` number

    |  ``datasource_id:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``date_time:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``client_ip:`` The IP address of the client defined within NetMRI.
    |  ``attribute type:`` string

    |  ``operation:`` The operation done is defined in NetMRI.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``record_id:`` The internal NetMRI identifier of the record.
    |  ``attribute type:`` number

    |  ``message:`` The audit log entry is defined as a message within NetMRI.
    |  ``attribute type:`` string

    |  ``field_changes:`` It describes the audit field changes in NetMRI.
    |  ``attribute type:`` string

    |  ``user_name:`` The username portion of the User Audit Log.
    |  ``attribute type:`` string

    |  ``event_type:`` The type of events occurs in the User Audit section.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which audit log information entry was collected.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "datasource_id",
                  "date_time",
                  "client_ip",
                  "operation",
                  "created_at",
                  "updated_at",
                  "record_id",
                  "message",
                  "field_changes",
                  "user_name",
                  "event_type",
                  "DeviceID",
                  )
