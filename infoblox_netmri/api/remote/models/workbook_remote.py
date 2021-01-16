from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class WorkbookRemote(RemoteModel):
    """
    A collection of user-selected Device Rule List


    |  ``id:`` The identifier for Workbook.
    |  ``attribute type:`` number

    |  ``name:`` The Workbook name specified by user.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the Workbook was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the Workbook was last modified in NetMRI
    |  ``attribute type:`` datetime

    |  ``comments:`` The comment associated to the Workbook.
    |  ``attribute type:`` string

    |  ``created_by:`` Indicates by whom Workbook was created.
    |  ``attribute type:`` string

    |  ``updated_by:`` Indicates by whom Workbook was updated.
    |  ``attribute type:`` string

    |  ``active_set_ind:`` A flag indicating a temporary workbook.
    |  ``attribute type:`` bool


    """

    properties = ("id",
                  "name",
                  "created_at",
                  "updated_at",
                  "comments",
                  "created_by",
                  "updated_by",
                  "active_set_ind",
                  )

    @property
    @check_api_availability
    def device_filter_sets(self):
        """
        The rule lists included in the workbook
        ``attribute type:`` model
        """
        return self.broker.device_filter_sets(**{"id": self.id})
