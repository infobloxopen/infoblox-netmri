from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NiosGridMemberRemote(RemoteModel):
    """
    This table list out entries of Nios Grid members


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``GridMemberStatusID:`` The internal NetMRI identifier of the status in the NIOS GridMember.
    |  ``attribute type:`` number

    |  ``GridMemberStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``GridMemberEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``GridMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``GridMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``GridMemberFirstSeenTime:`` The timestamp of when NetMRI first discovered this interface in the NIOS GridMember.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which NIOS GridMember entry was collected.
    |  ``attribute type:`` number

    |  ``GridMemberDeviceID:`` The internal NetMRI identifier of each device in the NIOS GridMember.
    |  ``attribute type:`` number

    |  ``GridMemberIPDotted:`` The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``GridMemberIPNumeric:`` The numerical value of the GridMember.
    |  ``attribute type:`` number

    |  ``GridMemberStatus:`` The status of the NIOS GridMember.
    |  ``attribute type:`` string

    |  ``GridMemberQueueFromMaster:`` The grid member queue return from master in the NIOS GridMember.
    |  ``attribute type:`` string

    |  ``GridMemberLastRepTimeFromMaster:`` The last response time returned from master in the NIOS GridMember.
    |  ``attribute type:`` string

    |  ``GridMemberQueueToMaster:`` The grid member queue sent to master in the NIOs GridMember.
    |  ``attribute type:`` string

    |  ``GridMemberLastRepTimeToMaster:`` The last response time sent to master of the NIOS grid member.
    |  ``attribute type:`` string



    """

    properties = ("DataSourceID",
                  "GridMemberStatusID",
                  "GridMemberStartTime",
                  "GridMemberEndTime",
                  "GridMemberChangedCols",
                  "GridMemberTimestamp",
                  "GridMemberFirstSeenTime",
                  "DeviceID",
                  "GridMemberDeviceID",
                  "GridMemberIPDotted",
                  "GridMemberIPNumeric",
                  "GridMemberStatus",
                  "GridMemberQueueFromMaster",
                  "GridMemberLastRepTimeFromMaster",
                  "GridMemberQueueToMaster",
                  "GridMemberLastRepTimeToMaster",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"GridMemberStatusID": self.GridMemberStatusID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"GridMemberStatusID": self.GridMemberStatusID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"GridMemberStatusID": self.GridMemberStatusID})
