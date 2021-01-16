from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IssueDetailRemote(RemoteModel):
    """
    The issues NetMRI has identified on the network. This includes the common issue fields described below, but not fields specific to each issue type.



    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that raised this issue.
    |  ``attribute type:`` number

    |  ``IssueID:`` The internal NetMRI identifier for this issue instance.
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``IssueTypeID:`` An internal NetMRI identifier for the type of this issue.
    |  ``attribute type:`` string

    |  ``DetailID:`` A unique identifier for this issue instance.
    |  ``attribute type:`` string


    |  ``DeviceID:`` The internal NetMRI identifier for the device to which this issue applies.
    |  ``attribute type:`` number


    |  ``InterfaceID:`` The internal NetMRI identifier for the interface to which this issue applies, if relevant.
    |  ``attribute type:`` number


    |  ``VlanID:`` The internal NetMRI identifier of the VLAN to which this issue applies, if relevant.
    |  ``attribute type:`` number


    |  ``SubnetID:`` The internal NetMRI identifier for the subnet to which this issue applies, if relevant.
    |  ``attribute type:`` number


    |  ``IprgID:`` The internal NetMRI identifier for the HSRP or VRRP group to which this issue applies, if relevant.
    |  ``attribute type:`` number

    |  ``BatchID:`` The internal NetMRI identifier for the job execution batch to which this issue applies, if relevant.
    |  ``attribute type:`` number

    |  ``AltDeviceID:`` The internal NetMRI identifier of the alternate device (such as a neighbor) involved in this issue, if relevant.
    |  ``attribute type:`` number


    |  ``Criteria:`` The criteria value for this issue at the time it was raised.
    |  ``attribute type:`` string

    |  ``IssueValue:`` The meaning of this field varies based upon the specific issue.
    |  ``attribute type:`` string

    |  ``Component:`` The issue component (Devices, Configuration, VLANs, etc.).
    |  ``attribute type:`` string

    |  ``SeverityID:`` The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
    |  ``attribute type:`` number

    |  ``Correctness:`` The correctness contribution for this issue.
    |  ``attribute type:`` float

    |  ``Stability:`` The stability contribution for this issue.
    |  ``attribute type:`` float

    |  ``SuppressedInd:`` A flag indicating whether this issue is suppressed or not.
    |  ``attribute type:`` bool


    |  ``StartTime:`` The date/time this issue instance was raised.
    |  ``attribute type:`` datetime

    |  ``title:`` The descriptive title for this type of issue.
    |  ``attribute type:`` string

    |  ``severity:`` The issue severity.
    |  ``attribute type:`` string


    """

    properties = ("DataSourceID",
                  "IssueID",
                  "StartTime",
                  "EndTime",
                  "ChangedCols",
                  "Timestamp",
                  "IssueTypeID",
                  "DetailID",
                  "DeviceID",
                  "InterfaceID",
                  "VlanID",
                  "SubnetID",
                  "IprgID",
                  "BatchID",
                  "AltDeviceID",
                  "Criteria",
                  "IssueValue",
                  "Component",
                  "SeverityID",
                  "Correctness",
                  "Stability",
                  "SuppressedInd",
                  "StartTime",
                  "title",
                  "severity",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that raised this issue.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def device(self):
        """
        The device to which this issue applies.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface to which this issue applies, if relevant.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The VLAN to which this issue applies, if relevant.
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def subnet(self):
        """
        The subnet to which this issue applies, if relevant.
        ``attribute type:`` model
        """
        return self.broker.subnet(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def iprg(self):
        """
        The HSRP or VRRP group to which this issue applies, if relevant.
        ``attribute type:`` model
        """
        return self.broker.iprg(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def alternate_device(self):
        """
        The alternate device (such as a neighbor) involved in this issue, if relevant.
        ``attribute type:`` model
        """
        return self.broker.alternate_device(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def issue_desc(self):
        """
        Information such as title and description, that depends only on the issue type, and does not change with each issue instance.
        ``attribute type:`` model
        """
        return self.broker.issue_desc(**{"IssueID": self.IssueID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device to which this issue applies.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IssueID": self.IssueID})
