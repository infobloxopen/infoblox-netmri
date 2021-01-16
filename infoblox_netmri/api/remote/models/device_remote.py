from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceRemote(RemoteModel):
    """
    The devices discovered by NetMRI.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` An internal NetMRI identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``DeviceEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DeviceChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

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

    |  ``DeviceDNSName:`` The device name as reported by DNS.
    |  ``attribute type:`` string

    |  ``DeviceFirstOccurrenceTime:`` The date/time that this device was first seen on the network.
    |  ``attribute type:`` datetime

    |  ``DeviceTimestamp:`` The date and time this record was collected.
    |  ``attribute type:`` datetime

    |  ``DeviceAddlInfo:`` Additional information about the device; IP phones will contain the extension in this field.
    |  ``attribute type:`` string

    |  ``DeviceMAC:`` The MAC of the interface corresponding to the management IP, if available. Otherwise, it is the lowest numbered non-zero MAC for any interface on the device. If no interface records are available for the device, the lowest non-zero MAC address corresponding to the management IP address found in the global ARP table will be used.
    |  ``attribute type:`` string

    |  ``ParentDeviceID:`` The internal NetMRI identifier for the device containing this virtual device.
    |  ``attribute type:`` number

    |  ``DeviceNetBIOSName:`` The NetBIOS name of the device.
    |  ``attribute type:`` string

    |  ``DeviceOUI:`` The NetMRI-determined device vendor using OUI.
    |  ``attribute type:`` string

    |  ``InfraDeviceInd:`` A flag indicating whether this device is an infrastructure device or not.
    |  ``attribute type:`` bool

    |  ``NetworkDeviceInd:`` A flag indicating whether this device is a network device or an end host.
    |  ``attribute type:`` bool

    |  ``VirtualInd:`` A flag indicating if the source device is a virtual device.
    |  ``attribute type:`` bool

    |  ``DeviceSysContact:`` The contact information of a device.
    |  ``attribute type:`` string




    |  ``running_config_text:`` The contents of the newest saved running config.
    |  ``attribute type:`` string

    |  ``saved_config_text:`` The contents of the newest saved startup config.
    |  ``attribute type:`` string




    |  ``running_config_diff:`` The differences between the current and previous running config.
    |  ``attribute type:`` string

    |  ``saved_config_diff:`` The differences between the current and previous saved config.
    |  ``attribute type:`` string

    |  ``asset_type:`` The physical/virtual aspect of the device (Virtual Host, Virtual Device, or Physical Device).
    |  ``attribute type:`` string

    |  ``SwitchingInd:`` A flag indicating if this device act as a switcher
    |  ``attribute type:`` bool

    |  ``RoutingInd:`` A flag indicating if this device act as a router
    |  ``attribute type:`` bool

    |  ``DeviceSAAVersion:`` the SAA version of this device
    |  ``attribute type:`` string

    |  ``DeviceRebootTime:`` the reboot time of this device
    |  ``attribute type:`` datetime

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


    |  ``DeviceContextName:`` The name of the virtual context of this virtual device.
    |  ``attribute type:`` string

    |  ``MgmtServerDeviceID:`` The Device ID of the management server for the device
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal NetMRI identifier of the Virtual Network on which this device is defined, or blank if this cannot be determined.
    |  ``attribute type:`` number

    |  ``DeviceUniqueKey:`` Unique key which allows duplicates detecting over different Virtual Networks.
    |  ``attribute type:`` string


    |  ``network_name:`` A Network View assigned to the device.
    |  ``attribute type:`` string









    |  ``control_capabilities:`` Configuration capabilities for this interface, related to Port Control.
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


    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "DeviceStartTime",
                  "DeviceEndTime",
                  "DeviceChangedCols",
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
                  "DeviceDNSName",
                  "DeviceFirstOccurrenceTime",
                  "DeviceTimestamp",
                  "DeviceAddlInfo",
                  "DeviceMAC",
                  "ParentDeviceID",
                  "DeviceNetBIOSName",
                  "DeviceOUI",
                  "InfraDeviceInd",
                  "NetworkDeviceInd",
                  "VirtualInd",
                  "DeviceSysContact",
                  "running_config_text",
                  "saved_config_text",
                  "running_config_diff",
                  "saved_config_diff",
                  "asset_type",
                  "SwitchingInd",
                  "RoutingInd",
                  "DeviceSAAVersion",
                  "DeviceRebootTime",
                  "DeviceCommunitySecure",
                  "DeviceRank",
                  "DeviceCommunity",
                  "DeviceFirstOccurrence",
                  "virtual_child_count",
                  "DeviceContextName",
                  "MgmtServerDeviceID",
                  "VirtualNetworkID",
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
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
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
    def device_setting(self):
        """
        Returns settings for selected device
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
    def virtual_network(self):
        """
        A Virtual Network model assigned to the device.
        ``attribute type:`` model
        """
        return self.broker.virtual_network(**{"DeviceID": self.DeviceID})

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
    def interfaces(self):
        """
        Returns an array of interfaces for this device, if available.
        ``attribute type:`` model
        """
        return self.broker.interfaces(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def if_addrs(self):
        """
        Returns an array of interface IP addresses for this device, if available. If interfaces have not been collected for this device, there will be no data returned.
        ``attribute type:`` model
        """
        return self.broker.if_addrs(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_routes(self):
        """
        Returns an array of routing table entries for this device, if available.
        ``attribute type:`` model
        """
        return self.broker.device_routes(**{"DeviceID": self.DeviceID})

    @property
    @check_api_availability
    def device_physicals(self):
        """
        Returns an array of physical components for this device, if available.
        ``attribute type:`` model
        """
        return self.broker.device_physicals(**{"DeviceID": self.DeviceID})

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

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"DeviceID": self.DeviceID})
