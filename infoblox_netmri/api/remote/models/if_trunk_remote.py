from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfTrunkRemote(RemoteModel):
    """
    Configuration information on VLAN trunking, per interface.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this record was collected.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface to which this trunk configuration applies.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP interface index for the interface to which this trunk configuration applies.
    |  ``attribute type:`` string

    |  ``TrunkTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``TrunkStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``TrunkEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``TrunkChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``TrunkEncapsulationType:`` The trunking protocol for this trunk port.
    |  ``attribute type:`` string

    |  ``TrunkNativeVlanIndex:`` The VLAN number for the Native VLAN for this interface.
    |  ``attribute type:`` string

    |  ``TrunkNativeVlanID:`` The internal NetMRI identifier for the Native VLAN for this interface.
    |  ``attribute type:`` number

    |  ``TrunkState:`` The configured trunk state.
    |  ``attribute type:`` string

    |  ``TrunkStatus:`` The operational trunk status.
    |  ``attribute type:`` string




    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "InterfaceID",
                  "ifIndex",
                  "TrunkTimestamp",
                  "TrunkStartTime",
                  "TrunkEndTime",
                  "TrunkChangedCols",
                  "TrunkEncapsulationType",
                  "TrunkNativeVlanIndex",
                  "TrunkNativeVlanID",
                  "TrunkState",
                  "TrunkStatus",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface object for this trunk configuration.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"InterfaceID": self.InterfaceID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"InterfaceID": self.InterfaceID})
