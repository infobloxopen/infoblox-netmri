from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class PortListGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``Protocol:`` none
    |  ``attribute type:`` string
    
    |  ``Port:`` none
    |  ``attribute type:`` string
    
    |  ``Service:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "Protocol",
                  "Port",
                  "Service",
                  )

    
    
    
    
    