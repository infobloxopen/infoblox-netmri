from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IssueDescRemote(RemoteModel):
    """
    Includes information about the types of issues NetMRI can raise, including title, description, and other useful data.


    |  ``IssueDescID:`` The internal NetMRI identifier for this issue description.
    |  ``attribute type:`` number

    |  ``IssueTypeID:`` The internal NetMRI identifier for this type of issue.
    |  ``attribute type:`` string

    |  ``Title:`` The descriptive name of the issue type.
    |  ``attribute type:`` string

    |  ``Description:`` A detailed description of the issue.
    |  ``attribute type:`` string

    |  ``Frequency:`` The time in seconds of how often the analysis engine checks for issues of this type.
    |  ``attribute type:`` number

    |  ``Timeout:`` The period in seconds in which the issue instance is expired if it isn't reported again.
    |  ``attribute type:`` number

    |  ``SeverityID:`` The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
    |  ``attribute type:`` number

    |  ``PriorityID:`` Not currently used.
    |  ``attribute type:`` number

    |  ``Component:`` The issue component (Devices, Configuration, VLANs, etc.).
    |  ``attribute type:`` string

    |  ``Correctness:`` The correctness contribution for this issue.
    |  ``attribute type:`` float

    |  ``Stability:`` The stability contribution for this issue.
    |  ``attribute type:`` float

    |  ``IssueType:`` The source of the issue (S = built into system, C = custom issue, P = policy violation issue, E = event analysis issue).
    |  ``attribute type:`` string

    |  ``Context:`` For internal use only.
    |  ``attribute type:`` string

    |  ``severity:`` The issue severity.
    |  ``attribute type:`` string


    """

    properties = ("IssueDescID",
                  "IssueTypeID",
                  "Title",
                  "Description",
                  "Frequency",
                  "Timeout",
                  "SeverityID",
                  "PriorityID",
                  "Component",
                  "Correctness",
                  "Stability",
                  "IssueType",
                  "Context",
                  "severity",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"IssueTypeID": self.IssueTypeID})
