from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class CdpNeighborRemote(RemoteModel):
    """
    The CDP table entries for the device.


    |  ``CDPNeighborID:`` The internal NetMRI identifier for this CDP table entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this CDP data was collected.
    |  ``attribute type:`` number

    |  ``CDPNeighborCapabilities:`` The neighbor capabilities, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``CDPNeighborDescription:`` The description of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``CDPNeighborIPDotted:`` The management IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborIPNumeric:`` The numerical value of the management IP address that was reported by CDP.
    |  ``attribute type:`` number

    |  ``CDPNeighborMAC:`` The Media Access Controller (MAC) address of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborMapSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``CDPNeighborOrigTable:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``CDPNeighborPlatform:`` The platform description of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborPortName:`` The port name of the neighbor interface, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``CDPNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``CDPNeighborVersion:`` The version of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this CDP neighbor table entry.
    |  ``attribute type:`` number


    |  ``CDPNeighborInterfaceID:`` The internal NetMRI identifier for the neighbor interface reported by CDP, if available.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP index for the local interface for this CDP neighbor table entry.
    |  ``attribute type:`` number

    |  ``CDPNeighborIfIndex:`` The SNMP index for the neighbor interface reported by CDP, if available.
    |  ``attribute type:`` number


    |  ``CDPNeighborDeviceID:`` The internal NetMRI identifier for the neighbor device reported by CDP, if available.
    |  ``attribute type:`` number


    """

    properties = ("CDPNeighborID",
                  "DeviceID",
                  "CDPNeighborCapabilities",
                  "CDPNeighborChangedCols",
                  "CDPNeighborDescription",
                  "CDPNeighborEndTime",
                  "CDPNeighborIPDotted",
                  "CDPNeighborIPNumeric",
                  "CDPNeighborMAC",
                  "CDPNeighborMapSource",
                  "CDPNeighborOrigTable",
                  "CDPNeighborPlatform",
                  "CDPNeighborPortName",
                  "CDPNeighborStartTime",
                  "CDPNeighborTimestamp",
                  "CDPNeighborVersion",
                  "DataSourceID",
                  "InterfaceID",
                  "CDPNeighborInterfaceID",
                  "ifIndex",
                  "CDPNeighborIfIndex",
                  "CDPNeighborDeviceID",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this CDP data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"CDPNeighborID": self.CDPNeighborID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"CDPNeighborID": self.CDPNeighborID})

    @property
    @check_api_availability
    def interface(self):
        """
        The local interface for this CDP neighbor table entry.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"CDPNeighborID": self.CDPNeighborID})

    @property
    @check_api_availability
    def neighbor_interface(self):
        """
        The neighbor interface reported by CDP, if available.
        ``attribute type:`` model
        """
        return self.broker.neighbor_interface(**{"CDPNeighborID": self.CDPNeighborID})

    @property
    @check_api_availability
    def neighbor_device(self):
        """
        The neighbor device reported by CDP, if available.
        ``attribute type:`` model
        """
        return self.broker.neighbor_device(**{"CDPNeighborID": self.CDPNeighborID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this CDP data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"CDPNeighborID": self.CDPNeighborID})
