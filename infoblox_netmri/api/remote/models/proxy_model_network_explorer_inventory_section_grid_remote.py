from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class ProxyModelNetworkExplorerInventorySectionGridRemote(RemoteModel):
    """
    

    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``model_label:`` none
    |  ``attribute type:`` string
    
    |  ``model_count:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceModel:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("DeviceID",
                  "model_label",
                  "model_count",
                  "DeviceModel",
                  "DeviceVendor",
                  )

    
    
    
    
    
    