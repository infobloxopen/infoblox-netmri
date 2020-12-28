from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DataCategoryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryID:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryName:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryDescription:`` none
    |  ``attribute type:`` string

    |  ``ArchiveAgeDays:`` none
    |  ``attribute type:`` string

    |  ``MaxDataAgeDays:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DataCategoryID",
                  "DataCategoryName",
                  "DataCategoryDescription",
                  "ArchiveAgeDays",
                  "MaxDataAgeDays",
                  )
