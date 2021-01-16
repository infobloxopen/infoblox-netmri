from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class RevSwitchFwdNeighborRemote(RemoteModel):
    """
    Refers to the 'reversed' switch forwarding relationship; ie, from the access device to the switch.


    |  ``NeighborID:`` The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
    |  ``attribute type:`` number

    |  ``RevSwitchFwdNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``RevSwitchFwdNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``RevSwitchFwdNeighborMapSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``RevSwitchFwdNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``RevSwitchFwdNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SwitchFwdNeighborID:`` The internal NetMRI identifier for the switch forwarding neighbor relationship that was 'reversed' in order to generate this neighbor relationship.
    |  ``attribute type:`` number


    """

    properties = ("NeighborID",
                  "RevSwitchFwdNeighborChangedCols",
                  "RevSwitchFwdNeighborEndTime",
                  "RevSwitchFwdNeighborMapSource",
                  "RevSwitchFwdNeighborStartTime",
                  "RevSwitchFwdNeighborTimestamp",
                  "SwitchFwdNeighborID",
                  )

    @property
    @check_api_availability
    def neighbor(self):
        """
        The neighbor relationship, which contains the source and destination device information.
        ``attribute type:`` model
        """
        return self.broker.neighbor(**{"NeighborID": self.NeighborID})
