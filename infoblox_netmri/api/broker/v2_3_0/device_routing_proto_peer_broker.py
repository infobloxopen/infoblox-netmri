from ..broker import Broker


class DeviceRoutingProtoPeerBroker(Broker):
    controller = "device_routing_proto_peers"

    def show(self, **kwargs):
        """Shows the details for the specified device routing proto peer.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device routing proto peer methods. The listed methods will be called on each device routing proto peer returned and included in the output. Available methods are: peer_device, peer_interface, data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: peer_device, peer_interface, data_source, device, interface, routing_area.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_routing_proto_peer: The device routing proto peer identified by the specified DeviceRPPeerID.
             :rtype device_routing_proto_peer: DeviceRoutingProtoPeer

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device routing proto peers. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing peer data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing peer data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface over which this peer relationship exists, if available.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface over which this peer relationship exists, if available.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship.
             :type RoutingAreaID: Array of Integer

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

             :param timestamp: The data returned will represent the device routing proto peers as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device routing proto peer methods. The listed methods will be called on each device routing proto peer returned and included in the output. Available methods are: peer_device, peer_interface, data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: peer_device, peer_interface, data_source, device, interface, routing_area.
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
            |  ``default:`` DeviceRPPeerID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRPPeerID. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each DeviceRoutingProtoPeer. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return device_routing_proto_peers: An array of the DeviceRoutingProtoPeer objects that match the specified input criteria.
             :rtype device_routing_proto_peers: Array of DeviceRoutingProtoPeer

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device routing proto peers matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalIPDotted: The numerical local IP address for this peer relationship's BGP connection.
             :type BGPLocalIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalIPDotted: The numerical local IP address for this peer relationship's BGP connection.
             :type BGPLocalIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalIPNumeric: The local IP address for this peer relationship's BGP connection, in dotted (or colon-delimited for IPv6) notation.
             :type BGPLocalIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalIPNumeric: The local IP address for this peer relationship's BGP connection, in dotted (or colon-delimited for IPv6) notation.
             :type BGPLocalIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalPort: The local TCP port number for this entry's BGP connection.
             :type BGPLocalPort: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BGPLocalPort: The local TCP port number for this entry's BGP connection.
             :type BGPLocalPort: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BGPPeerPort: The remote TCP port number for this entry's BGP connection.
             :type BGPPeerPort: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BGPPeerPort: The remote TCP port number for this entry's BGP connection.
             :type BGPPeerPort: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device from which this routing peer data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this routing peer data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpRetransCount: The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up.
             :type EigrpRetransCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpRetransCount: The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up.
             :type EigrpRetransCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpRetriesCount: The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged.
             :type EigrpRetriesCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EigrpRetriesCount: The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged.
             :type EigrpRetriesCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for the local IP address used in this peer relationship, if available.
             :type IfAddrID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for the local IP address used in this peer relationship, if available.
             :type IfAddrID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface over which this peer relationship exists, if available.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface over which this peer relationship exists, if available.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerAddresslessIndex: For addressless peer interfaces, this will contain the SNMP interface index for the peer's interface. The peer IP address will contain the IP of another interface on the peer.
             :type OspfPeerAddresslessIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerAddresslessIndex: For addressless peer interfaces, this will contain the SNMP interface index for the peer's interface. The peer IP address will contain the IP of another interface on the peer.
             :type OspfPeerAddresslessIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerEventsDelta: The number of times that this neighbor relationship has changed state, since the last time NetMRI polled the device.
             :type OspfPeerEventsDelta: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerEventsDelta: The number of times that this neighbor relationship has changed state, since the last time NetMRI polled the device.
             :type OspfPeerEventsDelta: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerPermanence: How this neighbor was determined, 'dynamic' for learned through the protocol, 'permanent' for configured.
             :type OspfPeerPermanence: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerPermanence: How this neighbor was determined, 'dynamic' for learned through the protocol, 'permanent' for configured.
             :type OspfPeerPermanence: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerRouterIdentDotted: The OSPF router identifier of the peer, in dotted (or colon-delimited for IPv6) format, if relevant.
             :type OspfPeerRouterIdentDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerRouterIdentDotted: The OSPF router identifier of the peer, in dotted (or colon-delimited for IPv6) format, if relevant.
             :type OspfPeerRouterIdentDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerRouterIdentNumeric: The numerical OSPF router identifier of the peer.
             :type OspfPeerRouterIdentNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OspfPeerRouterIdentNumeric: The numerical OSPF router identifier of the peer.
             :type OspfPeerRouterIdentNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PeerDeviceID: The internal NetMRI identifier for the peer device.
             :type PeerDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PeerDeviceID: The internal NetMRI identifier for the peer device.
             :type PeerDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PeerInterfaceID: The internal NetMRI identifier for the remote router's interface over which this peer relationship exists, if available.
             :type PeerInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PeerInterfaceID: The internal NetMRI identifier for the remote router's interface over which this peer relationship exists, if available.
             :type PeerInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RPPeerChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type RPPeerChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RPPeerEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type RPPeerEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerIPDotted: The IP address of the peer, in dotted (or colon-delimited for IPv6) format.
             :type RPPeerIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerIPDotted: The IP address of the peer, in dotted (or colon-delimited for IPv6) format.
             :type RPPeerIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerIPNumeric: The numerical IP address of the peer.
             :type RPPeerIPNumeric: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerIPNumeric: The numerical IP address of the peer.
             :type RPPeerIPNumeric: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerMapSource: Internal tracking data for NetMRI algorithms.
             :type RPPeerMapSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerMapSource: Internal tracking data for NetMRI algorithms.
             :type RPPeerMapSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerStartTime: The starting effective time of this revision of the record.
             :type RPPeerStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerStartTime: The starting effective time of this revision of the record.
             :type RPPeerStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerState: The protocol-specific state of this routing peer relationship.
             :type RPPeerState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerState: The protocol-specific state of this routing peer relationship.
             :type RPPeerState: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerTimestamp: The date and time this record was collected or calculated.
             :type RPPeerTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerTimestamp: The date and time this record was collected or calculated.
             :type RPPeerTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerType: Identifies the type of routing peer relationship this is (OSPF, BGP, IGRP). This is distinct from the protocol as some vendors may use different protocol names for similar protocols (IGRP and EIGRP, for example).
             :type RPPeerType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerType: Identifies the type of routing peer relationship this is (OSPF, BGP, IGRP). This is distinct from the protocol as some vendors may use different protocol names for similar protocols (IGRP and EIGRP, for example).
             :type RPPeerType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerUpSince: The date and time this peer relationship has been active, without interruption. The granularity level varies with each protocol.
             :type RPPeerUpSince: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RPPeerUpSince: The date and time this peer relationship has been active, without interruption. The granularity level varies with each protocol.
             :type RPPeerUpSince: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RouteProto: Identifies the routing protocol used for this peer relationship.
             :type RouteProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteProto: Identifies the routing protocol used for this peer relationship.
             :type RouteProto: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship.
             :type RoutingAreaID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship.
             :type RoutingAreaID: Array of Integer

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

             :param timestamp: The data returned will represent the device routing proto peers as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device routing proto peer methods. The listed methods will be called on each device routing proto peer returned and included in the output. Available methods are: peer_device, peer_interface, data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: peer_device, peer_interface, data_source, device, interface, routing_area.
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
            |  ``default:`` DeviceRPPeerID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRPPeerID. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each DeviceRoutingProtoPeer. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device routing proto peers, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: BGPLocalIPDotted, BGPLocalIPNumeric, BGPLocalPort, BGPPeerPort, DataSourceID, DeviceID, DeviceRPPeerID, EigrpRetransCount, EigrpRetriesCount, IfAddrID, InterfaceID, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, PeerDeviceID, PeerInterfaceID, RPPeerChangedCols, RPPeerEndTime, RPPeerIPDotted, RPPeerIPNumeric, RPPeerMapSource, RPPeerStartTime, RPPeerState, RPPeerTimestamp, RPPeerType, RPPeerUpSince, RouteProto, RoutingAreaID.
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

             :return device_routing_proto_peers: An array of the DeviceRoutingProtoPeer objects that match the specified input criteria.
             :rtype device_routing_proto_peers: Array of DeviceRoutingProtoPeer

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device routing proto peers matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: BGPLocalIPDotted, BGPLocalIPNumeric, BGPLocalPort, BGPPeerPort, DataSourceID, DeviceID, DeviceRPPeerID, EigrpRetransCount, EigrpRetriesCount, IfAddrID, InterfaceID, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, PeerDeviceID, PeerInterfaceID, RPPeerChangedCols, RPPeerEndTime, RPPeerIPDotted, RPPeerIPNumeric, RPPeerMapSource, RPPeerStartTime, RPPeerState, RPPeerTimestamp, RPPeerType, RPPeerUpSince, RouteProto, RoutingAreaID.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BGPLocalIPDotted: The operator to apply to the field BGPLocalIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BGPLocalIPDotted: The numerical local IP address for this peer relationship's BGP connection. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BGPLocalIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BGPLocalIPDotted: If op_BGPLocalIPDotted is specified, the field named in this input will be compared to the value in BGPLocalIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BGPLocalIPDotted must be specified if op_BGPLocalIPDotted is specified.
             :type val_f_BGPLocalIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BGPLocalIPDotted: If op_BGPLocalIPDotted is specified, this value will be compared to the value in BGPLocalIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BGPLocalIPDotted must be specified if op_BGPLocalIPDotted is specified.
             :type val_c_BGPLocalIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BGPLocalIPNumeric: The operator to apply to the field BGPLocalIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BGPLocalIPNumeric: The local IP address for this peer relationship's BGP connection, in dotted (or colon-delimited for IPv6) notation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BGPLocalIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BGPLocalIPNumeric: If op_BGPLocalIPNumeric is specified, the field named in this input will be compared to the value in BGPLocalIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BGPLocalIPNumeric must be specified if op_BGPLocalIPNumeric is specified.
             :type val_f_BGPLocalIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BGPLocalIPNumeric: If op_BGPLocalIPNumeric is specified, this value will be compared to the value in BGPLocalIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BGPLocalIPNumeric must be specified if op_BGPLocalIPNumeric is specified.
             :type val_c_BGPLocalIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BGPLocalPort: The operator to apply to the field BGPLocalPort. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BGPLocalPort: The local TCP port number for this entry's BGP connection. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BGPLocalPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BGPLocalPort: If op_BGPLocalPort is specified, the field named in this input will be compared to the value in BGPLocalPort using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BGPLocalPort must be specified if op_BGPLocalPort is specified.
             :type val_f_BGPLocalPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BGPLocalPort: If op_BGPLocalPort is specified, this value will be compared to the value in BGPLocalPort using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BGPLocalPort must be specified if op_BGPLocalPort is specified.
             :type val_c_BGPLocalPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BGPPeerPort: The operator to apply to the field BGPPeerPort. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BGPPeerPort: The remote TCP port number for this entry's BGP connection. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BGPPeerPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BGPPeerPort: If op_BGPPeerPort is specified, the field named in this input will be compared to the value in BGPPeerPort using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BGPPeerPort must be specified if op_BGPPeerPort is specified.
             :type val_f_BGPPeerPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BGPPeerPort: If op_BGPPeerPort is specified, this value will be compared to the value in BGPPeerPort using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BGPPeerPort must be specified if op_BGPPeerPort is specified.
             :type val_c_BGPPeerPort: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this routing peer data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceRPPeerID: The operator to apply to the field DeviceRPPeerID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRPPeerID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRPPeerID: If op_DeviceRPPeerID is specified, the field named in this input will be compared to the value in DeviceRPPeerID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRPPeerID must be specified if op_DeviceRPPeerID is specified.
             :type val_f_DeviceRPPeerID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRPPeerID: If op_DeviceRPPeerID is specified, this value will be compared to the value in DeviceRPPeerID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRPPeerID must be specified if op_DeviceRPPeerID is specified.
             :type val_c_DeviceRPPeerID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EigrpRetransCount: The operator to apply to the field EigrpRetransCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EigrpRetransCount: The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EigrpRetransCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EigrpRetransCount: If op_EigrpRetransCount is specified, the field named in this input will be compared to the value in EigrpRetransCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EigrpRetransCount must be specified if op_EigrpRetransCount is specified.
             :type val_f_EigrpRetransCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EigrpRetransCount: If op_EigrpRetransCount is specified, this value will be compared to the value in EigrpRetransCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EigrpRetransCount must be specified if op_EigrpRetransCount is specified.
             :type val_c_EigrpRetransCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EigrpRetriesCount: The operator to apply to the field EigrpRetriesCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EigrpRetriesCount: The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EigrpRetriesCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EigrpRetriesCount: If op_EigrpRetriesCount is specified, the field named in this input will be compared to the value in EigrpRetriesCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EigrpRetriesCount must be specified if op_EigrpRetriesCount is specified.
             :type val_f_EigrpRetriesCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EigrpRetriesCount: If op_EigrpRetriesCount is specified, this value will be compared to the value in EigrpRetriesCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EigrpRetriesCount must be specified if op_EigrpRetriesCount is specified.
             :type val_c_EigrpRetriesCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IfAddrID: The operator to apply to the field IfAddrID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfAddrID: The internal NetMRI identifier for the local IP address used in this peer relationship, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfAddrID: If op_IfAddrID is specified, the field named in this input will be compared to the value in IfAddrID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_f_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfAddrID: If op_IfAddrID is specified, this value will be compared to the value in IfAddrID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_c_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the interface over which this peer relationship exists, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_OspfPeerAddresslessIndex: The operator to apply to the field OspfPeerAddresslessIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfPeerAddresslessIndex: For addressless peer interfaces, this will contain the SNMP interface index for the peer's interface. The peer IP address will contain the IP of another interface on the peer. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfPeerAddresslessIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfPeerAddresslessIndex: If op_OspfPeerAddresslessIndex is specified, the field named in this input will be compared to the value in OspfPeerAddresslessIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfPeerAddresslessIndex must be specified if op_OspfPeerAddresslessIndex is specified.
             :type val_f_OspfPeerAddresslessIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfPeerAddresslessIndex: If op_OspfPeerAddresslessIndex is specified, this value will be compared to the value in OspfPeerAddresslessIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfPeerAddresslessIndex must be specified if op_OspfPeerAddresslessIndex is specified.
             :type val_c_OspfPeerAddresslessIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfPeerEventsDelta: The operator to apply to the field OspfPeerEventsDelta. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfPeerEventsDelta: The number of times that this neighbor relationship has changed state, since the last time NetMRI polled the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfPeerEventsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfPeerEventsDelta: If op_OspfPeerEventsDelta is specified, the field named in this input will be compared to the value in OspfPeerEventsDelta using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfPeerEventsDelta must be specified if op_OspfPeerEventsDelta is specified.
             :type val_f_OspfPeerEventsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfPeerEventsDelta: If op_OspfPeerEventsDelta is specified, this value will be compared to the value in OspfPeerEventsDelta using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfPeerEventsDelta must be specified if op_OspfPeerEventsDelta is specified.
             :type val_c_OspfPeerEventsDelta: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfPeerPermanence: The operator to apply to the field OspfPeerPermanence. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfPeerPermanence: How this neighbor was determined, 'dynamic' for learned through the protocol, 'permanent' for configured. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfPeerPermanence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfPeerPermanence: If op_OspfPeerPermanence is specified, the field named in this input will be compared to the value in OspfPeerPermanence using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfPeerPermanence must be specified if op_OspfPeerPermanence is specified.
             :type val_f_OspfPeerPermanence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfPeerPermanence: If op_OspfPeerPermanence is specified, this value will be compared to the value in OspfPeerPermanence using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfPeerPermanence must be specified if op_OspfPeerPermanence is specified.
             :type val_c_OspfPeerPermanence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfPeerRouterIdentDotted: The operator to apply to the field OspfPeerRouterIdentDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfPeerRouterIdentDotted: The OSPF router identifier of the peer, in dotted (or colon-delimited for IPv6) format, if relevant. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfPeerRouterIdentDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfPeerRouterIdentDotted: If op_OspfPeerRouterIdentDotted is specified, the field named in this input will be compared to the value in OspfPeerRouterIdentDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfPeerRouterIdentDotted must be specified if op_OspfPeerRouterIdentDotted is specified.
             :type val_f_OspfPeerRouterIdentDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfPeerRouterIdentDotted: If op_OspfPeerRouterIdentDotted is specified, this value will be compared to the value in OspfPeerRouterIdentDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfPeerRouterIdentDotted must be specified if op_OspfPeerRouterIdentDotted is specified.
             :type val_c_OspfPeerRouterIdentDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OspfPeerRouterIdentNumeric: The operator to apply to the field OspfPeerRouterIdentNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OspfPeerRouterIdentNumeric: The numerical OSPF router identifier of the peer. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OspfPeerRouterIdentNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OspfPeerRouterIdentNumeric: If op_OspfPeerRouterIdentNumeric is specified, the field named in this input will be compared to the value in OspfPeerRouterIdentNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OspfPeerRouterIdentNumeric must be specified if op_OspfPeerRouterIdentNumeric is specified.
             :type val_f_OspfPeerRouterIdentNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OspfPeerRouterIdentNumeric: If op_OspfPeerRouterIdentNumeric is specified, this value will be compared to the value in OspfPeerRouterIdentNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OspfPeerRouterIdentNumeric must be specified if op_OspfPeerRouterIdentNumeric is specified.
             :type val_c_OspfPeerRouterIdentNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PeerDeviceID: The operator to apply to the field PeerDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PeerDeviceID: The internal NetMRI identifier for the peer device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PeerDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PeerDeviceID: If op_PeerDeviceID is specified, the field named in this input will be compared to the value in PeerDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PeerDeviceID must be specified if op_PeerDeviceID is specified.
             :type val_f_PeerDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PeerDeviceID: If op_PeerDeviceID is specified, this value will be compared to the value in PeerDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PeerDeviceID must be specified if op_PeerDeviceID is specified.
             :type val_c_PeerDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PeerInterfaceID: The operator to apply to the field PeerInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PeerInterfaceID: The internal NetMRI identifier for the remote router's interface over which this peer relationship exists, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PeerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PeerInterfaceID: If op_PeerInterfaceID is specified, the field named in this input will be compared to the value in PeerInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PeerInterfaceID must be specified if op_PeerInterfaceID is specified.
             :type val_f_PeerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PeerInterfaceID: If op_PeerInterfaceID is specified, this value will be compared to the value in PeerInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PeerInterfaceID must be specified if op_PeerInterfaceID is specified.
             :type val_c_PeerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerChangedCols: The operator to apply to the field RPPeerChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerChangedCols: If op_RPPeerChangedCols is specified, the field named in this input will be compared to the value in RPPeerChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerChangedCols must be specified if op_RPPeerChangedCols is specified.
             :type val_f_RPPeerChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerChangedCols: If op_RPPeerChangedCols is specified, this value will be compared to the value in RPPeerChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerChangedCols must be specified if op_RPPeerChangedCols is specified.
             :type val_c_RPPeerChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerEndTime: The operator to apply to the field RPPeerEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerEndTime: If op_RPPeerEndTime is specified, the field named in this input will be compared to the value in RPPeerEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerEndTime must be specified if op_RPPeerEndTime is specified.
             :type val_f_RPPeerEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerEndTime: If op_RPPeerEndTime is specified, this value will be compared to the value in RPPeerEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerEndTime must be specified if op_RPPeerEndTime is specified.
             :type val_c_RPPeerEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerIPDotted: The operator to apply to the field RPPeerIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerIPDotted: The IP address of the peer, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerIPDotted: If op_RPPeerIPDotted is specified, the field named in this input will be compared to the value in RPPeerIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerIPDotted must be specified if op_RPPeerIPDotted is specified.
             :type val_f_RPPeerIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerIPDotted: If op_RPPeerIPDotted is specified, this value will be compared to the value in RPPeerIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerIPDotted must be specified if op_RPPeerIPDotted is specified.
             :type val_c_RPPeerIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerIPNumeric: The operator to apply to the field RPPeerIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerIPNumeric: The numerical IP address of the peer. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerIPNumeric: If op_RPPeerIPNumeric is specified, the field named in this input will be compared to the value in RPPeerIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerIPNumeric must be specified if op_RPPeerIPNumeric is specified.
             :type val_f_RPPeerIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerIPNumeric: If op_RPPeerIPNumeric is specified, this value will be compared to the value in RPPeerIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerIPNumeric must be specified if op_RPPeerIPNumeric is specified.
             :type val_c_RPPeerIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerMapSource: The operator to apply to the field RPPeerMapSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerMapSource: Internal tracking data for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerMapSource: If op_RPPeerMapSource is specified, the field named in this input will be compared to the value in RPPeerMapSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerMapSource must be specified if op_RPPeerMapSource is specified.
             :type val_f_RPPeerMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerMapSource: If op_RPPeerMapSource is specified, this value will be compared to the value in RPPeerMapSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerMapSource must be specified if op_RPPeerMapSource is specified.
             :type val_c_RPPeerMapSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerStartTime: The operator to apply to the field RPPeerStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerStartTime: If op_RPPeerStartTime is specified, the field named in this input will be compared to the value in RPPeerStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerStartTime must be specified if op_RPPeerStartTime is specified.
             :type val_f_RPPeerStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerStartTime: If op_RPPeerStartTime is specified, this value will be compared to the value in RPPeerStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerStartTime must be specified if op_RPPeerStartTime is specified.
             :type val_c_RPPeerStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerState: The operator to apply to the field RPPeerState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerState: The protocol-specific state of this routing peer relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerState: If op_RPPeerState is specified, the field named in this input will be compared to the value in RPPeerState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerState must be specified if op_RPPeerState is specified.
             :type val_f_RPPeerState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerState: If op_RPPeerState is specified, this value will be compared to the value in RPPeerState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerState must be specified if op_RPPeerState is specified.
             :type val_c_RPPeerState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerTimestamp: The operator to apply to the field RPPeerTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerTimestamp: If op_RPPeerTimestamp is specified, the field named in this input will be compared to the value in RPPeerTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerTimestamp must be specified if op_RPPeerTimestamp is specified.
             :type val_f_RPPeerTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerTimestamp: If op_RPPeerTimestamp is specified, this value will be compared to the value in RPPeerTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerTimestamp must be specified if op_RPPeerTimestamp is specified.
             :type val_c_RPPeerTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerType: The operator to apply to the field RPPeerType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerType: Identifies the type of routing peer relationship this is (OSPF, BGP, IGRP). This is distinct from the protocol as some vendors may use different protocol names for similar protocols (IGRP and EIGRP, for example). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerType: If op_RPPeerType is specified, the field named in this input will be compared to the value in RPPeerType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerType must be specified if op_RPPeerType is specified.
             :type val_f_RPPeerType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerType: If op_RPPeerType is specified, this value will be compared to the value in RPPeerType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerType must be specified if op_RPPeerType is specified.
             :type val_c_RPPeerType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RPPeerUpSince: The operator to apply to the field RPPeerUpSince. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RPPeerUpSince: The date and time this peer relationship has been active, without interruption. The granularity level varies with each protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RPPeerUpSince: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RPPeerUpSince: If op_RPPeerUpSince is specified, the field named in this input will be compared to the value in RPPeerUpSince using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RPPeerUpSince must be specified if op_RPPeerUpSince is specified.
             :type val_f_RPPeerUpSince: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RPPeerUpSince: If op_RPPeerUpSince is specified, this value will be compared to the value in RPPeerUpSince using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RPPeerUpSince must be specified if op_RPPeerUpSince is specified.
             :type val_c_RPPeerUpSince: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteProto: The operator to apply to the field RouteProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteProto: Identifies the routing protocol used for this peer relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RoutingAreaID: The operator to apply to the field RoutingAreaID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingAreaID: The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device routing proto peers as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device routing proto peer methods. The listed methods will be called on each device routing proto peer returned and included in the output. Available methods are: peer_device, peer_interface, data_source, device, interface, routing_area, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: peer_device, peer_interface, data_source, device, interface, routing_area.
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
            |  ``default:`` DeviceRPPeerID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceRPPeerID. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each DeviceRoutingProtoPeer. Valid values are DeviceRPPeerID, RPPeerStartTime, RPPeerEndTime, RPPeerChangedCols, RPPeerTimestamp, DeviceID, InterfaceID, IfAddrID, RPPeerMapSource, RPPeerType, RouteProto, RoutingAreaID, RPPeerIPDotted, RPPeerIPNumeric, PeerDeviceID, PeerInterfaceID, RPPeerState, RPPeerUpSince, OspfPeerRouterIdentDotted, OspfPeerRouterIdentNumeric, OspfPeerAddresslessIndex, OspfPeerEventsDelta, OspfPeerPermanence, EigrpRetransCount, EigrpRetriesCount, BGPPeerPort, BGPLocalPort, BGPLocalIPDotted, BGPLocalIPNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return device_routing_proto_peers: An array of the DeviceRoutingProtoPeer objects that match the specified input criteria.
             :rtype device_routing_proto_peers: Array of DeviceRoutingProtoPeer

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def peer_device(self, **kwargs):
        """The peer router with which this device exchanges routing data.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The peer router with which this device exchanges routing data.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("peer_device"), kwargs)

    def interface(self, **kwargs):
        """The interface over which this peer relationship exists, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface over which this peer relationship exists, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def peer_interface(self, **kwargs):
        """The remote router's interface over which this peer relationship exists, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The remote router's interface over which this peer relationship exists, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("peer_interface"), kwargs)

    def routing_area(self, **kwargs):
        """The routing area or autonomous system associated with this routing peer relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The routing area or autonomous system associated with this routing peer relationship.
             :rtype : RoutingArea

            """

        return self.api_request(self._get_method_fullname("routing_area"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this routing peer data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this routing peer data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this routing peer data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceRPPeerID: The internal NetMRI identifier of this routing peer relationship.
             :type DeviceRPPeerID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device from which this routing peer data was collected.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
