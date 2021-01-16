from ..broker import Broker


class VirtualNetworkMemberBroker(Broker):
    controller = "virtual_network_members"

    def index(self, **kwargs):
        """Lists the available virtual network members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier for the VRF-based VPN related to this record.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberArtificialInd: Indicates is this is an artificial VNM.
             :type VirtualNetworkMemberArtificialInd: Array of Boolean

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Array of Integer

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

             :param methods: A list of virtual network member methods. The listed methods will be called on each virtual network member returned and included in the output. Available methods are: virtual_network, device, assigned_network_id, member_rd.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: virtual_network, device.
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
            |  ``default:`` VirtualNetworkMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VirtualNetworkMemberID. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount.
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

             :param select: The list of attributes to return for each VirtualNetworkMember. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount. If empty or omitted, all attributes will be returned.
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

             :return virtual_network_members: An array of the VirtualNetworkMember objects that match the specified input criteria.
             :rtype virtual_network_members: Array of VirtualNetworkMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified virtual network member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of virtual network member methods. The listed methods will be called on each virtual network member returned and included in the output. Available methods are: virtual_network, device, assigned_network_id, member_rd.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: virtual_network, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return virtual_network_member: The virtual network member identified by the specified VirtualNetworkMemberID.
             :rtype virtual_network_member: VirtualNetworkMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available virtual network members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier for the VRF-based VPN related to this record.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberArtificialInd: Indicates is this is an artificial VNM.
             :type VirtualNetworkMemberArtificialInd: Array of Boolean

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Array of Integer

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

             :param methods: A list of virtual network member methods. The listed methods will be called on each virtual network member returned and included in the output. Available methods are: virtual_network, device, assigned_network_id, member_rd.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: virtual_network, device.
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
            |  ``default:`` VirtualNetworkMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VirtualNetworkMemberID. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount.
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

             :param select: The list of attributes to return for each VirtualNetworkMember. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against virtual network members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: CurrentCount, DataSourceID, DefaultRDLeft, DefaultRDRight, DefaultRDType, DefaultVPNID, DeviceID, RouteLimit, VirtualNetworkID, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberChangedCols, VirtualNetworkMemberDefaultInd, VirtualNetworkMemberDescription, VirtualNetworkMemberEndTime, VirtualNetworkMemberFirstTime, VirtualNetworkMemberID, VirtualNetworkMemberName, VirtualNetworkMemberStartTime, VirtualNetworkMemberTimestamp, WarningLimit.
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

             :return virtual_network_members: An array of the VirtualNetworkMember objects that match the specified input criteria.
             :rtype virtual_network_members: Array of VirtualNetworkMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available virtual network members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: CurrentCount, DataSourceID, DefaultRDLeft, DefaultRDRight, DefaultRDType, DefaultVPNID, DeviceID, RouteLimit, VirtualNetworkID, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberChangedCols, VirtualNetworkMemberDefaultInd, VirtualNetworkMemberDescription, VirtualNetworkMemberEndTime, VirtualNetworkMemberFirstTime, VirtualNetworkMemberID, VirtualNetworkMemberName, VirtualNetworkMemberStartTime, VirtualNetworkMemberTimestamp, WarningLimit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CurrentCount: The operator to apply to the field CurrentCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CurrentCount: The number of routes currently in the VRF. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CurrentCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CurrentCount: If op_CurrentCount is specified, the field named in this input will be compared to the value in CurrentCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CurrentCount must be specified if op_CurrentCount is specified.
             :type val_f_CurrentCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CurrentCount: If op_CurrentCount is specified, this value will be compared to the value in CurrentCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CurrentCount must be specified if op_CurrentCount is specified.
             :type val_c_CurrentCount: String

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

             :param op_DefaultRDLeft: The operator to apply to the field DefaultRDLeft. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DefaultRDLeft: The left-hand portion of the default Route Distinguisher; use DefaultRDType to identify if it is an AS number or and IPv4 address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DefaultRDLeft: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DefaultRDLeft: If op_DefaultRDLeft is specified, the field named in this input will be compared to the value in DefaultRDLeft using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DefaultRDLeft must be specified if op_DefaultRDLeft is specified.
             :type val_f_DefaultRDLeft: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DefaultRDLeft: If op_DefaultRDLeft is specified, this value will be compared to the value in DefaultRDLeft using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DefaultRDLeft must be specified if op_DefaultRDLeft is specified.
             :type val_c_DefaultRDLeft: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DefaultRDRight: The operator to apply to the field DefaultRDRight. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DefaultRDRight: The right-hand portion of the default Route Distinguisher. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DefaultRDRight: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DefaultRDRight: If op_DefaultRDRight is specified, the field named in this input will be compared to the value in DefaultRDRight using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DefaultRDRight must be specified if op_DefaultRDRight is specified.
             :type val_f_DefaultRDRight: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DefaultRDRight: If op_DefaultRDRight is specified, this value will be compared to the value in DefaultRDRight using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DefaultRDRight must be specified if op_DefaultRDRight is specified.
             :type val_c_DefaultRDRight: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DefaultRDType: The operator to apply to the field DefaultRDType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DefaultRDType: The style of the default Route Distinguisher, asn or ipv4. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DefaultRDType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DefaultRDType: If op_DefaultRDType is specified, the field named in this input will be compared to the value in DefaultRDType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DefaultRDType must be specified if op_DefaultRDType is specified.
             :type val_f_DefaultRDType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DefaultRDType: If op_DefaultRDType is specified, this value will be compared to the value in DefaultRDType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DefaultRDType must be specified if op_DefaultRDType is specified.
             :type val_c_DefaultRDType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DefaultVPNID: The operator to apply to the field DefaultVPNID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DefaultVPNID: The VPN ID assigned to this VRF, as configured on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DefaultVPNID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DefaultVPNID: If op_DefaultVPNID is specified, the field named in this input will be compared to the value in DefaultVPNID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DefaultVPNID must be specified if op_DefaultVPNID is specified.
             :type val_f_DefaultVPNID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DefaultVPNID: If op_DefaultVPNID is specified, this value will be compared to the value in DefaultVPNID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DefaultVPNID must be specified if op_DefaultVPNID is specified.
             :type val_c_DefaultVPNID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this VRF membership configuration was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_RouteLimit: The operator to apply to the field RouteLimit. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteLimit: The maximum number of routes that this VRF is configured to contain. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteLimit: If op_RouteLimit is specified, the field named in this input will be compared to the value in RouteLimit using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteLimit must be specified if op_RouteLimit is specified.
             :type val_f_RouteLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteLimit: If op_RouteLimit is specified, this value will be compared to the value in RouteLimit using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteLimit must be specified if op_RouteLimit is specified.
             :type val_c_RouteLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkID: The operator to apply to the field VirtualNetworkID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkID: The internal NetMRI identifier for the VRF-based VPN related to this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VirtualNetworkMemberArtificialInd: The operator to apply to the field VirtualNetworkMemberArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberArtificialInd: Indicates is this is an artificial VNM. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberArtificialInd: If op_VirtualNetworkMemberArtificialInd is specified, the field named in this input will be compared to the value in VirtualNetworkMemberArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberArtificialInd must be specified if op_VirtualNetworkMemberArtificialInd is specified.
             :type val_f_VirtualNetworkMemberArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberArtificialInd: If op_VirtualNetworkMemberArtificialInd is specified, this value will be compared to the value in VirtualNetworkMemberArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberArtificialInd must be specified if op_VirtualNetworkMemberArtificialInd is specified.
             :type val_c_VirtualNetworkMemberArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberChangedCols: The operator to apply to the field VirtualNetworkMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberChangedCols: If op_VirtualNetworkMemberChangedCols is specified, the field named in this input will be compared to the value in VirtualNetworkMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberChangedCols must be specified if op_VirtualNetworkMemberChangedCols is specified.
             :type val_f_VirtualNetworkMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberChangedCols: If op_VirtualNetworkMemberChangedCols is specified, this value will be compared to the value in VirtualNetworkMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberChangedCols must be specified if op_VirtualNetworkMemberChangedCols is specified.
             :type val_c_VirtualNetworkMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberDefaultInd: The operator to apply to the field VirtualNetworkMemberDefaultInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberDefaultInd: Indicates is this is a default VNM. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberDefaultInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberDefaultInd: If op_VirtualNetworkMemberDefaultInd is specified, the field named in this input will be compared to the value in VirtualNetworkMemberDefaultInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberDefaultInd must be specified if op_VirtualNetworkMemberDefaultInd is specified.
             :type val_f_VirtualNetworkMemberDefaultInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberDefaultInd: If op_VirtualNetworkMemberDefaultInd is specified, this value will be compared to the value in VirtualNetworkMemberDefaultInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberDefaultInd must be specified if op_VirtualNetworkMemberDefaultInd is specified.
             :type val_c_VirtualNetworkMemberDefaultInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberDescription: The operator to apply to the field VirtualNetworkMemberDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberDescription: The description of the VRF as configured on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberDescription: If op_VirtualNetworkMemberDescription is specified, the field named in this input will be compared to the value in VirtualNetworkMemberDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberDescription must be specified if op_VirtualNetworkMemberDescription is specified.
             :type val_f_VirtualNetworkMemberDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberDescription: If op_VirtualNetworkMemberDescription is specified, this value will be compared to the value in VirtualNetworkMemberDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberDescription must be specified if op_VirtualNetworkMemberDescription is specified.
             :type val_c_VirtualNetworkMemberDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberEndTime: The operator to apply to the field VirtualNetworkMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberEndTime: If op_VirtualNetworkMemberEndTime is specified, the field named in this input will be compared to the value in VirtualNetworkMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberEndTime must be specified if op_VirtualNetworkMemberEndTime is specified.
             :type val_f_VirtualNetworkMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberEndTime: If op_VirtualNetworkMemberEndTime is specified, this value will be compared to the value in VirtualNetworkMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberEndTime must be specified if op_VirtualNetworkMemberEndTime is specified.
             :type val_c_VirtualNetworkMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberFirstTime: The operator to apply to the field VirtualNetworkMemberFirstTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberFirstTime: The first time this data element was seen on the network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberFirstTime: If op_VirtualNetworkMemberFirstTime is specified, the field named in this input will be compared to the value in VirtualNetworkMemberFirstTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberFirstTime must be specified if op_VirtualNetworkMemberFirstTime is specified.
             :type val_f_VirtualNetworkMemberFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberFirstTime: If op_VirtualNetworkMemberFirstTime is specified, this value will be compared to the value in VirtualNetworkMemberFirstTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberFirstTime must be specified if op_VirtualNetworkMemberFirstTime is specified.
             :type val_c_VirtualNetworkMemberFirstTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberID: The operator to apply to the field VirtualNetworkMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_VirtualNetworkMemberName: The operator to apply to the field VirtualNetworkMemberName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberName: The name of the VRF as configured on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberName: If op_VirtualNetworkMemberName is specified, the field named in this input will be compared to the value in VirtualNetworkMemberName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberName must be specified if op_VirtualNetworkMemberName is specified.
             :type val_f_VirtualNetworkMemberName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberName: If op_VirtualNetworkMemberName is specified, this value will be compared to the value in VirtualNetworkMemberName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberName must be specified if op_VirtualNetworkMemberName is specified.
             :type val_c_VirtualNetworkMemberName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberStartTime: The operator to apply to the field VirtualNetworkMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberStartTime: If op_VirtualNetworkMemberStartTime is specified, the field named in this input will be compared to the value in VirtualNetworkMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberStartTime must be specified if op_VirtualNetworkMemberStartTime is specified.
             :type val_f_VirtualNetworkMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberStartTime: If op_VirtualNetworkMemberStartTime is specified, this value will be compared to the value in VirtualNetworkMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberStartTime must be specified if op_VirtualNetworkMemberStartTime is specified.
             :type val_c_VirtualNetworkMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkMemberTimestamp: The operator to apply to the field VirtualNetworkMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkMemberTimestamp: If op_VirtualNetworkMemberTimestamp is specified, the field named in this input will be compared to the value in VirtualNetworkMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkMemberTimestamp must be specified if op_VirtualNetworkMemberTimestamp is specified.
             :type val_f_VirtualNetworkMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkMemberTimestamp: If op_VirtualNetworkMemberTimestamp is specified, this value will be compared to the value in VirtualNetworkMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkMemberTimestamp must be specified if op_VirtualNetworkMemberTimestamp is specified.
             :type val_c_VirtualNetworkMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WarningLimit: The operator to apply to the field WarningLimit. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WarningLimit: The number of routes in the VRF that will trigger this device to produce a warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WarningLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WarningLimit: If op_WarningLimit is specified, the field named in this input will be compared to the value in WarningLimit using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WarningLimit must be specified if op_WarningLimit is specified.
             :type val_f_WarningLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WarningLimit: If op_WarningLimit is specified, this value will be compared to the value in WarningLimit using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WarningLimit must be specified if op_WarningLimit is specified.
             :type val_c_WarningLimit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_assigned_network_id: The operator to apply to the field assigned_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. assigned_network_id: The current network view id assigned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_assigned_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_assigned_network_id: If op_assigned_network_id is specified, the field named in this input will be compared to the value in assigned_network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_assigned_network_id must be specified if op_assigned_network_id is specified.
             :type val_f_assigned_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_assigned_network_id: If op_assigned_network_id is specified, this value will be compared to the value in assigned_network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_assigned_network_id must be specified if op_assigned_network_id is specified.
             :type val_c_assigned_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_member_rd: The operator to apply to the field member_rd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. member_rd: The displayable VRF route distinguisher of this obkect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_member_rd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_member_rd: If op_member_rd is specified, the field named in this input will be compared to the value in member_rd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_member_rd must be specified if op_member_rd is specified.
             :type val_f_member_rd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_member_rd: If op_member_rd is specified, this value will be compared to the value in member_rd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_member_rd must be specified if op_member_rd is specified.
             :type val_c_member_rd: String

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

             :param methods: A list of virtual network member methods. The listed methods will be called on each virtual network member returned and included in the output. Available methods are: virtual_network, device, assigned_network_id, member_rd.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: virtual_network, device.
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
            |  ``default:`` VirtualNetworkMemberID

             :param sort: The data field(s) to use for sorting the output. Default is VirtualNetworkMemberID. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount.
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

             :param select: The list of attributes to return for each VirtualNetworkMember. Valid values are VirtualNetworkMemberID, VirtualNetworkMemberStartTime, VirtualNetworkMemberEndTime, VirtualNetworkMemberChangedCols, VirtualNetworkMemberTimestamp, VirtualNetworkMemberFirstTime, DataSourceID, DeviceID, VirtualNetworkID, VirtualNetworkMemberName, VirtualNetworkMemberDescription, VirtualNetworkMemberArtificialInd, VirtualNetworkMemberDefaultInd, DefaultRDType, DefaultRDLeft, DefaultRDRight, DefaultVPNID, RouteLimit, WarningLimit, CurrentCount. If empty or omitted, all attributes will be returned.
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

             :return virtual_network_members: An array of the VirtualNetworkMember objects that match the specified input criteria.
             :rtype virtual_network_members: Array of VirtualNetworkMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device(self, **kwargs):
        """The device from which this VRF membership configuration was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this VRF membership configuration was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def virtual_network(self, **kwargs):
        """Network assigned to current VRF instance.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Network assigned to current VRF instance.
             :rtype : VirtualNetwork

            """

        return self.api_request(self._get_method_fullname("virtual_network"), kwargs)

    def member_rd(self, **kwargs):
        """The displayable VRF route distinguisher of this obkect.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The displayable VRF route distinguisher of this obkect.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("member_rd"), kwargs)

    def assigned_network_id(self, **kwargs):
        """The current network view id assigned.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkMemberID: The internal NetMRI identifier for this VRF membership.
             :type VirtualNetworkMemberID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The current network view id assigned.
             :rtype : Integer

            """

        return self.api_request(self._get_method_fullname("assigned_network_id"), kwargs)
