from ..broker import Broker


class SerialNeighborBroker(Broker):
    controller = "serial_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified serial neighbor.

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

             :param methods: A list of serial neighbor methods. The listed methods will be called on each serial neighbor returned and included in the output. Available methods are: neighbor.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: neighbor.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return serial_neighbor: The serial neighbor identified by the specified NeighborID.
             :rtype serial_neighbor: SerialNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available serial neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

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

             :param timestamp: The data returned will represent the serial neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of serial neighbor methods. The listed methods will be called on each serial neighbor returned and included in the output. Available methods are: neighbor.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: neighbor.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric.
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

             :param select: The list of attributes to return for each SerialNeighbor. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric. If empty or omitted, all attributes will be returned.
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

             :return serial_neighbors: An array of the SerialNeighbor objects that match the specified input criteria.
             :rtype serial_neighbors: Array of SerialNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available serial neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param SerialNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SerialNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SerialNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SerialNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SerialNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborIPDotted: The IP address of the point-to-point neighbor, in dotted (or colon-delimited for IPv6) format. This is the IP in the subnet used to create the numbered point-to-point relationship.
             :type SerialNeighborIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborIPDotted: The IP address of the point-to-point neighbor, in dotted (or colon-delimited for IPv6) format. This is the IP in the subnet used to create the numbered point-to-point relationship.
             :type SerialNeighborIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborIPNumeric: The numerical value of the IP address of the point-to-point neighbor.
             :type SerialNeighborIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborIPNumeric: The numerical value of the IP address of the point-to-point neighbor.
             :type SerialNeighborIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type SerialNeighborMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type SerialNeighborMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborNetMaskDotted: The network mask of the subnet used in the numbered point-to-point relationship,  in dotted (or colon-delimited for IPv6) format.
             :type SerialNeighborNetMaskDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborNetMaskDotted: The network mask of the subnet used in the numbered point-to-point relationship,  in dotted (or colon-delimited for IPv6) format.
             :type SerialNeighborNetMaskDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborNetMaskNumeric: The numerical value of the netmask of the subnet used in the numbered point-to-point relationship.
             :type SerialNeighborNetMaskNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborNetMaskNumeric: The numerical value of the netmask of the subnet used in the numbered point-to-point relationship.
             :type SerialNeighborNetMaskNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborStartTime: The starting effective time of this revision of the record.
             :type SerialNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborStartTime: The starting effective time of this revision of the record.
             :type SerialNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborSubnetIPDotted: The network address of the subnet used in the numbered point-to-point relationship, in dotted (or colon-delimited for IPv6) format.
             :type SerialNeighborSubnetIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborSubnetIPDotted: The network address of the subnet used in the numbered point-to-point relationship, in dotted (or colon-delimited for IPv6) format.
             :type SerialNeighborSubnetIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborSubnetIPNumeric: The numerical value of the network address of the subnet used in the numbered point-to-point relationship.
             :type SerialNeighborSubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborSubnetIPNumeric: The numerical value of the network address of the subnet used in the numbered point-to-point relationship.
             :type SerialNeighborSubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborTimestamp: The date and time this record was collected or calculated.
             :type SerialNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SerialNeighborTimestamp: The date and time this record was collected or calculated.
             :type SerialNeighborTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the serial neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of serial neighbor methods. The listed methods will be called on each serial neighbor returned and included in the output. Available methods are: neighbor.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: neighbor.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric.
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

             :param select: The list of attributes to return for each SerialNeighbor. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against serial neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, NeighborID, SerialNeighborChangedCols, SerialNeighborEndTime, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborMapSource, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric, SerialNeighborStartTime, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborTimestamp.
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

             :return serial_neighbors: An array of the SerialNeighbor objects that match the specified input criteria.
             :rtype serial_neighbors: Array of SerialNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available serial neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, NeighborID, SerialNeighborChangedCols, SerialNeighborEndTime, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborMapSource, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric, SerialNeighborStartTime, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborTimestamp.

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

             :param op_SerialNeighborChangedCols: The operator to apply to the field SerialNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborChangedCols: If op_SerialNeighborChangedCols is specified, the field named in this input will be compared to the value in SerialNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborChangedCols must be specified if op_SerialNeighborChangedCols is specified.
             :type val_f_SerialNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborChangedCols: If op_SerialNeighborChangedCols is specified, this value will be compared to the value in SerialNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborChangedCols must be specified if op_SerialNeighborChangedCols is specified.
             :type val_c_SerialNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborEndTime: The operator to apply to the field SerialNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborEndTime: If op_SerialNeighborEndTime is specified, the field named in this input will be compared to the value in SerialNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborEndTime must be specified if op_SerialNeighborEndTime is specified.
             :type val_f_SerialNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborEndTime: If op_SerialNeighborEndTime is specified, this value will be compared to the value in SerialNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborEndTime must be specified if op_SerialNeighborEndTime is specified.
             :type val_c_SerialNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborIPDotted: The operator to apply to the field SerialNeighborIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborIPDotted: The IP address of the point-to-point neighbor, in dotted (or colon-delimited for IPv6) format. This is the IP in the subnet used to create the numbered point-to-point relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborIPDotted: If op_SerialNeighborIPDotted is specified, the field named in this input will be compared to the value in SerialNeighborIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborIPDotted must be specified if op_SerialNeighborIPDotted is specified.
             :type val_f_SerialNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborIPDotted: If op_SerialNeighborIPDotted is specified, this value will be compared to the value in SerialNeighborIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborIPDotted must be specified if op_SerialNeighborIPDotted is specified.
             :type val_c_SerialNeighborIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborIPNumeric: The operator to apply to the field SerialNeighborIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborIPNumeric: The numerical value of the IP address of the point-to-point neighbor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborIPNumeric: If op_SerialNeighborIPNumeric is specified, the field named in this input will be compared to the value in SerialNeighborIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborIPNumeric must be specified if op_SerialNeighborIPNumeric is specified.
             :type val_f_SerialNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborIPNumeric: If op_SerialNeighborIPNumeric is specified, this value will be compared to the value in SerialNeighborIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborIPNumeric must be specified if op_SerialNeighborIPNumeric is specified.
             :type val_c_SerialNeighborIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborMapSource: The operator to apply to the field SerialNeighborMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborMapSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborMapSource: If op_SerialNeighborMapSource is specified, the field named in this input will be compared to the value in SerialNeighborMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborMapSource must be specified if op_SerialNeighborMapSource is specified.
             :type val_f_SerialNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborMapSource: If op_SerialNeighborMapSource is specified, this value will be compared to the value in SerialNeighborMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborMapSource must be specified if op_SerialNeighborMapSource is specified.
             :type val_c_SerialNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborNetMaskDotted: The operator to apply to the field SerialNeighborNetMaskDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborNetMaskDotted: The network mask of the subnet used in the numbered point-to-point relationship,  in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborNetMaskDotted: If op_SerialNeighborNetMaskDotted is specified, the field named in this input will be compared to the value in SerialNeighborNetMaskDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborNetMaskDotted must be specified if op_SerialNeighborNetMaskDotted is specified.
             :type val_f_SerialNeighborNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborNetMaskDotted: If op_SerialNeighborNetMaskDotted is specified, this value will be compared to the value in SerialNeighborNetMaskDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborNetMaskDotted must be specified if op_SerialNeighborNetMaskDotted is specified.
             :type val_c_SerialNeighborNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborNetMaskNumeric: The operator to apply to the field SerialNeighborNetMaskNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborNetMaskNumeric: The numerical value of the netmask of the subnet used in the numbered point-to-point relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborNetMaskNumeric: If op_SerialNeighborNetMaskNumeric is specified, the field named in this input will be compared to the value in SerialNeighborNetMaskNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborNetMaskNumeric must be specified if op_SerialNeighborNetMaskNumeric is specified.
             :type val_f_SerialNeighborNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborNetMaskNumeric: If op_SerialNeighborNetMaskNumeric is specified, this value will be compared to the value in SerialNeighborNetMaskNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborNetMaskNumeric must be specified if op_SerialNeighborNetMaskNumeric is specified.
             :type val_c_SerialNeighborNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborStartTime: The operator to apply to the field SerialNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborStartTime: If op_SerialNeighborStartTime is specified, the field named in this input will be compared to the value in SerialNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborStartTime must be specified if op_SerialNeighborStartTime is specified.
             :type val_f_SerialNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborStartTime: If op_SerialNeighborStartTime is specified, this value will be compared to the value in SerialNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborStartTime must be specified if op_SerialNeighborStartTime is specified.
             :type val_c_SerialNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborSubnetIPDotted: The operator to apply to the field SerialNeighborSubnetIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborSubnetIPDotted: The network address of the subnet used in the numbered point-to-point relationship, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborSubnetIPDotted: If op_SerialNeighborSubnetIPDotted is specified, the field named in this input will be compared to the value in SerialNeighborSubnetIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborSubnetIPDotted must be specified if op_SerialNeighborSubnetIPDotted is specified.
             :type val_f_SerialNeighborSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborSubnetIPDotted: If op_SerialNeighborSubnetIPDotted is specified, this value will be compared to the value in SerialNeighborSubnetIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborSubnetIPDotted must be specified if op_SerialNeighborSubnetIPDotted is specified.
             :type val_c_SerialNeighborSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborSubnetIPNumeric: The operator to apply to the field SerialNeighborSubnetIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborSubnetIPNumeric: The numerical value of the network address of the subnet used in the numbered point-to-point relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborSubnetIPNumeric: If op_SerialNeighborSubnetIPNumeric is specified, the field named in this input will be compared to the value in SerialNeighborSubnetIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborSubnetIPNumeric must be specified if op_SerialNeighborSubnetIPNumeric is specified.
             :type val_f_SerialNeighborSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborSubnetIPNumeric: If op_SerialNeighborSubnetIPNumeric is specified, this value will be compared to the value in SerialNeighborSubnetIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborSubnetIPNumeric must be specified if op_SerialNeighborSubnetIPNumeric is specified.
             :type val_c_SerialNeighborSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SerialNeighborTimestamp: The operator to apply to the field SerialNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SerialNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SerialNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SerialNeighborTimestamp: If op_SerialNeighborTimestamp is specified, the field named in this input will be compared to the value in SerialNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SerialNeighborTimestamp must be specified if op_SerialNeighborTimestamp is specified.
             :type val_f_SerialNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SerialNeighborTimestamp: If op_SerialNeighborTimestamp is specified, this value will be compared to the value in SerialNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SerialNeighborTimestamp must be specified if op_SerialNeighborTimestamp is specified.
             :type val_c_SerialNeighborTimestamp: String

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

             :param timestamp: The data returned will represent the serial neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of serial neighbor methods. The listed methods will be called on each serial neighbor returned and included in the output. Available methods are: neighbor.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: neighbor.
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
            |  ``default:`` NeighborID

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric.
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

             :param select: The list of attributes to return for each SerialNeighbor. Valid values are DataSourceID, NeighborID, SerialNeighborStartTime, SerialNeighborEndTime, SerialNeighborChangedCols, SerialNeighborTimestamp, SerialNeighborMapSource, SerialNeighborSubnetIPDotted, SerialNeighborSubnetIPNumeric, SerialNeighborIPDotted, SerialNeighborIPNumeric, SerialNeighborNetMaskDotted, SerialNeighborNetMaskNumeric. If empty or omitted, all attributes will be returned.
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

             :return serial_neighbors: An array of the SerialNeighbor objects that match the specified input criteria.
             :rtype serial_neighbors: Array of SerialNeighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def neighbor(self, **kwargs):
        """The neighbor relationship, which contains the source and destination device information.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
             :type NeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The neighbor relationship, which contains the source and destination device information.
             :rtype : Neighbor

            """

        return self.api_request(self._get_method_fullname("neighbor"), kwargs)
