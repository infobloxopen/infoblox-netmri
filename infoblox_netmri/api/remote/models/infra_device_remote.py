from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class InfraDeviceRemote(RemoteModel):
    """
    The infrastructure devices discovered by NetMRI.


    |  ``DeviceID:`` An internal NetMRI identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``DeviceName:`` The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` The assurance level of the device type value.
    |  ``attribute type:`` number

    |  ``DeviceVendor:`` The device vendor name.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The device model name.
    |  ``attribute type:`` string

    |  ``DeviceVersion:`` The device OS version.
    |  ``attribute type:`` string

    |  ``DeviceSysName:`` The device name as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceSysDescr:`` The device sysDescr as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceSysLocation:`` The device sysLocation as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceSysContact:`` The Device sysContact as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceDNSName:`` The device name as reported by DNS.
    |  ``attribute type:`` string

    |  ``DeviceFirstOccurrenceTime:`` The date/time that this device was first seen on the network.
    |  ``attribute type:`` datetime

    |  ``DeviceSAAVersion:`` The SAA version running on this device.
    |  ``attribute type:`` string

    |  ``DeviceRebootTime:`` The date/time this device was last rebooted.
    |  ``attribute type:`` datetime

    |  ``DeviceRunningConfigLastChangedTime:`` The date/time, as reported by SNMP, that the device's running configuration was last changed.
    |  ``attribute type:`` datetime

    |  ``DeviceSavedConfigLastChangedTime:`` The date/time, as reported by SNMP, that the device's saved configuration was last changed.
    |  ``attribute type:`` datetime

    |  ``DeviceConfigLastCheckedTime:`` The date/time of the last attempted retrieval of the device's configuration file.
    |  ``attribute type:`` datetime

    |  ``DevicePolicyScheduleMode:`` Not currently used.
    |  ``attribute type:`` string

    |  ``DeviceAddlInfo:`` Additional information about the device; IP phones will contain the extension in this field.
    |  ``attribute type:`` string

    |  ``DeviceMAC:`` The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
    |  ``attribute type:`` string

    |  ``ParentDeviceID:`` The internal NetMRI identifier for the device containing this virtual device.
    |  ``attribute type:`` number

    |  ``DeviceContextName:`` The name of the virtual context of this virtual device.
    |  ``attribute type:`` string

    |  ``DeviceNetBIOSName:`` The NetBIOS name of the device.
    |  ``attribute type:`` string

    |  ``DeviceOUI:`` The NetMRI-determined device vendor using OUI.
    |  ``attribute type:`` string

    |  ``NetworkDeviceInd:`` A flag indicating whether this device is a network device or an end host.
    |  ``attribute type:`` bool

    |  ``RoutingInd:`` A flag indicating whether this device is configured with any routing capability and whether a routing table was retrieved from this device.
    |  ``attribute type:`` bool

    |  ``SwitchingInd:`` A flag indicating whether a switch port forwarding table was retrieved from this device.
    |  ``attribute type:`` bool

    |  ``VirtualInd:`` A flag indicating if the source device is a virtual device.
    |  ``attribute type:`` bool

    |  ``chassis_serial_number:`` The combined comma separated serial numbers reported by the chassis snmp MIB.
    |  ``attribute type:`` string

    |  ``available_mgmt_ips:`` Available Management IPs for a device.
    |  ``attribute type:`` string

    |  ``InfraDeviceTimestamp:`` The date and time this record was collected.
    |  ``attribute type:`` datetime

    |  ``DeviceConfigTimestamp:`` The date/time the configuration file was last successfully retrieved for this device.
    |  ``attribute type:`` datetime

    |  ``InfraDeviceStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``InfraDeviceEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``InfraDeviceChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number





    |  ``running_config_text:`` The contents of the newest saved running config.
    |  ``attribute type:`` string

    |  ``saved_config_text:`` The contents of the newest saved startup config.
    |  ``attribute type:`` string




    |  ``asset_type:`` The physical/virtual aspect of the device (Virtual Host, Virtual Device, or Physical Device).
    |  ``attribute type:`` string

    |  ``FilteringInd:`` A flag indicating whether this device is eligible for Security Device Controller
    |  ``attribute type:`` bool

    |  ``FilterProvisionData:``  Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string

    |  ``DeviceCommunitySecure:`` The secured community name
    |  ``attribute type:`` string

    |  ``DeviceRank:`` The rank of this device in its virtual brotherhood
    |  ``attribute type:`` number

    |  ``DeviceCommunity:`` The community string.
    |  ``attribute type:`` string

    |  ``DeviceFirstOccurrence:`` The first occurrence of this device
    |  ``attribute type:`` datetime

    |  ``virtual_child_count:`` The number of virtual devices hosted on this device
    |  ``attribute type:`` number



    |  ``DeviceStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DeviceEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``running_config_diff:`` The differences between the current and previous running config.
    |  ``attribute type:`` string

    |  ``saved_config_diff:`` The differences between the current and previous saved config.
    |  ``attribute type:`` string

    |  ``MgmtServerDeviceID:`` The Device ID of the management server for the device
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
    |  ``attribute type:`` number

    |  ``VirtualNetworkingInd:`` Set to null, 0 or 1.  0 indicates this is not a VRF Aware device.  1 Indicates it is VRF Aware.
    |  ``attribute type:`` bool

    |  ``DeviceUniqueKey:`` Unique key which allows duplicates detecting over different Virtual Networks.
    |  ``attribute type:`` string

    |  ``network_name:`` A Network View assigned to the device.
    |  ``attribute type:`` string









    |  ``control_capabilities:`` Capabilities of configuring the interfaces of this device.
    |  ``attribute type:`` string

    |  ``cap_description_ind:`` Capability of changing the description of an interface of this device.
    |  ``attribute type:`` bool

    |  ``cap_admin_status_ind:`` Capability of changing the Admin Status of an interface of this device.
    |  ``attribute type:`` bool

    |  ``cap_vlan_assignment_ind:`` Capability of assigning a regular data VLAN to an interface of this device.
    |  ``attribute type:`` bool

    |  ``cap_voice_vlan_ind:`` Capability of assigning a voice VLAN to an interface of this device.
    |  ``attribute type:`` bool

    |  ``cap_net_provisioning_ind:`` Capability of provisioning a network on an interface of this device.
    |  ``attribute type:`` bool

    |  ``cap_net_vlan_provisioning_ind:`` Capability of creating a VLAN and provision a netowrk on its virtual interface.
    |  ``attribute type:`` bool

    |  ``cap_net_deprovisioning_ind:`` Capability of de-provisioning a network from this device.
    |  ``attribute type:`` bool

    |  ``cap_description_na_reason:`` Reason of non ability of changing the description of an interface of this device.
    |  ``attribute type:`` string

    |  ``cap_admin_status_na_reason:`` Reason of non ability of changing the Admin Status of an interface of this device.
    |  ``attribute type:`` string

    |  ``cap_vlan_assignment_na_reason:`` Reason of non ability of assigning a regular data VLAN to an interface of this device.
    |  ``attribute type:`` string

    |  ``cap_voice_vlan_na_reason:`` Reason of non ability of assigning a voice VLAN to an interface of this device.
    |  ``attribute type:`` string

    |  ``cap_net_provisioning_na_reason:`` Reason of non ability of provisioning a network on an interface of this device.
    |  ``attribute type:`` string

    |  ``cap_net_vlan_provisioning_na_reason:`` Reason of non ability of creating a VLAN and provision a netowrk on its virtual interface.
    |  ``attribute type:`` string

    |  ``cap_net_deprovisioning_na_reason:`` Reason of non ability of de-provisioning a network from this device.
    |  ``attribute type:`` string

    |  ``privileged_polling:`` A flag indicating whether to poll the device in privileged mode.
    |  ``attribute type:`` bool

    |  ``rawSysModel:`` Unprocessed Device Model value as returned by SNMP
    |  ``attribute type:`` string

    |  ``rawSysVersion:`` Unprocessed Device Version value as returned by SNMP
    |  ``attribute type:`` string

    |  ``rawSysDescr:`` Unprocessed Device Description value as returned by SNMP
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceType",
                  "DeviceAssurance",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceVersion",
                  "DeviceSysName",
                  "DeviceSysDescr",
                  "DeviceSysLocation",
                  "DeviceSysContact",
                  "DeviceDNSName",
                  "DeviceFirstOccurrenceTime",
                  "DeviceSAAVersion",
                  "DeviceRebootTime",
                  "DeviceRunningConfigLastChangedTime",
                  "DeviceSavedConfigLastChangedTime",
                  "DeviceConfigLastCheckedTime",
                  "DevicePolicyScheduleMode",
                  "DeviceAddlInfo",
                  "DeviceMAC",
                  "ParentDeviceID",
                  "DeviceContextName",
                  "DeviceNetBIOSName",
                  "DeviceOUI",
                  "NetworkDeviceInd",
                  "RoutingInd",
                  "SwitchingInd",
                  "VirtualInd",
                  "chassis_serial_number",
                  "available_mgmt_ips",
                  "InfraDeviceTimestamp",
                  "DeviceConfigTimestamp",
                  "InfraDeviceStartTime",
                  "InfraDeviceEndTime",
                  "InfraDeviceChangedCols",
                  "DataSourceID",
                  "running_config_text",
                  "saved_config_text",
                  "asset_type",
                  "FilteringInd",
                  "FilterProvisionData",
                  "DeviceCommunitySecure",
                  "DeviceRank",
                  "DeviceCommunity",
                  "DeviceFirstOccurrence",
                  "virtual_child_count",
                  "DeviceStartTime",
                  "DeviceEndTime",
                  "running_config_diff",
                  "saved_config_diff",
                  "MgmtServerDeviceID",
                  "VirtualNetworkID",
                  "VirtualNetworkingInd",
                  "DeviceUniqueKey",
                  "network_name",
                  "control_capabilities",
                  "cap_description_ind",
                  "cap_admin_status_ind",
                  "cap_vlan_assignment_ind",
                  "cap_voice_vlan_ind",
                  "cap_net_provisioning_ind",
                  "cap_net_vlan_provisioning_ind",
                  "cap_net_deprovisioning_ind",
                  "cap_description_na_reason",
                  "cap_admin_status_na_reason",
                  "cap_vlan_assignment_na_reason",
                  "cap_voice_vlan_na_reason",
                  "cap_net_provisioning_na_reason",
                  "cap_net_vlan_provisioning_na_reason",
                  "cap_net_deprovisioning_na_reason",
                  "privileged_polling",
                  "rawSysModel",
                  "rawSysVersion",
                  "rawSysDescr",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def group(self):
        """
        Returns an array of device groups to which this device belongs.
        ``attribute type:`` model
        """
        return self.broker.group(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def parent_device(self):
        """
        The device containing this virtual device.
        ``attribute type:`` model
        """
        return self.broker.parent_device(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def gateway_device(self):
        """
        Returns the default gateway router for this device, based on the following in order of preference: device routing table, device configuration file, device subnet and common conventions.
        ``attribute type:`` model
        """
        return self.broker.gateway_device(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def running_config(self):
        """
        Returns the ConfigRevision object corresponding to the device's current running configuration.
        ``attribute type:`` model
        """
        return self.broker.running_config(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def saved_config(self):
        """
        Returns the ConfigRevision object corresponding to the device's current startup configuration.
        ``attribute type:`` model
        """
        return self.broker.saved_config(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device(self):
        """
        The general Device object corresponding to this infrastructure device.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_setting(self):
        """
        The settings information for this device
        ``attribute type:`` model
        """
        return self.broker.device_setting(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def data_collection_status(self):
        """
        All information about collection of data for this device
        ``attribute type:`` model
        """
        return self.broker.data_collection_status(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def interfaces(self):
        """
        Returns an array of interfaces for this device.
        ``attribute type:`` model
        """
        return self.broker.interfaces(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_physicals(self):
        """
        Returns an array of physical components for this device.
        ``attribute type:`` model
        """
        return self.broker.device_physicals(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_routes(self):
        """
        Returns an array of routing table entries for this device.
        ``attribute type:`` model
        """
        return self.broker.device_routes(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def if_addrs(self):
        """
        Returns an array of interface IP addresses for this device.
        ``attribute type:`` model
        """
        return self.broker.if_addrs(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def issue_details(self):
        """
        Returns an array of issues for this device.
        ``attribute type:`` model
        """
        return self.broker.issue_details(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_ports(self):
        """
        Returns an array of open TCP/UDP ports on this device.
        ``attribute type:`` model
        """
        return self.broker.device_ports(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def config_revisions(self):
        """
        Returns an array of cofiguration revisions on this device.
        ``attribute type:`` model
        """
        return self.broker.config_revisions(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def detected_changes(self):
        """
        Returns an array of detected changes on this device.
        ``attribute type:`` model
        """
        return self.broker.detected_changes(**{"DeviceID": self.DeviceID})
