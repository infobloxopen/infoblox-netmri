from ..broker import Broker


class ExcludedDeviceBroker(Broker):
    controller = "excluded_devices"

    def index(self, **kwargs):
        """Lists the available excluded devices. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ExclusionID: The internal NetMRI identifier for this banned device definition.
             :type ExclusionID: Array of Integer

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LastUpdate: The date and time the banned device was added to the exclusion list.
             :type LastUpdate: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPEngineID: The unique identifier of the banned device.
             :type SNMPEngineID: Array of String

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
            |  ``default:`` ExclusionID

             :param sort: The data field(s) to use for sorting the output. Default is ExclusionID. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName.
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

             :param select: The list of attributes to return for each ExcludedDevice. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName. If empty or omitted, all attributes will be returned.
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

             :return excluded_devices: An array of the ExcludedDevice objects that match the specified input criteria.
             :rtype excluded_devices: Array of ExcludedDevice

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available excluded devices matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ExclusionID: The internal NetMRI identifier for this banned device definition.
             :type ExclusionID: Array of Integer

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPAddress: The IP address of the banned device.
             :type IPAddress: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LastUpdate: The date and time the banned device was added to the exclusion list.
             :type LastUpdate: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPEngineID: The unique identifier of the banned device.
             :type SNMPEngineID: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the collector on which the device is banned.
             :type UnitID: Array of Integer

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VirtualNetworkName: The name of the Network View.
             :type VirtualNetworkName: Array of String

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
            |  ``default:`` ExclusionID

             :param sort: The data field(s) to use for sorting the output. Default is ExclusionID. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName.
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

             :param select: The list of attributes to return for each ExcludedDevice. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against excluded devices, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: SNMPEngineID, IPAddress, LastUpdate.
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

             :return excluded_devices: An array of the ExcludedDevice objects that match the specified input criteria.
             :rtype excluded_devices: Array of ExcludedDevice

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available excluded devices matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ExclusionID, IPAddress, LastUpdate, SNMPEngineID, UnitID, VirtualNetworkName.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ExclusionID: The operator to apply to the field ExclusionID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ExclusionID: The internal NetMRI identifier for this banned device definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ExclusionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ExclusionID: If op_ExclusionID is specified, the field named in this input will be compared to the value in ExclusionID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ExclusionID must be specified if op_ExclusionID is specified.
             :type val_f_ExclusionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ExclusionID: If op_ExclusionID is specified, this value will be compared to the value in ExclusionID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ExclusionID must be specified if op_ExclusionID is specified.
             :type val_c_ExclusionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPAddress: The operator to apply to the field IPAddress. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPAddress: The IP address of the banned device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPAddress: If op_IPAddress is specified, the field named in this input will be compared to the value in IPAddress using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPAddress must be specified if op_IPAddress is specified.
             :type val_f_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPAddress: If op_IPAddress is specified, this value will be compared to the value in IPAddress using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPAddress must be specified if op_IPAddress is specified.
             :type val_c_IPAddress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_LastUpdate: The operator to apply to the field LastUpdate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LastUpdate: The date and time the banned device was added to the exclusion list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LastUpdate: If op_LastUpdate is specified, the field named in this input will be compared to the value in LastUpdate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LastUpdate must be specified if op_LastUpdate is specified.
             :type val_f_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LastUpdate: If op_LastUpdate is specified, this value will be compared to the value in LastUpdate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LastUpdate must be specified if op_LastUpdate is specified.
             :type val_c_LastUpdate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPEngineID: The operator to apply to the field SNMPEngineID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPEngineID: The unique identifier of the banned device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPEngineID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPEngineID: If op_SNMPEngineID is specified, the field named in this input will be compared to the value in SNMPEngineID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPEngineID must be specified if op_SNMPEngineID is specified.
             :type val_f_SNMPEngineID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPEngineID: If op_SNMPEngineID is specified, this value will be compared to the value in SNMPEngineID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPEngineID must be specified if op_SNMPEngineID is specified.
             :type val_c_SNMPEngineID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier for the collector on which the device is banned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UnitID: If op_UnitID is specified, the field named in this input will be compared to the value in UnitID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UnitID must be specified if op_UnitID is specified.
             :type val_f_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UnitID: If op_UnitID is specified, this value will be compared to the value in UnitID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UnitID must be specified if op_UnitID is specified.
             :type val_c_UnitID: String

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

             :param val_c_VirtualNetworkName: If op_VirtualNetworkName is specified, this value will be compared to the value in VirtualNetworkName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VirtualNetworkName must be specified if op_VirtualNetworkName is specified.
             :type val_c_VirtualNetworkName: String

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
            |  ``default:`` ExclusionID

             :param sort: The data field(s) to use for sorting the output. Default is ExclusionID. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName.
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

             :param select: The list of attributes to return for each ExcludedDevice. Valid values are ExclusionID, SNMPEngineID, IPAddress, UnitID, LastUpdate, VirtualNetworkName. If empty or omitted, all attributes will be returned.
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

             :return excluded_devices: An array of the ExcludedDevice objects that match the specified input criteria.
             :rtype excluded_devices: Array of ExcludedDevice

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified excluded device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ExclusionID: The internal NetMRI identifier for this banned device definition.
             :type ExclusionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return excluded_device: The excluded device identified by the specified ExclusionID.
             :rtype excluded_device: ExcludedDevice

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def destroy_many(self, **kwargs):
        """Remove several excluded devices

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ids: The IDs array of the excluded devices to delete. When sending form encoded use ids[].
             :type ids: Array

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy_many"), kwargs)
