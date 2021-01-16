from ..broker import Broker


class DeviceRouteBroker(Broker):
    controller = "device_routes"

    def show(self, **kwargs):
        """Shows the details for the specified device route.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device route methods. The listed methods will be called on each device route returned and included in the output. Available methods are: data_source, device, interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_route: The device route identified by the specified DeviceRouteID.
             :rtype device_route: DeviceRoute

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device routes. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing table entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing table entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the outgoing interface for this route.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the outgoing interface for this route.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route destination network in CIDR format.
             :type RouteCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route destination network in CIDR format.
             :type RouteCIDR: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RouteEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RouteEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPNumeric: The numerical value of the route destination network address.
             :type RouteSubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPNumeric: The numerical value of the route destination network address.
             :type RouteSubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the VRF-based VPN related to this record.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the VRF-based VPN related to this record.
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

             :param timestamp: The data returned will represent the device routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device route methods. The listed methods will be called on each device route returned and included in the output. Available methods are: data_source, device, interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each DeviceRoute. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :return device_routes: An array of the DeviceRoute objects that match the specified input criteria.
             :rtype device_routes: Array of DeviceRoute

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device routes matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device from which this routing table entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing table entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the outgoing interface for this route.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the outgoing interface for this route.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteAdminDistance: The administrative distance of the protocol through which this route was learned, as specified by default Cisco conventions.
             :type RouteAdminDistance: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteAdminDistance: The administrative distance of the protocol through which this route was learned, as specified by default Cisco conventions.
             :type RouteAdminDistance: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route destination network in CIDR format.
             :type RouteCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteCIDR: The route destination network in CIDR format.
             :type RouteCIDR: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RouteChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RouteChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RouteEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RouteEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteIfIndex: The SNMP interface index of the outgoing interface for this route.
             :type RouteIfIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteIfIndex: The SNMP interface index of the outgoing interface for this route.
             :type RouteIfIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteMetric1: The first route metric value.
             :type RouteMetric1: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteMetric1: The first route metric value.
             :type RouteMetric1: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteMetric2: The second route metric value.
             :type RouteMetric2: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteMetric2: The second route metric value.
             :type RouteMetric2: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNetMaskDotted: The network mask of the route destination network in dotted (or colon-delimited for IPv6) format.
             :type RouteNetMaskDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNetMaskDotted: The network mask of the route destination network in dotted (or colon-delimited for IPv6) format.
             :type RouteNetMaskDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNetMaskNumeric: The numerical value of the network mask.
             :type RouteNetMaskNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNetMaskNumeric: The numerical value of the network mask.
             :type RouteNetMaskNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNextHopIPDotted: The next hop IP address for this route, in dotted (or colon-delimited for IPv6) format.
             :type RouteNextHopIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNextHopIPDotted: The next hop IP address for this route, in dotted (or colon-delimited for IPv6) format.
             :type RouteNextHopIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNextHopIPNumeric: The numerical value of the next hop IP address.
             :type RouteNextHopIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteNextHopIPNumeric: The numerical value of the next hop IP address.
             :type RouteNextHopIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteStartTime: The starting effective time of this revision of the record.
             :type RouteStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteStartTime: The starting effective time of this revision of the record.
             :type RouteStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPDotted: The route destination network address in dotted (or colon-delimited for IPv6) format.
             :type RouteSubnetIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPDotted: The route destination network address in dotted (or colon-delimited for IPv6) format.
             :type RouteSubnetIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPNumeric: The numerical value of the route destination network address.
             :type RouteSubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteSubnetIPNumeric: The numerical value of the route destination network address.
             :type RouteSubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteTimestamp: The date and time this record was collected or calculated.
             :type RouteTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteTimestamp: The date and time this record was collected or calculated.
             :type RouteTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteType: The type of the route.
             :type RouteType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteType: The type of the route.
             :type RouteType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the VRF-based VPN related to this record.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for the VRF-based VPN related to this record.
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

             :param timestamp: The data returned will represent the device routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device route methods. The listed methods will be called on each device route returned and included in the output. Available methods are: data_source, device, interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each DeviceRoute. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device routes, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DeviceRouteID, InterfaceID, RouteAdminDistance, RouteCIDR, RouteChangedCols, RouteEndTime, RouteIfIndex, RouteMetric1, RouteMetric2, RouteNetMaskDotted, RouteNetMaskNumeric, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteStartTime, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteTimestamp, RouteType, VirtualNetworkMemberID.
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

             :return device_routes: An array of the DeviceRoute objects that match the specified input criteria.
             :rtype device_routes: Array of DeviceRoute

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device routes matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DeviceRouteID, InterfaceID, RouteAdminDistance, RouteCIDR, RouteChangedCols, RouteEndTime, RouteIfIndex, RouteMetric1, RouteMetric2, RouteNetMaskDotted, RouteNetMaskNumeric, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteStartTime, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteTimestamp, RouteType, VirtualNetworkMemberID.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this routing table entry was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceRouteID: The operator to apply to the field DeviceRouteID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of the outgoing interface for this route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RouteAdminDistance: The operator to apply to the field RouteAdminDistance. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteAdminDistance: The administrative distance of the protocol through which this route was learned, as specified by default Cisco conventions. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteAdminDistance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteAdminDistance: If op_RouteAdminDistance is specified, the field named in this input will be compared to the value in RouteAdminDistance using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteAdminDistance must be specified if op_RouteAdminDistance is specified.
             :type val_f_RouteAdminDistance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteAdminDistance: If op_RouteAdminDistance is specified, this value will be compared to the value in RouteAdminDistance using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteAdminDistance must be specified if op_RouteAdminDistance is specified.
             :type val_c_RouteAdminDistance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteCIDR: The operator to apply to the field RouteCIDR. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteCIDR: The route destination network in CIDR format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RouteChangedCols: The operator to apply to the field RouteChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteChangedCols: If op_RouteChangedCols is specified, the field named in this input will be compared to the value in RouteChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteChangedCols must be specified if op_RouteChangedCols is specified.
             :type val_f_RouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteChangedCols: If op_RouteChangedCols is specified, this value will be compared to the value in RouteChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteChangedCols must be specified if op_RouteChangedCols is specified.
             :type val_c_RouteChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteEndTime: The operator to apply to the field RouteEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteEndTime: If op_RouteEndTime is specified, the field named in this input will be compared to the value in RouteEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteEndTime must be specified if op_RouteEndTime is specified.
             :type val_f_RouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteEndTime: If op_RouteEndTime is specified, this value will be compared to the value in RouteEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteEndTime must be specified if op_RouteEndTime is specified.
             :type val_c_RouteEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteIfIndex: The operator to apply to the field RouteIfIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteIfIndex: The SNMP interface index of the outgoing interface for this route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteIfIndex: If op_RouteIfIndex is specified, the field named in this input will be compared to the value in RouteIfIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteIfIndex must be specified if op_RouteIfIndex is specified.
             :type val_f_RouteIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteIfIndex: If op_RouteIfIndex is specified, this value will be compared to the value in RouteIfIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteIfIndex must be specified if op_RouteIfIndex is specified.
             :type val_c_RouteIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteMetric1: The operator to apply to the field RouteMetric1. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteMetric1: The first route metric value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteMetric1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteMetric1: If op_RouteMetric1 is specified, the field named in this input will be compared to the value in RouteMetric1 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteMetric1 must be specified if op_RouteMetric1 is specified.
             :type val_f_RouteMetric1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteMetric1: If op_RouteMetric1 is specified, this value will be compared to the value in RouteMetric1 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteMetric1 must be specified if op_RouteMetric1 is specified.
             :type val_c_RouteMetric1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteMetric2: The operator to apply to the field RouteMetric2. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteMetric2: The second route metric value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteMetric2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteMetric2: If op_RouteMetric2 is specified, the field named in this input will be compared to the value in RouteMetric2 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteMetric2 must be specified if op_RouteMetric2 is specified.
             :type val_f_RouteMetric2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteMetric2: If op_RouteMetric2 is specified, this value will be compared to the value in RouteMetric2 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteMetric2 must be specified if op_RouteMetric2 is specified.
             :type val_c_RouteMetric2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteNetMaskDotted: The operator to apply to the field RouteNetMaskDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteNetMaskDotted: The network mask of the route destination network in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteNetMaskDotted: If op_RouteNetMaskDotted is specified, the field named in this input will be compared to the value in RouteNetMaskDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteNetMaskDotted must be specified if op_RouteNetMaskDotted is specified.
             :type val_f_RouteNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteNetMaskDotted: If op_RouteNetMaskDotted is specified, this value will be compared to the value in RouteNetMaskDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteNetMaskDotted must be specified if op_RouteNetMaskDotted is specified.
             :type val_c_RouteNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteNetMaskNumeric: The operator to apply to the field RouteNetMaskNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteNetMaskNumeric: The numerical value of the network mask. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteNetMaskNumeric: If op_RouteNetMaskNumeric is specified, the field named in this input will be compared to the value in RouteNetMaskNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteNetMaskNumeric must be specified if op_RouteNetMaskNumeric is specified.
             :type val_f_RouteNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteNetMaskNumeric: If op_RouteNetMaskNumeric is specified, this value will be compared to the value in RouteNetMaskNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteNetMaskNumeric must be specified if op_RouteNetMaskNumeric is specified.
             :type val_c_RouteNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteNextHopIPDotted: The operator to apply to the field RouteNextHopIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteNextHopIPDotted: The next hop IP address for this route, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteNextHopIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteNextHopIPDotted: If op_RouteNextHopIPDotted is specified, the field named in this input will be compared to the value in RouteNextHopIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteNextHopIPDotted must be specified if op_RouteNextHopIPDotted is specified.
             :type val_f_RouteNextHopIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteNextHopIPDotted: If op_RouteNextHopIPDotted is specified, this value will be compared to the value in RouteNextHopIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteNextHopIPDotted must be specified if op_RouteNextHopIPDotted is specified.
             :type val_c_RouteNextHopIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteNextHopIPNumeric: The operator to apply to the field RouteNextHopIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteNextHopIPNumeric: The numerical value of the next hop IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteNextHopIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteNextHopIPNumeric: If op_RouteNextHopIPNumeric is specified, the field named in this input will be compared to the value in RouteNextHopIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteNextHopIPNumeric must be specified if op_RouteNextHopIPNumeric is specified.
             :type val_f_RouteNextHopIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteNextHopIPNumeric: If op_RouteNextHopIPNumeric is specified, this value will be compared to the value in RouteNextHopIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteNextHopIPNumeric must be specified if op_RouteNextHopIPNumeric is specified.
             :type val_c_RouteNextHopIPNumeric: String

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

             :param op_RouteStartTime: The operator to apply to the field RouteStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteStartTime: If op_RouteStartTime is specified, the field named in this input will be compared to the value in RouteStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteStartTime must be specified if op_RouteStartTime is specified.
             :type val_f_RouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteStartTime: If op_RouteStartTime is specified, this value will be compared to the value in RouteStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteStartTime must be specified if op_RouteStartTime is specified.
             :type val_c_RouteStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteSubnetIPDotted: The operator to apply to the field RouteSubnetIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteSubnetIPDotted: The route destination network address in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteSubnetIPDotted: If op_RouteSubnetIPDotted is specified, the field named in this input will be compared to the value in RouteSubnetIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteSubnetIPDotted must be specified if op_RouteSubnetIPDotted is specified.
             :type val_f_RouteSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteSubnetIPDotted: If op_RouteSubnetIPDotted is specified, this value will be compared to the value in RouteSubnetIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteSubnetIPDotted must be specified if op_RouteSubnetIPDotted is specified.
             :type val_c_RouteSubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteSubnetIPNumeric: The operator to apply to the field RouteSubnetIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteSubnetIPNumeric: The numerical value of the route destination network address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteSubnetIPNumeric: If op_RouteSubnetIPNumeric is specified, the field named in this input will be compared to the value in RouteSubnetIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteSubnetIPNumeric must be specified if op_RouteSubnetIPNumeric is specified.
             :type val_f_RouteSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteSubnetIPNumeric: If op_RouteSubnetIPNumeric is specified, this value will be compared to the value in RouteSubnetIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteSubnetIPNumeric must be specified if op_RouteSubnetIPNumeric is specified.
             :type val_c_RouteSubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteTimestamp: The operator to apply to the field RouteTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteTimestamp: If op_RouteTimestamp is specified, the field named in this input will be compared to the value in RouteTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteTimestamp must be specified if op_RouteTimestamp is specified.
             :type val_f_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteTimestamp: If op_RouteTimestamp is specified, this value will be compared to the value in RouteTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteTimestamp must be specified if op_RouteTimestamp is specified.
             :type val_c_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteType: The operator to apply to the field RouteType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteType: The type of the route. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VirtualNetworkMemberID: The operator to apply to the field VirtualNetworkMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberID: The internal NetMRI identifier for the VRF-based VPN related to this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param timestamp: The data returned will represent the device routes as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device route methods. The listed methods will be called on each device route returned and included in the output. Available methods are: data_source, device, interface, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRouteID. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID.
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

             :param select: The list of attributes to return for each DeviceRoute. Valid values are DeviceRouteID, RouteStartTime, RouteEndTime, RouteChangedCols, RouteTimestamp, DataSourceID, DeviceID, InterfaceID, RouteSubnetIPDotted, RouteSubnetIPNumeric, RouteCIDR, RouteIfIndex, RouteNetMaskDotted, RouteNetMaskNumeric, RouteMetric1, RouteMetric2, RouteNextHopIPDotted, RouteNextHopIPNumeric, RouteProto, RouteType, RouteAdminDistance, VirtualNetworkMemberID. If empty or omitted, all attributes will be returned.
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

             :return device_routes: An array of the DeviceRoute objects that match the specified input criteria.
             :rtype device_routes: Array of DeviceRoute

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

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
        """The outgoing interface for this route.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The outgoing interface for this route.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this routing table entry was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this routing table entry was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this routing table entry was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRouteID: The internal NetMRI identifier for this routing table entry on this device.
             :type DeviceRouteID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this routing table entry was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
