from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class RoutingAreaRemote(RemoteModel):
    """
    This model captures the OSPF routing areas as well as the BGP and EIGRP autonomous systems identified as running on or connected to the network.


    |  ``EigrpVpnIndex:`` The SNMP index of the VRF to which this routing area belongs.
    |  ``attribute type:`` number

    |  ``RoutingAreaChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``RoutingAreaEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``RoutingAreaID:`` The internal NetMRI identifier for the routing area or autonomous system.
    |  ``attribute type:`` number

    |  ``RoutingAreaName:`` For OSPF, the dotted version of the Area ID. For other protocols, the AS.
    |  ``attribute type:`` string

    |  ``RoutingAreaNumber:`` The numerical OSPF Area ID, BGP AS or EIGRP AS.
    |  ``attribute type:`` number

    |  ``RoutingAreaStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``RoutingAreaTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``RoutingAreaType:`` OSPF, BGP, or EIGRP.
    |  ``attribute type:`` string


    """

    properties = ("EigrpVpnIndex",
                  "RoutingAreaChangedCols",
                  "RoutingAreaEndTime",
                  "RoutingAreaID",
                  "RoutingAreaName",
                  "RoutingAreaNumber",
                  "RoutingAreaStartTime",
                  "RoutingAreaTimestamp",
                  "RoutingAreaType",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"RoutingAreaID": self.RoutingAreaID})
