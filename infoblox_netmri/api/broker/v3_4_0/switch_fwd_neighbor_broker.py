from ..broker import Broker


class SwitchFwdNeighborBroker(Broker):
    controller = "switch_fwd_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified switch fwd neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch fwd neighbor methods. The listed methods will be called on each switch fwd neighbor returned and included in the output. Available methods are: network_name.
             :type methods: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return switch_fwd_neighbor: The switch fwd neighbor identified by the specified NeighborID.
             :rtype switch_fwd_neighbor: SwitchFwdNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available switch fwd neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMAC: The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship.
             :type SwitchFwdNeighborMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMAC: The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship.
             :type SwitchFwdNeighborMAC: Array of String

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

             :param timestamp: The data returned will represent the switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch fwd neighbor methods. The listed methods will be called on each switch fwd neighbor returned and included in the output. Available methods are: network_name.
             :type methods: Array of String

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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex.
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

             :param select: The list of attributes to return for each SwitchFwdNeighbor. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex. If empty or omitted, all attributes will be returned.
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

             :return switch_fwd_neighbors: An array of the SwitchFwdNeighbor objects that match the specified input criteria.
             :rtype switch_fwd_neighbors: Array of SwitchFwdNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available switch fwd neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SwitchFwdNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SwitchFwdNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SwitchFwdNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SwitchFwdNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborFirstSeenTime: The date and time this switch forwarding neighbor was first seen on the network, and since which it has been continuously present.
             :type SwitchFwdNeighborFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborFirstSeenTime: The date and time this switch forwarding neighbor was first seen on the network, and since which it has been continuously present.
             :type SwitchFwdNeighborFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborIPDotted: The IP address corresponding to the MAC found in the switch forwarding table, in dotted (or colon-delimited for IPv6) format.
             :type SwitchFwdNeighborIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborIPDotted: The IP address corresponding to the MAC found in the switch forwarding table, in dotted (or colon-delimited for IPv6) format.
             :type SwitchFwdNeighborIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborIPNumeric: The numerical value of the IP address corresponding to the MAC found in the switch forwarding table.
             :type SwitchFwdNeighborIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborIPNumeric: The numerical value of the IP address corresponding to the MAC found in the switch forwarding table.
             :type SwitchFwdNeighborIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMAC: The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship.
             :type SwitchFwdNeighborMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMAC: The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship.
             :type SwitchFwdNeighborMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type SwitchFwdNeighborMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type SwitchFwdNeighborMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborStartTime: The starting effective time of this revision of the record.
             :type SwitchFwdNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborStartTime: The starting effective time of this revision of the record.
             :type SwitchFwdNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborTimestamp: The date and time this record was collected or calculated.
             :type SwitchFwdNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborTimestamp: The date and time this record was collected or calculated.
             :type SwitchFwdNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborType: Internal tracking information for NetMRI algorithms.
             :type SwitchFwdNeighborType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborType: Internal tracking information for NetMRI algorithms.
             :type SwitchFwdNeighborType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborVlanID: The internal NetMRI identifier for the VLAN of this neighbor.
             :type SwitchFwdNeighborVlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborVlanID: The internal NetMRI identifier for the VLAN of this neighbor.
             :type SwitchFwdNeighborVlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborVlanIndex: The numerical VLAN number (VLAN ID) of this neighbor.
             :type SwitchFwdNeighborVlanIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborVlanIndex: The numerical VLAN number (VLAN ID) of this neighbor.
             :type SwitchFwdNeighborVlanIndex: Array of Integer

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

             :param timestamp: The data returned will represent the switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch fwd neighbor methods. The listed methods will be called on each switch fwd neighbor returned and included in the output. Available methods are: network_name.
             :type methods: Array of String

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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex.
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

             :param select: The list of attributes to return for each SwitchFwdNeighbor. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against switch fwd neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, NeighborID, SwitchFwdNeighborChangedCols, SwitchFwdNeighborEndTime, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborMAC, SwitchFwdNeighborMapSource, SwitchFwdNeighborStartTime, SwitchFwdNeighborTimestamp, SwitchFwdNeighborType, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex.
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

             :return switch_fwd_neighbors: An array of the SwitchFwdNeighbor objects that match the specified input criteria.
             :rtype switch_fwd_neighbors: Array of SwitchFwdNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available switch fwd neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, NeighborID, SwitchFwdNeighborChangedCols, SwitchFwdNeighborEndTime, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborMAC, SwitchFwdNeighborMapSource, SwitchFwdNeighborStartTime, SwitchFwdNeighborTimestamp, SwitchFwdNeighborType, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex.

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

             :param op_NeighborID: The operator to apply to the field NeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborID: If op_NeighborID is specified, the field named in this input will be compared to the value in NeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborID must be specified if op_NeighborID is specified.
             :type val_f_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborID: If op_NeighborID is specified, this value will be compared to the value in NeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborID must be specified if op_NeighborID is specified.
             :type val_c_NeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborChangedCols: The operator to apply to the field SwitchFwdNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborChangedCols: If op_SwitchFwdNeighborChangedCols is specified, the field named in this input will be compared to the value in SwitchFwdNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborChangedCols must be specified if op_SwitchFwdNeighborChangedCols is specified.
             :type val_f_SwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborChangedCols: If op_SwitchFwdNeighborChangedCols is specified, this value will be compared to the value in SwitchFwdNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborChangedCols must be specified if op_SwitchFwdNeighborChangedCols is specified.
             :type val_c_SwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborEndTime: The operator to apply to the field SwitchFwdNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborEndTime: If op_SwitchFwdNeighborEndTime is specified, the field named in this input will be compared to the value in SwitchFwdNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborEndTime must be specified if op_SwitchFwdNeighborEndTime is specified.
             :type val_f_SwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborEndTime: If op_SwitchFwdNeighborEndTime is specified, this value will be compared to the value in SwitchFwdNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborEndTime must be specified if op_SwitchFwdNeighborEndTime is specified.
             :type val_c_SwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborFirstSeenTime: The operator to apply to the field SwitchFwdNeighborFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborFirstSeenTime: The date and time this switch forwarding neighbor was first seen on the network, and since which it has been continuously present. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborFirstSeenTime: If op_SwitchFwdNeighborFirstSeenTime is specified, the field named in this input will be compared to the value in SwitchFwdNeighborFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborFirstSeenTime must be specified if op_SwitchFwdNeighborFirstSeenTime is specified.
             :type val_f_SwitchFwdNeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborFirstSeenTime: If op_SwitchFwdNeighborFirstSeenTime is specified, this value will be compared to the value in SwitchFwdNeighborFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborFirstSeenTime must be specified if op_SwitchFwdNeighborFirstSeenTime is specified.
             :type val_c_SwitchFwdNeighborFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborIPDotted: The operator to apply to the field SwitchFwdNeighborIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborIPDotted: The IP address corresponding to the MAC found in the switch forwarding table, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborIPDotted: If op_SwitchFwdNeighborIPDotted is specified, the field named in this input will be compared to the value in SwitchFwdNeighborIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborIPDotted must be specified if op_SwitchFwdNeighborIPDotted is specified.
             :type val_f_SwitchFwdNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborIPDotted: If op_SwitchFwdNeighborIPDotted is specified, this value will be compared to the value in SwitchFwdNeighborIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborIPDotted must be specified if op_SwitchFwdNeighborIPDotted is specified.
             :type val_c_SwitchFwdNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborIPNumeric: The operator to apply to the field SwitchFwdNeighborIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborIPNumeric: The numerical value of the IP address corresponding to the MAC found in the switch forwarding table. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborIPNumeric: If op_SwitchFwdNeighborIPNumeric is specified, the field named in this input will be compared to the value in SwitchFwdNeighborIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborIPNumeric must be specified if op_SwitchFwdNeighborIPNumeric is specified.
             :type val_f_SwitchFwdNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborIPNumeric: If op_SwitchFwdNeighborIPNumeric is specified, this value will be compared to the value in SwitchFwdNeighborIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborIPNumeric must be specified if op_SwitchFwdNeighborIPNumeric is specified.
             :type val_c_SwitchFwdNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborMAC: The operator to apply to the field SwitchFwdNeighborMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborMAC: The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborMAC: If op_SwitchFwdNeighborMAC is specified, the field named in this input will be compared to the value in SwitchFwdNeighborMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborMAC must be specified if op_SwitchFwdNeighborMAC is specified.
             :type val_f_SwitchFwdNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborMAC: If op_SwitchFwdNeighborMAC is specified, this value will be compared to the value in SwitchFwdNeighborMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborMAC must be specified if op_SwitchFwdNeighborMAC is specified.
             :type val_c_SwitchFwdNeighborMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborMapSource: The operator to apply to the field SwitchFwdNeighborMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborMapSource: If op_SwitchFwdNeighborMapSource is specified, the field named in this input will be compared to the value in SwitchFwdNeighborMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborMapSource must be specified if op_SwitchFwdNeighborMapSource is specified.
             :type val_f_SwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborMapSource: If op_SwitchFwdNeighborMapSource is specified, this value will be compared to the value in SwitchFwdNeighborMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborMapSource must be specified if op_SwitchFwdNeighborMapSource is specified.
             :type val_c_SwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborStartTime: The operator to apply to the field SwitchFwdNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborStartTime: If op_SwitchFwdNeighborStartTime is specified, the field named in this input will be compared to the value in SwitchFwdNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborStartTime must be specified if op_SwitchFwdNeighborStartTime is specified.
             :type val_f_SwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborStartTime: If op_SwitchFwdNeighborStartTime is specified, this value will be compared to the value in SwitchFwdNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborStartTime must be specified if op_SwitchFwdNeighborStartTime is specified.
             :type val_c_SwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborTimestamp: The operator to apply to the field SwitchFwdNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborTimestamp: If op_SwitchFwdNeighborTimestamp is specified, the field named in this input will be compared to the value in SwitchFwdNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborTimestamp must be specified if op_SwitchFwdNeighborTimestamp is specified.
             :type val_f_SwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborTimestamp: If op_SwitchFwdNeighborTimestamp is specified, this value will be compared to the value in SwitchFwdNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborTimestamp must be specified if op_SwitchFwdNeighborTimestamp is specified.
             :type val_c_SwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborType: The operator to apply to the field SwitchFwdNeighborType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborType: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborType: If op_SwitchFwdNeighborType is specified, the field named in this input will be compared to the value in SwitchFwdNeighborType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborType must be specified if op_SwitchFwdNeighborType is specified.
             :type val_f_SwitchFwdNeighborType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborType: If op_SwitchFwdNeighborType is specified, this value will be compared to the value in SwitchFwdNeighborType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborType must be specified if op_SwitchFwdNeighborType is specified.
             :type val_c_SwitchFwdNeighborType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborVlanID: The operator to apply to the field SwitchFwdNeighborVlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborVlanID: The internal NetMRI identifier for the VLAN of this neighbor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborVlanID: If op_SwitchFwdNeighborVlanID is specified, the field named in this input will be compared to the value in SwitchFwdNeighborVlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborVlanID must be specified if op_SwitchFwdNeighborVlanID is specified.
             :type val_f_SwitchFwdNeighborVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborVlanID: If op_SwitchFwdNeighborVlanID is specified, this value will be compared to the value in SwitchFwdNeighborVlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborVlanID must be specified if op_SwitchFwdNeighborVlanID is specified.
             :type val_c_SwitchFwdNeighborVlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborVlanIndex: The operator to apply to the field SwitchFwdNeighborVlanIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborVlanIndex: The numerical VLAN number (VLAN ID) of this neighbor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborVlanIndex: If op_SwitchFwdNeighborVlanIndex is specified, the field named in this input will be compared to the value in SwitchFwdNeighborVlanIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborVlanIndex must be specified if op_SwitchFwdNeighborVlanIndex is specified.
             :type val_f_SwitchFwdNeighborVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborVlanIndex: If op_SwitchFwdNeighborVlanIndex is specified, this value will be compared to the value in SwitchFwdNeighborVlanIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborVlanIndex must be specified if op_SwitchFwdNeighborVlanIndex is specified.
             :type val_c_SwitchFwdNeighborVlanIndex: String

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

             :param timestamp: The data returned will represent the switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of switch fwd neighbor methods. The listed methods will be called on each switch fwd neighbor returned and included in the output. Available methods are: network_name.
             :type methods: Array of String

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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex.
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

             :param select: The list of attributes to return for each SwitchFwdNeighbor. Valid values are DataSourceID, NeighborID, SwitchFwdNeighborFirstSeenTime, SwitchFwdNeighborStartTime, SwitchFwdNeighborEndTime, SwitchFwdNeighborChangedCols, SwitchFwdNeighborTimestamp, SwitchFwdNeighborMapSource, SwitchFwdNeighborType, SwitchFwdNeighborMAC, SwitchFwdNeighborIPDotted, SwitchFwdNeighborIPNumeric, SwitchFwdNeighborVlanID, SwitchFwdNeighborVlanIndex. If empty or omitted, all attributes will be returned.
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

             :return switch_fwd_neighbors: An array of the SwitchFwdNeighbor objects that match the specified input criteria.
             :rtype switch_fwd_neighbors: Array of SwitchFwdNeighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
