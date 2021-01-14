from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class BestOriginRouteRemote(RemoteModel):
    """
    The device routing table entries found in the network with the lowest administrative distance for the specific route.


    |  ``DeviceRouteID:`` The internal NetMRI identifier of the device routing table entry.
    |  ``attribute type:`` number

    |  ``BORouteStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``BORouteEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``BORouteChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``BORouteTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this route was collected.
    |  ``attribute type:`` number

    |  ``RouteCIDR:`` The route, in CIDR notation.
    |  ``attribute type:`` string

    |  ``RouteProto:`` The routing protocol through which this route was learned.
    |  ``attribute type:`` string

    |  ``RouteType:`` The route type as reported by the device.
    |  ``attribute type:`` string

    |  ``RouteLocation:`` The route location, either Internal or External. Internal routes are those within the NetMRI discovery ranges.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberID:`` The internal NetMRI identifier for the Virtual Network Member for this route.
    |  ``attribute type:`` number



    """

    properties = ("DeviceRouteID",
                  "BORouteStartTime",
                  "BORouteEndTime",
                  "BORouteChangedCols",
                  "BORouteTimestamp",
                  "DeviceID",
                  "RouteCIDR",
                  "RouteProto",
                  "RouteType",
                  "RouteLocation",
                  "VirtualNetworkMemberID",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceRouteID": self.DeviceRouteID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DeviceRouteID": self.DeviceRouteID})
