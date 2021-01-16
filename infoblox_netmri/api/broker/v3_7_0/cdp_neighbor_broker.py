from ..broker import Broker


class CdpNeighborBroker(Broker):
    controller = "cdp_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified cdp neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of cdp neighbor methods. The listed methods will be called on each cdp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
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

             :return cdp_neighbor: The cdp neighbor identified by the specified CDPNeighborID.
             :rtype cdp_neighbor: CdpNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available cdp neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by CDP, if available.
             :type CDPNeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by CDP, if available.
             :type CDPNeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this CDP data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this CDP data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this CDP neighbor table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this CDP neighbor table entry.
             :type InterfaceID: Array of Integer

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

             :param timestamp: The data returned will represent the cdp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of cdp neighbor methods. The listed methods will be called on each cdp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
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
            |  ``default:`` CDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is CDPNeighborID. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC.
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

             :param select: The list of attributes to return for each CdpNeighbor. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC. If empty or omitted, all attributes will be returned.
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

             :return cdp_neighbors: An array of the CdpNeighbor objects that match the specified input criteria.
             :rtype cdp_neighbors: Array of CdpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available cdp neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborCapabilities: The neighbor capabilities, as reported by CDP.
             :type CDPNeighborCapabilities: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborCapabilities: The neighbor capabilities, as reported by CDP.
             :type CDPNeighborCapabilities: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type CDPNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type CDPNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDescription: The description of the neighbor, as reported by CDP.
             :type CDPNeighborDescription: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDescription: The description of the neighbor, as reported by CDP.
             :type CDPNeighborDescription: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by CDP, if available.
             :type CDPNeighborDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by CDP, if available.
             :type CDPNeighborDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type CDPNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type CDPNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIPDotted: The management IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by CDP.
             :type CDPNeighborIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIPDotted: The management IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by CDP.
             :type CDPNeighborIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIPNumeric: The numerical value of the management IP address that was reported by CDP.
             :type CDPNeighborIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIPNumeric: The numerical value of the management IP address that was reported by CDP.
             :type CDPNeighborIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIfIndex: The SNMP index for the neighbor interface reported by CDP, if available.
             :type CDPNeighborIfIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborIfIndex: The SNMP index for the neighbor interface reported by CDP, if available.
             :type CDPNeighborIfIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by CDP, if available.
             :type CDPNeighborInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by CDP, if available.
             :type CDPNeighborInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by CDP.
             :type CDPNeighborMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by CDP.
             :type CDPNeighborMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type CDPNeighborMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type CDPNeighborMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborOrigTable: Internal tracking information for NetMRI algorithms.
             :type CDPNeighborOrigTable: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborOrigTable: Internal tracking information for NetMRI algorithms.
             :type CDPNeighborOrigTable: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborPlatform: The platform description of the neighbor, as reported by CDP.
             :type CDPNeighborPlatform: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborPlatform: The platform description of the neighbor, as reported by CDP.
             :type CDPNeighborPlatform: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborPortName: The port name of the neighbor interface, as reported by CDP.
             :type CDPNeighborPortName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborPortName: The port name of the neighbor interface, as reported by CDP.
             :type CDPNeighborPortName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborStartTime: The starting effective time of this revision of the record.
             :type CDPNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborStartTime: The starting effective time of this revision of the record.
             :type CDPNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborTimestamp: The date and time this record was collected or calculated.
             :type CDPNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborTimestamp: The date and time this record was collected or calculated.
             :type CDPNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborVersion: The version of the neighbor, as reported by CDP.
             :type CDPNeighborVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CDPNeighborVersion: The version of the neighbor, as reported by CDP.
             :type CDPNeighborVersion: Array of String

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

             :param DeviceID: The internal NetMRI identifier for the device from which this CDP data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this CDP data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this CDP neighbor table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this CDP neighbor table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this CDP neighbor table entry.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this CDP neighbor table entry.
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

             :param timestamp: The data returned will represent the cdp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of cdp neighbor methods. The listed methods will be called on each cdp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
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
            |  ``default:`` CDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is CDPNeighborID. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC.
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

             :param select: The list of attributes to return for each CdpNeighbor. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against cdp neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: CDPNeighborCapabilities, CDPNeighborChangedCols, CDPNeighborDescription, CDPNeighborDeviceID, CDPNeighborEndTime, CDPNeighborID, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborIfIndex, CDPNeighborInterfaceID, CDPNeighborMAC, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborPlatform, CDPNeighborPortName, CDPNeighborStartTime, CDPNeighborTimestamp, CDPNeighborVersion, DataSourceID, DeviceID, InterfaceID, ifIndex.
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

             :return cdp_neighbors: An array of the CdpNeighbor objects that match the specified input criteria.
             :rtype cdp_neighbors: Array of CdpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available cdp neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: CDPNeighborCapabilities, CDPNeighborChangedCols, CDPNeighborDescription, CDPNeighborDeviceID, CDPNeighborEndTime, CDPNeighborID, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborIfIndex, CDPNeighborInterfaceID, CDPNeighborMAC, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborPlatform, CDPNeighborPortName, CDPNeighborStartTime, CDPNeighborTimestamp, CDPNeighborVersion, DataSourceID, DeviceID, InterfaceID, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborCapabilities: The operator to apply to the field CDPNeighborCapabilities. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborCapabilities: The neighbor capabilities, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborCapabilities: If op_CDPNeighborCapabilities is specified, the field named in this input will be compared to the value in CDPNeighborCapabilities using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborCapabilities must be specified if op_CDPNeighborCapabilities is specified.
             :type val_f_CDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborCapabilities: If op_CDPNeighborCapabilities is specified, this value will be compared to the value in CDPNeighborCapabilities using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborCapabilities must be specified if op_CDPNeighborCapabilities is specified.
             :type val_c_CDPNeighborCapabilities: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborChangedCols: The operator to apply to the field CDPNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborChangedCols: If op_CDPNeighborChangedCols is specified, the field named in this input will be compared to the value in CDPNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborChangedCols must be specified if op_CDPNeighborChangedCols is specified.
             :type val_f_CDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborChangedCols: If op_CDPNeighborChangedCols is specified, this value will be compared to the value in CDPNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborChangedCols must be specified if op_CDPNeighborChangedCols is specified.
             :type val_c_CDPNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborDescription: The operator to apply to the field CDPNeighborDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborDescription: The description of the neighbor, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborDescription: If op_CDPNeighborDescription is specified, the field named in this input will be compared to the value in CDPNeighborDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborDescription must be specified if op_CDPNeighborDescription is specified.
             :type val_f_CDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborDescription: If op_CDPNeighborDescription is specified, this value will be compared to the value in CDPNeighborDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborDescription must be specified if op_CDPNeighborDescription is specified.
             :type val_c_CDPNeighborDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborDeviceID: The operator to apply to the field CDPNeighborDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborDeviceID: The internal NetMRI identifier for the neighbor device reported by CDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborDeviceID: If op_CDPNeighborDeviceID is specified, the field named in this input will be compared to the value in CDPNeighborDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborDeviceID must be specified if op_CDPNeighborDeviceID is specified.
             :type val_f_CDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborDeviceID: If op_CDPNeighborDeviceID is specified, this value will be compared to the value in CDPNeighborDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborDeviceID must be specified if op_CDPNeighborDeviceID is specified.
             :type val_c_CDPNeighborDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborEndTime: The operator to apply to the field CDPNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborEndTime: If op_CDPNeighborEndTime is specified, the field named in this input will be compared to the value in CDPNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborEndTime must be specified if op_CDPNeighborEndTime is specified.
             :type val_f_CDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborEndTime: If op_CDPNeighborEndTime is specified, this value will be compared to the value in CDPNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborEndTime must be specified if op_CDPNeighborEndTime is specified.
             :type val_c_CDPNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborID: The operator to apply to the field CDPNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborID: The internal NetMRI identifier for this CDP table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborID: If op_CDPNeighborID is specified, the field named in this input will be compared to the value in CDPNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborID must be specified if op_CDPNeighborID is specified.
             :type val_f_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborID: If op_CDPNeighborID is specified, this value will be compared to the value in CDPNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborID must be specified if op_CDPNeighborID is specified.
             :type val_c_CDPNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborIPDotted: The operator to apply to the field CDPNeighborIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborIPDotted: The management IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborIPDotted: If op_CDPNeighborIPDotted is specified, the field named in this input will be compared to the value in CDPNeighborIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborIPDotted must be specified if op_CDPNeighborIPDotted is specified.
             :type val_f_CDPNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborIPDotted: If op_CDPNeighborIPDotted is specified, this value will be compared to the value in CDPNeighborIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborIPDotted must be specified if op_CDPNeighborIPDotted is specified.
             :type val_c_CDPNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborIPNumeric: The operator to apply to the field CDPNeighborIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborIPNumeric: The numerical value of the management IP address that was reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborIPNumeric: If op_CDPNeighborIPNumeric is specified, the field named in this input will be compared to the value in CDPNeighborIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborIPNumeric must be specified if op_CDPNeighborIPNumeric is specified.
             :type val_f_CDPNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborIPNumeric: If op_CDPNeighborIPNumeric is specified, this value will be compared to the value in CDPNeighborIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborIPNumeric must be specified if op_CDPNeighborIPNumeric is specified.
             :type val_c_CDPNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborIfIndex: The operator to apply to the field CDPNeighborIfIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborIfIndex: The SNMP index for the neighbor interface reported by CDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborIfIndex: If op_CDPNeighborIfIndex is specified, the field named in this input will be compared to the value in CDPNeighborIfIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborIfIndex must be specified if op_CDPNeighborIfIndex is specified.
             :type val_f_CDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborIfIndex: If op_CDPNeighborIfIndex is specified, this value will be compared to the value in CDPNeighborIfIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborIfIndex must be specified if op_CDPNeighborIfIndex is specified.
             :type val_c_CDPNeighborIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborInterfaceID: The operator to apply to the field CDPNeighborInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborInterfaceID: The internal NetMRI identifier for the neighbor interface reported by CDP, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborInterfaceID: If op_CDPNeighborInterfaceID is specified, the field named in this input will be compared to the value in CDPNeighborInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborInterfaceID must be specified if op_CDPNeighborInterfaceID is specified.
             :type val_f_CDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborInterfaceID: If op_CDPNeighborInterfaceID is specified, this value will be compared to the value in CDPNeighborInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborInterfaceID must be specified if op_CDPNeighborInterfaceID is specified.
             :type val_c_CDPNeighborInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborMAC: The operator to apply to the field CDPNeighborMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborMAC: The Media Access Controller (MAC) address of the neighbor, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborMAC: If op_CDPNeighborMAC is specified, the field named in this input will be compared to the value in CDPNeighborMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborMAC must be specified if op_CDPNeighborMAC is specified.
             :type val_f_CDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborMAC: If op_CDPNeighborMAC is specified, this value will be compared to the value in CDPNeighborMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborMAC must be specified if op_CDPNeighborMAC is specified.
             :type val_c_CDPNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborMapSource: The operator to apply to the field CDPNeighborMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborMapSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborMapSource: If op_CDPNeighborMapSource is specified, the field named in this input will be compared to the value in CDPNeighborMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborMapSource must be specified if op_CDPNeighborMapSource is specified.
             :type val_f_CDPNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborMapSource: If op_CDPNeighborMapSource is specified, this value will be compared to the value in CDPNeighborMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborMapSource must be specified if op_CDPNeighborMapSource is specified.
             :type val_c_CDPNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborOrigTable: The operator to apply to the field CDPNeighborOrigTable. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborOrigTable: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborOrigTable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborOrigTable: If op_CDPNeighborOrigTable is specified, the field named in this input will be compared to the value in CDPNeighborOrigTable using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborOrigTable must be specified if op_CDPNeighborOrigTable is specified.
             :type val_f_CDPNeighborOrigTable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborOrigTable: If op_CDPNeighborOrigTable is specified, this value will be compared to the value in CDPNeighborOrigTable using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborOrigTable must be specified if op_CDPNeighborOrigTable is specified.
             :type val_c_CDPNeighborOrigTable: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborPlatform: The operator to apply to the field CDPNeighborPlatform. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborPlatform: The platform description of the neighbor, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborPlatform: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborPlatform: If op_CDPNeighborPlatform is specified, the field named in this input will be compared to the value in CDPNeighborPlatform using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborPlatform must be specified if op_CDPNeighborPlatform is specified.
             :type val_f_CDPNeighborPlatform: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborPlatform: If op_CDPNeighborPlatform is specified, this value will be compared to the value in CDPNeighborPlatform using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborPlatform must be specified if op_CDPNeighborPlatform is specified.
             :type val_c_CDPNeighborPlatform: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborPortName: The operator to apply to the field CDPNeighborPortName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborPortName: The port name of the neighbor interface, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborPortName: If op_CDPNeighborPortName is specified, the field named in this input will be compared to the value in CDPNeighborPortName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborPortName must be specified if op_CDPNeighborPortName is specified.
             :type val_f_CDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborPortName: If op_CDPNeighborPortName is specified, this value will be compared to the value in CDPNeighborPortName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborPortName must be specified if op_CDPNeighborPortName is specified.
             :type val_c_CDPNeighborPortName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborStartTime: The operator to apply to the field CDPNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborStartTime: If op_CDPNeighborStartTime is specified, the field named in this input will be compared to the value in CDPNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborStartTime must be specified if op_CDPNeighborStartTime is specified.
             :type val_f_CDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborStartTime: If op_CDPNeighborStartTime is specified, this value will be compared to the value in CDPNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborStartTime must be specified if op_CDPNeighborStartTime is specified.
             :type val_c_CDPNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborTimestamp: The operator to apply to the field CDPNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborTimestamp: If op_CDPNeighborTimestamp is specified, the field named in this input will be compared to the value in CDPNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborTimestamp must be specified if op_CDPNeighborTimestamp is specified.
             :type val_f_CDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborTimestamp: If op_CDPNeighborTimestamp is specified, this value will be compared to the value in CDPNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborTimestamp must be specified if op_CDPNeighborTimestamp is specified.
             :type val_c_CDPNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CDPNeighborVersion: The operator to apply to the field CDPNeighborVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CDPNeighborVersion: The version of the neighbor, as reported by CDP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CDPNeighborVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CDPNeighborVersion: If op_CDPNeighborVersion is specified, the field named in this input will be compared to the value in CDPNeighborVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CDPNeighborVersion must be specified if op_CDPNeighborVersion is specified.
             :type val_f_CDPNeighborVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CDPNeighborVersion: If op_CDPNeighborVersion is specified, this value will be compared to the value in CDPNeighborVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CDPNeighborVersion must be specified if op_CDPNeighborVersion is specified.
             :type val_c_CDPNeighborVersion: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this CDP data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the local interface for this CDP neighbor table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index for the local interface for this CDP neighbor table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param timestamp: The data returned will represent the cdp neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of cdp neighbor methods. The listed methods will be called on each cdp neighbor returned and included in the output. Available methods are: data_source, device, interface, neighbor_device, neighbor_interface, infradevice.
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
            |  ``default:`` CDPNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is CDPNeighborID. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC.
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

             :param select: The list of attributes to return for each CdpNeighbor. Valid values are DataSourceID, CDPNeighborID, DeviceID, InterfaceID, ifIndex, CDPNeighborDeviceID, CDPNeighborInterfaceID, CDPNeighborIfIndex, CDPNeighborStartTime, CDPNeighborEndTime, CDPNeighborChangedCols, CDPNeighborTimestamp, CDPNeighborMapSource, CDPNeighborOrigTable, CDPNeighborVersion, CDPNeighborDescription, CDPNeighborPortName, CDPNeighborPlatform, CDPNeighborCapabilities, CDPNeighborIPDotted, CDPNeighborIPNumeric, CDPNeighborMAC. If empty or omitted, all attributes will be returned.
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

             :return cdp_neighbors: An array of the CdpNeighbor objects that match the specified input criteria.
             :rtype cdp_neighbors: Array of CdpNeighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def interface(self, **kwargs):
        """The local interface for this CDP neighbor table entry.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The local interface for this CDP neighbor table entry.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def neighbor_interface(self, **kwargs):
        """The neighbor interface reported by CDP, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The neighbor interface reported by CDP, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("neighbor_interface"), kwargs)

    def neighbor_device(self, **kwargs):
        """The neighbor device reported by CDP, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The neighbor device reported by CDP, if available.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("neighbor_device"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this CDP data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this CDP data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this CDP data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param CDPNeighborID: The internal NetMRI identifier for this CDP table entry.
             :type CDPNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this CDP data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
