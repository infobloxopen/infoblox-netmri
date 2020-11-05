from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


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

    
    
    
    
    