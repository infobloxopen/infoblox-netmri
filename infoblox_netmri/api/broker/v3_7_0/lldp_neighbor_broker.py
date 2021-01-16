from ..broker import Broker


class LldpNeighborBroker(Broker):
    controller = "lldp_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified lldp neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of lldp neighbor methods. The listed methods will be called on each lldp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, neighbor_device, neighbor_interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return lldp_neighbor: The lldp neighbor identified by the specified LLDPNeighborID.
             :rtype lldp_neighbor: LldpNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available lldp neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this LLDP data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this LLDP data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this LLDP neighbor table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this LLDP neighbor table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by LLDP, if available.
             :type LLDPNeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by LLDP, if available.
             :type LLDPNeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the lldp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of lldp neighbor methods. The listed methods will be called on each lldp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, neighbor_device, neighbor_interface.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` LLDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is LLDPNeighborID. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each LldpNeighbor. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return lldp_neighbors: An array of the LldpNeighbor objects that match the specified input criteria.
             :rtype lldp_neighbors: Array of LldpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available lldp neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this LLDP data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this LLDP data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this LLDP neighbor table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this LLDP neighbor table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborCapabilities: The neighbor capabilities, as reported by LLDP.
             :type LLDPNeighborCapabilities: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborCapabilities: The neighbor capabilities, as reported by LLDP.
             :type LLDPNeighborCapabilities: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborCapabilitiesNumeric: The numerical value of neighbor capabilities, as reported by LLDP.
             :type LLDPNeighborCapabilitiesNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborCapabilitiesNumeric: The numerical value of neighbor capabilities, as reported by LLDP.
             :type LLDPNeighborCapabilitiesNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type LLDPNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type LLDPNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDescription: The description of the neighbor, as reported by LLDP.
             :type LLDPNeighborDescription: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDescription: The description of the neighbor, as reported by LLDP.
             :type LLDPNeighborDescription: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by LLDP, if available.
             :type LLDPNeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by LLDP, if available.
             :type LLDPNeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type LLDPNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type LLDPNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborIfIndex: The SNMP index for the neighbor interface reported by LLDP, if available.
             :type LLDPNeighborIfIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborIfIndex: The SNMP index for the neighbor interface reported by LLDP, if available.
             :type LLDPNeighborIfIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by LLDP, if available.
             :type LLDPNeighborInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by LLDP, if available.
             :type LLDPNeighborInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by LLDP.
             :type LLDPNeighborMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by LLDP.
             :type LLDPNeighborMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborName: The name of the neighbor interface, as reported by LLDP.
             :type LLDPNeighborName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborName: The name of the neighbor interface, as reported by LLDP.
             :type LLDPNeighborName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPortName: The port name of the neighbor interface, as reported by LLDP.
             :type LLDPNeighborPortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPortName: The port name of the neighbor interface, as reported by LLDP.
             :type LLDPNeighborPortName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPrimaryIPDotted: The management Primary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
             :type LLDPNeighborPrimaryIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPrimaryIPDotted: The management Primary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
             :type LLDPNeighborPrimaryIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPrimaryIPNumeric: The numerical value of the management Primary IP address that was reported by LLDP.
             :type LLDPNeighborPrimaryIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborPrimaryIPNumeric: The numerical value of the management Primary IP address that was reported by LLDP.
             :type LLDPNeighborPrimaryIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborSecondaryIPDotted: The management Secondary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
             :type LLDPNeighborSecondaryIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborSecondaryIPDotted: The management Secondary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP.
             :type LLDPNeighborSecondaryIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborSecondaryIPNumeric: The numerical value of the management Secondary IP address that was reported by LLDP.
             :type LLDPNeighborSecondaryIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborSecondaryIPNumeric: The numerical value of the management Secondary IP address that was reported by LLDP.
             :type LLDPNeighborSecondaryIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborStartTime: The starting effective time of this revision of the record.
             :type LLDPNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborStartTime: The starting effective time of this revision of the record.
             :type LLDPNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborTimestamp: The date and time this record was collected or calculated.
             :type LLDPNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborTimestamp: The date and time this record was collected or calculated.
             :type LLDPNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborVersion: The version of the neighbor, as reported by LLDP.
             :type LLDPNeighborVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LLDPNeighborVersion: The version of the neighbor, as reported by LLDP.
             :type LLDPNeighborVersion: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this LLDP neighbor table entry.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this LLDP neighbor table entry.
             :type ifIndex: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the lldp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of lldp neighbor methods. The listed methods will be called on each lldp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, neighbor_device, neighbor_interface.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` LLDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is LLDPNeighborID. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each LldpNeighbor. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against lldp neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, InterfaceID, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborChangedCols, LLDPNeighborDescription, LLDPNeighborDeviceID, LLDPNeighborEndTime, LLDPNeighborID, LLDPNeighborIfIndex, LLDPNeighborInterfaceID, LLDPNeighborMAC, LLDPNeighborName, LLDPNeighborPortName, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborStartTime, LLDPNeighborTimestamp, LLDPNeighborVersion, ifIndex.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return lldp_neighbors: An array of the LldpNeighbor objects that match the specified input criteria.
             :rtype lldp_neighbors: Array of LldpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available lldp neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, InterfaceID, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborChangedCols, LLDPNeighborDescription, LLDPNeighborDeviceID, LLDPNeighborEndTime, LLDPNeighborID, LLDPNeighborIfIndex, LLDPNeighborInterfaceID, LLDPNeighborMAC, LLDPNeighborName, LLDPNeighborPortName, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborStartTime, LLDPNeighborTimestamp, LLDPNeighborVersion, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceID: If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_f_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceID: If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_c_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this LLDP data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceID: If op_DeviceID is specified, the field named in this input will be compared to the value in DeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceID must be specified if op_DeviceID is specified.
             :type val_f_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceID: If op_DeviceID is specified, this value will be compared to the value in DeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceID must be specified if op_DeviceID is specified.
             :type val_c_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the local interface for this LLDP neighbor table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborCapabilities: The operator to apply to the field LLDPNeighborCapabilities. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborCapabilities: The neighbor capabilities, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborCapabilities: If op_LLDPNeighborCapabilities is specified, the field named in this input will be compared to the value in LLDPNeighborCapabilities using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborCapabilities must be specified if op_LLDPNeighborCapabilities is specified.
             :type val_f_LLDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborCapabilities: If op_LLDPNeighborCapabilities is specified, this value will be compared to the value in LLDPNeighborCapabilities using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborCapabilities must be specified if op_LLDPNeighborCapabilities is specified.
             :type val_c_LLDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborCapabilitiesNumeric: The operator to apply to the field LLDPNeighborCapabilitiesNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborCapabilitiesNumeric: The numerical value of neighbor capabilities, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborCapabilitiesNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborCapabilitiesNumeric: If op_LLDPNeighborCapabilitiesNumeric is specified, the field named in this input will be compared to the value in LLDPNeighborCapabilitiesNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborCapabilitiesNumeric must be specified if op_LLDPNeighborCapabilitiesNumeric is specified.
             :type val_f_LLDPNeighborCapabilitiesNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborCapabilitiesNumeric: If op_LLDPNeighborCapabilitiesNumeric is specified, this value will be compared to the value in LLDPNeighborCapabilitiesNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborCapabilitiesNumeric must be specified if op_LLDPNeighborCapabilitiesNumeric is specified.
             :type val_c_LLDPNeighborCapabilitiesNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborChangedCols: The operator to apply to the field LLDPNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborChangedCols: If op_LLDPNeighborChangedCols is specified, the field named in this input will be compared to the value in LLDPNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborChangedCols must be specified if op_LLDPNeighborChangedCols is specified.
             :type val_f_LLDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborChangedCols: If op_LLDPNeighborChangedCols is specified, this value will be compared to the value in LLDPNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborChangedCols must be specified if op_LLDPNeighborChangedCols is specified.
             :type val_c_LLDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborDescription: The operator to apply to the field LLDPNeighborDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborDescription: The description of the neighbor, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborDescription: If op_LLDPNeighborDescription is specified, the field named in this input will be compared to the value in LLDPNeighborDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborDescription must be specified if op_LLDPNeighborDescription is specified.
             :type val_f_LLDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborDescription: If op_LLDPNeighborDescription is specified, this value will be compared to the value in LLDPNeighborDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborDescription must be specified if op_LLDPNeighborDescription is specified.
             :type val_c_LLDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborDeviceID: The operator to apply to the field LLDPNeighborDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by LLDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborDeviceID: If op_LLDPNeighborDeviceID is specified, the field named in this input will be compared to the value in LLDPNeighborDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborDeviceID must be specified if op_LLDPNeighborDeviceID is specified.
             :type val_f_LLDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborDeviceID: If op_LLDPNeighborDeviceID is specified, this value will be compared to the value in LLDPNeighborDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborDeviceID must be specified if op_LLDPNeighborDeviceID is specified.
             :type val_c_LLDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborEndTime: The operator to apply to the field LLDPNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborEndTime: If op_LLDPNeighborEndTime is specified, the field named in this input will be compared to the value in LLDPNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborEndTime must be specified if op_LLDPNeighborEndTime is specified.
             :type val_f_LLDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborEndTime: If op_LLDPNeighborEndTime is specified, this value will be compared to the value in LLDPNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborEndTime must be specified if op_LLDPNeighborEndTime is specified.
             :type val_c_LLDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborID: The operator to apply to the field LLDPNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborID: If op_LLDPNeighborID is specified, the field named in this input will be compared to the value in LLDPNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborID must be specified if op_LLDPNeighborID is specified.
             :type val_f_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborID: If op_LLDPNeighborID is specified, this value will be compared to the value in LLDPNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborID must be specified if op_LLDPNeighborID is specified.
             :type val_c_LLDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborIfIndex: The operator to apply to the field LLDPNeighborIfIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborIfIndex: The SNMP index for the neighbor interface reported by LLDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborIfIndex: If op_LLDPNeighborIfIndex is specified, the field named in this input will be compared to the value in LLDPNeighborIfIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborIfIndex must be specified if op_LLDPNeighborIfIndex is specified.
             :type val_f_LLDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborIfIndex: If op_LLDPNeighborIfIndex is specified, this value will be compared to the value in LLDPNeighborIfIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborIfIndex must be specified if op_LLDPNeighborIfIndex is specified.
             :type val_c_LLDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborInterfaceID: The operator to apply to the field LLDPNeighborInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by LLDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborInterfaceID: If op_LLDPNeighborInterfaceID is specified, the field named in this input will be compared to the value in LLDPNeighborInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborInterfaceID must be specified if op_LLDPNeighborInterfaceID is specified.
             :type val_f_LLDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborInterfaceID: If op_LLDPNeighborInterfaceID is specified, this value will be compared to the value in LLDPNeighborInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborInterfaceID must be specified if op_LLDPNeighborInterfaceID is specified.
             :type val_c_LLDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborMAC: The operator to apply to the field LLDPNeighborMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborMAC: If op_LLDPNeighborMAC is specified, the field named in this input will be compared to the value in LLDPNeighborMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborMAC must be specified if op_LLDPNeighborMAC is specified.
             :type val_f_LLDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborMAC: If op_LLDPNeighborMAC is specified, this value will be compared to the value in LLDPNeighborMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborMAC must be specified if op_LLDPNeighborMAC is specified.
             :type val_c_LLDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborName: The operator to apply to the field LLDPNeighborName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborName: The name of the neighbor interface, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborName: If op_LLDPNeighborName is specified, the field named in this input will be compared to the value in LLDPNeighborName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborName must be specified if op_LLDPNeighborName is specified.
             :type val_f_LLDPNeighborName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborName: If op_LLDPNeighborName is specified, this value will be compared to the value in LLDPNeighborName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborName must be specified if op_LLDPNeighborName is specified.
             :type val_c_LLDPNeighborName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborPortName: The operator to apply to the field LLDPNeighborPortName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborPortName: The port name of the neighbor interface, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborPortName: If op_LLDPNeighborPortName is specified, the field named in this input will be compared to the value in LLDPNeighborPortName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborPortName must be specified if op_LLDPNeighborPortName is specified.
             :type val_f_LLDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborPortName: If op_LLDPNeighborPortName is specified, this value will be compared to the value in LLDPNeighborPortName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborPortName must be specified if op_LLDPNeighborPortName is specified.
             :type val_c_LLDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborPrimaryIPDotted: The operator to apply to the field LLDPNeighborPrimaryIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborPrimaryIPDotted: The management Primary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborPrimaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborPrimaryIPDotted: If op_LLDPNeighborPrimaryIPDotted is specified, the field named in this input will be compared to the value in LLDPNeighborPrimaryIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborPrimaryIPDotted must be specified if op_LLDPNeighborPrimaryIPDotted is specified.
             :type val_f_LLDPNeighborPrimaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborPrimaryIPDotted: If op_LLDPNeighborPrimaryIPDotted is specified, this value will be compared to the value in LLDPNeighborPrimaryIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborPrimaryIPDotted must be specified if op_LLDPNeighborPrimaryIPDotted is specified.
             :type val_c_LLDPNeighborPrimaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborPrimaryIPNumeric: The operator to apply to the field LLDPNeighborPrimaryIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborPrimaryIPNumeric: The numerical value of the management Primary IP address that was reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborPrimaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborPrimaryIPNumeric: If op_LLDPNeighborPrimaryIPNumeric is specified, the field named in this input will be compared to the value in LLDPNeighborPrimaryIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborPrimaryIPNumeric must be specified if op_LLDPNeighborPrimaryIPNumeric is specified.
             :type val_f_LLDPNeighborPrimaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborPrimaryIPNumeric: If op_LLDPNeighborPrimaryIPNumeric is specified, this value will be compared to the value in LLDPNeighborPrimaryIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborPrimaryIPNumeric must be specified if op_LLDPNeighborPrimaryIPNumeric is specified.
             :type val_c_LLDPNeighborPrimaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborSecondaryIPDotted: The operator to apply to the field LLDPNeighborSecondaryIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborSecondaryIPDotted: The management Secondary IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborSecondaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborSecondaryIPDotted: If op_LLDPNeighborSecondaryIPDotted is specified, the field named in this input will be compared to the value in LLDPNeighborSecondaryIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborSecondaryIPDotted must be specified if op_LLDPNeighborSecondaryIPDotted is specified.
             :type val_f_LLDPNeighborSecondaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborSecondaryIPDotted: If op_LLDPNeighborSecondaryIPDotted is specified, this value will be compared to the value in LLDPNeighborSecondaryIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborSecondaryIPDotted must be specified if op_LLDPNeighborSecondaryIPDotted is specified.
             :type val_c_LLDPNeighborSecondaryIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborSecondaryIPNumeric: The operator to apply to the field LLDPNeighborSecondaryIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborSecondaryIPNumeric: The numerical value of the management Secondary IP address that was reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborSecondaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborSecondaryIPNumeric: If op_LLDPNeighborSecondaryIPNumeric is specified, the field named in this input will be compared to the value in LLDPNeighborSecondaryIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborSecondaryIPNumeric must be specified if op_LLDPNeighborSecondaryIPNumeric is specified.
             :type val_f_LLDPNeighborSecondaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborSecondaryIPNumeric: If op_LLDPNeighborSecondaryIPNumeric is specified, this value will be compared to the value in LLDPNeighborSecondaryIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborSecondaryIPNumeric must be specified if op_LLDPNeighborSecondaryIPNumeric is specified.
             :type val_c_LLDPNeighborSecondaryIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborStartTime: The operator to apply to the field LLDPNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborStartTime: If op_LLDPNeighborStartTime is specified, the field named in this input will be compared to the value in LLDPNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborStartTime must be specified if op_LLDPNeighborStartTime is specified.
             :type val_f_LLDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborStartTime: If op_LLDPNeighborStartTime is specified, this value will be compared to the value in LLDPNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborStartTime must be specified if op_LLDPNeighborStartTime is specified.
             :type val_c_LLDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborTimestamp: The operator to apply to the field LLDPNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborTimestamp: If op_LLDPNeighborTimestamp is specified, the field named in this input will be compared to the value in LLDPNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborTimestamp must be specified if op_LLDPNeighborTimestamp is specified.
             :type val_f_LLDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborTimestamp: If op_LLDPNeighborTimestamp is specified, this value will be compared to the value in LLDPNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborTimestamp must be specified if op_LLDPNeighborTimestamp is specified.
             :type val_c_LLDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LLDPNeighborVersion: The operator to apply to the field LLDPNeighborVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LLDPNeighborVersion: The version of the neighbor, as reported by LLDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LLDPNeighborVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LLDPNeighborVersion: If op_LLDPNeighborVersion is specified, the field named in this input will be compared to the value in LLDPNeighborVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LLDPNeighborVersion must be specified if op_LLDPNeighborVersion is specified.
             :type val_f_LLDPNeighborVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LLDPNeighborVersion: If op_LLDPNeighborVersion is specified, this value will be compared to the value in LLDPNeighborVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LLDPNeighborVersion must be specified if op_LLDPNeighborVersion is specified.
             :type val_c_LLDPNeighborVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index for the local interface for this LLDP neighbor table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the lldp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of lldp neighbor methods. The listed methods will be called on each lldp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, neighbor_device, neighbor_interface.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` LLDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is LLDPNeighborID. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each LldpNeighbor. Valid values are DataSourceID, LLDPNeighborID, DeviceID, InterfaceID, ifIndex, LLDPNeighborStartTime, LLDPNeighborEndTime, LLDPNeighborChangedCols, LLDPNeighborTimestamp, LLDPNeighborDeviceID, LLDPNeighborInterfaceID, LLDPNeighborIfIndex, LLDPNeighborName, LLDPNeighborDescription, LLDPNeighborPortName, LLDPNeighborCapabilities, LLDPNeighborCapabilitiesNumeric, LLDPNeighborPrimaryIPDotted, LLDPNeighborPrimaryIPNumeric, LLDPNeighborSecondaryIPDotted, LLDPNeighborSecondaryIPNumeric, LLDPNeighborMAC, LLDPNeighborVersion. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return lldp_neighbors: An array of the LldpNeighbor objects that match the specified input criteria.
             :rtype lldp_neighbors: Array of LldpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def interface(self, **kwargs):
        """The interface object on which the LLDP neighbor was reported.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface object on which the LLDP neighbor was reported.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def neighbor_device(self, **kwargs):
        """The device object corresponding to the LLDP neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device object corresponding to the LLDP neighbor.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("neighbor_device"), kwargs)

    def neighbor_interface(self, **kwargs):
        """The interface object on the neighboring device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface object on the neighboring device.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("neighbor_interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param LLDPNeighborID: The internal NetMRI identifier for this LLDP table entry.
             :type LLDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
