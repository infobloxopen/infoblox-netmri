from ..broker import Broker


class VirtualNetworkBroker(Broker):
    controller = "virtual_networks"

    def index(self, **kwargs):
        """Lists the available virtual networks. Any of the inputs listed may be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkDeleteInd: Indicates if this Virtual Network has been deleted.
             :type VirtualNetworkDeleteInd: Array of Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` VirtualNetworkID

             :param sort: The data field(s) to use for sorting the output. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each VirtualNetwork. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd. If empty or omitted, all attributes will be returned.
             :type select: Array

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return virtual_networks: An array of the VirtualNetwork objects that match the specified input criteria.
             :rtype virtual_networks: Array of VirtualNetwork

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified virtual network.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier for this Network View.
             :type VirtualNetworkID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return virtual_network: The virtual network identified by the specified VirtualNetworkID.
             :rtype virtual_network: VirtualNetwork

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available virtual networks matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkDeleteInd: Indicates if this Virtual Network has been deleted.
             :type VirtualNetworkDeleteInd: Array of Boolean

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkDescription: A description of this Virtual Network.
             :type VirtualNetworkDescription: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The internal NetMRI identifier for this Network View.
             :type VirtualNetworkID: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkName: The name of the Network View.
             :type VirtualNetworkName: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` VirtualNetworkID

             :param sort: The data field(s) to use for sorting the output. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each VirtualNetwork. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against virtual networks, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: VirtualNetworkDeleteInd, VirtualNetworkDescription, VirtualNetworkID, VirtualNetworkName.
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

             :return virtual_networks: An array of the VirtualNetwork objects that match the specified input criteria.
             :rtype virtual_networks: Array of VirtualNetwork

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available virtual networks matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: VirtualNetworkDeleteInd, VirtualNetworkDescription, VirtualNetworkID, VirtualNetworkName.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkDeleteInd: The operator to apply to the field VirtualNetworkDeleteInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkDeleteInd: Indicates if this Virtual Network has been deleted. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkDeleteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkDeleteInd: If op_VirtualNetworkDeleteInd is specified, the field named in this input will be compared to the value in VirtualNetworkDeleteInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkDeleteInd must be specified if op_VirtualNetworkDeleteInd is specified.
             :type val_f_VirtualNetworkDeleteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkDeleteInd: If op_VirtualNetworkDeleteInd is specified, this value will be compared to the value in VirtualNetworkDeleteInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkDeleteInd must be specified if op_VirtualNetworkDeleteInd is specified. If the rlike or not rlike value is specified in the op_VirtualNetworkDeleteInd field, escape regex special characters because a regular expression is expected.
             :type val_c_VirtualNetworkDeleteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkDescription: The operator to apply to the field VirtualNetworkDescription. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkDescription: A description of this Virtual Network. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkDescription: If op_VirtualNetworkDescription is specified, the field named in this input will be compared to the value in VirtualNetworkDescription using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkDescription must be specified if op_VirtualNetworkDescription is specified.
             :type val_f_VirtualNetworkDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkDescription: If op_VirtualNetworkDescription is specified, this value will be compared to the value in VirtualNetworkDescription using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkDescription must be specified if op_VirtualNetworkDescription is specified. If the rlike or not rlike value is specified in the op_VirtualNetworkDescription field, escape regex special characters because a regular expression is expected.
             :type val_c_VirtualNetworkDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkID: The operator to apply to the field VirtualNetworkID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkID: The internal NetMRI identifier for this Network View. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param val_c_VirtualNetworkID: If op_VirtualNetworkID is specified, this value will be compared to the value in VirtualNetworkID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkID must be specified if op_VirtualNetworkID is specified. If the rlike or not rlike value is specified in the op_VirtualNetworkID field, escape regex special characters because a regular expression is expected.
             :type val_c_VirtualNetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VirtualNetworkName: The operator to apply to the field VirtualNetworkName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VirtualNetworkName: The name of the Network View. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VirtualNetworkName: If op_VirtualNetworkName is specified, the field named in this input will be compared to the value in VirtualNetworkName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VirtualNetworkName must be specified if op_VirtualNetworkName is specified.
             :type val_f_VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VirtualNetworkName: If op_VirtualNetworkName is specified, this value will be compared to the value in VirtualNetworkName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkName must be specified if op_VirtualNetworkName is specified. If the rlike or not rlike value is specified in the op_VirtualNetworkName field, escape regex special characters because a regular expression is expected.
             :type val_c_VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

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
            |  ``default:`` VirtualNetworkID

             :param sort: The data field(s) to use for sorting the output. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each VirtualNetwork. Valid values are VirtualNetworkID, VirtualNetworkName, VirtualNetworkDescription, VirtualNetworkDeleteInd. If empty or omitted, all attributes will be returned.
             :type select: Array

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

             :return virtual_networks: An array of the VirtualNetwork objects that match the specified input criteria.
             :rtype virtual_networks: Array of VirtualNetwork

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Update Virtual Network

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Virtual Network identifier
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkName: The name for Virtual Network, must be unique
             :type VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkDescription: Virtual Network description/comment
             :type VirtualNetworkDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberIDs: An array of VirtualNetworkMember identifiers to be assigned to this Virtual Network, all existing members will be replaced with contents of this array. Note: Using only invalid IDs or empty value will unassign all VirtualNetworkMembers. Use single value -1 to let unchanged the Virtual Network Member list
             :type VirtualNetworkMemberIDs: Array of Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def create(self, **kwargs):
        """Create Virtual Network

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkID: The ID for Virtual Network, must be unique, use only for collector/oc
             :type VirtualNetworkID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param VirtualNetworkName: The name for Virtual Network, must be unique
             :type VirtualNetworkName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkDescription: Virtual Network description/comment
             :type VirtualNetworkDescription: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkMemberIDs: An array of VirtualNetworkMember identifiers
             :type VirtualNetworkMemberIDs: Array of Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def delete(self, **kwargs):
        """Delete Virtual Network

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Virtual Network identifier to delete
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)
