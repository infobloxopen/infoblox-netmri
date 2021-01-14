from ..broker import Broker


class InterfaceBroker(Broker):
    controller = "interfaces"

    def show(self, **kwargs):
        """Shows the details for the specified interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of interface methods. The listed methods will be called on each interface returned and included in the output. Available methods are: cap_if_description_ind, cap_if_admin_status_ind, cap_if_vlan_assignment_ind, cap_if_voice_vlan_ind, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, cap_itf_net_deprovisioning_ind, cap_if_description_na_reason, cap_if_admin_status_na_reason, cap_if_vlan_assignment_na_reason, cap_if_voice_vlan_na_reason, cap_if_net_provisioning_ipv4_na_reason, cap_if_net_provisioning_ipv6_na_reason, cap_if_net_deprovisioning_ipv4_na_reason, cap_if_net_deprovisioning_ipv6_na_reason, cap_itf_net_deprovisioning_na_reason, aggr_interface, infradevice, ifphysaddress, control_capabilities, vrf_name, vrf_description, vrf_rd, network_id, aggr_interface_name, vpc_peer_ifname, vpc_peer_device_id, meta, network_name, data_source, device, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: aggr_interface, meta, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return interface: The interface identified by the specified InterfaceID.
             :rtype interface: Interface

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available interfaces. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AggrInterfaceID: The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.
             :type AggrInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AggrInterfaceID: The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.
             :type AggrInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this interface.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this interface.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined.
             :type VirtualNetworkMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifMAC: The interface Media Access Controller (MAC) address.
             :type ifMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifMAC: The interface Media Access Controller (MAC) address.
             :type ifMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifName: The name of this interface. This is typically the short name of the interface as it is identified in the console.
             :type ifName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifName: The name of this interface. This is typically the short name of the interface as it is identified in the console.
             :type ifName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifNameSort: The internal NetMRI name of this interface for sorting purpose.
             :type ifNameSort: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifNameSort: The internal NetMRI name of this interface for sorting purpose.
             :type ifNameSort: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifTrunkStatus: If "on", then this interface is a VLAN trunk port.
             :type ifTrunkStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifTrunkStatus: If "on", then this interface is a VLAN trunk port.
             :type ifTrunkStatus: Array of String

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

             :param timestamp: The data returned will represent the interfaces as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of interface methods. The listed methods will be called on each interface returned and included in the output. Available methods are: cap_if_description_ind, cap_if_admin_status_ind, cap_if_vlan_assignment_ind, cap_if_voice_vlan_ind, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, cap_itf_net_deprovisioning_ind, cap_if_description_na_reason, cap_if_admin_status_na_reason, cap_if_vlan_assignment_na_reason, cap_if_voice_vlan_na_reason, cap_if_net_provisioning_ipv4_na_reason, cap_if_net_provisioning_ipv6_na_reason, cap_if_net_deprovisioning_ipv4_na_reason, cap_if_net_deprovisioning_ipv6_na_reason, cap_itf_net_deprovisioning_na_reason, aggr_interface, infradevice, ifphysaddress, control_capabilities, vrf_name, vrf_description, vrf_rd, network_id, aggr_interface_name, vpc_peer_ifname, vpc_peer_device_id, meta, network_name, data_source, device, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: aggr_interface, meta, data_source, device.
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
            |  ``default:`` InterfaceID

             :param sort: The data field(s) to use for sorting the output. Default is InterfaceID. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount.
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

             :param select: The list of attributes to return for each Interface. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount. If empty or omitted, all attributes will be returned.
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

             :return interfaces: An array of the Interface objects that match the specified input criteria.
             :rtype interfaces: Array of Interface

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available interfaces matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AggrInterfaceID: The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.
             :type AggrInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AggrInterfaceID: The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members.
             :type AggrInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this interface.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing this interface.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DownstreamSwitchCount: The number of downstream switches for this interface (only available for switch ports).
             :type DownstreamSwitchCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DownstreamSwitchCount: The number of downstream switches for this interface (only available for switch ports).
             :type DownstreamSwitchCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PoEPower: Power draw of the supplied device in millivolts.
             :type PoEPower: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PoEPower: Power draw of the supplied device in millivolts.
             :type PoEPower: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PoEStatus: Status of the PoE connection.
             :type PoEStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PoEStatus: Status of the PoE connection.
             :type PoEStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Port: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
             :type Port: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Port: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
             :type Port: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Slot: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
             :type Slot: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Slot: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices.
             :type Slot: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortNumber: The switch port number from the dot1d bridge MIB for this interface.
             :type SwitchPortNumber: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SwitchPortNumber: The switch port number from the dot1d bridge MIB for this interface.
             :type SwitchPortNumber: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined.
             :type VirtualNetworkMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifAdminDuplex: Admin setting of duplex, Auto indicates the device will try to negotiate with the other end to determine.
             :type ifAdminDuplex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifAdminDuplex: Admin setting of duplex, Auto indicates the device will try to negotiate with the other end to determine.
             :type ifAdminDuplex: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifAdminStatus: The configured status (up/down) of the interface.
             :type ifAdminStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifAdminStatus: The configured status (up/down) of the interface.
             :type ifAdminStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifAggrMemberInd: A flag indicating whether or not this is a member interface in a link aggregation.
             :type ifAggrMemberInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifAggrMemberInd: A flag indicating whether or not this is a member interface in a link aggregation.
             :type ifAggrMemberInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifAlias: Interface alias.
             :type ifAlias: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifAlias: Interface alias.
             :type ifAlias: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifArtificialInd: Not currently used.
             :type ifArtificialInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifArtificialInd: Not currently used.
             :type ifArtificialInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifConnector: If "true" or "1", then this interface has a physical connector.
             :type ifConnector: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifConnector: If "true" or "1", then this interface has a physical connector.
             :type ifConnector: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifDescr: The description of the interface, as set in the device's configuration file.
             :type ifDescr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifDescr: The description of the interface, as set in the device's configuration file.
             :type ifDescr: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifDescrRaw: The raw description of the interface before any NetMRI processing.
             :type ifDescrRaw: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifDescrRaw: The raw description of the interface before any NetMRI processing.
             :type ifDescrRaw: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifDuplex: The operational duplex of this interface.
             :type ifDuplex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifDuplex: The operational duplex of this interface.
             :type ifDuplex: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifEncapsulationTag: Indicates the encapsulation Tag for this interface.
             :type ifEncapsulationTag: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifEncapsulationTag: Indicates the encapsulation Tag for this interface.
             :type ifEncapsulationTag: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifEncapsulationType: Indicates the encapsulation Type for this interface.
             :type ifEncapsulationType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifEncapsulationType: Indicates the encapsulation Type for this interface.
             :type ifEncapsulationType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type ifEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type ifEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifFirstSeenTime: The date and time this interface was first seen on the network, and since which it has been continuously present.
             :type ifFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifFirstSeenTime: The date and time this interface was first seen on the network, and since which it has been continuously present.
             :type ifFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index value of the interface.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index value of the interface.
             :type ifIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLastChange: The date/time of the last status change for this interface.
             :type ifLastChange: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLastChange: The date/time of the last status change for this interface.
             :type ifLastChange: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkAggrInd: A flag indicating whether or not this is a link aggregation (port channel, etherchannel, LACP, etc.) interface.
             :type ifLinkAggrInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkAggrInd: A flag indicating whether or not this is a link aggregation (port channel, etherchannel, LACP, etc.) interface.
             :type ifLinkAggrInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkAggrIndex: The port group or port channel number for link aggregations interface or their member interfaces.
             :type ifLinkAggrIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkAggrIndex: The port group or port channel number for link aggregations interface or their member interfaces.
             :type ifLinkAggrIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkTrap: If "enabled", this device is configured to send link up/down traps.
             :type ifLinkTrap: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLinkTrap: If "enabled", this device is configured to send link up/down traps.
             :type ifLinkTrap: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLowerLayer: The SNMP interface index of the lower-layer interface on which this interface is constructed.
             :type ifLowerLayer: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLowerLayer: The SNMP interface index of the lower-layer interface on which this interface is constructed.
             :type ifLowerLayer: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLowerLayerInterfaceID: The internal NetMRI identifier for the lower-layer interface on which this interface is constructed.
             :type ifLowerLayerInterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLowerLayerInterfaceID: The internal NetMRI identifier for the lower-layer interface on which this interface is constructed.
             :type ifLowerLayerInterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifMAC: The interface Media Access Controller (MAC) address.
             :type ifMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifMAC: The interface Media Access Controller (MAC) address.
             :type ifMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifMtu: The size of the largest packet or datagram which can be sent/received on the interface, specified in octets.
             :type ifMtu: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifMtu: The size of the largest packet or datagram which can be sent/received on the interface, specified in octets.
             :type ifMtu: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifName: The name of this interface. This is typically the short name of the interface as it is identified in the console.
             :type ifName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifName: The name of this interface. This is typically the short name of the interface as it is identified in the console.
             :type ifName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifNameSort: The internal NetMRI name of this interface for sorting purpose.
             :type ifNameSort: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifNameSort: The internal NetMRI name of this interface for sorting purpose.
             :type ifNameSort: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOperStatus: The operational status (up/down) of the interface.
             :type ifOperStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOperStatus: The operational status (up/down) of the interface.
             :type ifOperStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOperStatusChange: The date/time of the last operational status change (e.g. free or used) for this interface.
             :type ifOperStatusChange: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOperStatusChange: The date/time of the last operational status change (e.g. free or used) for this interface.
             :type ifOperStatusChange: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifPortControlInd: A flag indicating whether or not this interface is available for port control actions.
             :type ifPortControlInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifPortControlInd: A flag indicating whether or not this interface is available for port control actions.
             :type ifPortControlInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifPortFast: If "enabled" then port fast is active on the interface.
             :type ifPortFast: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifPortFast: If "enabled" then port fast is active on the interface.
             :type ifPortFast: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifSpeed: The operational speed, in bps, of this interface.
             :type ifSpeed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifSpeed: The operational speed, in bps, of this interface.
             :type ifSpeed: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifStartTime: The starting effective time of this revision of the record.
             :type ifStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifStartTime: The starting effective time of this revision of the record.
             :type ifStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifSwitchPortMgmtInd: A flag indicating whether or not this interface is available in switch port management views.
             :type ifSwitchPortMgmtInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifSwitchPortMgmtInd: A flag indicating whether or not this interface is available in switch port management views.
             :type ifSwitchPortMgmtInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifTimestamp: The date and time this record was collected or calculated.
             :type ifTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifTimestamp: The date and time this record was collected or calculated.
             :type ifTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifTrunkStatus: If "on", then this interface is a VLAN trunk port.
             :type ifTrunkStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifTrunkStatus: If "on", then this interface is a VLAN trunk port.
             :type ifTrunkStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifTunnelInd: A flag indicating whether or not this is a tunnel interface.
             :type ifTunnelInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifTunnelInd: A flag indicating whether or not this is a tunnel interface.
             :type ifTunnelInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifType: The interface type.
             :type ifType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifType: The interface type.
             :type ifType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifVirtualInd: A flag indicating whether or not this is a virtual interface.
             :type ifVirtualInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifVirtualInd: A flag indicating whether or not this is a virtual interface.
             :type ifVirtualInd: Array of Boolean

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

             :param timestamp: The data returned will represent the interfaces as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of interface methods. The listed methods will be called on each interface returned and included in the output. Available methods are: cap_if_description_ind, cap_if_admin_status_ind, cap_if_vlan_assignment_ind, cap_if_voice_vlan_ind, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, cap_itf_net_deprovisioning_ind, cap_if_description_na_reason, cap_if_admin_status_na_reason, cap_if_vlan_assignment_na_reason, cap_if_voice_vlan_na_reason, cap_if_net_provisioning_ipv4_na_reason, cap_if_net_provisioning_ipv6_na_reason, cap_if_net_deprovisioning_ipv4_na_reason, cap_if_net_deprovisioning_ipv6_na_reason, cap_itf_net_deprovisioning_na_reason, aggr_interface, infradevice, ifphysaddress, control_capabilities, vrf_name, vrf_description, vrf_rd, network_id, aggr_interface_name, vpc_peer_ifname, vpc_peer_device_id, meta, network_name, data_source, device, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: aggr_interface, meta, data_source, device.
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
            |  ``default:`` InterfaceID

             :param sort: The data field(s) to use for sorting the output. Default is InterfaceID. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount.
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

             :param select: The list of attributes to return for each Interface. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against interfaces, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: AggrInterfaceID, DataSourceID, DeviceID, DownstreamSwitchCount, InterfaceID, PoEPower, PoEStatus, Port, Slot, SwitchPortNumber, VirtualNetworkMemberID, ifAdminDuplex, ifAdminStatus, ifAggrMemberInd, ifAlias, ifArtificialInd, ifChangedCols, ifConnector, ifDescr, ifDescrRaw, ifDuplex, ifEncapsulationTag, ifEncapsulationType, ifEndTime, ifFirstSeenTime, ifIndex, ifLastChange, ifLinkAggrInd, ifLinkAggrIndex, ifLinkTrap, ifLowerLayer, ifLowerLayerInterfaceID, ifMAC, ifMtu, ifName, ifNameSort, ifOperStatus, ifOperStatusChange, ifPortControlInd, ifPortFast, ifSpeed, ifStartTime, ifSwitchPortMgmtInd, ifTimestamp, ifTrunkStatus, ifTunnelInd, ifType, ifVirtualInd.
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

             :return interfaces: An array of the Interface objects that match the specified input criteria.
             :rtype interfaces: Array of Interface

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available interfaces matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: AggrInterfaceID, DataSourceID, DeviceID, DownstreamSwitchCount, InterfaceID, PoEPower, PoEStatus, Port, Slot, SwitchPortNumber, VirtualNetworkMemberID, ifAdminDuplex, ifAdminStatus, ifAggrMemberInd, ifAlias, ifArtificialInd, ifChangedCols, ifConnector, ifDescr, ifDescrRaw, ifDuplex, ifEncapsulationTag, ifEncapsulationType, ifEndTime, ifFirstSeenTime, ifIndex, ifLastChange, ifLinkAggrInd, ifLinkAggrIndex, ifLinkTrap, ifLowerLayer, ifLowerLayerInterfaceID, ifMAC, ifMtu, ifName, ifNameSort, ifOperStatus, ifOperStatusChange, ifPortControlInd, ifPortFast, ifSpeed, ifStartTime, ifSwitchPortMgmtInd, ifTimestamp, ifTrunkStatus, ifTunnelInd, ifType, ifVirtualInd.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AggrInterfaceID: The operator to apply to the field AggrInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AggrInterfaceID: The internal NetMRI identifier for the 'owning' link aggregation interface for link aggregate members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AggrInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AggrInterfaceID: If op_AggrInterfaceID is specified, the field named in this input will be compared to the value in AggrInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AggrInterfaceID must be specified if op_AggrInterfaceID is specified.
             :type val_f_AggrInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AggrInterfaceID: If op_AggrInterfaceID is specified, this value will be compared to the value in AggrInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AggrInterfaceID must be specified if op_AggrInterfaceID is specified.
             :type val_c_AggrInterfaceID: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device containing this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DownstreamSwitchCount: The operator to apply to the field DownstreamSwitchCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DownstreamSwitchCount: The number of downstream switches for this interface (only available for switch ports). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DownstreamSwitchCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DownstreamSwitchCount: If op_DownstreamSwitchCount is specified, the field named in this input will be compared to the value in DownstreamSwitchCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DownstreamSwitchCount must be specified if op_DownstreamSwitchCount is specified.
             :type val_f_DownstreamSwitchCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DownstreamSwitchCount: If op_DownstreamSwitchCount is specified, this value will be compared to the value in DownstreamSwitchCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DownstreamSwitchCount must be specified if op_DownstreamSwitchCount is specified.
             :type val_c_DownstreamSwitchCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PoEPower: The operator to apply to the field PoEPower. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PoEPower: Power draw of the supplied device in millivolts. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PoEPower: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PoEPower: If op_PoEPower is specified, the field named in this input will be compared to the value in PoEPower using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PoEPower must be specified if op_PoEPower is specified.
             :type val_f_PoEPower: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PoEPower: If op_PoEPower is specified, this value will be compared to the value in PoEPower using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PoEPower must be specified if op_PoEPower is specified.
             :type val_c_PoEPower: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PoEStatus: The operator to apply to the field PoEStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PoEStatus: Status of the PoE connection. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PoEStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PoEStatus: If op_PoEStatus is specified, the field named in this input will be compared to the value in PoEStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PoEStatus must be specified if op_PoEStatus is specified.
             :type val_f_PoEStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PoEStatus: If op_PoEStatus is specified, this value will be compared to the value in PoEStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PoEStatus must be specified if op_PoEStatus is specified.
             :type val_c_PoEStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Port: The operator to apply to the field Port. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Port: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Port: If op_Port is specified, the field named in this input will be compared to the value in Port using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Port must be specified if op_Port is specified.
             :type val_f_Port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Port: If op_Port is specified, this value will be compared to the value in Port using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Port must be specified if op_Port is specified.
             :type val_c_Port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Slot: The operator to apply to the field Slot. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Slot: The slot of the interface, ONLY determined for SwitchPort management for Power Over Ethernet devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Slot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Slot: If op_Slot is specified, the field named in this input will be compared to the value in Slot using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Slot must be specified if op_Slot is specified.
             :type val_f_Slot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Slot: If op_Slot is specified, this value will be compared to the value in Slot using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Slot must be specified if op_Slot is specified.
             :type val_c_Slot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SwitchPortNumber: The operator to apply to the field SwitchPortNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SwitchPortNumber: The switch port number from the dot1d bridge MIB for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SwitchPortNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SwitchPortNumber: If op_SwitchPortNumber is specified, the field named in this input will be compared to the value in SwitchPortNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SwitchPortNumber must be specified if op_SwitchPortNumber is specified.
             :type val_f_SwitchPortNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SwitchPortNumber: If op_SwitchPortNumber is specified, this value will be compared to the value in SwitchPortNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SwitchPortNumber must be specified if op_SwitchPortNumber is specified.
             :type val_c_SwitchPortNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberID: The operator to apply to the field VirtualNetworkMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberID: The internal NetMRI identifier of the Virtual Network Member on which this interface is defined, or blank if this cannot be determined. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberID: If op_VirtualNetworkMemberID is specified, the field named in this input will be compared to the value in VirtualNetworkMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberID must be specified if op_VirtualNetworkMemberID is specified.
             :type val_f_VirtualNetworkMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberID: If op_VirtualNetworkMemberID is specified, this value will be compared to the value in VirtualNetworkMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberID must be specified if op_VirtualNetworkMemberID is specified.
             :type val_c_VirtualNetworkMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggr_interface_name: The operator to apply to the field aggr_interface_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggr_interface_name: The name of aggregated interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggr_interface_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggr_interface_name: If op_aggr_interface_name is specified, the field named in this input will be compared to the value in aggr_interface_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggr_interface_name must be specified if op_aggr_interface_name is specified.
             :type val_f_aggr_interface_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggr_interface_name: If op_aggr_interface_name is specified, this value will be compared to the value in aggr_interface_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggr_interface_name must be specified if op_aggr_interface_name is specified.
             :type val_c_aggr_interface_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_admin_status_ind: The operator to apply to the field cap_if_admin_status_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_admin_status_ind: Capability of changing the Admin Status of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_admin_status_ind: If op_cap_if_admin_status_ind is specified, the field named in this input will be compared to the value in cap_if_admin_status_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_admin_status_ind must be specified if op_cap_if_admin_status_ind is specified.
             :type val_f_cap_if_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_admin_status_ind: If op_cap_if_admin_status_ind is specified, this value will be compared to the value in cap_if_admin_status_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_admin_status_ind must be specified if op_cap_if_admin_status_ind is specified.
             :type val_c_cap_if_admin_status_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_admin_status_na_reason: The operator to apply to the field cap_if_admin_status_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_admin_status_na_reason: Reason of non ability of changing the Admin Status of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_admin_status_na_reason: If op_cap_if_admin_status_na_reason is specified, the field named in this input will be compared to the value in cap_if_admin_status_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_admin_status_na_reason must be specified if op_cap_if_admin_status_na_reason is specified.
             :type val_f_cap_if_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_admin_status_na_reason: If op_cap_if_admin_status_na_reason is specified, this value will be compared to the value in cap_if_admin_status_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_admin_status_na_reason must be specified if op_cap_if_admin_status_na_reason is specified.
             :type val_c_cap_if_admin_status_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_description_ind: The operator to apply to the field cap_if_description_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_description_ind: Capability of changing the description of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_description_ind: If op_cap_if_description_ind is specified, the field named in this input will be compared to the value in cap_if_description_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_description_ind must be specified if op_cap_if_description_ind is specified.
             :type val_f_cap_if_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_description_ind: If op_cap_if_description_ind is specified, this value will be compared to the value in cap_if_description_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_description_ind must be specified if op_cap_if_description_ind is specified.
             :type val_c_cap_if_description_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_description_na_reason: The operator to apply to the field cap_if_description_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_description_na_reason: Reason of non ability of changing the description of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_description_na_reason: If op_cap_if_description_na_reason is specified, the field named in this input will be compared to the value in cap_if_description_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_description_na_reason must be specified if op_cap_if_description_na_reason is specified.
             :type val_f_cap_if_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_description_na_reason: If op_cap_if_description_na_reason is specified, this value will be compared to the value in cap_if_description_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_description_na_reason must be specified if op_cap_if_description_na_reason is specified.
             :type val_c_cap_if_description_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_deprovisioning_ipv4_ind: The operator to apply to the field cap_if_net_deprovisioning_ipv4_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_deprovisioning_ipv4_ind: Capability of de-provisioning an ipv4 network from this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_deprovisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_deprovisioning_ipv4_ind: If op_cap_if_net_deprovisioning_ipv4_ind is specified, the field named in this input will be compared to the value in cap_if_net_deprovisioning_ipv4_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_deprovisioning_ipv4_ind must be specified if op_cap_if_net_deprovisioning_ipv4_ind is specified.
             :type val_f_cap_if_net_deprovisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_deprovisioning_ipv4_ind: If op_cap_if_net_deprovisioning_ipv4_ind is specified, this value will be compared to the value in cap_if_net_deprovisioning_ipv4_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_deprovisioning_ipv4_ind must be specified if op_cap_if_net_deprovisioning_ipv4_ind is specified.
             :type val_c_cap_if_net_deprovisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_deprovisioning_ipv4_na_reason: The operator to apply to the field cap_if_net_deprovisioning_ipv4_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_deprovisioning_ipv4_na_reason: Reason of non ability of de-provisioning an ipv4 network from this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_deprovisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_deprovisioning_ipv4_na_reason: If op_cap_if_net_deprovisioning_ipv4_na_reason is specified, the field named in this input will be compared to the value in cap_if_net_deprovisioning_ipv4_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_deprovisioning_ipv4_na_reason must be specified if op_cap_if_net_deprovisioning_ipv4_na_reason is specified.
             :type val_f_cap_if_net_deprovisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_deprovisioning_ipv4_na_reason: If op_cap_if_net_deprovisioning_ipv4_na_reason is specified, this value will be compared to the value in cap_if_net_deprovisioning_ipv4_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_deprovisioning_ipv4_na_reason must be specified if op_cap_if_net_deprovisioning_ipv4_na_reason is specified.
             :type val_c_cap_if_net_deprovisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_deprovisioning_ipv6_ind: The operator to apply to the field cap_if_net_deprovisioning_ipv6_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_deprovisioning_ipv6_ind: Capability of de-provisioning an ipv6 network from this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_deprovisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_deprovisioning_ipv6_ind: If op_cap_if_net_deprovisioning_ipv6_ind is specified, the field named in this input will be compared to the value in cap_if_net_deprovisioning_ipv6_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_deprovisioning_ipv6_ind must be specified if op_cap_if_net_deprovisioning_ipv6_ind is specified.
             :type val_f_cap_if_net_deprovisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_deprovisioning_ipv6_ind: If op_cap_if_net_deprovisioning_ipv6_ind is specified, this value will be compared to the value in cap_if_net_deprovisioning_ipv6_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_deprovisioning_ipv6_ind must be specified if op_cap_if_net_deprovisioning_ipv6_ind is specified.
             :type val_c_cap_if_net_deprovisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_deprovisioning_ipv6_na_reason: The operator to apply to the field cap_if_net_deprovisioning_ipv6_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_deprovisioning_ipv6_na_reason: Reason of non ability of de-provisioning an ipv6 network from this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_deprovisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_deprovisioning_ipv6_na_reason: If op_cap_if_net_deprovisioning_ipv6_na_reason is specified, the field named in this input will be compared to the value in cap_if_net_deprovisioning_ipv6_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_deprovisioning_ipv6_na_reason must be specified if op_cap_if_net_deprovisioning_ipv6_na_reason is specified.
             :type val_f_cap_if_net_deprovisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_deprovisioning_ipv6_na_reason: If op_cap_if_net_deprovisioning_ipv6_na_reason is specified, this value will be compared to the value in cap_if_net_deprovisioning_ipv6_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_deprovisioning_ipv6_na_reason must be specified if op_cap_if_net_deprovisioning_ipv6_na_reason is specified.
             :type val_c_cap_if_net_deprovisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_provisioning_ipv4_ind: The operator to apply to the field cap_if_net_provisioning_ipv4_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_provisioning_ipv4_ind: Capability to provision an ipv4 network on this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_provisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_provisioning_ipv4_ind: If op_cap_if_net_provisioning_ipv4_ind is specified, the field named in this input will be compared to the value in cap_if_net_provisioning_ipv4_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_provisioning_ipv4_ind must be specified if op_cap_if_net_provisioning_ipv4_ind is specified.
             :type val_f_cap_if_net_provisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_provisioning_ipv4_ind: If op_cap_if_net_provisioning_ipv4_ind is specified, this value will be compared to the value in cap_if_net_provisioning_ipv4_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_provisioning_ipv4_ind must be specified if op_cap_if_net_provisioning_ipv4_ind is specified.
             :type val_c_cap_if_net_provisioning_ipv4_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_provisioning_ipv4_na_reason: The operator to apply to the field cap_if_net_provisioning_ipv4_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_provisioning_ipv4_na_reason: Reason of non ability to provision an ipv4 network on this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_provisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_provisioning_ipv4_na_reason: If op_cap_if_net_provisioning_ipv4_na_reason is specified, the field named in this input will be compared to the value in cap_if_net_provisioning_ipv4_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_provisioning_ipv4_na_reason must be specified if op_cap_if_net_provisioning_ipv4_na_reason is specified.
             :type val_f_cap_if_net_provisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_provisioning_ipv4_na_reason: If op_cap_if_net_provisioning_ipv4_na_reason is specified, this value will be compared to the value in cap_if_net_provisioning_ipv4_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_provisioning_ipv4_na_reason must be specified if op_cap_if_net_provisioning_ipv4_na_reason is specified.
             :type val_c_cap_if_net_provisioning_ipv4_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_provisioning_ipv6_ind: The operator to apply to the field cap_if_net_provisioning_ipv6_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_provisioning_ipv6_ind: Capability to provision an ipv6 network on this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_provisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_provisioning_ipv6_ind: If op_cap_if_net_provisioning_ipv6_ind is specified, the field named in this input will be compared to the value in cap_if_net_provisioning_ipv6_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_provisioning_ipv6_ind must be specified if op_cap_if_net_provisioning_ipv6_ind is specified.
             :type val_f_cap_if_net_provisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_provisioning_ipv6_ind: If op_cap_if_net_provisioning_ipv6_ind is specified, this value will be compared to the value in cap_if_net_provisioning_ipv6_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_provisioning_ipv6_ind must be specified if op_cap_if_net_provisioning_ipv6_ind is specified.
             :type val_c_cap_if_net_provisioning_ipv6_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_net_provisioning_ipv6_na_reason: The operator to apply to the field cap_if_net_provisioning_ipv6_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_net_provisioning_ipv6_na_reason: Reason of non ability to provision an ipv6 network on this interface.i For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_net_provisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_net_provisioning_ipv6_na_reason: If op_cap_if_net_provisioning_ipv6_na_reason is specified, the field named in this input will be compared to the value in cap_if_net_provisioning_ipv6_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_net_provisioning_ipv6_na_reason must be specified if op_cap_if_net_provisioning_ipv6_na_reason is specified.
             :type val_f_cap_if_net_provisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_net_provisioning_ipv6_na_reason: If op_cap_if_net_provisioning_ipv6_na_reason is specified, this value will be compared to the value in cap_if_net_provisioning_ipv6_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_net_provisioning_ipv6_na_reason must be specified if op_cap_if_net_provisioning_ipv6_na_reason is specified.
             :type val_c_cap_if_net_provisioning_ipv6_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_vlan_assignment_ind: The operator to apply to the field cap_if_vlan_assignment_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_vlan_assignment_ind: Capability of assigning a regular data VLAN to this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_vlan_assignment_ind: If op_cap_if_vlan_assignment_ind is specified, the field named in this input will be compared to the value in cap_if_vlan_assignment_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_vlan_assignment_ind must be specified if op_cap_if_vlan_assignment_ind is specified.
             :type val_f_cap_if_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_vlan_assignment_ind: If op_cap_if_vlan_assignment_ind is specified, this value will be compared to the value in cap_if_vlan_assignment_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_vlan_assignment_ind must be specified if op_cap_if_vlan_assignment_ind is specified.
             :type val_c_cap_if_vlan_assignment_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_vlan_assignment_na_reason: The operator to apply to the field cap_if_vlan_assignment_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_vlan_assignment_na_reason: Reason of non ability of assigning a regular data VLAN to this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_vlan_assignment_na_reason: If op_cap_if_vlan_assignment_na_reason is specified, the field named in this input will be compared to the value in cap_if_vlan_assignment_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_vlan_assignment_na_reason must be specified if op_cap_if_vlan_assignment_na_reason is specified.
             :type val_f_cap_if_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_vlan_assignment_na_reason: If op_cap_if_vlan_assignment_na_reason is specified, this value will be compared to the value in cap_if_vlan_assignment_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_vlan_assignment_na_reason must be specified if op_cap_if_vlan_assignment_na_reason is specified.
             :type val_c_cap_if_vlan_assignment_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_voice_vlan_ind: The operator to apply to the field cap_if_voice_vlan_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_voice_vlan_ind: Capability of assigning a voice VLAN to this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_voice_vlan_ind: If op_cap_if_voice_vlan_ind is specified, the field named in this input will be compared to the value in cap_if_voice_vlan_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_voice_vlan_ind must be specified if op_cap_if_voice_vlan_ind is specified.
             :type val_f_cap_if_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_voice_vlan_ind: If op_cap_if_voice_vlan_ind is specified, this value will be compared to the value in cap_if_voice_vlan_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_voice_vlan_ind must be specified if op_cap_if_voice_vlan_ind is specified.
             :type val_c_cap_if_voice_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_if_voice_vlan_na_reason: The operator to apply to the field cap_if_voice_vlan_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_if_voice_vlan_na_reason: Reason of non ability of assigning a voice VLAN to this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_if_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_if_voice_vlan_na_reason: If op_cap_if_voice_vlan_na_reason is specified, the field named in this input will be compared to the value in cap_if_voice_vlan_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_if_voice_vlan_na_reason must be specified if op_cap_if_voice_vlan_na_reason is specified.
             :type val_f_cap_if_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_if_voice_vlan_na_reason: If op_cap_if_voice_vlan_na_reason is specified, this value will be compared to the value in cap_if_voice_vlan_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_if_voice_vlan_na_reason must be specified if op_cap_if_voice_vlan_na_reason is specified.
             :type val_c_cap_if_voice_vlan_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_itf_net_deprovisioning_ind: The operator to apply to the field cap_itf_net_deprovisioning_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_itf_net_deprovisioning_ind: Capability of de-provisioning a network from this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_itf_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_itf_net_deprovisioning_ind: If op_cap_itf_net_deprovisioning_ind is specified, the field named in this input will be compared to the value in cap_itf_net_deprovisioning_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_itf_net_deprovisioning_ind must be specified if op_cap_itf_net_deprovisioning_ind is specified.
             :type val_f_cap_itf_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_itf_net_deprovisioning_ind: If op_cap_itf_net_deprovisioning_ind is specified, this value will be compared to the value in cap_itf_net_deprovisioning_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_itf_net_deprovisioning_ind must be specified if op_cap_itf_net_deprovisioning_ind is specified.
             :type val_c_cap_itf_net_deprovisioning_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cap_itf_net_deprovisioning_na_reason: The operator to apply to the field cap_itf_net_deprovisioning_na_reason. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cap_itf_net_deprovisioning_na_reason: The reason a network from this interface was unable to be deprovisioned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cap_itf_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cap_itf_net_deprovisioning_na_reason: If op_cap_itf_net_deprovisioning_na_reason is specified, the field named in this input will be compared to the value in cap_itf_net_deprovisioning_na_reason using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cap_itf_net_deprovisioning_na_reason must be specified if op_cap_itf_net_deprovisioning_na_reason is specified.
             :type val_f_cap_itf_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cap_itf_net_deprovisioning_na_reason: If op_cap_itf_net_deprovisioning_na_reason is specified, this value will be compared to the value in cap_itf_net_deprovisioning_na_reason using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cap_itf_net_deprovisioning_na_reason must be specified if op_cap_itf_net_deprovisioning_na_reason is specified.
             :type val_c_cap_itf_net_deprovisioning_na_reason: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifAdminDuplex: The operator to apply to the field ifAdminDuplex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifAdminDuplex: Admin setting of duplex, Auto indicates the device will try to negotiate with the other end to determine. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifAdminDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifAdminDuplex: If op_ifAdminDuplex is specified, the field named in this input will be compared to the value in ifAdminDuplex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifAdminDuplex must be specified if op_ifAdminDuplex is specified.
             :type val_f_ifAdminDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifAdminDuplex: If op_ifAdminDuplex is specified, this value will be compared to the value in ifAdminDuplex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifAdminDuplex must be specified if op_ifAdminDuplex is specified.
             :type val_c_ifAdminDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifAdminStatus: The operator to apply to the field ifAdminStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifAdminStatus: The configured status (up/down) of the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifAdminStatus: If op_ifAdminStatus is specified, the field named in this input will be compared to the value in ifAdminStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifAdminStatus must be specified if op_ifAdminStatus is specified.
             :type val_f_ifAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifAdminStatus: If op_ifAdminStatus is specified, this value will be compared to the value in ifAdminStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifAdminStatus must be specified if op_ifAdminStatus is specified.
             :type val_c_ifAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifAggrMemberInd: The operator to apply to the field ifAggrMemberInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifAggrMemberInd: A flag indicating whether or not this is a member interface in a link aggregation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifAggrMemberInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifAggrMemberInd: If op_ifAggrMemberInd is specified, the field named in this input will be compared to the value in ifAggrMemberInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifAggrMemberInd must be specified if op_ifAggrMemberInd is specified.
             :type val_f_ifAggrMemberInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifAggrMemberInd: If op_ifAggrMemberInd is specified, this value will be compared to the value in ifAggrMemberInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifAggrMemberInd must be specified if op_ifAggrMemberInd is specified.
             :type val_c_ifAggrMemberInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifAlias: The operator to apply to the field ifAlias. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifAlias: Interface alias. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifAlias: If op_ifAlias is specified, the field named in this input will be compared to the value in ifAlias using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifAlias must be specified if op_ifAlias is specified.
             :type val_f_ifAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifAlias: If op_ifAlias is specified, this value will be compared to the value in ifAlias using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifAlias must be specified if op_ifAlias is specified.
             :type val_c_ifAlias: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifArtificialInd: The operator to apply to the field ifArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifArtificialInd: Not currently used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifArtificialInd: If op_ifArtificialInd is specified, the field named in this input will be compared to the value in ifArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifArtificialInd must be specified if op_ifArtificialInd is specified.
             :type val_f_ifArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifArtificialInd: If op_ifArtificialInd is specified, this value will be compared to the value in ifArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifArtificialInd must be specified if op_ifArtificialInd is specified.
             :type val_c_ifArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifChangedCols: The operator to apply to the field ifChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifChangedCols: If op_ifChangedCols is specified, the field named in this input will be compared to the value in ifChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifChangedCols must be specified if op_ifChangedCols is specified.
             :type val_f_ifChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifChangedCols: If op_ifChangedCols is specified, this value will be compared to the value in ifChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifChangedCols must be specified if op_ifChangedCols is specified.
             :type val_c_ifChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifConnector: The operator to apply to the field ifConnector. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifConnector: If "true" or "1", then this interface has a physical connector. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifConnector: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifConnector: If op_ifConnector is specified, the field named in this input will be compared to the value in ifConnector using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifConnector must be specified if op_ifConnector is specified.
             :type val_f_ifConnector: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifConnector: If op_ifConnector is specified, this value will be compared to the value in ifConnector using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifConnector must be specified if op_ifConnector is specified.
             :type val_c_ifConnector: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifDescr: The operator to apply to the field ifDescr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifDescr: The description of the interface, as set in the device's configuration file. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifDescr: If op_ifDescr is specified, the field named in this input will be compared to the value in ifDescr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifDescr must be specified if op_ifDescr is specified.
             :type val_f_ifDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifDescr: If op_ifDescr is specified, this value will be compared to the value in ifDescr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifDescr must be specified if op_ifDescr is specified.
             :type val_c_ifDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifDescrRaw: The operator to apply to the field ifDescrRaw. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifDescrRaw: The raw description of the interface before any NetMRI processing. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifDescrRaw: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifDescrRaw: If op_ifDescrRaw is specified, the field named in this input will be compared to the value in ifDescrRaw using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifDescrRaw must be specified if op_ifDescrRaw is specified.
             :type val_f_ifDescrRaw: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifDescrRaw: If op_ifDescrRaw is specified, this value will be compared to the value in ifDescrRaw using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifDescrRaw must be specified if op_ifDescrRaw is specified.
             :type val_c_ifDescrRaw: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifDuplex: The operator to apply to the field ifDuplex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifDuplex: The operational duplex of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifDuplex: If op_ifDuplex is specified, the field named in this input will be compared to the value in ifDuplex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifDuplex must be specified if op_ifDuplex is specified.
             :type val_f_ifDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifDuplex: If op_ifDuplex is specified, this value will be compared to the value in ifDuplex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifDuplex must be specified if op_ifDuplex is specified.
             :type val_c_ifDuplex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifEncapsulationTag: The operator to apply to the field ifEncapsulationTag. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifEncapsulationTag: Indicates the encapsulation Tag for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifEncapsulationTag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifEncapsulationTag: If op_ifEncapsulationTag is specified, the field named in this input will be compared to the value in ifEncapsulationTag using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifEncapsulationTag must be specified if op_ifEncapsulationTag is specified.
             :type val_f_ifEncapsulationTag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifEncapsulationTag: If op_ifEncapsulationTag is specified, this value will be compared to the value in ifEncapsulationTag using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifEncapsulationTag must be specified if op_ifEncapsulationTag is specified.
             :type val_c_ifEncapsulationTag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifEncapsulationType: The operator to apply to the field ifEncapsulationType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifEncapsulationType: Indicates the encapsulation Type for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifEncapsulationType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifEncapsulationType: If op_ifEncapsulationType is specified, the field named in this input will be compared to the value in ifEncapsulationType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifEncapsulationType must be specified if op_ifEncapsulationType is specified.
             :type val_f_ifEncapsulationType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifEncapsulationType: If op_ifEncapsulationType is specified, this value will be compared to the value in ifEncapsulationType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifEncapsulationType must be specified if op_ifEncapsulationType is specified.
             :type val_c_ifEncapsulationType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifEndTime: The operator to apply to the field ifEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifEndTime: If op_ifEndTime is specified, the field named in this input will be compared to the value in ifEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifEndTime must be specified if op_ifEndTime is specified.
             :type val_f_ifEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifEndTime: If op_ifEndTime is specified, this value will be compared to the value in ifEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifEndTime must be specified if op_ifEndTime is specified.
             :type val_c_ifEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifFirstSeenTime: The operator to apply to the field ifFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifFirstSeenTime: The date and time this interface was first seen on the network, and since which it has been continuously present. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifFirstSeenTime: If op_ifFirstSeenTime is specified, the field named in this input will be compared to the value in ifFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifFirstSeenTime must be specified if op_ifFirstSeenTime is specified.
             :type val_f_ifFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifFirstSeenTime: If op_ifFirstSeenTime is specified, this value will be compared to the value in ifFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifFirstSeenTime must be specified if op_ifFirstSeenTime is specified.
             :type val_c_ifFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index value of the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLastChange: The operator to apply to the field ifLastChange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLastChange: The date/time of the last status change for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLastChange: If op_ifLastChange is specified, the field named in this input will be compared to the value in ifLastChange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLastChange must be specified if op_ifLastChange is specified.
             :type val_f_ifLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLastChange: If op_ifLastChange is specified, this value will be compared to the value in ifLastChange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLastChange must be specified if op_ifLastChange is specified.
             :type val_c_ifLastChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLinkAggrInd: The operator to apply to the field ifLinkAggrInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLinkAggrInd: A flag indicating whether or not this is a link aggregation (port channel, etherchannel, LACP, etc.) interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLinkAggrInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLinkAggrInd: If op_ifLinkAggrInd is specified, the field named in this input will be compared to the value in ifLinkAggrInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLinkAggrInd must be specified if op_ifLinkAggrInd is specified.
             :type val_f_ifLinkAggrInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLinkAggrInd: If op_ifLinkAggrInd is specified, this value will be compared to the value in ifLinkAggrInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLinkAggrInd must be specified if op_ifLinkAggrInd is specified.
             :type val_c_ifLinkAggrInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLinkAggrIndex: The operator to apply to the field ifLinkAggrIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLinkAggrIndex: The port group or port channel number for link aggregations interface or their member interfaces. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLinkAggrIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLinkAggrIndex: If op_ifLinkAggrIndex is specified, the field named in this input will be compared to the value in ifLinkAggrIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLinkAggrIndex must be specified if op_ifLinkAggrIndex is specified.
             :type val_f_ifLinkAggrIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLinkAggrIndex: If op_ifLinkAggrIndex is specified, this value will be compared to the value in ifLinkAggrIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLinkAggrIndex must be specified if op_ifLinkAggrIndex is specified.
             :type val_c_ifLinkAggrIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLinkTrap: The operator to apply to the field ifLinkTrap. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLinkTrap: If "enabled", this device is configured to send link up/down traps. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLinkTrap: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLinkTrap: If op_ifLinkTrap is specified, the field named in this input will be compared to the value in ifLinkTrap using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLinkTrap must be specified if op_ifLinkTrap is specified.
             :type val_f_ifLinkTrap: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLinkTrap: If op_ifLinkTrap is specified, this value will be compared to the value in ifLinkTrap using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLinkTrap must be specified if op_ifLinkTrap is specified.
             :type val_c_ifLinkTrap: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLowerLayer: The operator to apply to the field ifLowerLayer. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLowerLayer: The SNMP interface index of the lower-layer interface on which this interface is constructed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLowerLayer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLowerLayer: If op_ifLowerLayer is specified, the field named in this input will be compared to the value in ifLowerLayer using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLowerLayer must be specified if op_ifLowerLayer is specified.
             :type val_f_ifLowerLayer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLowerLayer: If op_ifLowerLayer is specified, this value will be compared to the value in ifLowerLayer using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLowerLayer must be specified if op_ifLowerLayer is specified.
             :type val_c_ifLowerLayer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLowerLayerInterfaceID: The operator to apply to the field ifLowerLayerInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLowerLayerInterfaceID: The internal NetMRI identifier for the lower-layer interface on which this interface is constructed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLowerLayerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLowerLayerInterfaceID: If op_ifLowerLayerInterfaceID is specified, the field named in this input will be compared to the value in ifLowerLayerInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLowerLayerInterfaceID must be specified if op_ifLowerLayerInterfaceID is specified.
             :type val_f_ifLowerLayerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLowerLayerInterfaceID: If op_ifLowerLayerInterfaceID is specified, this value will be compared to the value in ifLowerLayerInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLowerLayerInterfaceID must be specified if op_ifLowerLayerInterfaceID is specified.
             :type val_c_ifLowerLayerInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifMAC: The operator to apply to the field ifMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifMAC: The interface Media Access Controller (MAC) address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifMAC: If op_ifMAC is specified, the field named in this input will be compared to the value in ifMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifMAC must be specified if op_ifMAC is specified.
             :type val_f_ifMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifMAC: If op_ifMAC is specified, this value will be compared to the value in ifMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifMAC must be specified if op_ifMAC is specified.
             :type val_c_ifMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifMtu: The operator to apply to the field ifMtu. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifMtu: The size of the largest packet or datagram which can be sent/received on the interface, specified in octets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifMtu: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifMtu: If op_ifMtu is specified, the field named in this input will be compared to the value in ifMtu using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifMtu must be specified if op_ifMtu is specified.
             :type val_f_ifMtu: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifMtu: If op_ifMtu is specified, this value will be compared to the value in ifMtu using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifMtu must be specified if op_ifMtu is specified.
             :type val_c_ifMtu: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifName: The operator to apply to the field ifName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifName: The name of this interface. This is typically the short name of the interface as it is identified in the console. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifName: If op_ifName is specified, the field named in this input will be compared to the value in ifName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifName must be specified if op_ifName is specified.
             :type val_f_ifName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifName: If op_ifName is specified, this value will be compared to the value in ifName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifName must be specified if op_ifName is specified.
             :type val_c_ifName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifNameSort: The operator to apply to the field ifNameSort. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifNameSort: The internal NetMRI name of this interface for sorting purpose. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifNameSort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifNameSort: If op_ifNameSort is specified, the field named in this input will be compared to the value in ifNameSort using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifNameSort must be specified if op_ifNameSort is specified.
             :type val_f_ifNameSort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifNameSort: If op_ifNameSort is specified, this value will be compared to the value in ifNameSort using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifNameSort must be specified if op_ifNameSort is specified.
             :type val_c_ifNameSort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOperStatus: The operator to apply to the field ifOperStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOperStatus: The operational status (up/down) of the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOperStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOperStatus: If op_ifOperStatus is specified, the field named in this input will be compared to the value in ifOperStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOperStatus must be specified if op_ifOperStatus is specified.
             :type val_f_ifOperStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOperStatus: If op_ifOperStatus is specified, this value will be compared to the value in ifOperStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOperStatus must be specified if op_ifOperStatus is specified.
             :type val_c_ifOperStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOperStatusChange: The operator to apply to the field ifOperStatusChange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOperStatusChange: The date/time of the last operational status change (e.g. free or used) for this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOperStatusChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOperStatusChange: If op_ifOperStatusChange is specified, the field named in this input will be compared to the value in ifOperStatusChange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOperStatusChange must be specified if op_ifOperStatusChange is specified.
             :type val_f_ifOperStatusChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOperStatusChange: If op_ifOperStatusChange is specified, this value will be compared to the value in ifOperStatusChange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOperStatusChange must be specified if op_ifOperStatusChange is specified.
             :type val_c_ifOperStatusChange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifPortControlInd: The operator to apply to the field ifPortControlInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifPortControlInd: A flag indicating whether or not this interface is available for port control actions. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifPortControlInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifPortControlInd: If op_ifPortControlInd is specified, the field named in this input will be compared to the value in ifPortControlInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifPortControlInd must be specified if op_ifPortControlInd is specified.
             :type val_f_ifPortControlInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifPortControlInd: If op_ifPortControlInd is specified, this value will be compared to the value in ifPortControlInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifPortControlInd must be specified if op_ifPortControlInd is specified.
             :type val_c_ifPortControlInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifPortFast: The operator to apply to the field ifPortFast. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifPortFast: If "enabled" then port fast is active on the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifPortFast: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifPortFast: If op_ifPortFast is specified, the field named in this input will be compared to the value in ifPortFast using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifPortFast must be specified if op_ifPortFast is specified.
             :type val_f_ifPortFast: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifPortFast: If op_ifPortFast is specified, this value will be compared to the value in ifPortFast using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifPortFast must be specified if op_ifPortFast is specified.
             :type val_c_ifPortFast: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifSpeed: The operator to apply to the field ifSpeed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifSpeed: The operational speed, in bps, of this interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifSpeed: If op_ifSpeed is specified, the field named in this input will be compared to the value in ifSpeed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifSpeed must be specified if op_ifSpeed is specified.
             :type val_f_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifSpeed: If op_ifSpeed is specified, this value will be compared to the value in ifSpeed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifSpeed must be specified if op_ifSpeed is specified.
             :type val_c_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifStartTime: The operator to apply to the field ifStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifStartTime: If op_ifStartTime is specified, the field named in this input will be compared to the value in ifStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifStartTime must be specified if op_ifStartTime is specified.
             :type val_f_ifStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifStartTime: If op_ifStartTime is specified, this value will be compared to the value in ifStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifStartTime must be specified if op_ifStartTime is specified.
             :type val_c_ifStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifSwitchPortMgmtInd: The operator to apply to the field ifSwitchPortMgmtInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifSwitchPortMgmtInd: A flag indicating whether or not this interface is available in switch port management views. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifSwitchPortMgmtInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifSwitchPortMgmtInd: If op_ifSwitchPortMgmtInd is specified, the field named in this input will be compared to the value in ifSwitchPortMgmtInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifSwitchPortMgmtInd must be specified if op_ifSwitchPortMgmtInd is specified.
             :type val_f_ifSwitchPortMgmtInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifSwitchPortMgmtInd: If op_ifSwitchPortMgmtInd is specified, this value will be compared to the value in ifSwitchPortMgmtInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifSwitchPortMgmtInd must be specified if op_ifSwitchPortMgmtInd is specified.
             :type val_c_ifSwitchPortMgmtInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifTimestamp: The operator to apply to the field ifTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifTimestamp: If op_ifTimestamp is specified, the field named in this input will be compared to the value in ifTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifTimestamp must be specified if op_ifTimestamp is specified.
             :type val_f_ifTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifTimestamp: If op_ifTimestamp is specified, this value will be compared to the value in ifTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifTimestamp must be specified if op_ifTimestamp is specified.
             :type val_c_ifTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifTrunkStatus: The operator to apply to the field ifTrunkStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifTrunkStatus: If "on", then this interface is a VLAN trunk port. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifTrunkStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifTrunkStatus: If op_ifTrunkStatus is specified, the field named in this input will be compared to the value in ifTrunkStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifTrunkStatus must be specified if op_ifTrunkStatus is specified.
             :type val_f_ifTrunkStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifTrunkStatus: If op_ifTrunkStatus is specified, this value will be compared to the value in ifTrunkStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifTrunkStatus must be specified if op_ifTrunkStatus is specified.
             :type val_c_ifTrunkStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifTunnelInd: The operator to apply to the field ifTunnelInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifTunnelInd: A flag indicating whether or not this is a tunnel interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifTunnelInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifTunnelInd: If op_ifTunnelInd is specified, the field named in this input will be compared to the value in ifTunnelInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifTunnelInd must be specified if op_ifTunnelInd is specified.
             :type val_f_ifTunnelInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifTunnelInd: If op_ifTunnelInd is specified, this value will be compared to the value in ifTunnelInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifTunnelInd must be specified if op_ifTunnelInd is specified.
             :type val_c_ifTunnelInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifType: The operator to apply to the field ifType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifType: The interface type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifType: If op_ifType is specified, the field named in this input will be compared to the value in ifType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifType must be specified if op_ifType is specified.
             :type val_f_ifType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifType: If op_ifType is specified, this value will be compared to the value in ifType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifType must be specified if op_ifType is specified.
             :type val_c_ifType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifVirtualInd: The operator to apply to the field ifVirtualInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifVirtualInd: A flag indicating whether or not this is a virtual interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifVirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifVirtualInd: If op_ifVirtualInd is specified, the field named in this input will be compared to the value in ifVirtualInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifVirtualInd must be specified if op_ifVirtualInd is specified.
             :type val_f_ifVirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifVirtualInd: If op_ifVirtualInd is specified, this value will be compared to the value in ifVirtualInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifVirtualInd must be specified if op_ifVirtualInd is specified.
             :type val_c_ifVirtualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_network_id: The operator to apply to the field network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. network_id: The Network View ID assigned to the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_network_id: If op_network_id is specified, the field named in this input will be compared to the value in network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_network_id must be specified if op_network_id is specified.
             :type val_f_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_network_id: If op_network_id is specified, this value will be compared to the value in network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_network_id must be specified if op_network_id is specified.
             :type val_c_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vpc_peer_device_id: The operator to apply to the field vpc_peer_device_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vpc_peer_device_id: DeviceID of VPC peer device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vpc_peer_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vpc_peer_device_id: If op_vpc_peer_device_id is specified, the field named in this input will be compared to the value in vpc_peer_device_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vpc_peer_device_id must be specified if op_vpc_peer_device_id is specified.
             :type val_f_vpc_peer_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vpc_peer_device_id: If op_vpc_peer_device_id is specified, this value will be compared to the value in vpc_peer_device_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vpc_peer_device_id must be specified if op_vpc_peer_device_id is specified.
             :type val_c_vpc_peer_device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vpc_peer_ifname: The operator to apply to the field vpc_peer_ifname. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vpc_peer_ifname: The name of peer interface of VPC pair. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vpc_peer_ifname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vpc_peer_ifname: If op_vpc_peer_ifname is specified, the field named in this input will be compared to the value in vpc_peer_ifname using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vpc_peer_ifname must be specified if op_vpc_peer_ifname is specified.
             :type val_f_vpc_peer_ifname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vpc_peer_ifname: If op_vpc_peer_ifname is specified, this value will be compared to the value in vpc_peer_ifname using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vpc_peer_ifname must be specified if op_vpc_peer_ifname is specified.
             :type val_c_vpc_peer_ifname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vrf_description: The operator to apply to the field vrf_description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vrf_description: The VRF description of the vrf assigned to the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vrf_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vrf_description: If op_vrf_description is specified, the field named in this input will be compared to the value in vrf_description using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vrf_description must be specified if op_vrf_description is specified.
             :type val_f_vrf_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vrf_description: If op_vrf_description is specified, this value will be compared to the value in vrf_description using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vrf_description must be specified if op_vrf_description is specified.
             :type val_c_vrf_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vrf_name: The operator to apply to the field vrf_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vrf_name: The VRF name assigned to the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vrf_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vrf_name: If op_vrf_name is specified, the field named in this input will be compared to the value in vrf_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vrf_name must be specified if op_vrf_name is specified.
             :type val_f_vrf_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vrf_name: If op_vrf_name is specified, this value will be compared to the value in vrf_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vrf_name must be specified if op_vrf_name is specified.
             :type val_c_vrf_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vrf_rd: The operator to apply to the field vrf_rd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vrf_rd: The VRF route distinguisher of the vrf  assigned to the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vrf_rd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vrf_rd: If op_vrf_rd is specified, the field named in this input will be compared to the value in vrf_rd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vrf_rd must be specified if op_vrf_rd is specified.
             :type val_f_vrf_rd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vrf_rd: If op_vrf_rd is specified, this value will be compared to the value in vrf_rd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vrf_rd must be specified if op_vrf_rd is specified.
             :type val_c_vrf_rd: String

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

             :param timestamp: The data returned will represent the interfaces as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of interface methods. The listed methods will be called on each interface returned and included in the output. Available methods are: cap_if_description_ind, cap_if_admin_status_ind, cap_if_vlan_assignment_ind, cap_if_voice_vlan_ind, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, cap_itf_net_deprovisioning_ind, cap_if_description_na_reason, cap_if_admin_status_na_reason, cap_if_vlan_assignment_na_reason, cap_if_voice_vlan_na_reason, cap_if_net_provisioning_ipv4_na_reason, cap_if_net_provisioning_ipv6_na_reason, cap_if_net_deprovisioning_ipv4_na_reason, cap_if_net_deprovisioning_ipv6_na_reason, cap_itf_net_deprovisioning_na_reason, aggr_interface, infradevice, ifphysaddress, control_capabilities, vrf_name, vrf_description, vrf_rd, network_id, aggr_interface_name, vpc_peer_ifname, vpc_peer_device_id, meta, network_name, data_source, device, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: aggr_interface, meta, data_source, device.
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
            |  ``default:`` InterfaceID

             :param sort: The data field(s) to use for sorting the output. Default is InterfaceID. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount.
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

             :param select: The list of attributes to return for each Interface. Valid values are DataSourceID, DeviceID, InterfaceID, ifIndex, ifTimestamp, ifFirstSeenTime, ifStartTime, ifEndTime, ifChangedCols, ifName, ifNameSort, ifDescr, ifType, ifMtu, ifMAC, ifLinkTrap, ifConnector, ifDuplex, ifSpeed, ifLowerLayer, ifAdminStatus, ifOperStatus, ifTrunkStatus, ifPortFast, ifTunnelInd, ifVirtualInd, ifLinkAggrInd, ifAggrMemberInd, ifArtificialInd, ifLinkAggrIndex, AggrInterfaceID, ifLastChange, ifAlias, ifDescrRaw, ifAdminDuplex, Slot, Port, PoEPower, PoEStatus, SwitchPortNumber, VirtualNetworkMemberID, ifEncapsulationType, ifEncapsulationTag, ifPortControlInd, ifSwitchPortMgmtInd, ifOperStatusChange, ifLowerLayerInterfaceID, DownstreamSwitchCount. If empty or omitted, all attributes will be returned.
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

             :return interfaces: An array of the Interface objects that match the specified input criteria.
             :rtype interfaces: Array of Interface

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated interface.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated interface.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated interface.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return interface: The updated interface.
             :rtype interface: Interface

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def update_custom_field(self, **kwargs):
        """Updates an existing interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated interface.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated interface.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated interface.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return interface: The updated interface.
             :rtype interface: Interface

            """

        return self.api_request(self._get_method_fullname("update_custom_field"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def aggr_interface(self, **kwargs):
        """The 'owning' link aggregation interface for link aggregate members (refers back to self for link aggregates).

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The 'owning' link aggregation interface for link aggregate members (refers back to self for link aggregates).
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("aggr_interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device containing this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing this interface.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def vlan(self, **kwargs):
        """The first virtual LAN attached to that interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The first virtual LAN attached to that interface
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def network_name(self, **kwargs):
        """A Network View assigned to the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : A Network View assigned to the device.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("network_name"), kwargs)

    def network_id(self, **kwargs):
        """The Network View ID assigned to the interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Network View ID assigned to the interface.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("network_id"), kwargs)

    def vrf_name(self, **kwargs):
        """The VRF name assigned to the interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VRF name assigned to the interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("vrf_name"), kwargs)

    def vrf_description(self, **kwargs):
        """The VRF description of the vrf assigned to the interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VRF description of the vrf assigned to the interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("vrf_description"), kwargs)

    def vrf_rd(self, **kwargs):
        """The VRF route distinguisher of the vrf  assigned to the interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VRF route distinguisher of the vrf  assigned to the interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("vrf_rd"), kwargs)

    def cap_if_description_ind(self, **kwargs):
        """Capability of changing the description of this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of changing the description of this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_description_ind"), kwargs)

    def cap_if_admin_status_ind(self, **kwargs):
        """Capability of changing the Admin Status of this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of changing the Admin Status of this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_admin_status_ind"), kwargs)

    def cap_if_vlan_assignment_ind(self, **kwargs):
        """Capability of assigning a regular data VLAN to this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of assigning a regular data VLAN to this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_vlan_assignment_ind"), kwargs)

    def cap_if_voice_vlan_ind(self, **kwargs):
        """Capability of assigning a voice VLAN to this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of assigning a voice VLAN to this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_voice_vlan_ind"), kwargs)

    def control_capabilities(self, **kwargs):
        """Configuration capabilities for this interface, related to Port Control.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Configuration capabilities for this interface, related to Port Control.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("control_capabilities"), kwargs)

    def cap_itf_net_deprovisioning_ind(self, **kwargs):
        """Capability of de-provisioning a network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of de-provisioning a network from this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_itf_net_deprovisioning_ind"), kwargs)

    def cap_if_description_na_reason(self, **kwargs):
        """Reason of non ability of changing the description of this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of changing the description of this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_description_na_reason"), kwargs)

    def cap_if_admin_status_na_reason(self, **kwargs):
        """Reason of non ability of changing the Admin Status of this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of changing the Admin Status of this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_admin_status_na_reason"), kwargs)

    def cap_if_vlan_assignment_na_reason(self, **kwargs):
        """Reason of non ability of assigning a regular data VLAN to this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of assigning a regular data VLAN to this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_vlan_assignment_na_reason"), kwargs)

    def cap_if_voice_vlan_na_reason(self, **kwargs):
        """Reason of non ability of assigning a voice VLAN to this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of assigning a voice VLAN to this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_voice_vlan_na_reason"), kwargs)

    def cap_if_net_provisioning_ipv4_ind(self, **kwargs):
        """Capability to provision an ipv4 network on this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability to provision an ipv4 network on this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv4_ind"), kwargs)

    def cap_if_net_provisioning_ipv4_na_reason(self, **kwargs):
        """Reason of non ability to provision an ipv4 network on this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability to provision an ipv4 network on this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv4_na_reason"), kwargs)

    def cap_if_net_provisioning_ipv6_ind(self, **kwargs):
        """Capability to provision an ipv6 network on this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability to provision an ipv6 network on this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv6_ind"), kwargs)

    def cap_if_net_provisioning_ipv6_na_reason(self, **kwargs):
        """Reason of non ability to provision an ipv6 network on this interface.i

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability to provision an ipv6 network on this interface.i
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv6_na_reason"), kwargs)

    def cap_if_net_deprovisioning_ipv4_ind(self, **kwargs):
        """Capability of de-provisioning an ipv4 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of de-provisioning an ipv4 network from this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv4_ind"), kwargs)

    def cap_if_net_deprovisioning_ipv4_na_reason(self, **kwargs):
        """Reason of non ability of de-provisioning an ipv4 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of de-provisioning an ipv4 network from this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv4_na_reason"), kwargs)

    def cap_if_net_deprovisioning_ipv6_ind(self, **kwargs):
        """Capability of de-provisioning an ipv6 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of de-provisioning an ipv6 network from this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv6_ind"), kwargs)

    def cap_if_net_deprovisioning_ipv6_na_reason(self, **kwargs):
        """Reason of non ability of de-provisioning an ipv6 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Reason of non ability of de-provisioning an ipv6 network from this interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv6_na_reason"), kwargs)

    def cap_itf_net_deprovisioning_na_reason(self, **kwargs):
        """The reason a network from this interface was unable to be deprovisioned.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The reason a network from this interface was unable to be deprovisioned.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("cap_itf_net_deprovisioning_na_reason"), kwargs)

    def aggr_interface_name(self, **kwargs):
        """The name of aggregated interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The name of aggregated interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("aggr_interface_name"), kwargs)

    def vpc_peer_ifname(self, **kwargs):
        """The name of peer interface of VPC pair.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The name of peer interface of VPC pair.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("vpc_peer_ifname"), kwargs)

    def vpc_peer_device_id(self, **kwargs):
        """DeviceID of VPC peer device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : DeviceID of VPC peer device.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("vpc_peer_device_id"), kwargs)

    def device(self, **kwargs):
        """The device containing this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for this interface.
             :type InterfaceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing this interface.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
