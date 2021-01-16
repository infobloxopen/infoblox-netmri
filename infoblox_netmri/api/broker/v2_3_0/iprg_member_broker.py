from ..broker import Broker


class IprgMemberBroker(Broker):
    controller = "iprg_members"

    def show(self, **kwargs):
        """Shows the details for the specified iprg member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg member methods. The listed methods will be called on each iprg member returned and included in the output. Available methods are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return iprg_member: The iprg member identified by the specified IprgMemberID.
             :rtype iprg_member: IprgMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available iprg members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device configured with this HSRP/VRRP membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device configured with this HSRP/VRRP membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains.
             :type IprgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains.
             :type IprgID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the iprg members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg member methods. The listed methods will be called on each iprg member returned and included in the output. Available methods are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg.
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
            |  ``default:`` IprgMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IprgMemberID. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState.
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

             :param select: The list of attributes to return for each IprgMember. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState. If empty or omitted, all attributes will be returned.
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

             :return iprg_members: An array of the IprgMember objects that match the specified input criteria.
             :rtype iprg_members: Array of IprgMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available iprg members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device configured with this HSRP/VRRP membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device configured with this HSRP/VRRP membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains.
             :type IprgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains.
             :type IprgID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveDeviceID: The internal NetMRI identifier of the device that this router believes is the current active/master router.
             :type IprgMemberActiveDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveDeviceID: The internal NetMRI identifier of the device that this router believes is the current active/master router.
             :type IprgMemberActiveDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveIPDotted: The IP address for the active or master router, according to this device, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberActiveIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveIPDotted: The IP address for the active or master router, according to this device, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberActiveIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveIPNumeric: The numerical IP address for the active or master router, according to this device.
             :type IprgMemberActiveIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveIPNumeric: The numerical IP address for the active or master router, according to this device.
             :type IprgMemberActiveIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveInterfaceID: The internal NetMRI identifier of the interface corresponding to the active/master IP address, if available.
             :type IprgMemberActiveInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberActiveInterfaceID: The internal NetMRI identifier of the interface corresponding to the active/master IP address, if available.
             :type IprgMemberActiveInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IprgMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IprgMemberChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberConfiguredHelloTime: The configured hello or advertise interval.
             :type IprgMemberConfiguredHelloTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberConfiguredHelloTime: The configured hello or advertise interval.
             :type IprgMemberConfiguredHelloTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberConfiguredHoldTime: The configured hold time or master down interval.
             :type IprgMemberConfiguredHoldTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberConfiguredHoldTime: The configured hold time or master down interval.
             :type IprgMemberConfiguredHoldTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IprgMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IprgMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberLearnedHelloTime: The learned hello or advertise interval.
             :type IprgMemberLearnedHelloTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberLearnedHelloTime: The learned hello or advertise interval.
             :type IprgMemberLearnedHelloTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberLearnedHoldTime: The learned hold time or master down interval.
             :type IprgMemberLearnedHoldTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberLearnedHoldTime: The learned hold time or master down interval.
             :type IprgMemberLearnedHoldTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPreemptDelay: The number of seconds after booting that preemption is enabled. This prevents a router with an unpopulated routing table from preempting until the routing table is ready.
             :type IprgMemberPreemptDelay: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPreemptDelay: The number of seconds after booting that preemption is enabled. This prevents a router with an unpopulated routing table from preempting until the routing table is ready.
             :type IprgMemberPreemptDelay: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPreemptInd: A flag indicating whether this router is configured to preempt lower priority routers.
             :type IprgMemberPreemptInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPreemptInd: A flag indicating whether this router is configured to preempt lower priority routers.
             :type IprgMemberPreemptInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPriority: The router's priority in this HSRP or VRRP.
             :type IprgMemberPriority: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberPriority: The router's priority in this HSRP or VRRP.
             :type IprgMemberPriority: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyDeviceID: The internal NetMRI identifier of the device that this router believes is the current standby/backup router.
             :type IprgMemberStandbyDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyDeviceID: The internal NetMRI identifier of the device that this router believes is the current standby/backup router.
             :type IprgMemberStandbyDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyIPDotted: The IP address for the standby or backup router, according to this device, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberStandbyIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyIPDotted: The IP address for the standby or backup router, according to this device, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberStandbyIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyIPNumeric: The numerical IP address for the standby or backup router, according to this device.
             :type IprgMemberStandbyIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyIPNumeric: The numerical IP address for the standby or backup router, according to this device.
             :type IprgMemberStandbyIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyInterfaceID: The internal NetMRI identifier of the interface corresponding to the standby/backup IP address, if available.
             :type IprgMemberStandbyInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStandbyInterfaceID: The internal NetMRI identifier of the interface corresponding to the standby/backup IP address, if available.
             :type IprgMemberStandbyInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStartTime: The starting effective time of this revision of the record.
             :type IprgMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberStartTime: The starting effective time of this revision of the record.
             :type IprgMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberState: The current HSRP or VRRP state of this router for this HSRP/VRRP group.
             :type IprgMemberState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberState: The current HSRP or VRRP state of this router for this HSRP/VRRP group.
             :type IprgMemberState: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberTimestamp: The date and time this record was collected or calculated.
             :type IprgMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberTimestamp: The date and time this record was collected or calculated.
             :type IprgMemberTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberUseConfigVirtualIPInd: A flag indicating whether to use the configured or learned virtual IP value.
             :type IprgMemberUseConfigVirtualIPInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberUseConfigVirtualIPInd: A flag indicating whether to use the configured or learned virtual IP value.
             :type IprgMemberUseConfigVirtualIPInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberUseConfiguredTimersInd: A flag indicating whether to use the configured or learned timer values.
             :type IprgMemberUseConfiguredTimersInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberUseConfiguredTimersInd: A flag indicating whether to use the configured or learned timer values.
             :type IprgMemberUseConfiguredTimersInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberVirtualIPDotted: The virtual IP address for the associated HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberVirtualIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberVirtualIPDotted: The virtual IP address for the associated HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
             :type IprgMemberVirtualIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberVirtualIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgMemberVirtualIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMemberVirtualIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgMemberVirtualIPNumeric: Array of Integer

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

             :param timestamp: The data returned will represent the iprg members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg member methods. The listed methods will be called on each iprg member returned and included in the output. Available methods are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg.
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
            |  ``default:`` IprgMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IprgMemberID. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState.
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

             :param select: The list of attributes to return for each IprgMember. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against iprg members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, InterfaceID, IprgID, IprgMemberActiveDeviceID, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveInterfaceID, IprgMemberChangedCols, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberEndTime, IprgMemberID, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberPreemptDelay, IprgMemberPreemptInd, IprgMemberPriority, IprgMemberStandbyDeviceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyInterfaceID, IprgMemberStartTime, IprgMemberState, IprgMemberTimestamp, IprgMemberUseConfigVirtualIPInd, IprgMemberUseConfiguredTimersInd, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric.
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

             :return iprg_members: An array of the IprgMember objects that match the specified input criteria.
             :rtype iprg_members: Array of IprgMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available iprg members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, InterfaceID, IprgID, IprgMemberActiveDeviceID, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveInterfaceID, IprgMemberChangedCols, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberEndTime, IprgMemberID, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberPreemptDelay, IprgMemberPreemptInd, IprgMemberPriority, IprgMemberStandbyDeviceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyInterfaceID, IprgMemberStartTime, IprgMemberState, IprgMemberTimestamp, IprgMemberUseConfigVirtualIPInd, IprgMemberUseConfiguredTimersInd, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of the device configured with this HSRP/VRRP membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IprgID: The operator to apply to the field IprgID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgID: The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgID: If op_IprgID is specified, the field named in this input will be compared to the value in IprgID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgID must be specified if op_IprgID is specified.
             :type val_f_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgID: If op_IprgID is specified, this value will be compared to the value in IprgID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgID must be specified if op_IprgID is specified.
             :type val_c_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberActiveDeviceID: The operator to apply to the field IprgMemberActiveDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberActiveDeviceID: The internal NetMRI identifier of the device that this router believes is the current active/master router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberActiveDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberActiveDeviceID: If op_IprgMemberActiveDeviceID is specified, the field named in this input will be compared to the value in IprgMemberActiveDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberActiveDeviceID must be specified if op_IprgMemberActiveDeviceID is specified.
             :type val_f_IprgMemberActiveDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberActiveDeviceID: If op_IprgMemberActiveDeviceID is specified, this value will be compared to the value in IprgMemberActiveDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberActiveDeviceID must be specified if op_IprgMemberActiveDeviceID is specified.
             :type val_c_IprgMemberActiveDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberActiveIPDotted: The operator to apply to the field IprgMemberActiveIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberActiveIPDotted: The IP address for the active or master router, according to this device, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberActiveIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberActiveIPDotted: If op_IprgMemberActiveIPDotted is specified, the field named in this input will be compared to the value in IprgMemberActiveIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberActiveIPDotted must be specified if op_IprgMemberActiveIPDotted is specified.
             :type val_f_IprgMemberActiveIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberActiveIPDotted: If op_IprgMemberActiveIPDotted is specified, this value will be compared to the value in IprgMemberActiveIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberActiveIPDotted must be specified if op_IprgMemberActiveIPDotted is specified.
             :type val_c_IprgMemberActiveIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberActiveIPNumeric: The operator to apply to the field IprgMemberActiveIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberActiveIPNumeric: The numerical IP address for the active or master router, according to this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberActiveIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberActiveIPNumeric: If op_IprgMemberActiveIPNumeric is specified, the field named in this input will be compared to the value in IprgMemberActiveIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberActiveIPNumeric must be specified if op_IprgMemberActiveIPNumeric is specified.
             :type val_f_IprgMemberActiveIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberActiveIPNumeric: If op_IprgMemberActiveIPNumeric is specified, this value will be compared to the value in IprgMemberActiveIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberActiveIPNumeric must be specified if op_IprgMemberActiveIPNumeric is specified.
             :type val_c_IprgMemberActiveIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberActiveInterfaceID: The operator to apply to the field IprgMemberActiveInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberActiveInterfaceID: The internal NetMRI identifier of the interface corresponding to the active/master IP address, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberActiveInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberActiveInterfaceID: If op_IprgMemberActiveInterfaceID is specified, the field named in this input will be compared to the value in IprgMemberActiveInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberActiveInterfaceID must be specified if op_IprgMemberActiveInterfaceID is specified.
             :type val_f_IprgMemberActiveInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberActiveInterfaceID: If op_IprgMemberActiveInterfaceID is specified, this value will be compared to the value in IprgMemberActiveInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberActiveInterfaceID must be specified if op_IprgMemberActiveInterfaceID is specified.
             :type val_c_IprgMemberActiveInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberChangedCols: The operator to apply to the field IprgMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberChangedCols: If op_IprgMemberChangedCols is specified, the field named in this input will be compared to the value in IprgMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberChangedCols must be specified if op_IprgMemberChangedCols is specified.
             :type val_f_IprgMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberChangedCols: If op_IprgMemberChangedCols is specified, this value will be compared to the value in IprgMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberChangedCols must be specified if op_IprgMemberChangedCols is specified.
             :type val_c_IprgMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberConfiguredHelloTime: The operator to apply to the field IprgMemberConfiguredHelloTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberConfiguredHelloTime: The configured hello or advertise interval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberConfiguredHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberConfiguredHelloTime: If op_IprgMemberConfiguredHelloTime is specified, the field named in this input will be compared to the value in IprgMemberConfiguredHelloTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberConfiguredHelloTime must be specified if op_IprgMemberConfiguredHelloTime is specified.
             :type val_f_IprgMemberConfiguredHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberConfiguredHelloTime: If op_IprgMemberConfiguredHelloTime is specified, this value will be compared to the value in IprgMemberConfiguredHelloTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberConfiguredHelloTime must be specified if op_IprgMemberConfiguredHelloTime is specified.
             :type val_c_IprgMemberConfiguredHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberConfiguredHoldTime: The operator to apply to the field IprgMemberConfiguredHoldTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberConfiguredHoldTime: The configured hold time or master down interval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberConfiguredHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberConfiguredHoldTime: If op_IprgMemberConfiguredHoldTime is specified, the field named in this input will be compared to the value in IprgMemberConfiguredHoldTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberConfiguredHoldTime must be specified if op_IprgMemberConfiguredHoldTime is specified.
             :type val_f_IprgMemberConfiguredHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberConfiguredHoldTime: If op_IprgMemberConfiguredHoldTime is specified, this value will be compared to the value in IprgMemberConfiguredHoldTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberConfiguredHoldTime must be specified if op_IprgMemberConfiguredHoldTime is specified.
             :type val_c_IprgMemberConfiguredHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberEndTime: The operator to apply to the field IprgMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberEndTime: If op_IprgMemberEndTime is specified, the field named in this input will be compared to the value in IprgMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberEndTime must be specified if op_IprgMemberEndTime is specified.
             :type val_f_IprgMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberEndTime: If op_IprgMemberEndTime is specified, this value will be compared to the value in IprgMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberEndTime must be specified if op_IprgMemberEndTime is specified.
             :type val_c_IprgMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberID: The operator to apply to the field IprgMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IprgMemberLearnedHelloTime: The operator to apply to the field IprgMemberLearnedHelloTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberLearnedHelloTime: The learned hello or advertise interval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberLearnedHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberLearnedHelloTime: If op_IprgMemberLearnedHelloTime is specified, the field named in this input will be compared to the value in IprgMemberLearnedHelloTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberLearnedHelloTime must be specified if op_IprgMemberLearnedHelloTime is specified.
             :type val_f_IprgMemberLearnedHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberLearnedHelloTime: If op_IprgMemberLearnedHelloTime is specified, this value will be compared to the value in IprgMemberLearnedHelloTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberLearnedHelloTime must be specified if op_IprgMemberLearnedHelloTime is specified.
             :type val_c_IprgMemberLearnedHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberLearnedHoldTime: The operator to apply to the field IprgMemberLearnedHoldTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberLearnedHoldTime: The learned hold time or master down interval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberLearnedHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberLearnedHoldTime: If op_IprgMemberLearnedHoldTime is specified, the field named in this input will be compared to the value in IprgMemberLearnedHoldTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberLearnedHoldTime must be specified if op_IprgMemberLearnedHoldTime is specified.
             :type val_f_IprgMemberLearnedHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberLearnedHoldTime: If op_IprgMemberLearnedHoldTime is specified, this value will be compared to the value in IprgMemberLearnedHoldTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberLearnedHoldTime must be specified if op_IprgMemberLearnedHoldTime is specified.
             :type val_c_IprgMemberLearnedHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberPreemptDelay: The operator to apply to the field IprgMemberPreemptDelay. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberPreemptDelay: The number of seconds after booting that preemption is enabled. This prevents a router with an unpopulated routing table from preempting until the routing table is ready. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberPreemptDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberPreemptDelay: If op_IprgMemberPreemptDelay is specified, the field named in this input will be compared to the value in IprgMemberPreemptDelay using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberPreemptDelay must be specified if op_IprgMemberPreemptDelay is specified.
             :type val_f_IprgMemberPreemptDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberPreemptDelay: If op_IprgMemberPreemptDelay is specified, this value will be compared to the value in IprgMemberPreemptDelay using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberPreemptDelay must be specified if op_IprgMemberPreemptDelay is specified.
             :type val_c_IprgMemberPreemptDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberPreemptInd: The operator to apply to the field IprgMemberPreemptInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberPreemptInd: A flag indicating whether this router is configured to preempt lower priority routers. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberPreemptInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberPreemptInd: If op_IprgMemberPreemptInd is specified, the field named in this input will be compared to the value in IprgMemberPreemptInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberPreemptInd must be specified if op_IprgMemberPreemptInd is specified.
             :type val_f_IprgMemberPreemptInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberPreemptInd: If op_IprgMemberPreemptInd is specified, this value will be compared to the value in IprgMemberPreemptInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberPreemptInd must be specified if op_IprgMemberPreemptInd is specified.
             :type val_c_IprgMemberPreemptInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberPriority: The operator to apply to the field IprgMemberPriority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberPriority: The router's priority in this HSRP or VRRP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberPriority: If op_IprgMemberPriority is specified, the field named in this input will be compared to the value in IprgMemberPriority using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberPriority must be specified if op_IprgMemberPriority is specified.
             :type val_f_IprgMemberPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberPriority: If op_IprgMemberPriority is specified, this value will be compared to the value in IprgMemberPriority using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberPriority must be specified if op_IprgMemberPriority is specified.
             :type val_c_IprgMemberPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberStandbyDeviceID: The operator to apply to the field IprgMemberStandbyDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberStandbyDeviceID: The internal NetMRI identifier of the device that this router believes is the current standby/backup router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberStandbyDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberStandbyDeviceID: If op_IprgMemberStandbyDeviceID is specified, the field named in this input will be compared to the value in IprgMemberStandbyDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberStandbyDeviceID must be specified if op_IprgMemberStandbyDeviceID is specified.
             :type val_f_IprgMemberStandbyDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberStandbyDeviceID: If op_IprgMemberStandbyDeviceID is specified, this value will be compared to the value in IprgMemberStandbyDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberStandbyDeviceID must be specified if op_IprgMemberStandbyDeviceID is specified.
             :type val_c_IprgMemberStandbyDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberStandbyIPDotted: The operator to apply to the field IprgMemberStandbyIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberStandbyIPDotted: The IP address for the standby or backup router, according to this device, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberStandbyIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberStandbyIPDotted: If op_IprgMemberStandbyIPDotted is specified, the field named in this input will be compared to the value in IprgMemberStandbyIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberStandbyIPDotted must be specified if op_IprgMemberStandbyIPDotted is specified.
             :type val_f_IprgMemberStandbyIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberStandbyIPDotted: If op_IprgMemberStandbyIPDotted is specified, this value will be compared to the value in IprgMemberStandbyIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberStandbyIPDotted must be specified if op_IprgMemberStandbyIPDotted is specified.
             :type val_c_IprgMemberStandbyIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberStandbyIPNumeric: The operator to apply to the field IprgMemberStandbyIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberStandbyIPNumeric: The numerical IP address for the standby or backup router, according to this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberStandbyIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberStandbyIPNumeric: If op_IprgMemberStandbyIPNumeric is specified, the field named in this input will be compared to the value in IprgMemberStandbyIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberStandbyIPNumeric must be specified if op_IprgMemberStandbyIPNumeric is specified.
             :type val_f_IprgMemberStandbyIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberStandbyIPNumeric: If op_IprgMemberStandbyIPNumeric is specified, this value will be compared to the value in IprgMemberStandbyIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberStandbyIPNumeric must be specified if op_IprgMemberStandbyIPNumeric is specified.
             :type val_c_IprgMemberStandbyIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberStandbyInterfaceID: The operator to apply to the field IprgMemberStandbyInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberStandbyInterfaceID: The internal NetMRI identifier of the interface corresponding to the standby/backup IP address, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberStandbyInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberStandbyInterfaceID: If op_IprgMemberStandbyInterfaceID is specified, the field named in this input will be compared to the value in IprgMemberStandbyInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberStandbyInterfaceID must be specified if op_IprgMemberStandbyInterfaceID is specified.
             :type val_f_IprgMemberStandbyInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberStandbyInterfaceID: If op_IprgMemberStandbyInterfaceID is specified, this value will be compared to the value in IprgMemberStandbyInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberStandbyInterfaceID must be specified if op_IprgMemberStandbyInterfaceID is specified.
             :type val_c_IprgMemberStandbyInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberStartTime: The operator to apply to the field IprgMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberStartTime: If op_IprgMemberStartTime is specified, the field named in this input will be compared to the value in IprgMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberStartTime must be specified if op_IprgMemberStartTime is specified.
             :type val_f_IprgMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberStartTime: If op_IprgMemberStartTime is specified, this value will be compared to the value in IprgMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberStartTime must be specified if op_IprgMemberStartTime is specified.
             :type val_c_IprgMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberState: The operator to apply to the field IprgMemberState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberState: The current HSRP or VRRP state of this router for this HSRP/VRRP group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberState: If op_IprgMemberState is specified, the field named in this input will be compared to the value in IprgMemberState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberState must be specified if op_IprgMemberState is specified.
             :type val_f_IprgMemberState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberState: If op_IprgMemberState is specified, this value will be compared to the value in IprgMemberState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberState must be specified if op_IprgMemberState is specified.
             :type val_c_IprgMemberState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberTimestamp: The operator to apply to the field IprgMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberTimestamp: If op_IprgMemberTimestamp is specified, the field named in this input will be compared to the value in IprgMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberTimestamp must be specified if op_IprgMemberTimestamp is specified.
             :type val_f_IprgMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberTimestamp: If op_IprgMemberTimestamp is specified, this value will be compared to the value in IprgMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberTimestamp must be specified if op_IprgMemberTimestamp is specified.
             :type val_c_IprgMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberUseConfigVirtualIPInd: The operator to apply to the field IprgMemberUseConfigVirtualIPInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberUseConfigVirtualIPInd: A flag indicating whether to use the configured or learned virtual IP value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberUseConfigVirtualIPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberUseConfigVirtualIPInd: If op_IprgMemberUseConfigVirtualIPInd is specified, the field named in this input will be compared to the value in IprgMemberUseConfigVirtualIPInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberUseConfigVirtualIPInd must be specified if op_IprgMemberUseConfigVirtualIPInd is specified.
             :type val_f_IprgMemberUseConfigVirtualIPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberUseConfigVirtualIPInd: If op_IprgMemberUseConfigVirtualIPInd is specified, this value will be compared to the value in IprgMemberUseConfigVirtualIPInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberUseConfigVirtualIPInd must be specified if op_IprgMemberUseConfigVirtualIPInd is specified.
             :type val_c_IprgMemberUseConfigVirtualIPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberUseConfiguredTimersInd: The operator to apply to the field IprgMemberUseConfiguredTimersInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberUseConfiguredTimersInd: A flag indicating whether to use the configured or learned timer values. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberUseConfiguredTimersInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberUseConfiguredTimersInd: If op_IprgMemberUseConfiguredTimersInd is specified, the field named in this input will be compared to the value in IprgMemberUseConfiguredTimersInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberUseConfiguredTimersInd must be specified if op_IprgMemberUseConfiguredTimersInd is specified.
             :type val_f_IprgMemberUseConfiguredTimersInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberUseConfiguredTimersInd: If op_IprgMemberUseConfiguredTimersInd is specified, this value will be compared to the value in IprgMemberUseConfiguredTimersInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberUseConfiguredTimersInd must be specified if op_IprgMemberUseConfiguredTimersInd is specified.
             :type val_c_IprgMemberUseConfiguredTimersInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberVirtualIPDotted: The operator to apply to the field IprgMemberVirtualIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberVirtualIPDotted: The virtual IP address for the associated HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberVirtualIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberVirtualIPDotted: If op_IprgMemberVirtualIPDotted is specified, the field named in this input will be compared to the value in IprgMemberVirtualIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberVirtualIPDotted must be specified if op_IprgMemberVirtualIPDotted is specified.
             :type val_f_IprgMemberVirtualIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberVirtualIPDotted: If op_IprgMemberVirtualIPDotted is specified, this value will be compared to the value in IprgMemberVirtualIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberVirtualIPDotted must be specified if op_IprgMemberVirtualIPDotted is specified.
             :type val_c_IprgMemberVirtualIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMemberVirtualIPNumeric: The operator to apply to the field IprgMemberVirtualIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMemberVirtualIPNumeric: The numerical value of the HSRP/VRRP virtual IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMemberVirtualIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMemberVirtualIPNumeric: If op_IprgMemberVirtualIPNumeric is specified, the field named in this input will be compared to the value in IprgMemberVirtualIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMemberVirtualIPNumeric must be specified if op_IprgMemberVirtualIPNumeric is specified.
             :type val_f_IprgMemberVirtualIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMemberVirtualIPNumeric: If op_IprgMemberVirtualIPNumeric is specified, this value will be compared to the value in IprgMemberVirtualIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMemberVirtualIPNumeric must be specified if op_IprgMemberVirtualIPNumeric is specified.
             :type val_c_IprgMemberVirtualIPNumeric: String

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

             :param timestamp: The data returned will represent the iprg members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg member methods. The listed methods will be called on each iprg member returned and included in the output. Available methods are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_interface, active_router, standby_router, standby_interface, data_source, device, interface, iprg.
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
            |  ``default:`` IprgMemberID

             :param sort: The data field(s) to use for sorting the output. Default is IprgMemberID. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState.
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

             :param select: The list of attributes to return for each IprgMember. Valid values are IprgMemberID, IprgMemberStartTime, IprgMemberEndTime, IprgMemberTimestamp, IprgMemberChangedCols, IprgID, InterfaceID, DeviceID, DataSourceID, IprgMemberPriority, IprgMemberPreemptInd, IprgMemberPreemptDelay, IprgMemberUseConfiguredTimersInd, IprgMemberConfiguredHelloTime, IprgMemberConfiguredHoldTime, IprgMemberLearnedHelloTime, IprgMemberLearnedHoldTime, IprgMemberVirtualIPDotted, IprgMemberVirtualIPNumeric, IprgMemberUseConfigVirtualIPInd, IprgMemberActiveIPDotted, IprgMemberActiveIPNumeric, IprgMemberActiveDeviceID, IprgMemberActiveInterfaceID, IprgMemberStandbyIPDotted, IprgMemberStandbyIPNumeric, IprgMemberStandbyDeviceID, IprgMemberStandbyInterfaceID, IprgMemberState. If empty or omitted, all attributes will be returned.
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

             :return iprg_members: An array of the IprgMember objects that match the specified input criteria.
             :rtype iprg_members: Array of IprgMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def iprg(self, **kwargs):
        """The HSRP/VRRP group to which this membership pertains.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The HSRP/VRRP group to which this membership pertains.
             :rtype : Iprg

            """

        return self.api_request(self._get_method_fullname("iprg"), kwargs)

    def interface(self, **kwargs):
        """The interface configured with this HSRP/VRRP membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface configured with this HSRP/VRRP membership.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def active_router(self, **kwargs):
        """The device that this router believes is the current active or master device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device that this router believes is the current active or master device.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("active_router"), kwargs)

    def standby_router(self, **kwargs):
        """The device that this router believes is the current standby or backup device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device that this router believes is the current standby or backup device.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("standby_router"), kwargs)

    def active_interface(self, **kwargs):
        """The interface object corresponding to the active/master IP address, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface object corresponding to the active/master IP address, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("active_interface"), kwargs)

    def standby_interface(self, **kwargs):
        """The interface object corresponding to the  standby/backup IP address, if available.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface object corresponding to the  standby/backup IP address, if available.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("standby_interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device configured with this HSRP/VRRP membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device configured with this HSRP/VRRP membership.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device configured with this HSRP/VRRP membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgMemberID: The internal NetMRI identifier for this HSRP/VRRP membership.
             :type IprgMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device configured with this HSRP/VRRP membership.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
