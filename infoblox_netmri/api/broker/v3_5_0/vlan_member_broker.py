from ..broker import Broker


class VlanMemberBroker(Broker):
    controller = "vlan_members"

    def show(self, **kwargs):
        """Shows the details for the specified vlan member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan member methods. The listed methods will be called on each vlan member returned and included in the output. Available methods are: network_id, data_source, device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return vlan_member: The vlan member identified by the specified VlanMemberID.
             :rtype vlan_member: VlanMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available vlan members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this VLAN membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this VLAN membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN associated with this VLAN membership.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN associated with this VLAN membership.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Array of Integer

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

             :param timestamp: The data returned will represent the vlan members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan member methods. The listed methods will be called on each vlan member returned and included in the output. Available methods are: network_id, data_source, device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, vlan.
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
            |  ``default:`` VlanMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VlanMemberID. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay.
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

             :param select: The list of attributes to return for each VlanMember. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay. If empty or omitted, all attributes will be returned.
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

             :return vlan_members: An array of the VlanMember objects that match the specified input criteria.
             :rtype vlan_members: Array of VlanMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available vlan members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BaseBridgeAddress: The spanning tree protocol base bridge address of this bridge. Empty for non-bridge members.
             :type BaseBridgeAddress: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BaseBridgeAddress: The spanning tree protocol base bridge address of this bridge. Empty for non-bridge members.
             :type BaseBridgeAddress: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BaseNumPorts: The number of ports on this bridge. Empty for non-bridge members.
             :type BaseNumPorts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BaseNumPorts: The number of ports on this bridge. Empty for non-bridge members.
             :type BaseNumPorts: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param BridgeMemberInd: A flag indicating that this VLAN membership record represents a bridge device's configuration entry for the VLAN; that is, that this membership record is for a bridge participating in the VLAN, as opposed to a device attached to an access port.
             :type BridgeMemberInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BridgeMemberInd: A flag indicating that this VLAN membership record represents a bridge device's configuration entry for the VLAN; that is, that this membership record is for a bridge participating in the VLAN, as opposed to a device attached to an access port.
             :type BridgeMemberInd: Array of Boolean

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

             :param DeviceID: The internal NetMRI identifier for the device associated with this VLAN membership.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device associated with this VLAN membership.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the switched virtual interface for this VLAN on this device.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the switched virtual interface for this VLAN on this device.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The spanning tree protocol root bridge address; this is the designated root with the STP priority portion removed. Empty for non-bridge members.
             :type RootBridgeAddress: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RootBridgeAddress: The spanning tree protocol root bridge address; this is the designated root with the STP priority portion removed. Empty for non-bridge members.
             :type RootBridgeAddress: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeForwardDelay: The value that all bridges use for ForwardDelay when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeForwardDelay: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeForwardDelay: The value that all bridges use for ForwardDelay when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeForwardDelay: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeHelloTime: The value that all bridges use for HelloTime when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeHelloTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeHelloTime: The value that all bridges use for HelloTime when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeHelloTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeMaxAge: The value that all bridges use for MaxAge when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeMaxAge: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpBridgeMaxAge: The value that all bridges use for MaxAge when this bridge is acting as the root. Empty for non-bridge members.
             :type StpBridgeMaxAge: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpDesignatedRoot: The bridge identifier for this bridge. Empty for non-bridge members.
             :type StpDesignatedRoot: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpDesignatedRoot: The bridge identifier for this bridge. Empty for non-bridge members.
             :type StpDesignatedRoot: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpForwardDelay: This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state. The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state. This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. This is the value currently in use on this bridge. Empty for non-bridge members.
             :type StpForwardDelay: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpForwardDelay: This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state. The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state. This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. This is the value currently in use on this bridge. Empty for non-bridge members.
             :type StpForwardDelay: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpHelloTime: The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second. This is the actual value that this bridge is currently using.
             :type StpHelloTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpHelloTime: The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second. This is the actual value that this bridge is currently using.
             :type StpHelloTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpHoldTime: This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second.
             :type StpHoldTime: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpHoldTime: This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second.
             :type StpHoldTime: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpMaxAge: The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second. This is the actual value that this bridge is currently using. Empty for non-bridge members.
             :type StpMaxAge: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpMaxAge: The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second. This is the actual value that this bridge is currently using. Empty for non-bridge members.
             :type StpMaxAge: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpPriority: The spanning tree protocol priority for this bridge in this VLAN. Empty for non-bridge members.
             :type StpPriority: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpPriority: The spanning tree protocol priority for this bridge in this VLAN. Empty for non-bridge members.
             :type StpPriority: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpProtocolSpecification: The protocol of spanning tree running for this VLAN. Empty for non-bridge members.
             :type StpProtocolSpecification: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpProtocolSpecification: The protocol of spanning tree running for this VLAN. Empty for non-bridge members.
             :type StpProtocolSpecification: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpRootCost: The cost of the path to the root bridge as seen from this bridge. Empty for non-bridge members.
             :type StpRootCost: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpRootCost: The cost of the path to the root bridge as seen from this bridge. Empty for non-bridge members.
             :type StpRootCost: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpRootPort: The port number (i.e., the SwitchPortNumber attribute value of the interface) of the port that offers the lowest cost path from this bridge to the root bridge.
             :type StpRootPort: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpRootPort: The port number (i.e., the SwitchPortNumber attribute value of the interface) of the port that offers the lowest cost path from this bridge to the root bridge.
             :type StpRootPort: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StpTopChanges: The total number of topology changes detected by this bridge since the last reset. Empty for non-bridge members.
             :type StpTopChanges: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StpTopChanges: The total number of topology changes detected by this bridge since the last reset. Empty for non-bridge members.
             :type StpTopChanges: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VTPDomain: Management domain name if VLAN is VTP managed.
             :type VTPDomain: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VTPDomain: Management domain name if VLAN is VTP managed.
             :type VTPDomain: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN associated with this VLAN membership.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN associated with this VLAN membership.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type VlanMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type VlanMemberChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type VlanMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type VlanMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberStartTime: The starting effective time of this revision of the record.
             :type VlanMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberStartTime: The starting effective time of this revision of the record.
             :type VlanMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberTimestamp: The date and time this record was collected or calculated.
             :type VlanMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanMemberTimestamp: The date and time this record was collected or calculated.
             :type VlanMemberTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanName: The name of this VLAN as configured on this device. Empty for non-bridge members.
             :type VlanName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanName: The name of this VLAN as configured on this device. Empty for non-bridge members.
             :type VlanName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanState: The state of this VLAN on this device. Empty for non-bridge members.

The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.

The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports.
             :type VlanState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanState: The state of this VLAN on this device. Empty for non-bridge members.

The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.

The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports.
             :type VlanState: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanType: The type of this VLAN (1:ethernet, 2:fddi, 3:tokenRing, 4:fddiNet, 5:trNet, 6:deprecated) as configured on this device. Empty for non-bridge members.
             :type VlanType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanType: The type of this VLAN (1:ethernet, 2:fddi, 3:tokenRing, 4:fddiNet, 5:trNet, 6:deprecated) as configured on this device. Empty for non-bridge members.
             :type VlanType: Array of String

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

             :param timestamp: The data returned will represent the vlan members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan member methods. The listed methods will be called on each vlan member returned and included in the output. Available methods are: network_id, data_source, device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, vlan.
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
            |  ``default:`` VlanMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VlanMemberID. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay.
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

             :param select: The list of attributes to return for each VlanMember. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against vlan members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: BaseBridgeAddress, BaseNumPorts, BridgeMemberInd, DataSourceID, DeviceID, InterfaceID, RootBridgeAddress, StpBridgeForwardDelay, StpBridgeHelloTime, StpBridgeMaxAge, StpDesignatedRoot, StpForwardDelay, StpHelloTime, StpHoldTime, StpMaxAge, StpPriority, StpProtocolSpecification, StpRootCost, StpRootPort, StpTopChanges, VTPDomain, VlanID, VlanMemberChangedCols, VlanMemberEndTime, VlanMemberID, VlanMemberStartTime, VlanMemberTimestamp, VlanName, VlanState, VlanType.
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

             :return vlan_members: An array of the VlanMember objects that match the specified input criteria.
             :rtype vlan_members: Array of VlanMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available vlan members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: BaseBridgeAddress, BaseNumPorts, BridgeMemberInd, DataSourceID, DeviceID, InterfaceID, RootBridgeAddress, StpBridgeForwardDelay, StpBridgeHelloTime, StpBridgeMaxAge, StpDesignatedRoot, StpForwardDelay, StpHelloTime, StpHoldTime, StpMaxAge, StpPriority, StpProtocolSpecification, StpRootCost, StpRootPort, StpTopChanges, VTPDomain, VlanID, VlanMemberChangedCols, VlanMemberEndTime, VlanMemberID, VlanMemberStartTime, VlanMemberTimestamp, VlanName, VlanState, VlanType.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BaseBridgeAddress: The operator to apply to the field BaseBridgeAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BaseBridgeAddress: The spanning tree protocol base bridge address of this bridge. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BaseBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BaseBridgeAddress: If op_BaseBridgeAddress is specified, the field named in this input will be compared to the value in BaseBridgeAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BaseBridgeAddress must be specified if op_BaseBridgeAddress is specified.
             :type val_f_BaseBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BaseBridgeAddress: If op_BaseBridgeAddress is specified, this value will be compared to the value in BaseBridgeAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BaseBridgeAddress must be specified if op_BaseBridgeAddress is specified.
             :type val_c_BaseBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BaseNumPorts: The operator to apply to the field BaseNumPorts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BaseNumPorts: The number of ports on this bridge. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BaseNumPorts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BaseNumPorts: If op_BaseNumPorts is specified, the field named in this input will be compared to the value in BaseNumPorts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BaseNumPorts must be specified if op_BaseNumPorts is specified.
             :type val_f_BaseNumPorts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BaseNumPorts: If op_BaseNumPorts is specified, this value will be compared to the value in BaseNumPorts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BaseNumPorts must be specified if op_BaseNumPorts is specified.
             :type val_c_BaseNumPorts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_BridgeMemberInd: The operator to apply to the field BridgeMemberInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. BridgeMemberInd: A flag indicating that this VLAN membership record represents a bridge device's configuration entry for the VLAN; that is, that this membership record is for a bridge participating in the VLAN, as opposed to a device attached to an access port. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_BridgeMemberInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_BridgeMemberInd: If op_BridgeMemberInd is specified, the field named in this input will be compared to the value in BridgeMemberInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_BridgeMemberInd must be specified if op_BridgeMemberInd is specified.
             :type val_f_BridgeMemberInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_BridgeMemberInd: If op_BridgeMemberInd is specified, this value will be compared to the value in BridgeMemberInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_BridgeMemberInd must be specified if op_BridgeMemberInd is specified.
             :type val_c_BridgeMemberInd: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device associated with this VLAN membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the switched virtual interface for this VLAN on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RootBridgeAddress: The operator to apply to the field RootBridgeAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RootBridgeAddress: The spanning tree protocol root bridge address; this is the designated root with the STP priority portion removed. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RootBridgeAddress: If op_RootBridgeAddress is specified, the field named in this input will be compared to the value in RootBridgeAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RootBridgeAddress must be specified if op_RootBridgeAddress is specified.
             :type val_f_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RootBridgeAddress: If op_RootBridgeAddress is specified, this value will be compared to the value in RootBridgeAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RootBridgeAddress must be specified if op_RootBridgeAddress is specified.
             :type val_c_RootBridgeAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpBridgeForwardDelay: The operator to apply to the field StpBridgeForwardDelay. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpBridgeForwardDelay: The value that all bridges use for ForwardDelay when this bridge is acting as the root. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpBridgeForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpBridgeForwardDelay: If op_StpBridgeForwardDelay is specified, the field named in this input will be compared to the value in StpBridgeForwardDelay using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpBridgeForwardDelay must be specified if op_StpBridgeForwardDelay is specified.
             :type val_f_StpBridgeForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpBridgeForwardDelay: If op_StpBridgeForwardDelay is specified, this value will be compared to the value in StpBridgeForwardDelay using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpBridgeForwardDelay must be specified if op_StpBridgeForwardDelay is specified.
             :type val_c_StpBridgeForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpBridgeHelloTime: The operator to apply to the field StpBridgeHelloTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpBridgeHelloTime: The value that all bridges use for HelloTime when this bridge is acting as the root. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpBridgeHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpBridgeHelloTime: If op_StpBridgeHelloTime is specified, the field named in this input will be compared to the value in StpBridgeHelloTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpBridgeHelloTime must be specified if op_StpBridgeHelloTime is specified.
             :type val_f_StpBridgeHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpBridgeHelloTime: If op_StpBridgeHelloTime is specified, this value will be compared to the value in StpBridgeHelloTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpBridgeHelloTime must be specified if op_StpBridgeHelloTime is specified.
             :type val_c_StpBridgeHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpBridgeMaxAge: The operator to apply to the field StpBridgeMaxAge. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpBridgeMaxAge: The value that all bridges use for MaxAge when this bridge is acting as the root. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpBridgeMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpBridgeMaxAge: If op_StpBridgeMaxAge is specified, the field named in this input will be compared to the value in StpBridgeMaxAge using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpBridgeMaxAge must be specified if op_StpBridgeMaxAge is specified.
             :type val_f_StpBridgeMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpBridgeMaxAge: If op_StpBridgeMaxAge is specified, this value will be compared to the value in StpBridgeMaxAge using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpBridgeMaxAge must be specified if op_StpBridgeMaxAge is specified.
             :type val_c_StpBridgeMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpDesignatedRoot: The operator to apply to the field StpDesignatedRoot. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpDesignatedRoot: The bridge identifier for this bridge. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpDesignatedRoot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpDesignatedRoot: If op_StpDesignatedRoot is specified, the field named in this input will be compared to the value in StpDesignatedRoot using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpDesignatedRoot must be specified if op_StpDesignatedRoot is specified.
             :type val_f_StpDesignatedRoot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpDesignatedRoot: If op_StpDesignatedRoot is specified, this value will be compared to the value in StpDesignatedRoot using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpDesignatedRoot must be specified if op_StpDesignatedRoot is specified.
             :type val_c_StpDesignatedRoot: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpForwardDelay: The operator to apply to the field StpForwardDelay. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpForwardDelay: This time value, measured in units of hundredths of a second, controls how fast a port changes its spanning state when moving towards the Forwarding state. The value determines how long the port stays in each of the Listening and Learning states, which precede the Forwarding state. This value is also used when a topology change has been detected and is underway, to age all dynamic entries in the Forwarding Database. This is the value currently in use on this bridge. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpForwardDelay: If op_StpForwardDelay is specified, the field named in this input will be compared to the value in StpForwardDelay using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpForwardDelay must be specified if op_StpForwardDelay is specified.
             :type val_f_StpForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpForwardDelay: If op_StpForwardDelay is specified, this value will be compared to the value in StpForwardDelay using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpForwardDelay must be specified if op_StpForwardDelay is specified.
             :type val_c_StpForwardDelay: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpHelloTime: The operator to apply to the field StpHelloTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpHelloTime: The amount of time between the transmission of Configuration bridge PDUs by this node on any port when it is the root of the spanning tree, or trying to become so, in units of hundredths of a second. This is the actual value that this bridge is currently using. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpHelloTime: If op_StpHelloTime is specified, the field named in this input will be compared to the value in StpHelloTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpHelloTime must be specified if op_StpHelloTime is specified.
             :type val_f_StpHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpHelloTime: If op_StpHelloTime is specified, this value will be compared to the value in StpHelloTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpHelloTime must be specified if op_StpHelloTime is specified.
             :type val_c_StpHelloTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpHoldTime: The operator to apply to the field StpHoldTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpHoldTime: This time value determines the interval length during which no more than two Configuration bridge PDUs shall be transmitted by this node, in units of hundredths of a second. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpHoldTime: If op_StpHoldTime is specified, the field named in this input will be compared to the value in StpHoldTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpHoldTime must be specified if op_StpHoldTime is specified.
             :type val_f_StpHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpHoldTime: If op_StpHoldTime is specified, this value will be compared to the value in StpHoldTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpHoldTime must be specified if op_StpHoldTime is specified.
             :type val_c_StpHoldTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpMaxAge: The operator to apply to the field StpMaxAge. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpMaxAge: The maximum age of Spanning Tree Protocol information learned from the network on any port before it is discarded, in units of hundredths of a second. This is the actual value that this bridge is currently using. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpMaxAge: If op_StpMaxAge is specified, the field named in this input will be compared to the value in StpMaxAge using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpMaxAge must be specified if op_StpMaxAge is specified.
             :type val_f_StpMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpMaxAge: If op_StpMaxAge is specified, this value will be compared to the value in StpMaxAge using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpMaxAge must be specified if op_StpMaxAge is specified.
             :type val_c_StpMaxAge: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpPriority: The operator to apply to the field StpPriority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpPriority: The spanning tree protocol priority for this bridge in this VLAN. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpPriority: If op_StpPriority is specified, the field named in this input will be compared to the value in StpPriority using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpPriority must be specified if op_StpPriority is specified.
             :type val_f_StpPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpPriority: If op_StpPriority is specified, this value will be compared to the value in StpPriority using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpPriority must be specified if op_StpPriority is specified.
             :type val_c_StpPriority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpProtocolSpecification: The operator to apply to the field StpProtocolSpecification. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpProtocolSpecification: The protocol of spanning tree running for this VLAN. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpProtocolSpecification: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpProtocolSpecification: If op_StpProtocolSpecification is specified, the field named in this input will be compared to the value in StpProtocolSpecification using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpProtocolSpecification must be specified if op_StpProtocolSpecification is specified.
             :type val_f_StpProtocolSpecification: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpProtocolSpecification: If op_StpProtocolSpecification is specified, this value will be compared to the value in StpProtocolSpecification using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpProtocolSpecification must be specified if op_StpProtocolSpecification is specified.
             :type val_c_StpProtocolSpecification: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpRootCost: The operator to apply to the field StpRootCost. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpRootCost: The cost of the path to the root bridge as seen from this bridge. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpRootCost: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpRootCost: If op_StpRootCost is specified, the field named in this input will be compared to the value in StpRootCost using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpRootCost must be specified if op_StpRootCost is specified.
             :type val_f_StpRootCost: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpRootCost: If op_StpRootCost is specified, this value will be compared to the value in StpRootCost using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpRootCost must be specified if op_StpRootCost is specified.
             :type val_c_StpRootCost: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpRootPort: The operator to apply to the field StpRootPort. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpRootPort: The port number (i.e., the SwitchPortNumber attribute value of the interface) of the port that offers the lowest cost path from this bridge to the root bridge. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpRootPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpRootPort: If op_StpRootPort is specified, the field named in this input will be compared to the value in StpRootPort using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpRootPort must be specified if op_StpRootPort is specified.
             :type val_f_StpRootPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpRootPort: If op_StpRootPort is specified, this value will be compared to the value in StpRootPort using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpRootPort must be specified if op_StpRootPort is specified.
             :type val_c_StpRootPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StpTopChanges: The operator to apply to the field StpTopChanges. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StpTopChanges: The total number of topology changes detected by this bridge since the last reset. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StpTopChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StpTopChanges: If op_StpTopChanges is specified, the field named in this input will be compared to the value in StpTopChanges using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StpTopChanges must be specified if op_StpTopChanges is specified.
             :type val_f_StpTopChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StpTopChanges: If op_StpTopChanges is specified, this value will be compared to the value in StpTopChanges using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StpTopChanges must be specified if op_StpTopChanges is specified.
             :type val_c_StpTopChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VTPDomain: The operator to apply to the field VTPDomain. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VTPDomain: Management domain name if VLAN is VTP managed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VTPDomain: If op_VTPDomain is specified, the field named in this input will be compared to the value in VTPDomain using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VTPDomain must be specified if op_VTPDomain is specified.
             :type val_f_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VTPDomain: If op_VTPDomain is specified, this value will be compared to the value in VTPDomain using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VTPDomain must be specified if op_VTPDomain is specified.
             :type val_c_VTPDomain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier of the VLAN associated with this VLAN membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanID: If op_VlanID is specified, the field named in this input will be compared to the value in VlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanID must be specified if op_VlanID is specified.
             :type val_f_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanID: If op_VlanID is specified, this value will be compared to the value in VlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanID must be specified if op_VlanID is specified.
             :type val_c_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberChangedCols: The operator to apply to the field VlanMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberChangedCols: If op_VlanMemberChangedCols is specified, the field named in this input will be compared to the value in VlanMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberChangedCols must be specified if op_VlanMemberChangedCols is specified.
             :type val_f_VlanMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberChangedCols: If op_VlanMemberChangedCols is specified, this value will be compared to the value in VlanMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberChangedCols must be specified if op_VlanMemberChangedCols is specified.
             :type val_c_VlanMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberEndTime: The operator to apply to the field VlanMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberEndTime: If op_VlanMemberEndTime is specified, the field named in this input will be compared to the value in VlanMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberEndTime must be specified if op_VlanMemberEndTime is specified.
             :type val_f_VlanMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberEndTime: If op_VlanMemberEndTime is specified, this value will be compared to the value in VlanMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberEndTime must be specified if op_VlanMemberEndTime is specified.
             :type val_c_VlanMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberID: The operator to apply to the field VlanMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberID: The internal NetMRI identifier for this VLAN membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberID: If op_VlanMemberID is specified, the field named in this input will be compared to the value in VlanMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberID must be specified if op_VlanMemberID is specified.
             :type val_f_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberID: If op_VlanMemberID is specified, this value will be compared to the value in VlanMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberID must be specified if op_VlanMemberID is specified.
             :type val_c_VlanMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberStartTime: The operator to apply to the field VlanMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberStartTime: If op_VlanMemberStartTime is specified, the field named in this input will be compared to the value in VlanMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberStartTime must be specified if op_VlanMemberStartTime is specified.
             :type val_f_VlanMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberStartTime: If op_VlanMemberStartTime is specified, this value will be compared to the value in VlanMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberStartTime must be specified if op_VlanMemberStartTime is specified.
             :type val_c_VlanMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanMemberTimestamp: The operator to apply to the field VlanMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanMemberTimestamp: If op_VlanMemberTimestamp is specified, the field named in this input will be compared to the value in VlanMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanMemberTimestamp must be specified if op_VlanMemberTimestamp is specified.
             :type val_f_VlanMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanMemberTimestamp: If op_VlanMemberTimestamp is specified, this value will be compared to the value in VlanMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanMemberTimestamp must be specified if op_VlanMemberTimestamp is specified.
             :type val_c_VlanMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanName: The operator to apply to the field VlanName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanName: The name of this VLAN as configured on this device. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanName: If op_VlanName is specified, the field named in this input will be compared to the value in VlanName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanName must be specified if op_VlanName is specified.
             :type val_f_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanName: If op_VlanName is specified, this value will be compared to the value in VlanName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanName must be specified if op_VlanName is specified.
             :type val_c_VlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanState: The operator to apply to the field VlanState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanState: The state of this VLAN on this device. Empty for non-bridge members.

The state 'mtuTooBigForDevice' indicates that this device cannot participate in this VLAN because the VLAN's MTU is larger than the device can support.

The state 'mtuTooBigForTrunk' indicates that while this VLAN's MTU is supported by this device, it is too large for one or more of the device's trunk ports. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanState: If op_VlanState is specified, the field named in this input will be compared to the value in VlanState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanState must be specified if op_VlanState is specified.
             :type val_f_VlanState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanState: If op_VlanState is specified, this value will be compared to the value in VlanState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanState must be specified if op_VlanState is specified.
             :type val_c_VlanState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanType: The operator to apply to the field VlanType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanType: The type of this VLAN (1:ethernet, 2:fddi, 3:tokenRing, 4:fddiNet, 5:trNet, 6:deprecated) as configured on this device. Empty for non-bridge members. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanType: If op_VlanType is specified, the field named in this input will be compared to the value in VlanType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanType must be specified if op_VlanType is specified.
             :type val_f_VlanType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanType: If op_VlanType is specified, this value will be compared to the value in VlanType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanType must be specified if op_VlanType is specified.
             :type val_c_VlanType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_network_id: The operator to apply to the field network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. network_id: The Network View ID assigned to the Vlan membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the vlan members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of vlan member methods. The listed methods will be called on each vlan member returned and included in the output. Available methods are: network_id, data_source, device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface, vlan.
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
            |  ``default:`` VlanMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VlanMemberID. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay.
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

             :param select: The list of attributes to return for each VlanMember. Valid values are VlanMemberID, VlanMemberStartTime, VlanMemberEndTime, VlanMemberChangedCols, VlanMemberTimestamp, DataSourceID, DeviceID, VlanID, InterfaceID, BridgeMemberInd, VlanState, VlanType, VlanName, VTPDomain, RootBridgeAddress, BaseBridgeAddress, BaseNumPorts, StpDesignatedRoot, StpProtocolSpecification, StpPriority, StpTopChanges, StpRootCost, StpRootPort, StpMaxAge, StpHelloTime, StpHoldTime, StpForwardDelay, StpBridgeMaxAge, StpBridgeHelloTime, StpBridgeForwardDelay. If empty or omitted, all attributes will be returned.
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

             :return vlan_members: An array of the VlanMember objects that match the specified input criteria.
             :rtype vlan_members: Array of VlanMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def interface(self, **kwargs):
        """The switched virtual interface for this VLAN on this device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The switched virtual interface for this VLAN on this device.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def vlan(self, **kwargs):
        """The VLAN associated with this VLAN membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VLAN associated with this VLAN membership.
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def infradevice(self, **kwargs):
        """The device associated with this VLAN membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device associated with this VLAN membership.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def network_id(self, **kwargs):
        """The Network View ID assigned to the Vlan membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Network View ID assigned to the Vlan membership.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("network_id"), kwargs)

    def device(self, **kwargs):
        """The device associated with this VLAN membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VlanMemberID: The internal NetMRI identifier for this VLAN membership.
             :type VlanMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device associated with this VLAN membership.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
