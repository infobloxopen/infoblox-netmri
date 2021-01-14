from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceEnvironmentMonitorRemote(RemoteModel):
    """
    This table list out entries of Device Environment


    |  ``DevEnvMonID:`` The internal NetMRI identifier of Device Environment.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which device environment information was collected.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DevEnvMonStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DevEnvMonEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DevEnvMonTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DevEnvMonChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DevEnvMonIndex:`` The index of the device in the device environment.
    |  ``attribute type:`` string

    |  ``DevEnvMonType:`` The NetMRI-determined monitor type of Device Environment.
    |  ``attribute type:`` string

    |  ``DevEnvMonDescr:`` The NetMRI-determined description of the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonState:`` The current state of the device in the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonStatus:`` The status of the device in the Device Environment Monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonMeasure:`` The measure of the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonLowWarnVal:`` The low value of the warning message in the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonLowShutdown:`` The low value of the shut down process in the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonHighWarnVal:`` The high value of the warning message in the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonHighShutdown:`` The high value of the shut down process in the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonStatusMessage:`` The status message of the device environment monitor.
    |  ``attribute type:`` string

    |  ``DevEnvMonStatusAlert:`` The alert status of the device environment monitor.
    |  ``attribute type:`` string



    """

    properties = ("DevEnvMonID",
                  "DeviceID",
                  "DataSourceID",
                  "DevEnvMonStartTime",
                  "DevEnvMonEndTime",
                  "DevEnvMonTimestamp",
                  "DevEnvMonChangedCols",
                  "DevEnvMonIndex",
                  "DevEnvMonType",
                  "DevEnvMonDescr",
                  "DevEnvMonState",
                  "DevEnvMonStatus",
                  "DevEnvMonMeasure",
                  "DevEnvMonLowWarnVal",
                  "DevEnvMonLowShutdown",
                  "DevEnvMonHighWarnVal",
                  "DevEnvMonHighShutdown",
                  "DevEnvMonStatusMessage",
                  "DevEnvMonStatusAlert",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevEnvMonID": self.DevEnvMonID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevEnvMonID": self.DevEnvMonID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevEnvMonID": self.DevEnvMonID})
