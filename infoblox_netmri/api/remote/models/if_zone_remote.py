from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfZoneRemote(RemoteModel):
    """
    Attachment of the interfaces of the device to the zone of filtering


    |  ``IfZoneID:`` The internal NetMRI identifier for this relation between a Zone and an Interface of device.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device for which belongs Zone and Interface.
    |  ``attribute type:`` number

    |  ``DeviceZoneID:`` The internal NetMRI identifier of the Zone.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier of the Interface of the device.
    |  ``attribute type:`` number

    |  ``ifZoneFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this relationship.
    |  ``attribute type:`` datetime




    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``ifZoneStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ifZoneEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifZoneTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``ifZoneChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("IfZoneID",
                  "DeviceID",
                  "DeviceZoneID",
                  "InterfaceID",
                  "ifZoneFirstSeenTime",
                  "DataSourceID",
                  "ifZoneStartTime",
                  "ifZoneEndTime",
                  "ifZoneTimestamp",
                  "ifZoneChangedCols",
                  )

    @property
    @check_api_availability
    def device_zone(self):
        """
        The DeviceZone part of this relationship.
        ``attribute type:`` model
        """
        return self.broker.device_zone(**{"IfZoneID": self.IfZoneID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfZoneID": self.IfZoneID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfZoneID": self.IfZoneID})
