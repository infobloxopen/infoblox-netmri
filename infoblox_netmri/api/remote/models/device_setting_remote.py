from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceSettingRemote(RemoteModel):
    """
    This table list out the entries of device setting within NetMRI.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier of each device from which device setting was collected.
    |  ``attribute type:`` number

    |  ``DevSetStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DevSetEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DevSetChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DevSetTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceSNMPVersion:`` The SNMP version of the device.
    |  ``attribute type:`` string

    |  ``DeviceSNMP3AuthProto:`` The SNMP3 authentication protocol of the device.
    |  ``attribute type:`` string

    |  ``DeviceSNMP3PrivProto:`` The SNMP3 privilege protocol of the device.
    |  ``attribute type:`` string

    |  ``DeviceSNMPTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DeviceSNMPCommunityReadSource:`` The read source of the SNMP community of devices.
    |  ``attribute type:`` string

    |  ``DeviceRespTime:`` The response time of the devices.
    |  ``attribute type:`` datetime

    |  ``DeviceRank:`` The device rank as set on the Device Viewer settings screen.
    |  ``attribute type:`` number

    |  ``DeviceConfigLockLastChangeBy:`` The user that last changed the configuration locked status of the device.
    |  ``attribute type:`` string

    |  ``DeviceConfigLockLastChangedTime:`` The date/time of the last change to the configuration locked status of the device.
    |  ``attribute type:`` datetime

    |  ``DeviceConfigLockedInd:`` If true, then changes detected will be considered unauthorized.
    |  ``attribute type:`` bool

    |  ``DeviceSNMPPollingInd:`` If true, than NetMRI SNMP polling is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DeviceConfigPollingInd:`` If true, than NetMRI configuration collection is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DevicePortScanningInd:`` If true, than NetMRI port scanning is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DeviceSNMPAnalysisInd:`` If true, than NetMRI performs analysis on the device. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
    |  ``attribute type:`` bool

    |  ``DeviceFingerPrintInd:`` If true, then NetMRI fingerprinting is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DeviceCCSCollectionInd:`` If true, then CCS scripts may be executed against the device.
    |  ``attribute type:`` bool

    |  ``DeviceVendorDefaultCollectionInd:`` If true, then NetMRI vendor default credential checking is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DeviceStandardsComplianceInd:`` If true, than this device should be considered during standards compliance checks.
    |  ``attribute type:`` bool

    |  ``DeviceLicensedInd:`` If true, then this device is licensed as a network device by NetMRI.
    |  ``attribute type:`` bool

    |  ``DeviceManagedInd:`` If true, then this device is managed.
    |  ``attribute type:`` bool

    |  ``DeviceNetBIOSScanningInd:`` A flag indicating if NetMRI scans for the NetBIOS name.
    |  ``attribute type:`` bool

    |  ``SPMLicensedInd:`` A flag indicating if the Device is licensed under the Switch Port Management module.
    |  ``attribute type:`` bool

    |  ``ARPCacheRefreshInd:`` A flag indicating if NetMRI refreshes ARP caches to aid in switch-port data collection.
    |  ``attribute type:`` bool

    |  ``DeviceCommunitySecure:`` The SNMP read community string for the device.
    |  ``attribute type:`` string

    |  ``DeviceSNMPCommunityReadSecure:`` The read operation of each device in SNMP community.
    |  ``attribute type:`` string

    |  ``DeviceSNMPCommunityWriteSecure:`` The write operation of each device in SNMP community.
    |  ``attribute type:`` string

    |  ``DeviceSNMP3AuthPWSecure:`` The SNMP3 authentication password of the device.
    |  ``attribute type:`` string

    |  ``DeviceSNMP3PrivPWSecure:`` The SNMP3 privilege password of the device.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number

    |  ``SAMLicensedInd:`` This flag indicating if the Device Security Control enabled.
    |  ``attribute type:`` string

    |  ``DeviceCLIPollingInd:`` If true, than NetMRI CLI polling is enabled for the device.
    |  ``attribute type:`` bool

    |  ``DevicePerfEnvPollingInd:`` A flag that indicates if Performance and Environment polling is enabled for this device.
    |  ``attribute type:`` bool

    |  ``DevicePrivilegedPollingInd:`` A flag indicated that NetMRI should send enable command when interacting with device
    |  ``attribute type:`` bool

    |  ``PolFreqModifier:`` Polling frequency modifier for this device. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
    |  ``attribute type:`` number

    |  ``UseGlobalPolFreq:`` A flag indicating if Global Polling Frequency should be used instead Device Group Polling Frequency.
    |  ``attribute type:`` bool

    |  ``CredentialGroupID:`` The unique identifier of the credential group.
    |  ``attribute type:`` number

    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "DevSetStartTime",
                  "DevSetEndTime",
                  "DevSetChangedCols",
                  "DevSetTimestamp",
                  "DeviceSNMPVersion",
                  "DeviceSNMP3AuthProto",
                  "DeviceSNMP3PrivProto",
                  "DeviceSNMPTimestamp",
                  "DeviceSNMPCommunityReadSource",
                  "DeviceRespTime",
                  "DeviceRank",
                  "DeviceConfigLockLastChangeBy",
                  "DeviceConfigLockLastChangedTime",
                  "DeviceConfigLockedInd",
                  "DeviceSNMPPollingInd",
                  "DeviceConfigPollingInd",
                  "DevicePortScanningInd",
                  "DeviceSNMPAnalysisInd",
                  "DeviceFingerPrintInd",
                  "DeviceCCSCollectionInd",
                  "DeviceVendorDefaultCollectionInd",
                  "DeviceStandardsComplianceInd",
                  "DeviceLicensedInd",
                  "DeviceManagedInd",
                  "DeviceNetBIOSScanningInd",
                  "SPMLicensedInd",
                  "ARPCacheRefreshInd",
                  "DeviceCommunitySecure",
                  "DeviceSNMPCommunityReadSecure",
                  "DeviceSNMPCommunityWriteSecure",
                  "DeviceSNMP3AuthPWSecure",
                  "DeviceSNMP3PrivPWSecure",
                  "SecureVersion",
                  "SAMLicensedInd",
                  "DeviceCLIPollingInd",
                  "DevicePerfEnvPollingInd",
                  "DevicePrivilegedPollingInd",
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
        return self.broker.data_source(**{"DeviceID": self.DeviceID})
