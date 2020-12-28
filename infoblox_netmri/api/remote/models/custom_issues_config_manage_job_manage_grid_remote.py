from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class CustomIssuesConfigManageJobManageGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``IssueAdHocID:`` none
    |  ``attribute type:`` string

    |  ``Title:`` none
    |  ``attribute type:`` string

    |  ``IssueTypeID:`` none
    |  ``attribute type:`` string

    |  ``Component:`` none
    |  ``attribute type:`` string

    |  ``Correctness:`` none
    |  ``attribute type:`` string

    |  ``Stability:`` none
    |  ``attribute type:`` string

    |  ``Description:`` none
    |  ``attribute type:`` string

    |  ``IssueSource:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "IssueAdHocID",
                  "Title",
                  "IssueTypeID",
                  "Component",
                  "Correctness",
                  "Stability",
                  "Description",
                  "IssueSource",
                  )
