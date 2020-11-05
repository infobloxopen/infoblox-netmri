from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class ProxyOsNetworkExplorerInventorySectionGridRemote(RemoteModel):
    """
    

    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``os_label:`` none
    |  ``attribute type:`` string
    
    |  ``os_count:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("DeviceID",
                  "os_label",
                  "os_count",
                  "DeviceVersion",
                  "DeviceVendor",
                  )

    
    
    
    
    
    