from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class InfraDeviceNetworkExplorerInventorySummaryGridRemote(RemoteModel):
    """
    

    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``Collector:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string
    
    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string
    
    |  ``Network:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceName:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceType:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceModel:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string
    
    |  ``AssetType:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("DeviceID",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceAssurance",
                  "AssetType",
                  )

    
    
    
    
    
    
    
    
    
    
    
    
    