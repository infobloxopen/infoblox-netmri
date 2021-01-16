from ..broker import Broker


class DeviceFilterBroker(Broker):
    controller = "device_filters"

    def show(self, **kwargs):
        """Shows the details for the specified device filter.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter methods. The listed methods will be called on each device filter returned and included in the output. Available methods are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_filter: The device filter identified by the specified DeviceFilterID.
             :rtype device_filter: DeviceFilter

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device filters. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this rule belongs.
             :type DeviceID: Array of Integer

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

             :param timestamp: The data returned will represent the device filters as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter methods. The listed methods will be called on each device filter returned and included in the output. Available methods are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
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
            |  ``default:`` DeviceFilterID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterID. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilter. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_filters: An array of the DeviceFilter objects that match the specified input criteria.
             :rtype device_filters: Array of DeviceFilter

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device filters matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DestDeviceObjectID: The internal NetMRI identifier for the destination network object.
             :type DestDeviceObjectID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFilterSetID: The internal NetMRI identifier for the  rule to which this rule belongs.
             :type DeviceFilterSetID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this rule belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the service (ports, protocol).
             :type DeviceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltAllowInd: A flag indicator for allowance of rule.
             :type FltAllowInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltArtificialInd: A flag indicating that this rule has no counterpart in the device configuration.
             :type FltArtificialInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type FltChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltConfigText: The original text of the configuration from witch this rule is built.
             :type FltConfigText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltEnabledInd: A flag indicating whether this rule is enabled in the configuration or not.
             :type FltEnabledInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltEndTime: The ending effective time of this record, or empty if still in effect.
             :type FltEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltEstablishedInd: A flag indicating whether this rule has the option 'established' (cisco specific).
             :type FltEstablishedInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltFirstSeenTime: The timestamp of when NetMRI first discovered this rule.
             :type FltFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltKey: The computed key value that identifies this rule against text configuration.
             :type FltKey: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltOrder: The numerical order of this rule in its rule list.
             :type FltOrder: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltProvisionData: Internal data - do not modify, may change without warning.
             :type FltProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltRelevantInd: A flag indicating whether this rule is relevant for search operations.
             :type FltRelevantInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltStartTime: The starting effective time of this record.
             :type FltStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltTimestamp: The date and time this record was collected or calculated.
             :type FltTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SrcDeviceObjectID: The internal NetMRI identifier for the source network object.
             :type SrcDeviceObjectID: Array of Integer

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

             :param timestamp: The data returned will represent the device filters as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter methods. The listed methods will be called on each device filter returned and included in the output. Available methods are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
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
            |  ``default:`` DeviceFilterID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterID. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilter. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device filters, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DestDeviceObjectID, DeviceFilterID, DeviceFilterSetID, DeviceID, DeviceServiceID, FltAllowInd, FltArtificialInd, FltChangedCols, FltConfigText, FltEnabledInd, FltEndTime, FltEstablishedInd, FltFirstSeenTime, FltKey, FltOrder, FltProvisionData, FltRelevantInd, FltStartTime, FltTimestamp, SrcDeviceObjectID.
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

             :return device_filters: An array of the DeviceFilter objects that match the specified input criteria.
             :rtype device_filters: Array of DeviceFilter

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device filters matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DestDeviceObjectID, DeviceFilterID, DeviceFilterSetID, DeviceID, DeviceServiceID, FltAllowInd, FltArtificialInd, FltChangedCols, FltConfigText, FltEnabledInd, FltEndTime, FltEstablishedInd, FltFirstSeenTime, FltKey, FltOrder, FltProvisionData, FltRelevantInd, FltStartTime, FltTimestamp, SrcDeviceObjectID.

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

             :param op_DestDeviceObjectID: The operator to apply to the field DestDeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DestDeviceObjectID: The internal NetMRI identifier for the destination network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DestDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DestDeviceObjectID: If op_DestDeviceObjectID is specified, the field named in this input will be compared to the value in DestDeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DestDeviceObjectID must be specified if op_DestDeviceObjectID is specified.
             :type val_f_DestDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DestDeviceObjectID: If op_DestDeviceObjectID is specified, this value will be compared to the value in DestDeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DestDeviceObjectID must be specified if op_DestDeviceObjectID is specified.
             :type val_c_DestDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFilterID: The operator to apply to the field DeviceFilterID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFilterID: The internal NetMRI identifier for the rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFilterID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFilterID: If op_DeviceFilterID is specified, the field named in this input will be compared to the value in DeviceFilterID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFilterID must be specified if op_DeviceFilterID is specified.
             :type val_f_DeviceFilterID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFilterID: If op_DeviceFilterID is specified, this value will be compared to the value in DeviceFilterID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFilterID must be specified if op_DeviceFilterID is specified.
             :type val_c_DeviceFilterID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFilterSetID: The operator to apply to the field DeviceFilterSetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFilterSetID: The internal NetMRI identifier for the  rule to which this rule belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFilterSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFilterSetID: If op_DeviceFilterSetID is specified, the field named in this input will be compared to the value in DeviceFilterSetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFilterSetID must be specified if op_DeviceFilterSetID is specified.
             :type val_f_DeviceFilterSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFilterSetID: If op_DeviceFilterSetID is specified, this value will be compared to the value in DeviceFilterSetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFilterSetID must be specified if op_DeviceFilterSetID is specified.
             :type val_c_DeviceFilterSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which this rule belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceServiceID: The operator to apply to the field DeviceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceServiceID: The internal NetMRI identifier for the service (ports, protocol). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceServiceID: If op_DeviceServiceID is specified, the field named in this input will be compared to the value in DeviceServiceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceServiceID must be specified if op_DeviceServiceID is specified.
             :type val_f_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceServiceID: If op_DeviceServiceID is specified, this value will be compared to the value in DeviceServiceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceServiceID must be specified if op_DeviceServiceID is specified.
             :type val_c_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltAllowInd: The operator to apply to the field FltAllowInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltAllowInd: A flag indicator for allowance of rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltAllowInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltAllowInd: If op_FltAllowInd is specified, the field named in this input will be compared to the value in FltAllowInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltAllowInd must be specified if op_FltAllowInd is specified.
             :type val_f_FltAllowInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltAllowInd: If op_FltAllowInd is specified, this value will be compared to the value in FltAllowInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltAllowInd must be specified if op_FltAllowInd is specified.
             :type val_c_FltAllowInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltArtificialInd: The operator to apply to the field FltArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltArtificialInd: A flag indicating that this rule has no counterpart in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltArtificialInd: If op_FltArtificialInd is specified, the field named in this input will be compared to the value in FltArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltArtificialInd must be specified if op_FltArtificialInd is specified.
             :type val_f_FltArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltArtificialInd: If op_FltArtificialInd is specified, this value will be compared to the value in FltArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltArtificialInd must be specified if op_FltArtificialInd is specified.
             :type val_c_FltArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltChangedCols: The operator to apply to the field FltChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltChangedCols: If op_FltChangedCols is specified, the field named in this input will be compared to the value in FltChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltChangedCols must be specified if op_FltChangedCols is specified.
             :type val_f_FltChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltChangedCols: If op_FltChangedCols is specified, this value will be compared to the value in FltChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltChangedCols must be specified if op_FltChangedCols is specified.
             :type val_c_FltChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltConfigText: The operator to apply to the field FltConfigText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltConfigText: The original text of the configuration from witch this rule is built. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltConfigText: If op_FltConfigText is specified, the field named in this input will be compared to the value in FltConfigText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltConfigText must be specified if op_FltConfigText is specified.
             :type val_f_FltConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltConfigText: If op_FltConfigText is specified, this value will be compared to the value in FltConfigText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltConfigText must be specified if op_FltConfigText is specified.
             :type val_c_FltConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltEnabledInd: The operator to apply to the field FltEnabledInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltEnabledInd: A flag indicating whether this rule is enabled in the configuration or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltEnabledInd: If op_FltEnabledInd is specified, the field named in this input will be compared to the value in FltEnabledInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltEnabledInd must be specified if op_FltEnabledInd is specified.
             :type val_f_FltEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltEnabledInd: If op_FltEnabledInd is specified, this value will be compared to the value in FltEnabledInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltEnabledInd must be specified if op_FltEnabledInd is specified.
             :type val_c_FltEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltEndTime: The operator to apply to the field FltEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltEndTime: If op_FltEndTime is specified, the field named in this input will be compared to the value in FltEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltEndTime must be specified if op_FltEndTime is specified.
             :type val_f_FltEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltEndTime: If op_FltEndTime is specified, this value will be compared to the value in FltEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltEndTime must be specified if op_FltEndTime is specified.
             :type val_c_FltEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltEstablishedInd: The operator to apply to the field FltEstablishedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltEstablishedInd: A flag indicating whether this rule has the option 'established' (cisco specific). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltEstablishedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltEstablishedInd: If op_FltEstablishedInd is specified, the field named in this input will be compared to the value in FltEstablishedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltEstablishedInd must be specified if op_FltEstablishedInd is specified.
             :type val_f_FltEstablishedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltEstablishedInd: If op_FltEstablishedInd is specified, this value will be compared to the value in FltEstablishedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltEstablishedInd must be specified if op_FltEstablishedInd is specified.
             :type val_c_FltEstablishedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltFirstSeenTime: The operator to apply to the field FltFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltFirstSeenTime: The timestamp of when NetMRI first discovered this rule. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltFirstSeenTime: If op_FltFirstSeenTime is specified, the field named in this input will be compared to the value in FltFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltFirstSeenTime must be specified if op_FltFirstSeenTime is specified.
             :type val_f_FltFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltFirstSeenTime: If op_FltFirstSeenTime is specified, this value will be compared to the value in FltFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltFirstSeenTime must be specified if op_FltFirstSeenTime is specified.
             :type val_c_FltFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltKey: The operator to apply to the field FltKey. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltKey: The computed key value that identifies this rule against text configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltKey: If op_FltKey is specified, the field named in this input will be compared to the value in FltKey using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltKey must be specified if op_FltKey is specified.
             :type val_f_FltKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltKey: If op_FltKey is specified, this value will be compared to the value in FltKey using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltKey must be specified if op_FltKey is specified.
             :type val_c_FltKey: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltOrder: The operator to apply to the field FltOrder. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltOrder: The numerical order of this rule in its rule list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltOrder: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltOrder: If op_FltOrder is specified, the field named in this input will be compared to the value in FltOrder using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltOrder must be specified if op_FltOrder is specified.
             :type val_f_FltOrder: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltOrder: If op_FltOrder is specified, this value will be compared to the value in FltOrder using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltOrder must be specified if op_FltOrder is specified.
             :type val_c_FltOrder: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltProvisionData: The operator to apply to the field FltProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltProvisionData: If op_FltProvisionData is specified, the field named in this input will be compared to the value in FltProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltProvisionData must be specified if op_FltProvisionData is specified.
             :type val_f_FltProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltProvisionData: If op_FltProvisionData is specified, this value will be compared to the value in FltProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltProvisionData must be specified if op_FltProvisionData is specified.
             :type val_c_FltProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltRelevantInd: The operator to apply to the field FltRelevantInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltRelevantInd: A flag indicating whether this rule is relevant for search operations. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltRelevantInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltRelevantInd: If op_FltRelevantInd is specified, the field named in this input will be compared to the value in FltRelevantInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltRelevantInd must be specified if op_FltRelevantInd is specified.
             :type val_f_FltRelevantInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltRelevantInd: If op_FltRelevantInd is specified, this value will be compared to the value in FltRelevantInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltRelevantInd must be specified if op_FltRelevantInd is specified.
             :type val_c_FltRelevantInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltStartTime: The operator to apply to the field FltStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltStartTime: If op_FltStartTime is specified, the field named in this input will be compared to the value in FltStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltStartTime must be specified if op_FltStartTime is specified.
             :type val_f_FltStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltStartTime: If op_FltStartTime is specified, this value will be compared to the value in FltStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltStartTime must be specified if op_FltStartTime is specified.
             :type val_c_FltStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltTimestamp: The operator to apply to the field FltTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltTimestamp: If op_FltTimestamp is specified, the field named in this input will be compared to the value in FltTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltTimestamp must be specified if op_FltTimestamp is specified.
             :type val_f_FltTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltTimestamp: If op_FltTimestamp is specified, this value will be compared to the value in FltTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltTimestamp must be specified if op_FltTimestamp is specified.
             :type val_c_FltTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SrcDeviceObjectID: The operator to apply to the field SrcDeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SrcDeviceObjectID: The internal NetMRI identifier for the source network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SrcDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SrcDeviceObjectID: If op_SrcDeviceObjectID is specified, the field named in this input will be compared to the value in SrcDeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SrcDeviceObjectID must be specified if op_SrcDeviceObjectID is specified.
             :type val_f_SrcDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SrcDeviceObjectID: If op_SrcDeviceObjectID is specified, this value will be compared to the value in SrcDeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SrcDeviceObjectID must be specified if op_SrcDeviceObjectID is specified.
             :type val_c_SrcDeviceObjectID: String

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

             :param timestamp: The data returned will represent the device filters as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter methods. The listed methods will be called on each device filter returned and included in the output. Available methods are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, src_device_object, dest_device_object, device_filter_set, data_source, device.
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
            |  ``default:`` DeviceFilterID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterID. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilter. Valid values are DeviceFilterID, DeviceID, DataSourceID, DeviceServiceID, SrcDeviceObjectID, DestDeviceObjectID, DeviceFilterSetID, FltFirstSeenTime, FltStartTime, FltEndTime, FltTimestamp, FltChangedCols, FltOrder, FltKey, FltAllowInd, FltRelevantInd, FltEnabledInd, FltEstablishedInd, FltArtificialInd, FltConfigText, FltProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_filters: An array of the DeviceFilter objects that match the specified input criteria.
             :rtype device_filters: Array of DeviceFilter

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def src_device_object(self, **kwargs):
        """The network object for the source of the filtered traffic.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The network object for the source of the filtered traffic.
             :rtype : DeviceObject

            """

        return self.api_request(self._get_method_fullname("src_device_object"), kwargs)

    def dest_device_object(self, **kwargs):
        """The network object for the destination of the filtered traffic.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The network object for the destination of the filtered traffic.
             :rtype : DeviceObject

            """

        return self.api_request(self._get_method_fullname("dest_device_object"), kwargs)

    def device_service(self, **kwargs):
        """The service object of this rule

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The service object of this rule
             :rtype : DeviceService

            """

        return self.api_request(self._get_method_fullname("device_service"), kwargs)

    def device_filter_set(self, **kwargs):
        """The rule list to which that rule belongs

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The rule list to which that rule belongs
             :rtype : DeviceFilterSet

            """

        return self.api_request(self._get_method_fullname("device_filter_set"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterID: The internal NetMRI identifier for the rule.
             :type DeviceFilterID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def describe(self, **kwargs):
        """Returns inquired information about this device rule based on description type.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_filter_id: The internal identifier of this device rule.
             :type device_filter_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description_type: The description type for a specific device rule property: Source, Destination, Port, Protocol, Service, ConfigText
             :type description_type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("describe"), kwargs)
