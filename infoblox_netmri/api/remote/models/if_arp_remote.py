from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfArpRemote(RemoteModel):
    """
    ARP table entries on a device, per interface.



    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``ArpStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ArpEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ArpChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ArpTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime


    |  ``DeviceID:`` The internal NetMRI identifier of the device from which this ARP entry was collected.
    |  ``attribute type:`` number

    |  ``PhysicalAddr:`` The physical address for this ARP entry.
    |  ``attribute type:`` string

    |  ``IPAddrNumeric:`` The numerical value of the IP address for this ARP entry.
    |  ``attribute type:`` number

    |  ``IPAddrDotted:`` The IP address for this ARP entry, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP index for the local interface for this ARP table entry.
    |  ``attribute type:`` number


    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this ARP table entry.
    |  ``attribute type:`` number



    |  ``ArpDeviceID:`` The internal NetMRI identifier for the remote device to which the ARP entry refers, if available.
    |  ``attribute type:`` number

    |  ``ArpInterfaceID:`` The internal NetMRI identifier for the remote interface to which the ARP entry refers, if available.
    |  ``attribute type:`` number

    |  ``IfArpID:`` The internal NetMRI identifier for this ARP entry.
    |  ``attribute type:`` number

    |  ``VrfID:`` The internal NetMRI identifier for the VRF to which this ARP entry applies, if available.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "ArpStartTime",
                  "ArpEndTime",
                  "ArpChangedCols",
                  "ArpTimestamp",
                  "DeviceID",
                  "PhysicalAddr",
                  "IPAddrNumeric",
                  "IPAddrDotted",
                  "ifIndex",
                  "InterfaceID",
                  "ArpDeviceID",
                  "ArpInterfaceID",
                  "IfArpID",
                  "VrfID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The internal NetMRI identifier for the collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfArpID": self.IfArpID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this ARP entry was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfArpID": self.IfArpID})

    @property
    @check_api_availability
    def interface(self):
        """
        The local interface for this ARP table entry.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfArpID": self.IfArpID})

    @property
    @check_api_availability
    def remote_device(self):
        """
        The remote device to which the ARP entry refers, if available.
        ``attribute type:`` model
        """
        return self.broker.remote_device(**{"IfArpID": self.IfArpID})

    @property
    @check_api_availability
    def remote_interface(self):
        """
        The remote interface to which the ARP entry refers, if available.
        ``attribute type:`` model
        """
        return self.broker.remote_interface(**{"IfArpID": self.IfArpID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this ARP entry was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfArpID": self.IfArpID})
