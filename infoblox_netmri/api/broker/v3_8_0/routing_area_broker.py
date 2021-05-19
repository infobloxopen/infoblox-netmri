from ..broker import Broker


class RoutingAreaBroker(Broker):
    controller = "routing_areas"

    def show(self, **kwargs):
        """Shows the details for the specified routing area.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area methods. The listed methods will be called on each routing area returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return routing_area: The routing area identified by the specified RoutingAreaID.
             :rtype routing_area: RoutingArea

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available routing areas. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaNumber: The numerical OSPF Area ID, BGP AS or EIGRP AS.
             :type RoutingAreaNumber: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaNumber: The numerical OSPF Area ID, BGP AS or EIGRP AS.
             :type RoutingAreaNumber: Array of Integer

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

             :param timestamp: The data returned will represent the routing areas as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area methods. The listed methods will be called on each routing area returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` RoutingAreaID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaID. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex.
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

             :param select: The list of attributes to return for each RoutingArea. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex. If empty or omitted, all attributes will be returned.
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

             :return routing_areas: An array of the RoutingArea objects that match the specified input criteria.
             :rtype routing_areas: Array of RoutingArea

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available routing areas matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpVpnIndex: The SNMP index of the VRF to which this routing area belongs.
             :type EigrpVpnIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpVpnIndex: The SNMP index of the VRF to which this routing area belongs.
             :type EigrpVpnIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RoutingAreaChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RoutingAreaChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RoutingAreaEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RoutingAreaEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaName: For OSPF, the dotted version of the Area ID. For other protocols, the AS.
             :type RoutingAreaName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaName: For OSPF, the dotted version of the Area ID. For other protocols, the AS.
             :type RoutingAreaName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaNumber: The numerical OSPF Area ID, BGP AS or EIGRP AS.
             :type RoutingAreaNumber: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaNumber: The numerical OSPF Area ID, BGP AS or EIGRP AS.
             :type RoutingAreaNumber: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaStartTime: The starting effective time of this revision of the record.
             :type RoutingAreaStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaStartTime: The starting effective time of this revision of the record.
             :type RoutingAreaStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaTimestamp: The date and time this record was collected or calculated.
             :type RoutingAreaTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaTimestamp: The date and time this record was collected or calculated.
             :type RoutingAreaTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaType: OSPF, BGP, or EIGRP.
             :type RoutingAreaType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaType: OSPF, BGP, or EIGRP.
             :type RoutingAreaType: Array of String

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

             :param timestamp: The data returned will represent the routing areas as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area methods. The listed methods will be called on each routing area returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` RoutingAreaID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaID. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex.
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

             :param select: The list of attributes to return for each RoutingArea. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against routing areas, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: EigrpVpnIndex, RoutingAreaChangedCols, RoutingAreaEndTime, RoutingAreaID, RoutingAreaName, RoutingAreaNumber, RoutingAreaStartTime, RoutingAreaTimestamp, RoutingAreaType.
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

             :return routing_areas: An array of the RoutingArea objects that match the specified input criteria.
             :rtype routing_areas: Array of RoutingArea

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available routing areas matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: EigrpVpnIndex, RoutingAreaChangedCols, RoutingAreaEndTime, RoutingAreaID, RoutingAreaName, RoutingAreaNumber, RoutingAreaStartTime, RoutingAreaTimestamp, RoutingAreaType.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EigrpVpnIndex: The operator to apply to the field EigrpVpnIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EigrpVpnIndex: The SNMP index of the VRF to which this routing area belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EigrpVpnIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EigrpVpnIndex: If op_EigrpVpnIndex is specified, the field named in this input will be compared to the value in EigrpVpnIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EigrpVpnIndex must be specified if op_EigrpVpnIndex is specified.
             :type val_f_EigrpVpnIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EigrpVpnIndex: If op_EigrpVpnIndex is specified, this value will be compared to the value in EigrpVpnIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EigrpVpnIndex must be specified if op_EigrpVpnIndex is specified.
             :type val_c_EigrpVpnIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaChangedCols: The operator to apply to the field RoutingAreaChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaChangedCols: If op_RoutingAreaChangedCols is specified, the field named in this input will be compared to the value in RoutingAreaChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaChangedCols must be specified if op_RoutingAreaChangedCols is specified.
             :type val_f_RoutingAreaChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaChangedCols: If op_RoutingAreaChangedCols is specified, this value will be compared to the value in RoutingAreaChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaChangedCols must be specified if op_RoutingAreaChangedCols is specified.
             :type val_c_RoutingAreaChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaEndTime: The operator to apply to the field RoutingAreaEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaEndTime: If op_RoutingAreaEndTime is specified, the field named in this input will be compared to the value in RoutingAreaEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaEndTime must be specified if op_RoutingAreaEndTime is specified.
             :type val_f_RoutingAreaEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaEndTime: If op_RoutingAreaEndTime is specified, this value will be compared to the value in RoutingAreaEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaEndTime must be specified if op_RoutingAreaEndTime is specified.
             :type val_c_RoutingAreaEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaID: The operator to apply to the field RoutingAreaID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaID: If op_RoutingAreaID is specified, the field named in this input will be compared to the value in RoutingAreaID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaID must be specified if op_RoutingAreaID is specified.
             :type val_f_RoutingAreaID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaID: If op_RoutingAreaID is specified, this value will be compared to the value in RoutingAreaID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaID must be specified if op_RoutingAreaID is specified.
             :type val_c_RoutingAreaID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaName: The operator to apply to the field RoutingAreaName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaName: For OSPF, the dotted version of the Area ID. For other protocols, the AS. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaName: If op_RoutingAreaName is specified, the field named in this input will be compared to the value in RoutingAreaName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaName must be specified if op_RoutingAreaName is specified.
             :type val_f_RoutingAreaName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaName: If op_RoutingAreaName is specified, this value will be compared to the value in RoutingAreaName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaName must be specified if op_RoutingAreaName is specified.
             :type val_c_RoutingAreaName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaNumber: The operator to apply to the field RoutingAreaNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaNumber: The numerical OSPF Area ID, BGP AS or EIGRP AS. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaNumber: If op_RoutingAreaNumber is specified, the field named in this input will be compared to the value in RoutingAreaNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaNumber must be specified if op_RoutingAreaNumber is specified.
             :type val_f_RoutingAreaNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaNumber: If op_RoutingAreaNumber is specified, this value will be compared to the value in RoutingAreaNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaNumber must be specified if op_RoutingAreaNumber is specified.
             :type val_c_RoutingAreaNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaStartTime: The operator to apply to the field RoutingAreaStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaStartTime: If op_RoutingAreaStartTime is specified, the field named in this input will be compared to the value in RoutingAreaStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaStartTime must be specified if op_RoutingAreaStartTime is specified.
             :type val_f_RoutingAreaStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaStartTime: If op_RoutingAreaStartTime is specified, this value will be compared to the value in RoutingAreaStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaStartTime must be specified if op_RoutingAreaStartTime is specified.
             :type val_c_RoutingAreaStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaTimestamp: The operator to apply to the field RoutingAreaTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaTimestamp: If op_RoutingAreaTimestamp is specified, the field named in this input will be compared to the value in RoutingAreaTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaTimestamp must be specified if op_RoutingAreaTimestamp is specified.
             :type val_f_RoutingAreaTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaTimestamp: If op_RoutingAreaTimestamp is specified, this value will be compared to the value in RoutingAreaTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaTimestamp must be specified if op_RoutingAreaTimestamp is specified.
             :type val_c_RoutingAreaTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaType: The operator to apply to the field RoutingAreaType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaType: OSPF, BGP, or EIGRP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaType: If op_RoutingAreaType is specified, the field named in this input will be compared to the value in RoutingAreaType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaType must be specified if op_RoutingAreaType is specified.
             :type val_f_RoutingAreaType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaType: If op_RoutingAreaType is specified, this value will be compared to the value in RoutingAreaType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaType must be specified if op_RoutingAreaType is specified.
             :type val_c_RoutingAreaType: String

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

             :param timestamp: The data returned will represent the routing areas as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area methods. The listed methods will be called on each routing area returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` RoutingAreaID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaID. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex.
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

             :param select: The list of attributes to return for each RoutingArea. Valid values are RoutingAreaID, RoutingAreaStartTime, RoutingAreaEndTime, RoutingAreaChangedCols, RoutingAreaTimestamp, RoutingAreaType, RoutingAreaNumber, RoutingAreaName, EigrpVpnIndex. If empty or omitted, all attributes will be returned.
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

             :return routing_areas: An array of the RoutingArea objects that match the specified input criteria.
             :rtype routing_areas: Array of RoutingArea

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system.
             :type RoutingAreaID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)
