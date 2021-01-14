from ..remote import RemoteModel


class SwitchFwdNeighborRemote(RemoteModel):
    """
    Neighbor relationships between a device providing L2 switching and the peer device.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``NeighborID:`` The internal NetMRI identifier for the neighbor relationship. This can be used to look up the Neighbor relationship which contains the source and destination device information.
    |  ``attribute type:`` number

    |  ``SwitchFwdNeighborChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SwitchFwdNeighborEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SwitchFwdNeighborMAC:`` The Media Access Controller (MAC) address of the destination neighbor in this neighbor relationship.
    |  ``attribute type:`` string

    |  ``SwitchFwdNeighborMapSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``SwitchFwdNeighborStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``SwitchFwdNeighborTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SwitchFwdNeighborType:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``SwitchFwdNeighborIPDotted:`` The IP address corresponding to the MAC found in the switch forwarding table, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SwitchFwdNeighborIPNumeric:`` The numerical value of the IP address corresponding to the MAC found in the switch forwarding table.
    |  ``attribute type:`` number

    |  ``SwitchFwdNeighborFirstSeenTime:`` The date and time this switch forwarding neighbor was first seen on the network, and since which it has been continuously present.
    |  ``attribute type:`` datetime

    |  ``SwitchFwdNeighborVlanID:`` The internal NetMRI identifier for the VLAN of this neighbor.
    |  ``attribute type:`` number

    |  ``SwitchFwdNeighborVlanIndex:`` The numerical VLAN number (VLAN ID) of this neighbor.
    |  ``attribute type:`` number

    |  ``network_name:`` The name of the Network View associated.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "NeighborID",
                  "SwitchFwdNeighborChangedCols",
                  "SwitchFwdNeighborEndTime",
                  "SwitchFwdNeighborMAC",
                  "SwitchFwdNeighborMapSource",
                  "SwitchFwdNeighborStartTime",
                  "SwitchFwdNeighborTimestamp",
                  "SwitchFwdNeighborType",
                  "SwitchFwdNeighborIPDotted",
                  "SwitchFwdNeighborIPNumeric",
                  "SwitchFwdNeighborFirstSeenTime",
                  "SwitchFwdNeighborVlanID",
                  "SwitchFwdNeighborVlanIndex",
                  "network_name",
                  )
