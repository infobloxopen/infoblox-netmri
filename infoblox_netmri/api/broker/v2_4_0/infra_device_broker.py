from ..broker import Broker


class InfraDeviceBroker(Broker):
    controller = "infra_devices"

    def index(self, **kwargs):
        """Lists the available infra devices. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrenceTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrenceTime: Array of DateTime

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
             :type VirtualNetworkID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
             :type VirtualNetworkID: Array of Integer

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

             :param timestamp: The data returned will represent the infra devices as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of infra device methods. The listed methods will be called on each infra device returned and included in the output. Available methods are: DeviceCommunitySecure, DeviceRank, DeviceCommunity, DeviceFirstOccurrence, group, parent_device, gateway_device, running_config, running_config_text, saved_config, saved_config_text, running_config_diff, saved_config_diff, virtual_child_count, asset_type, device_setting, data_collection_status, control_capabilities, network_name, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, privileged_polling, DeviceStartTime, DeviceEndTime, cap_description_ind, cap_admin_status_ind, cap_vlan_assignment_ind, cap_voice_vlan_ind, cap_net_provisioning_ind, cap_net_vlan_provisioning_ind, cap_net_deprovisioning_ind, cap_description_na_reason, cap_admin_status_na_reason, cap_vlan_assignment_na_reason, cap_voice_vlan_na_reason, cap_net_provisioning_na_reason, cap_net_vlan_provisioning_na_reason, cap_net_deprovisioning_na_reason, chassis_serial_number, available_mgmt_ips, rawSysDescr, rawSysVersion, rawSysModel, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device, device_setting, data_collection_status, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, data_source, device.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey.
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

             :param select: The list of attributes to return for each InfraDevice. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param detail_ind: A flag to indicate whether discovery times should be included or not
             :type detail_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return infra_devices: An array of the InfraDevice objects that match the specified input criteria.
             :rtype infra_devices: Array of InfraDevice

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available infra devices matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

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

             :param DeviceAddlInfo: Additional information about the device; IP phones will contain the extension in this field.
             :type DeviceAddlInfo: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceAddlInfo: Additional information about the device; IP phones will contain the extension in this field.
             :type DeviceAddlInfo: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLastCheckedTime: The date/time of the last attempted retrieval of the device's configuration file.
             :type DeviceConfigLastCheckedTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceConfigLastCheckedTime: The date/time of the last attempted retrieval of the device's configuration file.
             :type DeviceConfigLastCheckedTime: Array of DateTime

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrenceTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network.
             :type DeviceFirstOccurrenceTime: Array of DateTime

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRunningConfigLastChangedTime: The date/time, as reported by SNMP, that the device's running configuration was last changed.
             :type DeviceRunningConfigLastChangedTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceRunningConfigLastChangedTime: The date/time, as reported by SNMP, that the device's running configuration was last changed.
             :type DeviceRunningConfigLastChangedTime: Array of DateTime

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSavedConfigLastChangedTime: The date/time, as reported by SNMP, that the device's saved configuration was last changed.
             :type DeviceSavedConfigLastChangedTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceSavedConfigLastChangedTime: The date/time, as reported by SNMP, that the device's saved configuration was last changed.
             :type DeviceSavedConfigLastChangedTime: Array of DateTime

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceUniqueKey: Unique key which allows duplicates detecting over different Virtual Networks.
             :type DeviceUniqueKey: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceUniqueKey: Unique key which allows duplicates detecting over different Virtual Networks.
             :type DeviceUniqueKey: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FilterProvisionData:  Internal data - do not modify, may change without warning.
             :type FilterProvisionData: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterProvisionData:  Internal data - do not modify, may change without warning.
             :type FilterProvisionData: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type InfraDeviceChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type InfraDeviceChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type InfraDeviceEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type InfraDeviceEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceStartTime: The starting effective time of this revision of the record.
             :type InfraDeviceStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceStartTime: The starting effective time of this revision of the record.
             :type InfraDeviceStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceTimestamp: The date and time this record was collected.
             :type InfraDeviceTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfraDeviceTimestamp: The date and time this record was collected.
             :type InfraDeviceTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MgmtServerDeviceID: The Device ID of the management server for the device
             :type MgmtServerDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MgmtServerDeviceID: The Device ID of the management server for the device
             :type MgmtServerDeviceID: Array of Integer

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
             :type VirtualNetworkID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkingInd: Set to null, 0 or 1.  0 indicates this is not a VRF Aware device.  1 Indicates it is VRF Aware.
             :type VirtualNetworkingInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkingInd: Set to null, 0 or 1.  0 indicates this is not a VRF Aware device.  1 Indicates it is VRF Aware.
             :type VirtualNetworkingInd: Array of Boolean

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

             :param timestamp: The data returned will represent the infra devices as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of infra device methods. The listed methods will be called on each infra device returned and included in the output. Available methods are: DeviceCommunitySecure, DeviceRank, DeviceCommunity, DeviceFirstOccurrence, group, parent_device, gateway_device, running_config, running_config_text, saved_config, saved_config_text, running_config_diff, saved_config_diff, virtual_child_count, asset_type, device_setting, data_collection_status, control_capabilities, network_name, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, privileged_polling, DeviceStartTime, DeviceEndTime, cap_description_ind, cap_admin_status_ind, cap_vlan_assignment_ind, cap_voice_vlan_ind, cap_net_provisioning_ind, cap_net_vlan_provisioning_ind, cap_net_deprovisioning_ind, cap_description_na_reason, cap_admin_status_na_reason, cap_vlan_assignment_na_reason, cap_voice_vlan_na_reason, cap_net_provisioning_na_reason, cap_net_vlan_provisioning_na_reason, cap_net_deprovisioning_na_reason, chassis_serial_number, available_mgmt_ips, rawSysDescr, rawSysVersion, rawSysModel, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device, device_setting, data_collection_status, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, data_source, device.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey.
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

             :param select: The list of attributes to return for each InfraDevice. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against infra devices, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceAddlInfo, DeviceAssurance, DeviceConfigLastCheckedTime, DeviceConfigTimestamp, DeviceContextName, DeviceDNSName, DeviceFirstOccurrenceTime, DeviceID, DeviceIPDotted, DeviceIPNumeric, DeviceMAC, DeviceModel, DeviceName, DeviceNetBIOSName, DeviceOUI, DevicePolicyScheduleMode, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSAAVersion, DeviceSavedConfigLastChangedTime, DeviceSysContact, DeviceSysDescr, DeviceSysLocation, DeviceSysName, DeviceType, DeviceUniqueKey, DeviceVendor, DeviceVersion, FilterProvisionData, FilteringInd, InfraDeviceChangedCols, InfraDeviceEndTime, InfraDeviceStartTime, InfraDeviceTimestamp, MgmtServerDeviceID, NetworkDeviceInd, ParentDeviceID, RoutingInd, SwitchingInd, VirtualInd, VirtualNetworkID, VirtualNetworkingInd.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param detail_ind: A flag to indicate whether discovery times should be included or not
             :type detail_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return infra_devices: An array of the InfraDevice objects that match the specified input criteria.
             :rtype infra_devices: Array of InfraDevice

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available infra devices matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceAddlInfo, DeviceAssurance, DeviceConfigLastCheckedTime, DeviceConfigTimestamp, DeviceContextName, DeviceDNSName, DeviceFirstOccurrenceTime, DeviceID, DeviceIPDotted, DeviceIPNumeric, DeviceMAC, DeviceModel, DeviceName, DeviceNetBIOSName, DeviceOUI, DevicePolicyScheduleMode, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSAAVersion, DeviceSavedConfigLastChangedTime, DeviceSysContact, DeviceSysDescr, DeviceSysLocation, DeviceSysName, DeviceType, DeviceUniqueKey, DeviceVendor, DeviceVersion, FilterProvisionData, FilteringInd, InfraDeviceChangedCols, InfraDeviceEndTime, InfraDeviceStartTime, InfraDeviceTimestamp, MgmtServerDeviceID, NetworkDeviceInd, ParentDeviceID, RoutingInd, SwitchingInd, VirtualInd, VirtualNetworkID, VirtualNetworkingInd.

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

             :param op_DeviceConfigLastCheckedTime: The operator to apply to the field DeviceConfigLastCheckedTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceConfigLastCheckedTime: The date/time of the last attempted retrieval of the device's configuration file. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceConfigLastCheckedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceConfigLastCheckedTime: If op_DeviceConfigLastCheckedTime is specified, the field named in this input will be compared to the value in DeviceConfigLastCheckedTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceConfigLastCheckedTime must be specified if op_DeviceConfigLastCheckedTime is specified.
             :type val_f_DeviceConfigLastCheckedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceConfigLastCheckedTime: If op_DeviceConfigLastCheckedTime is specified, this value will be compared to the value in DeviceConfigLastCheckedTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceConfigLastCheckedTime must be specified if op_DeviceConfigLastCheckedTime is specified.
             :type val_c_DeviceConfigLastCheckedTime: String

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

             :param op_DeviceFirstOccurrenceTime: The operator to apply to the field DeviceFirstOccurrenceTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFirstOccurrenceTime: The date/time that this device was first seen on the network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFirstOccurrenceTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFirstOccurrenceTime: If op_DeviceFirstOccurrenceTime is specified, the field named in this input will be compared to the value in DeviceFirstOccurrenceTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFirstOccurrenceTime must be specified if op_DeviceFirstOccurrenceTime is specified.
             :type val_f_DeviceFirstOccurrenceTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFirstOccurrenceTime: If op_DeviceFirstOccurrenceTime is specified, this value will be compared to the value in DeviceFirstOccurrenceTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFirstOccurrenceTime must be specified if op_DeviceFirstOccurrenceTime is specified.
             :type val_c_DeviceFirstOccurrenceTime: String

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

             :param op_DeviceRunningConfigLastChangedTime: The operator to apply to the field DeviceRunningConfigLastChangedTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceRunningConfigLastChangedTime: The date/time, as reported by SNMP, that the device's running configuration was last changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceRunningConfigLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceRunningConfigLastChangedTime: If op_DeviceRunningConfigLastChangedTime is specified, the field named in this input will be compared to the value in DeviceRunningConfigLastChangedTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceRunningConfigLastChangedTime must be specified if op_DeviceRunningConfigLastChangedTime is specified.
             :type val_f_DeviceRunningConfigLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceRunningConfigLastChangedTime: If op_DeviceRunningConfigLastChangedTime is specified, this value will be compared to the value in DeviceRunningConfigLastChangedTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceRunningConfigLastChangedTime must be specified if op_DeviceRunningConfigLastChangedTime is specified.
             :type val_c_DeviceRunningConfigLastChangedTime: String

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

             :param op_DeviceSavedConfigLastChangedTime: The operator to apply to the field DeviceSavedConfigLastChangedTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceSavedConfigLastChangedTime: The date/time, as reported by SNMP, that the device's saved configuration was last changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceSavedConfigLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceSavedConfigLastChangedTime: If op_DeviceSavedConfigLastChangedTime is specified, the field named in this input will be compared to the value in DeviceSavedConfigLastChangedTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceSavedConfigLastChangedTime must be specified if op_DeviceSavedConfigLastChangedTime is specified.
             :type val_f_DeviceSavedConfigLastChangedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceSavedConfigLastChangedTime: If op_DeviceSavedConfigLastChangedTime is specified, this value will be compared to the value in DeviceSavedConfigLastChangedTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceSavedConfigLastChangedTime must be specified if op_DeviceSavedConfigLastChangedTime is specified.
             :type val_c_DeviceSavedConfigLastChangedTime: String

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

             :param op_DeviceUniqueKey: The operator to apply to the field DeviceUniqueKey. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceUniqueKey: Unique key which allows duplicates detecting over different Virtual Networks. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceUniqueKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceUniqueKey: If op_DeviceUniqueKey is specified, the field named in this input will be compared to the value in DeviceUniqueKey using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceUniqueKey must be specified if op_DeviceUniqueKey is specified.
             :type val_f_DeviceUniqueKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceUniqueKey: If op_DeviceUniqueKey is specified, this value will be compared to the value in DeviceUniqueKey using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceUniqueKey must be specified if op_DeviceUniqueKey is specified.
             :type val_c_DeviceUniqueKey: String

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

             :param op_FilterProvisionData: The operator to apply to the field FilterProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterProvisionData:  Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterProvisionData: If op_FilterProvisionData is specified, the field named in this input will be compared to the value in FilterProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterProvisionData must be specified if op_FilterProvisionData is specified.
             :type val_f_FilterProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterProvisionData: If op_FilterProvisionData is specified, this value will be compared to the value in FilterProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterProvisionData must be specified if op_FilterProvisionData is specified.
             :type val_c_FilterProvisionData: String

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

             :param op_InfraDeviceChangedCols: The operator to apply to the field InfraDeviceChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfraDeviceChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfraDeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfraDeviceChangedCols: If op_InfraDeviceChangedCols is specified, the field named in this input will be compared to the value in InfraDeviceChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfraDeviceChangedCols must be specified if op_InfraDeviceChangedCols is specified.
             :type val_f_InfraDeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfraDeviceChangedCols: If op_InfraDeviceChangedCols is specified, this value will be compared to the value in InfraDeviceChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfraDeviceChangedCols must be specified if op_InfraDeviceChangedCols is specified.
             :type val_c_InfraDeviceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InfraDeviceEndTime: The operator to apply to the field InfraDeviceEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfraDeviceEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfraDeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfraDeviceEndTime: If op_InfraDeviceEndTime is specified, the field named in this input will be compared to the value in InfraDeviceEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfraDeviceEndTime must be specified if op_InfraDeviceEndTime is specified.
             :type val_f_InfraDeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfraDeviceEndTime: If op_InfraDeviceEndTime is specified, this value will be compared to the value in InfraDeviceEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfraDeviceEndTime must be specified if op_InfraDeviceEndTime is specified.
             :type val_c_InfraDeviceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InfraDeviceStartTime: The operator to apply to the field InfraDeviceStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfraDeviceStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfraDeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfraDeviceStartTime: If op_InfraDeviceStartTime is specified, the field named in this input will be compared to the value in InfraDeviceStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfraDeviceStartTime must be specified if op_InfraDeviceStartTime is specified.
             :type val_f_InfraDeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfraDeviceStartTime: If op_InfraDeviceStartTime is specified, this value will be compared to the value in InfraDeviceStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfraDeviceStartTime must be specified if op_InfraDeviceStartTime is specified.
             :type val_c_InfraDeviceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InfraDeviceTimestamp: The operator to apply to the field InfraDeviceTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfraDeviceTimestamp: The date and time this record was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfraDeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfraDeviceTimestamp: If op_InfraDeviceTimestamp is specified, the field named in this input will be compared to the value in InfraDeviceTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfraDeviceTimestamp must be specified if op_InfraDeviceTimestamp is specified.
             :type val_f_InfraDeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfraDeviceTimestamp: If op_InfraDeviceTimestamp is specified, this value will be compared to the value in InfraDeviceTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfraDeviceTimestamp must be specified if op_InfraDeviceTimestamp is specified.
             :type val_c_InfraDeviceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MgmtServerDeviceID: The operator to apply to the field MgmtServerDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MgmtServerDeviceID: The Device ID of the management server for the device For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MgmtServerDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MgmtServerDeviceID: If op_MgmtServerDeviceID is specified, the field named in this input will be compared to the value in MgmtServerDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MgmtServerDeviceID must be specified if op_MgmtServerDeviceID is specified.
             :type val_f_MgmtServerDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MgmtServerDeviceID: If op_MgmtServerDeviceID is specified, this value will be compared to the value in MgmtServerDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MgmtServerDeviceID must be specified if op_MgmtServerDeviceID is specified.
             :type val_c_MgmtServerDeviceID: String

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

             :param op_VirtualNetworkID: The operator to apply to the field VirtualNetworkID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkID: The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkID: If op_VirtualNetworkID is specified, the field named in this input will be compared to the value in VirtualNetworkID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkID must be specified if op_VirtualNetworkID is specified.
             :type val_f_VirtualNetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkID: If op_VirtualNetworkID is specified, this value will be compared to the value in VirtualNetworkID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkID must be specified if op_VirtualNetworkID is specified.
             :type val_c_VirtualNetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkingInd: The operator to apply to the field VirtualNetworkingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkingInd: Set to null, 0 or 1.  0 indicates this is not a VRF Aware device.  1 Indicates it is VRF Aware. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkingInd: If op_VirtualNetworkingInd is specified, the field named in this input will be compared to the value in VirtualNetworkingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkingInd must be specified if op_VirtualNetworkingInd is specified.
             :type val_f_VirtualNetworkingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkingInd: If op_VirtualNetworkingInd is specified, this value will be compared to the value in VirtualNetworkingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkingInd must be specified if op_VirtualNetworkingInd is specified.
             :type val_c_VirtualNetworkingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_available_mgmt_ips: The operator to apply to the field available_mgmt_ips. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. available_mgmt_ips: Available Management IPs for a device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_available_mgmt_ips: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_available_mgmt_ips: If op_available_mgmt_ips is specified, the field named in this input will be compared to the value in available_mgmt_ips using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_available_mgmt_ips must be specified if op_available_mgmt_ips is specified.
             :type val_f_available_mgmt_ips: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_available_mgmt_ips: If op_available_mgmt_ips is specified, this value will be compared to the value in available_mgmt_ips using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_available_mgmt_ips must be specified if op_available_mgmt_ips is specified.
             :type val_c_available_mgmt_ips: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_admin_status_ind: The operator to apply to the field cap_admin_status_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_admin_status_ind: Capability of changing the Admin Status of an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_admin_status_na_reason: The operator to apply to the field cap_admin_status_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_admin_status_na_reason: Reason of non ability of changing the Admin Status of an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_description_ind: The operator to apply to the field cap_description_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_description_ind: Capability of changing the description of an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_description_na_reason: The operator to apply to the field cap_description_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_description_na_reason: Reason of non ability of changing the description of an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_deprovisioning_ind: The operator to apply to the field cap_net_deprovisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_deprovisioning_ind: Capability of de-provisioning a network from this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_deprovisioning_na_reason: The operator to apply to the field cap_net_deprovisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_deprovisioning_na_reason: Reason of non ability of de-provisioning a network from this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_provisioning_ind: The operator to apply to the field cap_net_provisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_provisioning_ind: Capability of provisioning a network on an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_provisioning_na_reason: The operator to apply to the field cap_net_provisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_provisioning_na_reason: Reason of non ability of provisioning a network on an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_vlan_provisioning_ind: The operator to apply to the field cap_net_vlan_provisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_vlan_provisioning_ind: Capability of creating a VLAN and provision a netowrk on its virtual interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_net_vlan_provisioning_na_reason: The operator to apply to the field cap_net_vlan_provisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_net_vlan_provisioning_na_reason: Reason of non ability of creating a VLAN and provision a netowrk on its virtual interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_vlan_assignment_ind: The operator to apply to the field cap_vlan_assignment_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_vlan_assignment_ind: Capability of assigning a regular data VLAN to an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_vlan_assignment_na_reason: The operator to apply to the field cap_vlan_assignment_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_vlan_assignment_na_reason: Reason of non ability of assigning a regular data VLAN to an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_voice_vlan_ind: The operator to apply to the field cap_voice_vlan_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_voice_vlan_ind: Capability of assigning a voice VLAN to an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cap_voice_vlan_na_reason: The operator to apply to the field cap_voice_vlan_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_voice_vlan_na_reason: Reason of non ability of assigning a voice VLAN to an interface of this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_chassis_serial_number: The operator to apply to the field chassis_serial_number. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. chassis_serial_number: The combined comma separated serial numbers reported by the chassis snmp MIB. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_chassis_serial_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_chassis_serial_number: If op_chassis_serial_number is specified, the field named in this input will be compared to the value in chassis_serial_number using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_chassis_serial_number must be specified if op_chassis_serial_number is specified.
             :type val_f_chassis_serial_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_chassis_serial_number: If op_chassis_serial_number is specified, this value will be compared to the value in chassis_serial_number using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_chassis_serial_number must be specified if op_chassis_serial_number is specified.
             :type val_c_chassis_serial_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_privileged_polling: The operator to apply to the field privileged_polling. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. privileged_polling: A flag indicating whether to poll the device in privileged mode. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_rawSysDescr: The operator to apply to the field rawSysDescr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. rawSysDescr: Unprocessed Device Description value as returned by SNMP For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_rawSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_rawSysDescr: If op_rawSysDescr is specified, the field named in this input will be compared to the value in rawSysDescr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_rawSysDescr must be specified if op_rawSysDescr is specified.
             :type val_f_rawSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_rawSysDescr: If op_rawSysDescr is specified, this value will be compared to the value in rawSysDescr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_rawSysDescr must be specified if op_rawSysDescr is specified.
             :type val_c_rawSysDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_rawSysModel: The operator to apply to the field rawSysModel. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. rawSysModel: Unprocessed Device Model value as returned by SNMP For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_rawSysModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_rawSysModel: If op_rawSysModel is specified, the field named in this input will be compared to the value in rawSysModel using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_rawSysModel must be specified if op_rawSysModel is specified.
             :type val_f_rawSysModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_rawSysModel: If op_rawSysModel is specified, this value will be compared to the value in rawSysModel using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_rawSysModel must be specified if op_rawSysModel is specified.
             :type val_c_rawSysModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_rawSysVersion: The operator to apply to the field rawSysVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. rawSysVersion: Unprocessed Device Version value as returned by SNMP For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_rawSysVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_rawSysVersion: If op_rawSysVersion is specified, the field named in this input will be compared to the value in rawSysVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_rawSysVersion must be specified if op_rawSysVersion is specified.
             :type val_f_rawSysVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_rawSysVersion: If op_rawSysVersion is specified, this value will be compared to the value in rawSysVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_rawSysVersion must be specified if op_rawSysVersion is specified.
             :type val_c_rawSysVersion: String

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

             :param timestamp: The data returned will represent the infra devices as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of infra device methods. The listed methods will be called on each infra device returned and included in the output. Available methods are: DeviceCommunitySecure, DeviceRank, DeviceCommunity, DeviceFirstOccurrence, group, parent_device, gateway_device, running_config, running_config_text, saved_config, saved_config_text, running_config_diff, saved_config_diff, virtual_child_count, asset_type, device_setting, data_collection_status, control_capabilities, network_name, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, privileged_polling, DeviceStartTime, DeviceEndTime, cap_description_ind, cap_admin_status_ind, cap_vlan_assignment_ind, cap_voice_vlan_ind, cap_net_provisioning_ind, cap_net_vlan_provisioning_ind, cap_net_deprovisioning_ind, cap_description_na_reason, cap_admin_status_na_reason, cap_vlan_assignment_na_reason, cap_voice_vlan_na_reason, cap_net_provisioning_na_reason, cap_net_vlan_provisioning_na_reason, cap_net_deprovisioning_na_reason, chassis_serial_number, available_mgmt_ips, rawSysDescr, rawSysVersion, rawSysModel, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device, device_setting, data_collection_status, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, data_source, device.
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

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey.
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

             :param select: The list of attributes to return for each InfraDevice. Valid values are DataSourceID, DeviceID, InfraDeviceStartTime, InfraDeviceEndTime, InfraDeviceChangedCols, DeviceIPDotted, DeviceIPNumeric, DeviceName, DeviceType, DeviceAssurance, DeviceVendor, DeviceModel, DeviceVersion, DeviceSysName, DeviceSysDescr, DeviceSysLocation, DeviceSysContact, DeviceDNSName, DeviceConfigTimestamp, DeviceFirstOccurrenceTime, InfraDeviceTimestamp, DeviceSAAVersion, DeviceRebootTime, DeviceRunningConfigLastChangedTime, DeviceSavedConfigLastChangedTime, DeviceConfigLastCheckedTime, DevicePolicyScheduleMode, DeviceAddlInfo, DeviceMAC, ParentDeviceID, DeviceContextName, DeviceNetBIOSName, DeviceOUI, MgmtServerDeviceID, NetworkDeviceInd, RoutingInd, SwitchingInd, VirtualInd, FilteringInd, FilterProvisionData, VirtualNetworkID, VirtualNetworkingInd, DeviceUniqueKey. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param detail_ind: A flag to indicate whether discovery times should be included or not
             :type detail_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return infra_devices: An array of the InfraDevice objects that match the specified input criteria.
             :rtype infra_devices: Array of InfraDevice

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified infra device.

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

             :param methods: A list of infra device methods. The listed methods will be called on each infra device returned and included in the output. Available methods are: DeviceCommunitySecure, DeviceRank, DeviceCommunity, DeviceFirstOccurrence, group, parent_device, gateway_device, running_config, running_config_text, saved_config, saved_config_text, running_config_diff, saved_config_diff, virtual_child_count, asset_type, device_setting, data_collection_status, control_capabilities, network_name, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, privileged_polling, DeviceStartTime, DeviceEndTime, cap_description_ind, cap_admin_status_ind, cap_vlan_assignment_ind, cap_voice_vlan_ind, cap_net_provisioning_ind, cap_net_vlan_provisioning_ind, cap_net_deprovisioning_ind, cap_description_na_reason, cap_admin_status_na_reason, cap_vlan_assignment_na_reason, cap_voice_vlan_na_reason, cap_net_provisioning_na_reason, cap_net_vlan_provisioning_na_reason, cap_net_deprovisioning_na_reason, chassis_serial_number, available_mgmt_ips, rawSysDescr, rawSysVersion, rawSysModel, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device, device_setting, data_collection_status, interfaces, issue_details, device_routes, device_physicals, if_addrs, config_revisions, detected_changes, device_ports, data_source, device.
             :type include: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param detail_ind: A flag to indicate whether discovery times should be included or not
             :type detail_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return infra_device: The infra device identified by the specified DeviceID.
             :rtype infra_device: InfraDevice

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def update(self, **kwargs):
        """Updates an existing infra device.

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

             :return id: The id of the updated infra device.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated infra device.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated infra device.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return infra_device: The updated infra device.
             :rtype infra_device: InfraDevice

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

    def chassis_serial_number(self, **kwargs):
        """The combined comma separated serial numbers reported by the chassis snmp MIB.

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

             :return : The combined comma separated serial numbers reported by the chassis snmp MIB.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("chassis_serial_number"), kwargs)

    def available_mgmt_ips(self, **kwargs):
        """Available Management IPs for a device.

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

             :return : Available Management IPs for a device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("available_mgmt_ips"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

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

             :return : The NetMRI device that collected this record.
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

    def device(self, **kwargs):
        """The general Device object corresponding to this infrastructure device.

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

             :return : The general Device object corresponding to this infrastructure device.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

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

    def device_setting(self, **kwargs):
        """The settings information for this device

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

             :return : The settings information for this device
             :rtype : DeviceSetting

            """

        return self.api_request(self._get_method_fullname("device_setting"), kwargs)

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
        """Capabilities of configuring the interfaces of this device.

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

             :return : Capabilities of configuring the interfaces of this device.
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

    def rawSysModel(self, **kwargs):
        """Unprocessed Device Model value as returned by SNMP

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

             :return : Unprocessed Device Model value as returned by SNMP
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("rawSysModel"), kwargs)

    def rawSysVersion(self, **kwargs):
        """Unprocessed Device Version value as returned by SNMP

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

             :return : Unprocessed Device Version value as returned by SNMP
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("rawSysVersion"), kwargs)

    def rawSysDescr(self, **kwargs):
        """Unprocessed Device Description value as returned by SNMP

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

             :return : Unprocessed Device Description value as returned by SNMP
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("rawSysDescr"), kwargs)
