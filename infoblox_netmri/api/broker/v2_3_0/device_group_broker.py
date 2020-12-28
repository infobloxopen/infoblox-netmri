from ..broker import Broker


class DeviceGroupBroker(Broker):
    controller = "device_groups"

    def index(self, **kwargs):
        """Lists the available device groups. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Array of Integer

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

             :param timestamp: The data returned will represent the device groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group methods. The listed methods will be called on each device group returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceGroup. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return device_groups: An array of the DeviceGroup objects that match the specified input criteria.
             :rtype device_groups: Array of DeviceGroup

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device groups matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ARPCacheRefreshInd: A flag indicating if NetMRI refreshes ARP caches to aid in switch-port data collection.
             :type ARPCacheRefreshInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ARPCacheRefreshInd: A flag indicating if NetMRI refreshes ARP caches to aid in switch-port data collection.
             :type ARPCacheRefreshInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AdvancedGroupInd: A flag indicating whether this group is an advanced group.
             :type AdvancedGroupInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AdvancedGroupInd: A flag indicating whether this group is an advanced group.
             :type AdvancedGroupInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CCSCollection: If 1, then CCS scripts may be executed against the members of this device group.
             :type CCSCollection: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CCSCollection: If 1, then CCS scripts may be executed against the members of this device group.
             :type CCSCollection: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CLIPolling: A flag indicating whether this group should be polled via the command line interface.
             :type CLIPolling: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CLIPolling: A flag indicating whether this group should be polled via the command line interface.
             :type CLIPolling: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigLocked: If 1, then changes detected on members of the device group will be considered unauthorized.
             :type ConfigLocked: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigLocked: If 1, then changes detected on members of the device group will be considered unauthorized.
             :type ConfigLocked: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigPolling: 1 if NetMRI configuration collection is enabled for the device group members; 0 otherwise.
             :type ConfigPolling: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigPolling: 1 if NetMRI configuration collection is enabled for the device group members; 0 otherwise.
             :type ConfigPolling: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The criteria used to define membership within this device group.
             :type Criteria: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Criteria: The criteria used to define membership within this device group.
             :type Criteria: Array of String

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

             :param DeviceGroupChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceGroupChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceGroupChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupDefnID: Mapping to the Device Group Definition Identifier
             :type DeviceGroupDefnID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupDefnID: Mapping to the Device Group Definition Identifier
             :type DeviceGroupDefnID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceGroupEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceGroupEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier for this Device Group.
             :type DeviceGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier for this Device Group.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupStartTime: The starting effective time of this record.
             :type DeviceGroupStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupStartTime: The starting effective time of this record.
             :type DeviceGroupStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupTimestamp: The date and time this record was collected or calculated.
             :type DeviceGroupTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupTimestamp: The date and time this record was collected or calculated.
             :type DeviceGroupTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FingerPrint: If 1, then NetMRI fingerprinting is enabled for the device.
             :type FingerPrint: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FingerPrint: If 1, then NetMRI fingerprinting is enabled for the device.
             :type FingerPrint: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of this device group.
             :type GroupName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupName: The name of this device group.
             :type GroupName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IncludeEndHostsInd: A flag indicating whether this group should include end host devices.
             :type IncludeEndHostsInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IncludeEndHostsInd: A flag indicating whether this group should include end host devices.
             :type IncludeEndHostsInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The number of devices in the group.
             :type MemberCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemberCount: The number of devices in the group.
             :type MemberCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name.
             :type NetBIOSScanningInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name.
             :type NetBIOSScanningInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceGroupID: Internal identifier for the parent device group. A valus of 0 is used for root level groups.
             :type ParentDeviceGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceGroupID: Internal identifier for the parent device group. A valus of 0 is used for root level groups.
             :type ParentDeviceGroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for the device group members.
             :type PerfEnvPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for the device group members.
             :type PerfEnvPollingInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolFreqModifier: Polling frequency modifier for devices belonging to this device group. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
             :type PolFreqModifier: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolFreqModifier: Polling frequency modifier for devices belonging to this device group. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
             :type PolFreqModifier: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyScheduleMode: Unused.
             :type PolicyScheduleMode: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolicyScheduleMode: Unused.
             :type PolicyScheduleMode: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PortScanning: 1 if NetMRI port scanning is enabled for the device; 0 otherwise.
             :type PortScanning: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PortScanning: 1 if NetMRI port scanning is enabled for the device; 0 otherwise.
             :type PortScanning: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device
             :type PrivilegedPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device
             :type PrivilegedPollingInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The device group rank. If a device falls within multiple groups, the group settings with the highest rank will take precedence.
             :type Rank: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Rank: The device group rank. If a device falls within multiple groups, the group settings with the highest rank will take precedence.
             :type Rank: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SAMLicensedInd: A flag indicating if the Device Group has Security Control enabled.
             :type SAMLicensedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SAMLicensedInd: A flag indicating if the Device Group has Security Control enabled.
             :type SAMLicensedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAnalysis: 1 if NetMRI performs analysis on the device group members; 0 otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type SNMPAnalysis: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAnalysis: 1 if NetMRI performs analysis on the device group members; 0 otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type SNMPAnalysis: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: 1 if NetMRI SNMP polling is enabled for the device group members; 0 otherwise.
             :type SNMPPolling: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPolling: 1 if NetMRI SNMP polling is enabled for the device group members; 0 otherwise.
             :type SNMPPolling: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SPMCollectionInd: A flag indicating if the Device Group has Switch Port Management data collection enabled.
             :type SPMCollectionInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SPMCollectionInd: A flag indicating if the Device Group has Switch Port Management data collection enabled.
             :type SPMCollectionInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StandardsCompliance: 1 if this device group should be considered during standards compliance checks, 0 otherwise.
             :type StandardsCompliance: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StandardsCompliance: 1 if this device group should be considered during standards compliance checks, 0 otherwise.
             :type StandardsCompliance: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UseGlobalPolFreq: A flag indicating if Global Polling Frequency should be used instead Device Group Polling Frequency.
             :type UseGlobalPolFreq: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UseGlobalPolFreq: A flag indicating if Global Polling Frequency should be used instead Device Group Polling Frequency.
             :type UseGlobalPolFreq: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VendorDefaultCollection: If 1, then NetMRI vendor default credential checking is enabled for the device group members.
             :type VendorDefaultCollection: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VendorDefaultCollection: If 1, then NetMRI vendor default credential checking is enabled for the device group members.
             :type VendorDefaultCollection: Array of Integer

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

             :param timestamp: The data returned will represent the device groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group methods. The listed methods will be called on each device group returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceGroup. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device groups, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ARPCacheRefreshInd, AdvancedGroupInd, CCSCollection, CLIPolling, ConfigLocked, ConfigPolling, CredentialGroupID, Criteria, DataSourceID, DeviceGroupChangedCols, DeviceGroupDefnID, DeviceGroupEndTime, DeviceGroupID, DeviceGroupStartTime, DeviceGroupTimestamp, FingerPrint, GroupID, GroupName, IncludeEndHostsInd, MemberCount, NetBIOSScanningInd, ParentDeviceGroupID, PerfEnvPollingInd, PolFreqModifier, PolicyScheduleMode, PortScanning, PrivilegedPollingInd, Rank, SAMLicensedInd, SNMPAnalysis, SNMPPolling, SPMCollectionInd, StandardsCompliance, UseGlobalPolFreq, VendorDefaultCollection.
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

             :return device_groups: An array of the DeviceGroup objects that match the specified input criteria.
             :rtype device_groups: Array of DeviceGroup

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device groups matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ARPCacheRefreshInd, AdvancedGroupInd, CCSCollection, CLIPolling, ConfigLocked, ConfigPolling, CredentialGroupID, Criteria, DataSourceID, DeviceGroupChangedCols, DeviceGroupDefnID, DeviceGroupEndTime, DeviceGroupID, DeviceGroupStartTime, DeviceGroupTimestamp, FingerPrint, GroupID, GroupName, IncludeEndHostsInd, MemberCount, NetBIOSScanningInd, ParentDeviceGroupID, PerfEnvPollingInd, PolFreqModifier, PolicyScheduleMode, PortScanning, PrivilegedPollingInd, Rank, SAMLicensedInd, SNMPAnalysis, SNMPPolling, SPMCollectionInd, StandardsCompliance, UseGlobalPolFreq, VendorDefaultCollection.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ARPCacheRefreshInd: The operator to apply to the field ARPCacheRefreshInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ARPCacheRefreshInd: A flag indicating if NetMRI refreshes ARP caches to aid in switch-port data collection. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ARPCacheRefreshInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ARPCacheRefreshInd: If op_ARPCacheRefreshInd is specified, the field named in this input will be compared to the value in ARPCacheRefreshInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ARPCacheRefreshInd must be specified if op_ARPCacheRefreshInd is specified.
             :type val_f_ARPCacheRefreshInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ARPCacheRefreshInd: If op_ARPCacheRefreshInd is specified, this value will be compared to the value in ARPCacheRefreshInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ARPCacheRefreshInd must be specified if op_ARPCacheRefreshInd is specified.
             :type val_c_ARPCacheRefreshInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AdvancedGroupInd: The operator to apply to the field AdvancedGroupInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AdvancedGroupInd: A flag indicating whether this group is an advanced group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AdvancedGroupInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AdvancedGroupInd: If op_AdvancedGroupInd is specified, the field named in this input will be compared to the value in AdvancedGroupInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AdvancedGroupInd must be specified if op_AdvancedGroupInd is specified.
             :type val_f_AdvancedGroupInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AdvancedGroupInd: If op_AdvancedGroupInd is specified, this value will be compared to the value in AdvancedGroupInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AdvancedGroupInd must be specified if op_AdvancedGroupInd is specified.
             :type val_c_AdvancedGroupInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CCSCollection: The operator to apply to the field CCSCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CCSCollection: If 1, then CCS scripts may be executed against the members of this device group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CCSCollection: If op_CCSCollection is specified, the field named in this input will be compared to the value in CCSCollection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CCSCollection must be specified if op_CCSCollection is specified.
             :type val_f_CCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CCSCollection: If op_CCSCollection is specified, this value will be compared to the value in CCSCollection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CCSCollection must be specified if op_CCSCollection is specified.
             :type val_c_CCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CLIPolling: The operator to apply to the field CLIPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CLIPolling: A flag indicating whether this group should be polled via the command line interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CLIPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CLIPolling: If op_CLIPolling is specified, the field named in this input will be compared to the value in CLIPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CLIPolling must be specified if op_CLIPolling is specified.
             :type val_f_CLIPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CLIPolling: If op_CLIPolling is specified, this value will be compared to the value in CLIPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CLIPolling must be specified if op_CLIPolling is specified.
             :type val_c_CLIPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigLocked: The operator to apply to the field ConfigLocked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigLocked: If 1, then changes detected on members of the device group will be considered unauthorized. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigLocked: If op_ConfigLocked is specified, the field named in this input will be compared to the value in ConfigLocked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigLocked must be specified if op_ConfigLocked is specified.
             :type val_f_ConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigLocked: If op_ConfigLocked is specified, this value will be compared to the value in ConfigLocked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigLocked must be specified if op_ConfigLocked is specified.
             :type val_c_ConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigPolling: The operator to apply to the field ConfigPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigPolling: 1 if NetMRI configuration collection is enabled for the device group members; 0 otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigPolling: If op_ConfigPolling is specified, the field named in this input will be compared to the value in ConfigPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigPolling must be specified if op_ConfigPolling is specified.
             :type val_f_ConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigPolling: If op_ConfigPolling is specified, this value will be compared to the value in ConfigPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigPolling must be specified if op_ConfigPolling is specified.
             :type val_c_ConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CredentialGroupID: The operator to apply to the field CredentialGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CredentialGroupID: The unique identifier of the credential group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CredentialGroupID: If op_CredentialGroupID is specified, the field named in this input will be compared to the value in CredentialGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CredentialGroupID must be specified if op_CredentialGroupID is specified.
             :type val_f_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CredentialGroupID: If op_CredentialGroupID is specified, this value will be compared to the value in CredentialGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CredentialGroupID must be specified if op_CredentialGroupID is specified.
             :type val_c_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Criteria: The operator to apply to the field Criteria. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Criteria: The criteria used to define membership within this device group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Criteria: If op_Criteria is specified, the field named in this input will be compared to the value in Criteria using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Criteria must be specified if op_Criteria is specified.
             :type val_f_Criteria: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Criteria: If op_Criteria is specified, this value will be compared to the value in Criteria using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Criteria must be specified if op_Criteria is specified.
             :type val_c_Criteria: String

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

             :param op_DeviceGroupChangedCols: The operator to apply to the field DeviceGroupChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupChangedCols: If op_DeviceGroupChangedCols is specified, the field named in this input will be compared to the value in DeviceGroupChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupChangedCols must be specified if op_DeviceGroupChangedCols is specified.
             :type val_f_DeviceGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupChangedCols: If op_DeviceGroupChangedCols is specified, this value will be compared to the value in DeviceGroupChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupChangedCols must be specified if op_DeviceGroupChangedCols is specified.
             :type val_c_DeviceGroupChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupDefnID: The operator to apply to the field DeviceGroupDefnID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupDefnID: Mapping to the Device Group Definition Identifier For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupDefnID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupDefnID: If op_DeviceGroupDefnID is specified, the field named in this input will be compared to the value in DeviceGroupDefnID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupDefnID must be specified if op_DeviceGroupDefnID is specified.
             :type val_f_DeviceGroupDefnID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupDefnID: If op_DeviceGroupDefnID is specified, this value will be compared to the value in DeviceGroupDefnID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupDefnID must be specified if op_DeviceGroupDefnID is specified.
             :type val_c_DeviceGroupDefnID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupEndTime: The operator to apply to the field DeviceGroupEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupEndTime: If op_DeviceGroupEndTime is specified, the field named in this input will be compared to the value in DeviceGroupEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupEndTime must be specified if op_DeviceGroupEndTime is specified.
             :type val_f_DeviceGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupEndTime: If op_DeviceGroupEndTime is specified, this value will be compared to the value in DeviceGroupEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupEndTime must be specified if op_DeviceGroupEndTime is specified.
             :type val_c_DeviceGroupEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupID: The operator to apply to the field DeviceGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupID: The internal NetMRI identifier for this Device Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupID: If op_DeviceGroupID is specified, the field named in this input will be compared to the value in DeviceGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupID must be specified if op_DeviceGroupID is specified.
             :type val_f_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupID: If op_DeviceGroupID is specified, this value will be compared to the value in DeviceGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupID must be specified if op_DeviceGroupID is specified.
             :type val_c_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupStartTime: The operator to apply to the field DeviceGroupStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupStartTime: If op_DeviceGroupStartTime is specified, the field named in this input will be compared to the value in DeviceGroupStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupStartTime must be specified if op_DeviceGroupStartTime is specified.
             :type val_f_DeviceGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupStartTime: If op_DeviceGroupStartTime is specified, this value will be compared to the value in DeviceGroupStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupStartTime must be specified if op_DeviceGroupStartTime is specified.
             :type val_c_DeviceGroupStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupTimestamp: The operator to apply to the field DeviceGroupTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupTimestamp: If op_DeviceGroupTimestamp is specified, the field named in this input will be compared to the value in DeviceGroupTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupTimestamp must be specified if op_DeviceGroupTimestamp is specified.
             :type val_f_DeviceGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupTimestamp: If op_DeviceGroupTimestamp is specified, this value will be compared to the value in DeviceGroupTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupTimestamp must be specified if op_DeviceGroupTimestamp is specified.
             :type val_c_DeviceGroupTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FingerPrint: The operator to apply to the field FingerPrint. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FingerPrint: If 1, then NetMRI fingerprinting is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FingerPrint: If op_FingerPrint is specified, the field named in this input will be compared to the value in FingerPrint using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FingerPrint must be specified if op_FingerPrint is specified.
             :type val_f_FingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FingerPrint: If op_FingerPrint is specified, this value will be compared to the value in FingerPrint using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FingerPrint must be specified if op_FingerPrint is specified.
             :type val_c_FingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GroupID: The operator to apply to the field GroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupID: The internal NetMRI identifier for this Device Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GroupID: If op_GroupID is specified, the field named in this input will be compared to the value in GroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GroupID must be specified if op_GroupID is specified.
             :type val_f_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GroupID: If op_GroupID is specified, this value will be compared to the value in GroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GroupID must be specified if op_GroupID is specified.
             :type val_c_GroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GroupName: The operator to apply to the field GroupName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupName: The name of this device group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GroupName: If op_GroupName is specified, the field named in this input will be compared to the value in GroupName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GroupName must be specified if op_GroupName is specified.
             :type val_f_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GroupName: If op_GroupName is specified, this value will be compared to the value in GroupName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GroupName must be specified if op_GroupName is specified.
             :type val_c_GroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IncludeEndHostsInd: The operator to apply to the field IncludeEndHostsInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IncludeEndHostsInd: A flag indicating whether this group should include end host devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IncludeEndHostsInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IncludeEndHostsInd: If op_IncludeEndHostsInd is specified, the field named in this input will be compared to the value in IncludeEndHostsInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IncludeEndHostsInd must be specified if op_IncludeEndHostsInd is specified.
             :type val_f_IncludeEndHostsInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IncludeEndHostsInd: If op_IncludeEndHostsInd is specified, this value will be compared to the value in IncludeEndHostsInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IncludeEndHostsInd must be specified if op_IncludeEndHostsInd is specified.
             :type val_c_IncludeEndHostsInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemberCount: The operator to apply to the field MemberCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemberCount: The number of devices in the group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemberCount: If op_MemberCount is specified, the field named in this input will be compared to the value in MemberCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemberCount must be specified if op_MemberCount is specified.
             :type val_f_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemberCount: If op_MemberCount is specified, this value will be compared to the value in MemberCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemberCount must be specified if op_MemberCount is specified.
             :type val_c_MemberCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NetBIOSScanningInd: The operator to apply to the field NetBIOSScanningInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NetBIOSScanningInd: If op_NetBIOSScanningInd is specified, the field named in this input will be compared to the value in NetBIOSScanningInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NetBIOSScanningInd must be specified if op_NetBIOSScanningInd is specified.
             :type val_f_NetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NetBIOSScanningInd: If op_NetBIOSScanningInd is specified, this value will be compared to the value in NetBIOSScanningInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NetBIOSScanningInd must be specified if op_NetBIOSScanningInd is specified.
             :type val_c_NetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ParentDeviceGroupID: The operator to apply to the field ParentDeviceGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ParentDeviceGroupID: Internal identifier for the parent device group. A valus of 0 is used for root level groups. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ParentDeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ParentDeviceGroupID: If op_ParentDeviceGroupID is specified, the field named in this input will be compared to the value in ParentDeviceGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ParentDeviceGroupID must be specified if op_ParentDeviceGroupID is specified.
             :type val_f_ParentDeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ParentDeviceGroupID: If op_ParentDeviceGroupID is specified, this value will be compared to the value in ParentDeviceGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ParentDeviceGroupID must be specified if op_ParentDeviceGroupID is specified.
             :type val_c_ParentDeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PerfEnvPollingInd: The operator to apply to the field PerfEnvPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for the device group members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PerfEnvPollingInd: If op_PerfEnvPollingInd is specified, the field named in this input will be compared to the value in PerfEnvPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PerfEnvPollingInd must be specified if op_PerfEnvPollingInd is specified.
             :type val_f_PerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PerfEnvPollingInd: If op_PerfEnvPollingInd is specified, this value will be compared to the value in PerfEnvPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PerfEnvPollingInd must be specified if op_PerfEnvPollingInd is specified.
             :type val_c_PerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolFreqModifier: The operator to apply to the field PolFreqModifier. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolFreqModifier: Polling frequency modifier for devices belonging to this device group. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolFreqModifier: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolFreqModifier: If op_PolFreqModifier is specified, the field named in this input will be compared to the value in PolFreqModifier using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolFreqModifier must be specified if op_PolFreqModifier is specified.
             :type val_f_PolFreqModifier: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolFreqModifier: If op_PolFreqModifier is specified, this value will be compared to the value in PolFreqModifier using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolFreqModifier must be specified if op_PolFreqModifier is specified.
             :type val_c_PolFreqModifier: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolicyScheduleMode: The operator to apply to the field PolicyScheduleMode. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolicyScheduleMode: Unused. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PolicyScheduleMode: If op_PolicyScheduleMode is specified, the field named in this input will be compared to the value in PolicyScheduleMode using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PolicyScheduleMode must be specified if op_PolicyScheduleMode is specified.
             :type val_f_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PolicyScheduleMode: If op_PolicyScheduleMode is specified, this value will be compared to the value in PolicyScheduleMode using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PolicyScheduleMode must be specified if op_PolicyScheduleMode is specified.
             :type val_c_PolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PortScanning: The operator to apply to the field PortScanning. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PortScanning: 1 if NetMRI port scanning is enabled for the device; 0 otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PortScanning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PortScanning: If op_PortScanning is specified, the field named in this input will be compared to the value in PortScanning using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PortScanning must be specified if op_PortScanning is specified.
             :type val_f_PortScanning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PortScanning: If op_PortScanning is specified, this value will be compared to the value in PortScanning using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PortScanning must be specified if op_PortScanning is specified.
             :type val_c_PortScanning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PrivilegedPollingInd: The operator to apply to the field PrivilegedPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PrivilegedPollingInd: If op_PrivilegedPollingInd is specified, the field named in this input will be compared to the value in PrivilegedPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PrivilegedPollingInd must be specified if op_PrivilegedPollingInd is specified.
             :type val_f_PrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PrivilegedPollingInd: If op_PrivilegedPollingInd is specified, this value will be compared to the value in PrivilegedPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PrivilegedPollingInd must be specified if op_PrivilegedPollingInd is specified.
             :type val_c_PrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Rank: The operator to apply to the field Rank. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Rank: The device group rank. If a device falls within multiple groups, the group settings with the highest rank will take precedence. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Rank: If op_Rank is specified, the field named in this input will be compared to the value in Rank using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Rank must be specified if op_Rank is specified.
             :type val_f_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Rank: If op_Rank is specified, this value will be compared to the value in Rank using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Rank must be specified if op_Rank is specified.
             :type val_c_Rank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SAMLicensedInd: The operator to apply to the field SAMLicensedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SAMLicensedInd: A flag indicating if the Device Group has Security Control enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SAMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SAMLicensedInd: If op_SAMLicensedInd is specified, the field named in this input will be compared to the value in SAMLicensedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SAMLicensedInd must be specified if op_SAMLicensedInd is specified.
             :type val_f_SAMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SAMLicensedInd: If op_SAMLicensedInd is specified, this value will be compared to the value in SAMLicensedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SAMLicensedInd must be specified if op_SAMLicensedInd is specified.
             :type val_c_SAMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPAnalysis: The operator to apply to the field SNMPAnalysis. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPAnalysis: 1 if NetMRI performs analysis on the device group members; 0 otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPAnalysis: If op_SNMPAnalysis is specified, the field named in this input will be compared to the value in SNMPAnalysis using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPAnalysis must be specified if op_SNMPAnalysis is specified.
             :type val_f_SNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPAnalysis: If op_SNMPAnalysis is specified, this value will be compared to the value in SNMPAnalysis using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPAnalysis must be specified if op_SNMPAnalysis is specified.
             :type val_c_SNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPPolling: The operator to apply to the field SNMPPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPolling: 1 if NetMRI SNMP polling is enabled for the device group members; 0 otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPPolling: If op_SNMPPolling is specified, the field named in this input will be compared to the value in SNMPPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPPolling must be specified if op_SNMPPolling is specified.
             :type val_f_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPPolling: If op_SNMPPolling is specified, this value will be compared to the value in SNMPPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPPolling must be specified if op_SNMPPolling is specified.
             :type val_c_SNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SPMCollectionInd: The operator to apply to the field SPMCollectionInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SPMCollectionInd: A flag indicating if the Device Group has Switch Port Management data collection enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SPMCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SPMCollectionInd: If op_SPMCollectionInd is specified, the field named in this input will be compared to the value in SPMCollectionInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SPMCollectionInd must be specified if op_SPMCollectionInd is specified.
             :type val_f_SPMCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SPMCollectionInd: If op_SPMCollectionInd is specified, this value will be compared to the value in SPMCollectionInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SPMCollectionInd must be specified if op_SPMCollectionInd is specified.
             :type val_c_SPMCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StandardsCompliance: The operator to apply to the field StandardsCompliance. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StandardsCompliance: 1 if this device group should be considered during standards compliance checks, 0 otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StandardsCompliance: If op_StandardsCompliance is specified, the field named in this input will be compared to the value in StandardsCompliance using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StandardsCompliance must be specified if op_StandardsCompliance is specified.
             :type val_f_StandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StandardsCompliance: If op_StandardsCompliance is specified, this value will be compared to the value in StandardsCompliance using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StandardsCompliance must be specified if op_StandardsCompliance is specified.
             :type val_c_StandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UseGlobalPolFreq: The operator to apply to the field UseGlobalPolFreq. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UseGlobalPolFreq: A flag indicating if Global Polling Frequency should be used instead Device Group Polling Frequency. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UseGlobalPolFreq: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UseGlobalPolFreq: If op_UseGlobalPolFreq is specified, the field named in this input will be compared to the value in UseGlobalPolFreq using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UseGlobalPolFreq must be specified if op_UseGlobalPolFreq is specified.
             :type val_f_UseGlobalPolFreq: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UseGlobalPolFreq: If op_UseGlobalPolFreq is specified, this value will be compared to the value in UseGlobalPolFreq using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UseGlobalPolFreq must be specified if op_UseGlobalPolFreq is specified.
             :type val_c_UseGlobalPolFreq: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VendorDefaultCollection: The operator to apply to the field VendorDefaultCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VendorDefaultCollection: If 1, then NetMRI vendor default credential checking is enabled for the device group members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VendorDefaultCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VendorDefaultCollection: If op_VendorDefaultCollection is specified, the field named in this input will be compared to the value in VendorDefaultCollection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VendorDefaultCollection must be specified if op_VendorDefaultCollection is specified.
             :type val_f_VendorDefaultCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VendorDefaultCollection: If op_VendorDefaultCollection is specified, this value will be compared to the value in VendorDefaultCollection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VendorDefaultCollection must be specified if op_VendorDefaultCollection is specified.
             :type val_c_VendorDefaultCollection: String

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

             :param timestamp: The data returned will represent the device groups as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device group methods. The listed methods will be called on each device group returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupID

             :param sort: The data field(s) to use for sorting the output. Default is GroupID. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceGroup. Valid values are DeviceGroupID, ParentDeviceGroupID, DeviceGroupDefnID, DeviceGroupStartTime, DeviceGroupEndTime, DeviceGroupChangedCols, DeviceGroupTimestamp, DataSourceID, GroupID, GroupName, Criteria, Rank, SNMPPolling, CLIPolling, SNMPAnalysis, FingerPrint, CCSCollection, VendorDefaultCollection, ConfigPolling, PortScanning, StandardsCompliance, MemberCount, ConfigLocked, PrivilegedPollingInd, UseGlobalPolFreq, PolFreqModifier, PolicyScheduleMode, PerfEnvPollingInd, SPMCollectionInd, NetBIOSScanningInd, ARPCacheRefreshInd, SAMLicensedInd, AdvancedGroupInd, IncludeEndHostsInd, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return device_groups: An array of the DeviceGroup objects that match the specified input criteria.
             :rtype device_groups: Array of DeviceGroup

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupID: The internal NetMRI identifier for this Device Group.
             :type GroupID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_group: The device group identified by the specified GroupID.
             :rtype device_group: DeviceGroup

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)
