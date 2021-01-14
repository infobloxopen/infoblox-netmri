from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class CircuitLinkComponentRemote(RemoteModel):
    """
    This table list out all the entries of circuit link components.


    |  ``CLinkCompID:`` The internal NetMRI identifier of the circuit link component.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which circuit link component was collected.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``CLinkCompStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``CLinkCompEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``CLinkCompTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``CLinkCompChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``CLinkCompDtgIndex:`` The index of the device in the circuit link components.
    |  ``attribute type:`` string

    |  ``CLinkCompCounter:`` The number of devices in the circuit link component.
    |  ``attribute type:`` string

    |  ``CLinkCompType:`` The NetMRI-determined device type of the circuit link component.
    |  ``attribute type:`` string

    |  ``CLinkCompUnitNumber:`` The serial number of the collector in the circuit link component.
    |  ``attribute type:`` string

    |  ``CLinkCompState:`` The circuit link component state of this interface for this VLAN.
    |  ``attribute type:`` string




    """

    properties = ("CLinkCompID",
                  "DeviceID",
                  "DataSourceID",
                  "CLinkCompStartTime",
                  "CLinkCompEndTime",
                  "CLinkCompTimestamp",
                  "CLinkCompChangedCols",
                  "CLinkCompDtgIndex",
                  "CLinkCompCounter",
                  "CLinkCompType",
                  "CLinkCompUnitNumber",
                  "CLinkCompState",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"CLinkCompID": self.CLinkCompID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"CLinkCompID": self.CLinkCompID})

    @property
    @check_api_availability
    def interface(self):
        """
        interface
        ``attribute type:`` model
        """
        return self.broker.interface(**{"CLinkCompID": self.CLinkCompID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"CLinkCompID": self.CLinkCompID})
