from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IssueListDeviceRemote(RemoteModel):
    """
    This table list out the entries of issues in the device.


    |  ``IssueTimestamp:`` The date and time this issue list device record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which issue list device information was collected.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``Count:`` The total number of issues in the list device captured within NetMRI.
    |  ``attribute type:`` number

    |  ``Adds:`` Added a new type of issue in the list device.
    |  ``attribute type:`` string

    |  ``Deletes:`` Remove a issue from the list device.
    |  ``attribute type:`` string

    |  ``Same:`` Maintain the issues as in the list device.
    |  ``attribute type:`` string

    |  ``Suppressed:``  A flag indicating whether this issue is suppressed or not.
    |  ``attribute type:`` string

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this interface.
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``TotalCount:`` The total number of issues occured in each device.
    |  ``attribute type:`` number

    |  ``Component:`` The issue component (Devices, Configuration, VLANs, etc.).
    |  ``attribute type:`` string

    |  ``SeverityID:`` The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
    |  ``attribute type:`` number

    |  ``SeverityName:`` The severity name in the issue list device.
    |  ``attribute type:`` string

    |  ``Correctness:`` The correctness contribution for this issue.
    |  ``attribute type:`` string

    |  ``Stability:`` The stability contribution for this issue.
    |  ``attribute type:`` string

    |  ``Status:`` A status of the issues in the device.
    |  ``attribute type:`` string

    """

    properties = ("IssueTimestamp",
                  "DeviceID",
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
                  "Component",
                  "SeverityID",
                  "SeverityName",
                  "Correctness",
                  "Stability",
                  "Status",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceID": self.DeviceID})
