from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class EventDeviceGridRemote(RemoteModel):
    """



    |  ``EventID:`` none
    |  ``attribute type:`` string

    |  ``EventTimestamp:`` none
    |  ``attribute type:`` string

    |  ``DataSourceName:`` none
    |  ``attribute type:`` string

    |  ``EventType:`` none
    |  ``attribute type:`` string

    |  ``EventDetail:`` none
    |  ``attribute type:`` string

    |  ``EventCategory:`` none
    |  ``attribute type:`` string

    |  ``EventCategoryID:`` none
    |  ``attribute type:`` string

    """

    properties = ("EventID",
                  "EventTimestamp",
                  "DataSourceName",
                  "EventType",
                  "EventDetail",
                  "EventCategory",
                  "EventCategoryID",
                  )
