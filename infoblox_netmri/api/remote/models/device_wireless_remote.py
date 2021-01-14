from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceWirelessRemote(RemoteModel):
    """
    This table list out the entries of wireless device.


    |  ``DeviceWirelessID:`` The internal NetMRI identifier of the device wireless.
    |  ``attribute type:`` number

    |  ``DeviceWirelessStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DeviceWirelessEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DeviceWirelessChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DeviceWirelessTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier of each device from which wireless setting was collected.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP index of a local interface for the device wireless table entry.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier of a local interface for the device wireless.
    |  ``attribute type:`` number

    |  ``StationID:`` The internal NetMRI identifier of a station.
    |  ``attribute type:`` string

    |  ``DesiredSSID:`` The service set identifier(SSID) of desired wireless device.
    |  ``attribute type:`` string

    |  ``StationRole:`` The role name of the station.
    |  ``attribute type:`` string

    |  ``WEPEnabledInd:`` A flag indicates whether a wired equivalent privacy is enabled or not?
    |  ``attribute type:`` bool

    |  ``WEPAllowedInd:`` A flag indicates whether a wired equivalent privacy is allowed or not?
    |  ``attribute type:`` bool

    |  ``WEPOnlyTrafficInd:`` A flag indicates whether a wired equivalent privacy is traffic or not?
    |  ``attribute type:`` bool

    |  ``WEPICVErrorCount:`` The total number of integrity check errors in WEP.
    |  ``attribute type:`` number

    |  ``WEPDefaultKeyLen1:`` The initial default key length of wired equivalent privacy.
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen2:`` The second default key length of wired equivalent privacy.
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen3:`` The third default key length of wired equivalent privacy.
    |  ``attribute type:`` string

    |  ``WEPDefaultKeyLen4:`` The fourth default key length of wired equivalent privacy.
    |  ``attribute type:`` string




    """

    properties = ("DeviceWirelessID",
                  "DeviceWirelessStartTime",
                  "DeviceWirelessEndTime",
                  "DeviceWirelessChangedCols",
                  "DeviceWirelessTimestamp",
                  "DataSourceID",
                  "DeviceID",
                  "ifIndex",
                  "InterfaceID",
                  "StationID",
                  "DesiredSSID",
                  "StationRole",
                  "WEPEnabledInd",
                  "WEPAllowedInd",
                  "WEPOnlyTrafficInd",
                  "WEPICVErrorCount",
                  "WEPDefaultKeyLen1",
                  "WEPDefaultKeyLen2",
                  "WEPDefaultKeyLen3",
                  "WEPDefaultKeyLen4",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceWirelessID": self.DeviceWirelessID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceWirelessID": self.DeviceWirelessID})

    @property
    @check_api_availability
    def interface(self):
        """
        interface
        ``attribute type:`` model
        """
        return self.broker.interface(**{"DeviceWirelessID": self.DeviceWirelessID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceWirelessID": self.DeviceWirelessID})
