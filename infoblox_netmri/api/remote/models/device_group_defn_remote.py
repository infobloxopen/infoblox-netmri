from ..remote import RemoteModel


class DeviceGroupDefnRemote(RemoteModel):
    """
    The device group criteria definitions. This is distinct from the evaluated device groups captured in the DeviceGroup API. One Device Group Definition may result in several Device Groups, one within each defined Network.


    |  ``GroupID:`` The internal NetMRI identifier for this device group definition.
    |  ``attribute type:`` number

    |  ``GroupName:`` The device group name, as specified by the user.
    |  ``attribute type:`` string

    |  ``Criteria:`` The criteria used to place members within the group.
    |  ``attribute type:`` string

    |  ``Rank:`` The rank is used to determine which group settings to apply to a device that is a member of multiple groups. The highest ranked group's settings will be used.
    |  ``attribute type:`` string

    |  ``SNMPPolling:`` A flag indicating whether this group should be polled via SNMP.
    |  ``attribute type:`` number

    |  ``SNMPAnalysis:`` A flag indicating whether issue analysis should be performed on this group.
    |  ``attribute type:`` number

    |  ``FingerPrint:`` A flag indicating whether network fingerprinting should be performed on this group.
    |  ``attribute type:`` number

    |  ``CCSCollection:`` A flag indicating whether job execution is enabled against this group.
    |  ``attribute type:`` number

    |  ``VendorDefaultCollection:`` A flag indicating whether vendor default credential collection is enabled for this group.
    |  ``attribute type:`` number

    |  ``ConfigPolling:`` A flag indicating whether configuration file collection is enabled for this group.
    |  ``attribute type:`` number

    |  ``PortScanning:`` A flag indicating whether port scanning is enabled for this group.
    |  ``attribute type:`` number

    |  ``StandardsCompliance:`` A flag indicating whether this group is subject to standard's compliance reporting.
    |  ``attribute type:`` number

    |  ``MemberCount:`` Not used.
    |  ``attribute type:`` number

    |  ``ConfigLocked:`` Indicates whether configuration changes within this group are considered authorized or unauthorized.
    |  ``attribute type:`` number

    |  ``PolicyScheduleMode:`` Not used.
    |  ``attribute type:`` string

    |  ``SPMCollectionInd:`` A flag indicating whether Switch Port Management collection applies to this group.
    |  ``attribute type:`` bool

    |  ``NetBIOSScanningInd:`` A flag indicating whether to scan this group for NetBOIS names.
    |  ``attribute type:`` bool

    |  ``ARPCacheRefreshInd:`` A flag indicating whether to refresh the device ARP and forwarding table caches for devices in this group prior to data collection.
    |  ``attribute type:`` bool

    |  ``SAMLicensedInd:`` A flag indicating whether or not access diff viewer is available for this entry.
    |  ``attribute type:`` bool

    |  ``UpdatedAt:`` The date and time this record was last modified.
    |  ``attribute type:`` datetime

    |  ``StartBlackoutSchedule:`` The blackout start time in cron format.
    |  ``attribute type:`` string

    |  ``BlackoutDuration:`` The blackout duration in minutes.
    |  ``attribute type:`` number

    |  ``CLIPolling:`` A flag indicating whether this group should be polled via the command line interface.
    |  ``attribute type:`` bool

    |  ``StartPortControlBlackoutSchedule:`` Port Control Blackout in cron format.
    |  ``attribute type:`` string

    |  ``PortControlBlackoutDuration:`` Port Control Blackout in minutes.
    |  ``attribute type:`` number

    |  ``AdvancedGroupInd:`` A flag indicating whether this group is an advanced group.
    |  ``attribute type:`` bool

    |  ``IncludeEndHostsInd:`` A flag indicating whether this group should include end host devices.
    |  ``attribute type:`` bool

    |  ``ParentDeviceGroupID:`` Internal identifier for the parent device group. A valus of 0 is used for root level groups.
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

    properties = ("GroupID",
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
                  "SPMCollectionInd",
                  "NetBIOSScanningInd",
                  "ARPCacheRefreshInd",
                  "SAMLicensedInd",
                  "UpdatedAt",
                  "StartBlackoutSchedule",
                  "BlackoutDuration",
                  "CLIPolling",
                  "StartPortControlBlackoutSchedule",
                  "PortControlBlackoutDuration",
                  "AdvancedGroupInd",
                  "IncludeEndHostsInd",
                  "ParentDeviceGroupID",
                  "PerfEnvPollingInd",
                  "PrivilegedPollingInd",
                  "PolFreqModifier",
                  "UseGlobalPolFreq",
                  "CredentialGroupID",
                  )
