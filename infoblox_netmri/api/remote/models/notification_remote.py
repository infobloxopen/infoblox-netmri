from ..remote import RemoteModel


class NotificationRemote(RemoteModel):
    """
    Configurable notifications on issues, etc.


    |  ``id:`` The internal NetMRI identifier for the notification.
    |  ``attribute type:`` number

    |  ``auth_user_id:`` User ID of the creator.
    |  ``attribute type:`` number

    |  ``category:`` A category of the notification. Possible values are 'issue','change','job','systemalert'.
    |  ``attribute type:`` string

    |  ``delivery_method:`` Delivery method of the notification. Possible values are 'email', 'syslog', 'snmp'.
    |  ``attribute type:`` string

    |  ``mime:`` Message MIME type. Possible values are 'html' or 'text'.
    |  ``attribute type:`` string

    |  ``subject:`` Subject of the notification e-mail.
    |  ``attribute type:`` string

    |  ``message_template:`` Notification message template.
    |  ``attribute type:`` string

    |  ``details_template:`` Notification details template.
    |  ``attribute type:`` string

    |  ``to:`` Notification e-mail 'To:' field.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``from:`` Notification e-mail 'from:' field.
    |  ``attribute type:`` string

    |  ``from_name:`` Name for the 'from:' field.
    |  ``attribute type:`` string

    |  ``severity:`` Severity level from 1 to 3.
    |  ``attribute type:`` number

    |  ``all_in_category_ind:`` Notify for all in the category.
    |  ``attribute type:`` bool

    |  ``all_device_groups_ind:`` Do not restrict notification to particular device groups.
    |  ``attribute type:`` bool

    |  ``all_interface_groups_ind:`` Do not restrict notification to particular interface groups.
    |  ``attribute type:`` bool

    |  ``time_window_id:`` Time window id.
    |  ``attribute type:`` number

    |  ``event_type:`` List of events that we subscribe to. Default is all events.
    |  ``attribute type:`` string

    |  ``send_clearing_ind:`` Whether to send a notification on issue clearing.
    |  ``attribute type:`` bool

    |  ``cron:`` Schedule for summary notifications in cron format.
    |  ``attribute type:`` string

    |  ``last_run:`` Last run.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "auth_user_id",
                  "category",
                  "delivery_method",
                  "mime",
                  "subject",
                  "message_template",
                  "details_template",
                  "to",
                  "created_at",
                  "updated_at",
                  "from",
                  "from_name",
                  "severity",
                  "all_in_category_ind",
                  "all_device_groups_ind",
                  "all_interface_groups_ind",
                  "time_window_id",
                  "event_type",
                  "send_clearing_ind",
                  "cron",
                  "last_run",
                  )
