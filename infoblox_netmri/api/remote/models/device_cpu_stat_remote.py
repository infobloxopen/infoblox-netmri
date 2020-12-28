from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceCpuStatRemote(RemoteModel):
    """
    Device CPU Statistics captured by NetMRI.


    |  ``DeviceCpuStatsID:`` The internal NetMRI for this device CPU statistics record.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this record was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting date/time for the sample interval.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The ending date/time for the sample interval.
    |  ``attribute type:`` datetime

    |  ``CpuIndex:`` The CPU number.
    |  ``attribute type:`` number

    |  ``CpuBusy:`` The CPU busy reading for the time period.
    |  ``attribute type:`` number



    """

    properties = ("DeviceCpuStatsID",
                  "DataSourceID",
                  "DeviceID",
                  "StartTime",
                  "EndTime",
                  "CpuIndex",
                  "CpuBusy",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceCpuStatsID": self.DeviceCpuStatsID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceCpuStatsID": self.DeviceCpuStatsID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceCpuStatsID": self.DeviceCpuStatsID})
