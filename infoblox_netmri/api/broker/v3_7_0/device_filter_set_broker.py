from ..broker import Broker


class DeviceFilterSetBroker(Broker):
    controller = "device_filter_sets"

    def show(self, **kwargs):
        """Shows the details for the specified device filter set.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterSetID: The internal NetMRI identifier for this rule list.
             :type DeviceFilterSetID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter set methods. The listed methods will be called on each device filter set returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_filter_set: The device filter set identified by the specified DeviceFilterSetID.
             :rtype device_filter_set: DeviceFilterSet

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device filter sets. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFilterSetID: The internal NetMRI identifier for this rule list.
             :type DeviceFilterSetID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this rule list belongs.
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

             :param timestamp: The data returned will represent the device filter sets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter set methods. The listed methods will be called on each device filter set returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DeviceFilterSetID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterSetID. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilterSet. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_filter_sets: An array of the DeviceFilterSet objects that match the specified input criteria.
             :rtype device_filter_sets: Array of DeviceFilterSet

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device filter sets matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceFilterSetID: The internal NetMRI identifier for this rule list.
             :type DeviceFilterSetID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this rule list belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetArtificialInd: A flag indicating that this rule list has no counterpart in the device configuration.
             :type FltSetArtificialInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type FltSetChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetConfigText: The original text of the definition of this rule list in the device configuration.
             :type FltSetConfigText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetEndTime: The ending effective time of this record, or empty if still in effect.
             :type FltSetEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetFirstSeenTime: The timestamp of when NetMRI first discovered this rule list.
             :type FltSetFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetIPVersion: the IP version of the packets filtered by this rule list - default is 4.
             :type FltSetIPVersion: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetName: The name of this rule-list.
             :type FltSetName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetProvisionData: Internal data - do not modify, may change without warning.
             :type FltSetProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetStartTime: The starting effective time of this record.
             :type FltSetStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetTimestamp: The date and time this record was collected or calculated.
             :type FltSetTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FltSetUseCount: The number of usage of this rule list inside the configuration (may be for filtering or for NAT, vpn etc).
             :type FltSetUseCount: Array of Integer

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

             :param timestamp: The data returned will represent the device filter sets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter set methods. The listed methods will be called on each device filter set returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DeviceFilterSetID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterSetID. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilterSet. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device filter sets, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceFilterSetID, DeviceID, FltSetArtificialInd, FltSetChangedCols, FltSetConfigText, FltSetEndTime, FltSetFirstSeenTime, FltSetIPVersion, FltSetName, FltSetProvisionData, FltSetStartTime, FltSetTimestamp, FltSetUseCount.
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

             :return device_filter_sets: An array of the DeviceFilterSet objects that match the specified input criteria.
             :rtype device_filter_sets: Array of DeviceFilterSet

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device filter sets matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceFilterSetID, DeviceID, FltSetArtificialInd, FltSetChangedCols, FltSetConfigText, FltSetEndTime, FltSetFirstSeenTime, FltSetIPVersion, FltSetName, FltSetProvisionData, FltSetStartTime, FltSetTimestamp, FltSetUseCount.

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

             :param op_DeviceFilterSetID: The operator to apply to the field DeviceFilterSetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFilterSetID: The internal NetMRI identifier for this rule list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which this rule list belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_FltSetArtificialInd: The operator to apply to the field FltSetArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetArtificialInd: A flag indicating that this rule list has no counterpart in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetArtificialInd: If op_FltSetArtificialInd is specified, the field named in this input will be compared to the value in FltSetArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetArtificialInd must be specified if op_FltSetArtificialInd is specified.
             :type val_f_FltSetArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetArtificialInd: If op_FltSetArtificialInd is specified, this value will be compared to the value in FltSetArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetArtificialInd must be specified if op_FltSetArtificialInd is specified.
             :type val_c_FltSetArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetChangedCols: The operator to apply to the field FltSetChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetChangedCols: If op_FltSetChangedCols is specified, the field named in this input will be compared to the value in FltSetChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetChangedCols must be specified if op_FltSetChangedCols is specified.
             :type val_f_FltSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetChangedCols: If op_FltSetChangedCols is specified, this value will be compared to the value in FltSetChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetChangedCols must be specified if op_FltSetChangedCols is specified.
             :type val_c_FltSetChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetConfigText: The operator to apply to the field FltSetConfigText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetConfigText: The original text of the definition of this rule list in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetConfigText: If op_FltSetConfigText is specified, the field named in this input will be compared to the value in FltSetConfigText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetConfigText must be specified if op_FltSetConfigText is specified.
             :type val_f_FltSetConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetConfigText: If op_FltSetConfigText is specified, this value will be compared to the value in FltSetConfigText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetConfigText must be specified if op_FltSetConfigText is specified.
             :type val_c_FltSetConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetEndTime: The operator to apply to the field FltSetEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetEndTime: If op_FltSetEndTime is specified, the field named in this input will be compared to the value in FltSetEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetEndTime must be specified if op_FltSetEndTime is specified.
             :type val_f_FltSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetEndTime: If op_FltSetEndTime is specified, this value will be compared to the value in FltSetEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetEndTime must be specified if op_FltSetEndTime is specified.
             :type val_c_FltSetEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetFirstSeenTime: The operator to apply to the field FltSetFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetFirstSeenTime: The timestamp of when NetMRI first discovered this rule list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetFirstSeenTime: If op_FltSetFirstSeenTime is specified, the field named in this input will be compared to the value in FltSetFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetFirstSeenTime must be specified if op_FltSetFirstSeenTime is specified.
             :type val_f_FltSetFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetFirstSeenTime: If op_FltSetFirstSeenTime is specified, this value will be compared to the value in FltSetFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetFirstSeenTime must be specified if op_FltSetFirstSeenTime is specified.
             :type val_c_FltSetFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetIPVersion: The operator to apply to the field FltSetIPVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetIPVersion: the IP version of the packets filtered by this rule list - default is 4. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetIPVersion: If op_FltSetIPVersion is specified, the field named in this input will be compared to the value in FltSetIPVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetIPVersion must be specified if op_FltSetIPVersion is specified.
             :type val_f_FltSetIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetIPVersion: If op_FltSetIPVersion is specified, this value will be compared to the value in FltSetIPVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetIPVersion must be specified if op_FltSetIPVersion is specified.
             :type val_c_FltSetIPVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetName: The operator to apply to the field FltSetName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetName: The name of this rule-list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetName: If op_FltSetName is specified, the field named in this input will be compared to the value in FltSetName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetName must be specified if op_FltSetName is specified.
             :type val_f_FltSetName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetName: If op_FltSetName is specified, this value will be compared to the value in FltSetName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetName must be specified if op_FltSetName is specified.
             :type val_c_FltSetName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetProvisionData: The operator to apply to the field FltSetProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetProvisionData: If op_FltSetProvisionData is specified, the field named in this input will be compared to the value in FltSetProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetProvisionData must be specified if op_FltSetProvisionData is specified.
             :type val_f_FltSetProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetProvisionData: If op_FltSetProvisionData is specified, this value will be compared to the value in FltSetProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetProvisionData must be specified if op_FltSetProvisionData is specified.
             :type val_c_FltSetProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetStartTime: The operator to apply to the field FltSetStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetStartTime: If op_FltSetStartTime is specified, the field named in this input will be compared to the value in FltSetStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetStartTime must be specified if op_FltSetStartTime is specified.
             :type val_f_FltSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetStartTime: If op_FltSetStartTime is specified, this value will be compared to the value in FltSetStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetStartTime must be specified if op_FltSetStartTime is specified.
             :type val_c_FltSetStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetTimestamp: The operator to apply to the field FltSetTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetTimestamp: If op_FltSetTimestamp is specified, the field named in this input will be compared to the value in FltSetTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetTimestamp must be specified if op_FltSetTimestamp is specified.
             :type val_f_FltSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetTimestamp: If op_FltSetTimestamp is specified, this value will be compared to the value in FltSetTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetTimestamp must be specified if op_FltSetTimestamp is specified.
             :type val_c_FltSetTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FltSetUseCount: The operator to apply to the field FltSetUseCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FltSetUseCount: The number of usage of this rule list inside the configuration (may be for filtering or for NAT, vpn etc). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FltSetUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FltSetUseCount: If op_FltSetUseCount is specified, the field named in this input will be compared to the value in FltSetUseCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FltSetUseCount must be specified if op_FltSetUseCount is specified.
             :type val_f_FltSetUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FltSetUseCount: If op_FltSetUseCount is specified, this value will be compared to the value in FltSetUseCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FltSetUseCount must be specified if op_FltSetUseCount is specified.
             :type val_c_FltSetUseCount: String

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

             :param timestamp: The data returned will represent the device filter sets as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device filter set methods. The listed methods will be called on each device filter set returned and included in the output. Available methods are: data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DeviceFilterSetID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFilterSetID. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData.
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

             :param select: The list of attributes to return for each DeviceFilterSet. Valid values are DeviceFilterSetID, DeviceID, DataSourceID, FltSetFirstSeenTime, FltSetStartTime, FltSetEndTime, FltSetTimestamp, FltSetChangedCols, FltSetName, FltSetIPVersion, FltSetUseCount, FltSetArtificialInd, FltSetConfigText, FltSetProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_filter_sets: An array of the DeviceFilterSet objects that match the specified input criteria.
             :rtype device_filter_sets: Array of DeviceFilterSet

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFilterSetID: The internal NetMRI identifier for this rule list.
             :type DeviceFilterSetID: Integer

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

             :param DeviceFilterSetID: The internal NetMRI identifier for this rule list.
             :type DeviceFilterSetID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
