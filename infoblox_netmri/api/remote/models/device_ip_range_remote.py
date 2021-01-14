from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceIpRangeRemote(RemoteModel):
    """
    Network IP Ranges definition


    |  ``DeviceIPRangeID:`` The internal NetMRI identifier for ip address range definition.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this flow.
    |  ``attribute type:`` number

    |  ``DeviceObjectID:`` The internal NetMRI identifier for the service to which belongs this flow.
    |  ``attribute type:`` number

    |  ``IprFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this flow.
    |  ``attribute type:`` datetime

    |  ``IprIPVersion:`` The ip version for this range. 4 or 6.
    |  ``attribute type:`` number

    |  ``IprDisplayText:`` The text that was defined in the configuration for this ip address range.
    |  ``attribute type:`` string

    |  ``IprIPNumericMin:`` The numeric value for the range min value.
    |  ``attribute type:`` number

    |  ``IprIPNumericMax:`` The numeric value for the range max value.
    |  ``attribute type:`` number




    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``IprStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``IprEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``IprTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``IprChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceIPRangeID",
                  "DeviceID",
                  "DeviceObjectID",
                  "IprFirstSeenTime",
                  "IprIPVersion",
                  "IprDisplayText",
                  "IprIPNumericMin",
                  "IprIPNumericMax",
                  "DataSourceID",
                  "IprStartTime",
                  "IprEndTime",
                  "IprTimestamp",
                  "IprChangedCols",
                  )

    @property
    @check_api_availability
    def device_object(self):
        """
        the network object to which belongs this ip address range.
        ``attribute type:`` model
        """
        return self.broker.device_object(**{"DeviceIPRangeID": self.DeviceIPRangeID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceIPRangeID": self.DeviceIPRangeID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceIPRangeID": self.DeviceIPRangeID})
