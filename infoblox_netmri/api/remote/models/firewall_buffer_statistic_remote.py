from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class FirewallBufferStatisticRemote(RemoteModel):
    """
    This table list out the entries of FirewallBufferStatistics


    |  ``FWBSID:`` The internal NetMRI identifier of the firewall buffer statistics.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which firewall buffer statistics information was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``FWBSSize:`` The size of the firewall buffer statistics.
    |  ``attribute type:`` string

    |  ``FWBSMaximum:`` The maximum buffer size of the firewall.
    |  ``attribute type:`` string

    |  ``FWBSLow:`` The minimum buffer size of the firewall.
    |  ``attribute type:`` string

    |  ``FWBSFree:`` The free buffer size of the firewall buffer statistics.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    """

    properties = ("FWBSID",
                  "DeviceID",
                  "StartTime",
                  "EndTime",
                  "FWBSSize",
                  "FWBSMaximum",
                  "FWBSLow",
                  "FWBSFree",
                  "DataSourceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"FWBSID": self.FWBSID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"FWBSID": self.FWBSID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"FWBSID": self.FWBSID})
