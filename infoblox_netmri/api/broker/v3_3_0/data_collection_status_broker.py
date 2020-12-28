from ..broker import Broker


class DataCollectionStatusBroker(Broker):
    controller = "data_collection_statuses"

    def index(self, **kwargs):
        """Lists the available data collection statuses. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device on which collection applied.
             :type DeviceID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data collection status methods. The listed methods will be called on each data collection status returned and included in the output. Available methods are: system, cpu, memory, vlans, forwarding, environmental, inventory, arp, route, neighbor, config, access, vrf, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp.
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

             :param select: The list of attributes to return for each DataCollectionStatus. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp. If empty or omitted, all attributes will be returned.
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

             :return data_collection_statuses: An array of the DataCollectionStatus objects that match the specified input criteria.
             :rtype data_collection_statuses: Array of DataCollectionStatus

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified data collection status.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device on which collection applied.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data collection status methods. The listed methods will be called on each data collection status returned and included in the output. Available methods are: system, cpu, memory, vlans, forwarding, environmental, inventory, arp, route, neighbor, config, access, vrf, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return data_collection_status: The data collection status identified by the specified DeviceID.
             :rtype data_collection_status: DataCollectionStatus

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available data collection statuses matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ARPInd: The indicator of collection of the arp information.
             :type ARPInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ARPTimestamp: The date and time of last collect of the arp information.
             :type ARPTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessInd: The indicator of collection of the filtering access information.
             :type AccessInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessTimestamp: The date and time of last collect of the filtering access information.
             :type AccessTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CPUInd: The indicator of collection of cpu information.
             :type CPUInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CPUTimestamp: The date and time of last collect of the cpu information.
             :type CPUTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigInd: The indicator of collection of the configuration information.
             :type ConfigInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigTimestamp: The date and time of last collect of the configuration information.
             :type ConfigTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device on which collection applied.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EnvironmentalInd: The indicator of collection of environmental information.
             :type EnvironmentalInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EnvironmentalTimestamp: The date and time of last collect of the environmental information.
             :type EnvironmentalTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ForwardingInd: The indicator of collection of forwarding information.
             :type ForwardingInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ForwardingTimestamp: The date and time of last collect of the forwarding information.
             :type ForwardingTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InventoryInd: The indicator of collection of the inventory information.
             :type InventoryInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InventoryTimestamp: The date and time of last collect of the inventory information.
             :type InventoryTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemoryInd: The indicator of collection of memory information.
             :type MemoryInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemoryTimestamp: The date and time of last collect of the memory information.
             :type MemoryTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborInd: The indicator of collection of the neighborhood information.
             :type NeighborInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NeighborTimestamp: The date and time of last collect of the neighborhood information.
             :type NeighborTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteInd: The indicator of collection of the route information.
             :type RouteInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param RouteTimestamp: The date and time of last collect of the route information.
             :type RouteTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemInd: The indicator of collection of system information.
             :type SystemInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemTimestamp: The date and time of last collect of the system information.
             :type SystemTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlansInd: The indicator of collection of virtual LAN information.
             :type VlansInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlansTimestamp: The date and time of last collect of the virtual LAN information.
             :type VlansTimestamp: Array of DateTime

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfInd: The indicator of collection of virtual network information.
             :type VrfInd: Array of String

            |  ``api version min:`` 2.7
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VrfTimestamp: The date and time of last collect of the virtual network information.
             :type VrfTimestamp: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data collection status methods. The listed methods will be called on each data collection status returned and included in the output. Available methods are: system, cpu, memory, vlans, forwarding, environmental, inventory, arp, route, neighbor, config, access, vrf, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp.
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

             :param select: The list of attributes to return for each DataCollectionStatus. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against data collection statuses, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ARPInd, ARPTimestamp, AccessInd, AccessTimestamp, CPUInd, CPUTimestamp, ConfigInd, ConfigTimestamp, DeviceID, EnvironmentalInd, EnvironmentalTimestamp, ForwardingInd, ForwardingTimestamp, InventoryInd, InventoryTimestamp, MemoryInd, MemoryTimestamp, NeighborInd, NeighborTimestamp, RouteInd, RouteTimestamp, SystemInd, SystemTimestamp, VlansInd, VlansTimestamp, VrfInd, VrfTimestamp.
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

             :return data_collection_statuses: An array of the DataCollectionStatus objects that match the specified input criteria.
             :rtype data_collection_statuses: Array of DataCollectionStatus

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available data collection statuses matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ARPInd, ARPTimestamp, AccessInd, AccessTimestamp, CPUInd, CPUTimestamp, ConfigInd, ConfigTimestamp, DeviceID, EnvironmentalInd, EnvironmentalTimestamp, ForwardingInd, ForwardingTimestamp, InventoryInd, InventoryTimestamp, MemoryInd, MemoryTimestamp, NeighborInd, NeighborTimestamp, RouteInd, RouteTimestamp, SystemInd, SystemTimestamp, VlansInd, VlansTimestamp, VrfInd, VrfTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ARPInd: The operator to apply to the field ARPInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ARPInd: The indicator of collection of the arp information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ARPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ARPInd: If op_ARPInd is specified, the field named in this input will be compared to the value in ARPInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ARPInd must be specified if op_ARPInd is specified.
             :type val_f_ARPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ARPInd: If op_ARPInd is specified, this value will be compared to the value in ARPInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ARPInd must be specified if op_ARPInd is specified.
             :type val_c_ARPInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ARPTimestamp: The operator to apply to the field ARPTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ARPTimestamp: The date and time of last collect of the arp information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ARPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ARPTimestamp: If op_ARPTimestamp is specified, the field named in this input will be compared to the value in ARPTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ARPTimestamp must be specified if op_ARPTimestamp is specified.
             :type val_f_ARPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ARPTimestamp: If op_ARPTimestamp is specified, this value will be compared to the value in ARPTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ARPTimestamp must be specified if op_ARPTimestamp is specified.
             :type val_c_ARPTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AccessInd: The operator to apply to the field AccessInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AccessInd: The indicator of collection of the filtering access information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AccessInd: If op_AccessInd is specified, the field named in this input will be compared to the value in AccessInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AccessInd must be specified if op_AccessInd is specified.
             :type val_f_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AccessInd: If op_AccessInd is specified, this value will be compared to the value in AccessInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AccessInd must be specified if op_AccessInd is specified.
             :type val_c_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AccessTimestamp: The operator to apply to the field AccessTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AccessTimestamp: The date and time of last collect of the filtering access information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AccessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AccessTimestamp: If op_AccessTimestamp is specified, the field named in this input will be compared to the value in AccessTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AccessTimestamp must be specified if op_AccessTimestamp is specified.
             :type val_f_AccessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AccessTimestamp: If op_AccessTimestamp is specified, this value will be compared to the value in AccessTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AccessTimestamp must be specified if op_AccessTimestamp is specified.
             :type val_c_AccessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CPUInd: The operator to apply to the field CPUInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CPUInd: The indicator of collection of cpu information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CPUInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CPUInd: If op_CPUInd is specified, the field named in this input will be compared to the value in CPUInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CPUInd must be specified if op_CPUInd is specified.
             :type val_f_CPUInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CPUInd: If op_CPUInd is specified, this value will be compared to the value in CPUInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CPUInd must be specified if op_CPUInd is specified.
             :type val_c_CPUInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CPUTimestamp: The operator to apply to the field CPUTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CPUTimestamp: The date and time of last collect of the cpu information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CPUTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CPUTimestamp: If op_CPUTimestamp is specified, the field named in this input will be compared to the value in CPUTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CPUTimestamp must be specified if op_CPUTimestamp is specified.
             :type val_f_CPUTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CPUTimestamp: If op_CPUTimestamp is specified, this value will be compared to the value in CPUTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CPUTimestamp must be specified if op_CPUTimestamp is specified.
             :type val_c_CPUTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigInd: The operator to apply to the field ConfigInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigInd: The indicator of collection of the configuration information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigInd: If op_ConfigInd is specified, the field named in this input will be compared to the value in ConfigInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigInd must be specified if op_ConfigInd is specified.
             :type val_f_ConfigInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigInd: If op_ConfigInd is specified, this value will be compared to the value in ConfigInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigInd must be specified if op_ConfigInd is specified.
             :type val_c_ConfigInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigTimestamp: The operator to apply to the field ConfigTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigTimestamp: The date and time of last collect of the configuration information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigTimestamp: If op_ConfigTimestamp is specified, the field named in this input will be compared to the value in ConfigTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigTimestamp must be specified if op_ConfigTimestamp is specified.
             :type val_f_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigTimestamp: If op_ConfigTimestamp is specified, this value will be compared to the value in ConfigTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigTimestamp must be specified if op_ConfigTimestamp is specified.
             :type val_c_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device on which collection applied. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_EnvironmentalInd: The operator to apply to the field EnvironmentalInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EnvironmentalInd: The indicator of collection of environmental information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EnvironmentalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EnvironmentalInd: If op_EnvironmentalInd is specified, the field named in this input will be compared to the value in EnvironmentalInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EnvironmentalInd must be specified if op_EnvironmentalInd is specified.
             :type val_f_EnvironmentalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EnvironmentalInd: If op_EnvironmentalInd is specified, this value will be compared to the value in EnvironmentalInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EnvironmentalInd must be specified if op_EnvironmentalInd is specified.
             :type val_c_EnvironmentalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EnvironmentalTimestamp: The operator to apply to the field EnvironmentalTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EnvironmentalTimestamp: The date and time of last collect of the environmental information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EnvironmentalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EnvironmentalTimestamp: If op_EnvironmentalTimestamp is specified, the field named in this input will be compared to the value in EnvironmentalTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EnvironmentalTimestamp must be specified if op_EnvironmentalTimestamp is specified.
             :type val_f_EnvironmentalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EnvironmentalTimestamp: If op_EnvironmentalTimestamp is specified, this value will be compared to the value in EnvironmentalTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EnvironmentalTimestamp must be specified if op_EnvironmentalTimestamp is specified.
             :type val_c_EnvironmentalTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ForwardingInd: The operator to apply to the field ForwardingInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ForwardingInd: The indicator of collection of forwarding information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ForwardingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ForwardingInd: If op_ForwardingInd is specified, the field named in this input will be compared to the value in ForwardingInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ForwardingInd must be specified if op_ForwardingInd is specified.
             :type val_f_ForwardingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ForwardingInd: If op_ForwardingInd is specified, this value will be compared to the value in ForwardingInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ForwardingInd must be specified if op_ForwardingInd is specified.
             :type val_c_ForwardingInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ForwardingTimestamp: The operator to apply to the field ForwardingTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ForwardingTimestamp: The date and time of last collect of the forwarding information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ForwardingTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ForwardingTimestamp: If op_ForwardingTimestamp is specified, the field named in this input will be compared to the value in ForwardingTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ForwardingTimestamp must be specified if op_ForwardingTimestamp is specified.
             :type val_f_ForwardingTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ForwardingTimestamp: If op_ForwardingTimestamp is specified, this value will be compared to the value in ForwardingTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ForwardingTimestamp must be specified if op_ForwardingTimestamp is specified.
             :type val_c_ForwardingTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InventoryInd: The operator to apply to the field InventoryInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InventoryInd: The indicator of collection of the inventory information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InventoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InventoryInd: If op_InventoryInd is specified, the field named in this input will be compared to the value in InventoryInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InventoryInd must be specified if op_InventoryInd is specified.
             :type val_f_InventoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InventoryInd: If op_InventoryInd is specified, this value will be compared to the value in InventoryInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InventoryInd must be specified if op_InventoryInd is specified.
             :type val_c_InventoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InventoryTimestamp: The operator to apply to the field InventoryTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InventoryTimestamp: The date and time of last collect of the inventory information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InventoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InventoryTimestamp: If op_InventoryTimestamp is specified, the field named in this input will be compared to the value in InventoryTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InventoryTimestamp must be specified if op_InventoryTimestamp is specified.
             :type val_f_InventoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InventoryTimestamp: If op_InventoryTimestamp is specified, this value will be compared to the value in InventoryTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InventoryTimestamp must be specified if op_InventoryTimestamp is specified.
             :type val_c_InventoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemoryInd: The operator to apply to the field MemoryInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemoryInd: The indicator of collection of memory information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemoryInd: If op_MemoryInd is specified, the field named in this input will be compared to the value in MemoryInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemoryInd must be specified if op_MemoryInd is specified.
             :type val_f_MemoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemoryInd: If op_MemoryInd is specified, this value will be compared to the value in MemoryInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemoryInd must be specified if op_MemoryInd is specified.
             :type val_c_MemoryInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemoryTimestamp: The operator to apply to the field MemoryTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemoryTimestamp: The date and time of last collect of the memory information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemoryTimestamp: If op_MemoryTimestamp is specified, the field named in this input will be compared to the value in MemoryTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemoryTimestamp must be specified if op_MemoryTimestamp is specified.
             :type val_f_MemoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemoryTimestamp: If op_MemoryTimestamp is specified, this value will be compared to the value in MemoryTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemoryTimestamp must be specified if op_MemoryTimestamp is specified.
             :type val_c_MemoryTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborInd: The operator to apply to the field NeighborInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborInd: The indicator of collection of the neighborhood information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborInd: If op_NeighborInd is specified, the field named in this input will be compared to the value in NeighborInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborInd must be specified if op_NeighborInd is specified.
             :type val_f_NeighborInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborInd: If op_NeighborInd is specified, this value will be compared to the value in NeighborInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborInd must be specified if op_NeighborInd is specified.
             :type val_c_NeighborInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NeighborTimestamp: The operator to apply to the field NeighborTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NeighborTimestamp: The date and time of last collect of the neighborhood information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NeighborTimestamp: If op_NeighborTimestamp is specified, the field named in this input will be compared to the value in NeighborTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NeighborTimestamp must be specified if op_NeighborTimestamp is specified.
             :type val_f_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NeighborTimestamp: If op_NeighborTimestamp is specified, this value will be compared to the value in NeighborTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NeighborTimestamp must be specified if op_NeighborTimestamp is specified.
             :type val_c_NeighborTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteInd: The operator to apply to the field RouteInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteInd: The indicator of collection of the route information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_RouteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_RouteInd: If op_RouteInd is specified, the field named in this input will be compared to the value in RouteInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_RouteInd must be specified if op_RouteInd is specified.
             :type val_f_RouteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_RouteInd: If op_RouteInd is specified, this value will be compared to the value in RouteInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_RouteInd must be specified if op_RouteInd is specified.
             :type val_c_RouteInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_RouteTimestamp: The operator to apply to the field RouteTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. RouteTimestamp: The date and time of last collect of the route information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SystemInd: The operator to apply to the field SystemInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SystemInd: The indicator of collection of system information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SystemInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SystemInd: If op_SystemInd is specified, the field named in this input will be compared to the value in SystemInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SystemInd must be specified if op_SystemInd is specified.
             :type val_f_SystemInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SystemInd: If op_SystemInd is specified, this value will be compared to the value in SystemInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SystemInd must be specified if op_SystemInd is specified.
             :type val_c_SystemInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SystemTimestamp: The operator to apply to the field SystemTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SystemTimestamp: The date and time of last collect of the system information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SystemTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SystemTimestamp: If op_SystemTimestamp is specified, the field named in this input will be compared to the value in SystemTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SystemTimestamp must be specified if op_SystemTimestamp is specified.
             :type val_f_SystemTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SystemTimestamp: If op_SystemTimestamp is specified, this value will be compared to the value in SystemTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SystemTimestamp must be specified if op_SystemTimestamp is specified.
             :type val_c_SystemTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlansInd: The operator to apply to the field VlansInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlansInd: The indicator of collection of virtual LAN information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlansInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlansInd: If op_VlansInd is specified, the field named in this input will be compared to the value in VlansInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlansInd must be specified if op_VlansInd is specified.
             :type val_f_VlansInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlansInd: If op_VlansInd is specified, this value will be compared to the value in VlansInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlansInd must be specified if op_VlansInd is specified.
             :type val_c_VlansInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlansTimestamp: The operator to apply to the field VlansTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlansTimestamp: The date and time of last collect of the virtual LAN information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlansTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlansTimestamp: If op_VlansTimestamp is specified, the field named in this input will be compared to the value in VlansTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlansTimestamp must be specified if op_VlansTimestamp is specified.
             :type val_f_VlansTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlansTimestamp: If op_VlansTimestamp is specified, this value will be compared to the value in VlansTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlansTimestamp must be specified if op_VlansTimestamp is specified.
             :type val_c_VlansTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfInd: The operator to apply to the field VrfInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfInd: The indicator of collection of virtual network information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfInd: If op_VrfInd is specified, the field named in this input will be compared to the value in VrfInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfInd must be specified if op_VrfInd is specified.
             :type val_f_VrfInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfInd: If op_VrfInd is specified, this value will be compared to the value in VrfInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfInd must be specified if op_VrfInd is specified.
             :type val_c_VrfInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VrfTimestamp: The operator to apply to the field VrfTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VrfTimestamp: The date and time of last collect of the virtual network information. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VrfTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VrfTimestamp: If op_VrfTimestamp is specified, the field named in this input will be compared to the value in VrfTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VrfTimestamp must be specified if op_VrfTimestamp is specified.
             :type val_f_VrfTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VrfTimestamp: If op_VrfTimestamp is specified, this value will be compared to the value in VrfTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VrfTimestamp must be specified if op_VrfTimestamp is specified.
             :type val_c_VrfTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data collection status methods. The listed methods will be called on each data collection status returned and included in the output. Available methods are: system, cpu, memory, vlans, forwarding, environmental, inventory, arp, route, neighbor, config, access, vrf, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp.
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

             :param select: The list of attributes to return for each DataCollectionStatus. Valid values are DeviceID, SystemInd, CPUInd, MemoryInd, VlansInd, ForwardingInd, EnvironmentalInd, InventoryInd, ARPInd, RouteInd, NeighborInd, ConfigInd, AccessInd, VrfInd, SystemTimestamp, CPUTimestamp, MemoryTimestamp, VlansTimestamp, ForwardingTimestamp, EnvironmentalTimestamp, InventoryTimestamp, ARPTimestamp, RouteTimestamp, NeighborTimestamp, ConfigTimestamp, AccessTimestamp, VrfTimestamp. If empty or omitted, all attributes will be returned.
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

             :return data_collection_statuses: An array of the DataCollectionStatus objects that match the specified input criteria.
             :rtype data_collection_statuses: Array of DataCollectionStatus

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
