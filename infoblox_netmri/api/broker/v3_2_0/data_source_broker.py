from ..broker import Broker


class DataSourceBroker(Broker):
    controller = "data_sources"

    def index(self, **kwargs):
        """Lists the available data sources. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for this data source.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for this data source.
             :type DataSourceID: Array of Integer

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

             :param timestamp: The data returned will represent the data sources as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data source methods. The listed methods will be called on each data source returned and included in the output. Available methods are: network_name.
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
            |  ``default:`` DataSourceID

             :param sort: The data field(s) to use for sorting the output. Default is DataSourceID. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo.
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

             :param select: The list of attributes to return for each DataSource. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo. If empty or omitted, all attributes will be returned.
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

             :return data_sources: An array of the DataSource objects that match the specified input criteria.
             :rtype data_sources: Array of DataSource

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified data source.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for this data source.
             :type DataSourceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data source methods. The listed methods will be called on each data source returned and included in the output. Available methods are: network_name.
             :type methods: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return data_source: The data source identified by the specified DataSourceID.
             :rtype data_source: DataSource

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available data sources matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DataSourceChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DataSourceChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DataSourceEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type DataSourceEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for this data source.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for this data source.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceIPDotted: The IP address of this data source, in dotted notation.
             :type DataSourceIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceIPDotted: The IP address of this data source, in dotted notation.
             :type DataSourceIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceIPNumeric: The numerical IP address of this data source.
             :type DataSourceIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceIPNumeric: The numerical IP address of this data source.
             :type DataSourceIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceName: The name of this data source.
             :type DataSourceName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceName: The name of this data source.
             :type DataSourceName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourcePrivateIPDotted: Another IP address for the data source, in dotted notation.
             :type DataSourcePrivateIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourcePrivateIPDotted: Another IP address for the data source, in dotted notation.
             :type DataSourcePrivateIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourcePrivateIPNumeric: The numerical version of the alternate IP address.
             :type DataSourcePrivateIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourcePrivateIPNumeric: The numerical version of the alternate IP address.
             :type DataSourcePrivateIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceSerialNo: The serial number of the collector.
             :type DataSourceSerialNo: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceSerialNo: The serial number of the collector.
             :type DataSourceSerialNo: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceStartTime: The starting effective time of this revision of the record.
             :type DataSourceStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceStartTime: The starting effective time of this revision of the record.
             :type DataSourceStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceTimestamp: The date and time this record was collected or calculated.
             :type DataSourceTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceTimestamp: The date and time this record was collected or calculated.
             :type DataSourceTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Network: The network to which this data source is assigned.
             :type Network: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Network: The network to which this data source is assigned.
             :type Network: Array of String

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

             :param timestamp: The data returned will represent the data sources as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data source methods. The listed methods will be called on each data source returned and included in the output. Available methods are: network_name.
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
            |  ``default:`` DataSourceID

             :param sort: The data field(s) to use for sorting the output. Default is DataSourceID. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo.
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

             :param select: The list of attributes to return for each DataSource. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against data sources, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceChangedCols, DataSourceEndTime, DataSourceID, DataSourceIPDotted, DataSourceIPNumeric, DataSourceName, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo, DataSourceStartTime, DataSourceTimestamp, Network.
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

             :return data_sources: An array of the DataSource objects that match the specified input criteria.
             :rtype data_sources: Array of DataSource

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available data sources matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceChangedCols, DataSourceEndTime, DataSourceID, DataSourceIPDotted, DataSourceIPNumeric, DataSourceName, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo, DataSourceStartTime, DataSourceTimestamp, Network.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceChangedCols: The operator to apply to the field DataSourceChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceChangedCols: If op_DataSourceChangedCols is specified, the field named in this input will be compared to the value in DataSourceChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceChangedCols must be specified if op_DataSourceChangedCols is specified.
             :type val_f_DataSourceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceChangedCols: If op_DataSourceChangedCols is specified, this value will be compared to the value in DataSourceChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceChangedCols must be specified if op_DataSourceChangedCols is specified.
             :type val_c_DataSourceChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceEndTime: The operator to apply to the field DataSourceEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceEndTime: If op_DataSourceEndTime is specified, the field named in this input will be compared to the value in DataSourceEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceEndTime must be specified if op_DataSourceEndTime is specified.
             :type val_f_DataSourceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceEndTime: If op_DataSourceEndTime is specified, this value will be compared to the value in DataSourceEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceEndTime must be specified if op_DataSourceEndTime is specified.
             :type val_c_DataSourceEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for this data source. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DataSourceIPDotted: The operator to apply to the field DataSourceIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceIPDotted: The IP address of this data source, in dotted notation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceIPDotted: If op_DataSourceIPDotted is specified, the field named in this input will be compared to the value in DataSourceIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceIPDotted must be specified if op_DataSourceIPDotted is specified.
             :type val_f_DataSourceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceIPDotted: If op_DataSourceIPDotted is specified, this value will be compared to the value in DataSourceIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceIPDotted must be specified if op_DataSourceIPDotted is specified.
             :type val_c_DataSourceIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceIPNumeric: The operator to apply to the field DataSourceIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceIPNumeric: The numerical IP address of this data source. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceIPNumeric: If op_DataSourceIPNumeric is specified, the field named in this input will be compared to the value in DataSourceIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceIPNumeric must be specified if op_DataSourceIPNumeric is specified.
             :type val_f_DataSourceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceIPNumeric: If op_DataSourceIPNumeric is specified, this value will be compared to the value in DataSourceIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceIPNumeric must be specified if op_DataSourceIPNumeric is specified.
             :type val_c_DataSourceIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceName: The operator to apply to the field DataSourceName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceName: The name of this data source. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceName: If op_DataSourceName is specified, the field named in this input will be compared to the value in DataSourceName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceName must be specified if op_DataSourceName is specified.
             :type val_f_DataSourceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceName: If op_DataSourceName is specified, this value will be compared to the value in DataSourceName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceName must be specified if op_DataSourceName is specified.
             :type val_c_DataSourceName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourcePrivateIPDotted: The operator to apply to the field DataSourcePrivateIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourcePrivateIPDotted: Another IP address for the data source, in dotted notation. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourcePrivateIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourcePrivateIPDotted: If op_DataSourcePrivateIPDotted is specified, the field named in this input will be compared to the value in DataSourcePrivateIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourcePrivateIPDotted must be specified if op_DataSourcePrivateIPDotted is specified.
             :type val_f_DataSourcePrivateIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourcePrivateIPDotted: If op_DataSourcePrivateIPDotted is specified, this value will be compared to the value in DataSourcePrivateIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourcePrivateIPDotted must be specified if op_DataSourcePrivateIPDotted is specified.
             :type val_c_DataSourcePrivateIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourcePrivateIPNumeric: The operator to apply to the field DataSourcePrivateIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourcePrivateIPNumeric: The numerical version of the alternate IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourcePrivateIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourcePrivateIPNumeric: If op_DataSourcePrivateIPNumeric is specified, the field named in this input will be compared to the value in DataSourcePrivateIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourcePrivateIPNumeric must be specified if op_DataSourcePrivateIPNumeric is specified.
             :type val_f_DataSourcePrivateIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourcePrivateIPNumeric: If op_DataSourcePrivateIPNumeric is specified, this value will be compared to the value in DataSourcePrivateIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourcePrivateIPNumeric must be specified if op_DataSourcePrivateIPNumeric is specified.
             :type val_c_DataSourcePrivateIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceSerialNo: The operator to apply to the field DataSourceSerialNo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceSerialNo: The serial number of the collector. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceSerialNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceSerialNo: If op_DataSourceSerialNo is specified, the field named in this input will be compared to the value in DataSourceSerialNo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceSerialNo must be specified if op_DataSourceSerialNo is specified.
             :type val_f_DataSourceSerialNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceSerialNo: If op_DataSourceSerialNo is specified, this value will be compared to the value in DataSourceSerialNo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceSerialNo must be specified if op_DataSourceSerialNo is specified.
             :type val_c_DataSourceSerialNo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceStartTime: The operator to apply to the field DataSourceStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceStartTime: If op_DataSourceStartTime is specified, the field named in this input will be compared to the value in DataSourceStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceStartTime must be specified if op_DataSourceStartTime is specified.
             :type val_f_DataSourceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceStartTime: If op_DataSourceStartTime is specified, this value will be compared to the value in DataSourceStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceStartTime must be specified if op_DataSourceStartTime is specified.
             :type val_c_DataSourceStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceTimestamp: The operator to apply to the field DataSourceTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceTimestamp: If op_DataSourceTimestamp is specified, the field named in this input will be compared to the value in DataSourceTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceTimestamp must be specified if op_DataSourceTimestamp is specified.
             :type val_f_DataSourceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceTimestamp: If op_DataSourceTimestamp is specified, this value will be compared to the value in DataSourceTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceTimestamp must be specified if op_DataSourceTimestamp is specified.
             :type val_c_DataSourceTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Network: The operator to apply to the field Network. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Network: The network to which this data source is assigned. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Network: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Network: If op_Network is specified, the field named in this input will be compared to the value in Network using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Network must be specified if op_Network is specified.
             :type val_f_Network: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Network: If op_Network is specified, this value will be compared to the value in Network using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Network must be specified if op_Network is specified.
             :type val_c_Network: String

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

             :param timestamp: The data returned will represent the data sources as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of data source methods. The listed methods will be called on each data source returned and included in the output. Available methods are: network_name.
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
            |  ``default:`` DataSourceID

             :param sort: The data field(s) to use for sorting the output. Default is DataSourceID. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo.
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

             :param select: The list of attributes to return for each DataSource. Valid values are DataSourceID, DataSourceStartTime, DataSourceEndTime, DataSourceChangedCols, DataSourceTimestamp, Network, DataSourceName, DataSourceIPDotted, DataSourceIPNumeric, DataSourcePrivateIPDotted, DataSourcePrivateIPNumeric, DataSourceSerialNo. If empty or omitted, all attributes will be returned.
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

             :return data_sources: An array of the DataSource objects that match the specified input criteria.
             :rtype data_sources: Array of DataSource

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
