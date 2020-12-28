from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SerialNeighborRemote(RemoteModel):
    """
    Neighbor relationships identified the  NetMRI Point-to-Point neighbor detection algorithm. This includes serial neighbors and other numbered point-to-point connections.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``NeighborID:`` The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
    |  ``attribute type:`` number

    |  ``SerialNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SerialNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SerialNeighborIPDotted:`` The IP address of the point-to-point neighbor, in dotted (or colon-delimited for IPv6) format. This is the IP in the subnet used to create the numbered point-to-point relationship.
    |  ``attribute type:`` string

    |  ``SerialNeighborIPNumeric:`` The numerical value of the IP address of the point-to-point neighbor.
    |  ``attribute type:`` number

    |  ``SerialNeighborMapSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``SerialNeighborNetMaskDotted:`` The network mask of the subnet used in the numbered point-to-point relationship,  in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SerialNeighborNetMaskNumeric:`` The numerical value of the netmask of the subnet used in the numbered point-to-point relationship.
    |  ``attribute type:`` number

    |  ``SerialNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``SerialNeighborSubnetIPDotted:`` The network address of the subnet used in the numbered point-to-point relationship, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SerialNeighborSubnetIPNumeric:`` The numerical value of the network address of the subnet used in the numbered point-to-point relationship.
    |  ``attribute type:`` number

    |  ``SerialNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime


    """

    properties = ("DataSourceID",
                  "NeighborID",
                  "SerialNeighborChangedCols",
                  "SerialNeighborEndTime",
                  "SerialNeighborIPDotted",
                  "SerialNeighborIPNumeric",
                  "SerialNeighborMapSource",
                  "SerialNeighborNetMaskDotted",
                  "SerialNeighborNetMaskNumeric",
                  "SerialNeighborStartTime",
                  "SerialNeighborSubnetIPDotted",
                  "SerialNeighborSubnetIPNumeric",
                  "SerialNeighborTimestamp",
                  )

    @property
    @check_api_availability
    def neighbor(self):
        """
        The neighbor relationship, which contains the source and destination device information.
        ``attribute type:`` model
        """
        return self.broker.neighbor(**{"NeighborID": self.NeighborID})
