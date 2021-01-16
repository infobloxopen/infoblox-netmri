from ..remote import RemoteModel


class EventNetworkAnalysisGridRemote(RemoteModel):
    """



    |  ``EventID:`` none
    |  ``attribute type:`` string

    |  ``EventCategory:`` none
    |  ``attribute type:`` string

    |  ``EventCategoryID:`` none
    |  ``attribute type:`` string

    |  ``EventTimestamp:`` none
    |  ``attribute type:`` string

    """

    properties = ("EventID",
                  "EventCategory",
                  "EventCategoryID",
                  "EventTimestamp",
                  )
