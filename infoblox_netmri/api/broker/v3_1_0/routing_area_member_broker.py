from ..broker import Broker


class RoutingAreaMemberBroker(Broker):
    controller = "routing_area_members"

    def show(self, **kwargs):
        """Shows the details for the specified routing area member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area member methods. The listed methods will be called on each routing area member returned and included in the output. Available methods are: data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, routing_area.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return routing_area_member: The routing area member identified by the specified RoutingAreaMemberID.
             :rtype routing_area_member: RoutingAreaMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available routing area members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing area membership was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing area membership was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this membership.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this membership.
             :type RoutingAreaID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the routing area members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area member methods. The listed methods will be called on each routing area member returned and included in the output. Available methods are: data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, routing_area.
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
            |  ``default:`` RoutingAreaMemberID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaMemberID. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd.
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

             :param select: The list of attributes to return for each RoutingAreaMember. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd. If empty or omitted, all attributes will be returned.
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

             :return routing_area_members: An array of the RoutingAreaMember objects that match the specified input criteria.
             :rtype routing_area_members: Array of RoutingAreaMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available routing area members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device from which this routing area membership was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing area membership was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaBdrRtrCount: The total number of area border routers reachable within this area.  This is initially zero, and is calculated in each SPF Pass.
             :type OspfAreaBdrRtrCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaBdrRtrCount: The total number of area border routers reachable within this area.  This is initially zero, and is calculated in each SPF Pass.
             :type OspfAreaBdrRtrCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaLsaCksumSum: The sum of the link-state advertisements' LS checksums contained in this area's link-state database on this router. This sum excludes external (LS type 5) link-state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link-state database of two routers.
             :type OspfAreaLsaCksumSum: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaLsaCksumSum: The sum of the link-state advertisements' LS checksums contained in this area's link-state database on this router. This sum excludes external (LS type 5) link-state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link-state database of two routers.
             :type OspfAreaLsaCksumSum: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaLsaCount: The total number of link-state advertisements in this area's link-state database on this router, excluding AS External LSA's.
             :type OspfAreaLsaCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaLsaCount: The total number of link-state advertisements in this area's link-state database on this router, excluding AS External LSA's.
             :type OspfAreaLsaCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaSummaryInd: Indicates how the router handles import of summary LSAs into stub areas. It has no effect on other areas.

If true, than the router will both summarize and propagate summary LSAs into the stub area.

Otherwise, the router will neither originate nor propagate summary LSAs. It will rely entirely on its default route.
             :type OspfAreaSummaryInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAreaSummaryInd: Indicates how the router handles import of summary LSAs into stub areas. It has no effect on other areas.

If true, than the router will both summarize and propagate summary LSAs into the stub area.

Otherwise, the router will neither originate nor propagate summary LSAs. It will rely entirely on its default route.
             :type OspfAreaSummaryInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAsBdrRtrCount: The total number of Autonomous System border routers reachable within this area, according to this router. This is initially zero, and is calculated in each SPF Pass.
             :type OspfAsBdrRtrCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAsBdrRtrCount: The total number of Autonomous System border routers reachable within this area, according to this router. This is initially zero, and is calculated in each SPF Pass.
             :type OspfAsBdrRtrCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAuthType: The type of authentication configured on this area for this router.
             :type OspfAuthType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfAuthType: The type of authentication configured on this area for this router.
             :type OspfAuthType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfImportAsExtern: The type of this OSPF area, according to this router. (importExternal for a standard are, noImportExternal for a stub, and importNssa for a not-so-stubby area).
             :type OspfImportAsExtern: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfImportAsExtern: The type of this OSPF area, according to this router. (importExternal for a standard are, noImportExternal for a stub, and importNssa for a not-so-stubby area).
             :type OspfImportAsExtern: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfSpfRunsDelta: The number of times that the intra-area route table has been calculated using this area's link-state database (typically using Dijkstra's algorithm), since the last time NetMRI polled the device.
             :type OspfSpfRunsDelta: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfSpfRunsDelta: The number of times that the intra-area route table has been calculated using this area's link-state database (typically using Dijkstra's algorithm), since the last time NetMRI polled the device.
             :type OspfSpfRunsDelta: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this membership.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this membership.
             :type RoutingAreaID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RoutingAreaMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RoutingAreaMemberChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RoutingAreaMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RoutingAreaMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberSource: Internal tracking information for NetMRI algorithms.
             :type RoutingAreaMemberSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberSource: Internal tracking information for NetMRI algorithms.
             :type RoutingAreaMemberSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberStartTime: The starting effective time of this revision of the record.
             :type RoutingAreaMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberStartTime: The starting effective time of this revision of the record.
             :type RoutingAreaMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberTimestamp: The date and time this record was collected or calculated.
             :type RoutingAreaMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaMemberTimestamp: The date and time this record was collected or calculated.
             :type RoutingAreaMemberTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the routing area members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area member methods. The listed methods will be called on each routing area member returned and included in the output. Available methods are: data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, routing_area.
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
            |  ``default:`` RoutingAreaMemberID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaMemberID. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd.
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

             :param select: The list of attributes to return for each RoutingAreaMember. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against routing area members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, OspfAreaBdrRtrCount, OspfAreaLsaCksumSum, OspfAreaLsaCount, OspfAreaSummaryInd, OspfAsBdrRtrCount, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, RoutingAreaID, RoutingAreaMemberChangedCols, RoutingAreaMemberEndTime, RoutingAreaMemberID, RoutingAreaMemberSource, RoutingAreaMemberStartTime, RoutingAreaMemberTimestamp.
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

             :return routing_area_members: An array of the RoutingAreaMember objects that match the specified input criteria.
             :rtype routing_area_members: Array of RoutingAreaMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available routing area members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, OspfAreaBdrRtrCount, OspfAreaLsaCksumSum, OspfAreaLsaCount, OspfAreaSummaryInd, OspfAsBdrRtrCount, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, RoutingAreaID, RoutingAreaMemberChangedCols, RoutingAreaMemberEndTime, RoutingAreaMemberID, RoutingAreaMemberSource, RoutingAreaMemberStartTime, RoutingAreaMemberTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this routing area membership was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_OspfAreaBdrRtrCount: The operator to apply to the field OspfAreaBdrRtrCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAreaBdrRtrCount: The total number of area border routers reachable within this area.  This is initially zero, and is calculated in each SPF Pass. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAreaBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAreaBdrRtrCount: If op_OspfAreaBdrRtrCount is specified, the field named in this input will be compared to the value in OspfAreaBdrRtrCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAreaBdrRtrCount must be specified if op_OspfAreaBdrRtrCount is specified.
             :type val_f_OspfAreaBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAreaBdrRtrCount: If op_OspfAreaBdrRtrCount is specified, this value will be compared to the value in OspfAreaBdrRtrCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAreaBdrRtrCount must be specified if op_OspfAreaBdrRtrCount is specified.
             :type val_c_OspfAreaBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfAreaLsaCksumSum: The operator to apply to the field OspfAreaLsaCksumSum. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAreaLsaCksumSum: The sum of the link-state advertisements' LS checksums contained in this area's link-state database on this router. This sum excludes external (LS type 5) link-state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link-state database of two routers. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAreaLsaCksumSum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAreaLsaCksumSum: If op_OspfAreaLsaCksumSum is specified, the field named in this input will be compared to the value in OspfAreaLsaCksumSum using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAreaLsaCksumSum must be specified if op_OspfAreaLsaCksumSum is specified.
             :type val_f_OspfAreaLsaCksumSum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAreaLsaCksumSum: If op_OspfAreaLsaCksumSum is specified, this value will be compared to the value in OspfAreaLsaCksumSum using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAreaLsaCksumSum must be specified if op_OspfAreaLsaCksumSum is specified.
             :type val_c_OspfAreaLsaCksumSum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfAreaLsaCount: The operator to apply to the field OspfAreaLsaCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAreaLsaCount: The total number of link-state advertisements in this area's link-state database on this router, excluding AS External LSA's. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAreaLsaCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAreaLsaCount: If op_OspfAreaLsaCount is specified, the field named in this input will be compared to the value in OspfAreaLsaCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAreaLsaCount must be specified if op_OspfAreaLsaCount is specified.
             :type val_f_OspfAreaLsaCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAreaLsaCount: If op_OspfAreaLsaCount is specified, this value will be compared to the value in OspfAreaLsaCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAreaLsaCount must be specified if op_OspfAreaLsaCount is specified.
             :type val_c_OspfAreaLsaCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfAreaSummaryInd: The operator to apply to the field OspfAreaSummaryInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAreaSummaryInd: Indicates how the router handles import of summary LSAs into stub areas. It has no effect on other areas.

If true, than the router will both summarize and propagate summary LSAs into the stub area.

Otherwise, the router will neither originate nor propagate summary LSAs. It will rely entirely on its default route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAreaSummaryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAreaSummaryInd: If op_OspfAreaSummaryInd is specified, the field named in this input will be compared to the value in OspfAreaSummaryInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAreaSummaryInd must be specified if op_OspfAreaSummaryInd is specified.
             :type val_f_OspfAreaSummaryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAreaSummaryInd: If op_OspfAreaSummaryInd is specified, this value will be compared to the value in OspfAreaSummaryInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAreaSummaryInd must be specified if op_OspfAreaSummaryInd is specified.
             :type val_c_OspfAreaSummaryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfAsBdrRtrCount: The operator to apply to the field OspfAsBdrRtrCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAsBdrRtrCount: The total number of Autonomous System border routers reachable within this area, according to this router. This is initially zero, and is calculated in each SPF Pass. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAsBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAsBdrRtrCount: If op_OspfAsBdrRtrCount is specified, the field named in this input will be compared to the value in OspfAsBdrRtrCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAsBdrRtrCount must be specified if op_OspfAsBdrRtrCount is specified.
             :type val_f_OspfAsBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAsBdrRtrCount: If op_OspfAsBdrRtrCount is specified, this value will be compared to the value in OspfAsBdrRtrCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAsBdrRtrCount must be specified if op_OspfAsBdrRtrCount is specified.
             :type val_c_OspfAsBdrRtrCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfAuthType: The operator to apply to the field OspfAuthType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfAuthType: The type of authentication configured on this area for this router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfAuthType: If op_OspfAuthType is specified, the field named in this input will be compared to the value in OspfAuthType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfAuthType must be specified if op_OspfAuthType is specified.
             :type val_f_OspfAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfAuthType: If op_OspfAuthType is specified, this value will be compared to the value in OspfAuthType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfAuthType must be specified if op_OspfAuthType is specified.
             :type val_c_OspfAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfImportAsExtern: The operator to apply to the field OspfImportAsExtern. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfImportAsExtern: The type of this OSPF area, according to this router. (importExternal for a standard are, noImportExternal for a stub, and importNssa for a not-so-stubby area). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfImportAsExtern: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfImportAsExtern: If op_OspfImportAsExtern is specified, the field named in this input will be compared to the value in OspfImportAsExtern using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfImportAsExtern must be specified if op_OspfImportAsExtern is specified.
             :type val_f_OspfImportAsExtern: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfImportAsExtern: If op_OspfImportAsExtern is specified, this value will be compared to the value in OspfImportAsExtern using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfImportAsExtern must be specified if op_OspfImportAsExtern is specified.
             :type val_c_OspfImportAsExtern: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfSpfRunsDelta: The operator to apply to the field OspfSpfRunsDelta. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfSpfRunsDelta: The number of times that the intra-area route table has been calculated using this area's link-state database (typically using Dijkstra's algorithm), since the last time NetMRI polled the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfSpfRunsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfSpfRunsDelta: If op_OspfSpfRunsDelta is specified, the field named in this input will be compared to the value in OspfSpfRunsDelta using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfSpfRunsDelta must be specified if op_OspfSpfRunsDelta is specified.
             :type val_f_OspfSpfRunsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfSpfRunsDelta: If op_OspfSpfRunsDelta is specified, this value will be compared to the value in OspfSpfRunsDelta using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfSpfRunsDelta must be specified if op_OspfSpfRunsDelta is specified.
             :type val_c_OspfSpfRunsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaID: The operator to apply to the field RoutingAreaID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RoutingAreaMemberChangedCols: The operator to apply to the field RoutingAreaMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberChangedCols: If op_RoutingAreaMemberChangedCols is specified, the field named in this input will be compared to the value in RoutingAreaMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberChangedCols must be specified if op_RoutingAreaMemberChangedCols is specified.
             :type val_f_RoutingAreaMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberChangedCols: If op_RoutingAreaMemberChangedCols is specified, this value will be compared to the value in RoutingAreaMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberChangedCols must be specified if op_RoutingAreaMemberChangedCols is specified.
             :type val_c_RoutingAreaMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaMemberEndTime: The operator to apply to the field RoutingAreaMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberEndTime: If op_RoutingAreaMemberEndTime is specified, the field named in this input will be compared to the value in RoutingAreaMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberEndTime must be specified if op_RoutingAreaMemberEndTime is specified.
             :type val_f_RoutingAreaMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberEndTime: If op_RoutingAreaMemberEndTime is specified, this value will be compared to the value in RoutingAreaMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberEndTime must be specified if op_RoutingAreaMemberEndTime is specified.
             :type val_c_RoutingAreaMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaMemberID: The operator to apply to the field RoutingAreaMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberID: If op_RoutingAreaMemberID is specified, the field named in this input will be compared to the value in RoutingAreaMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberID must be specified if op_RoutingAreaMemberID is specified.
             :type val_f_RoutingAreaMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberID: If op_RoutingAreaMemberID is specified, this value will be compared to the value in RoutingAreaMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberID must be specified if op_RoutingAreaMemberID is specified.
             :type val_c_RoutingAreaMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaMemberSource: The operator to apply to the field RoutingAreaMemberSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberSource: If op_RoutingAreaMemberSource is specified, the field named in this input will be compared to the value in RoutingAreaMemberSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberSource must be specified if op_RoutingAreaMemberSource is specified.
             :type val_f_RoutingAreaMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberSource: If op_RoutingAreaMemberSource is specified, this value will be compared to the value in RoutingAreaMemberSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberSource must be specified if op_RoutingAreaMemberSource is specified.
             :type val_c_RoutingAreaMemberSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaMemberStartTime: The operator to apply to the field RoutingAreaMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberStartTime: If op_RoutingAreaMemberStartTime is specified, the field named in this input will be compared to the value in RoutingAreaMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberStartTime must be specified if op_RoutingAreaMemberStartTime is specified.
             :type val_f_RoutingAreaMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberStartTime: If op_RoutingAreaMemberStartTime is specified, this value will be compared to the value in RoutingAreaMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberStartTime must be specified if op_RoutingAreaMemberStartTime is specified.
             :type val_c_RoutingAreaMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingAreaMemberTimestamp: The operator to apply to the field RoutingAreaMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingAreaMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingAreaMemberTimestamp: If op_RoutingAreaMemberTimestamp is specified, the field named in this input will be compared to the value in RoutingAreaMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingAreaMemberTimestamp must be specified if op_RoutingAreaMemberTimestamp is specified.
             :type val_f_RoutingAreaMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingAreaMemberTimestamp: If op_RoutingAreaMemberTimestamp is specified, this value will be compared to the value in RoutingAreaMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingAreaMemberTimestamp must be specified if op_RoutingAreaMemberTimestamp is specified.
             :type val_c_RoutingAreaMemberTimestamp: String

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

             :param timestamp: The data returned will represent the routing area members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of routing area member methods. The listed methods will be called on each routing area member returned and included in the output. Available methods are: data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, routing_area.
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
            |  ``default:`` RoutingAreaMemberID

             :param sort: The data field(s) to use for sorting the output. Default is RoutingAreaMemberID. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd.
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

             :param select: The list of attributes to return for each RoutingAreaMember. Valid values are RoutingAreaMemberID, RoutingAreaMemberStartTime, RoutingAreaMemberEndTime, RoutingAreaMemberChangedCols, RoutingAreaMemberTimestamp, RoutingAreaMemberSource, DataSourceID, DeviceID, RoutingAreaID, OspfAuthType, OspfImportAsExtern, OspfSpfRunsDelta, OspfAreaBdrRtrCount, OspfAsBdrRtrCount, OspfAreaLsaCount, OspfAreaLsaCksumSum, OspfAreaSummaryInd. If empty or omitted, all attributes will be returned.
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

             :return routing_area_members: An array of the RoutingAreaMember objects that match the specified input criteria.
             :rtype routing_area_members: Array of RoutingAreaMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def routing_area(self, **kwargs):
        """The routing area or autonomous system associated with this membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The routing area or autonomous system associated with this membership.
             :rtype : RoutingArea

            """

        return self.api_request(self._get_method_fullname("routing_area"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI collector that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI collector that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def interface(self, **kwargs):
        """The interface used to participate in this routing area.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface used to participate in this routing area.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this routing area membership was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this routing area membership was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this routing area membership was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param RoutingAreaMemberID: The internal NetMRI identifier for this routing area membership.
             :type RoutingAreaMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this routing area membership was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
