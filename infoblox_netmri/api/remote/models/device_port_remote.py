from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePortRemote(RemoteModel):
    """
    This table list out the entries of Service port details of each device.


    |  ``DevicePortID:`` The internal NetMRI identifier of the device port.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which device service port information was collected.
    |  ``attribute type:`` number

    |  ``Port:`` The port of the device.
    |  ``attribute type:`` string

    |  ``PortProtocol:`` The protocol of the device port.
    |  ``attribute type:`` string

    |  ``PortStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``PortEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``PortChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``PortTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``PortState:`` The current state of the port in the device service port.
    |  ``attribute type:`` string

    |  ``Service:`` The current service of the port.
    |  ``attribute type:`` string

    |  ``ExpectedService:`` The expected service of the device port.
    |  ``attribute type:`` string

    |  ``FirstOccurrence:`` The first occurance in the device port.
    |  ``attribute type:`` string

    |  ``ListenAddr:`` The address of the listening port of each device.
    |  ``attribute type:`` string



    """

    properties = ("DevicePortID",
                  "DataSourceID",
                  "DeviceID",
                  "Port",
                  "PortProtocol",
                  "PortStartTime",
                  "PortEndTime",
                  "PortChangedCols",
                  "PortTimestamp",
                  "PortState",
                  "Service",
                  "ExpectedService",
                  "FirstOccurrence",
                  "ListenAddr",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePortID": self.DevicePortID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePortID": self.DevicePortID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePortID": self.DevicePortID})
