from ..broker import Broker


class IpRoutedNeighborBroker(Broker):
    controller = "ip_routed_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified ip routed neighbor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship.
             :type IPRoutedNeighborID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ip_routed_neighbor: The ip routed neighbor identified by the specified IPRoutedNeighborID.
             :rtype ip_routed_neighbor: IpRoutedNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available ip routed neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for the route which this record references.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for the route which this record references.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship.
             :type IPRoutedNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship.
             :type IPRoutedNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborTimestamp: The date and time this record was collected or calculated.
             :type IPRoutedNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborTimestamp: The date and time this record was collected or calculated.
             :type IPRoutedNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier of the corresponding neighbor record for this relationship.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier of the corresponding neighbor record for this relationship.
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

             :param timestamp: The data returned will represent the ip routed neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` IPRoutedNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is IPRoutedNeighborID. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID.
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

             :param select: The list of attributes to return for each IpRoutedNeighbor. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID. If empty or omitted, all attributes will be returned.
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

             :return ip_routed_neighbors: An array of the IpRoutedNeighbor objects that match the specified input criteria.
             :rtype ip_routed_neighbors: Array of IpRoutedNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available ip routed neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceRouteID: The internal NetMRI identifier for the route which this record references.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for the route which this record references.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IPRoutedNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IPRoutedNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IPRoutedNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IPRoutedNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship.
             :type IPRoutedNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship.
             :type IPRoutedNeighborID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type IPRoutedNeighborMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type IPRoutedNeighborMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborStartTime: The starting effective time of this revision of the record.
             :type IPRoutedNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborStartTime: The starting effective time of this revision of the record.
             :type IPRoutedNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborTimestamp: The date and time this record was collected or calculated.
             :type IPRoutedNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPRoutedNeighborTimestamp: The date and time this record was collected or calculated.
             :type IPRoutedNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier of the corresponding neighbor record for this relationship.
             :type NeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborID: The internal NetMRI identifier of the corresponding neighbor record for this relationship.
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

             :param timestamp: The data returned will represent the ip routed neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` IPRoutedNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is IPRoutedNeighborID. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID.
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

             :param select: The list of attributes to return for each IpRoutedNeighbor. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against ip routed neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceRouteID, IPRoutedNeighborChangedCols, IPRoutedNeighborEndTime, IPRoutedNeighborID, IPRoutedNeighborMapSource, IPRoutedNeighborStartTime, IPRoutedNeighborTimestamp, NeighborID.
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

             :return ip_routed_neighbors: An array of the IpRoutedNeighbor objects that match the specified input criteria.
             :rtype ip_routed_neighbors: Array of IpRoutedNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available ip routed neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceRouteID, IPRoutedNeighborChangedCols, IPRoutedNeighborEndTime, IPRoutedNeighborID, IPRoutedNeighborMapSource, IPRoutedNeighborStartTime, IPRoutedNeighborTimestamp, NeighborID.

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

             :param op_DeviceRouteID: The operator to apply to the field DeviceRouteID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRouteID: The internal NetMRI identifier for the route which this record references. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRouteID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRouteID: If op_DeviceRouteID is specified, the field named in this input will be compared to the value in DeviceRouteID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRouteID must be specified if op_DeviceRouteID is specified.
             :type val_f_DeviceRouteID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRouteID: If op_DeviceRouteID is specified, this value will be compared to the value in DeviceRouteID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRouteID must be specified if op_DeviceRouteID is specified.
             :type val_c_DeviceRouteID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborChangedCols: The operator to apply to the field IPRoutedNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborChangedCols: If op_IPRoutedNeighborChangedCols is specified, the field named in this input will be compared to the value in IPRoutedNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborChangedCols must be specified if op_IPRoutedNeighborChangedCols is specified.
             :type val_f_IPRoutedNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborChangedCols: If op_IPRoutedNeighborChangedCols is specified, this value will be compared to the value in IPRoutedNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborChangedCols must be specified if op_IPRoutedNeighborChangedCols is specified.
             :type val_c_IPRoutedNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborEndTime: The operator to apply to the field IPRoutedNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborEndTime: If op_IPRoutedNeighborEndTime is specified, the field named in this input will be compared to the value in IPRoutedNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborEndTime must be specified if op_IPRoutedNeighborEndTime is specified.
             :type val_f_IPRoutedNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborEndTime: If op_IPRoutedNeighborEndTime is specified, this value will be compared to the value in IPRoutedNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborEndTime must be specified if op_IPRoutedNeighborEndTime is specified.
             :type val_c_IPRoutedNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborID: The operator to apply to the field IPRoutedNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborID: The internal NetMRI identifier for this neighbor/route relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborID: If op_IPRoutedNeighborID is specified, the field named in this input will be compared to the value in IPRoutedNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborID must be specified if op_IPRoutedNeighborID is specified.
             :type val_f_IPRoutedNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborID: If op_IPRoutedNeighborID is specified, this value will be compared to the value in IPRoutedNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborID must be specified if op_IPRoutedNeighborID is specified.
             :type val_c_IPRoutedNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborMapSource: The operator to apply to the field IPRoutedNeighborMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborMapSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborMapSource: If op_IPRoutedNeighborMapSource is specified, the field named in this input will be compared to the value in IPRoutedNeighborMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborMapSource must be specified if op_IPRoutedNeighborMapSource is specified.
             :type val_f_IPRoutedNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborMapSource: If op_IPRoutedNeighborMapSource is specified, this value will be compared to the value in IPRoutedNeighborMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborMapSource must be specified if op_IPRoutedNeighborMapSource is specified.
             :type val_c_IPRoutedNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborStartTime: The operator to apply to the field IPRoutedNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborStartTime: If op_IPRoutedNeighborStartTime is specified, the field named in this input will be compared to the value in IPRoutedNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborStartTime must be specified if op_IPRoutedNeighborStartTime is specified.
             :type val_f_IPRoutedNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborStartTime: If op_IPRoutedNeighborStartTime is specified, this value will be compared to the value in IPRoutedNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborStartTime must be specified if op_IPRoutedNeighborStartTime is specified.
             :type val_c_IPRoutedNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPRoutedNeighborTimestamp: The operator to apply to the field IPRoutedNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPRoutedNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPRoutedNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPRoutedNeighborTimestamp: If op_IPRoutedNeighborTimestamp is specified, the field named in this input will be compared to the value in IPRoutedNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPRoutedNeighborTimestamp must be specified if op_IPRoutedNeighborTimestamp is specified.
             :type val_f_IPRoutedNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPRoutedNeighborTimestamp: If op_IPRoutedNeighborTimestamp is specified, this value will be compared to the value in IPRoutedNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPRoutedNeighborTimestamp must be specified if op_IPRoutedNeighborTimestamp is specified.
             :type val_c_IPRoutedNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborID: The operator to apply to the field NeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborID: The internal NetMRI identifier of the corresponding neighbor record for this relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the ip routed neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` IPRoutedNeighborID

             :param sort: The data field(s) to use for sorting the output. Default is IPRoutedNeighborID. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID.
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

             :param select: The list of attributes to return for each IpRoutedNeighbor. Valid values are IPRoutedNeighborID, DataSourceID, NeighborID, IPRoutedNeighborStartTime, IPRoutedNeighborEndTime, IPRoutedNeighborChangedCols, IPRoutedNeighborTimestamp, IPRoutedNeighborMapSource, DeviceRouteID. If empty or omitted, all attributes will be returned.
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

             :return ip_routed_neighbors: An array of the IpRoutedNeighbor objects that match the specified input criteria.
             :rtype ip_routed_neighbors: Array of IpRoutedNeighbor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
