from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VrfNeVnSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  )
