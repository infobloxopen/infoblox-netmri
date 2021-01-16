from ..broker import Broker


class DeviceBroker(Broker):
    controller = "devices"

    def index(self, **kwargs):
        """Lists the available devices. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: No description is available for DeviceFirstOccurrenceTime.
             :type DeviceFirstOccurrenceTime: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: No description is available for DeviceFirstOccurrenceTime.
             :type DeviceFirstOccurrenceTime: Array of String

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
             :type DeviceIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
             :type DeviceIPDotted: Array of String

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPNumeric: The numerical value of the device IP address.
             :type DeviceIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPNumeric: The numerical value of the device IP address.
             :type DeviceIPNumeric: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceMAC: The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
             :type DeviceMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceMAC: The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
             :type DeviceMAC: Array of String

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
             :type DeviceName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
             :type DeviceName: Array of String

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceID: The internal NetMRI identifier for the device containing this virtual device.
             :type ParentDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceID: The internal NetMRI identifier for the device containing this virtual device.
             :type ParentDeviceID: Array of Integer

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

             :param timestamp: The data returned will represent the devices as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device methods. The listed methods will be called on each device returned and included in the output. Available methods are: data_source.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceCommunity, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceDNSName, DeviceSNMPPolling, DeviceConfigPolling, DevicePortScanning, DeviceSNMPAnalysis, DeviceFingerPrint, DeviceCCSCollection, DeviceVendorDefaultCollection, DeviceConfigTimestamp, DeviceFirstOccurrence, DeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSavedConfigLastChange, DeviceConfigLocked, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChange, DeviceConfigLastChecked, DeviceLicensed, DevicePolicyScheduleMode, NetworkDeviceInd, RoutingInd, SwitchingInd, DeviceRank, DeviceAddlInfo, DeviceMAC, DeviceStandardsCompliance, ParentDeviceID, DeviceContextName, VirtualInd, DeviceSysContact, DeviceManagedInd, SPMLicensedInd, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, ARPCacheRefreshInd, FilteringInd.
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

             :param select: The list of attributes to return for each Device. Valid values are DataSourceID, DeviceID, DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceCommunity, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceDNSName, DeviceSNMPPolling, DeviceConfigPolling, DevicePortScanning, DeviceSNMPAnalysis, DeviceFingerPrint, DeviceCCSCollection, DeviceVendorDefaultCollection, DeviceConfigTimestamp, DeviceFirstOccurrence, DeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSavedConfigLastChange, DeviceConfigLocked, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChange, DeviceConfigLastChecked, DeviceLicensed, DevicePolicyScheduleMode, NetworkDeviceInd, RoutingInd, SwitchingInd, DeviceRank, DeviceAddlInfo, DeviceMAC, DeviceStandardsCompliance, ParentDeviceID, DeviceContextName, VirtualInd, DeviceSysContact, DeviceManagedInd, SPMLicensedInd, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, ARPCacheRefreshInd, FilteringInd. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkID: The network id to which results would be limited.
             :type NetworkID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return devices: An array of the Device objects that match the specified input criteria.
             :rtype devices: Array of DeviceConfig

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available devices matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceAddlInfo: Additional information about the device; IP phones will contain the extension in this field.
             :type DeviceAddlInfo: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceAddlInfo: Additional information about the device; IP phones will contain the extension in this field.
             :type DeviceAddlInfo: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceAssurance: The assurance level of the device type value.
             :type DeviceAssurance: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceAssurance: The assurance level of the device type value.
             :type DeviceAssurance: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCCSCollection: If "on", then CCS scripts may be executed against the device.
             :type DeviceCCSCollection: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCCSCollection: If "on", then CCS scripts may be executed against the device.
             :type DeviceCCSCollection: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceChangedCols: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCommunity: The SNMP read community string for the device.
             :type DeviceCommunity: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceCommunity: The SNMP read community string for the device.
             :type DeviceCommunity: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLastChecked: The date/time of the last attempted retrieval of the device's configuration file.
             :type DeviceConfigLastChecked: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLastChecked: The date/time of the last attempted retrieval of the device's configuration file.
             :type DeviceConfigLastChecked: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChange: The date/time of the last change to the configuration locked status of the device.
             :type DeviceConfigLockLastChange: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLockLastChange: The date/time of the last change to the configuration locked status of the device.
             :type DeviceConfigLockLastChange: Array of DateTime

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLocked: If 1, then changes detected will be considered unauthorized.
             :type DeviceConfigLocked: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLocked: If 1, then changes detected will be considered unauthorized.
             :type DeviceConfigLocked: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigPolling: on if NetMRI configuration collection is enabled for the device; off otherwise.
             :type DeviceConfigPolling: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigPolling: on if NetMRI configuration collection is enabled for the device; off otherwise.
             :type DeviceConfigPolling: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigTimestamp: The date/time the configuration file was last successfully retrieved for this device.
             :type DeviceConfigTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigTimestamp: The date/time the configuration file was last successfully retrieved for this device.
             :type DeviceConfigTimestamp: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceContextName: The name of the virtual context of this virtual device.
             :type DeviceContextName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceContextName: The name of the virtual context of this virtual device.
             :type DeviceContextName: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceDNSName: The device name as reported by DNS.
             :type DeviceDNSName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceDNSName: The device name as reported by DNS.
             :type DeviceDNSName: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DeviceEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DeviceEndTime: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFingerPrint: If "on", then NetMRI fingerprinting is enabled for the device.
             :type DeviceFingerPrint: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFingerPrint: If "on", then NetMRI fingerprinting is enabled for the device.
             :type DeviceFingerPrint: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrence: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrence: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrence: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrence: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
             :type DeviceIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
             :type DeviceIPDotted: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPNumeric: The numerical value of the device IP address.
             :type DeviceIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPNumeric: The numerical value of the device IP address.
             :type DeviceIPNumeric: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceLicensed: If 1, then this device is licensed as a network device by NetMRI.
             :type DeviceLicensed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceLicensed: If 1, then this device is licensed as a network device by NetMRI.
             :type DeviceLicensed: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceMAC: The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
             :type DeviceMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceMAC: The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
             :type DeviceMAC: Array of String

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceModel: The device model name.
             :type DeviceModel: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceModel: The device model name.
             :type DeviceModel: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
             :type DeviceName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
             :type DeviceName: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceNetBIOSName: The NetBIOS name of the device.
             :type DeviceNetBIOSName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceNetBIOSName: The NetBIOS name of the device.
             :type DeviceNetBIOSName: Array of String

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceOUI: The NetMRI-determined device vendor using OUI.
             :type DeviceOUI: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceOUI: The NetMRI-determined device vendor using OUI.
             :type DeviceOUI: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyScheduleMode: Not currently used.
             :type DevicePolicyScheduleMode: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePolicyScheduleMode: Not currently used.
             :type DevicePolicyScheduleMode: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePortScanning: on if NetMRI port scanning is enabled for the device; off otherwise.
             :type DevicePortScanning: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePortScanning: on if NetMRI port scanning is enabled for the device; off otherwise.
             :type DevicePortScanning: Array of String

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRebootTime: The date/time this device was last rebooted.
             :type DeviceRebootTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRebootTime: The date/time this device was last rebooted.
             :type DeviceRebootTime: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRunningConfigLastChange: The date/time, as reported by SNMP, that the device's running configuration was last changed.
             :type DeviceRunningConfigLastChange: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRunningConfigLastChange: The date/time, as reported by SNMP, that the device's running configuration was last changed.
             :type DeviceRunningConfigLastChange: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSAAVersion: The SAA version running on this device.
             :type DeviceSAAVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSAAVersion: The SAA version running on this device.
             :type DeviceSAAVersion: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPAnalysis: on if NetMRI performs analysis on the device; off otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type DeviceSNMPAnalysis: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPAnalysis: on if NetMRI performs analysis on the device; off otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis.
             :type DeviceSNMPAnalysis: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPPolling: on if NetMRI SNMP polling is enabled for the device; off otherwise.
             :type DeviceSNMPPolling: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSNMPPolling: on if NetMRI SNMP polling is enabled for the device; off otherwise.
             :type DeviceSNMPPolling: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSavedConfigLastChange: The date/time, as reported by SNMP, that the device's saved configuration was last changed.
             :type DeviceSavedConfigLastChange: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSavedConfigLastChange: The date/time, as reported by SNMP, that the device's saved configuration was last changed.
             :type DeviceSavedConfigLastChange: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStandardsCompliance: on if this device should be considered during standards compliance checks, "off" otherwise.
             :type DeviceStandardsCompliance: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStandardsCompliance: on if this device should be considered during standards compliance checks, "off" otherwise.
             :type DeviceStandardsCompliance: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStartTime: The starting effective time of this revision of the record.
             :type DeviceStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceStartTime: The starting effective time of this revision of the record.
             :type DeviceStartTime: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysContact: The Device sysContact as reported by SNMP.
             :type DeviceSysContact: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysContact: The Device sysContact as reported by SNMP.
             :type DeviceSysContact: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysDescr: The device sysDescr as reported by SNMP.
             :type DeviceSysDescr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysDescr: The device sysDescr as reported by SNMP.
             :type DeviceSysDescr: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysLocation: The device sysLocation as reported by SNMP.
             :type DeviceSysLocation: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysLocation: The device sysLocation as reported by SNMP.
             :type DeviceSysLocation: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysName: The device name as reported by SNMP.
             :type DeviceSysName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSysName: The device name as reported by SNMP.
             :type DeviceSysName: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceTimestamp: The date and time this record was collected.
             :type DeviceTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceTimestamp: The date and time this record was collected.
             :type DeviceTimestamp: Array of DateTime

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceType: The NetMRI-determined device type.
             :type DeviceType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceType: The NetMRI-determined device type.
             :type DeviceType: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendor: The device vendor name.
             :type DeviceVendor: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendor: The device vendor name.
             :type DeviceVendor: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendorDefaultCollection: If "on", then NetMRI vendor default credential checking is enabled for the device.
             :type DeviceVendorDefaultCollection: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVendorDefaultCollection: If "on", then NetMRI vendor default credential checking is enabled for the device.
             :type DeviceVendorDefaultCollection: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVersion: The device OS version.
             :type DeviceVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceVersion: The device OS version.
             :type DeviceVersion: Array of String

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FilteringInd: A flag indicating whether this device is eligible for Security Device Controller
             :type FilteringInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilteringInd: A flag indicating whether this device is eligible for Security Device Controller
             :type FilteringInd: Array of Boolean

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkDeviceInd: A flag indicating whether this device is a network device or an end host.
             :type NetworkDeviceInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkDeviceInd: A flag indicating whether this device is a network device or an end host.
             :type NetworkDeviceInd: Array of Boolean

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceID: The internal NetMRI identifier for the device containing this virtual device.
             :type ParentDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceID: The internal NetMRI identifier for the device containing this virtual device.
             :type ParentDeviceID: Array of Integer

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingInd: A flag indicating whether this device is configured with any routing capability and whether a routing table was retrieved from this device.
             :type RoutingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RoutingInd: A flag indicating whether this device is configured with any routing capability and whether a routing table was retrieved from this device.
             :type RoutingInd: Array of Boolean

            |  ``api version min:`` 2.2
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

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchingInd: A flag indicating whether a switch port forwarding table was retrieved from this device.
             :type SwitchingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchingInd: A flag indicating whether a switch port forwarding table was retrieved from this device.
             :type SwitchingInd: Array of Boolean

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualInd: A flag indicating if the source device is a virtual device.
             :type VirtualInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualInd: A flag indicating if the source device is a virtual device.
             :type VirtualInd: Array of Boolean

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

             :param timestamp: The data returned will represent the devices as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device methods. The listed methods will be called on each device returned and included in the output. Available methods are: data_source.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceCommunity, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceDNSName, DeviceSNMPPolling, DeviceConfigPolling, DevicePortScanning, DeviceSNMPAnalysis, DeviceFingerPrint, DeviceCCSCollection, DeviceVendorDefaultCollection, DeviceConfigTimestamp, DeviceFirstOccurrence, DeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSavedConfigLastChange, DeviceConfigLocked, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChange, DeviceConfigLastChecked, DeviceLicensed, DevicePolicyScheduleMode, NetworkDeviceInd, RoutingInd, SwitchingInd, DeviceRank, DeviceAddlInfo, DeviceMAC, DeviceStandardsCompliance, ParentDeviceID, DeviceContextName, VirtualInd, DeviceSysContact, DeviceManagedInd, SPMLicensedInd, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, ARPCacheRefreshInd, FilteringInd.
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

             :param select: The list of attributes to return for each Device. Valid values are DataSourceID, DeviceID, DeviceStartTime, DeviceEndTime, DeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceCommunity, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceDNSName, DeviceSNMPPolling, DeviceConfigPolling, DevicePortScanning, DeviceSNMPAnalysis, DeviceFingerPrint, DeviceCCSCollection, DeviceVendorDefaultCollection, DeviceConfigTimestamp, DeviceFirstOccurrence, DeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSavedConfigLastChange, DeviceConfigLocked, DeviceConfigLockLastChangeBy, DeviceConfigLockLastChange, DeviceConfigLastChecked, DeviceLicensed, DevicePolicyScheduleMode, NetworkDeviceInd, RoutingInd, SwitchingInd, DeviceRank, DeviceAddlInfo, DeviceMAC, DeviceStandardsCompliance, ParentDeviceID, DeviceContextName, VirtualInd, DeviceSysContact, DeviceManagedInd, SPMLicensedInd, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, ARPCacheRefreshInd, FilteringInd. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NetworkID: The network id to which results would be limited.
             :type NetworkID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against devices, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ARPCacheRefreshInd, DataSourceID, DeviceAddlInfo, DeviceAssurance, DeviceCCSCollection, DeviceChangedCols, DeviceCommunity, DeviceConfigLastChecked, DeviceConfigLockLastChange, DeviceConfigLockLastChangeBy, DeviceConfigLocked, DeviceConfigPolling, DeviceConfigTimestamp, DeviceContextName, DeviceDNSName, DeviceEndTime, DeviceFingerPrint, DeviceFirstOccurrence, DeviceID, DeviceIPDotted, DeviceIPNumeric, DeviceLicensed, DeviceMAC, DeviceManagedInd, DeviceModel, DeviceName, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, DevicePolicyScheduleMode, DevicePortScanning, DeviceRank, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSAAVersion, DeviceSNMPAnalysis, DeviceSNMPPolling, DeviceSavedConfigLastChange, DeviceStandardsCompliance, DeviceStartTime, DeviceSysContact, DeviceSysDescr, DeviceSysLocation, DeviceSysName, DeviceTimestamp, DeviceType, DeviceVendor, DeviceVendorDefaultCollection, DeviceVersion, FilteringInd, NetworkDeviceInd, ParentDeviceID, RoutingInd, SPMLicensedInd, SwitchingInd, VirtualInd.
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

             :return devices: An array of the Device objects that match the specified input criteria.
             :rtype devices: Array of DeviceConfig

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device methods. The listed methods will be called on each device returned and included in the output. Available methods are: data_source.
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

             :return device: The device identified by the specified DeviceID.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def update(self, **kwargs):
        """Updates an existing device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated device.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated device.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated device.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The updated device.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified device from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: An internal NetMRI identifier for the device.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param exclude_ind: Set to true if you want the device to be excluded from the discovery process.
             :type exclude_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def delete(self, **kwargs):
        """Remove many devices, with the option to remove them from discovery

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ids: The ids of the devices to delete comma separated ex: 1,2,3,4.  When sending form encoded use ids[].
             :type ids: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param exclude_ind: Set to 1 if you want these devices to be excluded from the discovery process
             :type exclude_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)
