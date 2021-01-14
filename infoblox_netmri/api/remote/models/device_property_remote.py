from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePropertyRemote(RemoteModel):
    """
    Miscellaneous data about a device, gathered from SNMP or other sources.





    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DevicePropertyID:`` The Unique Identifier for the Device Property.
    |  ``attribute type:`` number

    |  ``DevicePropStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DevicePropEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DevicePropChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DevicePropTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The Device ID that relates to the Device Property
    |  ``attribute type:`` number

    |  ``DevicePropName:`` The Device Property Name.
    |  ``attribute type:`` string

    |  ``DevicePropIndex:`` The Device Property Index
    |  ``attribute type:`` string

    |  ``DevicePropSource:`` The Device Property Source
    |  ``attribute type:`` string

    |  ``DevicePropValue:`` The Device Property Value
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The Secure Version number
    |  ``attribute type:`` number

    """

    properties = ("DataSourceID",
                  "DevicePropertyID",
                  "DevicePropStartTime",
                  "DevicePropEndTime",
                  "DevicePropChangedCols",
                  "DevicePropTimestamp",
                  "DeviceID",
                  "DevicePropName",
                  "DevicePropIndex",
                  "DevicePropSource",
                  "DevicePropValue",
                  "SecureVersion",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePropertyID": self.DevicePropertyID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePropertyID": self.DevicePropertyID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePropertyID": self.DevicePropertyID})
