from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceDiskUtilizationRemote(RemoteModel):
    """
    This table list out entries of Device Disk Utilization


    |  ``HRStorageID:`` The internal NetMRI identifier of the high rate storage in the device disk utilization.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which device disk utilization information was collected.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``HRStorageIndex:`` The current index of the high risk storage device in the device disk utilization.
    |  ``attribute type:`` string

    |  ``HRStorageDescr:`` The high risk storage description of the device disk utilization.
    |  ``attribute type:`` string

    |  ``HRStorageAllocationUnits:`` The allocated units of the high risk storage in the device disk utilization.
    |  ``attribute type:`` string

    |  ``HRStorageSize:`` The storage size in the device disk utilization.
    |  ``attribute type:`` string

    |  ``HRStorageUsed:`` The used storage size in the device disk utilization.
    |  ``attribute type:`` string



    """

    properties = ("HRStorageID",
                  "DeviceID",
                  "DataSourceID",
                  "StartTime",
                  "EndTime",
                  "HRStorageIndex",
                  "HRStorageDescr",
                  "HRStorageAllocationUnits",
                  "HRStorageSize",
                  "HRStorageUsed",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"HRStorageID": self.HRStorageID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"HRStorageID": self.HRStorageID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"HRStorageID": self.HRStorageID})
