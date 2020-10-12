from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VrfNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``VirtualNetworkMemberID:`` none
    |  ``attribute type:`` string
    
    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string
    
    |  ``VirtualNetworkMemberDescription:`` none
    |  ``attribute type:`` string
    
    |  ``Count:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "VirtualNetworkMemberID",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkMemberDescription",
                  "Count",
                  )

    
    
    
    
    
    