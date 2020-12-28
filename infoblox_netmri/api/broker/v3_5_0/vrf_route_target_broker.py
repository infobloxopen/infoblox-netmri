from ..broker import Broker


class VrfRouteTargetBroker(Broker):
    controller = "vrf_route_targets"

    def show(self, **kwargs):
        """Shows the details for the specified vrf route target.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VrfRouteTargetID: The internal NetMRI identifier for this VRF route target.
             :type VrfRouteTargetID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrf route target methods. The listed methods will be called on each vrf route target returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return vrf_route_target: The vrf route target identified by the specified VrfRouteTargetID.
             :rtype vrf_route_target: VrfRouteTarget

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available vrf route targets. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member that corresponds to this VRF route target.
             :type VirtualNetworkMemberID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetID: The internal NetMRI identifier for this VRF route target.
             :type VrfRouteTargetID: Array of Integer

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

             :param timestamp: The data returned will represent the vrf route targets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrf route target methods. The listed methods will be called on each vrf route target returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` VrfRouteTargetID

             :param sort: The data field(s) to use for sorting the output. Default is VrfRouteTargetID. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide.
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

             :param select: The list of attributes to return for each VrfRouteTarget. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide. If empty or omitted, all attributes will be returned.
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

             :return vrf_route_targets: An array of the VrfRouteTarget objects that match the specified input criteria.
             :rtype vrf_route_targets: Array of VrfRouteTarget

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available vrf route targets matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RTLeftSide: The left-hand portion of the route target; use Type to identify if it is an AS number or and IPv4 address.
             :type RTLeftSide: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RTRightSide: The right-hand portion of the route target.
             :type RTRightSide: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RTType: The style of the route target, asn or ipv4.
             :type RTType: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member that corresponds to this VRF route target.
             :type VirtualNetworkMemberID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfDirection: The direction of the RT (import or export).
             :type VrfDirection: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type VrfRouteTargetChangedCols: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetEndTime: The ending effective time of this record, or empty if still in effect.
             :type VrfRouteTargetEndTime: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetFirstTime: The first time this data element was seen on the network.
             :type VrfRouteTargetFirstTime: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetID: The internal NetMRI identifier for this VRF route target.
             :type VrfRouteTargetID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetStartTime: The starting effective time of this record.
             :type VrfRouteTargetStartTime: Array of DateTime

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfRouteTargetTimestamp: The date and time this record was collected or calculated.
             :type VrfRouteTargetTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the vrf route targets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrf route target methods. The listed methods will be called on each vrf route target returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` VrfRouteTargetID

             :param sort: The data field(s) to use for sorting the output. Default is VrfRouteTargetID. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide.
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

             :param select: The list of attributes to return for each VrfRouteTarget. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against vrf route targets, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, RTLeftSide, RTRightSide, RTType, VirtualNetworkMemberID, VrfDirection, VrfRouteTargetChangedCols, VrfRouteTargetEndTime, VrfRouteTargetFirstTime, VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetTimestamp.
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

             :return vrf_route_targets: An array of the VrfRouteTarget objects that match the specified input criteria.
             :rtype vrf_route_targets: Array of VrfRouteTarget

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available vrf route targets matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, RTLeftSide, RTRightSide, RTType, VirtualNetworkMemberID, VrfDirection, VrfRouteTargetChangedCols, VrfRouteTargetEndTime, VrfRouteTargetFirstTime, VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RTLeftSide: The operator to apply to the field RTLeftSide. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RTLeftSide: The left-hand portion of the route target; use Type to identify if it is an AS number or and IPv4 address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RTLeftSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RTLeftSide: If op_RTLeftSide is specified, the field named in this input will be compared to the value in RTLeftSide using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RTLeftSide must be specified if op_RTLeftSide is specified.
             :type val_f_RTLeftSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RTLeftSide: If op_RTLeftSide is specified, this value will be compared to the value in RTLeftSide using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RTLeftSide must be specified if op_RTLeftSide is specified.
             :type val_c_RTLeftSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RTRightSide: The operator to apply to the field RTRightSide. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RTRightSide: The right-hand portion of the route target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RTRightSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RTRightSide: If op_RTRightSide is specified, the field named in this input will be compared to the value in RTRightSide using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RTRightSide must be specified if op_RTRightSide is specified.
             :type val_f_RTRightSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RTRightSide: If op_RTRightSide is specified, this value will be compared to the value in RTRightSide using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RTRightSide must be specified if op_RTRightSide is specified.
             :type val_c_RTRightSide: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RTType: The operator to apply to the field RTType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RTType: The style of the route target, asn or ipv4. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RTType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RTType: If op_RTType is specified, the field named in this input will be compared to the value in RTType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RTType must be specified if op_RTType is specified.
             :type val_f_RTType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RTType: If op_RTType is specified, this value will be compared to the value in RTType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RTType must be specified if op_RTType is specified.
             :type val_c_RTType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberID: The operator to apply to the field VirtualNetworkMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberID: The internal NetMRI identifier for the Virtual Network Member that corresponds to this VRF route target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VrfDirection: The operator to apply to the field VrfDirection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfDirection: The direction of the RT (import or export). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfDirection: If op_VrfDirection is specified, the field named in this input will be compared to the value in VrfDirection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfDirection must be specified if op_VrfDirection is specified.
             :type val_f_VrfDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfDirection: If op_VrfDirection is specified, this value will be compared to the value in VrfDirection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfDirection must be specified if op_VrfDirection is specified.
             :type val_c_VrfDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetChangedCols: The operator to apply to the field VrfRouteTargetChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetChangedCols: If op_VrfRouteTargetChangedCols is specified, the field named in this input will be compared to the value in VrfRouteTargetChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetChangedCols must be specified if op_VrfRouteTargetChangedCols is specified.
             :type val_f_VrfRouteTargetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetChangedCols: If op_VrfRouteTargetChangedCols is specified, this value will be compared to the value in VrfRouteTargetChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetChangedCols must be specified if op_VrfRouteTargetChangedCols is specified.
             :type val_c_VrfRouteTargetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetEndTime: The operator to apply to the field VrfRouteTargetEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetEndTime: If op_VrfRouteTargetEndTime is specified, the field named in this input will be compared to the value in VrfRouteTargetEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetEndTime must be specified if op_VrfRouteTargetEndTime is specified.
             :type val_f_VrfRouteTargetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetEndTime: If op_VrfRouteTargetEndTime is specified, this value will be compared to the value in VrfRouteTargetEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetEndTime must be specified if op_VrfRouteTargetEndTime is specified.
             :type val_c_VrfRouteTargetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetFirstTime: The operator to apply to the field VrfRouteTargetFirstTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetFirstTime: The first time this data element was seen on the network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetFirstTime: If op_VrfRouteTargetFirstTime is specified, the field named in this input will be compared to the value in VrfRouteTargetFirstTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetFirstTime must be specified if op_VrfRouteTargetFirstTime is specified.
             :type val_f_VrfRouteTargetFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetFirstTime: If op_VrfRouteTargetFirstTime is specified, this value will be compared to the value in VrfRouteTargetFirstTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetFirstTime must be specified if op_VrfRouteTargetFirstTime is specified.
             :type val_c_VrfRouteTargetFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetID: The operator to apply to the field VrfRouteTargetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetID: The internal NetMRI identifier for this VRF route target. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetID: If op_VrfRouteTargetID is specified, the field named in this input will be compared to the value in VrfRouteTargetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetID must be specified if op_VrfRouteTargetID is specified.
             :type val_f_VrfRouteTargetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetID: If op_VrfRouteTargetID is specified, this value will be compared to the value in VrfRouteTargetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetID must be specified if op_VrfRouteTargetID is specified.
             :type val_c_VrfRouteTargetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetStartTime: The operator to apply to the field VrfRouteTargetStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetStartTime: If op_VrfRouteTargetStartTime is specified, the field named in this input will be compared to the value in VrfRouteTargetStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetStartTime must be specified if op_VrfRouteTargetStartTime is specified.
             :type val_f_VrfRouteTargetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetStartTime: If op_VrfRouteTargetStartTime is specified, this value will be compared to the value in VrfRouteTargetStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetStartTime must be specified if op_VrfRouteTargetStartTime is specified.
             :type val_c_VrfRouteTargetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfRouteTargetTimestamp: The operator to apply to the field VrfRouteTargetTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfRouteTargetTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfRouteTargetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfRouteTargetTimestamp: If op_VrfRouteTargetTimestamp is specified, the field named in this input will be compared to the value in VrfRouteTargetTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfRouteTargetTimestamp must be specified if op_VrfRouteTargetTimestamp is specified.
             :type val_f_VrfRouteTargetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfRouteTargetTimestamp: If op_VrfRouteTargetTimestamp is specified, this value will be compared to the value in VrfRouteTargetTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfRouteTargetTimestamp must be specified if op_VrfRouteTargetTimestamp is specified.
             :type val_c_VrfRouteTargetTimestamp: String

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

             :param timestamp: The data returned will represent the vrf route targets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrf route target methods. The listed methods will be called on each vrf route target returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` VrfRouteTargetID

             :param sort: The data field(s) to use for sorting the output. Default is VrfRouteTargetID. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide.
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

             :param select: The list of attributes to return for each VrfRouteTarget. Valid values are VrfRouteTargetID, VrfRouteTargetStartTime, VrfRouteTargetEndTime, VrfRouteTargetChangedCols, VrfRouteTargetTimestamp, VrfRouteTargetFirstTime, DataSourceID, DeviceID, VirtualNetworkMemberID, VrfDirection, RTType, RTLeftSide, RTRightSide. If empty or omitted, all attributes will be returned.
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

             :return vrf_route_targets: An array of the VrfRouteTarget objects that match the specified input criteria.
             :rtype vrf_route_targets: Array of VrfRouteTarget

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
