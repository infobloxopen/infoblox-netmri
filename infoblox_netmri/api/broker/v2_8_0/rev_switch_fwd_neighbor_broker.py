from ..broker import Broker


class RevSwitchFwdNeighborBroker(Broker):
    controller = "rev_switch_fwd_neighbors"

    def show(self, **kwargs):
        """Shows the details for the specified rev switch fwd neighbor.

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

             :param methods: A list of rev switch fwd neighbor methods. The listed methods will be called on each rev switch fwd neighbor returned and included in the output. Available methods are: neighbor.
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

             :return rev_switch_fwd_neighbor: The rev switch fwd neighbor identified by the specified NeighborID.
             :rtype rev_switch_fwd_neighbor: RevSwitchFwdNeighbor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available rev switch fwd neighbors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

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

             :param SwitchFwdNeighborID: The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship.
             :type SwitchFwdNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborID: The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship.
             :type SwitchFwdNeighborID: Array of Integer

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

             :param timestamp: The data returned will represent the rev switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of rev switch fwd neighbor methods. The listed methods will be called on each rev switch fwd neighbor returned and included in the output. Available methods are: neighbor.
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

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID.
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

             :param select: The list of attributes to return for each RevSwitchFwdNeighbor. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID. If empty or omitted, all attributes will be returned.
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

             :return rev_switch_fwd_neighbors: An array of the RevSwitchFwdNeighbor objects that match the specified input criteria.
             :rtype rev_switch_fwd_neighbors: Array of RevSwitchFwdNeighbor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available rev switch fwd neighbors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param RevSwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RevSwitchFwdNeighborChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RevSwitchFwdNeighborChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RevSwitchFwdNeighborEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RevSwitchFwdNeighborEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type RevSwitchFwdNeighborMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms.
             :type RevSwitchFwdNeighborMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborStartTime: The starting effective time of this revision of the record.
             :type RevSwitchFwdNeighborStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborStartTime: The starting effective time of this revision of the record.
             :type RevSwitchFwdNeighborStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborTimestamp: The date and time this record was collected or calculated.
             :type RevSwitchFwdNeighborTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RevSwitchFwdNeighborTimestamp: The date and time this record was collected or calculated.
             :type RevSwitchFwdNeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborID: The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship.
             :type SwitchFwdNeighborID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchFwdNeighborID: The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship.
             :type SwitchFwdNeighborID: Array of Integer

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

             :param timestamp: The data returned will represent the rev switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of rev switch fwd neighbor methods. The listed methods will be called on each rev switch fwd neighbor returned and included in the output. Available methods are: neighbor.
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

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID.
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

             :param select: The list of attributes to return for each RevSwitchFwdNeighbor. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against rev switch fwd neighbors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: NeighborID, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborMapSource, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborTimestamp, SwitchFwdNeighborID.
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

             :return rev_switch_fwd_neighbors: An array of the RevSwitchFwdNeighbor objects that match the specified input criteria.
             :rtype rev_switch_fwd_neighbors: Array of RevSwitchFwdNeighbor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available rev switch fwd neighbors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: NeighborID, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborMapSource, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborTimestamp, SwitchFwdNeighborID.

            **Inputs**

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

             :param op_RevSwitchFwdNeighborChangedCols: The operator to apply to the field RevSwitchFwdNeighborChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdNeighborChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdNeighborChangedCols: If op_RevSwitchFwdNeighborChangedCols is specified, the field named in this input will be compared to the value in RevSwitchFwdNeighborChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdNeighborChangedCols must be specified if op_RevSwitchFwdNeighborChangedCols is specified.
             :type val_f_RevSwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdNeighborChangedCols: If op_RevSwitchFwdNeighborChangedCols is specified, this value will be compared to the value in RevSwitchFwdNeighborChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdNeighborChangedCols must be specified if op_RevSwitchFwdNeighborChangedCols is specified.
             :type val_c_RevSwitchFwdNeighborChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RevSwitchFwdNeighborEndTime: The operator to apply to the field RevSwitchFwdNeighborEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdNeighborEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdNeighborEndTime: If op_RevSwitchFwdNeighborEndTime is specified, the field named in this input will be compared to the value in RevSwitchFwdNeighborEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdNeighborEndTime must be specified if op_RevSwitchFwdNeighborEndTime is specified.
             :type val_f_RevSwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdNeighborEndTime: If op_RevSwitchFwdNeighborEndTime is specified, this value will be compared to the value in RevSwitchFwdNeighborEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdNeighborEndTime must be specified if op_RevSwitchFwdNeighborEndTime is specified.
             :type val_c_RevSwitchFwdNeighborEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RevSwitchFwdNeighborMapSource: The operator to apply to the field RevSwitchFwdNeighborMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdNeighborMapSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdNeighborMapSource: If op_RevSwitchFwdNeighborMapSource is specified, the field named in this input will be compared to the value in RevSwitchFwdNeighborMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdNeighborMapSource must be specified if op_RevSwitchFwdNeighborMapSource is specified.
             :type val_f_RevSwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdNeighborMapSource: If op_RevSwitchFwdNeighborMapSource is specified, this value will be compared to the value in RevSwitchFwdNeighborMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdNeighborMapSource must be specified if op_RevSwitchFwdNeighborMapSource is specified.
             :type val_c_RevSwitchFwdNeighborMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RevSwitchFwdNeighborStartTime: The operator to apply to the field RevSwitchFwdNeighborStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdNeighborStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdNeighborStartTime: If op_RevSwitchFwdNeighborStartTime is specified, the field named in this input will be compared to the value in RevSwitchFwdNeighborStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdNeighborStartTime must be specified if op_RevSwitchFwdNeighborStartTime is specified.
             :type val_f_RevSwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdNeighborStartTime: If op_RevSwitchFwdNeighborStartTime is specified, this value will be compared to the value in RevSwitchFwdNeighborStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdNeighborStartTime must be specified if op_RevSwitchFwdNeighborStartTime is specified.
             :type val_c_RevSwitchFwdNeighborStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RevSwitchFwdNeighborTimestamp: The operator to apply to the field RevSwitchFwdNeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RevSwitchFwdNeighborTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RevSwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RevSwitchFwdNeighborTimestamp: If op_RevSwitchFwdNeighborTimestamp is specified, the field named in this input will be compared to the value in RevSwitchFwdNeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RevSwitchFwdNeighborTimestamp must be specified if op_RevSwitchFwdNeighborTimestamp is specified.
             :type val_f_RevSwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RevSwitchFwdNeighborTimestamp: If op_RevSwitchFwdNeighborTimestamp is specified, this value will be compared to the value in RevSwitchFwdNeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RevSwitchFwdNeighborTimestamp must be specified if op_RevSwitchFwdNeighborTimestamp is specified.
             :type val_c_RevSwitchFwdNeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchFwdNeighborID: The operator to apply to the field SwitchFwdNeighborID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchFwdNeighborID: The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchFwdNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchFwdNeighborID: If op_SwitchFwdNeighborID is specified, the field named in this input will be compared to the value in SwitchFwdNeighborID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchFwdNeighborID must be specified if op_SwitchFwdNeighborID is specified.
             :type val_f_SwitchFwdNeighborID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchFwdNeighborID: If op_SwitchFwdNeighborID is specified, this value will be compared to the value in SwitchFwdNeighborID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchFwdNeighborID must be specified if op_SwitchFwdNeighborID is specified.
             :type val_c_SwitchFwdNeighborID: String

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

             :param timestamp: The data returned will represent the rev switch fwd neighbors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of rev switch fwd neighbor methods. The listed methods will be called on each rev switch fwd neighbor returned and included in the output. Available methods are: neighbor.
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

             :param sort: The data field(s) to use for sorting the output. Default is NeighborID. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID.
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

             :param select: The list of attributes to return for each RevSwitchFwdNeighbor. Valid values are NeighborID, RevSwitchFwdNeighborStartTime, RevSwitchFwdNeighborEndTime, RevSwitchFwdNeighborChangedCols, RevSwitchFwdNeighborTimestamp, RevSwitchFwdNeighborMapSource, SwitchFwdNeighborID. If empty or omitted, all attributes will be returned.
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

             :return rev_switch_fwd_neighbors: An array of the RevSwitchFwdNeighbor objects that match the specified input criteria.
             :rtype rev_switch_fwd_neighbors: Array of RevSwitchFwdNeighbor

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
