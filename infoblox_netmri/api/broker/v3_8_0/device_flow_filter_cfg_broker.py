from ..broker import Broker


class DeviceFlowFilterCfgBroker(Broker):
    controller = "device_flow_filter_cfgs"

    def show(self, **kwargs):
        """Shows the details for the specified device flow filter cfg.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device flow filter cfg methods. The listed methods will be called on each device flow filter cfg returned and included in the output. Available methods are: src_device_zone, dest_device_zone, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: src_device_zone, dest_device_zone, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_flow_filter_cfg: The device flow filter cfg identified by the specified DeviceFlowFilterCfgID.
             :rtype device_flow_filter_cfg: DeviceFlowFilterCfg

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device flow filter cfgs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Array of Integer

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

             :param timestamp: The data returned will represent the device flow filter cfgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device flow filter cfg methods. The listed methods will be called on each device flow filter cfg returned and included in the output. Available methods are: src_device_zone, dest_device_zone, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: src_device_zone, dest_device_zone, data_source, device.
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
            |  ``default:`` DeviceFlowFilterCfgID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFlowFilterCfgID. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData.
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

             :param select: The list of attributes to return for each DeviceFlowFilterCfg. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_flow_filter_cfgs: An array of the DeviceFlowFilterCfg objects that match the specified input criteria.
             :rtype device_flow_filter_cfgs: Array of DeviceFlowFilterCfg

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device flow filter cfgs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DestDeviceZoneID: The internal NetMRI identifier of the Zone that is destination point for this ip packet flow definition.
             :type DestDeviceZoneID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this ip packet flow definition
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type FfcChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcConfigText: The text that was defined in the configuration for this ip packet flow definition.
             :type FfcConfigText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcData: Extra data for this usage of the rulelist. May depend on the vendor implementation.
             :type FfcData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcDisplayText: The associated text for display.
             :type FfcDisplayText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcEndTime: The ending effective time of this record, or empty if still in effect.
             :type FfcEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcFirstSeenTime: The timestamp of when NetMRI saw for the first time this ip packet flow definition
             :type FfcFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcName: The name associated with this usage of the rulelist.
             :type FfcName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcProvisionData: Internal data - do not modify, may change without warning.
             :type FfcProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcStartTime: The starting effective time of this record.
             :type FfcStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcTimestamp: The date and time this record was collected or calculated.
             :type FfcTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FfcType: The type of operation applied on this ip packet flow definition. One of : 'filter', 'nat', 'vpn',
             :type FfcType: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SrcDeviceZoneID: The internal NetMRI identifier of the Zone that is source point for this ip packet flow definition
             :type SrcDeviceZoneID: Array of Integer

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

             :param timestamp: The data returned will represent the device flow filter cfgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device flow filter cfg methods. The listed methods will be called on each device flow filter cfg returned and included in the output. Available methods are: src_device_zone, dest_device_zone, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: src_device_zone, dest_device_zone, data_source, device.
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
            |  ``default:`` DeviceFlowFilterCfgID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFlowFilterCfgID. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData.
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

             :param select: The list of attributes to return for each DeviceFlowFilterCfg. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device flow filter cfgs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DestDeviceZoneID, DeviceFlowFilterCfgID, DeviceID, FfcChangedCols, FfcConfigText, FfcData, FfcDisplayText, FfcEndTime, FfcFirstSeenTime, FfcName, FfcProvisionData, FfcStartTime, FfcTimestamp, FfcType, SrcDeviceZoneID.
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

             :return device_flow_filter_cfgs: An array of the DeviceFlowFilterCfg objects that match the specified input criteria.
             :rtype device_flow_filter_cfgs: Array of DeviceFlowFilterCfg

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device flow filter cfgs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DestDeviceZoneID, DeviceFlowFilterCfgID, DeviceID, FfcChangedCols, FfcConfigText, FfcData, FfcDisplayText, FfcEndTime, FfcFirstSeenTime, FfcName, FfcProvisionData, FfcStartTime, FfcTimestamp, FfcType, SrcDeviceZoneID.

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

             :param op_DestDeviceZoneID: The operator to apply to the field DestDeviceZoneID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DestDeviceZoneID: The internal NetMRI identifier of the Zone that is destination point for this ip packet flow definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DestDeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DestDeviceZoneID: If op_DestDeviceZoneID is specified, the field named in this input will be compared to the value in DestDeviceZoneID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DestDeviceZoneID must be specified if op_DestDeviceZoneID is specified.
             :type val_f_DestDeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DestDeviceZoneID: If op_DestDeviceZoneID is specified, this value will be compared to the value in DestDeviceZoneID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DestDeviceZoneID must be specified if op_DestDeviceZoneID is specified.
             :type val_c_DestDeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceFlowFilterCfgID: The operator to apply to the field DeviceFlowFilterCfgID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceFlowFilterCfgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceFlowFilterCfgID: If op_DeviceFlowFilterCfgID is specified, the field named in this input will be compared to the value in DeviceFlowFilterCfgID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceFlowFilterCfgID must be specified if op_DeviceFlowFilterCfgID is specified.
             :type val_f_DeviceFlowFilterCfgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceFlowFilterCfgID: If op_DeviceFlowFilterCfgID is specified, this value will be compared to the value in DeviceFlowFilterCfgID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceFlowFilterCfgID must be specified if op_DeviceFlowFilterCfgID is specified.
             :type val_c_DeviceFlowFilterCfgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which belongs this ip packet flow definition For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_FfcChangedCols: The operator to apply to the field FfcChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcChangedCols: If op_FfcChangedCols is specified, the field named in this input will be compared to the value in FfcChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcChangedCols must be specified if op_FfcChangedCols is specified.
             :type val_f_FfcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcChangedCols: If op_FfcChangedCols is specified, this value will be compared to the value in FfcChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcChangedCols must be specified if op_FfcChangedCols is specified.
             :type val_c_FfcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcConfigText: The operator to apply to the field FfcConfigText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcConfigText: The text that was defined in the configuration for this ip packet flow definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcConfigText: If op_FfcConfigText is specified, the field named in this input will be compared to the value in FfcConfigText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcConfigText must be specified if op_FfcConfigText is specified.
             :type val_f_FfcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcConfigText: If op_FfcConfigText is specified, this value will be compared to the value in FfcConfigText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcConfigText must be specified if op_FfcConfigText is specified.
             :type val_c_FfcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcData: The operator to apply to the field FfcData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcData: Extra data for this usage of the rulelist. May depend on the vendor implementation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcData: If op_FfcData is specified, the field named in this input will be compared to the value in FfcData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcData must be specified if op_FfcData is specified.
             :type val_f_FfcData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcData: If op_FfcData is specified, this value will be compared to the value in FfcData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcData must be specified if op_FfcData is specified.
             :type val_c_FfcData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcDisplayText: The operator to apply to the field FfcDisplayText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcDisplayText: The associated text for display. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcDisplayText: If op_FfcDisplayText is specified, the field named in this input will be compared to the value in FfcDisplayText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcDisplayText must be specified if op_FfcDisplayText is specified.
             :type val_f_FfcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcDisplayText: If op_FfcDisplayText is specified, this value will be compared to the value in FfcDisplayText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcDisplayText must be specified if op_FfcDisplayText is specified.
             :type val_c_FfcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcEndTime: The operator to apply to the field FfcEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcEndTime: If op_FfcEndTime is specified, the field named in this input will be compared to the value in FfcEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcEndTime must be specified if op_FfcEndTime is specified.
             :type val_f_FfcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcEndTime: If op_FfcEndTime is specified, this value will be compared to the value in FfcEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcEndTime must be specified if op_FfcEndTime is specified.
             :type val_c_FfcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcFirstSeenTime: The operator to apply to the field FfcFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcFirstSeenTime: The timestamp of when NetMRI saw for the first time this ip packet flow definition For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcFirstSeenTime: If op_FfcFirstSeenTime is specified, the field named in this input will be compared to the value in FfcFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcFirstSeenTime must be specified if op_FfcFirstSeenTime is specified.
             :type val_f_FfcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcFirstSeenTime: If op_FfcFirstSeenTime is specified, this value will be compared to the value in FfcFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcFirstSeenTime must be specified if op_FfcFirstSeenTime is specified.
             :type val_c_FfcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcName: The operator to apply to the field FfcName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcName: The name associated with this usage of the rulelist. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcName: If op_FfcName is specified, the field named in this input will be compared to the value in FfcName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcName must be specified if op_FfcName is specified.
             :type val_f_FfcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcName: If op_FfcName is specified, this value will be compared to the value in FfcName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcName must be specified if op_FfcName is specified.
             :type val_c_FfcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcProvisionData: The operator to apply to the field FfcProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcProvisionData: If op_FfcProvisionData is specified, the field named in this input will be compared to the value in FfcProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcProvisionData must be specified if op_FfcProvisionData is specified.
             :type val_f_FfcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcProvisionData: If op_FfcProvisionData is specified, this value will be compared to the value in FfcProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcProvisionData must be specified if op_FfcProvisionData is specified.
             :type val_c_FfcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcStartTime: The operator to apply to the field FfcStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcStartTime: If op_FfcStartTime is specified, the field named in this input will be compared to the value in FfcStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcStartTime must be specified if op_FfcStartTime is specified.
             :type val_f_FfcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcStartTime: If op_FfcStartTime is specified, this value will be compared to the value in FfcStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcStartTime must be specified if op_FfcStartTime is specified.
             :type val_c_FfcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcTimestamp: The operator to apply to the field FfcTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcTimestamp: If op_FfcTimestamp is specified, the field named in this input will be compared to the value in FfcTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcTimestamp must be specified if op_FfcTimestamp is specified.
             :type val_f_FfcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcTimestamp: If op_FfcTimestamp is specified, this value will be compared to the value in FfcTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcTimestamp must be specified if op_FfcTimestamp is specified.
             :type val_c_FfcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FfcType: The operator to apply to the field FfcType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FfcType: The type of operation applied on this ip packet flow definition. One of : 'filter', 'nat', 'vpn',  For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FfcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FfcType: If op_FfcType is specified, the field named in this input will be compared to the value in FfcType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FfcType must be specified if op_FfcType is specified.
             :type val_f_FfcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FfcType: If op_FfcType is specified, this value will be compared to the value in FfcType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FfcType must be specified if op_FfcType is specified.
             :type val_c_FfcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SrcDeviceZoneID: The operator to apply to the field SrcDeviceZoneID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SrcDeviceZoneID: The internal NetMRI identifier of the Zone that is source point for this ip packet flow definition For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SrcDeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SrcDeviceZoneID: If op_SrcDeviceZoneID is specified, the field named in this input will be compared to the value in SrcDeviceZoneID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SrcDeviceZoneID must be specified if op_SrcDeviceZoneID is specified.
             :type val_f_SrcDeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SrcDeviceZoneID: If op_SrcDeviceZoneID is specified, this value will be compared to the value in SrcDeviceZoneID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SrcDeviceZoneID must be specified if op_SrcDeviceZoneID is specified.
             :type val_c_SrcDeviceZoneID: String

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

             :param timestamp: The data returned will represent the device flow filter cfgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device flow filter cfg methods. The listed methods will be called on each device flow filter cfg returned and included in the output. Available methods are: src_device_zone, dest_device_zone, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: src_device_zone, dest_device_zone, data_source, device.
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
            |  ``default:`` DeviceFlowFilterCfgID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceFlowFilterCfgID. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData.
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

             :param select: The list of attributes to return for each DeviceFlowFilterCfg. Valid values are DeviceFlowFilterCfgID, DeviceID, DataSourceID, FfcName, FfcData, FfcFirstSeenTime, FfcStartTime, FfcEndTime, FfcTimestamp, FfcChangedCols, SrcDeviceZoneID, DestDeviceZoneID, FfcType, FfcDisplayText, FfcConfigText, FfcProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_flow_filter_cfgs: An array of the DeviceFlowFilterCfg objects that match the specified input criteria.
             :rtype device_flow_filter_cfgs: Array of DeviceFlowFilterCfg

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def src_device_zone(self, **kwargs):
        """The DeviceZone that is source point for this ip packet flow definition.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The DeviceZone that is source point for this ip packet flow definition.
             :rtype : DeviceZone

            """

        return self.api_request(self._get_method_fullname("src_device_zone"), kwargs)

    def dest_device_zone(self, **kwargs):
        """The DeviceZone that is destination point for this ip packet flow definition.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The DeviceZone that is destination point for this ip packet flow definition.
             :rtype : DeviceZone

            """

        return self.api_request(self._get_method_fullname("dest_device_zone"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceFlowFilterCfgID: The internal NetMRI identifier for this ip packet flow definition.
             :type DeviceFlowFilterCfgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)
