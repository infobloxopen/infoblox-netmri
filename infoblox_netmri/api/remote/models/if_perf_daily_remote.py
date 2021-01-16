from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfPerfDailyRemote(RemoteModel):
    """
    This table list out the entries of interface daily performance.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which interface daily performance information was collected.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The current index of local interface for the interface daily performance table entry.
    |  ``attribute type:`` number

    |  ``ifTotalChanges:`` The total number of changes occurs in each interface.
    |  ``attribute type:`` number

    |  ``ifInOctets:`` The number of incoming octets in interface daily performance.
    |  ``attribute type:`` number

    |  ``ifInUcastPkts:`` The number of Incoming unicast packets of local interface daily performance.
    |  ``attribute type:`` number

    |  ``ifInNUcastPkts:`` The number of non unicast packets of local interface daily performance.
    |  ``attribute type:`` number

    |  ``ifInMulticastPkts:`` The number of incoming multicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifInBroadcastPkts:`` The number of incoming broadcast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifInDiscards:`` The number of incoming discard packets of an interface.
    |  ``attribute type:`` number

    |  ``ifInErrors:`` The number of incoming errors of an interface.
    |  ``attribute type:`` number

    |  ``ifOutOctets:`` The number of outgoing octets.
    |  ``attribute type:`` number

    |  ``ifOutUcastPkts:`` The outgoing unicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutNUcastPkts:`` The outgoing non unicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutMulticastPkts:`` The outgoing multicast packets of each interface.
    |  ``attribute type:`` number

    |  ``ifOutBroadcastPkts:`` The outgoing broadcast packets of each interface.
    |  ``attribute type:`` number

    |  ``ifOutDiscards:`` The outgoing discarded packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutErrors:`` The outgoing errors of an interface.
    |  ``attribute type:`` number

    |  ``ifAlignmentErrors:`` The alignment errors of each interface.
    |  ``attribute type:`` number

    |  ``ifFCSErrors:`` The FCS Errors of each interface.
    |  ``attribute type:`` number

    |  ``ifLateCollisions:`` It describes a late collisions of daily performance interface.
    |  ``attribute type:`` number

    |  ``InThru:`` The number of packets coming from the starting point.
    |  ``attribute type:`` float

    |  ``OutThru:`` The number of packets reaching the destination point.
    |  ``attribute type:`` float

    |  ``TotalThru:`` The total number of packets passing through an interface.
    |  ``attribute type:`` float

    |  ``InUtil:`` Incoming utilities of each interface.
    |  ``attribute type:`` float

    |  ``OutUtil:`` Outgoing utilities of each interface.
    |  ``attribute type:`` float

    |  ``TotalUtil:`` The total number of utilities used in each interface.
    |  ``attribute type:`` float

    |  ``InErrorPct:`` The total number of incoming error packets.
    |  ``attribute type:`` float

    |  ``OutErrorPct:`` The total number of outgoing error packets.
    |  ``attribute type:`` float

    |  ``TotalErrorPct:`` The total number of error packets.
    |  ``attribute type:`` float

    |  ``InBcastPct:`` The total number of incoming broadcast packets.
    |  ``attribute type:`` float

    |  ``OutBcastPct:`` The total number of outgoing broadcast packets.
    |  ``attribute type:`` float

    |  ``TotalBcastPct:`` The total number of Broadcasting Packets.
    |  ``attribute type:`` float

    |  ``InDiscardPct:`` The total number of incoming discarded packets.
    |  ``attribute type:`` float

    |  ``OutDiscardPct:`` The total number of outgoing discarded packets.
    |  ``attribute type:`` float

    |  ``TotalDiscardPct:`` The total number of discard packets in each interface.
    |  ``attribute type:`` float

    """

    properties = ("DataSourceID",
                  "StartTime",
                  "EndTime",
                  "DeviceID",
                  "ifIndex",
                  "ifTotalChanges",
                  "ifInOctets",
                  "ifInUcastPkts",
                  "ifInNUcastPkts",
                  "ifInMulticastPkts",
                  "ifInBroadcastPkts",
                  "ifInDiscards",
                  "ifInErrors",
                  "ifOutOctets",
                  "ifOutUcastPkts",
                  "ifOutNUcastPkts",
                  "ifOutMulticastPkts",
                  "ifOutBroadcastPkts",
                  "ifOutDiscards",
                  "ifOutErrors",
                  "ifAlignmentErrors",
                  "ifFCSErrors",
                  "ifLateCollisions",
                  "InThru",
                  "OutThru",
                  "TotalThru",
                  "InUtil",
                  "OutUtil",
                  "TotalUtil",
                  "InErrorPct",
                  "OutErrorPct",
                  "TotalErrorPct",
                  "InBcastPct",
                  "OutBcastPct",
                  "TotalBcastPct",
                  "InDiscardPct",
                  "OutDiscardPct",
                  "TotalDiscardPct",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceID": self.DeviceID})
