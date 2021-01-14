from ..broker import Broker


class DeviceSupportBundleBroker(Broker):
    controller = "device_support_bundles"

    def index(self, **kwargs):
        """Lists the available device support bundles. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind.
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

             :param select: The list of attributes to return for each DeviceSupportBundle. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind. If empty or omitted, all attributes will be returned.
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

             :return device_support_bundles: An array of the DeviceSupportBundle objects that match the specified input criteria.
             :rtype device_support_bundles: Array of DeviceSupportBundle

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device support bundles matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param author: The author of the Device Support Bundle.
             :type author: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param author: The author of the Device Support Bundle.
             :type author: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param config_ind: A flag indicating if configuration is shown in Device Viewer for devices.
             :type config_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param config_ind: A flag indicating if configuration is shown in Device Viewer for devices.
             :type config_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param cpu_ind: A flag indicating if CPU information is shown in Device Viewer for devices.
             :type cpu_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cpu_ind: A flag indicating if CPU information is shown in Device Viewer for devices.
             :type cpu_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the Device Support Bundle was created.
             :type created_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the Device Support Bundle was created.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: Indicates by whom Device Support Bundle was created.
             :type created_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: Indicates by whom Device Support Bundle was created.
             :type created_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_ind: A flag indicating if the Device Support Bundle is enabled.
             :type enabled_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_ind: A flag indicating if the Device Support Bundle is enabled.
             :type enabled_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param environmental_ind: A flag indicating if environmental information is shown in Device Viewer for devices.
             :type environmental_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param environmental_ind: A flag indicating if environmental information is shown in Device Viewer for devices.
             :type environmental_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param forwarding_ind: A flag indicating if forwarding information is shown in Device Viewer for devices.
             :type forwarding_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param forwarding_ind: A flag indicating if forwarding information is shown in Device Viewer for devices.
             :type forwarding_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param integrated_ind: A flag indicating if the Device Support Bundle is integrated.
             :type integrated_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param integrated_ind: A flag indicating if the Device Support Bundle is integrated.
             :type integrated_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param inventory_ind: A flag indicating if inventory information is shown in Device Viewer for devices.
             :type inventory_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param inventory_ind: A flag indicating if inventory information is shown in Device Viewer for devices.
             :type inventory_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param memory_ind: A flag indicating if memory information is shown in Device Viewer for devices.
             :type memory_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param memory_ind: A flag indicating if memory information is shown in Device Viewer for devices.
             :type memory_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The unique name of the Device Support Bundle.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The unique name of the Device Support Bundle.
             :type name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param neighbor_ind: A flag indicating if neighbor information is shown in Device Viewer for devices.
             :type neighbor_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param neighbor_ind: A flag indicating if neighbor information is shown in Device Viewer for devices.
             :type neighbor_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param port_ind: A flag indicating if port config is shown in Device Viewer for devices.
             :type port_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port_ind: A flag indicating if port config is shown in Device Viewer for devices.
             :type port_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param status: The current editing state of the Device Support Bundle.
             :type status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The current editing state of the Device Support Bundle.
             :type status: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param system_ind: A flag indicating if system information is shown in Device Viewer for devices.
             :type system_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param system_ind: A flag indicating if system information is shown in Device Viewer for devices.
             :type system_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param unit_tests: The current state of unit testing for the Device Support Bundle.
             :type unit_tests: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_tests: The current state of unit testing for the Device Support Bundle.
             :type unit_tests: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the Device Support Bundle was updated.
             :type updated_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the Device Support Bundle was updated.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: Indicates by whom the Device Support Bundle was updated.
             :type updated_by: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: Indicates by whom the Device Support Bundle was updated.
             :type updated_by: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param valid_ind: A flag indicating whether the Device Support Bundle is valid.
             :type valid_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param valid_ind: A flag indicating whether the Device Support Bundle is valid.
             :type valid_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param version: The version of the Device Support Bundle.
             :type version: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param version: The version of the Device Support Bundle.
             :type version: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param vlan_ind: A flag indicating if VLAN information is shown in Device Viewer for devices.
             :type vlan_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param vlan_ind: A flag indicating if VLAN information is shown in Device Viewer for devices.
             :type vlan_ind: Array of Boolean

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind.
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

             :param select: The list of attributes to return for each DeviceSupportBundle. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device support bundles, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: author, config_ind, cpu_ind, created_at, created_by, enabled_ind, environmental_ind, forwarding_ind, id, integrated_ind, inventory_ind, memory_ind, name, neighbor_ind, port_ind, status, system_ind, unit_tests, updated_at, updated_by, valid_ind, version, vlan_ind.
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

             :return device_support_bundles: An array of the DeviceSupportBundle objects that match the specified input criteria.
             :rtype device_support_bundles: Array of DeviceSupportBundle

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device support bundles matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: author, config_ind, cpu_ind, created_at, created_by, enabled_ind, environmental_ind, forwarding_ind, id, integrated_ind, inventory_ind, memory_ind, name, neighbor_ind, port_ind, status, system_ind, unit_tests, updated_at, updated_by, valid_ind, version, vlan_ind.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_author: The operator to apply to the field author. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. author: The author of the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_author: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_author: If op_author is specified, the field named in this input will be compared to the value in author using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_author must be specified if op_author is specified.
             :type val_f_author: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_author: If op_author is specified, this value will be compared to the value in author using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_author must be specified if op_author is specified.
             :type val_c_author: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_config_ind: The operator to apply to the field config_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. config_ind: A flag indicating if configuration is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_config_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_config_ind: If op_config_ind is specified, the field named in this input will be compared to the value in config_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_config_ind must be specified if op_config_ind is specified.
             :type val_f_config_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_config_ind: If op_config_ind is specified, this value will be compared to the value in config_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_config_ind must be specified if op_config_ind is specified.
             :type val_c_config_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cpu_ind: The operator to apply to the field cpu_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cpu_ind: A flag indicating if CPU information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cpu_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cpu_ind: If op_cpu_ind is specified, the field named in this input will be compared to the value in cpu_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cpu_ind must be specified if op_cpu_ind is specified.
             :type val_f_cpu_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cpu_ind: If op_cpu_ind is specified, this value will be compared to the value in cpu_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cpu_ind must be specified if op_cpu_ind is specified.
             :type val_c_cpu_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the Device Support Bundle was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_at: If op_created_at is specified, the field named in this input will be compared to the value in created_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_at must be specified if op_created_at is specified.
             :type val_f_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_at: If op_created_at is specified, this value will be compared to the value in created_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_at must be specified if op_created_at is specified.
             :type val_c_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: Indicates by whom Device Support Bundle was created. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_by: If op_created_by is specified, the field named in this input will be compared to the value in created_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_by must be specified if op_created_by is specified.
             :type val_f_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_by: If op_created_by is specified, this value will be compared to the value in created_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_by must be specified if op_created_by is specified.
             :type val_c_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_enabled_ind: The operator to apply to the field enabled_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. enabled_ind: A flag indicating if the Device Support Bundle is enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_enabled_ind: If op_enabled_ind is specified, the field named in this input will be compared to the value in enabled_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_enabled_ind must be specified if op_enabled_ind is specified.
             :type val_f_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_enabled_ind: If op_enabled_ind is specified, this value will be compared to the value in enabled_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_enabled_ind must be specified if op_enabled_ind is specified.
             :type val_c_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_environmental_ind: The operator to apply to the field environmental_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. environmental_ind: A flag indicating if environmental information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_environmental_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_environmental_ind: If op_environmental_ind is specified, the field named in this input will be compared to the value in environmental_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_environmental_ind must be specified if op_environmental_ind is specified.
             :type val_f_environmental_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_environmental_ind: If op_environmental_ind is specified, this value will be compared to the value in environmental_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_environmental_ind must be specified if op_environmental_ind is specified.
             :type val_c_environmental_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_forwarding_ind: The operator to apply to the field forwarding_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. forwarding_ind: A flag indicating if forwarding information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_forwarding_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_forwarding_ind: If op_forwarding_ind is specified, the field named in this input will be compared to the value in forwarding_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_forwarding_ind must be specified if op_forwarding_ind is specified.
             :type val_f_forwarding_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_forwarding_ind: If op_forwarding_ind is specified, this value will be compared to the value in forwarding_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_forwarding_ind must be specified if op_forwarding_ind is specified.
             :type val_c_forwarding_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier of the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_integrated_ind: The operator to apply to the field integrated_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. integrated_ind: A flag indicating if the Device Support Bundle is integrated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_integrated_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_integrated_ind: If op_integrated_ind is specified, the field named in this input will be compared to the value in integrated_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_integrated_ind must be specified if op_integrated_ind is specified.
             :type val_f_integrated_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_integrated_ind: If op_integrated_ind is specified, this value will be compared to the value in integrated_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_integrated_ind must be specified if op_integrated_ind is specified.
             :type val_c_integrated_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_inventory_ind: The operator to apply to the field inventory_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. inventory_ind: A flag indicating if inventory information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_inventory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_inventory_ind: If op_inventory_ind is specified, the field named in this input will be compared to the value in inventory_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_inventory_ind must be specified if op_inventory_ind is specified.
             :type val_f_inventory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_inventory_ind: If op_inventory_ind is specified, this value will be compared to the value in inventory_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_inventory_ind must be specified if op_inventory_ind is specified.
             :type val_c_inventory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_memory_ind: The operator to apply to the field memory_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. memory_ind: A flag indicating if memory information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_memory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_memory_ind: If op_memory_ind is specified, the field named in this input will be compared to the value in memory_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_memory_ind must be specified if op_memory_ind is specified.
             :type val_f_memory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_memory_ind: If op_memory_ind is specified, this value will be compared to the value in memory_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_memory_ind must be specified if op_memory_ind is specified.
             :type val_c_memory_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The unique name of the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_neighbor_ind: The operator to apply to the field neighbor_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. neighbor_ind: A flag indicating if neighbor information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_neighbor_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_neighbor_ind: If op_neighbor_ind is specified, the field named in this input will be compared to the value in neighbor_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_neighbor_ind must be specified if op_neighbor_ind is specified.
             :type val_f_neighbor_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_neighbor_ind: If op_neighbor_ind is specified, this value will be compared to the value in neighbor_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_neighbor_ind must be specified if op_neighbor_ind is specified.
             :type val_c_neighbor_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_port_ind: The operator to apply to the field port_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. port_ind: A flag indicating if port config is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_port_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_port_ind: If op_port_ind is specified, the field named in this input will be compared to the value in port_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_port_ind must be specified if op_port_ind is specified.
             :type val_f_port_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_port_ind: If op_port_ind is specified, this value will be compared to the value in port_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_port_ind must be specified if op_port_ind is specified.
             :type val_c_port_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The current editing state of the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_status: If op_status is specified, the field named in this input will be compared to the value in status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_status must be specified if op_status is specified.
             :type val_f_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_status: If op_status is specified, this value will be compared to the value in status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_status must be specified if op_status is specified.
             :type val_c_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_system_ind: The operator to apply to the field system_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. system_ind: A flag indicating if system information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_system_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_system_ind: If op_system_ind is specified, the field named in this input will be compared to the value in system_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_system_ind must be specified if op_system_ind is specified.
             :type val_f_system_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_system_ind: If op_system_ind is specified, this value will be compared to the value in system_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_system_ind must be specified if op_system_ind is specified.
             :type val_c_system_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_unit_tests: The operator to apply to the field unit_tests. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. unit_tests: The current state of unit testing for the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_unit_tests: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_unit_tests: If op_unit_tests is specified, the field named in this input will be compared to the value in unit_tests using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_unit_tests must be specified if op_unit_tests is specified.
             :type val_f_unit_tests: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_unit_tests: If op_unit_tests is specified, this value will be compared to the value in unit_tests using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_unit_tests must be specified if op_unit_tests is specified.
             :type val_c_unit_tests: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the Device Support Bundle was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_at: If op_updated_at is specified, the field named in this input will be compared to the value in updated_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_at must be specified if op_updated_at is specified.
             :type val_f_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_at: If op_updated_at is specified, this value will be compared to the value in updated_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_at must be specified if op_updated_at is specified.
             :type val_c_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_by: The operator to apply to the field updated_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_by: Indicates by whom the Device Support Bundle was updated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_by: If op_updated_by is specified, the field named in this input will be compared to the value in updated_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_by must be specified if op_updated_by is specified.
             :type val_f_updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_by: If op_updated_by is specified, this value will be compared to the value in updated_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_by must be specified if op_updated_by is specified.
             :type val_c_updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_valid_ind: The operator to apply to the field valid_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. valid_ind: A flag indicating whether the Device Support Bundle is valid. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_valid_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_valid_ind: If op_valid_ind is specified, the field named in this input will be compared to the value in valid_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_valid_ind must be specified if op_valid_ind is specified.
             :type val_f_valid_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_valid_ind: If op_valid_ind is specified, this value will be compared to the value in valid_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_valid_ind must be specified if op_valid_ind is specified.
             :type val_c_valid_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_version: The operator to apply to the field version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. version: The version of the Device Support Bundle. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_version: If op_version is specified, the field named in this input will be compared to the value in version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_version must be specified if op_version is specified.
             :type val_f_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_version: If op_version is specified, this value will be compared to the value in version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_version must be specified if op_version is specified.
             :type val_c_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_vlan_ind: The operator to apply to the field vlan_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. vlan_ind: A flag indicating if VLAN information is shown in Device Viewer for devices. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_vlan_ind: If op_vlan_ind is specified, the field named in this input will be compared to the value in vlan_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_vlan_ind must be specified if op_vlan_ind is specified.
             :type val_f_vlan_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_vlan_ind: If op_vlan_ind is specified, this value will be compared to the value in vlan_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_vlan_ind must be specified if op_vlan_ind is specified.
             :type val_c_vlan_ind: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind.
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

             :param select: The list of attributes to return for each DeviceSupportBundle. Valid values are id, name, version, author, enabled_ind, system_ind, neighbor_ind, inventory_ind, environmental_ind, cpu_ind, memory_ind, vlan_ind, forwarding_ind, port_ind, config_ind, created_by, updated_by, created_at, updated_at, valid_ind, unit_tests, status, integrated_ind. If empty or omitted, all attributes will be returned.
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

             :return device_support_bundles: An array of the DeviceSupportBundle objects that match the specified input criteria.
             :rtype device_support_bundles: Array of DeviceSupportBundle

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified device support bundle from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the Device Support Bundle.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def delete(self, **kwargs):
        """Delete a device support bundle specified by name

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the delete output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)

    def export(self, **kwargs):
        """Export specified device support bundle in tgz format.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: Unique Device Support Bundle name indicating the bundle to export
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("export"), kwargs)

    def import_data(self, **kwargs):
        """Import Device Support Bundles in bulk via a xml, tgz, tar, or zip file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param file: Device Support Bundle file contents to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the import output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def discard(self, **kwargs):
        """Discard all changes to the modified Device Support Bundle

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: Name of the DSB for which changes should be discarded
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("discard"), kwargs)

    def generate_templates(self, **kwargs):
        """Return DSB file templates

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: The unique name of the new DSB (it will be inserted into template files where necessary)
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param type: The type of the DSB template
             :type type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("generate_templates"), kwargs)

    def show(self, **kwargs):
        """Return all existing files for a DSB

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def validate(self, **kwargs):
        """Validate DSB files

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: DSB config description content
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ccs_scripts: DSB Perl scripts content
             :type ccs_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param perl_scripts: DSB CCS scripts content
             :type perl_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("validate"), kwargs)

    def save(self, **kwargs):
        """Save DSB scripts to working directory

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description: DSB config description content
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ccs_scripts: DSB Perl scripts content
             :type ccs_scripts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param perl_scripts: DSB CCS scripts content
             :type perl_scripts: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("save"), kwargs)

    def install(self, **kwargs):
        """Install a saved, validated DSB script

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: DSB name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("install"), kwargs)

    def test_bundle(self, **kwargs):
        """Test DSB in real-time

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ip: Device IP to test the DSB against
             :type device_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the test output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("test_bundle"), kwargs)

    def validate_bundle(self, **kwargs):
        """Validate DSB

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param dsb_name: Unique device support bundle name
             :type dsb_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes already read from the validation output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("validate_bundle"), kwargs)
