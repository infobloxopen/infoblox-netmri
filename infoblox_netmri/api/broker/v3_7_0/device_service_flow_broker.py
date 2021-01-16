from ..broker import Broker


class DeviceServiceFlowBroker(Broker):
    controller = "device_service_flows"

    def show(self, **kwargs):
        """Shows the details for the specified device service flow.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service flow methods. The listed methods will be called on each device service flow returned and included in the output. Available methods are: device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_service_flow: The device service flow identified by the specified DeviceServiceFlowID.
             :rtype device_service_flow: DeviceServiceFlow

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device service flows. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

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

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the service to which belongs this flow.
             :type DeviceServiceID: Array of Integer

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

             :param timestamp: The data returned will represent the device service flows as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service flow methods. The listed methods will be called on each device service flow returned and included in the output. Available methods are: device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, data_source, device.
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
            |  ``default:`` DeviceServiceFlowID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceFlowID. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax.
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

             :param select: The list of attributes to return for each DeviceServiceFlow. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax. If empty or omitted, all attributes will be returned.
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

             :return device_service_flows: An array of the DeviceServiceFlow objects that match the specified input criteria.
             :rtype device_service_flows: Array of DeviceServiceFlow

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device service flows matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the service to which belongs this flow.
             :type DeviceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SvfChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfDestDisplayText: The text that was defined in the configuration for the destination port part of this flow.
             :type SvfDestDisplayText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfDestPortMax: The numeric value for the destination port range max value. -1 if no meaning.
             :type SvfDestPortMax: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfDestPortMin: The numeric value for the destination port range min value. -1 if no meaning.
             :type SvfDestPortMin: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfEndTime: The ending effective time of this record, or empty if still in effect.
             :type SvfEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfFirstSeenTime: The timestamp of when NetMRI saw for the first time this flow.
             :type SvfFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfProtocolName: The protocol name.
             :type SvfProtocolName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfProtocolNum: The protocol number of the flow. A value between 0 to 255, 0 is for generic ip protocol.
             :type SvfProtocolNum: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfSrcDisplayText: The text that was defined in the configuration for the source port part of this flow.
             :type SvfSrcDisplayText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfSrcPortMax: The numeric value for the source port range max value. -1 if no meaning.
             :type SvfSrcPortMax: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfSrcPortMin: The numeric value for the source port range min value. -1 if no meaning.
             :type SvfSrcPortMin: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfStartTime: The starting effective time of this record.
             :type SvfStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvfTimestamp: The date and time this record was collected or calculated.
             :type SvfTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the device service flows as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service flow methods. The listed methods will be called on each device service flow returned and included in the output. Available methods are: device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, data_source, device.
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
            |  ``default:`` DeviceServiceFlowID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceFlowID. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax.
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

             :param select: The list of attributes to return for each DeviceServiceFlow. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device service flows, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DeviceServiceFlowID, DeviceServiceID, SvfChangedCols, SvfDestDisplayText, SvfDestPortMax, SvfDestPortMin, SvfEndTime, SvfFirstSeenTime, SvfProtocolName, SvfProtocolNum, SvfSrcDisplayText, SvfSrcPortMax, SvfSrcPortMin, SvfStartTime, SvfTimestamp.
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

             :return device_service_flows: An array of the DeviceServiceFlow objects that match the specified input criteria.
             :rtype device_service_flows: Array of DeviceServiceFlow

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device service flows matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DeviceServiceFlowID, DeviceServiceID, SvfChangedCols, SvfDestDisplayText, SvfDestPortMax, SvfDestPortMin, SvfEndTime, SvfFirstSeenTime, SvfProtocolName, SvfProtocolNum, SvfSrcDisplayText, SvfSrcPortMax, SvfSrcPortMin, SvfStartTime, SvfTimestamp.

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

             :param op_DeviceServiceFlowID: The operator to apply to the field DeviceServiceFlowID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceServiceFlowID: The internal NetMRI identifier for this flow description. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceServiceFlowID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceServiceFlowID: If op_DeviceServiceFlowID is specified, the field named in this input will be compared to the value in DeviceServiceFlowID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceServiceFlowID must be specified if op_DeviceServiceFlowID is specified.
             :type val_f_DeviceServiceFlowID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceServiceFlowID: If op_DeviceServiceFlowID is specified, this value will be compared to the value in DeviceServiceFlowID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceServiceFlowID must be specified if op_DeviceServiceFlowID is specified.
             :type val_c_DeviceServiceFlowID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceServiceID: The operator to apply to the field DeviceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceServiceID: The internal NetMRI identifier for the service to which belongs this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SvfChangedCols: The operator to apply to the field SvfChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfChangedCols: If op_SvfChangedCols is specified, the field named in this input will be compared to the value in SvfChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfChangedCols must be specified if op_SvfChangedCols is specified.
             :type val_f_SvfChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfChangedCols: If op_SvfChangedCols is specified, this value will be compared to the value in SvfChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfChangedCols must be specified if op_SvfChangedCols is specified.
             :type val_c_SvfChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfDestDisplayText: The operator to apply to the field SvfDestDisplayText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfDestDisplayText: The text that was defined in the configuration for the destination port part of this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfDestDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfDestDisplayText: If op_SvfDestDisplayText is specified, the field named in this input will be compared to the value in SvfDestDisplayText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfDestDisplayText must be specified if op_SvfDestDisplayText is specified.
             :type val_f_SvfDestDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfDestDisplayText: If op_SvfDestDisplayText is specified, this value will be compared to the value in SvfDestDisplayText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfDestDisplayText must be specified if op_SvfDestDisplayText is specified.
             :type val_c_SvfDestDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfDestPortMax: The operator to apply to the field SvfDestPortMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfDestPortMax: The numeric value for the destination port range max value. -1 if no meaning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfDestPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfDestPortMax: If op_SvfDestPortMax is specified, the field named in this input will be compared to the value in SvfDestPortMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfDestPortMax must be specified if op_SvfDestPortMax is specified.
             :type val_f_SvfDestPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfDestPortMax: If op_SvfDestPortMax is specified, this value will be compared to the value in SvfDestPortMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfDestPortMax must be specified if op_SvfDestPortMax is specified.
             :type val_c_SvfDestPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfDestPortMin: The operator to apply to the field SvfDestPortMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfDestPortMin: The numeric value for the destination port range min value. -1 if no meaning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfDestPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfDestPortMin: If op_SvfDestPortMin is specified, the field named in this input will be compared to the value in SvfDestPortMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfDestPortMin must be specified if op_SvfDestPortMin is specified.
             :type val_f_SvfDestPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfDestPortMin: If op_SvfDestPortMin is specified, this value will be compared to the value in SvfDestPortMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfDestPortMin must be specified if op_SvfDestPortMin is specified.
             :type val_c_SvfDestPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfEndTime: The operator to apply to the field SvfEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfEndTime: If op_SvfEndTime is specified, the field named in this input will be compared to the value in SvfEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfEndTime must be specified if op_SvfEndTime is specified.
             :type val_f_SvfEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfEndTime: If op_SvfEndTime is specified, this value will be compared to the value in SvfEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfEndTime must be specified if op_SvfEndTime is specified.
             :type val_c_SvfEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfFirstSeenTime: The operator to apply to the field SvfFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfFirstSeenTime: The timestamp of when NetMRI saw for the first time this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfFirstSeenTime: If op_SvfFirstSeenTime is specified, the field named in this input will be compared to the value in SvfFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfFirstSeenTime must be specified if op_SvfFirstSeenTime is specified.
             :type val_f_SvfFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfFirstSeenTime: If op_SvfFirstSeenTime is specified, this value will be compared to the value in SvfFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfFirstSeenTime must be specified if op_SvfFirstSeenTime is specified.
             :type val_c_SvfFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfProtocolName: The operator to apply to the field SvfProtocolName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfProtocolName: The protocol name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfProtocolName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfProtocolName: If op_SvfProtocolName is specified, the field named in this input will be compared to the value in SvfProtocolName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfProtocolName must be specified if op_SvfProtocolName is specified.
             :type val_f_SvfProtocolName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfProtocolName: If op_SvfProtocolName is specified, this value will be compared to the value in SvfProtocolName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfProtocolName must be specified if op_SvfProtocolName is specified.
             :type val_c_SvfProtocolName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfProtocolNum: The operator to apply to the field SvfProtocolNum. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfProtocolNum: The protocol number of the flow. A value between 0 to 255, 0 is for generic ip protocol. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfProtocolNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfProtocolNum: If op_SvfProtocolNum is specified, the field named in this input will be compared to the value in SvfProtocolNum using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfProtocolNum must be specified if op_SvfProtocolNum is specified.
             :type val_f_SvfProtocolNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfProtocolNum: If op_SvfProtocolNum is specified, this value will be compared to the value in SvfProtocolNum using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfProtocolNum must be specified if op_SvfProtocolNum is specified.
             :type val_c_SvfProtocolNum: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfSrcDisplayText: The operator to apply to the field SvfSrcDisplayText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfSrcDisplayText: The text that was defined in the configuration for the source port part of this flow. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfSrcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfSrcDisplayText: If op_SvfSrcDisplayText is specified, the field named in this input will be compared to the value in SvfSrcDisplayText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfSrcDisplayText must be specified if op_SvfSrcDisplayText is specified.
             :type val_f_SvfSrcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfSrcDisplayText: If op_SvfSrcDisplayText is specified, this value will be compared to the value in SvfSrcDisplayText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfSrcDisplayText must be specified if op_SvfSrcDisplayText is specified.
             :type val_c_SvfSrcDisplayText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfSrcPortMax: The operator to apply to the field SvfSrcPortMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfSrcPortMax: The numeric value for the source port range max value. -1 if no meaning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfSrcPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfSrcPortMax: If op_SvfSrcPortMax is specified, the field named in this input will be compared to the value in SvfSrcPortMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfSrcPortMax must be specified if op_SvfSrcPortMax is specified.
             :type val_f_SvfSrcPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfSrcPortMax: If op_SvfSrcPortMax is specified, this value will be compared to the value in SvfSrcPortMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfSrcPortMax must be specified if op_SvfSrcPortMax is specified.
             :type val_c_SvfSrcPortMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfSrcPortMin: The operator to apply to the field SvfSrcPortMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfSrcPortMin: The numeric value for the source port range min value. -1 if no meaning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfSrcPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfSrcPortMin: If op_SvfSrcPortMin is specified, the field named in this input will be compared to the value in SvfSrcPortMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfSrcPortMin must be specified if op_SvfSrcPortMin is specified.
             :type val_f_SvfSrcPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfSrcPortMin: If op_SvfSrcPortMin is specified, this value will be compared to the value in SvfSrcPortMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfSrcPortMin must be specified if op_SvfSrcPortMin is specified.
             :type val_c_SvfSrcPortMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfStartTime: The operator to apply to the field SvfStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfStartTime: If op_SvfStartTime is specified, the field named in this input will be compared to the value in SvfStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfStartTime must be specified if op_SvfStartTime is specified.
             :type val_f_SvfStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfStartTime: If op_SvfStartTime is specified, this value will be compared to the value in SvfStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfStartTime must be specified if op_SvfStartTime is specified.
             :type val_c_SvfStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvfTimestamp: The operator to apply to the field SvfTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvfTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvfTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvfTimestamp: If op_SvfTimestamp is specified, the field named in this input will be compared to the value in SvfTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvfTimestamp must be specified if op_SvfTimestamp is specified.
             :type val_f_SvfTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvfTimestamp: If op_SvfTimestamp is specified, this value will be compared to the value in SvfTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvfTimestamp must be specified if op_SvfTimestamp is specified.
             :type val_c_SvfTimestamp: String

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

             :param timestamp: The data returned will represent the device service flows as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service flow methods. The listed methods will be called on each device service flow returned and included in the output. Available methods are: device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_service, data_source, device.
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
            |  ``default:`` DeviceServiceFlowID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceFlowID. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax.
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

             :param select: The list of attributes to return for each DeviceServiceFlow. Valid values are DeviceServiceFlowID, DeviceServiceID, DeviceID, DataSourceID, SvfFirstSeenTime, SvfStartTime, SvfEndTime, SvfTimestamp, SvfChangedCols, SvfProtocolNum, SvfProtocolName, SvfSrcDisplayText, SvfSrcPortMin, SvfSrcPortMax, SvfDestDisplayText, SvfDestPortMin, SvfDestPortMax. If empty or omitted, all attributes will be returned.
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

             :return device_service_flows: An array of the DeviceServiceFlow objects that match the specified input criteria.
             :rtype device_service_flows: Array of DeviceServiceFlow

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device_service(self, **kwargs):
        """The service object to which this flow belongs.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The service object to which this flow belongs.
             :rtype : DeviceService

            """

        return self.api_request(self._get_method_fullname("device_service"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Integer

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

             :param DeviceServiceFlowID: The internal NetMRI identifier for this flow description.
             :type DeviceServiceFlowID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
