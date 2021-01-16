from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class EventRemote(RemoteModel):
    """
    This table list out the entries of system events occured within the NetMRI.


    |  ``EventID:`` The internal NetMRI identifier of an event.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``EventCategory:`` The category of an event.
    |  ``attribute type:`` string

    |  ``EventCategoryID:`` The internal NetMRI identifier of a category in an event.
    |  ``attribute type:`` number

    |  ``EventType:`` The type of an event.
    |  ``attribute type:`` string

    |  ``EventTimestamp:`` The date and time this record was collected.
    |  ``attribute type:`` datetime

    |  ``EventState:`` The state of an event.
    |  ``attribute type:`` string

    |  ``EventDetail:`` The detail of an event.
    |  ``attribute type:`` string

    """

    properties = ("EventID",
                  "DataSourceID",
                  "EventCategory",
                  "EventCategoryID",
                  "EventType",
                  "EventTimestamp",
                  "EventState",
                  "EventDetail",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"EventID": self.EventID})
