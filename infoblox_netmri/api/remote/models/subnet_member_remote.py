from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SubnetMemberRemote(RemoteModel):
    """
    Members of subnets.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device associated with this subnet membership.
    |  ``attribute type:`` number

    |  ``IfAddrID:`` The internal NetMRI identifier for the interface address associated with this subnet membership, if available.
    |  ``attribute type:`` number

    |  ``SubnetID:`` The internal NetMRI identifier for the subnet associated with this subnet membership.
    |  ``attribute type:`` number

    |  ``SubnetMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SubnetMemberEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SubnetMemberID:`` The internal NetMRI identifier for this subnet membership.
    |  ``attribute type:`` number

    |  ``SubnetMemberSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``SubnetMemberStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``SubnetMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime





    |  ``AciBdID:`` ID of ACI bridge domain subnet member is assigned to
    |  ``attribute type:`` number

    |  ``AciEpgID:`` ID of ACI EPG subnet member is assigned to
    |  ``attribute type:`` number

    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "IfAddrID",
                  "SubnetID",
                  "SubnetMemberChangedCols",
                  "SubnetMemberEndTime",
                  "SubnetMemberID",
                  "SubnetMemberSource",
                  "SubnetMemberStartTime",
                  "SubnetMemberTimestamp",
                  "AciBdID",
                  "AciEpgID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"SubnetMemberID": self.SubnetMemberID})

    @property
    @check_api_availability
    def device(self):
        """
        The device associated with this subnet membership.
        ``attribute type:`` model
        """
        return self.broker.device(**{"SubnetMemberID": self.SubnetMemberID})

    @property
    @check_api_availability
    def subnet(self):
        """
        Returns the associated Subnet object for this subnet member.
        ``attribute type:`` model
        """
        return self.broker.subnet(**{"SubnetMemberID": self.SubnetMemberID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device associated with this subnet membership.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"SubnetMemberID": self.SubnetMemberID})
