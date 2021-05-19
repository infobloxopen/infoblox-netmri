from ..broker import Broker


class DeviceIpRangeBroker(Broker):
    controller = "device_ip_ranges"

    def show(self, **kwargs):
        """Shows the details for the specified device ip range.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device ip range methods. The listed methods will be called on each device ip range returned and included in the output. Available methods are: device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_object, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_ip_range: The device ip range identified by the specified DeviceIPRangeID.
             :rtype device_ip_range: DeviceIpRange

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device ip ranges. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this flow.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for the service to which belongs this flow.
             :type DeviceObjectID: Array of Integer

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

             :param timestamp: The data returned will represent the device ip ranges as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device ip range methods. The listed methods will be called on each device ip range returned and included in the output. Available methods are: device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_object, data_source, device.
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
            |  ``default:`` DeviceIPRangeID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceIPRangeID. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax.
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

             :param select: The list of attributes to return for each DeviceIpRange. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax. If empty or omitted, all attributes will be returned.
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

             :return device_ip_ranges: An array of the DeviceIpRange objects that match the specified input criteria.
             :rtype device_ip_ranges: Array of DeviceIpRange

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device ip ranges matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this flow.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for the service to which belongs this flow.
             :type DeviceObjectID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IprChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprDisplayText: The text that was defined in the configuration for this ip address range.
             :type IprDisplayText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprEndTime: The ending effective time of this record, or empty if still in effect.
             :type IprEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprFirstSeenTime: The timestamp of when NetMRI saw for the first time this flow.
             :type IprFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprIPNumericMax: The numeric value for the range max value.
             :type IprIPNumericMax: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprIPNumericMin: The numeric value for the range min value.
             :type IprIPNumericMin: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprIPVersion: The ip version for this range. 4 or 6.
             :type IprIPVersion: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprStartTime: The starting effective time of this record.
             :type IprStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprTimestamp: The date and time this record was collected or calculated.
             :type IprTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the device ip ranges as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device ip range methods. The listed methods will be called on each device ip range returned and included in the output. Available methods are: device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_object, data_source, device.
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
            |  ``default:`` DeviceIPRangeID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceIPRangeID. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax.
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

             :param select: The list of attributes to return for each DeviceIpRange. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device ip ranges, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DeviceIPRangeID, DeviceObjectID, IprChangedCols, IprDisplayText, IprEndTime, IprFirstSeenTime, IprIPNumericMax, IprIPNumericMin, IprIPVersion, IprStartTime, IprTimestamp.
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

             :return device_ip_ranges: An array of the DeviceIpRange objects that match the specified input criteria.
             :rtype device_ip_ranges: Array of DeviceIpRange

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device ip ranges matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DeviceIPRangeID, DeviceObjectID, IprChangedCols, IprDisplayText, IprEndTime, IprFirstSeenTime, IprIPNumericMax, IprIPNumericMin, IprIPVersion, IprStartTime, IprTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which belongs this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceIPRangeID: The operator to apply to the field DeviceIPRangeID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceIPRangeID: The internal NetMRI identifier for ip address range definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceIPRangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceIPRangeID: If op_DeviceIPRangeID is specified, the field named in this input will be compared to the value in DeviceIPRangeID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceIPRangeID must be specified if op_DeviceIPRangeID is specified.
             :type val_f_DeviceIPRangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceIPRangeID: If op_DeviceIPRangeID is specified, this value will be compared to the value in DeviceIPRangeID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceIPRangeID must be specified if op_DeviceIPRangeID is specified.
             :type val_c_DeviceIPRangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceObjectID: The operator to apply to the field DeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceObjectID: The internal NetMRI identifier for the service to which belongs this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceObjectID: If op_DeviceObjectID is specified, the field named in this input will be compared to the value in DeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceObjectID must be specified if op_DeviceObjectID is specified.
             :type val_f_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceObjectID: If op_DeviceObjectID is specified, this value will be compared to the value in DeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceObjectID must be specified if op_DeviceObjectID is specified.
             :type val_c_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprChangedCols: The operator to apply to the field IprChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprChangedCols: If op_IprChangedCols is specified, the field named in this input will be compared to the value in IprChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprChangedCols must be specified if op_IprChangedCols is specified.
             :type val_f_IprChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprChangedCols: If op_IprChangedCols is specified, this value will be compared to the value in IprChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprChangedCols must be specified if op_IprChangedCols is specified.
             :type val_c_IprChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprDisplayText: The operator to apply to the field IprDisplayText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprDisplayText: The text that was defined in the configuration for this ip address range. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprDisplayText: If op_IprDisplayText is specified, the field named in this input will be compared to the value in IprDisplayText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprDisplayText must be specified if op_IprDisplayText is specified.
             :type val_f_IprDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprDisplayText: If op_IprDisplayText is specified, this value will be compared to the value in IprDisplayText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprDisplayText must be specified if op_IprDisplayText is specified.
             :type val_c_IprDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprEndTime: The operator to apply to the field IprEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprEndTime: If op_IprEndTime is specified, the field named in this input will be compared to the value in IprEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprEndTime must be specified if op_IprEndTime is specified.
             :type val_f_IprEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprEndTime: If op_IprEndTime is specified, this value will be compared to the value in IprEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprEndTime must be specified if op_IprEndTime is specified.
             :type val_c_IprEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprFirstSeenTime: The operator to apply to the field IprFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprFirstSeenTime: The timestamp of when NetMRI saw for the first time this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprFirstSeenTime: If op_IprFirstSeenTime is specified, the field named in this input will be compared to the value in IprFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprFirstSeenTime must be specified if op_IprFirstSeenTime is specified.
             :type val_f_IprFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprFirstSeenTime: If op_IprFirstSeenTime is specified, this value will be compared to the value in IprFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprFirstSeenTime must be specified if op_IprFirstSeenTime is specified.
             :type val_c_IprFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprIPNumericMax: The operator to apply to the field IprIPNumericMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprIPNumericMax: The numeric value for the range max value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprIPNumericMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprIPNumericMax: If op_IprIPNumericMax is specified, the field named in this input will be compared to the value in IprIPNumericMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprIPNumericMax must be specified if op_IprIPNumericMax is specified.
             :type val_f_IprIPNumericMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprIPNumericMax: If op_IprIPNumericMax is specified, this value will be compared to the value in IprIPNumericMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprIPNumericMax must be specified if op_IprIPNumericMax is specified.
             :type val_c_IprIPNumericMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprIPNumericMin: The operator to apply to the field IprIPNumericMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprIPNumericMin: The numeric value for the range min value. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprIPNumericMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprIPNumericMin: If op_IprIPNumericMin is specified, the field named in this input will be compared to the value in IprIPNumericMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprIPNumericMin must be specified if op_IprIPNumericMin is specified.
             :type val_f_IprIPNumericMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprIPNumericMin: If op_IprIPNumericMin is specified, this value will be compared to the value in IprIPNumericMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprIPNumericMin must be specified if op_IprIPNumericMin is specified.
             :type val_c_IprIPNumericMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprIPVersion: The operator to apply to the field IprIPVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprIPVersion: The ip version for this range. 4 or 6. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprIPVersion: If op_IprIPVersion is specified, the field named in this input will be compared to the value in IprIPVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprIPVersion must be specified if op_IprIPVersion is specified.
             :type val_f_IprIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprIPVersion: If op_IprIPVersion is specified, this value will be compared to the value in IprIPVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprIPVersion must be specified if op_IprIPVersion is specified.
             :type val_c_IprIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprStartTime: The operator to apply to the field IprStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprStartTime: If op_IprStartTime is specified, the field named in this input will be compared to the value in IprStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprStartTime must be specified if op_IprStartTime is specified.
             :type val_f_IprStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprStartTime: If op_IprStartTime is specified, this value will be compared to the value in IprStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprStartTime must be specified if op_IprStartTime is specified.
             :type val_c_IprStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprTimestamp: The operator to apply to the field IprTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprTimestamp: If op_IprTimestamp is specified, the field named in this input will be compared to the value in IprTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprTimestamp must be specified if op_IprTimestamp is specified.
             :type val_f_IprTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprTimestamp: If op_IprTimestamp is specified, this value will be compared to the value in IprTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprTimestamp must be specified if op_IprTimestamp is specified.
             :type val_c_IprTimestamp: String

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

             :param timestamp: The data returned will represent the device ip ranges as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device ip range methods. The listed methods will be called on each device ip range returned and included in the output. Available methods are: device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_object, data_source, device.
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
            |  ``default:`` DeviceIPRangeID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceIPRangeID. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax.
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

             :param select: The list of attributes to return for each DeviceIpRange. Valid values are DeviceIPRangeID, DeviceID, DeviceObjectID, DataSourceID, IprFirstSeenTime, IprStartTime, IprEndTime, IprTimestamp, IprChangedCols, IprIPVersion, IprDisplayText, IprIPNumericMin, IprIPNumericMax. If empty or omitted, all attributes will be returned.
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

             :return device_ip_ranges: An array of the DeviceIpRange objects that match the specified input criteria.
             :rtype device_ip_ranges: Array of DeviceIpRange

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device_object(self, **kwargs):
        """the network object to which belongs this ip address range.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : the network object to which belongs this ip address range.
             :rtype : DeviceObject

            """

        return self.api_request(self._get_method_fullname("device_object"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceIPRangeID: The internal NetMRI identifier for ip address range definition.
             :type DeviceIPRangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
