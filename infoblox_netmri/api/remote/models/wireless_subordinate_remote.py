from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class WirelessSubordinateRemote(RemoteModel):
    """
    This table list out all the entries of regarding wireless subordinates.


    |  ``WirelessSubordinantID:`` The internal NetMRI identifier of the WirelessSubordinantID
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which wireless subordinates was collected.
    |  ``attribute type:`` number

    |  ``SubStartTime:`` The starting effective date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SubEndTime:`` The ending effective date and time of this record was collected or calculated, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SubChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SubTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SubMac:`` The Media Access Controller(MAC) address of the end host.
    |  ``attribute type:`` string

    |  ``SubDeviceID:`` The internal NetMRI identifier of each wireless subordinate device.
    |  ``attribute type:`` number

    |  ``SubNumOfSlots:`` The required number of slots available in the wireless subordinates.
    |  ``attribute type:`` string

    |  ``SubName:`` The name of the wireless subordinates defined within NetMRI.
    |  ``attribute type:`` string

    |  ``SubLocation:`` The location as reported by the wireless.
    |  ``attribute type:`` string

    |  ``SubMonitorOnlyMode:`` The mode operation of wireless is monitored in the NetMRI.
    |  ``attribute type:`` string

    |  ``SubOperationStatus:`` The operational status(up/down) of the wireless.
    |  ``attribute type:`` string

    |  ``SubSoftwareVersion:`` The software version is running on this device.
    |  ``attribute type:`` string

    |  ``SubBootVersion:`` The boot version of the wireless subordinate is running on this device.
    |  ``attribute type:`` string

    |  ``SubModel:`` The wireless subordinate model name.
    |  ``attribute type:`` string

    |  ``SubSerialNumber:`` The vendor-specific serial number string for the wireless subordinates.The preferred value is the serial number string actually printed on the component itself(if present).
    |  ``attribute type:`` string

    |  ``SubIPNumeric:`` The numerical value of the wireless IP Address.
    |  ``attribute type:`` number

    |  ``SubIPDotted:`` The management IP address of the wireless subordinate in dotted,(or colon delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SubType:`` The NetMRI-determined subordinate type of the wireless.
    |  ``attribute type:`` string

    |  ``SubGroupVlanName:`` The Vlan name of the wireless subordinate group.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the Vlan.
    |  ``attribute type:`` number

    |  ``SubAdminStatus:`` The configured status(up/down) of the interface.
    |  ``attribute type:`` string

    |  ``SubOSVersion:`` The operating system version of the wireless subordinate is running on this device.
    |  ``attribute type:`` string




    """

    properties = ("WirelessSubordinantID",
                  "DataSourceID",
                  "DeviceID",
                  "SubStartTime",
                  "SubEndTime",
                  "SubChangedCols",
                  "SubTimestamp",
                  "SubMac",
                  "SubDeviceID",
                  "SubNumOfSlots",
                  "SubName",
                  "SubLocation",
                  "SubMonitorOnlyMode",
                  "SubOperationStatus",
                  "SubSoftwareVersion",
                  "SubBootVersion",
                  "SubModel",
                  "SubSerialNumber",
                  "SubIPNumeric",
                  "SubIPDotted",
                  "SubType",
                  "SubGroupVlanName",
                  "VlanID",
                  "SubAdminStatus",
                  "SubOSVersion",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"WirelessSubordinantID": self.WirelessSubordinantID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"WirelessSubordinantID": self.WirelessSubordinantID})

    @property
    @check_api_availability
    def vlan(self):
        """
        vlan
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"WirelessSubordinantID": self.WirelessSubordinantID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"WirelessSubordinantID": self.WirelessSubordinantID})
