from ..broker import Broker


class DeviceSettingBroker(Broker):
    controller = "device_settings"

    def index(self, **kwargs):
        """Lists the available device settings. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSecure: The read operation of each device in SNMP community.
             :type DeviceSNMPCommunityReadSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSecure: The read operation of each device in SNMP community.
             :type DeviceSNMPCommunityReadSecure: Array of String

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

             :param timestamp: The data returned will represent the device settings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device setting methods. The listed methods will be called on each device setting returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceSetting. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return device_settings: An array of the DeviceSetting objects that match the specified input criteria.
             :rtype device_settings: Array of DeviceSetting

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device setting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device setting methods. The listed methods will be called on each device setting returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_setting: The device setting identified by the specified DeviceID.
             :rtype device_setting: DeviceSetting

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device settings matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

             :param DevSetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevSetChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevSetChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevSetEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevSetEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetStartTime: The starting effective time of this record.
             :type DevSetStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetStartTime: The starting effective time of this record.
             :type DevSetStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetTimestamp: The date and time this record was collected or calculated.
             :type DevSetTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevSetTimestamp: The date and time this record was collected or calculated.
             :type DevSetTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCCSCollectionInd: If true, then CCS scripts may be executed against the device.
             :type DeviceCCSCollectionInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCCSCollectionInd: If true, then CCS scripts may be executed against the device.
             :type DeviceCCSCollectionInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCLIPollingInd: If true, than NetMRI CLI polling is enabled for the device.
             :type DeviceCLIPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCLIPollingInd: If true, than NetMRI CLI polling is enabled for the device.
             :type DeviceCLIPollingInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCommunitySecure: The SNMP read community string for the device.
             :type DeviceCommunitySecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCommunitySecure: The SNMP read community string for the device.
             :type DeviceCommunitySecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChangeBy: The user that last changed the configuration locked status of the device.
             :type DeviceConfigLockLastChangeBy: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChangeBy: The user that last changed the configuration locked status of the device.
             :type DeviceConfigLockLastChangeBy: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChangedTime: The date/time of the last change to the configuration locked status of the device.
             :type DeviceConfigLockLastChangedTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChangedTime: The date/time of the last change to the configuration locked status of the device.
             :type DeviceConfigLockLastChangedTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockedInd: If true, then changes detected will be considered unauthorized.
             :type DeviceConfigLockedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockedInd: If true, then changes detected will be considered unauthorized.
             :type DeviceConfigLockedInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigPollingInd: If true, than NetMRI configuration collection is enabled for the device.
             :type DeviceConfigPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigPollingInd: If true, than NetMRI configuration collection is enabled for the device.
             :type DeviceConfigPollingInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFingerPrintInd: If true, then NetMRI fingerprinting is enabled for the device.
             :type DeviceFingerPrintInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFingerPrintInd: If true, then NetMRI fingerprinting is enabled for the device.
             :type DeviceFingerPrintInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceLicensedInd: If true, then this device is licensed as a network device by NetMRI.
             :type DeviceLicensedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceLicensedInd: If true, then this device is licensed as a network device by NetMRI.
             :type DeviceLicensedInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceManagedInd: If true, then this device is managed.
             :type DeviceManagedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceManagedInd: If true, then this device is managed.
             :type DeviceManagedInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceNetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name.
             :type DeviceNetBIOSScanningInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceNetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name.
             :type DeviceNetBIOSScanningInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for this device.
             :type DevicePerfEnvPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for this device.
             :type DevicePerfEnvPollingInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePortScanningInd: If true, than NetMRI port scanning is enabled for the device.
             :type DevicePortScanningInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePortScanningInd: If true, than NetMRI port scanning is enabled for the device.
             :type DevicePortScanningInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device
             :type DevicePrivilegedPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device
             :type DevicePrivilegedPollingInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRank: The device rank as set on the Device Viewer settings screen.
             :type DeviceRank: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRank: The device rank as set on the Device Viewer settings screen.
             :type DeviceRank: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRespTime: The response time of the devices.
             :type DeviceRespTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRespTime: The response time of the devices.
             :type DeviceRespTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3AuthPWSecure: The SNMP3 authentication password of the device.
             :type DeviceSNMP3AuthPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3AuthPWSecure: The SNMP3 authentication password of the device.
             :type DeviceSNMP3AuthPWSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3AuthProto: The SNMP3 authentication protocol of the device.
             :type DeviceSNMP3AuthProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3AuthProto: The SNMP3 authentication protocol of the device.
             :type DeviceSNMP3AuthProto: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3PrivPWSecure: The SNMP3 privilege password of the device.
             :type DeviceSNMP3PrivPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3PrivPWSecure: The SNMP3 privilege password of the device.
             :type DeviceSNMP3PrivPWSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3PrivProto: The SNMP3 privilege protocol of the device.
             :type DeviceSNMP3PrivProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMP3PrivProto: The SNMP3 privilege protocol of the device.
             :type DeviceSNMP3PrivProto: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPAnalysisInd: If true, than NetMRI performs analysis on the device. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type DeviceSNMPAnalysisInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPAnalysisInd: If true, than NetMRI performs analysis on the device. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type DeviceSNMPAnalysisInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSecure: The read operation of each device in SNMP community.
             :type DeviceSNMPCommunityReadSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSecure: The read operation of each device in SNMP community.
             :type DeviceSNMPCommunityReadSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSource: The read source of the SNMP community of devices.
             :type DeviceSNMPCommunityReadSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityReadSource: The read source of the SNMP community of devices.
             :type DeviceSNMPCommunityReadSource: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityWriteSecure: The write operation of each device in SNMP community.
             :type DeviceSNMPCommunityWriteSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPCommunityWriteSecure: The write operation of each device in SNMP community.
             :type DeviceSNMPCommunityWriteSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPPollingInd: If true, than NetMRI SNMP polling is enabled for the device.
             :type DeviceSNMPPollingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPPollingInd: If true, than NetMRI SNMP polling is enabled for the device.
             :type DeviceSNMPPollingInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPTimestamp: The date and time this record was collected or calculated.
             :type DeviceSNMPTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPTimestamp: The date and time this record was collected or calculated.
             :type DeviceSNMPTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPVersion: The SNMP version of the device.
             :type DeviceSNMPVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPVersion: The SNMP version of the device.
             :type DeviceSNMPVersion: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStandardsComplianceInd: If true, than this device should be considered during standards compliance checks.
             :type DeviceStandardsComplianceInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStandardsComplianceInd: If true, than this device should be considered during standards compliance checks.
             :type DeviceStandardsComplianceInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendorDefaultCollectionInd: If true, then NetMRI vendor default credential checking is enabled for the device.
             :type DeviceVendorDefaultCollectionInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendorDefaultCollectionInd: If true, then NetMRI vendor default credential checking is enabled for the device.
             :type DeviceVendorDefaultCollectionInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PolFreqModifier: Polling frequency modifier for this device. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
             :type PolFreqModifier: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PolFreqModifier: Polling frequency modifier for this device. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value.
             :type PolFreqModifier: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SAMLicensedInd: This flag indicating if the Device Security Control enabled.
             :type SAMLicensedInd: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SAMLicensedInd: This flag indicating if the Device Security Control enabled.
             :type SAMLicensedInd: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SPMLicensedInd: A flag indicating if the Device is licensed under the Switch Port Management module.
             :type SPMLicensedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SPMLicensedInd: A flag indicating if the Device is licensed under the Switch Port Management module.
             :type SPMLicensedInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and passwords.
             :type SecureVersion: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and passwords.
             :type SecureVersion: Array of Integer

            |  ``api version min:`` 2.4
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

             :param timestamp: The data returned will represent the device settings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device setting methods. The listed methods will be called on each device setting returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceSetting. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device settings, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ARPCacheRefreshInd, CredentialGroupID, DataSourceID, DevSetChangedCols, DevSetEndTime, DevSetStartTime, DevSetTimestamp, DeviceCCSCollectionInd, DeviceCLIPollingInd, DeviceCommunitySecure, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DeviceConfigPollingInd, DeviceFingerPrintInd, DeviceID, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, DevicePortScanningInd, DevicePrivilegedPollingInd, DeviceRank, DeviceRespTime, DeviceSNMP3AuthPWSecure, DeviceSNMP3AuthProto, DeviceSNMP3PrivPWSecure, DeviceSNMP3PrivProto, DeviceSNMPAnalysisInd, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityReadSource, DeviceSNMPCommunityWriteSecure, DeviceSNMPPollingInd, DeviceSNMPTimestamp, DeviceSNMPVersion, DeviceStandardsComplianceInd, DeviceVendorDefaultCollectionInd, PolFreqModifier, SAMLicensedInd, SPMLicensedInd, SecureVersion, UseGlobalPolFreq.
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

             :return device_settings: An array of the DeviceSetting objects that match the specified input criteria.
             :rtype device_settings: Array of DeviceSetting

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device settings matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ARPCacheRefreshInd, CredentialGroupID, DataSourceID, DevSetChangedCols, DevSetEndTime, DevSetStartTime, DevSetTimestamp, DeviceCCSCollectionInd, DeviceCLIPollingInd, DeviceCommunitySecure, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DeviceConfigPollingInd, DeviceFingerPrintInd, DeviceID, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, DevicePortScanningInd, DevicePrivilegedPollingInd, DeviceRank, DeviceRespTime, DeviceSNMP3AuthPWSecure, DeviceSNMP3AuthProto, DeviceSNMP3PrivPWSecure, DeviceSNMP3PrivProto, DeviceSNMPAnalysisInd, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityReadSource, DeviceSNMPCommunityWriteSecure, DeviceSNMPPollingInd, DeviceSNMPTimestamp, DeviceSNMPVersion, DeviceStandardsComplianceInd, DeviceVendorDefaultCollectionInd, PolFreqModifier, SAMLicensedInd, SPMLicensedInd, SecureVersion, UseGlobalPolFreq.

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

             :param op_DevSetChangedCols: The operator to apply to the field DevSetChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevSetChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevSetChangedCols: If op_DevSetChangedCols is specified, the field named in this input will be compared to the value in DevSetChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevSetChangedCols must be specified if op_DevSetChangedCols is specified.
             :type val_f_DevSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevSetChangedCols: If op_DevSetChangedCols is specified, this value will be compared to the value in DevSetChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevSetChangedCols must be specified if op_DevSetChangedCols is specified.
             :type val_c_DevSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevSetEndTime: The operator to apply to the field DevSetEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevSetEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevSetEndTime: If op_DevSetEndTime is specified, the field named in this input will be compared to the value in DevSetEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevSetEndTime must be specified if op_DevSetEndTime is specified.
             :type val_f_DevSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevSetEndTime: If op_DevSetEndTime is specified, this value will be compared to the value in DevSetEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevSetEndTime must be specified if op_DevSetEndTime is specified.
             :type val_c_DevSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevSetStartTime: The operator to apply to the field DevSetStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevSetStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevSetStartTime: If op_DevSetStartTime is specified, the field named in this input will be compared to the value in DevSetStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevSetStartTime must be specified if op_DevSetStartTime is specified.
             :type val_f_DevSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevSetStartTime: If op_DevSetStartTime is specified, this value will be compared to the value in DevSetStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevSetStartTime must be specified if op_DevSetStartTime is specified.
             :type val_c_DevSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevSetTimestamp: The operator to apply to the field DevSetTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevSetTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevSetTimestamp: If op_DevSetTimestamp is specified, the field named in this input will be compared to the value in DevSetTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevSetTimestamp must be specified if op_DevSetTimestamp is specified.
             :type val_f_DevSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevSetTimestamp: If op_DevSetTimestamp is specified, this value will be compared to the value in DevSetTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevSetTimestamp must be specified if op_DevSetTimestamp is specified.
             :type val_c_DevSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceCCSCollectionInd: The operator to apply to the field DeviceCCSCollectionInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCCSCollectionInd: If true, then CCS scripts may be executed against the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCCSCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCCSCollectionInd: If op_DeviceCCSCollectionInd is specified, the field named in this input will be compared to the value in DeviceCCSCollectionInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCCSCollectionInd must be specified if op_DeviceCCSCollectionInd is specified.
             :type val_f_DeviceCCSCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCCSCollectionInd: If op_DeviceCCSCollectionInd is specified, this value will be compared to the value in DeviceCCSCollectionInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCCSCollectionInd must be specified if op_DeviceCCSCollectionInd is specified.
             :type val_c_DeviceCCSCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceCLIPollingInd: The operator to apply to the field DeviceCLIPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCLIPollingInd: If true, than NetMRI CLI polling is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCLIPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCLIPollingInd: If op_DeviceCLIPollingInd is specified, the field named in this input will be compared to the value in DeviceCLIPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCLIPollingInd must be specified if op_DeviceCLIPollingInd is specified.
             :type val_f_DeviceCLIPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCLIPollingInd: If op_DeviceCLIPollingInd is specified, this value will be compared to the value in DeviceCLIPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCLIPollingInd must be specified if op_DeviceCLIPollingInd is specified.
             :type val_c_DeviceCLIPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceCommunitySecure: The operator to apply to the field DeviceCommunitySecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCommunitySecure: The SNMP read community string for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCommunitySecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCommunitySecure: If op_DeviceCommunitySecure is specified, the field named in this input will be compared to the value in DeviceCommunitySecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCommunitySecure must be specified if op_DeviceCommunitySecure is specified.
             :type val_f_DeviceCommunitySecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCommunitySecure: If op_DeviceCommunitySecure is specified, this value will be compared to the value in DeviceCommunitySecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCommunitySecure must be specified if op_DeviceCommunitySecure is specified.
             :type val_c_DeviceCommunitySecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigLockLastChangeBy: The operator to apply to the field DeviceConfigLockLastChangeBy. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLockLastChangeBy: The user that last changed the configuration locked status of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLockLastChangeBy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLockLastChangeBy: If op_DeviceConfigLockLastChangeBy is specified, the field named in this input will be compared to the value in DeviceConfigLockLastChangeBy using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLockLastChangeBy must be specified if op_DeviceConfigLockLastChangeBy is specified.
             :type val_f_DeviceConfigLockLastChangeBy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLockLastChangeBy: If op_DeviceConfigLockLastChangeBy is specified, this value will be compared to the value in DeviceConfigLockLastChangeBy using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLockLastChangeBy must be specified if op_DeviceConfigLockLastChangeBy is specified.
             :type val_c_DeviceConfigLockLastChangeBy: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigLockLastChangedTime: The operator to apply to the field DeviceConfigLockLastChangedTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLockLastChangedTime: The date/time of the last change to the configuration locked status of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLockLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLockLastChangedTime: If op_DeviceConfigLockLastChangedTime is specified, the field named in this input will be compared to the value in DeviceConfigLockLastChangedTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLockLastChangedTime must be specified if op_DeviceConfigLockLastChangedTime is specified.
             :type val_f_DeviceConfigLockLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLockLastChangedTime: If op_DeviceConfigLockLastChangedTime is specified, this value will be compared to the value in DeviceConfigLockLastChangedTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLockLastChangedTime must be specified if op_DeviceConfigLockLastChangedTime is specified.
             :type val_c_DeviceConfigLockLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigLockedInd: The operator to apply to the field DeviceConfigLockedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLockedInd: If true, then changes detected will be considered unauthorized. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLockedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLockedInd: If op_DeviceConfigLockedInd is specified, the field named in this input will be compared to the value in DeviceConfigLockedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLockedInd must be specified if op_DeviceConfigLockedInd is specified.
             :type val_f_DeviceConfigLockedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLockedInd: If op_DeviceConfigLockedInd is specified, this value will be compared to the value in DeviceConfigLockedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLockedInd must be specified if op_DeviceConfigLockedInd is specified.
             :type val_c_DeviceConfigLockedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigPollingInd: The operator to apply to the field DeviceConfigPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigPollingInd: If true, than NetMRI configuration collection is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigPollingInd: If op_DeviceConfigPollingInd is specified, the field named in this input will be compared to the value in DeviceConfigPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigPollingInd must be specified if op_DeviceConfigPollingInd is specified.
             :type val_f_DeviceConfigPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigPollingInd: If op_DeviceConfigPollingInd is specified, this value will be compared to the value in DeviceConfigPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigPollingInd must be specified if op_DeviceConfigPollingInd is specified.
             :type val_c_DeviceConfigPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFingerPrintInd: The operator to apply to the field DeviceFingerPrintInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFingerPrintInd: If true, then NetMRI fingerprinting is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFingerPrintInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFingerPrintInd: If op_DeviceFingerPrintInd is specified, the field named in this input will be compared to the value in DeviceFingerPrintInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFingerPrintInd must be specified if op_DeviceFingerPrintInd is specified.
             :type val_f_DeviceFingerPrintInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFingerPrintInd: If op_DeviceFingerPrintInd is specified, this value will be compared to the value in DeviceFingerPrintInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFingerPrintInd must be specified if op_DeviceFingerPrintInd is specified.
             :type val_c_DeviceFingerPrintInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which device setting was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceLicensedInd: The operator to apply to the field DeviceLicensedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceLicensedInd: If true, then this device is licensed as a network device by NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceLicensedInd: If op_DeviceLicensedInd is specified, the field named in this input will be compared to the value in DeviceLicensedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceLicensedInd must be specified if op_DeviceLicensedInd is specified.
             :type val_f_DeviceLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceLicensedInd: If op_DeviceLicensedInd is specified, this value will be compared to the value in DeviceLicensedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceLicensedInd must be specified if op_DeviceLicensedInd is specified.
             :type val_c_DeviceLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceManagedInd: The operator to apply to the field DeviceManagedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceManagedInd: If true, then this device is managed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceManagedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceManagedInd: If op_DeviceManagedInd is specified, the field named in this input will be compared to the value in DeviceManagedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceManagedInd must be specified if op_DeviceManagedInd is specified.
             :type val_f_DeviceManagedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceManagedInd: If op_DeviceManagedInd is specified, this value will be compared to the value in DeviceManagedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceManagedInd must be specified if op_DeviceManagedInd is specified.
             :type val_c_DeviceManagedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceNetBIOSScanningInd: The operator to apply to the field DeviceNetBIOSScanningInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceNetBIOSScanningInd: A flag indicating if NetMRI scans for the NetBIOS name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceNetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceNetBIOSScanningInd: If op_DeviceNetBIOSScanningInd is specified, the field named in this input will be compared to the value in DeviceNetBIOSScanningInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceNetBIOSScanningInd must be specified if op_DeviceNetBIOSScanningInd is specified.
             :type val_f_DeviceNetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceNetBIOSScanningInd: If op_DeviceNetBIOSScanningInd is specified, this value will be compared to the value in DeviceNetBIOSScanningInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceNetBIOSScanningInd must be specified if op_DeviceNetBIOSScanningInd is specified.
             :type val_c_DeviceNetBIOSScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePerfEnvPollingInd: The operator to apply to the field DevicePerfEnvPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePerfEnvPollingInd: A flag that indicates if Performance and Environment polling is enabled for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePerfEnvPollingInd: If op_DevicePerfEnvPollingInd is specified, the field named in this input will be compared to the value in DevicePerfEnvPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePerfEnvPollingInd must be specified if op_DevicePerfEnvPollingInd is specified.
             :type val_f_DevicePerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePerfEnvPollingInd: If op_DevicePerfEnvPollingInd is specified, this value will be compared to the value in DevicePerfEnvPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePerfEnvPollingInd must be specified if op_DevicePerfEnvPollingInd is specified.
             :type val_c_DevicePerfEnvPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePortScanningInd: The operator to apply to the field DevicePortScanningInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePortScanningInd: If true, than NetMRI port scanning is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePortScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePortScanningInd: If op_DevicePortScanningInd is specified, the field named in this input will be compared to the value in DevicePortScanningInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePortScanningInd must be specified if op_DevicePortScanningInd is specified.
             :type val_f_DevicePortScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePortScanningInd: If op_DevicePortScanningInd is specified, this value will be compared to the value in DevicePortScanningInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePortScanningInd must be specified if op_DevicePortScanningInd is specified.
             :type val_c_DevicePortScanningInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePrivilegedPollingInd: The operator to apply to the field DevicePrivilegedPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePrivilegedPollingInd: A flag indicated that NetMRI should send enable command when interacting with device For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePrivilegedPollingInd: If op_DevicePrivilegedPollingInd is specified, the field named in this input will be compared to the value in DevicePrivilegedPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePrivilegedPollingInd must be specified if op_DevicePrivilegedPollingInd is specified.
             :type val_f_DevicePrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePrivilegedPollingInd: If op_DevicePrivilegedPollingInd is specified, this value will be compared to the value in DevicePrivilegedPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePrivilegedPollingInd must be specified if op_DevicePrivilegedPollingInd is specified.
             :type val_c_DevicePrivilegedPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceRank: The operator to apply to the field DeviceRank. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRank: The device rank as set on the Device Viewer settings screen. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRank: If op_DeviceRank is specified, the field named in this input will be compared to the value in DeviceRank using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRank must be specified if op_DeviceRank is specified.
             :type val_f_DeviceRank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRank: If op_DeviceRank is specified, this value will be compared to the value in DeviceRank using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRank must be specified if op_DeviceRank is specified.
             :type val_c_DeviceRank: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceRespTime: The operator to apply to the field DeviceRespTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRespTime: The response time of the devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRespTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRespTime: If op_DeviceRespTime is specified, the field named in this input will be compared to the value in DeviceRespTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRespTime must be specified if op_DeviceRespTime is specified.
             :type val_f_DeviceRespTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRespTime: If op_DeviceRespTime is specified, this value will be compared to the value in DeviceRespTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRespTime must be specified if op_DeviceRespTime is specified.
             :type val_c_DeviceRespTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMP3AuthPWSecure: The operator to apply to the field DeviceSNMP3AuthPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMP3AuthPWSecure: The SNMP3 authentication password of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMP3AuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMP3AuthPWSecure: If op_DeviceSNMP3AuthPWSecure is specified, the field named in this input will be compared to the value in DeviceSNMP3AuthPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMP3AuthPWSecure must be specified if op_DeviceSNMP3AuthPWSecure is specified.
             :type val_f_DeviceSNMP3AuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMP3AuthPWSecure: If op_DeviceSNMP3AuthPWSecure is specified, this value will be compared to the value in DeviceSNMP3AuthPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMP3AuthPWSecure must be specified if op_DeviceSNMP3AuthPWSecure is specified.
             :type val_c_DeviceSNMP3AuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMP3AuthProto: The operator to apply to the field DeviceSNMP3AuthProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMP3AuthProto: The SNMP3 authentication protocol of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMP3AuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMP3AuthProto: If op_DeviceSNMP3AuthProto is specified, the field named in this input will be compared to the value in DeviceSNMP3AuthProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMP3AuthProto must be specified if op_DeviceSNMP3AuthProto is specified.
             :type val_f_DeviceSNMP3AuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMP3AuthProto: If op_DeviceSNMP3AuthProto is specified, this value will be compared to the value in DeviceSNMP3AuthProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMP3AuthProto must be specified if op_DeviceSNMP3AuthProto is specified.
             :type val_c_DeviceSNMP3AuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMP3PrivPWSecure: The operator to apply to the field DeviceSNMP3PrivPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMP3PrivPWSecure: The SNMP3 privilege password of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMP3PrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMP3PrivPWSecure: If op_DeviceSNMP3PrivPWSecure is specified, the field named in this input will be compared to the value in DeviceSNMP3PrivPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMP3PrivPWSecure must be specified if op_DeviceSNMP3PrivPWSecure is specified.
             :type val_f_DeviceSNMP3PrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMP3PrivPWSecure: If op_DeviceSNMP3PrivPWSecure is specified, this value will be compared to the value in DeviceSNMP3PrivPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMP3PrivPWSecure must be specified if op_DeviceSNMP3PrivPWSecure is specified.
             :type val_c_DeviceSNMP3PrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMP3PrivProto: The operator to apply to the field DeviceSNMP3PrivProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMP3PrivProto: The SNMP3 privilege protocol of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMP3PrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMP3PrivProto: If op_DeviceSNMP3PrivProto is specified, the field named in this input will be compared to the value in DeviceSNMP3PrivProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMP3PrivProto must be specified if op_DeviceSNMP3PrivProto is specified.
             :type val_f_DeviceSNMP3PrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMP3PrivProto: If op_DeviceSNMP3PrivProto is specified, this value will be compared to the value in DeviceSNMP3PrivProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMP3PrivProto must be specified if op_DeviceSNMP3PrivProto is specified.
             :type val_c_DeviceSNMP3PrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPAnalysisInd: The operator to apply to the field DeviceSNMPAnalysisInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPAnalysisInd: If true, than NetMRI performs analysis on the device. NOTE: Despite the 'SNMP' in the name, this represents all analysis. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPAnalysisInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPAnalysisInd: If op_DeviceSNMPAnalysisInd is specified, the field named in this input will be compared to the value in DeviceSNMPAnalysisInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPAnalysisInd must be specified if op_DeviceSNMPAnalysisInd is specified.
             :type val_f_DeviceSNMPAnalysisInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPAnalysisInd: If op_DeviceSNMPAnalysisInd is specified, this value will be compared to the value in DeviceSNMPAnalysisInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPAnalysisInd must be specified if op_DeviceSNMPAnalysisInd is specified.
             :type val_c_DeviceSNMPAnalysisInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPCommunityReadSecure: The operator to apply to the field DeviceSNMPCommunityReadSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPCommunityReadSecure: The read operation of each device in SNMP community. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPCommunityReadSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPCommunityReadSecure: If op_DeviceSNMPCommunityReadSecure is specified, the field named in this input will be compared to the value in DeviceSNMPCommunityReadSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPCommunityReadSecure must be specified if op_DeviceSNMPCommunityReadSecure is specified.
             :type val_f_DeviceSNMPCommunityReadSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPCommunityReadSecure: If op_DeviceSNMPCommunityReadSecure is specified, this value will be compared to the value in DeviceSNMPCommunityReadSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPCommunityReadSecure must be specified if op_DeviceSNMPCommunityReadSecure is specified.
             :type val_c_DeviceSNMPCommunityReadSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPCommunityReadSource: The operator to apply to the field DeviceSNMPCommunityReadSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPCommunityReadSource: The read source of the SNMP community of devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPCommunityReadSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPCommunityReadSource: If op_DeviceSNMPCommunityReadSource is specified, the field named in this input will be compared to the value in DeviceSNMPCommunityReadSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPCommunityReadSource must be specified if op_DeviceSNMPCommunityReadSource is specified.
             :type val_f_DeviceSNMPCommunityReadSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPCommunityReadSource: If op_DeviceSNMPCommunityReadSource is specified, this value will be compared to the value in DeviceSNMPCommunityReadSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPCommunityReadSource must be specified if op_DeviceSNMPCommunityReadSource is specified.
             :type val_c_DeviceSNMPCommunityReadSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPCommunityWriteSecure: The operator to apply to the field DeviceSNMPCommunityWriteSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPCommunityWriteSecure: The write operation of each device in SNMP community. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPCommunityWriteSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPCommunityWriteSecure: If op_DeviceSNMPCommunityWriteSecure is specified, the field named in this input will be compared to the value in DeviceSNMPCommunityWriteSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPCommunityWriteSecure must be specified if op_DeviceSNMPCommunityWriteSecure is specified.
             :type val_f_DeviceSNMPCommunityWriteSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPCommunityWriteSecure: If op_DeviceSNMPCommunityWriteSecure is specified, this value will be compared to the value in DeviceSNMPCommunityWriteSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPCommunityWriteSecure must be specified if op_DeviceSNMPCommunityWriteSecure is specified.
             :type val_c_DeviceSNMPCommunityWriteSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPPollingInd: The operator to apply to the field DeviceSNMPPollingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPPollingInd: If true, than NetMRI SNMP polling is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPPollingInd: If op_DeviceSNMPPollingInd is specified, the field named in this input will be compared to the value in DeviceSNMPPollingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPPollingInd must be specified if op_DeviceSNMPPollingInd is specified.
             :type val_f_DeviceSNMPPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPPollingInd: If op_DeviceSNMPPollingInd is specified, this value will be compared to the value in DeviceSNMPPollingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPPollingInd must be specified if op_DeviceSNMPPollingInd is specified.
             :type val_c_DeviceSNMPPollingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPTimestamp: The operator to apply to the field DeviceSNMPTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPTimestamp: If op_DeviceSNMPTimestamp is specified, the field named in this input will be compared to the value in DeviceSNMPTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPTimestamp must be specified if op_DeviceSNMPTimestamp is specified.
             :type val_f_DeviceSNMPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPTimestamp: If op_DeviceSNMPTimestamp is specified, this value will be compared to the value in DeviceSNMPTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPTimestamp must be specified if op_DeviceSNMPTimestamp is specified.
             :type val_c_DeviceSNMPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPVersion: The operator to apply to the field DeviceSNMPVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPVersion: The SNMP version of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPVersion: If op_DeviceSNMPVersion is specified, the field named in this input will be compared to the value in DeviceSNMPVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPVersion must be specified if op_DeviceSNMPVersion is specified.
             :type val_f_DeviceSNMPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPVersion: If op_DeviceSNMPVersion is specified, this value will be compared to the value in DeviceSNMPVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPVersion must be specified if op_DeviceSNMPVersion is specified.
             :type val_c_DeviceSNMPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceStandardsComplianceInd: The operator to apply to the field DeviceStandardsComplianceInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceStandardsComplianceInd: If true, than this device should be considered during standards compliance checks. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceStandardsComplianceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceStandardsComplianceInd: If op_DeviceStandardsComplianceInd is specified, the field named in this input will be compared to the value in DeviceStandardsComplianceInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceStandardsComplianceInd must be specified if op_DeviceStandardsComplianceInd is specified.
             :type val_f_DeviceStandardsComplianceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceStandardsComplianceInd: If op_DeviceStandardsComplianceInd is specified, this value will be compared to the value in DeviceStandardsComplianceInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceStandardsComplianceInd must be specified if op_DeviceStandardsComplianceInd is specified.
             :type val_c_DeviceStandardsComplianceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceVendorDefaultCollectionInd: The operator to apply to the field DeviceVendorDefaultCollectionInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceVendorDefaultCollectionInd: If true, then NetMRI vendor default credential checking is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceVendorDefaultCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceVendorDefaultCollectionInd: If op_DeviceVendorDefaultCollectionInd is specified, the field named in this input will be compared to the value in DeviceVendorDefaultCollectionInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceVendorDefaultCollectionInd must be specified if op_DeviceVendorDefaultCollectionInd is specified.
             :type val_f_DeviceVendorDefaultCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceVendorDefaultCollectionInd: If op_DeviceVendorDefaultCollectionInd is specified, this value will be compared to the value in DeviceVendorDefaultCollectionInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceVendorDefaultCollectionInd must be specified if op_DeviceVendorDefaultCollectionInd is specified.
             :type val_c_DeviceVendorDefaultCollectionInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PolFreqModifier: The operator to apply to the field PolFreqModifier. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PolFreqModifier: Polling frequency modifier for this device. Actual polling frequency intervals for the device are calculated by multiplying the default intervals by this value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SAMLicensedInd: The operator to apply to the field SAMLicensedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SAMLicensedInd: This flag indicating if the Device Security Control enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SPMLicensedInd: The operator to apply to the field SPMLicensedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SPMLicensedInd: A flag indicating if the Device is licensed under the Switch Port Management module. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SPMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SPMLicensedInd: If op_SPMLicensedInd is specified, the field named in this input will be compared to the value in SPMLicensedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SPMLicensedInd must be specified if op_SPMLicensedInd is specified.
             :type val_f_SPMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SPMLicensedInd: If op_SPMLicensedInd is specified, this value will be compared to the value in SPMLicensedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SPMLicensedInd must be specified if op_SPMLicensedInd is specified.
             :type val_c_SPMLicensedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SecureVersion: The operator to apply to the field SecureVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SecureVersion: The encryption version of the username and passwords. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SecureVersion: If op_SecureVersion is specified, the field named in this input will be compared to the value in SecureVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_f_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SecureVersion: If op_SecureVersion is specified, this value will be compared to the value in SecureVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_c_SecureVersion: String

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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device settings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device setting methods. The listed methods will be called on each device setting returned and included in the output. Available methods are: data_source.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID.
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

             :param select: The list of attributes to return for each DeviceSetting. Valid values are DataSourceID, DeviceID, DevSetStartTime, DevSetEndTime, DevSetChangedCols, DevSetTimestamp, DeviceSNMPVersion, DeviceSNMP3AuthProto, DeviceSNMP3PrivProto, DeviceSNMPTimestamp, DeviceSNMPCommunityReadSource, DeviceRespTime, DeviceRank, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChangedTime, DeviceConfigLockedInd, DevicePrivilegedPollingInd, DeviceSNMPPollingInd, DeviceCLIPollingInd, DeviceConfigPollingInd, DevicePortScanningInd, DeviceSNMPAnalysisInd, DeviceFingerPrintInd, DeviceCCSCollectionInd, DeviceVendorDefaultCollectionInd, DeviceStandardsComplianceInd, DeviceLicensedInd, DeviceManagedInd, DeviceNetBIOSScanningInd, DevicePerfEnvPollingInd, SPMLicensedInd, ARPCacheRefreshInd, DeviceCommunitySecure, DeviceSNMPCommunityReadSecure, DeviceSNMPCommunityWriteSecure, DeviceSNMP3AuthPWSecure, DeviceSNMP3PrivPWSecure, SecureVersion, SAMLicensedInd, UseGlobalPolFreq, PolFreqModifier, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return device_settings: An array of the DeviceSetting objects that match the specified input criteria.
             :rtype device_settings: Array of DeviceSetting

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which device setting was collected.
             :type DeviceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)
