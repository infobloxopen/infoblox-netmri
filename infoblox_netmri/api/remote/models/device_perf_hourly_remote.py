from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePerfHourlyRemote(RemoteModel):
    """
    Contains hourly summaries of device performance statistics.


    |  ``DevicePerfHourlyID:`` The internal NetMRI identifier for this performance record.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this data was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The starting date/time of the one hour interval.
    |  ``attribute type:`` datetime

    |  ``CpuBusyMin:`` The minimum CPU busy reading during the hour.
    |  ``attribute type:`` number

    |  ``CpuBusyAvg:`` The mean CPU busy reading during the hour.
    |  ``attribute type:`` float

    |  ``CpuBusyMax:`` The maximum CPU busy reading during the hour.
    |  ``attribute type:`` number

    |  ``UsedMemMin:`` The minimum used memory reading during the hour.
    |  ``attribute type:`` number

    |  ``UsedMemAvg:`` The average used memory reading during the hour.
    |  ``attribute type:`` float

    |  ``UsedMemMax:`` The maximum used memory reading during the hour.
    |  ``attribute type:`` number

    |  ``FreeMemMin:`` The minimum free memory reading during the hour.
    |  ``attribute type:`` number

    |  ``FreeMemAvg:`` The mean free memory reading during the hour.
    |  ``attribute type:`` float

    |  ``FreeMemMax:`` The maximum free memory reading during the hour.
    |  ``attribute type:`` number

    |  ``MemUtil5Min:`` The minimum five-minute memory utilization reading during the hour.
    |  ``attribute type:`` number

    |  ``MemUtil5Avg:`` The mean five-minute memory utilization reading during the hour.
    |  ``attribute type:`` float

    |  ``MemUtil5Max:`` The maximum five-minute memory utilization reading during the hour.
    |  ``attribute type:`` number



    """

    properties = ("DevicePerfHourlyID",
                  "DataSourceID",
                  "DeviceID",
                  "StartTime",
                  "CpuBusyMin",
                  "CpuBusyAvg",
                  "CpuBusyMax",
                  "UsedMemMin",
                  "UsedMemAvg",
                  "UsedMemMax",
                  "FreeMemMin",
                  "FreeMemAvg",
                  "FreeMemMax",
                  "MemUtil5Min",
                  "MemUtil5Avg",
                  "MemUtil5Max",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePerfHourlyID": self.DevicePerfHourlyID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePerfHourlyID": self.DevicePerfHourlyID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePerfHourlyID": self.DevicePerfHourlyID})
