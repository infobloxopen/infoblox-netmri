from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceGroupMemberRemote(RemoteModel):
    """
    Contains entries representing each group and each device within the group.


    |  ``DeviceGroupMemberID:`` The internal NetMRI identifier for this device group membership record.
    |  ``attribute type:`` number

    |  ``GroupID:`` The internal NetMRI identifier for the group associated with this membership record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device associated with this membership record.
    |  ``attribute type:`` number

    |  ``DeviceGroupMemberStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupMemberEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DeviceGroupMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    """

    properties = ("DeviceGroupMemberID",
                  "GroupID",
                  "DeviceID",
                  "DeviceGroupMemberStartTime",
                  "DeviceGroupMemberEndTime",
                  "DeviceGroupMemberChangedCols",
                  "DeviceGroupMemberTimestamp",
                  "DataSourceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceGroupMemberID": self.DeviceGroupMemberID})

    @property
    @check_api_availability
    def device(self):
        """
        The device corresponding to this group membership record.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceGroupMemberID": self.DeviceGroupMemberID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device corresponding to this group membership record.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceGroupMemberID": self.DeviceGroupMemberID})
