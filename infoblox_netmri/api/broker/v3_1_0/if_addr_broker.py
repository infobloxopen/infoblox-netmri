from ..broker import Broker


class IfAddrBroker(Broker):
    controller = "if_addrs"

    def show(self, **kwargs):
        """Shows the details for the specified if addr.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if addr methods. The listed methods will be called on each if addr returned and included in the output. Available methods are: vrf_name, vrf_description, vrf_rd, network_id, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, meta, data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_addr: The if addr identified by the specified IfAddrID.
             :rtype if_addr: IfAddr

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available if addrs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing the interface configured with this address.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing the interface configured with this address.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface configured with this address.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface configured with this address.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network portion of the IP address.
             :type SubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network portion of the IP address.
             :type SubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPDotted: The IP address in dotted (or colon-delimited for IPv6) format.
             :type ifIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPDotted: The IP address in dotted (or colon-delimited for IPv6) format.
             :type ifIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPNumeric: The numerical value of the IP address.
             :type ifIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPNumeric: The numerical value of the IP address.
             :type ifIPNumeric: Array of Integer

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

             :param timestamp: The data returned will represent the if addrs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if addr methods. The listed methods will be called on each if addr returned and included in the output. Available methods are: vrf_name, vrf_description, vrf_rd, network_id, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, meta, data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface.
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
            |  ``default:`` IfAddrID

             :param sort: The data field(s) to use for sorting the output. Default is IfAddrID. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID.
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

             :param select: The list of attributes to return for each IfAddr. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID. If empty or omitted, all attributes will be returned.
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

             :return if_addrs: An array of the IfAddr objects that match the specified input criteria.
             :rtype if_addrs: Array of IfAddr

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available if addrs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AciBdID: ID of ACI bridge domain the device is assigned to
             :type AciBdID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AciBdID: ID of ACI bridge domain the device is assigned to
             :type AciBdID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AciEpgID: ID of ACI EPG the device is assigned to
             :type AciEpgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AciEpgID: ID of ACI EPG the device is assigned to
             :type AciEpgID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AddrChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type AddrChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AddrChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type AddrChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AddrEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type AddrEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AddrEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type AddrEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AddrStartTime: The starting effective time of this revision of the record.
             :type AddrStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AddrStartTime: The starting effective time of this revision of the record.
             :type AddrStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AddrTimestamp: The date and time this record was collected or calculated.
             :type AddrTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AddrTimestamp: The date and time this record was collected or calculated.
             :type AddrTimestamp: Array of DateTime

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

             :param DeviceID: The internal NetMRI identifier for the device containing the interface configured with this address.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device containing the interface configured with this address.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface configured with this address.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the interface configured with this address.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPDotted: The network portion of the IP address in dotted (or colon-delimited for IPv6) format.
             :type SubnetIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPDotted: The network portion of the IP address in dotted (or colon-delimited for IPv6) format.
             :type SubnetIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network portion of the IP address.
             :type SubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network portion of the IP address.
             :type SubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPDotted: The IP address in dotted (or colon-delimited for IPv6) format.
             :type ifIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPDotted: The IP address in dotted (or colon-delimited for IPv6) format.
             :type ifIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPNumeric: The numerical value of the IP address.
             :type ifIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIPNumeric: The numerical value of the IP address.
             :type ifIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP interface index of the interface configured with this address.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP interface index of the interface configured with this address.
             :type ifIndex: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifNetMaskDotted: The network mask value in dotted (or colon-delimited for IPv6) format.
             :type ifNetMaskDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifNetMaskDotted: The network mask value in dotted (or colon-delimited for IPv6) format.
             :type ifNetMaskDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifNetMaskNumeric: The numerical value of the network mask.
             :type ifNetMaskNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifNetMaskNumeric: The numerical value of the network mask.
             :type ifNetMaskNumeric: Array of Integer

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

             :param timestamp: The data returned will represent the if addrs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if addr methods. The listed methods will be called on each if addr returned and included in the output. Available methods are: vrf_name, vrf_description, vrf_rd, network_id, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, meta, data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface.
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
            |  ``default:`` IfAddrID

             :param sort: The data field(s) to use for sorting the output. Default is IfAddrID. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID.
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

             :param select: The list of attributes to return for each IfAddr. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if addrs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: AciBdID, AciEpgID, AddrChangedCols, AddrEndTime, AddrStartTime, AddrTimestamp, DataSourceID, DeviceID, IfAddrID, InterfaceID, SubnetIPDotted, SubnetIPNumeric, ifIPDotted, ifIPNumeric, ifIndex, ifNetMaskDotted, ifNetMaskNumeric.
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

             :return if_addrs: An array of the IfAddr objects that match the specified input criteria.
             :rtype if_addrs: Array of IfAddr

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if addrs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: AciBdID, AciEpgID, AddrChangedCols, AddrEndTime, AddrStartTime, AddrTimestamp, DataSourceID, DeviceID, IfAddrID, InterfaceID, SubnetIPDotted, SubnetIPNumeric, ifIPDotted, ifIPNumeric, ifIndex, ifNetMaskDotted, ifNetMaskNumeric.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AciBdID: The operator to apply to the field AciBdID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AciBdID: ID of ACI bridge domain the device is assigned to For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AciBdID: If op_AciBdID is specified, the field named in this input will be compared to the value in AciBdID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AciBdID must be specified if op_AciBdID is specified.
             :type val_f_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AciBdID: If op_AciBdID is specified, this value will be compared to the value in AciBdID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AciBdID must be specified if op_AciBdID is specified.
             :type val_c_AciBdID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AciEpgID: The operator to apply to the field AciEpgID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AciEpgID: ID of ACI EPG the device is assigned to For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AciEpgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AciEpgID: If op_AciEpgID is specified, the field named in this input will be compared to the value in AciEpgID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AciEpgID must be specified if op_AciEpgID is specified.
             :type val_f_AciEpgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AciEpgID: If op_AciEpgID is specified, this value will be compared to the value in AciEpgID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AciEpgID must be specified if op_AciEpgID is specified.
             :type val_c_AciEpgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AddrChangedCols: The operator to apply to the field AddrChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AddrChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AddrChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AddrChangedCols: If op_AddrChangedCols is specified, the field named in this input will be compared to the value in AddrChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AddrChangedCols must be specified if op_AddrChangedCols is specified.
             :type val_f_AddrChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AddrChangedCols: If op_AddrChangedCols is specified, this value will be compared to the value in AddrChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AddrChangedCols must be specified if op_AddrChangedCols is specified.
             :type val_c_AddrChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AddrEndTime: The operator to apply to the field AddrEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AddrEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AddrEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AddrEndTime: If op_AddrEndTime is specified, the field named in this input will be compared to the value in AddrEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AddrEndTime must be specified if op_AddrEndTime is specified.
             :type val_f_AddrEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AddrEndTime: If op_AddrEndTime is specified, this value will be compared to the value in AddrEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AddrEndTime must be specified if op_AddrEndTime is specified.
             :type val_c_AddrEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AddrStartTime: The operator to apply to the field AddrStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AddrStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AddrStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AddrStartTime: If op_AddrStartTime is specified, the field named in this input will be compared to the value in AddrStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AddrStartTime must be specified if op_AddrStartTime is specified.
             :type val_f_AddrStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AddrStartTime: If op_AddrStartTime is specified, this value will be compared to the value in AddrStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AddrStartTime must be specified if op_AddrStartTime is specified.
             :type val_c_AddrStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AddrTimestamp: The operator to apply to the field AddrTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AddrTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AddrTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AddrTimestamp: If op_AddrTimestamp is specified, the field named in this input will be compared to the value in AddrTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AddrTimestamp must be specified if op_AddrTimestamp is specified.
             :type val_f_AddrTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AddrTimestamp: If op_AddrTimestamp is specified, this value will be compared to the value in AddrTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AddrTimestamp must be specified if op_AddrTimestamp is specified.
             :type val_c_AddrTimestamp: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device containing the interface configured with this address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfAddrID: The operator to apply to the field IfAddrID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfAddrID: If op_IfAddrID is specified, the field named in this input will be compared to the value in IfAddrID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_f_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfAddrID: If op_IfAddrID is specified, this value will be compared to the value in IfAddrID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfAddrID must be specified if op_IfAddrID is specified.
             :type val_c_IfAddrID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the interface configured with this address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SubnetIPDotted: The operator to apply to the field SubnetIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetIPDotted: The network portion of the IP address in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetIPDotted: If op_SubnetIPDotted is specified, the field named in this input will be compared to the value in SubnetIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetIPDotted must be specified if op_SubnetIPDotted is specified.
             :type val_f_SubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetIPDotted: If op_SubnetIPDotted is specified, this value will be compared to the value in SubnetIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetIPDotted must be specified if op_SubnetIPDotted is specified.
             :type val_c_SubnetIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetIPNumeric: The operator to apply to the field SubnetIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetIPNumeric: The numerical value of the network portion of the IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetIPNumeric: If op_SubnetIPNumeric is specified, the field named in this input will be compared to the value in SubnetIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetIPNumeric must be specified if op_SubnetIPNumeric is specified.
             :type val_f_SubnetIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetIPNumeric: If op_SubnetIPNumeric is specified, this value will be compared to the value in SubnetIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetIPNumeric must be specified if op_SubnetIPNumeric is specified.
             :type val_c_SubnetIPNumeric: String

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

             :param op_ifIPDotted: The operator to apply to the field ifIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIPDotted: The IP address in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIPDotted: If op_ifIPDotted is specified, the field named in this input will be compared to the value in ifIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIPDotted must be specified if op_ifIPDotted is specified.
             :type val_f_ifIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIPDotted: If op_ifIPDotted is specified, this value will be compared to the value in ifIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIPDotted must be specified if op_ifIPDotted is specified.
             :type val_c_ifIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIPNumeric: The operator to apply to the field ifIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIPNumeric: The numerical value of the IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIPNumeric: If op_ifIPNumeric is specified, the field named in this input will be compared to the value in ifIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIPNumeric must be specified if op_ifIPNumeric is specified.
             :type val_f_ifIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIPNumeric: If op_ifIPNumeric is specified, this value will be compared to the value in ifIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIPNumeric must be specified if op_ifIPNumeric is specified.
             :type val_c_ifIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP interface index of the interface configured with this address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ifNetMaskDotted: The operator to apply to the field ifNetMaskDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifNetMaskDotted: The network mask value in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifNetMaskDotted: If op_ifNetMaskDotted is specified, the field named in this input will be compared to the value in ifNetMaskDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifNetMaskDotted must be specified if op_ifNetMaskDotted is specified.
             :type val_f_ifNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifNetMaskDotted: If op_ifNetMaskDotted is specified, this value will be compared to the value in ifNetMaskDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifNetMaskDotted must be specified if op_ifNetMaskDotted is specified.
             :type val_c_ifNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifNetMaskNumeric: The operator to apply to the field ifNetMaskNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifNetMaskNumeric: The numerical value of the network mask. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifNetMaskNumeric: If op_ifNetMaskNumeric is specified, the field named in this input will be compared to the value in ifNetMaskNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifNetMaskNumeric must be specified if op_ifNetMaskNumeric is specified.
             :type val_f_ifNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifNetMaskNumeric: If op_ifNetMaskNumeric is specified, this value will be compared to the value in ifNetMaskNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifNetMaskNumeric must be specified if op_ifNetMaskNumeric is specified.
             :type val_c_ifNetMaskNumeric: String

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

             :param timestamp: The data returned will represent the if addrs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if addr methods. The listed methods will be called on each if addr returned and included in the output. Available methods are: vrf_name, vrf_description, vrf_rd, network_id, cap_if_net_provisioning_ipv4_ind, cap_if_net_provisioning_ipv6_ind, cap_if_net_deprovisioning_ipv4_ind, cap_if_net_deprovisioning_ipv6_ind, meta, data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device, interface.
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
            |  ``default:`` IfAddrID

             :param sort: The data field(s) to use for sorting the output. Default is IfAddrID. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID.
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

             :param select: The list of attributes to return for each IfAddr. Valid values are IfAddrID, InterfaceID, DeviceID, ifIndex, DataSourceID, AddrStartTime, AddrEndTime, AddrChangedCols, AddrTimestamp, ifIPDotted, ifIPNumeric, ifNetMaskDotted, ifNetMaskNumeric, SubnetIPNumeric, SubnetIPDotted, AciBdID, AciEpgID. If empty or omitted, all attributes will be returned.
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

             :return if_addrs: An array of the IfAddr objects that match the specified input criteria.
             :rtype if_addrs: Array of IfAddr

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

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
        """The interface configured with this address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The interface configured with this address.
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device containing the interface configured with this address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing the interface configured with this address.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def network_id(self, **kwargs):
        """The Network View ID assigned to the interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

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

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

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

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

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

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VRF route distinguisher of the vrf  assigned to the interface.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("vrf_rd"), kwargs)

    def cap_if_net_provisioning_ipv4_ind(self, **kwargs):
        """Capability to provision an ipv4 network on this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability to provision an ipv4 network on this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv4_ind"), kwargs)

    def cap_if_net_provisioning_ipv6_ind(self, **kwargs):
        """Capability to provision an ipv6 network on this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability to provision an ipv6 network on this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_provisioning_ipv6_ind"), kwargs)

    def cap_if_net_deprovisioning_ipv4_ind(self, **kwargs):
        """Capability of de-provisioning an ipv4 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of de-provisioning an ipv4 network from this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv4_ind"), kwargs)

    def cap_if_net_deprovisioning_ipv6_ind(self, **kwargs):
        """Capability of de-provisioning an ipv6 network from this interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Capability of de-provisioning an ipv6 network from this interface.
             :rtype : Boolean

            """

        return self.api_request(self._get_method_fullname("cap_if_net_deprovisioning_ipv6_ind"), kwargs)

    def device(self, **kwargs):
        """The device containing the interface configured with this address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfAddrID: The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
             :type IfAddrID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device containing the interface configured with this address.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
