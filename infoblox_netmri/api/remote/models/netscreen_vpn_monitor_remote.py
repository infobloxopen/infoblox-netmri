from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class NetscreenVpnMonitorRemote(RemoteModel):
    """
    This table list out the entries of net screening vpn monitor.


    |  ``NSVpnMonID:`` The internal NetMRI identifier of net screen vpn monitor.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected.
    |  ``attribute type:`` number

    |  ``NSVpnMonStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``NSVpnMonEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``NSVpnMonTimeStamp:`` The date and time of net screen vpn monitor was found.
    |  ``attribute type:`` datetime

    |  ``NSVpnMonChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``NSVpnMonIndex:`` The index value of the local interface in the net screen vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonVpnName:`` The name of the Vpn in the netscreen monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonTunnelType:`` The NetMRI-determined tunnel type of net screen vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonEspEncAlg:`` The encrypted algorithm of netscreen monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonEspAuthAlg:`` The authenticate algorithm of net screen vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonKeyType:`` The NetMRI-determined key type of Netscreen Vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonP1Auth:`` The authentication of Netscreen Vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonVpnType:`` The NetMRI-determined Vpn type of Netscreen Vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonRmtGwIPDotted:`` The management IP address of the netscreen Vpn monitor id dotted(or colon delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``NSVpnMonRmtGwIPNumeric:`` The numerical value of remote IP address of netscreen Vpn monitor.
    |  ``attribute type:`` number

    |  ``NSVpnMonRmtGwId:`` The internal identifier of remote host in the netscreen Vpn monitor.
    |  ``attribute type:`` number

    |  ``NSVpnMonP1State:`` The initial state of netscreen Vpn monitor.
    |  ``attribute type:`` string

    |  ``NSVpnMonP2State:`` The second state of netscreen Vpn monitor.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    """

    properties = ("NSVpnMonID",
                  "DeviceID",
                  "NSVpnMonStartTime",
                  "NSVpnMonEndTime",
                  "NSVpnMonTimeStamp",
                  "NSVpnMonChangedCols",
                  "NSVpnMonIndex",
                  "NSVpnMonVpnName",
                  "NSVpnMonTunnelType",
                  "NSVpnMonEspEncAlg",
                  "NSVpnMonEspAuthAlg",
                  "NSVpnMonKeyType",
                  "NSVpnMonP1Auth",
                  "NSVpnMonVpnType",
                  "NSVpnMonRmtGwIPDotted",
                  "NSVpnMonRmtGwIPNumeric",
                  "NSVpnMonRmtGwId",
                  "NSVpnMonP1State",
                  "NSVpnMonP2State",
                  "DataSourceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"NSVpnMonID": self.NSVpnMonID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"NSVpnMonID": self.NSVpnMonID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"NSVpnMonID": self.NSVpnMonID})
