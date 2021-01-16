from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceRoutingProtoPeerRemote(RemoteModel):
    """
    This model captures routing peer information for EIGRP, BGP, and OSPF routing relationships.





    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``RPPeerStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``RPPeerEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``RPPeerChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``RPPeerTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceRPPeerID:`` The internal NetMRI identifier of this routing peer relationship.
    |  ``attribute type:`` number

    |  ``RPPeerMapSource:`` Internal tracking data for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``RouteProto:`` Identifies the routing protocol used for this peer relationship.
    |  ``attribute type:`` string

    |  ``RPPeerState:`` The protocol-specific state of this routing peer relationship.
    |  ``attribute type:`` string

    |  ``RPPeerUpSince:`` The date and time this peer relationship has been active, without interruption. The granularity level varies with each protocol.
    |  ``attribute type:`` datetime

    |  ``RPPeerType:`` Identifies the type of routing peer relationship this is (OSPF, BGP, IGRP). This is distinct from the protocol as some vendors may use different protocol names for similar protocols (IGRP and EIGRP, for example).
    |  ``attribute type:`` string


    |  ``InterfaceID:`` The internal NetMRI identifier for the interface over which this peer relationship exists, if available.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this routing peer data was collected.
    |  ``attribute type:`` number

    |  ``IfAddrID:`` The internal NetMRI identifier for the local IP address used in this peer relationship, if available.
    |  ``attribute type:`` number

    |  ``RPPeerIPDotted:`` The IP address of the peer, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``RPPeerIPNumeric:`` The numerical IP address of the peer.
    |  ``attribute type:`` string


    |  ``PeerInterfaceID:`` The internal NetMRI identifier for the remote router's interface over which this peer relationship exists, if available.
    |  ``attribute type:`` number

    |  ``PeerDeviceID:`` The internal NetMRI identifier for the peer device.
    |  ``attribute type:`` number


    |  ``OspfPeerRouterIdentDotted:`` The OSPF router identifier of the peer, in dotted (or colon-delimited for IPv6) format, if relevant.
    |  ``attribute type:`` string

    |  ``RoutingAreaID:`` The internal NetMRI identifier for the routing area or autonomous system associated with this routing peer relationship.
    |  ``attribute type:`` number

    |  ``OspfPeerRouterIdentNumeric:`` The numerical OSPF router identifier of the peer.
    |  ``attribute type:`` number

    |  ``OspfPeerAddresslessIndex:`` For addressless peer interfaces, this will contain the SNMP interface index for the peer's interface. The peer IP address will contain the IP of another interface on the peer.
    |  ``attribute type:`` number

    |  ``OspfPeerPermanence:`` How this neighbor was determined, 'dynamic' for learned through the protocol, 'permanent' for configured.
    |  ``attribute type:`` string

    |  ``OspfPeerEventsDelta:`` The number of times that this neighbor relationship has changed state, since the last time NetMRI polled the device.
    |  ``attribute type:`` number

    |  ``EigrpRetransCount:`` The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up.
    |  ``attribute type:`` number

    |  ``EigrpRetriesCount:`` The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged.
    |  ``attribute type:`` number

    |  ``BGPPeerPort:`` The remote TCP port number for this entry's BGP connection.
    |  ``attribute type:`` number

    |  ``BGPLocalPort:`` The local TCP port number for this entry's BGP connection.
    |  ``attribute type:`` number

    |  ``BGPLocalIPDotted:`` The numerical local IP address for this peer relationship's BGP connection.
    |  ``attribute type:`` string

    |  ``BGPLocalIPNumeric:`` The local IP address for this peer relationship's BGP connection, in dotted (or colon-delimited for IPv6) notation.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "RPPeerStartTime",
                  "RPPeerEndTime",
                  "RPPeerChangedCols",
                  "RPPeerTimestamp",
                  "DeviceRPPeerID",
                  "RPPeerMapSource",
                  "RouteProto",
                  "RPPeerState",
                  "RPPeerUpSince",
                  "RPPeerType",
                  "InterfaceID",
                  "DeviceID",
                  "IfAddrID",
                  "RPPeerIPDotted",
                  "RPPeerIPNumeric",
                  "PeerInterfaceID",
                  "PeerDeviceID",
                  "OspfPeerRouterIdentDotted",
                  "RoutingAreaID",
                  "OspfPeerRouterIdentNumeric",
                  "OspfPeerAddresslessIndex",
                  "OspfPeerPermanence",
                  "OspfPeerEventsDelta",
                  "EigrpRetransCount",
                  "EigrpRetriesCount",
                  "BGPPeerPort",
                  "BGPLocalPort",
                  "BGPLocalIPDotted",
                  "BGPLocalIPNumeric",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this routing peer data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def peer_device(self):
        """
        The peer router with which this device exchanges routing data.
        ``attribute type:`` model
        """
        return self.broker.peer_device(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The internal NetMRI identifier for the collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface over which this peer relationship exists, if available.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def peer_interface(self):
        """
        The remote router's interface over which this peer relationship exists, if available.
        ``attribute type:`` model
        """
        return self.broker.peer_interface(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def routing_area(self):
        """
        The routing area or autonomous system associated with this routing peer relationship.
        ``attribute type:`` model
        """
        return self.broker.routing_area(**{"DeviceRPPeerID": self.DeviceRPPeerID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this routing peer data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceRPPeerID": self.DeviceRPPeerID})
