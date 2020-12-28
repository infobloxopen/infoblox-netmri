from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IssueListRemote(RemoteModel):
    """
    This table list out the entries of Issues captured by the NetMRI.


    |  ``IssueTimestamp:`` The date and time of Issues was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``GroupSetID:`` The internal NetMRI identifier of the Group.
    |  ``attribute type:`` number

    |  ``IssueTypeID:`` The internal NetMRI identifier of the Issue Type.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``Count:`` The total number of issues captured within NetMRI.
    |  ``attribute type:`` number

    |  ``Adds:`` Added a new type of issue in the list.
    |  ``attribute type:`` string

    |  ``Deletes:`` Remove a issue from the list.
    |  ``attribute type:`` string

    |  ``Same:`` Maintain the issues as in the list.
    |  ``attribute type:`` string

    |  ``Suppressed:`` A flag indicates whether a issue is suppressed or not.
    |  ``attribute type:`` string

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this NetMRI.
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``TotalCount:`` The total number of issues in the list.
    |  ``attribute type:`` number

    |  ``DimDate:`` The dimensional date and time was found.
    |  ``attribute type:`` datetime

    |  ``ShortDate:`` The short date and time defined in the device statistics.
    |  ``attribute type:`` datetime

    |  ``UnixDimDate:`` The unique dimensional date and time od device statistics.
    |  ``attribute type:`` datetime

    |  ``Component:`` The issue component (Device,Configuration,VLANs,etc.)
    |  ``attribute type:`` string

    |  ``SeverityID:`` The issue severity ID (1 = Error , 2 = Warning ,3 = Info).Useful for sorting.
    |  ``attribute type:`` number

    |  ``SeverityName:`` The severity name in the issue list.
    |  ``attribute type:`` string

    |  ``Correctness:`` The correctness contribution for this device.
    |  ``attribute type:`` string

    |  ``Stability:`` The stability contribution for this device.
    |  ``attribute type:`` string

    |  ``Status:`` Status of the issue.
    |  ``attribute type:`` string

    |  ``Title:`` The descriptive name of the issue.
    |  ``attribute type:`` string

    |  ``PriorityID:`` Not currently used.
    |  ``attribute type:`` number

    """

    properties = ("IssueTimestamp",
                  "GroupSetID",
                  "IssueTypeID",
                  "DataSourceID",
                  "Count",
                  "Adds",
                  "Deletes",
                  "Same",
                  "Suppressed",
                  "FirstSeen",
                  "Timestamp",
                  "EndTime",
                  "TotalCount",
                  "DimDate",
                  "ShortDate",
                  "UnixDimDate",
                  "Component",
                  "SeverityID",
                  "SeverityName",
                  "Correctness",
                  "Stability",
                  "Status",
                  "Title",
                  "PriorityID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"GroupSetID": self.GroupSetID})
