from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceGroupRemote(RemoteModel):
    """
    Device groups defined in NetMRI.


    |  ``DeviceGroupID:`` The internal NetMRI identifier for this Device Group.
    |  ``attribute type:`` number

    |  ``DeviceGroupStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DeviceGroupTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``GroupID:`` The internal NetMRI identifier for this Device Group.
    |  ``attribute type:`` number

    |  ``GroupName:`` The name of this device group.
    |  ``attribute type:`` string

    |  ``Criteria:`` The criteria used to define membership within this device group.
    |  ``attribute type:`` string

    |  ``Rank:`` The device group rank. If a device falls within multiple groups, the group settings with the highest rank will take precedence.
    |  ``attribute type:`` number

    |  ``SNMPPolling:`` 1 if NetMRI SNMP polling is enabled for the device group members; 0 otherwise.
    |  ``attribute type:`` number

    |  ``SNMPAnalysis:`` 1 if NetMRI performs analysis on the device group members; 0 otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
    |  ``attribute type:`` number

    |  ``FingerPrint:`` If 1, then NetMRI fingerprinting is enabled for the device.
    |  ``attribute type:`` number

    |  ``CCSCollection:`` If 1, then CCS scripts may be executed against the members of this device group.
    |  ``attribute type:`` number

    |  ``VendorDefaultCollection:`` If 1, then NetMRI vendor default credential checking is enabled for the device group members.
    |  ``attribute type:`` number

    |  ``ConfigPolling:`` 1 if NetMRI configuration collection is enabled for the device group members; 0 otherwise.
    |  ``attribute type:`` number

    |  ``PortScanning:`` 1 if NetMRI port scanning is enabled for the device; 0 otherwise.
    |  ``attribute type:`` number

    |  ``StandardsCompliance:`` 1 if this device group should be considered during standards compliance checks, 0 otherwise.
    |  ``attribute type:`` number

    |  ``MemberCount:`` The number of devices in the group.
    |  ``attribute type:`` number

    |  ``ConfigLocked:`` If 1, then changes detected on members of the device group will be considered unauthorized.
    |  ``attribute type:`` number

    |  ``PolicyScheduleMode:`` Unused.
    |  ``attribute type:`` string

    |  ``NetBIOSScanningInd:`` A flag indicating if NetMRI scans for the NetBIOS name.
    |  ``attribute type:`` bool

    |  ``SPMCollectionInd:`` A flag indicating if the Device Group has Switch Port Management data collection enabled.
    |  ``attribute type:`` bool

    |  ``ARPCacheRefreshInd:`` A flag indicating if NetMRI refreshes ARP caches to aid in switch-port data collection.
    |  ``attribute type:`` bool

    |  ``SAMLicensedInd:`` A flag indicating if the Device Group has Security Control enabled.
    |  ``attribute type:`` bool

    |  ``CLIPolling:`` A flag indicating whether this group should be polled via the command line interface.
    |  ``attribute type:`` bool

    |  ``AdvancedGroupInd:`` A flag indicating whether this group is an advanced group.
    |  ``attribute type:`` bool

    |  ``IncludeEndHostsInd:`` A flag indicating whether this group should include end host devices.
    |  ``attribute type:`` bool

    |  ``ParentDeviceGroupID:`` Internal identifier for the parent device group. A valus of 0 is used for root level groups.
    |  ``attribute type:`` number

    |  ``DeviceGroupDefnID:`` Mapping to the Device Group Definition Identifier
    |  ``attribute type:`` number

    |  ``PerfEnvPollingInd:`` A flag that indicates if Performance and Environment polling is enabled for the device group members.
    |  ``attribute type:`` bool

    |  ``PrivilegedPollingInd:`` A flag indicated that NetMRI should send enable command when interacting with device
    |  ``attribute type:`` bool

    |  ``PolFreqModifier:`` Polling frequency modifier for devices belonging to this device group. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
    |  ``attribute type:`` number

    |  ``UseGlobalPolFreq:`` A flag indicating if Global Polling Frequency should be used instead Device Group Polling Frequency.
    |  ``attribute type:`` bool

    |  ``CredentialGroupID:`` The unique identifier of the credential group.
    |  ``attribute type:`` number

    """

    properties = ("DeviceGroupID",
                  "DeviceGroupStartTime",
                  "DeviceGroupEndTime",
                  "DeviceGroupChangedCols",
                  "DeviceGroupTimestamp",
                  "DataSourceID",
                  "GroupID",
                  "GroupName",
                  "Criteria",
                  "Rank",
                  "SNMPPolling",
                  "SNMPAnalysis",
                  "FingerPrint",
                  "CCSCollection",
                  "VendorDefaultCollection",
                  "ConfigPolling",
                  "PortScanning",
                  "StandardsCompliance",
                  "MemberCount",
                  "ConfigLocked",
                  "PolicyScheduleMode",
                  "NetBIOSScanningInd",
                  "SPMCollectionInd",
                  "ARPCacheRefreshInd",
                  "SAMLicensedInd",
                  "CLIPolling",
                  "AdvancedGroupInd",
                  "IncludeEndHostsInd",
                  "ParentDeviceGroupID",
                  "DeviceGroupDefnID",
                  "PerfEnvPollingInd",
                  "PrivilegedPollingInd",
                  "PolFreqModifier",
                  "UseGlobalPolFreq",
                  "CredentialGroupID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"GroupID": self.GroupID})
