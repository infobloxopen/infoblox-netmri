from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SwitchPortFwdRemote(RemoteModel):
    """
    The switch forwarding table entries per device, per switch port.


    |  ``SwitchPortFwdID:`` The internal NetMRI identifier for this switch port forwarding entry.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this switch port forwarding entry was collected.
    |  ``attribute type:`` number

    |  ``SwitchPortNumber:`` The switch port number for the port on which this switch forwarding entry was found. This is as reported by the SNMP BRIDGE MIB, and is not the same as the SNMP interface index.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface on which this switch forwarding entry was found.
    |  ``attribute type:`` number

    |  ``SwitchPortFwdStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``SwitchPortFwdEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SwitchPortFwdChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SwitchPortFwdTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SwitchPortFwdMAC:`` The MAC address that is being forwarded.
    |  ``attribute type:`` string

    |  ``SwitchPortFwdStatus:`` The status of this entry; indicates how the entry was entered in the switch forwarding table.
    |  ``attribute type:`` string

    |  ``SwitchPortFwdVlanIndex:`` The VLAN number for which this MAC address is forwarded.
    |  ``attribute type:`` number

    |  ``SwitchPortFwdVlanID:`` The internal NetMRI identifier for the VLAN for which this MAC address is forwarded.
    |  ``attribute type:`` number

    |  ``SwitchPortFwdInterfaceID:`` The internal NetMRI identifier of the interface to which the MAC address corresponds (that is, the destination interface).
    |  ``attribute type:`` number

    |  ``SwitchPortFwdDeviceID:`` The internal NetMRI identifier of the device to which the MAC address corresponds (that is, the destination device).
    |  ``attribute type:`` number





    """

    properties = ("SwitchPortFwdID",
                  "DataSourceID",
                  "DeviceID",
                  "SwitchPortNumber",
                  "InterfaceID",
                  "SwitchPortFwdStartTime",
                  "SwitchPortFwdEndTime",
                  "SwitchPortFwdChangedCols",
                  "SwitchPortFwdTimestamp",
                  "SwitchPortFwdMAC",
                  "SwitchPortFwdStatus",
                  "SwitchPortFwdVlanIndex",
                  "SwitchPortFwdVlanID",
                  "SwitchPortFwdInterfaceID",
                  "SwitchPortFwdDeviceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"SwitchPortFwdID": self.SwitchPortFwdID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"SwitchPortFwdID": self.SwitchPortFwdID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface on which the switch port forwarding entry was found.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"SwitchPortFwdID": self.SwitchPortFwdID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The VLAN on which the switch port forwarding entry was found.
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"SwitchPortFwdID": self.SwitchPortFwdID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"SwitchPortFwdID": self.SwitchPortFwdID})
