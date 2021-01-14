from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfWirelessSSIDRemote(RemoteModel):
    """
    This table list out the entries of Interface Wireless Service Set Identifier.


    |  ``IfWirelessSSIDID:`` The internal NetMRI identifier of wireless SSID in the interface.
    |  ``attribute type:`` number

    |  ``ifWirelessSSIDStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ifWirelessSSIDEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ifWirelessSSIDChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifWirelessSSIDTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier of each device from which Wireless SSID table entry was found.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP index of the local interface for the wireless SSID.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier of local interface for this wireless SSID table.
    |  ``attribute type:`` number

    |  ``SSIDIndex:`` The service set identifier(SSID) index of the interface wirelessSSID.
    |  ``attribute type:`` string

    |  ``SSID:`` The unique number of service set identifier(SSID) in the wirelessSSID.
    |  ``attribute type:`` number

    |  ``SSIDMaxAssociations:`` The maximum associations formed by the wirelessSSID.
    |  ``attribute type:`` string

    |  ``WEPMICAlgorithm:`` The algorithm process of web equivalent privacy in the wirelessSSID.
    |  ``attribute type:`` string

    |  ``WEPPermuteAlgorithm:`` The permutation algorithm of web equivalent privacy in the wirelessSSID.
    |  ``attribute type:`` string

    |  ``SSIDDefaultVlanIndex:`` The default VLAN Index of the wireless SSID.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``SSIDBroadcastInd:`` A flag indicates whether the broadcast index of the wireless SSID is enabled or not.
    |  ``attribute type:`` bool





    """

    properties = ("IfWirelessSSIDID",
                  "ifWirelessSSIDStartTime",
                  "ifWirelessSSIDEndTime",
                  "ifWirelessSSIDChangedCols",
                  "ifWirelessSSIDTimestamp",
                  "DataSourceID",
                  "DeviceID",
                  "ifIndex",
                  "InterfaceID",
                  "SSIDIndex",
                  "SSID",
                  "SSIDMaxAssociations",
                  "WEPMICAlgorithm",
                  "WEPPermuteAlgorithm",
                  "SSIDDefaultVlanIndex",
                  "VlanID",
                  "SSIDBroadcastInd",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfWirelessSSIDID": self.IfWirelessSSIDID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfWirelessSSIDID": self.IfWirelessSSIDID})

    @property
    @check_api_availability
    def interface(self):
        """
        interface
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfWirelessSSIDID": self.IfWirelessSSIDID})

    @property
    @check_api_availability
    def vlan(self):
        """
        vlan
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"IfWirelessSSIDID": self.IfWirelessSSIDID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfWirelessSSIDID": self.IfWirelessSSIDID})
