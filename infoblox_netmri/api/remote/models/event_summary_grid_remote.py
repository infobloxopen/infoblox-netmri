from ..remote import RemoteModel


class EventSummaryGridRemote(RemoteModel):
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
