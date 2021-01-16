from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class FirewallConnectionStatisticRemote(RemoteModel):
    """
    This table list out enties of FirewallConnectionStats


    |  ``FWCSID:`` The internal NetMRI identifier for this firewall connection statistics entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which firewall connection statistics information was collected.
    |  ``attribute type:`` number

    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``FWCSCurrentInUse:`` Currently in used firewall connection statistics.
    |  ``attribute type:`` string

    |  ``FWCSHigh:`` High level of firewall connection statistics.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``fwIndex:`` The current index of the local interface of firewall.
    |  ``attribute type:`` string



    """

    properties = ("FWCSID",
                  "DeviceID",
                  "StartTime",
                  "EndTime",
                  "FWCSCurrentInUse",
                  "FWCSHigh",
                  "DataSourceID",
                  "fwIndex",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"FWCSID": self.FWCSID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"FWCSID": self.FWCSID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"FWCSID": self.FWCSID})
