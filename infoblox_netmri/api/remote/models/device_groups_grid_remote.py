from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceGroupsGridRemote(RemoteModel):
    """
    

    
    |  ``id:`` none
    |  ``attribute type:`` string
    
    |  ``device_group_id:`` none
    |  ``attribute type:`` string
    
    |  ``device_group_name:`` none
    |  ``attribute type:`` string
    
    |  ``device_count:`` none
    |  ``attribute type:`` string
    
    |  ``advanced_group_ind:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("id",
                  "device_group_id",
                  "device_group_name",
                  "device_count",
                  "advanced_group_ind",
                  )

    
    
    
    
    
    