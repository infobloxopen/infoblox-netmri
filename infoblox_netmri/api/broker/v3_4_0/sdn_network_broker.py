from ..broker import Broker


class SdnNetworkBroker(Broker):
    controller = "sdn_networks"

    def index(self, **kwargs):
        """Lists the available sdn networks. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_network_id: The internal NetMRI identifier for this network
             :type sdn_network_id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_network_key: The unique identifier of each network at the SDN controller side
             :type sdn_network_key: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of sdn network methods. The listed methods will be called on each sdn network returned and included in the output. Available methods are: fabric_handle.
             :type methods: Array of String

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
            |  ``default:`` sdn_network_id

             :param sort: The data field(s) to use for sorting the output. Default is sdn_network_id. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime.
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

             :param select: The list of attributes to return for each SdnNetwork. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime. If empty or omitted, all attributes will be returned.
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

             :return sdn_networks: An array of the SdnNetwork objects that match the specified input criteria.
             :rtype sdn_networks: Array of SdnNetwork

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available sdn networks matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The ending date/time of this network
             :type EndTime: Array of DateTime

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The starting date/time of this network
             :type StartTime: Array of DateTime

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fabric_id: Identifier of SdnSetting from which this network was collected
             :type fabric_id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_network_id: The internal NetMRI identifier for this network
             :type sdn_network_id: Array of Integer

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_network_key: The unique identifier of each network at the SDN controller side
             :type sdn_network_key: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sdn_network_name: Name of SDN network
             :type sdn_network_name: Array of String

            |  ``api version min:`` 3.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: ID of Virtual Network which is assigned to this network
             :type virtual_network_id: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of sdn network methods. The listed methods will be called on each sdn network returned and included in the output. Available methods are: fabric_handle.
             :type methods: Array of String

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
            |  ``default:`` sdn_network_id

             :param sort: The data field(s) to use for sorting the output. Default is sdn_network_id. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime.
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

             :param select: The list of attributes to return for each SdnNetwork. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against sdn networks, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: EndTime, StartTime, fabric_id, sdn_network_id, sdn_network_key, sdn_network_name, virtual_network_id.
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

             :return sdn_networks: An array of the SdnNetwork objects that match the specified input criteria.
             :rtype sdn_networks: Array of SdnNetwork

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available sdn networks matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: EndTime, StartTime, fabric_id, sdn_network_id, sdn_network_key, sdn_network_name, virtual_network_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndTime: The operator to apply to the field EndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndTime: The ending date/time of this network For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndTime: If op_EndTime is specified, the field named in this input will be compared to the value in EndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndTime must be specified if op_EndTime is specified.
             :type val_f_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndTime: If op_EndTime is specified, this value will be compared to the value in EndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndTime must be specified if op_EndTime is specified.
             :type val_c_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The starting date/time of this network For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_fabric_handle: The operator to apply to the field fabric_handle. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. fabric_handle: Name of SDN controller from which this network was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_fabric_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_fabric_handle: If op_fabric_handle is specified, the field named in this input will be compared to the value in fabric_handle using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_fabric_handle must be specified if op_fabric_handle is specified.
             :type val_f_fabric_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_fabric_handle: If op_fabric_handle is specified, this value will be compared to the value in fabric_handle using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_fabric_handle must be specified if op_fabric_handle is specified.
             :type val_c_fabric_handle: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_fabric_id: The operator to apply to the field fabric_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. fabric_id: Identifier of SdnSetting from which this network was collected For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_fabric_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_fabric_id: If op_fabric_id is specified, the field named in this input will be compared to the value in fabric_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_fabric_id must be specified if op_fabric_id is specified.
             :type val_f_fabric_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_fabric_id: If op_fabric_id is specified, this value will be compared to the value in fabric_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_fabric_id must be specified if op_fabric_id is specified.
             :type val_c_fabric_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_network_id: The operator to apply to the field sdn_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_network_id: The internal NetMRI identifier for this network For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_network_id: If op_sdn_network_id is specified, the field named in this input will be compared to the value in sdn_network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_network_id must be specified if op_sdn_network_id is specified.
             :type val_f_sdn_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_network_id: If op_sdn_network_id is specified, this value will be compared to the value in sdn_network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_network_id must be specified if op_sdn_network_id is specified.
             :type val_c_sdn_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_network_key: The operator to apply to the field sdn_network_key. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_network_key: The unique identifier of each network at the SDN controller side For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_network_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_network_key: If op_sdn_network_key is specified, the field named in this input will be compared to the value in sdn_network_key using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_network_key must be specified if op_sdn_network_key is specified.
             :type val_f_sdn_network_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_network_key: If op_sdn_network_key is specified, this value will be compared to the value in sdn_network_key using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_network_key must be specified if op_sdn_network_key is specified.
             :type val_c_sdn_network_key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sdn_network_name: The operator to apply to the field sdn_network_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sdn_network_name: Name of SDN network For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sdn_network_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sdn_network_name: If op_sdn_network_name is specified, the field named in this input will be compared to the value in sdn_network_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sdn_network_name must be specified if op_sdn_network_name is specified.
             :type val_f_sdn_network_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sdn_network_name: If op_sdn_network_name is specified, this value will be compared to the value in sdn_network_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sdn_network_name must be specified if op_sdn_network_name is specified.
             :type val_c_sdn_network_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_virtual_network_id: The operator to apply to the field virtual_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. virtual_network_id: ID of Virtual Network which is assigned to this network For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_virtual_network_id: If op_virtual_network_id is specified, the field named in this input will be compared to the value in virtual_network_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_virtual_network_id must be specified if op_virtual_network_id is specified.
             :type val_f_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_virtual_network_id: If op_virtual_network_id is specified, this value will be compared to the value in virtual_network_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_virtual_network_id must be specified if op_virtual_network_id is specified.
             :type val_c_virtual_network_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of sdn network methods. The listed methods will be called on each sdn network returned and included in the output. Available methods are: fabric_handle.
             :type methods: Array of String

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
            |  ``default:`` sdn_network_id

             :param sort: The data field(s) to use for sorting the output. Default is sdn_network_id. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime.
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

             :param select: The list of attributes to return for each SdnNetwork. Valid values are sdn_network_id, sdn_network_key, sdn_network_name, fabric_id, virtual_network_id, StartTime, EndTime. If empty or omitted, all attributes will be returned.
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

             :return sdn_networks: An array of the SdnNetwork objects that match the specified input criteria.
             :rtype sdn_networks: Array of SdnNetwork

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified sdn network.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param sdn_network_id: The internal NetMRI identifier for this network
             :type sdn_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of sdn network methods. The listed methods will be called on each sdn network returned and included in the output. Available methods are: fabric_handle.
             :type methods: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sdn_network: The sdn network identified by the specified sdn_network_id.
             :rtype sdn_network: SdnNetwork

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)
