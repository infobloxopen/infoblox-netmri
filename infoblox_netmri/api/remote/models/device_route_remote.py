from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceRouteRemote(RemoteModel):
    """
    The routing table entries for each device.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this routing table entry was collected.
    |  ``attribute type:`` number

    |  ``DeviceRouteID:`` The internal NetMRI identifier for this routing table entry on this device.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier of the outgoing interface for this route.
    |  ``attribute type:`` number

    |  ``RouteAdminDistance:`` The administrative distance of the protocol through which this route was learned, as specified by default Cisco conventions.
    |  ``attribute type:`` number

    |  ``RouteChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``RouteCIDR:`` The route destination network in CIDR format.
    |  ``attribute type:`` string

    |  ``RouteEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``RouteIfIndex:`` The SNMP interface index of the outgoing interface for this route.
    |  ``attribute type:`` number

    |  ``RouteMetric1:`` The first route metric value.
    |  ``attribute type:`` number

    |  ``RouteMetric2:`` The second route metric value.
    |  ``attribute type:`` number

    |  ``RouteNetMaskDotted:`` The network mask of the route destination network in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``RouteNetMaskNumeric:`` The numerical value of the network mask.
    |  ``attribute type:`` number

    |  ``RouteNextHopIPDotted:`` The next hop IP address for this route, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``RouteNextHopIPNumeric:`` The numerical value of the next hop IP address.
    |  ``attribute type:`` number

    |  ``RouteProto:`` The routing protocol through which this route was learned.
    |  ``attribute type:`` string

    |  ``RouteStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``RouteSubnetIPDotted:`` The route destination network address in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``RouteSubnetIPNumeric:`` The numerical value of the route destination network address.
    |  ``attribute type:`` number

    |  ``RouteTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``RouteType:`` The type of the route.
    |  ``attribute type:`` string




    |  ``VirtualNetworkMemberID:`` The internal NetMRI identifier for the VRF-based VPN related to this record.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "DeviceRouteID",
                  "InterfaceID",
                  "RouteAdminDistance",
                  "RouteChangedCols",
                  "RouteCIDR",
                  "RouteEndTime",
                  "RouteIfIndex",
                  "RouteMetric1",
                  "RouteMetric2",
                  "RouteNetMaskDotted",
                  "RouteNetMaskNumeric",
                  "RouteNextHopIPDotted",
                  "RouteNextHopIPNumeric",
                  "RouteProto",
                  "RouteStartTime",
                  "RouteSubnetIPDotted",
                  "RouteSubnetIPNumeric",
                  "RouteTimestamp",
                  "RouteType",
                  "VirtualNetworkMemberID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceRouteID": self.DeviceRouteID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this routing table entry was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceRouteID": self.DeviceRouteID})

    @property
    @check_api_availability
    def interface(self):
        """
        The outgoing interface for this route.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"DeviceRouteID": self.DeviceRouteID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this routing table entry was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceRouteID": self.DeviceRouteID})
