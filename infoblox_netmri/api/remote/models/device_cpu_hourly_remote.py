from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceCpuHourlyRemote(RemoteModel):
    """
    Contains hourly summaries of device CPU statistics.


    |  ``DeviceCpuHourlyID:`` The internal NetMRI identifier for this Device CPU Hourly record.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this record was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting date/time for the hourly interval.
    |  ``attribute type:`` datetime

    |  ``CpuIndex:`` The CPU number.
    |  ``attribute type:`` number

    |  ``CpuBusyMin:`` The minimum CPU busy reading during the hour.
    |  ``attribute type:`` number

    |  ``CpuBusyAvg:`` The mean CPU busy reading during the hour.
    |  ``attribute type:`` float

    |  ``CpuBusyMax:`` The maximum CPU busy reading during the hour.
    |  ``attribute type:`` number



    """

    properties = ("DeviceCpuHourlyID",
                  "DataSourceID",
                  "DeviceID",
                  "StartTime",
                  "CpuIndex",
                  "CpuBusyMin",
                  "CpuBusyAvg",
                  "CpuBusyMax",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceCpuHourlyID": self.DeviceCpuHourlyID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceCpuHourlyID": self.DeviceCpuHourlyID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceCpuHourlyID": self.DeviceCpuHourlyID})
