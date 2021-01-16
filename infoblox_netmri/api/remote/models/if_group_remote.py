from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfGroupRemote(RemoteModel):
    """
    Interface Group Information gathered by NetMRI.


    |  ``GroupID:`` The internal NetMRI identifier for the interface group.
    |  ``attribute type:`` number

    |  ``IfGroupID:`` The internal NetMRI identifier for the interface group.
    |  ``attribute type:`` number

    |  ``ifGroupStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ifGroupEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifGroupChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifGroupTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``GroupName:`` The interface group name.
    |  ``attribute type:`` string

    |  ``Criteria:`` The interface group criteria, which define the group memberships.
    |  ``attribute type:`` string

    |  ``Rank:`` The Group rank.
    |  ``attribute type:`` string

    |  ``SNMPPolling:`` The SNMP Polling indicator of the Group.
    |  ``attribute type:`` string

    |  ``FlowCollection:`` The Flow Collection indicator of the Group.
    |  ``attribute type:`` string

    |  ``PerfFrequency:`` The Group performance data gathering frequency indicator.
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``MemberCount:`` The number of interfaces in this interface group.
    |  ``attribute type:`` number

    """

    properties = ("GroupID",
                  "IfGroupID",
                  "ifGroupStartTime",
                  "ifGroupEndTime",
                  "ifGroupChangedCols",
                  "ifGroupTimestamp",
                  "DataSourceID",
                  "GroupName",
                  "Criteria",
                  "Rank",
                  "SNMPPolling",
                  "FlowCollection",
                  "PerfFrequency",
                  "Timestamp",
                  "MemberCount",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfGroupID": self.IfGroupID})
