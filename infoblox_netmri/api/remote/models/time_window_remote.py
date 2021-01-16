from ..remote import RemoteModel


class TimeWindowRemote(RemoteModel):
    """
    This table list out the entries of Time Window System.


    |  ``id:`` The internal NetMRI identifier of a time window.
    |  ``attribute type:`` number

    |  ``schedule_name:`` The schedule name of a time window.
    |  ``attribute type:`` string

    |  ``time_zone:`` The time zone of a time window.
    |  ``attribute type:`` string

    |  ``system_window_ind:`` A flag indicates whether a time zone is a system time window or not.
    |  ``attribute type:`` bool

    |  ``recur_type:`` The recurrence type of a time window.
    |  ``attribute type:`` string

    |  ``start_date:`` The starting effective date of this record.
    |  ``attribute type:`` datetime

    |  ``end_date:`` The ending effective date of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``interval:`` The time interval(minutes) of a time window.
    |  ``attribute type:`` number

    |  ``ordinal:`` The ordinal number of a time window.
    |  ``attribute type:`` number

    |  ``period_mins:`` The duration (specified in minutes) of a time window system.
    |  ``attribute type:`` number

    |  ``start_min:`` The starting time of a time window.
    |  ``attribute type:`` number

    |  ``end_min:`` The ending time of a time window.
    |  ``attribute type:`` number

    |  ``sun_start:`` The start value of a Sunday in time window.
    |  ``attribute type:`` number

    |  ``sun_end:`` The end value of a Sunday in time window.
    |  ``attribute type:`` number

    |  ``mon_start:`` The start value of a Monday in time window.
    |  ``attribute type:`` number

    |  ``mon_end:`` The end value of a Monday in time window.
    |  ``attribute type:`` number

    |  ``tue_start:`` The start value of a Tuesday in time window.
    |  ``attribute type:`` number

    |  ``tue_end:`` The end value of a Tuesday in a time window.
    |  ``attribute type:`` number

    |  ``wed_start:`` The start value of a Wednesday in time window.
    |  ``attribute type:`` number

    |  ``wed_end:`` The end value of a Wednesday in a time window.
    |  ``attribute type:`` number

    |  ``thu_start:`` The start value of a Thursday in time window.
    |  ``attribute type:`` number

    |  ``thu_end:`` The end value of a Thursday in time window.
    |  ``attribute type:`` number

    |  ``fri_start:`` The start value of a Friday in time window.
    |  ``attribute type:`` number

    |  ``fri_end:`` The end value of a Friday in time window.
    |  ``attribute type:`` number

    |  ``sat_start:`` The start value of a Saturday in time window.
    |  ``attribute type:`` number

    |  ``sat_end:`` The end value of a Saturday in time window.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "schedule_name",
                  "time_zone",
                  "system_window_ind",
                  "recur_type",
                  "start_date",
                  "end_date",
                  "interval",
                  "ordinal",
                  "period_mins",
                  "start_min",
                  "end_min",
                  "sun_start",
                  "sun_end",
                  "mon_start",
                  "mon_end",
                  "tue_start",
                  "tue_end",
                  "wed_start",
                  "wed_end",
                  "thu_start",
                  "thu_end",
                  "fri_start",
                  "fri_end",
                  "sat_start",
                  "sat_end",
                  "created_at",
                  "updated_at",
                  )
