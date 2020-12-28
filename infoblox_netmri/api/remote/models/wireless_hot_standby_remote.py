from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class WirelessHotStandbyRemote(RemoteModel):
    """
    The wireless hot stand by information per device is defined within NetMRI.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which wireless hot standby entry was collected.
    |  ``attribute type:`` number

    |  ``WlsHotSbStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``WlsHotSbEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``WlsHotSbChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``WlsHotSbTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``WlsHotSbInd:`` The flag indicating whether a wireless stand hotby table was retrieved from this device.
    |  ``attribute type:`` bool

    |  ``WlsHotSbState:`` The wireless stand hotby state of this interface for this VLAN.
    |  ``attribute type:`` string

    |  ``WlsHotSbStatus:`` The operational status (up/down) of this interface.
    |  ``attribute type:`` string

    |  ``WlsHotSbMAC:`` The Media Access Controller(MAC) of this interface.
    |  ``attribute type:`` string

    |  ``WlsHotSbDeviceID:`` The internal NetMRI identifier for each device of wireless Hot Standby entry was found.
    |  ``attribute type:`` number

    |  ``WlsHotSbPollingFeq:`` It indicates the polling frequency of the wireless hot standby.
    |  ``attribute type:`` string

    |  ``WlsHotSbPollingTimeout:`` The timeout session of the polling in wireless hot standby entry was collected.
    |  ``attribute type:`` string



    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "WlsHotSbStartTime",
                  "WlsHotSbEndTime",
                  "WlsHotSbChangedCols",
                  "WlsHotSbTimestamp",
                  "WlsHotSbInd",
                  "WlsHotSbState",
                  "WlsHotSbStatus",
                  "WlsHotSbMAC",
                  "WlsHotSbDeviceID",
                  "WlsHotSbPollingFeq",
                  "WlsHotSbPollingTimeout",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceID": self.DeviceID})
