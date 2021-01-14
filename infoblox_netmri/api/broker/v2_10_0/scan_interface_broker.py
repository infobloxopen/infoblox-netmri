from ..broker import Broker


class ScanInterfaceBroker(Broker):
    controller = "scan_interfaces"

    def index(self, **kwargs):
        """Lists the available scan interfaces. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Scan Interface.
             :type id: Array of Integer

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains.
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

             :param select: The list of attributes to return for each ScanInterface. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains. If empty or omitted, all attributes will be returned.
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

             :return scan_interfaces: An array of the ScanInterface objects that match the specified input criteria.
             :rtype scan_interfaces: Array of ScanInterface

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified scan interface.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Scan Interface.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return scan_interface: The scan interface identified by the specified id.
             :rtype scan_interface: ScanInterface

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available scan interfaces matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param encap_tag: The 802.1Q encapsulation tag of traffic to be forwarded from the physical interface to the scan interface.
             :type encap_tag: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Scan Interface.
             :type id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param if_dev: The system device name of the scan interface.
             :type if_dev: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_address: The IP address of the scan interface in dotted format.
             :type ipv4_address: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_gateway: The gateway of the scan interface in dotted format.
             :type ipv4_gateway: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_mask: The network mask of the scan interface in dotted format.
             :type ipv4_mask: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_address: The IPv6 address of the scan interface in colon-delimited format.
             :type ipv6_address: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_gateway: The gateway of the scan interface in colon-delimited format IPv6.
             :type ipv6_gateway: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_prefix: The IPv6 mask of the scan interface.
             :type ipv6_prefix: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the scan interface.
             :type name: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param physical_if_id: The scan interface identifier of the physical interface, if this is a sub-interface.
             :type physical_if_id: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param primary_dns_server: The IP address of the scan interface primary dns server in dotted format.
             :type primary_dns_server: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_domains: Search domains for DNS resolving.
             :type search_domains: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secondary_dns_server: The IP address of the scan interface secondary dns server in dotted format.
             :type secondary_dns_server: Array of String

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: The internal identifier for the collector on which the scan interface exists.
             :type unit_id: Array of Integer

            |  ``api version min:`` 2.10
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the Virtual Network in which the scan interface is present.
             :type virtual_network_id: Array of Integer

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains.
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

             :param select: The list of attributes to return for each ScanInterface. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against scan interfaces, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: encap_tag, id, if_dev, ipv4_address, ipv4_gateway, ipv4_mask, ipv6_address, ipv6_gateway, ipv6_prefix, name, physical_if_id, primary_dns_server, search_domains, secondary_dns_server, unit_id, virtual_network_id.
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

             :return scan_interfaces: An array of the ScanInterface objects that match the specified input criteria.
             :rtype scan_interfaces: Array of ScanInterface

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available scan interfaces matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: encap_tag, id, if_dev, ipv4_address, ipv4_gateway, ipv4_mask, ipv6_address, ipv6_gateway, ipv6_prefix, name, physical_if_id, primary_dns_server, search_domains, secondary_dns_server, unit_id, virtual_network_id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_encap_tag: The operator to apply to the field encap_tag. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. encap_tag: The 802.1Q encapsulation tag of traffic to be forwarded from the physical interface to the scan interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_encap_tag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_encap_tag: If op_encap_tag is specified, the field named in this input will be compared to the value in encap_tag using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_encap_tag must be specified if op_encap_tag is specified.
             :type val_f_encap_tag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_encap_tag: If op_encap_tag is specified, this value will be compared to the value in encap_tag using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_encap_tag must be specified if op_encap_tag is specified.
             :type val_c_encap_tag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier of the Scan Interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_id: If op_id is specified, the field named in this input will be compared to the value in id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_id must be specified if op_id is specified.
             :type val_f_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_id: If op_id is specified, this value will be compared to the value in id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_id must be specified if op_id is specified.
             :type val_c_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_if_dev: The operator to apply to the field if_dev. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. if_dev: The system device name of the scan interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_if_dev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_if_dev: If op_if_dev is specified, the field named in this input will be compared to the value in if_dev using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_if_dev must be specified if op_if_dev is specified.
             :type val_f_if_dev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_if_dev: If op_if_dev is specified, this value will be compared to the value in if_dev using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_if_dev must be specified if op_if_dev is specified.
             :type val_c_if_dev: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv4_address: The operator to apply to the field ipv4_address. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv4_address: The IP address of the scan interface in dotted format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv4_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv4_address: If op_ipv4_address is specified, the field named in this input will be compared to the value in ipv4_address using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv4_address must be specified if op_ipv4_address is specified.
             :type val_f_ipv4_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv4_address: If op_ipv4_address is specified, this value will be compared to the value in ipv4_address using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv4_address must be specified if op_ipv4_address is specified.
             :type val_c_ipv4_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv4_gateway: The operator to apply to the field ipv4_gateway. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv4_gateway: The gateway of the scan interface in dotted format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv4_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv4_gateway: If op_ipv4_gateway is specified, the field named in this input will be compared to the value in ipv4_gateway using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv4_gateway must be specified if op_ipv4_gateway is specified.
             :type val_f_ipv4_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv4_gateway: If op_ipv4_gateway is specified, this value will be compared to the value in ipv4_gateway using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv4_gateway must be specified if op_ipv4_gateway is specified.
             :type val_c_ipv4_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv4_mask: The operator to apply to the field ipv4_mask. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv4_mask: The network mask of the scan interface in dotted format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv4_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv4_mask: If op_ipv4_mask is specified, the field named in this input will be compared to the value in ipv4_mask using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv4_mask must be specified if op_ipv4_mask is specified.
             :type val_f_ipv4_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv4_mask: If op_ipv4_mask is specified, this value will be compared to the value in ipv4_mask using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv4_mask must be specified if op_ipv4_mask is specified.
             :type val_c_ipv4_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv6_address: The operator to apply to the field ipv6_address. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv6_address: The IPv6 address of the scan interface in colon-delimited format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv6_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv6_address: If op_ipv6_address is specified, the field named in this input will be compared to the value in ipv6_address using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv6_address must be specified if op_ipv6_address is specified.
             :type val_f_ipv6_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv6_address: If op_ipv6_address is specified, this value will be compared to the value in ipv6_address using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv6_address must be specified if op_ipv6_address is specified.
             :type val_c_ipv6_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv6_gateway: The operator to apply to the field ipv6_gateway. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv6_gateway: The gateway of the scan interface in colon-delimited format IPv6. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv6_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv6_gateway: If op_ipv6_gateway is specified, the field named in this input will be compared to the value in ipv6_gateway using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv6_gateway must be specified if op_ipv6_gateway is specified.
             :type val_f_ipv6_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv6_gateway: If op_ipv6_gateway is specified, this value will be compared to the value in ipv6_gateway using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv6_gateway must be specified if op_ipv6_gateway is specified.
             :type val_c_ipv6_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ipv6_prefix: The operator to apply to the field ipv6_prefix. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ipv6_prefix: The IPv6 mask of the scan interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ipv6_prefix: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ipv6_prefix: If op_ipv6_prefix is specified, the field named in this input will be compared to the value in ipv6_prefix using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ipv6_prefix must be specified if op_ipv6_prefix is specified.
             :type val_f_ipv6_prefix: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ipv6_prefix: If op_ipv6_prefix is specified, this value will be compared to the value in ipv6_prefix using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ipv6_prefix must be specified if op_ipv6_prefix is specified.
             :type val_c_ipv6_prefix: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of the scan interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_name: If op_name is specified, the field named in this input will be compared to the value in name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_name must be specified if op_name is specified.
             :type val_f_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_name: If op_name is specified, this value will be compared to the value in name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_name must be specified if op_name is specified.
             :type val_c_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_physical_if_id: The operator to apply to the field physical_if_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. physical_if_id: The scan interface identifier of the physical interface, if this is a sub-interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_physical_if_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_physical_if_id: If op_physical_if_id is specified, the field named in this input will be compared to the value in physical_if_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_physical_if_id must be specified if op_physical_if_id is specified.
             :type val_f_physical_if_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_physical_if_id: If op_physical_if_id is specified, this value will be compared to the value in physical_if_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_physical_if_id must be specified if op_physical_if_id is specified.
             :type val_c_physical_if_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_primary_dns_server: The operator to apply to the field primary_dns_server. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. primary_dns_server: The IP address of the scan interface primary dns server in dotted format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_primary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_primary_dns_server: If op_primary_dns_server is specified, the field named in this input will be compared to the value in primary_dns_server using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_primary_dns_server must be specified if op_primary_dns_server is specified.
             :type val_f_primary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_primary_dns_server: If op_primary_dns_server is specified, this value will be compared to the value in primary_dns_server using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_primary_dns_server must be specified if op_primary_dns_server is specified.
             :type val_c_primary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_search_domains: The operator to apply to the field search_domains. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. search_domains: Search domains for DNS resolving. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_search_domains: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_search_domains: If op_search_domains is specified, the field named in this input will be compared to the value in search_domains using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_search_domains must be specified if op_search_domains is specified.
             :type val_f_search_domains: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_search_domains: If op_search_domains is specified, this value will be compared to the value in search_domains using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_search_domains must be specified if op_search_domains is specified.
             :type val_c_search_domains: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_secondary_dns_server: The operator to apply to the field secondary_dns_server. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. secondary_dns_server: The IP address of the scan interface secondary dns server in dotted format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_secondary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_secondary_dns_server: If op_secondary_dns_server is specified, the field named in this input will be compared to the value in secondary_dns_server using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_secondary_dns_server must be specified if op_secondary_dns_server is specified.
             :type val_f_secondary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_secondary_dns_server: If op_secondary_dns_server is specified, this value will be compared to the value in secondary_dns_server using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_secondary_dns_server must be specified if op_secondary_dns_server is specified.
             :type val_c_secondary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_unit_id: The operator to apply to the field unit_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. unit_id: The internal identifier for the collector on which the scan interface exists. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_unit_id: If op_unit_id is specified, the field named in this input will be compared to the value in unit_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_unit_id must be specified if op_unit_id is specified.
             :type val_f_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_unit_id: If op_unit_id is specified, this value will be compared to the value in unit_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_unit_id must be specified if op_unit_id is specified.
             :type val_c_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_virtual_network_id: The operator to apply to the field virtual_network_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. virtual_network_id: The internal NetMRI identifier of the Virtual Network in which the scan interface is present. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains.
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

             :param select: The list of attributes to return for each ScanInterface. Valid values are id, unit_id, if_dev, name, physical_if_id, encap_tag, ipv4_address, ipv4_mask, ipv4_gateway, ipv6_address, ipv6_prefix, ipv6_gateway, virtual_network_id, primary_dns_server, secondary_dns_server, search_domains. If empty or omitted, all attributes will be returned.
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

             :return scan_interfaces: An array of the ScanInterface objects that match the specified input criteria.
             :rtype scan_interfaces: Array of ScanInterface

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a Virtual Scan Interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the virtual network
             :type virtual_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param physical_if_id: The scan interface identifier of the physical scan interface
             :type physical_if_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param physical_if_name: The name of the physical scan interface
             :type physical_if_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: The unit id of the scan interface
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param encap_tag: The 802.1q tag identifier
             :type encap_tag: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_address: The IP address of the scan interface
             :type ipv4_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_mask: The mask of the scan interface
             :type ipv4_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_gateway: The gateway address of the scan interface
             :type ipv4_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_address: The IPv6 address of the scan interface
             :type ipv6_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_prefix: The IPv6 mask of the scan interface
             :type ipv6_prefix: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_gateway: The IPv6 gateway address of the scan interface
             :type ipv6_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param primary_dns_server: The IP address or hostname of the scan interface's primary DNS server
             :type primary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secondary_dns_server: The IP address or hostname of the scan interface's secondary DNS server
             :type secondary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_domain1: Default domain for DNS resolving.
             :type search_domain1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_domain2: Default domain for DNS resolving.
             :type search_domain2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the scan interface
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param if_dev: The system device name of the scan interface
             :type if_dev: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The unique identifier for Scan Interface initialized
             :rtype id: Integer

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates selected Scan Interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The unique identifier for Scan Interface
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the Scan Interface to update
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: The unit id of the Scan Interface to update
             :type unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier of the virtual network
             :type virtual_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param encap_tag: The vlan tag indentifier
             :type encap_tag: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_address: The IP address of the scan interface
             :type ipv4_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_mask: The mask of the scan interface
             :type ipv4_mask: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv4_gateway: The gateway address of the scan interface
             :type ipv4_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_address: The IPv6 address of the scan interface
             :type ipv6_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_prefix: The IPv6 mask of the scan interface
             :type ipv6_prefix: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ipv6_gateway: The IPv6 gateway address of the scan interface
             :type ipv6_gateway: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param primary_dns_server: The IP address or hostname of the scan interface's primary DNS server
             :type primary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secondary_dns_server: The IP address or hostname of the scan interface's secondary DNS server
             :type secondary_dns_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_domain1: Default domain for DNS resolving.
             :type search_domain1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param host_name: Computer host name.
             :type host_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_domain2: Default domain for DNS resolving.
             :type search_domain2: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return scan_interface: The scan interface has been updated.
             :rtype scan_interface: ScanInterface

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def delete(self, **kwargs):
        """Deletes selected Scan Interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The unique identifier for Scan Interface
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the Scan Interface to delete
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: The unit id of the Scan Interface to delete
             :type unit_id: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)

    def discover_available_interfaces(self, **kwargs):
        """Discover new physical interface, and make them available for configuration

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param unit_id: The collector (probe) id
             :type unit_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discover_available_interfaces"), kwargs)

    def check_network_assignments(self, **kwargs):
        """Detects is there Scan Interfaces assigned to the Network specified

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param virtual_network_id: The unique identifier for Virtual Network
             :type virtual_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param unit_id: The collector (probe) id
             :type unit_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("check_network_assignments"), kwargs)
