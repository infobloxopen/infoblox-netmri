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

    def find(self, **kwargs):
        """Lists the available devices matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ARPCacheRefreshInd, DataSourceID, DeviceAddlInfo, DeviceAssurance, DeviceCCSCollection, DeviceChangedCols, DeviceCommunity, DeviceConfigLastChecked, DeviceConfigLockLastChange, DeviceConfigLockLastChangeBy, DeviceConfigLocked, DeviceConfigPolling, DeviceConfigTimestamp, DeviceContextName, DeviceDNSName, DeviceEndTime, DeviceFingerPrint, DeviceFirstOccurrence, DeviceID, DeviceIPDotted, DeviceIPNumeric, DeviceLicensed, DeviceMAC, DeviceManagedInd, DeviceModel, DeviceName, DeviceNetBIOSName, DeviceNetBIOSScanningInd, DeviceOUI, DevicePolicyScheduleMode, DevicePortScanning, DeviceRank, DeviceRebootTime, DeviceRunningConfigLastChange, DeviceSAAVersion, DeviceSNMPAnalysis, DeviceSNMPPolling, DeviceSavedConfigLastChange, DeviceStandardsCompliance, DeviceStartTime, DeviceSysContact, DeviceSysDescr, DeviceSysLocation, DeviceSysName, DeviceTimestamp, DeviceType, DeviceVendor, DeviceVendorDefaultCollection, DeviceVersion, FilteringInd, NetworkDeviceInd, ParentDeviceID, RoutingInd, SPMLicensedInd, SwitchingInd, VirtualInd.

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

             :param op_DeviceAddlInfo: The operator to apply to the field DeviceAddlInfo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceAddlInfo: Additional information about the device; IP phones will contain the extension in this field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceAddlInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceAddlInfo: If op_DeviceAddlInfo is specified, the field named in this input will be compared to the value in DeviceAddlInfo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceAddlInfo must be specified if op_DeviceAddlInfo is specified.
             :type val_f_DeviceAddlInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceAddlInfo: If op_DeviceAddlInfo is specified, this value will be compared to the value in DeviceAddlInfo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceAddlInfo must be specified if op_DeviceAddlInfo is specified.
             :type val_c_DeviceAddlInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceAssurance: The operator to apply to the field DeviceAssurance. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceAssurance: The assurance level of the device type value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceAssurance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceAssurance: If op_DeviceAssurance is specified, the field named in this input will be compared to the value in DeviceAssurance using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceAssurance must be specified if op_DeviceAssurance is specified.
             :type val_f_DeviceAssurance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceAssurance: If op_DeviceAssurance is specified, this value will be compared to the value in DeviceAssurance using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceAssurance must be specified if op_DeviceAssurance is specified.
             :type val_c_DeviceAssurance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceCCSCollection: The operator to apply to the field DeviceCCSCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCCSCollection: If "on", then CCS scripts may be executed against the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCCSCollection: If op_DeviceCCSCollection is specified, the field named in this input will be compared to the value in DeviceCCSCollection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCCSCollection must be specified if op_DeviceCCSCollection is specified.
             :type val_f_DeviceCCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCCSCollection: If op_DeviceCCSCollection is specified, this value will be compared to the value in DeviceCCSCollection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCCSCollection must be specified if op_DeviceCCSCollection is specified.
             :type val_c_DeviceCCSCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceChangedCols: The operator to apply to the field DeviceChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceChangedCols: If op_DeviceChangedCols is specified, the field named in this input will be compared to the value in DeviceChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceChangedCols must be specified if op_DeviceChangedCols is specified.
             :type val_f_DeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceChangedCols: If op_DeviceChangedCols is specified, this value will be compared to the value in DeviceChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceChangedCols must be specified if op_DeviceChangedCols is specified.
             :type val_c_DeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceCommunity: The operator to apply to the field DeviceCommunity. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCommunity: The SNMP read community string for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCommunity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCommunity: If op_DeviceCommunity is specified, the field named in this input will be compared to the value in DeviceCommunity using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCommunity must be specified if op_DeviceCommunity is specified.
             :type val_f_DeviceCommunity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCommunity: If op_DeviceCommunity is specified, this value will be compared to the value in DeviceCommunity using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCommunity must be specified if op_DeviceCommunity is specified.
             :type val_c_DeviceCommunity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigLastChecked: The operator to apply to the field DeviceConfigLastChecked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLastChecked: The date/time of the last attempted retrieval of the device's configuration file. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLastChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLastChecked: If op_DeviceConfigLastChecked is specified, the field named in this input will be compared to the value in DeviceConfigLastChecked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLastChecked must be specified if op_DeviceConfigLastChecked is specified.
             :type val_f_DeviceConfigLastChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLastChecked: If op_DeviceConfigLastChecked is specified, this value will be compared to the value in DeviceConfigLastChecked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLastChecked must be specified if op_DeviceConfigLastChecked is specified.
             :type val_c_DeviceConfigLastChecked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigLockLastChange: The operator to apply to the field DeviceConfigLockLastChange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLockLastChange: The date/time of the last change to the configuration locked status of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLockLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLockLastChange: If op_DeviceConfigLockLastChange is specified, the field named in this input will be compared to the value in DeviceConfigLockLastChange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLockLastChange must be specified if op_DeviceConfigLockLastChange is specified.
             :type val_f_DeviceConfigLockLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLockLastChange: If op_DeviceConfigLockLastChange is specified, this value will be compared to the value in DeviceConfigLockLastChange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLockLastChange must be specified if op_DeviceConfigLockLastChange is specified.
             :type val_c_DeviceConfigLockLastChange: String

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

             :param op_DeviceConfigLocked: The operator to apply to the field DeviceConfigLocked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLocked: If 1, then changes detected will be considered unauthorized. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLocked: If op_DeviceConfigLocked is specified, the field named in this input will be compared to the value in DeviceConfigLocked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLocked must be specified if op_DeviceConfigLocked is specified.
             :type val_f_DeviceConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLocked: If op_DeviceConfigLocked is specified, this value will be compared to the value in DeviceConfigLocked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLocked must be specified if op_DeviceConfigLocked is specified.
             :type val_c_DeviceConfigLocked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigPolling: The operator to apply to the field DeviceConfigPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigPolling: on if NetMRI configuration collection is enabled for the device; off otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigPolling: If op_DeviceConfigPolling is specified, the field named in this input will be compared to the value in DeviceConfigPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigPolling must be specified if op_DeviceConfigPolling is specified.
             :type val_f_DeviceConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigPolling: If op_DeviceConfigPolling is specified, this value will be compared to the value in DeviceConfigPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigPolling must be specified if op_DeviceConfigPolling is specified.
             :type val_c_DeviceConfigPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceConfigTimestamp: The operator to apply to the field DeviceConfigTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigTimestamp: The date/time the configuration file was last successfully retrieved for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigTimestamp: If op_DeviceConfigTimestamp is specified, the field named in this input will be compared to the value in DeviceConfigTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigTimestamp must be specified if op_DeviceConfigTimestamp is specified.
             :type val_f_DeviceConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigTimestamp: If op_DeviceConfigTimestamp is specified, this value will be compared to the value in DeviceConfigTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigTimestamp must be specified if op_DeviceConfigTimestamp is specified.
             :type val_c_DeviceConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceContextName: The operator to apply to the field DeviceContextName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceContextName: The name of the virtual context of this virtual device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceContextName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceContextName: If op_DeviceContextName is specified, the field named in this input will be compared to the value in DeviceContextName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceContextName must be specified if op_DeviceContextName is specified.
             :type val_f_DeviceContextName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceContextName: If op_DeviceContextName is specified, this value will be compared to the value in DeviceContextName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceContextName must be specified if op_DeviceContextName is specified.
             :type val_c_DeviceContextName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceDNSName: The operator to apply to the field DeviceDNSName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceDNSName: The device name as reported by DNS. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceDNSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceDNSName: If op_DeviceDNSName is specified, the field named in this input will be compared to the value in DeviceDNSName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceDNSName must be specified if op_DeviceDNSName is specified.
             :type val_f_DeviceDNSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceDNSName: If op_DeviceDNSName is specified, this value will be compared to the value in DeviceDNSName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceDNSName must be specified if op_DeviceDNSName is specified.
             :type val_c_DeviceDNSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceEndTime: The operator to apply to the field DeviceEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceEndTime: If op_DeviceEndTime is specified, the field named in this input will be compared to the value in DeviceEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceEndTime must be specified if op_DeviceEndTime is specified.
             :type val_f_DeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceEndTime: If op_DeviceEndTime is specified, this value will be compared to the value in DeviceEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceEndTime must be specified if op_DeviceEndTime is specified.
             :type val_c_DeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFingerPrint: The operator to apply to the field DeviceFingerPrint. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFingerPrint: If "on", then NetMRI fingerprinting is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFingerPrint: If op_DeviceFingerPrint is specified, the field named in this input will be compared to the value in DeviceFingerPrint using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFingerPrint must be specified if op_DeviceFingerPrint is specified.
             :type val_f_DeviceFingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFingerPrint: If op_DeviceFingerPrint is specified, this value will be compared to the value in DeviceFingerPrint using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFingerPrint must be specified if op_DeviceFingerPrint is specified.
             :type val_c_DeviceFingerPrint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFirstOccurrence: The operator to apply to the field DeviceFirstOccurrence. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFirstOccurrence: The date/time that this device was first seen on the network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFirstOccurrence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFirstOccurrence: If op_DeviceFirstOccurrence is specified, the field named in this input will be compared to the value in DeviceFirstOccurrence using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFirstOccurrence must be specified if op_DeviceFirstOccurrence is specified.
             :type val_f_DeviceFirstOccurrence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFirstOccurrence: If op_DeviceFirstOccurrence is specified, this value will be compared to the value in DeviceFirstOccurrence using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFirstOccurrence must be specified if op_DeviceFirstOccurrence is specified.
             :type val_c_DeviceFirstOccurrence: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: An internal NetMRI identifier for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceIPDotted: The operator to apply to the field DeviceIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceIPDotted: The management IP address of the device, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceIPDotted: If op_DeviceIPDotted is specified, the field named in this input will be compared to the value in DeviceIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceIPDotted must be specified if op_DeviceIPDotted is specified.
             :type val_f_DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceIPDotted: If op_DeviceIPDotted is specified, this value will be compared to the value in DeviceIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceIPDotted must be specified if op_DeviceIPDotted is specified.
             :type val_c_DeviceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceIPNumeric: The operator to apply to the field DeviceIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceIPNumeric: The numerical value of the device IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceIPNumeric: If op_DeviceIPNumeric is specified, the field named in this input will be compared to the value in DeviceIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceIPNumeric must be specified if op_DeviceIPNumeric is specified.
             :type val_f_DeviceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceIPNumeric: If op_DeviceIPNumeric is specified, this value will be compared to the value in DeviceIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceIPNumeric must be specified if op_DeviceIPNumeric is specified.
             :type val_c_DeviceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceLicensed: The operator to apply to the field DeviceLicensed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceLicensed: If 1, then this device is licensed as a network device by NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceLicensed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceLicensed: If op_DeviceLicensed is specified, the field named in this input will be compared to the value in DeviceLicensed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceLicensed must be specified if op_DeviceLicensed is specified.
             :type val_f_DeviceLicensed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceLicensed: If op_DeviceLicensed is specified, this value will be compared to the value in DeviceLicensed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceLicensed must be specified if op_DeviceLicensed is specified.
             :type val_c_DeviceLicensed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceMAC: The operator to apply to the field DeviceMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceMAC: The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceMAC: If op_DeviceMAC is specified, the field named in this input will be compared to the value in DeviceMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceMAC must be specified if op_DeviceMAC is specified.
             :type val_f_DeviceMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceMAC: If op_DeviceMAC is specified, this value will be compared to the value in DeviceMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceMAC must be specified if op_DeviceMAC is specified.
             :type val_c_DeviceMAC: String

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

             :param op_DeviceModel: The operator to apply to the field DeviceModel. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceModel: The device model name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceModel: If op_DeviceModel is specified, the field named in this input will be compared to the value in DeviceModel using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceModel must be specified if op_DeviceModel is specified.
             :type val_f_DeviceModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceModel: If op_DeviceModel is specified, this value will be compared to the value in DeviceModel using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceModel must be specified if op_DeviceModel is specified.
             :type val_c_DeviceModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceName: The operator to apply to the field DeviceName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceName: The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceName: If op_DeviceName is specified, the field named in this input will be compared to the value in DeviceName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceName must be specified if op_DeviceName is specified.
             :type val_f_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceName: If op_DeviceName is specified, this value will be compared to the value in DeviceName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceName must be specified if op_DeviceName is specified.
             :type val_c_DeviceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceNetBIOSName: The operator to apply to the field DeviceNetBIOSName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceNetBIOSName: The NetBIOS name of the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceNetBIOSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceNetBIOSName: If op_DeviceNetBIOSName is specified, the field named in this input will be compared to the value in DeviceNetBIOSName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceNetBIOSName must be specified if op_DeviceNetBIOSName is specified.
             :type val_f_DeviceNetBIOSName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceNetBIOSName: If op_DeviceNetBIOSName is specified, this value will be compared to the value in DeviceNetBIOSName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceNetBIOSName must be specified if op_DeviceNetBIOSName is specified.
             :type val_c_DeviceNetBIOSName: String

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

             :param op_DeviceOUI: The operator to apply to the field DeviceOUI. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceOUI: The NetMRI-determined device vendor using OUI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceOUI: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceOUI: If op_DeviceOUI is specified, the field named in this input will be compared to the value in DeviceOUI using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceOUI must be specified if op_DeviceOUI is specified.
             :type val_f_DeviceOUI: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceOUI: If op_DeviceOUI is specified, this value will be compared to the value in DeviceOUI using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceOUI must be specified if op_DeviceOUI is specified.
             :type val_c_DeviceOUI: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePolicyScheduleMode: The operator to apply to the field DevicePolicyScheduleMode. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePolicyScheduleMode: Not currently used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePolicyScheduleMode: If op_DevicePolicyScheduleMode is specified, the field named in this input will be compared to the value in DevicePolicyScheduleMode using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePolicyScheduleMode must be specified if op_DevicePolicyScheduleMode is specified.
             :type val_f_DevicePolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePolicyScheduleMode: If op_DevicePolicyScheduleMode is specified, this value will be compared to the value in DevicePolicyScheduleMode using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePolicyScheduleMode must be specified if op_DevicePolicyScheduleMode is specified.
             :type val_c_DevicePolicyScheduleMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePortScanning: The operator to apply to the field DevicePortScanning. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePortScanning: on if NetMRI port scanning is enabled for the device; off otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePortScanning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePortScanning: If op_DevicePortScanning is specified, the field named in this input will be compared to the value in DevicePortScanning using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePortScanning must be specified if op_DevicePortScanning is specified.
             :type val_f_DevicePortScanning: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePortScanning: If op_DevicePortScanning is specified, this value will be compared to the value in DevicePortScanning using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePortScanning must be specified if op_DevicePortScanning is specified.
             :type val_c_DevicePortScanning: String

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

             :param op_DeviceRebootTime: The operator to apply to the field DeviceRebootTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRebootTime: The date/time this device was last rebooted. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRebootTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRebootTime: If op_DeviceRebootTime is specified, the field named in this input will be compared to the value in DeviceRebootTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRebootTime must be specified if op_DeviceRebootTime is specified.
             :type val_f_DeviceRebootTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRebootTime: If op_DeviceRebootTime is specified, this value will be compared to the value in DeviceRebootTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRebootTime must be specified if op_DeviceRebootTime is specified.
             :type val_c_DeviceRebootTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceRunningConfigLastChange: The operator to apply to the field DeviceRunningConfigLastChange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRunningConfigLastChange: The date/time, as reported by SNMP, that the device's running configuration was last changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRunningConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRunningConfigLastChange: If op_DeviceRunningConfigLastChange is specified, the field named in this input will be compared to the value in DeviceRunningConfigLastChange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRunningConfigLastChange must be specified if op_DeviceRunningConfigLastChange is specified.
             :type val_f_DeviceRunningConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRunningConfigLastChange: If op_DeviceRunningConfigLastChange is specified, this value will be compared to the value in DeviceRunningConfigLastChange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRunningConfigLastChange must be specified if op_DeviceRunningConfigLastChange is specified.
             :type val_c_DeviceRunningConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSAAVersion: The operator to apply to the field DeviceSAAVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSAAVersion: The SAA version running on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSAAVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSAAVersion: If op_DeviceSAAVersion is specified, the field named in this input will be compared to the value in DeviceSAAVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSAAVersion must be specified if op_DeviceSAAVersion is specified.
             :type val_f_DeviceSAAVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSAAVersion: If op_DeviceSAAVersion is specified, this value will be compared to the value in DeviceSAAVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSAAVersion must be specified if op_DeviceSAAVersion is specified.
             :type val_c_DeviceSAAVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPAnalysis: The operator to apply to the field DeviceSNMPAnalysis. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPAnalysis: on if NetMRI performs analysis on the device; off otherwise. NOTE: Despite the 'SNMP' in the name, this represents all analysis. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPAnalysis: If op_DeviceSNMPAnalysis is specified, the field named in this input will be compared to the value in DeviceSNMPAnalysis using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPAnalysis must be specified if op_DeviceSNMPAnalysis is specified.
             :type val_f_DeviceSNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPAnalysis: If op_DeviceSNMPAnalysis is specified, this value will be compared to the value in DeviceSNMPAnalysis using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPAnalysis must be specified if op_DeviceSNMPAnalysis is specified.
             :type val_c_DeviceSNMPAnalysis: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSNMPPolling: The operator to apply to the field DeviceSNMPPolling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSNMPPolling: on if NetMRI SNMP polling is enabled for the device; off otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSNMPPolling: If op_DeviceSNMPPolling is specified, the field named in this input will be compared to the value in DeviceSNMPPolling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSNMPPolling must be specified if op_DeviceSNMPPolling is specified.
             :type val_f_DeviceSNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSNMPPolling: If op_DeviceSNMPPolling is specified, this value will be compared to the value in DeviceSNMPPolling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSNMPPolling must be specified if op_DeviceSNMPPolling is specified.
             :type val_c_DeviceSNMPPolling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSavedConfigLastChange: The operator to apply to the field DeviceSavedConfigLastChange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSavedConfigLastChange: The date/time, as reported by SNMP, that the device's saved configuration was last changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSavedConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSavedConfigLastChange: If op_DeviceSavedConfigLastChange is specified, the field named in this input will be compared to the value in DeviceSavedConfigLastChange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSavedConfigLastChange must be specified if op_DeviceSavedConfigLastChange is specified.
             :type val_f_DeviceSavedConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSavedConfigLastChange: If op_DeviceSavedConfigLastChange is specified, this value will be compared to the value in DeviceSavedConfigLastChange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSavedConfigLastChange must be specified if op_DeviceSavedConfigLastChange is specified.
             :type val_c_DeviceSavedConfigLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceStandardsCompliance: The operator to apply to the field DeviceStandardsCompliance. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceStandardsCompliance: on if this device should be considered during standards compliance checks, "off" otherwise. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceStandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceStandardsCompliance: If op_DeviceStandardsCompliance is specified, the field named in this input will be compared to the value in DeviceStandardsCompliance using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceStandardsCompliance must be specified if op_DeviceStandardsCompliance is specified.
             :type val_f_DeviceStandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceStandardsCompliance: If op_DeviceStandardsCompliance is specified, this value will be compared to the value in DeviceStandardsCompliance using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceStandardsCompliance must be specified if op_DeviceStandardsCompliance is specified.
             :type val_c_DeviceStandardsCompliance: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceStartTime: The operator to apply to the field DeviceStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceStartTime: If op_DeviceStartTime is specified, the field named in this input will be compared to the value in DeviceStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceStartTime must be specified if op_DeviceStartTime is specified.
             :type val_f_DeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceStartTime: If op_DeviceStartTime is specified, this value will be compared to the value in DeviceStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceStartTime must be specified if op_DeviceStartTime is specified.
             :type val_c_DeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSysContact: The operator to apply to the field DeviceSysContact. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSysContact: The Device sysContact as reported by SNMP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSysContact: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSysContact: If op_DeviceSysContact is specified, the field named in this input will be compared to the value in DeviceSysContact using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSysContact must be specified if op_DeviceSysContact is specified.
             :type val_f_DeviceSysContact: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSysContact: If op_DeviceSysContact is specified, this value will be compared to the value in DeviceSysContact using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSysContact must be specified if op_DeviceSysContact is specified.
             :type val_c_DeviceSysContact: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSysDescr: The operator to apply to the field DeviceSysDescr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSysDescr: The device sysDescr as reported by SNMP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSysDescr: If op_DeviceSysDescr is specified, the field named in this input will be compared to the value in DeviceSysDescr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSysDescr must be specified if op_DeviceSysDescr is specified.
             :type val_f_DeviceSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSysDescr: If op_DeviceSysDescr is specified, this value will be compared to the value in DeviceSysDescr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSysDescr must be specified if op_DeviceSysDescr is specified.
             :type val_c_DeviceSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSysLocation: The operator to apply to the field DeviceSysLocation. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSysLocation: The device sysLocation as reported by SNMP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSysLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSysLocation: If op_DeviceSysLocation is specified, the field named in this input will be compared to the value in DeviceSysLocation using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSysLocation must be specified if op_DeviceSysLocation is specified.
             :type val_f_DeviceSysLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSysLocation: If op_DeviceSysLocation is specified, this value will be compared to the value in DeviceSysLocation using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSysLocation must be specified if op_DeviceSysLocation is specified.
             :type val_c_DeviceSysLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceSysName: The operator to apply to the field DeviceSysName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSysName: The device name as reported by SNMP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSysName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSysName: If op_DeviceSysName is specified, the field named in this input will be compared to the value in DeviceSysName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSysName must be specified if op_DeviceSysName is specified.
             :type val_f_DeviceSysName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSysName: If op_DeviceSysName is specified, this value will be compared to the value in DeviceSysName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSysName must be specified if op_DeviceSysName is specified.
             :type val_c_DeviceSysName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceTimestamp: The operator to apply to the field DeviceTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceTimestamp: The date and time this record was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceTimestamp: If op_DeviceTimestamp is specified, the field named in this input will be compared to the value in DeviceTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceTimestamp must be specified if op_DeviceTimestamp is specified.
             :type val_f_DeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceTimestamp: If op_DeviceTimestamp is specified, this value will be compared to the value in DeviceTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceTimestamp must be specified if op_DeviceTimestamp is specified.
             :type val_c_DeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceType: The operator to apply to the field DeviceType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceType: The NetMRI-determined device type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceType: If op_DeviceType is specified, the field named in this input will be compared to the value in DeviceType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceType must be specified if op_DeviceType is specified.
             :type val_f_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceType: If op_DeviceType is specified, this value will be compared to the value in DeviceType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceType must be specified if op_DeviceType is specified.
             :type val_c_DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceVendor: The operator to apply to the field DeviceVendor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceVendor: The device vendor name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceVendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceVendor: If op_DeviceVendor is specified, the field named in this input will be compared to the value in DeviceVendor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceVendor must be specified if op_DeviceVendor is specified.
             :type val_f_DeviceVendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceVendor: If op_DeviceVendor is specified, this value will be compared to the value in DeviceVendor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceVendor must be specified if op_DeviceVendor is specified.
             :type val_c_DeviceVendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceVendorDefaultCollection: The operator to apply to the field DeviceVendorDefaultCollection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceVendorDefaultCollection: If "on", then NetMRI vendor default credential checking is enabled for the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceVendorDefaultCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceVendorDefaultCollection: If op_DeviceVendorDefaultCollection is specified, the field named in this input will be compared to the value in DeviceVendorDefaultCollection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceVendorDefaultCollection must be specified if op_DeviceVendorDefaultCollection is specified.
             :type val_f_DeviceVendorDefaultCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceVendorDefaultCollection: If op_DeviceVendorDefaultCollection is specified, this value will be compared to the value in DeviceVendorDefaultCollection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceVendorDefaultCollection must be specified if op_DeviceVendorDefaultCollection is specified.
             :type val_c_DeviceVendorDefaultCollection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceVersion: The operator to apply to the field DeviceVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceVersion: The device OS version. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceVersion: If op_DeviceVersion is specified, the field named in this input will be compared to the value in DeviceVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceVersion must be specified if op_DeviceVersion is specified.
             :type val_f_DeviceVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceVersion: If op_DeviceVersion is specified, this value will be compared to the value in DeviceVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceVersion must be specified if op_DeviceVersion is specified.
             :type val_c_DeviceVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilteringInd: The operator to apply to the field FilteringInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilteringInd: A flag indicating whether this device is eligible for Security Device Controller For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilteringInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilteringInd: If op_FilteringInd is specified, the field named in this input will be compared to the value in FilteringInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilteringInd must be specified if op_FilteringInd is specified.
             :type val_f_FilteringInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilteringInd: If op_FilteringInd is specified, this value will be compared to the value in FilteringInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilteringInd must be specified if op_FilteringInd is specified.
             :type val_c_FilteringInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NetworkDeviceInd: The operator to apply to the field NetworkDeviceInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NetworkDeviceInd: A flag indicating whether this device is a network device or an end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NetworkDeviceInd: If op_NetworkDeviceInd is specified, the field named in this input will be compared to the value in NetworkDeviceInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NetworkDeviceInd must be specified if op_NetworkDeviceInd is specified.
             :type val_f_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NetworkDeviceInd: If op_NetworkDeviceInd is specified, this value will be compared to the value in NetworkDeviceInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NetworkDeviceInd must be specified if op_NetworkDeviceInd is specified.
             :type val_c_NetworkDeviceInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ParentDeviceID: The operator to apply to the field ParentDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ParentDeviceID: The internal NetMRI identifier for the device containing this virtual device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ParentDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ParentDeviceID: If op_ParentDeviceID is specified, the field named in this input will be compared to the value in ParentDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ParentDeviceID must be specified if op_ParentDeviceID is specified.
             :type val_f_ParentDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ParentDeviceID: If op_ParentDeviceID is specified, this value will be compared to the value in ParentDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ParentDeviceID must be specified if op_ParentDeviceID is specified.
             :type val_c_ParentDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RoutingInd: The operator to apply to the field RoutingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RoutingInd: A flag indicating whether this device is configured with any routing capability and whether a routing table was retrieved from this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RoutingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RoutingInd: If op_RoutingInd is specified, the field named in this input will be compared to the value in RoutingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RoutingInd must be specified if op_RoutingInd is specified.
             :type val_f_RoutingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RoutingInd: If op_RoutingInd is specified, this value will be compared to the value in RoutingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RoutingInd must be specified if op_RoutingInd is specified.
             :type val_c_RoutingInd: String

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

             :param op_SwitchingInd: The operator to apply to the field SwitchingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchingInd: A flag indicating whether a switch port forwarding table was retrieved from this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchingInd: If op_SwitchingInd is specified, the field named in this input will be compared to the value in SwitchingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchingInd must be specified if op_SwitchingInd is specified.
             :type val_f_SwitchingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchingInd: If op_SwitchingInd is specified, this value will be compared to the value in SwitchingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchingInd must be specified if op_SwitchingInd is specified.
             :type val_c_SwitchingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualInd: The operator to apply to the field VirtualInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualInd: A flag indicating if the source device is a virtual device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualInd: If op_VirtualInd is specified, the field named in this input will be compared to the value in VirtualInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualInd must be specified if op_VirtualInd is specified.
             :type val_f_VirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualInd: If op_VirtualInd is specified, this value will be compared to the value in VirtualInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualInd must be specified if op_VirtualInd is specified.
             :type val_c_VirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_admin_status_ind: The operator to apply to the field cap_admin_status_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_admin_status_ind: No description is available for cap_admin_status_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_admin_status_ind: If op_cap_admin_status_ind is specified, the field named in this input will be compared to the value in cap_admin_status_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_admin_status_ind must be specified if op_cap_admin_status_ind is specified.
             :type val_f_cap_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_admin_status_ind: If op_cap_admin_status_ind is specified, this value will be compared to the value in cap_admin_status_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_admin_status_ind must be specified if op_cap_admin_status_ind is specified.
             :type val_c_cap_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_admin_status_na_reason: The operator to apply to the field cap_admin_status_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_admin_status_na_reason: No description is available for cap_admin_status_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_admin_status_na_reason: If op_cap_admin_status_na_reason is specified, the field named in this input will be compared to the value in cap_admin_status_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_admin_status_na_reason must be specified if op_cap_admin_status_na_reason is specified.
             :type val_f_cap_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_admin_status_na_reason: If op_cap_admin_status_na_reason is specified, this value will be compared to the value in cap_admin_status_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_admin_status_na_reason must be specified if op_cap_admin_status_na_reason is specified.
             :type val_c_cap_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_description_ind: The operator to apply to the field cap_description_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_description_ind: No description is available for cap_description_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_description_ind: If op_cap_description_ind is specified, the field named in this input will be compared to the value in cap_description_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_description_ind must be specified if op_cap_description_ind is specified.
             :type val_f_cap_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_description_ind: If op_cap_description_ind is specified, this value will be compared to the value in cap_description_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_description_ind must be specified if op_cap_description_ind is specified.
             :type val_c_cap_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_description_na_reason: The operator to apply to the field cap_description_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_description_na_reason: No description is available for cap_description_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_description_na_reason: If op_cap_description_na_reason is specified, the field named in this input will be compared to the value in cap_description_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_description_na_reason must be specified if op_cap_description_na_reason is specified.
             :type val_f_cap_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_description_na_reason: If op_cap_description_na_reason is specified, this value will be compared to the value in cap_description_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_description_na_reason must be specified if op_cap_description_na_reason is specified.
             :type val_c_cap_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_deprovisioning_ind: The operator to apply to the field cap_net_deprovisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_deprovisioning_ind: No description is available for cap_net_deprovisioning_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_deprovisioning_ind: If op_cap_net_deprovisioning_ind is specified, the field named in this input will be compared to the value in cap_net_deprovisioning_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_deprovisioning_ind must be specified if op_cap_net_deprovisioning_ind is specified.
             :type val_f_cap_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_deprovisioning_ind: If op_cap_net_deprovisioning_ind is specified, this value will be compared to the value in cap_net_deprovisioning_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_deprovisioning_ind must be specified if op_cap_net_deprovisioning_ind is specified.
             :type val_c_cap_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_deprovisioning_na_reason: The operator to apply to the field cap_net_deprovisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_deprovisioning_na_reason: No description is available for cap_net_deprovisioning_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_deprovisioning_na_reason: If op_cap_net_deprovisioning_na_reason is specified, the field named in this input will be compared to the value in cap_net_deprovisioning_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_deprovisioning_na_reason must be specified if op_cap_net_deprovisioning_na_reason is specified.
             :type val_f_cap_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_deprovisioning_na_reason: If op_cap_net_deprovisioning_na_reason is specified, this value will be compared to the value in cap_net_deprovisioning_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_deprovisioning_na_reason must be specified if op_cap_net_deprovisioning_na_reason is specified.
             :type val_c_cap_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_provisioning_ind: The operator to apply to the field cap_net_provisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_provisioning_ind: No description is available for cap_net_provisioning_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_provisioning_ind: If op_cap_net_provisioning_ind is specified, the field named in this input will be compared to the value in cap_net_provisioning_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_provisioning_ind must be specified if op_cap_net_provisioning_ind is specified.
             :type val_f_cap_net_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_provisioning_ind: If op_cap_net_provisioning_ind is specified, this value will be compared to the value in cap_net_provisioning_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_provisioning_ind must be specified if op_cap_net_provisioning_ind is specified.
             :type val_c_cap_net_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_provisioning_na_reason: The operator to apply to the field cap_net_provisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_provisioning_na_reason: No description is available for cap_net_provisioning_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_provisioning_na_reason: If op_cap_net_provisioning_na_reason is specified, the field named in this input will be compared to the value in cap_net_provisioning_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_provisioning_na_reason must be specified if op_cap_net_provisioning_na_reason is specified.
             :type val_f_cap_net_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_provisioning_na_reason: If op_cap_net_provisioning_na_reason is specified, this value will be compared to the value in cap_net_provisioning_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_provisioning_na_reason must be specified if op_cap_net_provisioning_na_reason is specified.
             :type val_c_cap_net_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_vlan_provisioning_ind: The operator to apply to the field cap_net_vlan_provisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_vlan_provisioning_ind: No description is available for cap_net_vlan_provisioning_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_vlan_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_vlan_provisioning_ind: If op_cap_net_vlan_provisioning_ind is specified, the field named in this input will be compared to the value in cap_net_vlan_provisioning_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_vlan_provisioning_ind must be specified if op_cap_net_vlan_provisioning_ind is specified.
             :type val_f_cap_net_vlan_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_vlan_provisioning_ind: If op_cap_net_vlan_provisioning_ind is specified, this value will be compared to the value in cap_net_vlan_provisioning_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_vlan_provisioning_ind must be specified if op_cap_net_vlan_provisioning_ind is specified.
             :type val_c_cap_net_vlan_provisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_net_vlan_provisioning_na_reason: The operator to apply to the field cap_net_vlan_provisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_vlan_provisioning_na_reason: No description is available for cap_net_vlan_provisioning_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_net_vlan_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_net_vlan_provisioning_na_reason: If op_cap_net_vlan_provisioning_na_reason is specified, the field named in this input will be compared to the value in cap_net_vlan_provisioning_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_net_vlan_provisioning_na_reason must be specified if op_cap_net_vlan_provisioning_na_reason is specified.
             :type val_f_cap_net_vlan_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_net_vlan_provisioning_na_reason: If op_cap_net_vlan_provisioning_na_reason is specified, this value will be compared to the value in cap_net_vlan_provisioning_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_net_vlan_provisioning_na_reason must be specified if op_cap_net_vlan_provisioning_na_reason is specified.
             :type val_c_cap_net_vlan_provisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_vlan_assignment_ind: The operator to apply to the field cap_vlan_assignment_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_vlan_assignment_ind: No description is available for cap_vlan_assignment_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_vlan_assignment_ind: If op_cap_vlan_assignment_ind is specified, the field named in this input will be compared to the value in cap_vlan_assignment_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_vlan_assignment_ind must be specified if op_cap_vlan_assignment_ind is specified.
             :type val_f_cap_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_vlan_assignment_ind: If op_cap_vlan_assignment_ind is specified, this value will be compared to the value in cap_vlan_assignment_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_vlan_assignment_ind must be specified if op_cap_vlan_assignment_ind is specified.
             :type val_c_cap_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_vlan_assignment_na_reason: The operator to apply to the field cap_vlan_assignment_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_vlan_assignment_na_reason: No description is available for cap_vlan_assignment_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_vlan_assignment_na_reason: If op_cap_vlan_assignment_na_reason is specified, the field named in this input will be compared to the value in cap_vlan_assignment_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_vlan_assignment_na_reason must be specified if op_cap_vlan_assignment_na_reason is specified.
             :type val_f_cap_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_vlan_assignment_na_reason: If op_cap_vlan_assignment_na_reason is specified, this value will be compared to the value in cap_vlan_assignment_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_vlan_assignment_na_reason must be specified if op_cap_vlan_assignment_na_reason is specified.
             :type val_c_cap_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_voice_vlan_ind: The operator to apply to the field cap_voice_vlan_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_voice_vlan_ind: No description is available for cap_voice_vlan_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_voice_vlan_ind: If op_cap_voice_vlan_ind is specified, the field named in this input will be compared to the value in cap_voice_vlan_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_voice_vlan_ind must be specified if op_cap_voice_vlan_ind is specified.
             :type val_f_cap_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_voice_vlan_ind: If op_cap_voice_vlan_ind is specified, this value will be compared to the value in cap_voice_vlan_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_voice_vlan_ind must be specified if op_cap_voice_vlan_ind is specified.
             :type val_c_cap_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_voice_vlan_na_reason: The operator to apply to the field cap_voice_vlan_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_voice_vlan_na_reason: No description is available for cap_voice_vlan_na_reason. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_voice_vlan_na_reason: If op_cap_voice_vlan_na_reason is specified, the field named in this input will be compared to the value in cap_voice_vlan_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_voice_vlan_na_reason must be specified if op_cap_voice_vlan_na_reason is specified.
             :type val_f_cap_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_voice_vlan_na_reason: If op_cap_voice_vlan_na_reason is specified, this value will be compared to the value in cap_voice_vlan_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_voice_vlan_na_reason must be specified if op_cap_voice_vlan_na_reason is specified.
             :type val_c_cap_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_privileged_polling: The operator to apply to the field privileged_polling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. privileged_polling: No description is available for privileged_polling. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_privileged_polling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_privileged_polling: If op_privileged_polling is specified, the field named in this input will be compared to the value in privileged_polling using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_privileged_polling must be specified if op_privileged_polling is specified.
             :type val_f_privileged_polling: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_privileged_polling: If op_privileged_polling is specified, this value will be compared to the value in privileged_polling using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_privileged_polling must be specified if op_privileged_polling is specified.
             :type val_c_privileged_polling: String

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

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

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

    def running_config_text(self, **kwargs):
        """The contents of the newest saved running config.

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

             :return : The contents of the newest saved running config.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("running_config_text"), kwargs)

    def saved_config_text(self, **kwargs):
        """The contents of the newest saved startup config.

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

             :return : The contents of the newest saved startup config.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("saved_config_text"), kwargs)

    def DeviceCommunity(self, **kwargs):
        """The community string.

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

             :return : The community string.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("DeviceCommunity"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

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

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def parent_device(self, **kwargs):
        """The device containing this virtual device.

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

             :return : The device containing this virtual device.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("parent_device"), kwargs)

    def gateway_device(self, **kwargs):
        """Returns the default gateway router for this device, based on the following in order of preference: device routing table, device configuration file, device subnet and common conventions.

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

             :return : Returns the default gateway router for this device, based on the following in order of preference: device routing table, device configuration file, device subnet and common conventions.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("gateway_device"), kwargs)

    def running_config(self, **kwargs):
        """Returns the ConfigRevision object corresponding to the device's current running configuration.

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

             :return : Returns the ConfigRevision object corresponding to the device's current running configuration.
             :rtype : ConfigRevision

            """

        return self.api_request(self._get_method_fullname("running_config"), kwargs)

    def saved_config(self, **kwargs):
        """Returns the ConfigRevision object corresponding to the device's current startup configuration.

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

             :return : Returns the ConfigRevision object corresponding to the device's current startup configuration.
             :rtype : ConfigRevision

            """

        return self.api_request(self._get_method_fullname("saved_config"), kwargs)

    def device_setting(self, **kwargs):
        """Returns settings for selected device

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

             :return : Returns settings for selected device
             :rtype : DeviceSetting

            """

        return self.api_request(self._get_method_fullname("device_setting"), kwargs)

    def running_config_diff(self, **kwargs):
        """The differences between the current and previous running config.

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

             :return : The differences between the current and previous running config.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("running_config_diff"), kwargs)

    def saved_config_diff(self, **kwargs):
        """The differences between the current and previous saved config.

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

             :return : The differences between the current and previous saved config.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("saved_config_diff"), kwargs)

    def asset_type(self, **kwargs):
        """The physical/virtual aspect of the device (Virtual Host, Virtual Device, or Physical Device).

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

             :return : The physical/virtual aspect of the device (Virtual Host, Virtual Device, or Physical Device).
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("asset_type"), kwargs)

    def SwitchingInd(self, **kwargs):
        """A flag indicating if this device act as a switcher

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

             :return : A flag indicating if this device act as a switcher
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("SwitchingInd"), kwargs)

    def RoutingInd(self, **kwargs):
        """A flag indicating if this device act as a router

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

             :return : A flag indicating if this device act as a router
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("RoutingInd"), kwargs)

    def DeviceSAAVersion(self, **kwargs):
        """the SAA version of this device

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

             :return : the SAA version of this device
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("DeviceSAAVersion"), kwargs)

    def DeviceRebootTime(self, **kwargs):
        """the reboot time of this device

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

             :return : the reboot time of this device
             :rtype : DateTime

            """

        return self.api_request(self._get_method_fullname("DeviceRebootTime"), kwargs)

    def DeviceCommunitySecure(self, **kwargs):
        """The secured community name

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

             :return : The secured community name
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("DeviceCommunitySecure"), kwargs)

    def DeviceRank(self, **kwargs):
        """The rank of this device in its virtual brotherhood

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

             :return : The rank of this device in its virtual brotherhood
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("DeviceRank"), kwargs)

    def DeviceFirstOccurrence(self, **kwargs):
        """The first occurrence of this device

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

             :return : The first occurrence of this device
             :rtype : DateTime

            """

        return self.api_request(self._get_method_fullname("DeviceFirstOccurrence"), kwargs)

    def virtual_child_count(self, **kwargs):
        """The number of virtual devices hosted on this device

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

             :return : The number of virtual devices hosted on this device
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("virtual_child_count"), kwargs)

    def data_collection_status(self, **kwargs):
        """All information about collection of data for this device

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

             :return : All information about collection of data for this device
             :rtype : DataCollectionStatus

            """

        return self.api_request(self._get_method_fullname("data_collection_status"), kwargs)

    def DeviceContextName(self, **kwargs):
        """The name of the virtual context of this virtual device.

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

             :return : The name of the virtual context of this virtual device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("DeviceContextName"), kwargs)

    def virtual_network(self, **kwargs):
        """A Virtual Network model assigned to the device.

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

             :return : A Virtual Network model assigned to the device.
             :rtype : VirtualNetwork

            """

        return self.api_request(self._get_method_fullname("virtual_network"), kwargs)

    def network_name(self, **kwargs):
        """A Network View assigned to the device.

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

             :return : A Network View assigned to the device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("network_name"), kwargs)

    def control_capabilities(self, **kwargs):
        """Configuration capabilities for this interface, related to Port Control.

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

             :return : Configuration capabilities for this interface, related to Port Control.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("control_capabilities"), kwargs)

    def cap_description_ind(self, **kwargs):
        """Capability of changing the description of an interface of this device.

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

             :return : Capability of changing the description of an interface of this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_description_ind"), kwargs)

    def cap_admin_status_ind(self, **kwargs):
        """Capability of changing the Admin Status of an interface of this device.

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

             :return : Capability of changing the Admin Status of an interface of this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_admin_status_ind"), kwargs)

    def cap_vlan_assignment_ind(self, **kwargs):
        """Capability of assigning a regular data VLAN to an interface of this device.

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

             :return : Capability of assigning a regular data VLAN to an interface of this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_vlan_assignment_ind"), kwargs)

    def cap_voice_vlan_ind(self, **kwargs):
        """Capability of assigning a voice VLAN to an interface of this device.

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

             :return : Capability of assigning a voice VLAN to an interface of this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_voice_vlan_ind"), kwargs)

    def cap_net_provisioning_ind(self, **kwargs):
        """Capability of provisioning a network on an interface of this device.

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

             :return : Capability of provisioning a network on an interface of this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_net_provisioning_ind"), kwargs)

    def cap_net_vlan_provisioning_ind(self, **kwargs):
        """Capability of creating a VLAN and provision a netowrk on its virtual interface.

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

             :return : Capability of creating a VLAN and provision a netowrk on its virtual interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_net_vlan_provisioning_ind"), kwargs)

    def cap_net_deprovisioning_ind(self, **kwargs):
        """Capability of de-provisioning a network from this device.

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

             :return : Capability of de-provisioning a network from this device.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_net_deprovisioning_ind"), kwargs)

    def cap_description_na_reason(self, **kwargs):
        """Reason of non ability of changing the description of an interface of this device.

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

             :return : Reason of non ability of changing the description of an interface of this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_description_na_reason"), kwargs)

    def cap_admin_status_na_reason(self, **kwargs):
        """Reason of non ability of changing the Admin Status of an interface of this device.

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

             :return : Reason of non ability of changing the Admin Status of an interface of this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_admin_status_na_reason"), kwargs)

    def cap_vlan_assignment_na_reason(self, **kwargs):
        """Reason of non ability of assigning a regular data VLAN to an interface of this device.

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

             :return : Reason of non ability of assigning a regular data VLAN to an interface of this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_vlan_assignment_na_reason"), kwargs)

    def cap_voice_vlan_na_reason(self, **kwargs):
        """Reason of non ability of assigning a voice VLAN to an interface of this device.

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

             :return : Reason of non ability of assigning a voice VLAN to an interface of this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_voice_vlan_na_reason"), kwargs)

    def cap_net_provisioning_na_reason(self, **kwargs):
        """Reason of non ability of provisioning a network on an interface of this device.

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

             :return : Reason of non ability of provisioning a network on an interface of this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_net_provisioning_na_reason"), kwargs)

    def cap_net_vlan_provisioning_na_reason(self, **kwargs):
        """Reason of non ability of creating a VLAN and provision a netowrk on its virtual interface.

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

             :return : Reason of non ability of creating a VLAN and provision a netowrk on its virtual interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_net_vlan_provisioning_na_reason"), kwargs)

    def cap_net_deprovisioning_na_reason(self, **kwargs):
        """Reason of non ability of de-provisioning a network from this device.

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

             :return : Reason of non ability of de-provisioning a network from this device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_net_deprovisioning_na_reason"), kwargs)

    def privileged_polling(self, **kwargs):
        """A flag indicating whether to poll the device in privileged mode.

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

             :return : A flag indicating whether to poll the device in privileged mode.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("privileged_polling"), kwargs)

    def discover(self, **kwargs):
        """Performs an immediate discovery on an IP address, returning the new or updated Device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address: The IP address to discover.
             :type ip_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param ignore_history_ind: If true, NetMRI will not check for previous instances of this IP address, and therefore will not associate this IP address with any existing device history.
             :type ignore_history_ind: Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mac_address: Device MAC address to be discovered now
             :type mac_address: String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The identifier for the network view which this device belongs to. Required with 'ip_address' if no 'DeviceID' is specified in multiple network views system.
             :type virtual_network_id: Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device for which the discovery should be performed.
             :type DeviceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return ip_address: The IP address used for discovery.
             :rtype ip_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceID: The internal NetMRI identifier for the device.
             :rtype DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceType: The type of device as determined during this discovery.
             :rtype DeviceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return DeviceVendor: The vendor of the device as determined during this discovery.
             :rtype DeviceVendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The discovered device object.
             :rtype device: Device

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return initial: A flag indicating whether the initial device discovery was successful.
             :rtype initial: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return fingerprint: A flag indicating whether the NMAP Fingerprinting was successful.
             :rtype fingerprint: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return identification: A flag indicating whether the identification process was successful.
             :rtype identification: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_credentials: A flag indicating whether the SNMP credentials were determined for the device.
             :rtype snmp_credentials: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return system_info: A flag indicating whether the SNMP System MIB was successfully queried.
             :rtype system_info: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return confirm_type: A flag indicating whether the device type was confirmed after SNMP System MIB collection.
             :rtype confirm_type: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_credentials: A flag indicating whether the CLI credentials were determined for the device.
             :rtype cli_credentials: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_collection: A flag indicating whether the configuration file for the device was successfully collected.
             :rtype config_collection: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return returncode: The return code indicating the stage of discovery where discovery halted.</br>
        </br>  0: Device discovered successfully.
        </br>  1: Unable to perform device discovery, whether because the device is not licensed or the SNMP Collection is disabled for this device.
        </br>  2: Unable to discover device, because the entered ip address belongs to an existing device.
        </br>  3: Unable to determine SNMP credentials.
        </br>  4: Unable to perform device identification discovery.
        </br>  5: Unable to collect basic SystemInfo info via SNMP.
        </br>  6: Unable to discover second time to confirm device type.
        </br>  7: Unable to recollect basic SystemInfo info via SNMP.
        </br>  8: Unable to determine CLI credentials.
        </br>  9: Unable to collect config file.
        </br> 10: Skipping DiscoverNow for this IP address due to blackout period in effect.
        </br> 25: Lock-timeout: Gave up waiting for other process to finish.
             :rtype returncode: Integer

            """

        return self.api_request(self._get_method_fullname("discover"), kwargs)

    def poll(self, **kwargs):
        """Polls the device, either by SNMP or CLI, depending on the object and the device type, vendor, model, and OS version. The device must be licensed, and within a group with collection enabled.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the device to poll.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param objects: The objects to poll on the device. Valid values are: arp, forwarding, interface, inventory, routing, switch_port, vlan, vrf, wireless.
             :type objects: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 120

             :param timeout: Only a single on-demand polling action can be executing on an individual collector at a time. This value is the amount of time to wait to obtain the on-demand polling lock.
             :type timeout: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 120

             :param timeout_consolidation: This value is the amount of time to wait until consolidation is completed. If the consolidation is not completed at time, its goes into the background tasks and the job is finished successfully.
             :type timeout_consolidation: Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param async_ind: When false, the poll will be run synchronously, and the API call will block until it is complete. When true, poll id will be returned to use for subsequent calls
             :type async_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return text: When async_ind is false, poll text will be returned upon completion.
             :rtype text: String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The internal NetMRI identifier for previously initiated poll.
             :rtype id: String

            """

        return self.api_request(self._get_method_fullname("poll"), kwargs)

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

    def scan_port_for_open_dhcp(self, **kwargs):
        """Scans device for open DHCP services by sending a bogus request packet.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ip_address: The IP address of the end host to scan.
             :type ip_address: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the DHCP service (OPEN, CLOSED, UNRESPONSIVE).
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("scan_port_for_open_dhcp"), kwargs)
