from ..broker import Broker


class BestOriginRouteBroker(Broker):
    controller = "best_origin_routes"

    def show(self, **kwargs):
        """Shows the details for the specified best origin route.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier of the device routing table entry.
             :type DeviceRouteID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of best origin route methods. The listed methods will be called on each best origin route returned and included in the output. Available methods are: device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return best_origin_route: The best origin route identified by the specified DeviceRouteID.
             :rtype best_origin_route: BestOriginRoute

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available best origin routes. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this route was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this route was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier of the device routing table entry.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier of the device routing table entry.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route, in CIDR notation.
             :type RouteCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route, in CIDR notation.
             :type RouteCIDR: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member for this route.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member for this route.
             :type VirtualNetworkMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the best origin routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of best origin route methods. The listed methods will be called on each best origin route returned and included in the output. Available methods are: device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceRouteID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each BestOriginRoute. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :return best_origin_routes: An array of the BestOriginRoute objects that match the specified input criteria.
             :rtype best_origin_routes: Array of BestOriginRoute

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available best origin routes matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type BORouteChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type BORouteChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteEndTime: The ending effective time of this record, or empty if still in effect.
             :type BORouteEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteEndTime: The ending effective time of this record, or empty if still in effect.
             :type BORouteEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteStartTime: The starting effective time of this record.
             :type BORouteStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteStartTime: The starting effective time of this record.
             :type BORouteStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteTimestamp: The date and time this record was collected or calculated.
             :type BORouteTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BORouteTimestamp: The date and time this record was collected or calculated.
             :type BORouteTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this route was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this route was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier of the device routing table entry.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier of the device routing table entry.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route, in CIDR notation.
             :type RouteCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route, in CIDR notation.
             :type RouteCIDR: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteLocation: The route location, either Internal or External. Internal routes are those within the NetMRI discovery ranges.
             :type RouteLocation: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteLocation: The route location, either Internal or External. Internal routes are those within the NetMRI discovery ranges.
             :type RouteLocation: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteProto: The routing protocol through which this route was learned.
             :type RouteProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteProto: The routing protocol through which this route was learned.
             :type RouteProto: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteType: The route type as reported by the device.
             :type RouteType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteType: The route type as reported by the device.
             :type RouteType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member for this route.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member for this route.
             :type VirtualNetworkMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the best origin routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of best origin route methods. The listed methods will be called on each best origin route returned and included in the output. Available methods are: device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceRouteID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each BestOriginRoute. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against best origin routes, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: BORouteChangedCols, BORouteEndTime, BORouteStartTime, BORouteTimestamp, DeviceID, DeviceRouteID, RouteCIDR, RouteLocation, RouteProto, RouteType, VirtualNetworkMemberID.
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

             :return best_origin_routes: An array of the BestOriginRoute objects that match the specified input criteria.
             :rtype best_origin_routes: Array of BestOriginRoute

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available best origin routes matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: BORouteChangedCols, BORouteEndTime, BORouteStartTime, BORouteTimestamp, DeviceID, DeviceRouteID, RouteCIDR, RouteLocation, RouteProto, RouteType, VirtualNetworkMemberID.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BORouteChangedCols: The operator to apply to the field BORouteChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BORouteChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BORouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BORouteChangedCols: If op_BORouteChangedCols is specified, the field named in this input will be compared to the value in BORouteChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BORouteChangedCols must be specified if op_BORouteChangedCols is specified.
             :type val_f_BORouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BORouteChangedCols: If op_BORouteChangedCols is specified, this value will be compared to the value in BORouteChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BORouteChangedCols must be specified if op_BORouteChangedCols is specified.
             :type val_c_BORouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BORouteEndTime: The operator to apply to the field BORouteEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BORouteEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BORouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BORouteEndTime: If op_BORouteEndTime is specified, the field named in this input will be compared to the value in BORouteEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BORouteEndTime must be specified if op_BORouteEndTime is specified.
             :type val_f_BORouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BORouteEndTime: If op_BORouteEndTime is specified, this value will be compared to the value in BORouteEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BORouteEndTime must be specified if op_BORouteEndTime is specified.
             :type val_c_BORouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BORouteStartTime: The operator to apply to the field BORouteStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BORouteStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BORouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BORouteStartTime: If op_BORouteStartTime is specified, the field named in this input will be compared to the value in BORouteStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BORouteStartTime must be specified if op_BORouteStartTime is specified.
             :type val_f_BORouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BORouteStartTime: If op_BORouteStartTime is specified, this value will be compared to the value in BORouteStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BORouteStartTime must be specified if op_BORouteStartTime is specified.
             :type val_c_BORouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BORouteTimestamp: The operator to apply to the field BORouteTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BORouteTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BORouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BORouteTimestamp: If op_BORouteTimestamp is specified, the field named in this input will be compared to the value in BORouteTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BORouteTimestamp must be specified if op_BORouteTimestamp is specified.
             :type val_f_BORouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BORouteTimestamp: If op_BORouteTimestamp is specified, this value will be compared to the value in BORouteTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BORouteTimestamp must be specified if op_BORouteTimestamp is specified.
             :type val_c_BORouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this route was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceRouteID: The operator to apply to the field DeviceRouteID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRouteID: The internal NetMRI identifier of the device routing table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RouteCIDR: The operator to apply to the field RouteCIDR. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteCIDR: The route, in CIDR notation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteCIDR: If op_RouteCIDR is specified, the field named in this input will be compared to the value in RouteCIDR using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteCIDR must be specified if op_RouteCIDR is specified.
             :type val_f_RouteCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteCIDR: If op_RouteCIDR is specified, this value will be compared to the value in RouteCIDR using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteCIDR must be specified if op_RouteCIDR is specified.
             :type val_c_RouteCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteLocation: The operator to apply to the field RouteLocation. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteLocation: The route location, either Internal or External. Internal routes are those within the NetMRI discovery ranges. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteLocation: If op_RouteLocation is specified, the field named in this input will be compared to the value in RouteLocation using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteLocation must be specified if op_RouteLocation is specified.
             :type val_f_RouteLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteLocation: If op_RouteLocation is specified, this value will be compared to the value in RouteLocation using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteLocation must be specified if op_RouteLocation is specified.
             :type val_c_RouteLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteProto: The operator to apply to the field RouteProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteProto: The routing protocol through which this route was learned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteProto: If op_RouteProto is specified, the field named in this input will be compared to the value in RouteProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteProto must be specified if op_RouteProto is specified.
             :type val_f_RouteProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteProto: If op_RouteProto is specified, this value will be compared to the value in RouteProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteProto must be specified if op_RouteProto is specified.
             :type val_c_RouteProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteType: The operator to apply to the field RouteType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteType: The route type as reported by the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteType: If op_RouteType is specified, the field named in this input will be compared to the value in RouteType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteType must be specified if op_RouteType is specified.
             :type val_f_RouteType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteType: If op_RouteType is specified, this value will be compared to the value in RouteType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteType must be specified if op_RouteType is specified.
             :type val_c_RouteType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberID: The operator to apply to the field VirtualNetworkMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member for this route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberID: If op_VirtualNetworkMemberID is specified, the field named in this input will be compared to the value in VirtualNetworkMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberID must be specified if op_VirtualNetworkMemberID is specified.
             :type val_f_VirtualNetworkMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberID: If op_VirtualNetworkMemberID is specified, this value will be compared to the value in VirtualNetworkMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberID must be specified if op_VirtualNetworkMemberID is specified.
             :type val_c_VirtualNetworkMemberID: String

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

             :param timestamp: The data returned will represent the best origin routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of best origin route methods. The listed methods will be called on each best origin route returned and included in the output. Available methods are: device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceRouteID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each BestOriginRoute. Valid values are DeviceRouteID, BORouteStartTime, BORouteEndTime, BORouteChangedCols, BORouteTimestamp, DeviceID, RouteCIDR, RouteProto, RouteType, RouteLocation, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :return best_origin_routes: An array of the BestOriginRoute objects that match the specified input criteria.
             :rtype best_origin_routes: Array of BestOriginRoute

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
