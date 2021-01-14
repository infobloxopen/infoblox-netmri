from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfGroupMemberRemote(RemoteModel):
    """
    Interface Group Member information gathered by NetMRI.


    |  ``IfGroupMemberID:`` The internal NetMRI identifier for this interface group membership record.
    |  ``attribute type:`` number

    |  ``GroupID:`` The internal NetMRI identifier for the interface group.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this data was collected.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The internal NetMRI identifier for the device from which this data was collected.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The Interface ID.
    |  ``attribute type:`` number

    |  ``ifGroupMemberStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ifGroupMemberEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifGroupMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifGroupMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number



    |  ``IfGroupID:`` The internal NetMRI identifier for the interface group.
    |  ``attribute type:`` number

    """

    properties = ("IfGroupMemberID",
                  "GroupID",
                  "DeviceID",
                  "ifIndex",
                  "InterfaceID",
                  "ifGroupMemberStartTime",
                  "ifGroupMemberEndTime",
                  "ifGroupMemberChangedCols",
                  "ifGroupMemberTimestamp",
                  "DataSourceID",
                  "IfGroupID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfGroupMemberID": self.IfGroupMemberID})

    @property
    @check_api_availability
    def interface(self):
        """
        IfGroup model access the interface method from API accessible.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfGroupMemberID": self.IfGroupMemberID})
