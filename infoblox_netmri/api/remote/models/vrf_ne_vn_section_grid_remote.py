from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VrfNeVnSectionGridRemote(RemoteModel):
    """
    

    
    |  ``VrfID:`` none
    |  ``attribute type:`` string
    
    |  ``VrfName:`` none
    |  ``attribute type:`` string
    
    |  ``router_count:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("VrfID",
                  "VrfName",
                  "router_count",
                  )

    
    
    
    