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
