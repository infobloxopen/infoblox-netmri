from ..remote import RemoteModel


class CollectionScheduleRemote(RemoteModel):
    """
    This table list out the collection schedules.


    |  ``id:`` The internal NetMRI identifier for schedule.
    |  ``attribute type:`` number

    |  ``device_id:`` The internal NetMRI identifier for device.
    |  ``attribute type:`` number

    |  ``device_group_id:`` The internal NetMRI identifier for device group.
    |  ``attribute type:`` number

    |  ``schedule:`` Schedule name.
    |  ``attribute type:`` string

    |  ``schedule_type:`` The type of schedule.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "device_id",
                  "device_group_id",
                  "schedule",
                  "schedule_type",
                  )
