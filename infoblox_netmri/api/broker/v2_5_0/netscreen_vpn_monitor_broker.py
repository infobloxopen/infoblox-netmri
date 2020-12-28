from ..broker import Broker


class NetscreenVpnMonitorBroker(Broker):
    controller = "netscreen_vpn_monitors"

    def index(self, **kwargs):
        """Lists the available netscreen vpn monitors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the netscreen vpn monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen vpn monitor methods. The listed methods will be called on each netscreen vpn monitor returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` NSVpnMonID

             :param sort: The data field(s) to use for sorting the output. Default is NSVpnMonID. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each NetscreenVpnMonitor. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return netscreen_vpn_monitors: An array of the NetscreenVpnMonitor objects that match the specified input criteria.
             :rtype netscreen_vpn_monitors: Array of NetscreenVpnMonitor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified netscreen vpn monitor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen vpn monitor methods. The listed methods will be called on each netscreen vpn monitor returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return netscreen_vpn_monitor: The netscreen vpn monitor identified by the specified NSVpnMonID.
             :rtype netscreen_vpn_monitor: NetscreenVpnMonitor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available netscreen vpn monitors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NSVpnMonChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NSVpnMonChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEndTime: The ending effective time of this record, or empty if still in effect.
             :type NSVpnMonEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEndTime: The ending effective time of this record, or empty if still in effect.
             :type NSVpnMonEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEspAuthAlg: The authenticate algorithm of net screen vpn monitor.
             :type NSVpnMonEspAuthAlg: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEspAuthAlg: The authenticate algorithm of net screen vpn monitor.
             :type NSVpnMonEspAuthAlg: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEspEncAlg: The encrypted algorithm of netscreen monitor.
             :type NSVpnMonEspEncAlg: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonEspEncAlg: The encrypted algorithm of netscreen monitor.
             :type NSVpnMonEspEncAlg: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonIndex: The index value of the local interface in the net screen vpn monitor.
             :type NSVpnMonIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonIndex: The index value of the local interface in the net screen vpn monitor.
             :type NSVpnMonIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonKeyType: The NetMRI-determined key type of Netscreen Vpn monitor.
             :type NSVpnMonKeyType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonKeyType: The NetMRI-determined key type of Netscreen Vpn monitor.
             :type NSVpnMonKeyType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP1Auth: The authentication of Netscreen Vpn monitor.
             :type NSVpnMonP1Auth: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP1Auth: The authentication of Netscreen Vpn monitor.
             :type NSVpnMonP1Auth: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP1State: The initial state of netscreen Vpn monitor.
             :type NSVpnMonP1State: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP1State: The initial state of netscreen Vpn monitor.
             :type NSVpnMonP1State: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP2State: The second state of netscreen Vpn monitor.
             :type NSVpnMonP2State: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonP2State: The second state of netscreen Vpn monitor.
             :type NSVpnMonP2State: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwIPDotted: The management IP address of the netscreen Vpn monitor id dotted(or colon delimited for IPv6) format.
             :type NSVpnMonRmtGwIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwIPDotted: The management IP address of the netscreen Vpn monitor id dotted(or colon delimited for IPv6) format.
             :type NSVpnMonRmtGwIPDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwIPNumeric: The numerical value of remote IP address of netscreen Vpn monitor.
             :type NSVpnMonRmtGwIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwIPNumeric: The numerical value of remote IP address of netscreen Vpn monitor.
             :type NSVpnMonRmtGwIPNumeric: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwId: The internal identifier of remote host in the netscreen Vpn monitor.
             :type NSVpnMonRmtGwId: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonRmtGwId: The internal identifier of remote host in the netscreen Vpn monitor.
             :type NSVpnMonRmtGwId: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonStartTime: The starting effective time of this record.
             :type NSVpnMonStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonStartTime: The starting effective time of this record.
             :type NSVpnMonStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonTimeStamp: The date and time of net screen vpn monitor was found.
             :type NSVpnMonTimeStamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonTimeStamp: The date and time of net screen vpn monitor was found.
             :type NSVpnMonTimeStamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonTunnelType: The NetMRI-determined tunnel type of net screen vpn monitor.
             :type NSVpnMonTunnelType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonTunnelType: The NetMRI-determined tunnel type of net screen vpn monitor.
             :type NSVpnMonTunnelType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonVpnName: The name of the Vpn in the netscreen monitor.
             :type NSVpnMonVpnName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonVpnName: The name of the Vpn in the netscreen monitor.
             :type NSVpnMonVpnName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonVpnType: The NetMRI-determined Vpn type of Netscreen Vpn monitor.
             :type NSVpnMonVpnType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSVpnMonVpnType: The NetMRI-determined Vpn type of Netscreen Vpn monitor.
             :type NSVpnMonVpnType: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the netscreen vpn monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen vpn monitor methods. The listed methods will be called on each netscreen vpn monitor returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` NSVpnMonID

             :param sort: The data field(s) to use for sorting the output. Default is NSVpnMonID. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each NetscreenVpnMonitor. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against netscreen vpn monitors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, NSVpnMonChangedCols, NSVpnMonEndTime, NSVpnMonEspAuthAlg, NSVpnMonEspEncAlg, NSVpnMonID, NSVpnMonIndex, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonP1State, NSVpnMonP2State, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonStartTime, NSVpnMonTimeStamp, NSVpnMonTunnelType, NSVpnMonVpnName, NSVpnMonVpnType.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return netscreen_vpn_monitors: An array of the NetscreenVpnMonitor objects that match the specified input criteria.
             :rtype netscreen_vpn_monitors: Array of NetscreenVpnMonitor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available netscreen vpn monitors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, NSVpnMonChangedCols, NSVpnMonEndTime, NSVpnMonEspAuthAlg, NSVpnMonEspEncAlg, NSVpnMonID, NSVpnMonIndex, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonP1State, NSVpnMonP2State, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonStartTime, NSVpnMonTimeStamp, NSVpnMonTunnelType, NSVpnMonVpnName, NSVpnMonVpnType.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceID: If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_f_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceID: If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_c_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which netscreen vpn monitor entry was calculated or collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceID: If op_DeviceID is specified, the field named in this input will be compared to the value in DeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceID must be specified if op_DeviceID is specified.
             :type val_f_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceID: If op_DeviceID is specified, this value will be compared to the value in DeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceID must be specified if op_DeviceID is specified.
             :type val_c_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonChangedCols: The operator to apply to the field NSVpnMonChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonChangedCols: If op_NSVpnMonChangedCols is specified, the field named in this input will be compared to the value in NSVpnMonChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonChangedCols must be specified if op_NSVpnMonChangedCols is specified.
             :type val_f_NSVpnMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonChangedCols: If op_NSVpnMonChangedCols is specified, this value will be compared to the value in NSVpnMonChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonChangedCols must be specified if op_NSVpnMonChangedCols is specified.
             :type val_c_NSVpnMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonEndTime: The operator to apply to the field NSVpnMonEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonEndTime: If op_NSVpnMonEndTime is specified, the field named in this input will be compared to the value in NSVpnMonEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonEndTime must be specified if op_NSVpnMonEndTime is specified.
             :type val_f_NSVpnMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonEndTime: If op_NSVpnMonEndTime is specified, this value will be compared to the value in NSVpnMonEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonEndTime must be specified if op_NSVpnMonEndTime is specified.
             :type val_c_NSVpnMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonEspAuthAlg: The operator to apply to the field NSVpnMonEspAuthAlg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonEspAuthAlg: The authenticate algorithm of net screen vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonEspAuthAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonEspAuthAlg: If op_NSVpnMonEspAuthAlg is specified, the field named in this input will be compared to the value in NSVpnMonEspAuthAlg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonEspAuthAlg must be specified if op_NSVpnMonEspAuthAlg is specified.
             :type val_f_NSVpnMonEspAuthAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonEspAuthAlg: If op_NSVpnMonEspAuthAlg is specified, this value will be compared to the value in NSVpnMonEspAuthAlg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonEspAuthAlg must be specified if op_NSVpnMonEspAuthAlg is specified.
             :type val_c_NSVpnMonEspAuthAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonEspEncAlg: The operator to apply to the field NSVpnMonEspEncAlg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonEspEncAlg: The encrypted algorithm of netscreen monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonEspEncAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonEspEncAlg: If op_NSVpnMonEspEncAlg is specified, the field named in this input will be compared to the value in NSVpnMonEspEncAlg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonEspEncAlg must be specified if op_NSVpnMonEspEncAlg is specified.
             :type val_f_NSVpnMonEspEncAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonEspEncAlg: If op_NSVpnMonEspEncAlg is specified, this value will be compared to the value in NSVpnMonEspEncAlg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonEspEncAlg must be specified if op_NSVpnMonEspEncAlg is specified.
             :type val_c_NSVpnMonEspEncAlg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonID: The operator to apply to the field NSVpnMonID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonID: If op_NSVpnMonID is specified, the field named in this input will be compared to the value in NSVpnMonID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonID must be specified if op_NSVpnMonID is specified.
             :type val_f_NSVpnMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonID: If op_NSVpnMonID is specified, this value will be compared to the value in NSVpnMonID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonID must be specified if op_NSVpnMonID is specified.
             :type val_c_NSVpnMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonIndex: The operator to apply to the field NSVpnMonIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonIndex: The index value of the local interface in the net screen vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonIndex: If op_NSVpnMonIndex is specified, the field named in this input will be compared to the value in NSVpnMonIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonIndex must be specified if op_NSVpnMonIndex is specified.
             :type val_f_NSVpnMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonIndex: If op_NSVpnMonIndex is specified, this value will be compared to the value in NSVpnMonIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonIndex must be specified if op_NSVpnMonIndex is specified.
             :type val_c_NSVpnMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonKeyType: The operator to apply to the field NSVpnMonKeyType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonKeyType: The NetMRI-determined key type of Netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonKeyType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonKeyType: If op_NSVpnMonKeyType is specified, the field named in this input will be compared to the value in NSVpnMonKeyType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonKeyType must be specified if op_NSVpnMonKeyType is specified.
             :type val_f_NSVpnMonKeyType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonKeyType: If op_NSVpnMonKeyType is specified, this value will be compared to the value in NSVpnMonKeyType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonKeyType must be specified if op_NSVpnMonKeyType is specified.
             :type val_c_NSVpnMonKeyType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonP1Auth: The operator to apply to the field NSVpnMonP1Auth. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonP1Auth: The authentication of Netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonP1Auth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonP1Auth: If op_NSVpnMonP1Auth is specified, the field named in this input will be compared to the value in NSVpnMonP1Auth using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonP1Auth must be specified if op_NSVpnMonP1Auth is specified.
             :type val_f_NSVpnMonP1Auth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonP1Auth: If op_NSVpnMonP1Auth is specified, this value will be compared to the value in NSVpnMonP1Auth using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonP1Auth must be specified if op_NSVpnMonP1Auth is specified.
             :type val_c_NSVpnMonP1Auth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonP1State: The operator to apply to the field NSVpnMonP1State. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonP1State: The initial state of netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonP1State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonP1State: If op_NSVpnMonP1State is specified, the field named in this input will be compared to the value in NSVpnMonP1State using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonP1State must be specified if op_NSVpnMonP1State is specified.
             :type val_f_NSVpnMonP1State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonP1State: If op_NSVpnMonP1State is specified, this value will be compared to the value in NSVpnMonP1State using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonP1State must be specified if op_NSVpnMonP1State is specified.
             :type val_c_NSVpnMonP1State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonP2State: The operator to apply to the field NSVpnMonP2State. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonP2State: The second state of netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonP2State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonP2State: If op_NSVpnMonP2State is specified, the field named in this input will be compared to the value in NSVpnMonP2State using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonP2State must be specified if op_NSVpnMonP2State is specified.
             :type val_f_NSVpnMonP2State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonP2State: If op_NSVpnMonP2State is specified, this value will be compared to the value in NSVpnMonP2State using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonP2State must be specified if op_NSVpnMonP2State is specified.
             :type val_c_NSVpnMonP2State: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonRmtGwIPDotted: The operator to apply to the field NSVpnMonRmtGwIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonRmtGwIPDotted: The management IP address of the netscreen Vpn monitor id dotted(or colon delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonRmtGwIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonRmtGwIPDotted: If op_NSVpnMonRmtGwIPDotted is specified, the field named in this input will be compared to the value in NSVpnMonRmtGwIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonRmtGwIPDotted must be specified if op_NSVpnMonRmtGwIPDotted is specified.
             :type val_f_NSVpnMonRmtGwIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonRmtGwIPDotted: If op_NSVpnMonRmtGwIPDotted is specified, this value will be compared to the value in NSVpnMonRmtGwIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonRmtGwIPDotted must be specified if op_NSVpnMonRmtGwIPDotted is specified.
             :type val_c_NSVpnMonRmtGwIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonRmtGwIPNumeric: The operator to apply to the field NSVpnMonRmtGwIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonRmtGwIPNumeric: The numerical value of remote IP address of netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonRmtGwIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonRmtGwIPNumeric: If op_NSVpnMonRmtGwIPNumeric is specified, the field named in this input will be compared to the value in NSVpnMonRmtGwIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonRmtGwIPNumeric must be specified if op_NSVpnMonRmtGwIPNumeric is specified.
             :type val_f_NSVpnMonRmtGwIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonRmtGwIPNumeric: If op_NSVpnMonRmtGwIPNumeric is specified, this value will be compared to the value in NSVpnMonRmtGwIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonRmtGwIPNumeric must be specified if op_NSVpnMonRmtGwIPNumeric is specified.
             :type val_c_NSVpnMonRmtGwIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonRmtGwId: The operator to apply to the field NSVpnMonRmtGwId. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonRmtGwId: The internal identifier of remote host in the netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonRmtGwId: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonRmtGwId: If op_NSVpnMonRmtGwId is specified, the field named in this input will be compared to the value in NSVpnMonRmtGwId using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonRmtGwId must be specified if op_NSVpnMonRmtGwId is specified.
             :type val_f_NSVpnMonRmtGwId: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonRmtGwId: If op_NSVpnMonRmtGwId is specified, this value will be compared to the value in NSVpnMonRmtGwId using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonRmtGwId must be specified if op_NSVpnMonRmtGwId is specified.
             :type val_c_NSVpnMonRmtGwId: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonStartTime: The operator to apply to the field NSVpnMonStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonStartTime: If op_NSVpnMonStartTime is specified, the field named in this input will be compared to the value in NSVpnMonStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonStartTime must be specified if op_NSVpnMonStartTime is specified.
             :type val_f_NSVpnMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonStartTime: If op_NSVpnMonStartTime is specified, this value will be compared to the value in NSVpnMonStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonStartTime must be specified if op_NSVpnMonStartTime is specified.
             :type val_c_NSVpnMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonTimeStamp: The operator to apply to the field NSVpnMonTimeStamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonTimeStamp: The date and time of net screen vpn monitor was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonTimeStamp: If op_NSVpnMonTimeStamp is specified, the field named in this input will be compared to the value in NSVpnMonTimeStamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonTimeStamp must be specified if op_NSVpnMonTimeStamp is specified.
             :type val_f_NSVpnMonTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonTimeStamp: If op_NSVpnMonTimeStamp is specified, this value will be compared to the value in NSVpnMonTimeStamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonTimeStamp must be specified if op_NSVpnMonTimeStamp is specified.
             :type val_c_NSVpnMonTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonTunnelType: The operator to apply to the field NSVpnMonTunnelType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonTunnelType: The NetMRI-determined tunnel type of net screen vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonTunnelType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonTunnelType: If op_NSVpnMonTunnelType is specified, the field named in this input will be compared to the value in NSVpnMonTunnelType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonTunnelType must be specified if op_NSVpnMonTunnelType is specified.
             :type val_f_NSVpnMonTunnelType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonTunnelType: If op_NSVpnMonTunnelType is specified, this value will be compared to the value in NSVpnMonTunnelType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonTunnelType must be specified if op_NSVpnMonTunnelType is specified.
             :type val_c_NSVpnMonTunnelType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonVpnName: The operator to apply to the field NSVpnMonVpnName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonVpnName: The name of the Vpn in the netscreen monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonVpnName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonVpnName: If op_NSVpnMonVpnName is specified, the field named in this input will be compared to the value in NSVpnMonVpnName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonVpnName must be specified if op_NSVpnMonVpnName is specified.
             :type val_f_NSVpnMonVpnName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonVpnName: If op_NSVpnMonVpnName is specified, this value will be compared to the value in NSVpnMonVpnName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonVpnName must be specified if op_NSVpnMonVpnName is specified.
             :type val_c_NSVpnMonVpnName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSVpnMonVpnType: The operator to apply to the field NSVpnMonVpnType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSVpnMonVpnType: The NetMRI-determined Vpn type of Netscreen Vpn monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSVpnMonVpnType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSVpnMonVpnType: If op_NSVpnMonVpnType is specified, the field named in this input will be compared to the value in NSVpnMonVpnType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSVpnMonVpnType must be specified if op_NSVpnMonVpnType is specified.
             :type val_f_NSVpnMonVpnType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSVpnMonVpnType: If op_NSVpnMonVpnType is specified, this value will be compared to the value in NSVpnMonVpnType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSVpnMonVpnType must be specified if op_NSVpnMonVpnType is specified.
             :type val_c_NSVpnMonVpnType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the netscreen vpn monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen vpn monitor methods. The listed methods will be called on each netscreen vpn monitor returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` NSVpnMonID

             :param sort: The data field(s) to use for sorting the output. Default is NSVpnMonID. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each NetscreenVpnMonitor. Valid values are NSVpnMonID, DeviceID, NSVpnMonStartTime, NSVpnMonEndTime, NSVpnMonTimeStamp, NSVpnMonChangedCols, NSVpnMonIndex, NSVpnMonVpnName, NSVpnMonTunnelType, NSVpnMonEspEncAlg, NSVpnMonEspAuthAlg, NSVpnMonKeyType, NSVpnMonP1Auth, NSVpnMonVpnType, NSVpnMonRmtGwIPDotted, NSVpnMonRmtGwIPNumeric, NSVpnMonRmtGwId, NSVpnMonP1State, NSVpnMonP2State, DataSourceID. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return netscreen_vpn_monitors: An array of the NetscreenVpnMonitor objects that match the specified input criteria.
             :rtype netscreen_vpn_monitors: Array of NetscreenVpnMonitor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSVpnMonID: The internal NetMRI identifier of net screen vpn monitor.
             :type NSVpnMonID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
