from ..broker import Broker


class DiscoveryStatusesBroker(Broker):
    controller = "discovery_statuses"

    def check_withdrawal_license(self, **kwargs):
        """Check Management Server and Managed Devices when device unlicensed with SDC license

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: The list of devices to be checked
             :type DeviceIDs: Array

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cascading_impact: Warning message for user
             :rtype cascading_impact: String

            """

        return self.api_request(self._get_method_fullname("check_withdrawal_license"), kwargs)

    def search(self, **kwargs):
        """Searches the current discovery statuses based on view

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` current

             :param view: Defined filters for displaying discovery statuses data. Valid values are "current", "non_reached", "problems". "ok"
             :type view: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkID: The NetworkID maps to one or more collectors that are identified by DataSourceIDs.
             :type NetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceName: The operator to apply to the field DeviceName. DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
             :type op_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceName: If op_DeviceName is specified, this value will be compared to the value in DeviceName using the specified operator. The value in this input will be treated as an explicit constant value. This field must be specified if op_DeviceName is specified.
             :type val_c_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPAddress: The operator to apply to ip address fields like Device.DeviceIPDotted and ifAddr.IfIPDotted. DeviceIPDotted : The management IP address of the device, in dotted (or colon-delimited for IPv6) format. IfIPDotted: The IP address configured on the device in dotted (or colon-delimited for IPv6) format.
             :type op_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddress: If op_IPAddress is specified, this value will be compared to the value in IPAddress using the specified operator. The value in this input will be treated as an explicit constant value. This field must be specified if op_IPAddress is specified.
             :type val_c_IPAddress: String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param management_ip_only_ind: If op_IPAddress is used, by default entire ip addresses is searched. Set the value in this input to true to search only management ip addresses.
             :type management_ip_only_ind: Boolean

            |  ``api version min:`` 3.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of fields to return for each discovery status. Valid values are DeviceID, DeviceIPDotted, VirtualNetworkID, VirtualNetworkName, VirtualNetworkMemberArtificialInd, DeviceIPNumeric, DeviceName, DeviceType, DeviceUniqueKey, Status, StatusDetail, SPMLicensedInd, SAMLicensedInd, LicenseOverride, FirstSeen, DeviceFirstOccurrenceTime, LastSeen, FingerPrintEnabled, SDNCollectionEnabled, SNMPCollectionEnabled, CLICollectionEnabled, ConfigCollectionEnabled, CLICredentialMessage, CLICredentialStatus, CLICredentialTimestamp, GlobalConfigCollectionEnabled, GlobalConfigCollectionMessage, ConfigCollectionMessage, ConfigCollectionStatus, ConfigCollectionStatusSort, ConfigCollectionTimestamp, DeviceGroupMessage, DeviceGroupStatus, DeviceGroupTimestamp, ExistsMessage, ExistsTimestamp, FingerPrintMessage, FingerPrintStatus, FingerPrintTimestamp, SDNCollectionMessage, SDNCollectionStatus, SDNCollectionTimestamp, LastAction, LastTimestamp, ReachableMessage, ReachableStatus, ReachableTimestamp, SNMPCollectionMessage, SNMPCollectionStatus, SNMPCollectionTimestamp, SNMPCredentialMessage, SNMPCredentialStatus, SNMPCredentialTimestamp, RuleListAnalysisMessage, RuleListAnalysisStatus, RuleListAnalysisTimestamp, UnitID, AccessInd, ForwardingInd, StartPortControlBlackoutSchedule, PortControlBlackoutDuration, StartBlackoutSchedule, BlackoutDuration. If empty or omitted, all fields will be returned.
             :type select: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The index of the last row to display. Default value is 25
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param order: The sort order for the output.
             :type order: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit will not be enforced when this filter is used, and paging is not supported.
             :type xml_filter: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("search"), kwargs)

    def static(self, **kwargs):
        """Displays the current discovery statuses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` current

             :param view: Defined filters for displaying discovery statuses data. Valid values are "current", "licensed", "non_reached", "problems", "ok"
             :type view: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The index of the last row to display. Default value is 25
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: Search string
             :type query: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only. Specifying a UnitID will pull the most recent data from a specific collector while not specifying one will pull data directly from the OC.
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return AccessInd: The indicator of collection of the filtering access information
             :rtype AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return BlackoutDuration: The blackout duration in minutes
             :rtype BlackoutDuration: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICollectionEnabled: CLI collection enabled
             :rtype CLICollectionEnabled: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialMessage: A message detailing the current CLI credential status
             :rtype CLICredentialMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialStatus: Indicates the status of SSH discovery attempt of the device
             :rtype CLICredentialStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialTimestamp: The date/time of the last update to the CLI credential status
             :rtype CLICredentialTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionEnabled: Whether configuration polling is enabled for this device
             :rtype ConfigCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionMessage: A message detailing the current configuration file collection status
             :rtype ConfigCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionStatus: Indicates whether configuration files have been successfully collected from the device
             :rtype ConfigCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionStatusSort: Config collection status sorted
             :rtype ConfigCollectionStatusSort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionTimestamp: The date/time of the last update to the configuration collection status
             :rtype ConfigCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network
             :rtype DeviceFirstOccurrenceTime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupMessage: A message detailing the current device group assignment status
             :rtype DeviceGroupMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupStatus: Indicates whether the device has been successfully assigned to a device group
             :rtype DeviceGroupStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupTimestamp: The date/time of the last update to the device group assignment status
             :rtype DeviceGroupTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: Internal system identifier for the discovery status
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format
             :rtype DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPNumeric: The numerical value of the device IP address
             :rtype DeviceIPNumeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceName: The name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your configuration
             :rtype DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The determined device type
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceUniqueKey: Unique key which allows duplicates detecting over different Virtual Networks
             :rtype DeviceUniqueKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ExistsMessage: A message detailing the method by which the device is decided to exist
             :rtype ExistsMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ExistsTimestamp: The date/time of the last device existance update
             :rtype ExistsTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintEnabled: Whether fingerprinting is enabled for this device
             :rtype FingerPrintEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintMessage: A message detailing the current fingerprint status
             :rtype FingerPrintMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintStatus: Indicates whether device fingerprinting has been successfully executed for the device
             :rtype FingerPrintStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintTimestamp: The date/time of the last update to the fingerprint status
             :rtype FingerPrintTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FirstSeen: The date and time this record was first seen
             :rtype FirstSeen: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ForwardingInd: The indicator of collection of forwarding information
             :rtype ForwardingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return GlobalConfigCollectionEnabled: Whether configuration collection is enabled globally
             :rtype GlobalConfigCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return GlobalConfigCollectionMessage: Global configuration collection details message
             :rtype GlobalConfigCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return InBlackout: In Blackout?
             :rtype InBlackout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return InPortControlBlackout: In Port Control Blackout?
             :rtype InPortControlBlackout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastAction: The last action (from the set in this model) executed against this device
             :rtype LastAction: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastSeen: The timestamp of when data was last polled from this device
             :rtype LastSeen: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastTimestamp: The date/time of the last action
             :rtype LastTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LicenseOverride: Licensing setting. Requested unlicensed: 0, requested licensed: 1, automatic: 2
             :rtype LicenseOverride: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return PortControlBlackoutDuration: Port Control Blackout in minutes
             :rtype PortControlBlackoutDuration: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableMessage: A message detailing the current ACL/rule list analysis status
             :rtype ReachableMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableStatus: Indicates whether device is reachable according to it's ACL/rule list
             :rtype ReachableStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableTimestamp: The date/time of the last update to the reachable status
             :rtype ReachableTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisMessage: A message detailing the current ACL/rule list analysis status
             :rtype RuleListAnalysisMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisStatus: Indicates whether ACLs/rule lists have been successfully collected from the device
             :rtype RuleListAnalysisStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisTimestamp: The date/time of the last update to the rule list status
             :rtype RuleListAnalysisTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SAMLicensedInd: Licensed for Security Device Controller
             :rtype SAMLicensedInd: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionEnabled: SDN collection enabled?
             :rtype SDNCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionMessage: SDN collection message
             :rtype SDNCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionStatus: Indicates whether SDN data has been successfully collected for the device
             :rtype SDNCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionTimestamp: The date/time of the last update to the SDN collection status
             :rtype SDNCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionEnabled: SNMP collection enabled?
             :rtype SNMPCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionMessage: A message detailing the current SNMP collection status
             :rtype SNMPCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionStatus: Indicates whether SNMP data has been successfully collected from the device
             :rtype SNMPCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionTimestamp: The date/time of the last update to the SNMP collection status
             :rtype SNMPCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialMessage: A message detailing the current SNMP credential status
             :rtype SNMPCredentialMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialStatus: Indicates the status of SNMP discovery attempt of the device
             :rtype SNMPCredentialStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialTimestamp: The date/time of the last update to the SNMP credential status
             :rtype SNMPCredentialTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SPMLicensedInd: Licensed for Switch Port Manager
             :rtype SPMLicensedInd: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return StartBlackoutSchedule: The blackout start time in cron format
             :rtype StartBlackoutSchedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return StartPortControlBlackoutSchedule: Port Control Blackout in cron format
             :rtype StartPortControlBlackoutSchedule: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: License Status
             :rtype Status: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return StatusDetail: Licenses applied
             :rtype StatusDetail: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return UnitID: The internal identifier of the collector on which the device is configured
             :rtype UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkID: The internal identifier for the network which the device is associated to
             :rtype VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkMemberArtificialInd: Indicates is this is an artificial VNM
             :rtype VirtualNetworkMemberArtificialInd: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkName: The name of the Network View
             :rtype VirtualNetworkName: String

            """

        return self.api_request(self._get_method_fullname("static"), kwargs)

    def telnet_queue(self, **kwargs):
        """Displays the telnet queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The id of the device
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPDotted: The IP address of the device, in dotted (or colon-delimited for IPv6) format
             :rtype DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPNumeric: The numerical value of the device IP address
             :rtype DeviceIPNumeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceName: The name of the device
             :rtype DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The determined device type
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastAction: The last action executed against this device
             :rtype LastAction: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastTimestamp: The date/time of the last action
             :rtype LastTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NextAttempt: The date/time of the next attempt
             :rtype NextAttempt: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: The status of the request
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkID: The internal identifier for the network which the device is associated to
             :rtype VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkName: The name of the Network View
             :rtype VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return total: The total number of rows in the response
             :rtype total: Integer

            """

        return self.api_request(self._get_method_fullname("telnet_queue"), kwargs)

    def ssh_queue(self, **kwargs):
        """Displays the ssh queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The id of the device
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPDotted: The IP address of the device, in dotted (or colon-delimited for IPv6) format
             :rtype DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPNumeric: The numerical value of the device IP address
             :rtype DeviceIPNumeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceName: The name of the device
             :rtype DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The determined device type
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastAction: The last action executed against this device
             :rtype LastAction: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastTimestamp: The date/time of the last action
             :rtype LastTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NextAttempt: The date/time of the next attempt
             :rtype NextAttempt: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: The status of the request
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkID: The internal identifier for the network which the device is associated to
             :rtype VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkName: The name of the Network View
             :rtype VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return total: The total number of rows in the response
             :rtype total: Integer

            """

        return self.api_request(self._get_method_fullname("ssh_queue"), kwargs)

    def snmp_queue(self, **kwargs):
        """Displays the snmp queue

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The index of the first row to display
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 25

             :param limit: The maximum number of rows from the start to display
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The id of the device
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPDotted: The IP address of the device, in dotted (or colon-delimited for IPv6) format
             :rtype DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPNumeric: The numerical value of the device IP address
             :rtype DeviceIPNumeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceName: The name of the device
             :rtype DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The determined device type
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastAction: The last action executed against this device
             :rtype LastAction: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastTimestamp: The date/time of the last action
             :rtype LastTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NextAttempt: The date/time of the next attempt
             :rtype NextAttempt: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: The status of the request
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkID: The internal identifier for the network which the device is associated to
             :rtype VirtualNetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return VirtualNetworkName: The name of the Network View
             :rtype VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return total: The total number of rows in the response
             :rtype total: Integer

            """

        return self.api_request(self._get_method_fullname("snmp_queue"), kwargs)

    def summary(self, **kwargs):
        """Summary data for discovery statuses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NumIdentified: The number of identified IP addresses
             :rtype NumIdentified: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NumReached: The number of devices that have been touched by NetMRI
             :rtype NumReached: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NumClassified: The number of fully discovered devices
             :rtype NumClassified: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NumReachedNotClassified: The number of devices touched by NetMRI but not classified
             :rtype NumReachedNotClassified: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NumProcessed: The number of fully processed devices
             :rtype NumProcessed: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Licensed: The number of licensed devices
             :rtype Licensed: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Networked: The number of networked devices
             :rtype Networked: Integer

            """

        return self.api_request(self._get_method_fullname("summary"), kwargs)

    def discover_next(self, **kwargs):
        """Set the given device ids to be discovered next

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: An array of device ids to be discovered next
             :type DeviceIDs: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discover_next"), kwargs)

    def discover_now(self, **kwargs):
        """Set the "DeviceID" of the given device to be discovered now and check the status of previously started discovery process. If the "id" parameter is not set, the method starts a new Discover Now process and returns its id for further tracking the process status. If the "id" parameter is set, the method returns a chunk of log output of the corresponding discovery process. The number of bytes to read is defined by the "read" parameter.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the previously started discovery process required to retrieve its status
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param DeviceID: ID of the device to re-discover now, if known
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address: Device IP address to be discovered now
             :type ip_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the discover now output
             :type read: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param ignore_history_ind: If true, NetMRI will not check for previous instances of this IP address, and therefore will not associate this IP address with the associated device history.
             :type ignore_history_ind: Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mac_address: Device MAC address to be discovered now
             :type mac_address: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: ID for further tracking the process status
             :rtype id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return read: The number of bytes to read
             :rtype read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return output: Chunk of log output of the corresponding discovery process
             :rtype output: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the remaining output data: 0 - no data, 1 - data is available
             :rtype status: Integer

            """

        return self.api_request(self._get_method_fullname("discover_now"), kwargs)

    def abort_discovery(self, **kwargs):
        """Abort an outstanding discover now session

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: ID of the discover now request to abort
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("abort_discovery"), kwargs)

    def override_licenses(self, **kwargs):
        """Overrides a license for all or some devices

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: The list of devices to override licenses
             :type DeviceIDs: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Licensed: The state of the device license override. Valid values are 0 (unlicensed), 1 (licensed), 2 (automatic)
             :type Licensed: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortManagement: The state of the Switch Port Management license override. Valid values are on or off if exists. An empty string is passed if not present.
             :type SwitchPortManagement: String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessProvisioning: The state of the Security Device Controller license override. Valid values are on or off if exists. An empty string is passed if not present.
             :type AccessProvisioning: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("override_licenses"), kwargs)

    def unmanage(self, **kwargs):
        """Set one or more specified devices to unmanaged

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIDs: The list of devices to set to unmanaged
             :type DeviceIDs: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("unmanage"), kwargs)

    def update_snmp(self, **kwargs):
        """Update the SNMP read credential for a device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to be updated
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPVersion: The SNMP Version
             :type SNMPVersion: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPRead: The SNMP read community
             :type SNMPRead: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPW: The SNMP auth password for SNMPv3
             :type SNMPAuthPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMP auth protocol for SNMPv3
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPW: The SNMP priv password for SNMPv3
             :type SNMPPrivPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMP priv protocol for SNMPv3
             :type SNMPPrivProto: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_snmp"), kwargs)

    def update_cli_credentials(self, **kwargs):
        """Update the CLI credential for a device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to be updated
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Username: SSH username
             :type config.SSH.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.SSH.Password: SSH password
             :type config.SSH.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Username: Telnet username
             :type config.Telnet.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.Telnet.Password: Telnet password
             :type config.Telnet.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Username: HTTP username
             :type config.HTTP.Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.HTTP.Password: HTTP password
             :type config.HTTP.Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config.EnablePassword: Enable password
             :type config.EnablePassword: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 22

             :param config.SSH.Port: CLI SSH Port
             :type config.SSH.Port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 23

             :param config.Telnet.Port: CLI Telnet Port
             :type config.Telnet.Port: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_cli_credentials"), kwargs)

    def cli_guesses(self, **kwargs):
        """Displays the status of all devices CLI guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The id of the device
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Protocol: Protocol
             :rtype Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Username: Username
             :rtype Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Password: Password
             :rtype Password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return EnablePassword: Enable Password
             :rtype EnablePassword: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: Status
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Timestamp: Timestamp
             :rtype Timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Port: Port
             :rtype Port: Integer

            """

        return self.api_request(self._get_method_fullname("cli_guesses"), kwargs)

    def snmp_guesses(self, **kwargs):
        """Displays the status of all devices SNMP guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The id of the device
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Protocol: Protocol
             :rtype Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Username: Username
             :rtype Username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Community: The SNMP community string
             :rtype Community: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPAuthPW: The SNMPv3 authentication protocol password
             :rtype SNMPAuthPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential
             :rtype SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPPrivPW: The SNMPv3 privacy protocol password
             :rtype SNMPPrivPW: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential
             :rtype SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: Status
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Timestamp: Timestamp
             :rtype Timestamp: DateTime

            """

        return self.api_request(self._get_method_fullname("snmp_guesses"), kwargs)

    def show_opsec_certificate(self, **kwargs):
        """Return OPSEC device certificate

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show_opsec_certificate"), kwargs)

    def opsec_guesses(self, **kwargs):
        """Displays the status of all devices OPSEC guesses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: Filename for exported data
             :type filename: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("opsec_guesses"), kwargs)

    def status_management(self, **kwargs):
        """Returns a list of discovery statuses of the device with given id

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The id of the device to get management status
             :type DeviceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return AccessInd: The indicator of collection of the filtering access information
             :rtype AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialMessage: A message detailing the current CLI credential status
             :rtype CLICredentialMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialStatus: Indicates the status of SSH discovery attempt of the device
             :rtype CLICredentialStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return CLICredentialTimestamp: The date/time of the last update to the CLI credential status
             :rtype CLICredentialTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionEnabled: Whether configuration polling is enabled for this device
             :rtype ConfigCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionMessage: A message detailing the current configuration file collection status
             :rtype ConfigCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionStatus: Indicates whether configuration files have been successfully collected from the device
             :rtype ConfigCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ConfigCollectionTimestamp: The date/time of the last update to the configuration collection status
             :rtype ConfigCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DataSourceName: The name of this data source
             :rtype DataSourceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network
             :rtype DeviceFirstOccurrenceTime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupMessage: A message detailing the current device group assignment status
             :rtype DeviceGroupMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupStatus: Indicates whether the device has been successfully assigned to a device group
             :rtype DeviceGroupStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceGroupTimestamp: The date/time of the last update to the device group assignment status
             :rtype DeviceGroupTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: Internal system identifier for the discovery status
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format
             :rtype DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The determined device type
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DisplayCollector: Display collector
             :rtype DisplayCollector: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ExistsMessage: A message detailing the method by which the device is decided to exist
             :rtype ExistsMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ExistsTimestamp: The date/time of the last device existance update
             :rtype ExistsTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintEnabled: Whether fingerprinting is enabled for this device
             :rtype FingerPrintEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintMessage: A message detailing the current fingerprint status
             :rtype FingerPrintMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintStatus: Indicates whether device fingerprinting has been successfully executed for the device
             :rtype FingerPrintStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FingerPrintTimestamp: The date/time of the last update to the fingerprint status
             :rtype FingerPrintTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return FirstSeen: The date and time this record was first seen
             :rtype FirstSeen: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ForwardingInd: The indicator of collection of forwarding information
             :rtype ForwardingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastAction: The last action (from the set in this model) executed against this device
             :rtype LastAction: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastSeen: The timestamp of when data was last polled from this device
             :rtype LastSeen: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LastTimestamp: The date/time of the last action
             :rtype LastTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LicenseOverride: Licensing setting. Requested unlicensed: 0, requested licensed: 1, automatic: 2
             :rtype LicenseOverride: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return LicenseStatus: Licenses applied
             :rtype LicenseStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NetBIOSMessage: Message detailing current accessibility via NetBIOS
             :rtype NetBIOSMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NetBIOSStatus: Indicates where device is accessible via NetBIOS
             :rtype NetBIOSStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return NetBIOSTimestamp: The date/time of the last successful NetBIOS discovery attempt
             :rtype NetBIOSTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return PingMessage: Message detailing current pingable status
             :rtype PingMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return PingStatus: Indicates whether device is pingable
             :rtype PingStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return PingTimestamp: The date/time of the last successful ping
             :rtype PingTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableMessage: A message detailing the current ACL/rule list analysis status
             :rtype ReachableMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableStatus: Indicates whether device is reachable according to it's ACL/rule list
             :rtype ReachableStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ReachableTimestamp: The date/time of the last update to the reachable status
             :rtype ReachableTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisMessage: A message detailing the current ACL/rule list analysis status
             :rtype RuleListAnalysisMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisStatus: Indicates whether ACLs/rule lists have been successfully collected from the device
             :rtype RuleListAnalysisStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return RuleListAnalysisTimestamp: The date/time of the last update to the rule list status
             :rtype RuleListAnalysisTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SAMLicensedInd: Licensed for Security Device Controller
             :rtype SAMLicensedInd: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionMessage: SDN collection message
             :rtype SDNCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionStatus: Indicates whether SDN data has been successfully collected for the device
             :rtype SDNCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SDNCollectionTimestamp: The date/time of the last update to the SDN collection status
             :rtype SDNCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionEnabled: SNMP collection enabled?
             :rtype SNMPCollectionEnabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionMessage: A message detailing the current SNMP collection status
             :rtype SNMPCollectionMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionStatus: Indicates whether SNMP data has been successfully collected from the device
             :rtype SNMPCollectionStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCollectionTimestamp: The date/time of the last update to the SNMP collection status
             :rtype SNMPCollectionTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialMessage: A message detailing the current SNMP credential status
             :rtype SNMPCredentialMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialStatus: Indicates the status of SNMP discovery attempt of the device
             :rtype SNMPCredentialStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SNMPCredentialTimestamp: The date/time of the last update to the SNMP credential status
             :rtype SNMPCredentialTimestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return SPMLicensedInd: Licensed for Switch Port Manager
             :rtype SPMLicensedInd: Boolean

            """

        return self.api_request(self._get_method_fullname("status_management"), kwargs)

    def setup_summary(self, **kwargs):
        """Discovery Wizard setup summary information

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return automatic_discovery_enabled: Automatic discovery enabled
             :rtype automatic_discovery_enabled: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ranges_reasonably_small: Ranges reasonably small
             :rtype ranges_reasonably_small: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return seed_exists: Seed exists
             :rtype seed_exists: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_credentials_exist: CLI credentials exist
             :rtype cli_credentials_exist: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_credentials_exist: SNMP credentials exist
             :rtype snmp_credentials_exist: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return at_least_one_device_found: At least one device found
             :rtype at_least_one_device_found: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return at_least_one_device_fingerprinted: At least one device fingerprinted
             :rtype at_least_one_device_fingerprinted: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return at_least_one_device_fully_discovered: At least one device fully discovered
             :rtype at_least_one_device_fully_discovered: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_collected_from_one_device: SNMP collected from one device
             :rtype snmp_collected_from_one_device: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_collected_from_one_device: SDN collected from one device
             :rtype sdn_collected_from_one_device: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_collected_from_one_device: Config collected from one device
             :rtype config_collected_from_one_device: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_collection_enabled: SNMP collection enabled
             :rtype snmp_collection_enabled: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_collection_enabled: Config collection enabled
             :rtype config_collection_enabled: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return finger_print_enabled: Fingerprint enabled
             :rtype finger_print_enabled: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_collection_enabled: SDN collection enabled
             :rtype sdn_collection_enabled: Boolean

            """

        return self.api_request(self._get_method_fullname("setup_summary"), kwargs)
