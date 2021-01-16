from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class LldpNeighborRemote(RemoteModel):
    """
    The LLDP table entries for the device.


    |  ``LLDPNeighborID:`` The internal NetMRI identifier for this LLDP table entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this LLDP data was collected.
    |  ``attribute type:`` number

    |  ``LLDPNeighborCapabilities:`` The neighbor capabilities, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``LLDPNeighborDescription:`` The description of the neighbor, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``LLDPNeighborPrimaryIPDotted:`` The management Primary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborPrimaryIPNumeric:`` The numerical value of the management Primary IP address that was reported by LLDP.
    |  ``attribute type:`` number

    |  ``LLDPNeighborSecondaryIPDotted:`` The management Secondary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborSecondaryIPNumeric:`` The numerical value of the management Secondary IP address that was reported by LLDP.
    |  ``attribute type:`` number

    |  ``LLDPNeighborMAC:`` The Media Access Controller (MAC) address of the neighbor, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborPortName:`` The port name of the neighbor interface, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``LLDPNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this LLDP neighbor table entry.
    |  ``attribute type:`` number

    |  ``LLDPNeighborInterfaceID:`` The internal NetMRI identifier for the neighbor interface reported by LLDP, if available.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP index for the local interface for this LLDP neighbor table entry.
    |  ``attribute type:`` number

    |  ``LLDPNeighborIfIndex:`` The SNMP index for the neighbor interface reported by LLDP, if available.
    |  ``attribute type:`` number

    |  ``LLDPNeighborDeviceID:`` The internal NetMRI identifier for the neighbor device reported by LLDP, if available.
    |  ``attribute type:`` number

    |  ``LLDPNeighborName:`` The name of the neighbor interface, as reported by LLDP.
    |  ``attribute type:`` string

    |  ``LLDPNeighborCapabilitiesNumeric:`` The numerical value of neighbor capabilities, as reported by LLDP.
    |  ``attribute type:`` number







    |  ``LLDPNeighborVersion:`` The version of the neighbor, as reported by LLDP.
    |  ``attribute type:`` string

    """

    properties = ("LLDPNeighborID",
                  "DeviceID",
                  "LLDPNeighborCapabilities",
                  "LLDPNeighborChangedCols",
                  "LLDPNeighborDescription",
                  "LLDPNeighborEndTime",
                  "LLDPNeighborPrimaryIPDotted",
                  "LLDPNeighborPrimaryIPNumeric",
                  "LLDPNeighborSecondaryIPDotted",
                  "LLDPNeighborSecondaryIPNumeric",
                  "LLDPNeighborMAC",
                  "LLDPNeighborPortName",
                  "LLDPNeighborStartTime",
                  "LLDPNeighborTimestamp",
                  "DataSourceID",
                  "InterfaceID",
                  "LLDPNeighborInterfaceID",
                  "ifIndex",
                  "LLDPNeighborIfIndex",
                  "LLDPNeighborDeviceID",
                  "LLDPNeighborName",
                  "LLDPNeighborCapabilitiesNumeric",
                  "LLDPNeighborVersion",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"LLDPNeighborID": self.LLDPNeighborID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"LLDPNeighborID": self.LLDPNeighborID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface object on which the LLDP neighbor was reported.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"LLDPNeighborID": self.LLDPNeighborID})

    @property
    @check_api_availability
    def neighbor_device(self):
        """
        The device object corresponding to the LLDP neighbor.
        ``attribute type:`` model
        """
        return self.broker.neighbor_device(**{"LLDPNeighborID": self.LLDPNeighborID})

    @property
    @check_api_availability
    def neighbor_interface(self):
        """
        The interface object on the neighboring device.
        ``attribute type:`` model
        """
        return self.broker.neighbor_interface(**{"LLDPNeighborID": self.LLDPNeighborID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"LLDPNeighborID": self.LLDPNeighborID})
