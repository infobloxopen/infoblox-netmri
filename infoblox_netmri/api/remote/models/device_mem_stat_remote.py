from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceMemStatRemote(RemoteModel):
    """
    Device Memory Statistics captured by NetMRI.


    |  ``DeviceMemStatsID:`` The internal NetMRI identifier for this device memory statistics record.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this record was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting date/time for the sample interval.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The ending date/time for the sample interval.
    |  ``attribute type:`` datetime

    |  ``UsedMem:`` The amount of memory in use on the device.
    |  ``attribute type:`` number

    |  ``FreeMem:`` The amount of free memory on the device.
    |  ``attribute type:`` number

    |  ``Utilization5Min:`` The five-minute average memory utilization percentage.
    |  ``attribute type:`` number



    """

    properties = ("DeviceMemStatsID",
                  "DataSourceID",
                  "DeviceID",
                  "StartTime",
                  "EndTime",
                  "UsedMem",
                  "FreeMem",
                  "Utilization5Min",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceMemStatsID": self.DeviceMemStatsID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceMemStatsID": self.DeviceMemStatsID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceMemStatsID": self.DeviceMemStatsID})
