from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfPerfHourlyRemote(RemoteModel):
    """
    This table list out the entries of interface hourly performance.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which interface hourly performance information was collected.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The current index of hourly performance of an interface.
    |  ``attribute type:`` number

    |  ``ifSpeed:`` The speed of packets sends per hour.
    |  ``attribute type:`` number

    |  ``ifTotalChanges:`` The total number of changes occurs in each hour of an interface.
    |  ``attribute type:`` number

    |  ``ifInOctets:`` The total number of incoming octets.
    |  ``attribute type:`` number

    |  ``ifInUcastPkts:`` The number of incoming unicast packets.
    |  ``attribute type:`` number

    |  ``ifInNUcastPkts:`` The number of non unicasting packets.
    |  ``attribute type:`` number

    |  ``ifInMulticastPkts:`` The number of incoming multicast packets.
    |  ``attribute type:`` number

    |  ``ifInBroadcastPkts:`` The number of incoming broadcast packets.
    |  ``attribute type:`` number

    |  ``ifInDiscards:`` The number of incoming discarded packets.
    |  ``attribute type:`` number

    |  ``ifInErrors:`` The number of incoming errors in each packet of an interface.
    |  ``attribute type:`` number

    |  ``ifOutOctets:`` The number of outgoing octets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutUcastPkts:`` The number of outgoing unicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutNUcastPkts:`` The number of outgoing non unicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutMulticastPkts:`` The number of outgoing multicast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutBroadcastPkts:`` The number of outgoing broadcast packets of an interface.
    |  ``attribute type:`` number

    |  ``ifOutDiscards:`` The number of outgoing discarded packets.
    |  ``attribute type:`` number

    |  ``ifOutErrors:`` The number of outgoing error packets.
    |  ``attribute type:`` number

    |  ``ifAlignmentErrors:`` The number of alignment errors of each packet in the interface.
    |  ``attribute type:`` number

    |  ``ifFCSErrors:`` The number of FCS errors of each packet in the interface.
    |  ``attribute type:`` number

    |  ``ifLateCollisions:`` The number of late collisions occurs while sending the packets.
    |  ``attribute type:`` number

    """

    properties = ("DataSourceID",
                  "StartTime",
                  "EndTime",
                  "DeviceID",
                  "ifIndex",
                  "ifSpeed",
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
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceID": self.DeviceID})
