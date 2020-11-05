from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceFilterStatRemote(RemoteModel):
    """
    

    
    |  ``DeviceFilterStatsID:`` none
    |  ``attribute type:`` string
    
    |  ``DataSourceID:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceFilterID:`` none
    |  ``attribute type:`` string
    
    |  ``Timestamp:`` none
    |  ``attribute type:`` string
    
    |  ``HitCount:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("DeviceFilterStatsID",
                  "DataSourceID",
                  "DeviceID",
                  "DeviceFilterID",
                  "Timestamp",
                  "HitCount",
                  )

    
    
    
    
    
    
    