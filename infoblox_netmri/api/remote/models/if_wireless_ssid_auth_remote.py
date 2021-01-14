from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfWirelessSSIDAuthRemote(RemoteModel):
    """
    This table list out the entries of WirelessSSID Authentication.


    |  ``IfWirelessSSIDAuthID:`` The internal NetMRI identifier of the Wireless SSID Authentication.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which wireless SSID information was collected.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this Wireless SSID table entry.
    |  ``attribute type:`` number

    |  ``ifWirelessSSIDAuthStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ifWirelessSSIDAuthEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifWirelessSSIDAuthChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDAuthTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SSIDIndex:`` The SSID index of the local interface for this Wireless SSID.
    |  ``attribute type:`` string

    |  ``SSIDAlgorithmIndex:`` The SSID algorithm index of the wireless SSID.
    |  ``attribute type:`` string

    |  ``SSIDAuthEnabledInd:`` A flag indicates SSID Authentication is enabled or not.
    |  ``attribute type:`` bool

    |  ``SSIDEAPRequiredInd:`` A flag indicates whether a extensible authentication protocol is required or not.
    |  ``attribute type:`` bool

    |  ``SSIDEAPMethod:`` The Extensible Authentication Protocol Method is used in theWirelessSSIDAuth.
    |  ``attribute type:`` string

    |  ``SSIDMACAuthRequiredInd:`` A flag indicates the SSID Media Access Controller(MAC) is required the authentication or not.
    |  ``attribute type:`` bool

    |  ``SSIDMACAuthMethod:`` The Media Access Controller(MAC) authentication method in the Wireless SSID.
    |  ``attribute type:`` string

    |  ``SSIDDefaultVlanIndex:`` The default VLAN index of the local interface of the Wireless SSID.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``SSIDAuthAlgorithm:`` The SSID Authentication algorithm in the interface wireless.
    |  ``attribute type:`` string





    """

    properties = ("IfWirelessSSIDAuthID",
                  "DataSourceID",
                  "DeviceID",
                  "InterfaceID",
                  "ifWirelessSSIDAuthStartTime",
                  "ifWirelessSSIDAuthEndTime",
                  "ifWirelessSSIDAuthChangedCols",
                  "ifWirelessSSIDAuthTimestamp",
                  "SSIDIndex",
                  "SSIDAlgorithmIndex",
                  "SSIDAuthEnabledInd",
                  "SSIDEAPRequiredInd",
                  "SSIDEAPMethod",
                  "SSIDMACAuthRequiredInd",
                  "SSIDMACAuthMethod",
                  "SSIDDefaultVlanIndex",
                  "VlanID",
                  "SSIDAuthAlgorithm",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfWirelessSSIDAuthID": self.IfWirelessSSIDAuthID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfWirelessSSIDAuthID": self.IfWirelessSSIDAuthID})

    @property
    @check_api_availability
    def interface(self):
        """
        interface
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfWirelessSSIDAuthID": self.IfWirelessSSIDAuthID})

    @property
    @check_api_availability
    def vlan(self):
        """
        vlan
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"IfWirelessSSIDAuthID": self.IfWirelessSSIDAuthID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfWirelessSSIDAuthID": self.IfWirelessSSIDAuthID})
