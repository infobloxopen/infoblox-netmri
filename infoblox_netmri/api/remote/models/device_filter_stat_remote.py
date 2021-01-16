from ..remote import RemoteModel


class DeviceFilterStatRemote(RemoteModel):
    """



    |  ``DeviceFilterStatsID:`` none
    |  ``attribute type:`` string

    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceFilterID:`` none
    |  ``attribute type:`` string

    |  ``Timestamp:`` none
    |  ``attribute type:`` string

    |  ``HitCount:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceFilterStatsID",
                  "DataSourceID",
                  "DeviceID",
                  "DeviceFilterID",
                  "Timestamp",
                  "HitCount",
                  )
