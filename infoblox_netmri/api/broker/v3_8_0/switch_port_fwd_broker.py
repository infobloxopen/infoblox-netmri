from ..broker import Broker


class SwitchPortFwdBroker(Broker):
    controller = "switch_port_fwds"

    def show(self, **kwargs):
        """Shows the details for the specified switch port fwd.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry.
             :type SwitchPortFwdID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch port fwd methods. The listed methods will be called on each switch port fwd returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return switch_port_fwd: The switch port fwd identified by the specified SwitchPortFwdID.
             :rtype switch_port_fwd: SwitchPortFwd

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available switch port fwds. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this switch port forwarding entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this switch port forwarding entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which this switch forwarding entry was found.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which this switch forwarding entry was found.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry.
             :type SwitchPortFwdID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry.
             :type SwitchPortFwdID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdMAC: The MAC address that is being forwarded.
             :type SwitchPortFwdMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdMAC: The MAC address that is being forwarded.
             :type SwitchPortFwdMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStartTime: The starting effective time of this record.
             :type SwitchPortFwdStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStartTime: The starting effective time of this record.
             :type SwitchPortFwdStartTime: Array of DateTime

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

             :param timestamp: The data returned will represent the switch port fwds as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch port fwd methods. The listed methods will be called on each switch port fwd returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` SwitchPortFwdID

             :param sort: The data field(s) to use for sorting the output. Default is SwitchPortFwdID. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID.
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

             :param select: The list of attributes to return for each SwitchPortFwd. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID. If empty or omitted, all attributes will be returned.
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

             :return switch_port_fwds: An array of the SwitchPortFwd objects that match the specified input criteria.
             :rtype switch_port_fwds: Array of SwitchPortFwd

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available switch port fwds matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device from which this switch port forwarding entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this switch port forwarding entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which this switch forwarding entry was found.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface on which this switch forwarding entry was found.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SwitchPortFwdChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SwitchPortFwdChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdDeviceID: The internal NetMRI identifier of the device to which the MAC address corresponds (that is, the destination device).
             :type SwitchPortFwdDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdDeviceID: The internal NetMRI identifier of the device to which the MAC address corresponds (that is, the destination device).
             :type SwitchPortFwdDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdEndTime: The ending effective time of this record, or empty if still in effect.
             :type SwitchPortFwdEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdEndTime: The ending effective time of this record, or empty if still in effect.
             :type SwitchPortFwdEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry.
             :type SwitchPortFwdID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry.
             :type SwitchPortFwdID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdInterfaceID: The internal NetMRI identifier of the interface to which the MAC address corresponds (that is, the destination interface).
             :type SwitchPortFwdInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdInterfaceID: The internal NetMRI identifier of the interface to which the MAC address corresponds (that is, the destination interface).
             :type SwitchPortFwdInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdMAC: The MAC address that is being forwarded.
             :type SwitchPortFwdMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdMAC: The MAC address that is being forwarded.
             :type SwitchPortFwdMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStartTime: The starting effective time of this record.
             :type SwitchPortFwdStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStartTime: The starting effective time of this record.
             :type SwitchPortFwdStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStatus: The status of this entry; indicates how the entry was entered in the switch forwarding table.
             :type SwitchPortFwdStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdStatus: The status of this entry; indicates how the entry was entered in the switch forwarding table.
             :type SwitchPortFwdStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdTimestamp: The date and time this record was collected or calculated.
             :type SwitchPortFwdTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdTimestamp: The date and time this record was collected or calculated.
             :type SwitchPortFwdTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdVlanID: The internal NetMRI identifier for the VLAN for which this MAC address is forwarded.
             :type SwitchPortFwdVlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdVlanID: The internal NetMRI identifier for the VLAN for which this MAC address is forwarded.
             :type SwitchPortFwdVlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdVlanIndex: The VLAN number for which this MAC address is forwarded.
             :type SwitchPortFwdVlanIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortFwdVlanIndex: The VLAN number for which this MAC address is forwarded.
             :type SwitchPortFwdVlanIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortNumber: The switch port number for the port on which this switch forwarding entry was found. This is as reported by the SNMP BRIDGE MIB, and is not the same as the SNMP interface index.
             :type SwitchPortNumber: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortNumber: The switch port number for the port on which this switch forwarding entry was found. This is as reported by the SNMP BRIDGE MIB, and is not the same as the SNMP interface index.
             :type SwitchPortNumber: Array of String

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

             :param timestamp: The data returned will represent the switch port fwds as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch port fwd methods. The listed methods will be called on each switch port fwd returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` SwitchPortFwdID

             :param sort: The data field(s) to use for sorting the output. Default is SwitchPortFwdID. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID.
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

             :param select: The list of attributes to return for each SwitchPortFwd. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against switch port fwds, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, InterfaceID, SwitchPortFwdChangedCols, SwitchPortFwdDeviceID, SwitchPortFwdEndTime, SwitchPortFwdID, SwitchPortFwdInterfaceID, SwitchPortFwdMAC, SwitchPortFwdStartTime, SwitchPortFwdStatus, SwitchPortFwdTimestamp, SwitchPortFwdVlanID, SwitchPortFwdVlanIndex, SwitchPortNumber.
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

             :return switch_port_fwds: An array of the SwitchPortFwd objects that match the specified input criteria.
             :rtype switch_port_fwds: Array of SwitchPortFwd

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available switch port fwds matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, InterfaceID, SwitchPortFwdChangedCols, SwitchPortFwdDeviceID, SwitchPortFwdEndTime, SwitchPortFwdID, SwitchPortFwdInterfaceID, SwitchPortFwdMAC, SwitchPortFwdStartTime, SwitchPortFwdStatus, SwitchPortFwdTimestamp, SwitchPortFwdVlanID, SwitchPortFwdVlanIndex, SwitchPortNumber.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this switch port forwarding entry was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the interface on which this switch forwarding entry was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SwitchPortFwdChangedCols: The operator to apply to the field SwitchPortFwdChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdChangedCols: If op_SwitchPortFwdChangedCols is specified, the field named in this input will be compared to the value in SwitchPortFwdChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdChangedCols must be specified if op_SwitchPortFwdChangedCols is specified.
             :type val_f_SwitchPortFwdChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdChangedCols: If op_SwitchPortFwdChangedCols is specified, this value will be compared to the value in SwitchPortFwdChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdChangedCols must be specified if op_SwitchPortFwdChangedCols is specified.
             :type val_c_SwitchPortFwdChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdDeviceID: The operator to apply to the field SwitchPortFwdDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdDeviceID: The internal NetMRI identifier of the device to which the MAC address corresponds (that is, the destination device). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdDeviceID: If op_SwitchPortFwdDeviceID is specified, the field named in this input will be compared to the value in SwitchPortFwdDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdDeviceID must be specified if op_SwitchPortFwdDeviceID is specified.
             :type val_f_SwitchPortFwdDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdDeviceID: If op_SwitchPortFwdDeviceID is specified, this value will be compared to the value in SwitchPortFwdDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdDeviceID must be specified if op_SwitchPortFwdDeviceID is specified.
             :type val_c_SwitchPortFwdDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdEndTime: The operator to apply to the field SwitchPortFwdEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdEndTime: If op_SwitchPortFwdEndTime is specified, the field named in this input will be compared to the value in SwitchPortFwdEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdEndTime must be specified if op_SwitchPortFwdEndTime is specified.
             :type val_f_SwitchPortFwdEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdEndTime: If op_SwitchPortFwdEndTime is specified, this value will be compared to the value in SwitchPortFwdEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdEndTime must be specified if op_SwitchPortFwdEndTime is specified.
             :type val_c_SwitchPortFwdEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdID: The operator to apply to the field SwitchPortFwdID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdID: The internal NetMRI identifier for this switch port forwarding entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdID: If op_SwitchPortFwdID is specified, the field named in this input will be compared to the value in SwitchPortFwdID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdID must be specified if op_SwitchPortFwdID is specified.
             :type val_f_SwitchPortFwdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdID: If op_SwitchPortFwdID is specified, this value will be compared to the value in SwitchPortFwdID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdID must be specified if op_SwitchPortFwdID is specified.
             :type val_c_SwitchPortFwdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdInterfaceID: The operator to apply to the field SwitchPortFwdInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdInterfaceID: The internal NetMRI identifier of the interface to which the MAC address corresponds (that is, the destination interface). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdInterfaceID: If op_SwitchPortFwdInterfaceID is specified, the field named in this input will be compared to the value in SwitchPortFwdInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdInterfaceID must be specified if op_SwitchPortFwdInterfaceID is specified.
             :type val_f_SwitchPortFwdInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdInterfaceID: If op_SwitchPortFwdInterfaceID is specified, this value will be compared to the value in SwitchPortFwdInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdInterfaceID must be specified if op_SwitchPortFwdInterfaceID is specified.
             :type val_c_SwitchPortFwdInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdMAC: The operator to apply to the field SwitchPortFwdMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdMAC: The MAC address that is being forwarded. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdMAC: If op_SwitchPortFwdMAC is specified, the field named in this input will be compared to the value in SwitchPortFwdMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdMAC must be specified if op_SwitchPortFwdMAC is specified.
             :type val_f_SwitchPortFwdMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdMAC: If op_SwitchPortFwdMAC is specified, this value will be compared to the value in SwitchPortFwdMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdMAC must be specified if op_SwitchPortFwdMAC is specified.
             :type val_c_SwitchPortFwdMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdStartTime: The operator to apply to the field SwitchPortFwdStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdStartTime: If op_SwitchPortFwdStartTime is specified, the field named in this input will be compared to the value in SwitchPortFwdStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdStartTime must be specified if op_SwitchPortFwdStartTime is specified.
             :type val_f_SwitchPortFwdStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdStartTime: If op_SwitchPortFwdStartTime is specified, this value will be compared to the value in SwitchPortFwdStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdStartTime must be specified if op_SwitchPortFwdStartTime is specified.
             :type val_c_SwitchPortFwdStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdStatus: The operator to apply to the field SwitchPortFwdStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdStatus: The status of this entry; indicates how the entry was entered in the switch forwarding table. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdStatus: If op_SwitchPortFwdStatus is specified, the field named in this input will be compared to the value in SwitchPortFwdStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdStatus must be specified if op_SwitchPortFwdStatus is specified.
             :type val_f_SwitchPortFwdStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdStatus: If op_SwitchPortFwdStatus is specified, this value will be compared to the value in SwitchPortFwdStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdStatus must be specified if op_SwitchPortFwdStatus is specified.
             :type val_c_SwitchPortFwdStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdTimestamp: The operator to apply to the field SwitchPortFwdTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdTimestamp: If op_SwitchPortFwdTimestamp is specified, the field named in this input will be compared to the value in SwitchPortFwdTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdTimestamp must be specified if op_SwitchPortFwdTimestamp is specified.
             :type val_f_SwitchPortFwdTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdTimestamp: If op_SwitchPortFwdTimestamp is specified, this value will be compared to the value in SwitchPortFwdTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdTimestamp must be specified if op_SwitchPortFwdTimestamp is specified.
             :type val_c_SwitchPortFwdTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdVlanID: The operator to apply to the field SwitchPortFwdVlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdVlanID: The internal NetMRI identifier for the VLAN for which this MAC address is forwarded. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdVlanID: If op_SwitchPortFwdVlanID is specified, the field named in this input will be compared to the value in SwitchPortFwdVlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdVlanID must be specified if op_SwitchPortFwdVlanID is specified.
             :type val_f_SwitchPortFwdVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdVlanID: If op_SwitchPortFwdVlanID is specified, this value will be compared to the value in SwitchPortFwdVlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdVlanID must be specified if op_SwitchPortFwdVlanID is specified.
             :type val_c_SwitchPortFwdVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortFwdVlanIndex: The operator to apply to the field SwitchPortFwdVlanIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortFwdVlanIndex: The VLAN number for which this MAC address is forwarded. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortFwdVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortFwdVlanIndex: If op_SwitchPortFwdVlanIndex is specified, the field named in this input will be compared to the value in SwitchPortFwdVlanIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortFwdVlanIndex must be specified if op_SwitchPortFwdVlanIndex is specified.
             :type val_f_SwitchPortFwdVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortFwdVlanIndex: If op_SwitchPortFwdVlanIndex is specified, this value will be compared to the value in SwitchPortFwdVlanIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortFwdVlanIndex must be specified if op_SwitchPortFwdVlanIndex is specified.
             :type val_c_SwitchPortFwdVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortNumber: The operator to apply to the field SwitchPortNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortNumber: The switch port number for the port on which this switch forwarding entry was found. This is as reported by the SNMP BRIDGE MIB, and is not the same as the SNMP interface index. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortNumber: If op_SwitchPortNumber is specified, the field named in this input will be compared to the value in SwitchPortNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortNumber must be specified if op_SwitchPortNumber is specified.
             :type val_f_SwitchPortNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortNumber: If op_SwitchPortNumber is specified, this value will be compared to the value in SwitchPortNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortNumber must be specified if op_SwitchPortNumber is specified.
             :type val_c_SwitchPortNumber: String

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

             :param timestamp: The data returned will represent the switch port fwds as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch port fwd methods. The listed methods will be called on each switch port fwd returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` SwitchPortFwdID

             :param sort: The data field(s) to use for sorting the output. Default is SwitchPortFwdID. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID.
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

             :param select: The list of attributes to return for each SwitchPortFwd. Valid values are SwitchPortFwdID, DataSourceID, DeviceID, SwitchPortNumber, InterfaceID, SwitchPortFwdStartTime, SwitchPortFwdEndTime, SwitchPortFwdChangedCols, SwitchPortFwdTimestamp, SwitchPortFwdMAC, SwitchPortFwdStatus, SwitchPortFwdVlanIndex, SwitchPortFwdVlanID, SwitchPortFwdInterfaceID, SwitchPortFwdDeviceID. If empty or omitted, all attributes will be returned.
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

             :return switch_port_fwds: An array of the SwitchPortFwd objects that match the specified input criteria.
             :rtype switch_port_fwds: Array of SwitchPortFwd

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
