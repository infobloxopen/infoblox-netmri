from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfPerfRemote(RemoteModel):
    """
    Interface Performance information gathered by NetMRI.


    |  ``IfPerfID:`` The internal NetMRI identifier for this interface performance record.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``StartTime:`` The starting date/time of this sample.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The ending date and time of this sample.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP interface index for this interface.
    |  ``attribute type:`` string

    |  ``InterfaceID:`` The internal NetMRI identifier for this interface.
    |  ``attribute type:`` number

    |  ``ifSpeed:`` The interface speed indicator.
    |  ``attribute type:`` string

    |  ``ifTotalChanges:`` The interface total changes.
    |  ``attribute type:`` string

    |  ``ifInOctets:`` The number of octets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInUcastPkts:`` The number of Unicast packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInNUcastPkts:`` The number of Non-Unicast packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInMulticastPkts:`` The number of Multicast packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInBroadcastPkts:`` The number of Broadcast packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInDiscards:`` The number of discarded packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifInErrors:`` The number of error packets received by the interface.
    |  ``attribute type:`` string

    |  ``ifOutOctets:`` The number of octets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutUcastPkts:`` The number of Unicast packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutNUcastPkts:`` The number of Non-unicast packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutMulticastPkts:`` The number of multicast packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutBroadcastPkts:`` The number of broadcast packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutDiscards:`` The number of discarded packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifOutErrors:`` The number of error packets sent from the interface.
    |  ``attribute type:`` string

    |  ``ifAlignmentErrors:`` The number of alignment errors.
    |  ``attribute type:`` string

    |  ``ifFCSErrors:`` The number of FCS errors by the interface.
    |  ``attribute type:`` string

    |  ``ifLateCollisions:`` The number of LateCollisions by the interface.
    |  ``attribute type:`` string




    """

    properties = ("IfPerfID",
                  "DataSourceID",
                  "StartTime",
                  "EndTime",
                  "DeviceID",
                  "ifIndex",
                  "InterfaceID",
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
        return self.broker.data_source(**{"IfPerfID": self.IfPerfID})

    @property
    @check_api_availability
    def interface(self):
        """
        IfPerf model access the interface method from API accessible.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfPerfID": self.IfPerfID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfPerfID": self.IfPerfID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfPerfID": self.IfPerfID})
