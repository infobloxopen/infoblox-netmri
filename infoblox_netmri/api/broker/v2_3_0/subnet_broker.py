from ..broker import Broker


class SubnetBroker(Broker):
    controller = "subnets"

    def show(self, **kwargs):
        """Shows the details for the specified subnet.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet methods. The listed methods will be called on each subnet returned and included in the output. Available methods are: network_name, data_source, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return subnet: The subnet identified by the specified SubnetID.
             :rtype subnet: Subnet

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available subnets. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetCIDR: The subnet in CIDR format.
             :type SubnetCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetCIDR: The subnet in CIDR format.
             :type SubnetCIDR: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network address.
             :type SubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network address.
             :type SubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined.
             :type VirtualNetworkID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined.
             :type VlanID: Array of Integer

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

             :param timestamp: The data returned will represent the subnets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet methods. The listed methods will be called on each subnet returned and included in the output. Available methods are: network_name, data_source, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, vlan.
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
            |  ``default:`` SubnetID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetID. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd.
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

             :param select: The list of attributes to return for each Subnet. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd. If empty or omitted, all attributes will be returned.
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

             :return subnets: An array of the Subnet objects that match the specified input criteria.
             :rtype subnets: Array of Subnet

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available subnets matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

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

             :param RouteTimestamp: The date and time that this subnet was last seen on any router.
             :type RouteTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteTimestamp: The date and time that this subnet was last seen on any router.
             :type RouteTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetCIDR: The subnet in CIDR format.
             :type SubnetCIDR: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetCIDR: The subnet in CIDR format.
             :type SubnetCIDR: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubnetChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubnetChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SubnetEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type SubnetEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPDotted: The subnet network address in dotted (or colon-delimited for IPv6) format.
             :type SubnetIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPDotted: The subnet network address in dotted (or colon-delimited for IPv6) format.
             :type SubnetIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network address.
             :type SubnetIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetIPNumeric: The numerical value of the network address.
             :type SubnetIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetLastIPNumeric: The last IP address in the subnet. All IPs in the subnet will be between SubnetIPNumeric (Network Address, Numerical) and SubnetLastIPNumeric (Last IP Address, Numerical), inclusive.
             :type SubnetLastIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetLastIPNumeric: The last IP address in the subnet. All IPs in the subnet will be between SubnetIPNumeric (Network Address, Numerical) and SubnetLastIPNumeric (Last IP Address, Numerical), inclusive.
             :type SubnetLastIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetLocation: If the subnet is located within the NetMRI's configured CIDR blocks, it is identified as 'internal'. Otherwise, it is identified as 'external'.
             :type SubnetLocation: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetLocation: If the subnet is located within the NetMRI's configured CIDR blocks, it is identified as 'internal'. Otherwise, it is identified as 'external'.
             :type SubnetLocation: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetNetMaskDotted: The subnet network mask in dotted (or colon-delimited for IPv6) format.
             :type SubnetNetMaskDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetNetMaskDotted: The subnet network mask in dotted (or colon-delimited for IPv6) format.
             :type SubnetNetMaskDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetNetMaskNumeric: The numerical value of the network mask.
             :type SubnetNetMaskNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetNetMaskNumeric: The numerical value of the network mask.
             :type SubnetNetMaskNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetSdnInd: A flag indicating if this subnet collected from some SDN controller.
             :type SubnetSdnInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetSdnInd: A flag indicating if this subnet collected from some SDN controller.
             :type SubnetSdnInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetSource: Internal tracking information for NetMRI algorithms.
             :type SubnetSource: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetSource: Internal tracking information for NetMRI algorithms.
             :type SubnetSource: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetStartTime: The starting effective time of this revision of the record.
             :type SubnetStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetStartTime: The starting effective time of this revision of the record.
             :type SubnetStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetTimestamp: The date and time this record was collected or calculated.
             :type SubnetTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubnetTimestamp: The date and time this record was collected or calculated.
             :type SubnetTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined.
             :type VirtualNetworkID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined.
             :type VlanID: Array of Integer

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

             :param timestamp: The data returned will represent the subnets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet methods. The listed methods will be called on each subnet returned and included in the output. Available methods are: network_name, data_source, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, vlan.
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
            |  ``default:`` SubnetID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetID. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd.
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

             :param select: The list of attributes to return for each Subnet. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against subnets, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, RouteTimestamp, SubnetCIDR, SubnetChangedCols, SubnetEndTime, SubnetID, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetLocation, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetSdnInd, SubnetSource, SubnetStartTime, SubnetTimestamp, VirtualNetworkID, VlanID.
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

             :return subnets: An array of the Subnet objects that match the specified input criteria.
             :rtype subnets: Array of Subnet

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available subnets matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, RouteTimestamp, SubnetCIDR, SubnetChangedCols, SubnetEndTime, SubnetID, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetLocation, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetSdnInd, SubnetSource, SubnetStartTime, SubnetTimestamp, VirtualNetworkID, VlanID.

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

             :param op_RouteTimestamp: The operator to apply to the field RouteTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteTimestamp: The date and time that this subnet was last seen on any router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteTimestamp: If op_RouteTimestamp is specified, the field named in this input will be compared to the value in RouteTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteTimestamp must be specified if op_RouteTimestamp is specified.
             :type val_f_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteTimestamp: If op_RouteTimestamp is specified, this value will be compared to the value in RouteTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteTimestamp must be specified if op_RouteTimestamp is specified.
             :type val_c_RouteTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetCIDR: The operator to apply to the field SubnetCIDR. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetCIDR: The subnet in CIDR format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetCIDR: If op_SubnetCIDR is specified, the field named in this input will be compared to the value in SubnetCIDR using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetCIDR must be specified if op_SubnetCIDR is specified.
             :type val_f_SubnetCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetCIDR: If op_SubnetCIDR is specified, this value will be compared to the value in SubnetCIDR using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetCIDR must be specified if op_SubnetCIDR is specified.
             :type val_c_SubnetCIDR: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetChangedCols: The operator to apply to the field SubnetChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetChangedCols: If op_SubnetChangedCols is specified, the field named in this input will be compared to the value in SubnetChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetChangedCols must be specified if op_SubnetChangedCols is specified.
             :type val_f_SubnetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetChangedCols: If op_SubnetChangedCols is specified, this value will be compared to the value in SubnetChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetChangedCols must be specified if op_SubnetChangedCols is specified.
             :type val_c_SubnetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetEndTime: The operator to apply to the field SubnetEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetEndTime: If op_SubnetEndTime is specified, the field named in this input will be compared to the value in SubnetEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetEndTime must be specified if op_SubnetEndTime is specified.
             :type val_f_SubnetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetEndTime: If op_SubnetEndTime is specified, this value will be compared to the value in SubnetEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetEndTime must be specified if op_SubnetEndTime is specified.
             :type val_c_SubnetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetID: The operator to apply to the field SubnetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetID: The internal NetMRI identifier for this subnet. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetID: If op_SubnetID is specified, the field named in this input will be compared to the value in SubnetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetID must be specified if op_SubnetID is specified.
             :type val_f_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetID: If op_SubnetID is specified, this value will be compared to the value in SubnetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetID must be specified if op_SubnetID is specified.
             :type val_c_SubnetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetIPDotted: The operator to apply to the field SubnetIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetIPDotted: The subnet network address in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SubnetIPNumeric: The operator to apply to the field SubnetIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetIPNumeric: The numerical value of the network address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SubnetLastIPNumeric: The operator to apply to the field SubnetLastIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetLastIPNumeric: The last IP address in the subnet. All IPs in the subnet will be between SubnetIPNumeric (Network Address, Numerical) and SubnetLastIPNumeric (Last IP Address, Numerical), inclusive. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetLastIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetLastIPNumeric: If op_SubnetLastIPNumeric is specified, the field named in this input will be compared to the value in SubnetLastIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetLastIPNumeric must be specified if op_SubnetLastIPNumeric is specified.
             :type val_f_SubnetLastIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetLastIPNumeric: If op_SubnetLastIPNumeric is specified, this value will be compared to the value in SubnetLastIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetLastIPNumeric must be specified if op_SubnetLastIPNumeric is specified.
             :type val_c_SubnetLastIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetLocation: The operator to apply to the field SubnetLocation. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetLocation: If the subnet is located within the NetMRI's configured CIDR blocks, it is identified as 'internal'. Otherwise, it is identified as 'external'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetLocation: If op_SubnetLocation is specified, the field named in this input will be compared to the value in SubnetLocation using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetLocation must be specified if op_SubnetLocation is specified.
             :type val_f_SubnetLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetLocation: If op_SubnetLocation is specified, this value will be compared to the value in SubnetLocation using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetLocation must be specified if op_SubnetLocation is specified.
             :type val_c_SubnetLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetNetMaskDotted: The operator to apply to the field SubnetNetMaskDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetNetMaskDotted: The subnet network mask in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetNetMaskDotted: If op_SubnetNetMaskDotted is specified, the field named in this input will be compared to the value in SubnetNetMaskDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetNetMaskDotted must be specified if op_SubnetNetMaskDotted is specified.
             :type val_f_SubnetNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetNetMaskDotted: If op_SubnetNetMaskDotted is specified, this value will be compared to the value in SubnetNetMaskDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetNetMaskDotted must be specified if op_SubnetNetMaskDotted is specified.
             :type val_c_SubnetNetMaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetNetMaskNumeric: The operator to apply to the field SubnetNetMaskNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetNetMaskNumeric: The numerical value of the network mask. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetNetMaskNumeric: If op_SubnetNetMaskNumeric is specified, the field named in this input will be compared to the value in SubnetNetMaskNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetNetMaskNumeric must be specified if op_SubnetNetMaskNumeric is specified.
             :type val_f_SubnetNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetNetMaskNumeric: If op_SubnetNetMaskNumeric is specified, this value will be compared to the value in SubnetNetMaskNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetNetMaskNumeric must be specified if op_SubnetNetMaskNumeric is specified.
             :type val_c_SubnetNetMaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetSdnInd: The operator to apply to the field SubnetSdnInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetSdnInd: A flag indicating if this subnet collected from some SDN controller. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetSdnInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetSdnInd: If op_SubnetSdnInd is specified, the field named in this input will be compared to the value in SubnetSdnInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetSdnInd must be specified if op_SubnetSdnInd is specified.
             :type val_f_SubnetSdnInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetSdnInd: If op_SubnetSdnInd is specified, this value will be compared to the value in SubnetSdnInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetSdnInd must be specified if op_SubnetSdnInd is specified.
             :type val_c_SubnetSdnInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetSource: The operator to apply to the field SubnetSource. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetSource: Internal tracking information for NetMRI algorithms. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetSource: If op_SubnetSource is specified, the field named in this input will be compared to the value in SubnetSource using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetSource must be specified if op_SubnetSource is specified.
             :type val_f_SubnetSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetSource: If op_SubnetSource is specified, this value will be compared to the value in SubnetSource using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetSource must be specified if op_SubnetSource is specified.
             :type val_c_SubnetSource: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetStartTime: The operator to apply to the field SubnetStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetStartTime: If op_SubnetStartTime is specified, the field named in this input will be compared to the value in SubnetStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetStartTime must be specified if op_SubnetStartTime is specified.
             :type val_f_SubnetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetStartTime: If op_SubnetStartTime is specified, this value will be compared to the value in SubnetStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetStartTime must be specified if op_SubnetStartTime is specified.
             :type val_c_SubnetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubnetTimestamp: The operator to apply to the field SubnetTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubnetTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubnetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubnetTimestamp: If op_SubnetTimestamp is specified, the field named in this input will be compared to the value in SubnetTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubnetTimestamp must be specified if op_SubnetTimestamp is specified.
             :type val_f_SubnetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubnetTimestamp: If op_SubnetTimestamp is specified, this value will be compared to the value in SubnetTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubnetTimestamp must be specified if op_SubnetTimestamp is specified.
             :type val_c_SubnetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkID: The operator to apply to the field VirtualNetworkID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkID: The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the subnets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of subnet methods. The listed methods will be called on each subnet returned and included in the output. Available methods are: network_name, data_source, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, vlan.
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
            |  ``default:`` SubnetID

             :param sort: The data field(s) to use for sorting the output. Default is SubnetID. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd.
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

             :param select: The list of attributes to return for each Subnet. Valid values are SubnetID, DataSourceID, SubnetStartTime, SubnetEndTime, SubnetChangedCols, SubnetTimestamp, SubnetSource, SubnetIPDotted, SubnetIPNumeric, SubnetLastIPNumeric, SubnetNetMaskDotted, SubnetNetMaskNumeric, SubnetCIDR, SubnetLocation, VlanID, VirtualNetworkID, RouteTimestamp, SubnetSdnInd. If empty or omitted, all attributes will be returned.
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

             :return subnets: An array of the Subnet objects that match the specified input criteria.
             :rtype subnets: Array of Subnet

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def vlan(self, **kwargs):
        """The VLAN on which this subnet is defined, or blank if this cannot be determined.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The VLAN on which this subnet is defined, or blank if this cannot be determined.
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def network_name(self, **kwargs):
        """A Network View assigned to the subnet.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SubnetID: The internal NetMRI identifier for this subnet.
             :type SubnetID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : A Network View assigned to the subnet.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("network_name"), kwargs)
