from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class CircuitLinkGridRemote(RemoteModel):
    """
    

    
    |  ``CLinkID:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkIndex:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkIfIndex:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkOverallState:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkDTGNumber:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkTGCNumber:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkNodeType:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkTransmissionType:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkParentID:`` none
    |  ``attribute type:`` string
    
    |  ``CLinkSwitchCode:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("CLinkID",
                  "CLinkIndex",
                  "CLinkIfIndex",
                  "CLinkOverallState",
                  "CLinkDTGNumber",
                  "CLinkTGCNumber",
                  "CLinkNodeType",
                  "CLinkTransmissionType",
                  "CLinkParentID",
                  "CLinkSwitchCode",
                  )

    
    
    
    
    
    
    
    
    
    
    