from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceZoneRemote(RemoteModel):
    """
    Zones defined on a traffic filtering device. On devices that do not natively support zones (e.g., Cisco routers), there is one zone per interface, plus an additional 'internal' zone.


    |  ``DeviceZoneID:`` The internal NetMRI identifier for this filtering zone.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which this zone belongs.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``ZoneFirstSeenTime:`` The timestamp of when NetMRI first discovered this service.
    |  ``attribute type:`` datetime

    |  ``ZoneStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ZoneEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ZoneTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``ZoneChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ZoneName:`` The name of the zone.
    |  ``attribute type:`` string

    |  ``ZoneProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string

    |  ``ZoneInterfaceCount:`` The total number of interfaces connected to this zone.
    |  ``attribute type:`` number

    |  ``ZoneInterfaceID:`` The internal NetMRI identifier of that interface, if only one interface connected to this zone.
    |  ``attribute type:`` number

    |  ``ZoneArtificialInd:`` A flag indicating that this zone has no counterpart in the device configuration.
    |  ``attribute type:`` bool



    """

    properties = ("DeviceZoneID",
                  "DeviceID",
                  "DataSourceID",
                  "ZoneFirstSeenTime",
                  "ZoneStartTime",
                  "ZoneEndTime",
                  "ZoneTimestamp",
                  "ZoneChangedCols",
                  "ZoneName",
                  "ZoneProvisionData",
                  "ZoneInterfaceCount",
                  "ZoneInterfaceID",
                  "ZoneArtificialInd",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceZoneID": self.DeviceZoneID})

    @property
    @check_api_availability
    def zone_interface(self):
        """
        The Interface linked to this zone (if only one interface linked to this zone)
        ``attribute type:`` model
        """
        return self.broker.zone_interface(**{"DeviceZoneID": self.DeviceZoneID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceZoneID": self.DeviceZoneID})
