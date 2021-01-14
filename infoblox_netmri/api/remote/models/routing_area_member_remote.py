from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class RoutingAreaMemberRemote(RemoteModel):
    """
    This model details routers' memberships in routing areas or autonomous systems.




    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``RoutingAreaMemberStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``RoutingAreaMemberEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``RoutingAreaMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``RoutingAreaMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this routing area membership was collected.
    |  ``attribute type:`` number

    |  ``RoutingAreaMemberID:`` The internal NetMRI identifier for this routing area membership.
    |  ``attribute type:`` number

    |  ``RoutingAreaMemberSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``RoutingAreaID:`` The internal NetMRI identifier for the routing area associated with this membership.
    |  ``attribute type:`` number

    |  ``RoutingAreaID:`` The internal NetMRI identifier for the routing area or autonomous system associated with this membership.
    |  ``attribute type:`` number

    |  ``OspfSpfRunsDelta:`` The number of times that the intra-area route table has been calculated using this area's link-state database (typically using Dijkstra's algorithm), since the last time NetMRI polled the device.
    |  ``attribute type:`` number

    |  ``OspfAuthType:`` The type of authentication configured on this area for this router.
    |  ``attribute type:`` string

    |  ``OspfImportAsExtern:`` The type of this OSPF area, according to this router. (importExternal for a standard are, noImportExternal for a stub, and importNssa for a not-so-stubby area).
    |  ``attribute type:`` string

    |  ``OspfAreaBdrRtrCount:`` The total number of area border routers reachable within this area.  This is initially zero, and is calculated in each SPF Pass.
    |  ``attribute type:`` number

    |  ``OspfAsBdrRtrCount:`` The total number of Autonomous System border routers reachable within this area, according to this router. This is initially zero, and is calculated in each SPF Pass.
    |  ``attribute type:`` number

    |  ``OspfAreaLsaCount:`` The total number of link-state advertisements in this area's link-state database on this router, excluding AS External LSA's.
    |  ``attribute type:`` number

    |  ``OspfAreaLsaCksumSum:`` The sum of the link-state advertisements' LS checksums contained in this area's link-state database on this router. This sum excludes external (LS type 5) link-state advertisements. The sum can be used to determine if there has been a change in a router's link state database, and to compare the link-state database of two routers.
    |  ``attribute type:`` number

    |  ``OspfAreaSummaryInd:`` Indicates how the router handles import of summary LSAs into stub areas. It has no effect on other areas.

If true, than the router will both summarize and propagate summary LSAs into the stub area.

Otherwise, the router will neither originate nor propagate summary LSAs. It will rely entirely on its default route.
    |  ``attribute type:`` bool



    """

    properties = ("DataSourceID",
                  "RoutingAreaMemberStartTime",
                  "RoutingAreaMemberEndTime",
                  "RoutingAreaMemberChangedCols",
                  "RoutingAreaMemberTimestamp",
                  "DeviceID",
                  "RoutingAreaMemberID",
                  "RoutingAreaMemberSource",
                  "RoutingAreaID",
                  "RoutingAreaID",
                  "OspfSpfRunsDelta",
                  "OspfAuthType",
                  "OspfImportAsExtern",
                  "OspfAreaBdrRtrCount",
                  "OspfAsBdrRtrCount",
                  "OspfAreaLsaCount",
                  "OspfAreaLsaCksumSum",
                  "OspfAreaSummaryInd",
                  )

    @property
    @check_api_availability
    def routing_area(self):
        """
        The routing area or autonomous system associated with this membership.
        ``attribute type:`` model
        """
        return self.broker.routing_area(**{"RoutingAreaMemberID": self.RoutingAreaMemberID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI collector that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"RoutingAreaMemberID": self.RoutingAreaMemberID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this routing area membership was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"RoutingAreaMemberID": self.RoutingAreaMemberID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface used to participate in this routing area.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"RoutingAreaMemberID": self.RoutingAreaMemberID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this routing area membership was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"RoutingAreaMemberID": self.RoutingAreaMemberID})
