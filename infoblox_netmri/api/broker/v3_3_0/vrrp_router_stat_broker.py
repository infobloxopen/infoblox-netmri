from ..broker import Broker


class VrrpRouterStatBroker(Broker):
    controller = "vrrp_router_stats"

    def show(self, **kwargs):
        """Shows the details for the specified vrrp router stat.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrrp router stat methods. The listed methods will be called on each vrrp router stat returned and included in the output. Available methods are: device.
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

             :return vrrp_router_stat: The vrrp router stat identified by the specified VrrpRouterStatsID.
             :rtype vrrp_router_stat: VrrpRouterStat

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available vrrp router stats. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the vrrp router stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the vrrp router stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrrp router stat methods. The listed methods will be called on each vrrp router stat returned and included in the output. Available methods are: device.
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
            |  ``default:`` VrrpRouterStatsID

             :param sort: The data field(s) to use for sorting the output. Default is VrrpRouterStatsID. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors.
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

             :param select: The list of attributes to return for each VrrpRouterStat. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors. If empty or omitted, all attributes will be returned.
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

             :return vrrp_router_stats: An array of the VrrpRouterStat objects that match the specified input criteria.
             :rtype vrrp_router_stats: Array of VrrpRouterStat

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available vrrp router stats matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this Vrrp Router Statistics table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this Vrrp Router Statistics table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier of Iprg member in the vrrp router statistics.
             :type IprgMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier of Iprg member in the vrrp router statistics.
             :type IprgMemberID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The unique IprgNumber in the Vrrp router.
             :type IprgNumber: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The unique IprgNumber in the Vrrp router.
             :type IprgNumber: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAddressListErrors: The number of address list errors in the Vrrp router statistic
             :type VrrpAddressListErrors: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAddressListErrors: The number of address list errors in the Vrrp router statistic
             :type VrrpAddressListErrors: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAdvertiseIntervalErrors: The total number of interval errors in the Vrrp Router Statistics.
             :type VrrpAdvertiseIntervalErrors: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAdvertiseIntervalErrors: The total number of interval errors in the Vrrp Router Statistics.
             :type VrrpAdvertiseIntervalErrors: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAdvertiseRcvd: The received advertise of the Vrrp router statistics.
             :type VrrpAdvertiseRcvd: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAdvertiseRcvd: The received advertise of the Vrrp router statistics.
             :type VrrpAdvertiseRcvd: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAuthFailures: The total number of authentication failures occurred in the Vrrp router statistics.
             :type VrrpAuthFailures: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAuthFailures: The total number of authentication failures occurred in the Vrrp router statistics.
             :type VrrpAuthFailures: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAuthTypeMismatch: The mismatch authentication type.
             :type VrrpAuthTypeMismatch: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpAuthTypeMismatch: The mismatch authentication type.
             :type VrrpAuthTypeMismatch: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpBecomeMaster: The master of the Vrrp Router Statistics.
             :type VrrpBecomeMaster: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpBecomeMaster: The master of the Vrrp Router Statistics.
             :type VrrpBecomeMaster: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpInvalidAuthType: The Invalid Authentication type of Vrrp Router Statistics.
             :type VrrpInvalidAuthType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpInvalidAuthType: The Invalid Authentication type of Vrrp Router Statistics.
             :type VrrpInvalidAuthType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpInvalidTypePktsRcvd: The packet received with Invalid Type.
             :type VrrpInvalidTypePktsRcvd: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpInvalidTypePktsRcvd: The packet received with Invalid Type.
             :type VrrpInvalidTypePktsRcvd: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpIpTtlErrors: The total number of IP address error occurred in the Vrrp Router Statistics.
             :type VrrpIpTtlErrors: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpIpTtlErrors: The total number of IP address error occurred in the Vrrp Router Statistics.
             :type VrrpIpTtlErrors: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPacketLengthErrors: The number of packet length errors in the Vrrp Router Statistics.
             :type VrrpPacketLengthErrors: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPacketLengthErrors: The number of packet length errors in the Vrrp Router Statistics.
             :type VrrpPacketLengthErrors: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPriorityZeroPktsRcvd: The packet received with priority zero.
             :type VrrpPriorityZeroPktsRcvd: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPriorityZeroPktsRcvd: The packet received with priority zero.
             :type VrrpPriorityZeroPktsRcvd: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPriorityZeroPktsSent: The packet sent with priority zero.
             :type VrrpPriorityZeroPktsSent: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpPriorityZeroPktsSent: The packet sent with priority zero.
             :type VrrpPriorityZeroPktsSent: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this Vrrp router statistics table entry.
             :type ifIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index for the local interface for this Vrrp router statistics table entry.
             :type ifIndex: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the vrrp router stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the vrrp router stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrrp router stat methods. The listed methods will be called on each vrrp router stat returned and included in the output. Available methods are: device.
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
            |  ``default:`` VrrpRouterStatsID

             :param sort: The data field(s) to use for sorting the output. Default is VrrpRouterStatsID. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors.
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

             :param select: The list of attributes to return for each VrrpRouterStat. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against vrrp router stats, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DeviceID, EndTime, InterfaceID, IprgMemberID, IprgNumber, StartTime, VrrpAddressListErrors, VrrpAdvertiseIntervalErrors, VrrpAdvertiseRcvd, VrrpAuthFailures, VrrpAuthTypeMismatch, VrrpBecomeMaster, VrrpInvalidAuthType, VrrpInvalidTypePktsRcvd, VrrpIpTtlErrors, VrrpPacketLengthErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpRouterStatsID, ifIndex.
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

             :return vrrp_router_stats: An array of the VrrpRouterStat objects that match the specified input criteria.
             :rtype vrrp_router_stats: Array of VrrpRouterStat

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available vrrp router stats matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DeviceID, EndTime, InterfaceID, IprgMemberID, IprgNumber, StartTime, VrrpAddressListErrors, VrrpAdvertiseIntervalErrors, VrrpAdvertiseRcvd, VrrpAuthFailures, VrrpAuthTypeMismatch, VrrpBecomeMaster, VrrpInvalidAuthType, VrrpInvalidTypePktsRcvd, VrrpIpTtlErrors, VrrpPacketLengthErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpRouterStatsID, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_EndTime: The operator to apply to the field EndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndTime: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndTime: If op_EndTime is specified, the field named in this input will be compared to the value in EndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndTime must be specified if op_EndTime is specified.
             :type val_f_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndTime: If op_EndTime is specified, this value will be compared to the value in EndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndTime must be specified if op_EndTime is specified.
             :type val_c_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the local interface for this Vrrp Router Statistics table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberID: The operator to apply to the field IprgMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberID: The internal NetMRI identifier of Iprg member in the vrrp router statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberID: If op_IprgMemberID is specified, the field named in this input will be compared to the value in IprgMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberID must be specified if op_IprgMemberID is specified.
             :type val_f_IprgMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberID: If op_IprgMemberID is specified, this value will be compared to the value in IprgMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberID must be specified if op_IprgMemberID is specified.
             :type val_c_IprgMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgNumber: The operator to apply to the field IprgNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgNumber: The unique IprgNumber in the Vrrp router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgNumber: If op_IprgNumber is specified, the field named in this input will be compared to the value in IprgNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgNumber must be specified if op_IprgNumber is specified.
             :type val_f_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgNumber: If op_IprgNumber is specified, this value will be compared to the value in IprgNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgNumber must be specified if op_IprgNumber is specified.
             :type val_c_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpAddressListErrors: The operator to apply to the field VrrpAddressListErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpAddressListErrors: The number of address list errors in the Vrrp router statistic For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpAddressListErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpAddressListErrors: If op_VrrpAddressListErrors is specified, the field named in this input will be compared to the value in VrrpAddressListErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpAddressListErrors must be specified if op_VrrpAddressListErrors is specified.
             :type val_f_VrrpAddressListErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpAddressListErrors: If op_VrrpAddressListErrors is specified, this value will be compared to the value in VrrpAddressListErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpAddressListErrors must be specified if op_VrrpAddressListErrors is specified.
             :type val_c_VrrpAddressListErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpAdvertiseIntervalErrors: The operator to apply to the field VrrpAdvertiseIntervalErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpAdvertiseIntervalErrors: The total number of interval errors in the Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpAdvertiseIntervalErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpAdvertiseIntervalErrors: If op_VrrpAdvertiseIntervalErrors is specified, the field named in this input will be compared to the value in VrrpAdvertiseIntervalErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpAdvertiseIntervalErrors must be specified if op_VrrpAdvertiseIntervalErrors is specified.
             :type val_f_VrrpAdvertiseIntervalErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpAdvertiseIntervalErrors: If op_VrrpAdvertiseIntervalErrors is specified, this value will be compared to the value in VrrpAdvertiseIntervalErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpAdvertiseIntervalErrors must be specified if op_VrrpAdvertiseIntervalErrors is specified.
             :type val_c_VrrpAdvertiseIntervalErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpAdvertiseRcvd: The operator to apply to the field VrrpAdvertiseRcvd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpAdvertiseRcvd: The received advertise of the Vrrp router statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpAdvertiseRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpAdvertiseRcvd: If op_VrrpAdvertiseRcvd is specified, the field named in this input will be compared to the value in VrrpAdvertiseRcvd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpAdvertiseRcvd must be specified if op_VrrpAdvertiseRcvd is specified.
             :type val_f_VrrpAdvertiseRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpAdvertiseRcvd: If op_VrrpAdvertiseRcvd is specified, this value will be compared to the value in VrrpAdvertiseRcvd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpAdvertiseRcvd must be specified if op_VrrpAdvertiseRcvd is specified.
             :type val_c_VrrpAdvertiseRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpAuthFailures: The operator to apply to the field VrrpAuthFailures. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpAuthFailures: The total number of authentication failures occurred in the Vrrp router statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpAuthFailures: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpAuthFailures: If op_VrrpAuthFailures is specified, the field named in this input will be compared to the value in VrrpAuthFailures using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpAuthFailures must be specified if op_VrrpAuthFailures is specified.
             :type val_f_VrrpAuthFailures: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpAuthFailures: If op_VrrpAuthFailures is specified, this value will be compared to the value in VrrpAuthFailures using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpAuthFailures must be specified if op_VrrpAuthFailures is specified.
             :type val_c_VrrpAuthFailures: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpAuthTypeMismatch: The operator to apply to the field VrrpAuthTypeMismatch. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpAuthTypeMismatch: The mismatch authentication type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpAuthTypeMismatch: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpAuthTypeMismatch: If op_VrrpAuthTypeMismatch is specified, the field named in this input will be compared to the value in VrrpAuthTypeMismatch using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpAuthTypeMismatch must be specified if op_VrrpAuthTypeMismatch is specified.
             :type val_f_VrrpAuthTypeMismatch: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpAuthTypeMismatch: If op_VrrpAuthTypeMismatch is specified, this value will be compared to the value in VrrpAuthTypeMismatch using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpAuthTypeMismatch must be specified if op_VrrpAuthTypeMismatch is specified.
             :type val_c_VrrpAuthTypeMismatch: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpBecomeMaster: The operator to apply to the field VrrpBecomeMaster. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpBecomeMaster: The master of the Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpBecomeMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpBecomeMaster: If op_VrrpBecomeMaster is specified, the field named in this input will be compared to the value in VrrpBecomeMaster using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpBecomeMaster must be specified if op_VrrpBecomeMaster is specified.
             :type val_f_VrrpBecomeMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpBecomeMaster: If op_VrrpBecomeMaster is specified, this value will be compared to the value in VrrpBecomeMaster using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpBecomeMaster must be specified if op_VrrpBecomeMaster is specified.
             :type val_c_VrrpBecomeMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpInvalidAuthType: The operator to apply to the field VrrpInvalidAuthType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpInvalidAuthType: The Invalid Authentication type of Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpInvalidAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpInvalidAuthType: If op_VrrpInvalidAuthType is specified, the field named in this input will be compared to the value in VrrpInvalidAuthType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpInvalidAuthType must be specified if op_VrrpInvalidAuthType is specified.
             :type val_f_VrrpInvalidAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpInvalidAuthType: If op_VrrpInvalidAuthType is specified, this value will be compared to the value in VrrpInvalidAuthType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpInvalidAuthType must be specified if op_VrrpInvalidAuthType is specified.
             :type val_c_VrrpInvalidAuthType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpInvalidTypePktsRcvd: The operator to apply to the field VrrpInvalidTypePktsRcvd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpInvalidTypePktsRcvd: The packet received with Invalid Type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpInvalidTypePktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpInvalidTypePktsRcvd: If op_VrrpInvalidTypePktsRcvd is specified, the field named in this input will be compared to the value in VrrpInvalidTypePktsRcvd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpInvalidTypePktsRcvd must be specified if op_VrrpInvalidTypePktsRcvd is specified.
             :type val_f_VrrpInvalidTypePktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpInvalidTypePktsRcvd: If op_VrrpInvalidTypePktsRcvd is specified, this value will be compared to the value in VrrpInvalidTypePktsRcvd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpInvalidTypePktsRcvd must be specified if op_VrrpInvalidTypePktsRcvd is specified.
             :type val_c_VrrpInvalidTypePktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpIpTtlErrors: The operator to apply to the field VrrpIpTtlErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpIpTtlErrors: The total number of IP address error occurred in the Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpIpTtlErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpIpTtlErrors: If op_VrrpIpTtlErrors is specified, the field named in this input will be compared to the value in VrrpIpTtlErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpIpTtlErrors must be specified if op_VrrpIpTtlErrors is specified.
             :type val_f_VrrpIpTtlErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpIpTtlErrors: If op_VrrpIpTtlErrors is specified, this value will be compared to the value in VrrpIpTtlErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpIpTtlErrors must be specified if op_VrrpIpTtlErrors is specified.
             :type val_c_VrrpIpTtlErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpPacketLengthErrors: The operator to apply to the field VrrpPacketLengthErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpPacketLengthErrors: The number of packet length errors in the Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpPacketLengthErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpPacketLengthErrors: If op_VrrpPacketLengthErrors is specified, the field named in this input will be compared to the value in VrrpPacketLengthErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpPacketLengthErrors must be specified if op_VrrpPacketLengthErrors is specified.
             :type val_f_VrrpPacketLengthErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpPacketLengthErrors: If op_VrrpPacketLengthErrors is specified, this value will be compared to the value in VrrpPacketLengthErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpPacketLengthErrors must be specified if op_VrrpPacketLengthErrors is specified.
             :type val_c_VrrpPacketLengthErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpPriorityZeroPktsRcvd: The operator to apply to the field VrrpPriorityZeroPktsRcvd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpPriorityZeroPktsRcvd: The packet received with priority zero. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpPriorityZeroPktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpPriorityZeroPktsRcvd: If op_VrrpPriorityZeroPktsRcvd is specified, the field named in this input will be compared to the value in VrrpPriorityZeroPktsRcvd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpPriorityZeroPktsRcvd must be specified if op_VrrpPriorityZeroPktsRcvd is specified.
             :type val_f_VrrpPriorityZeroPktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpPriorityZeroPktsRcvd: If op_VrrpPriorityZeroPktsRcvd is specified, this value will be compared to the value in VrrpPriorityZeroPktsRcvd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpPriorityZeroPktsRcvd must be specified if op_VrrpPriorityZeroPktsRcvd is specified.
             :type val_c_VrrpPriorityZeroPktsRcvd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpPriorityZeroPktsSent: The operator to apply to the field VrrpPriorityZeroPktsSent. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpPriorityZeroPktsSent: The packet sent with priority zero. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpPriorityZeroPktsSent: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpPriorityZeroPktsSent: If op_VrrpPriorityZeroPktsSent is specified, the field named in this input will be compared to the value in VrrpPriorityZeroPktsSent using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpPriorityZeroPktsSent must be specified if op_VrrpPriorityZeroPktsSent is specified.
             :type val_f_VrrpPriorityZeroPktsSent: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpPriorityZeroPktsSent: If op_VrrpPriorityZeroPktsSent is specified, this value will be compared to the value in VrrpPriorityZeroPktsSent using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpPriorityZeroPktsSent must be specified if op_VrrpPriorityZeroPktsSent is specified.
             :type val_c_VrrpPriorityZeroPktsSent: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrrpRouterStatsID: The operator to apply to the field VrrpRouterStatsID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrrpRouterStatsID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrrpRouterStatsID: If op_VrrpRouterStatsID is specified, the field named in this input will be compared to the value in VrrpRouterStatsID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrrpRouterStatsID must be specified if op_VrrpRouterStatsID is specified.
             :type val_f_VrrpRouterStatsID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrrpRouterStatsID: If op_VrrpRouterStatsID is specified, this value will be compared to the value in VrrpRouterStatsID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrrpRouterStatsID must be specified if op_VrrpRouterStatsID is specified.
             :type val_c_VrrpRouterStatsID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index for the local interface for this Vrrp router statistics table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the vrrp router stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the vrrp router stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vrrp router stat methods. The listed methods will be called on each vrrp router stat returned and included in the output. Available methods are: device.
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
            |  ``default:`` VrrpRouterStatsID

             :param sort: The data field(s) to use for sorting the output. Default is VrrpRouterStatsID. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors.
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

             :param select: The list of attributes to return for each VrrpRouterStat. Valid values are VrrpRouterStatsID, DeviceID, IprgMemberID, InterfaceID, StartTime, EndTime, ifIndex, IprgNumber, VrrpBecomeMaster, VrrpAdvertiseRcvd, VrrpAdvertiseIntervalErrors, VrrpAuthFailures, VrrpIpTtlErrors, VrrpPriorityZeroPktsRcvd, VrrpPriorityZeroPktsSent, VrrpInvalidTypePktsRcvd, VrrpAddressListErrors, VrrpInvalidAuthType, VrrpAuthTypeMismatch, VrrpPacketLengthErrors. If empty or omitted, all attributes will be returned.
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

             :return vrrp_router_stats: An array of the VrrpRouterStat objects that match the specified input criteria.
             :rtype vrrp_router_stats: Array of VrrpRouterStat

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Integer

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

             :param VrrpRouterStatsID: The internal NetMRI identifier of the Vrrp Router Statistics.
             :type VrrpRouterStatsID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
