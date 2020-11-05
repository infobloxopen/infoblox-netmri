from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class ConfigErrorGridRemote(RemoteModel):
    """
    

    
    |  ``Timestamp:`` none
    |  ``attribute type:`` string
    
    |  ``ConfigErrorID:`` none
    |  ``attribute type:`` string
    
    |  ``DeviceID:`` none
    |  ``attribute type:`` string
    
    |  ``ErrMsg:`` none
    |  ``attribute type:`` string
    
    """

    properties = ("Timestamp",
                  "ConfigErrorID",
                  "DeviceID",
                  "ErrMsg",
                  )

    
    
    
    
    