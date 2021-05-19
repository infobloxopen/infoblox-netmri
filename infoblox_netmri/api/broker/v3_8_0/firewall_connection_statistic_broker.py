from ..broker import Broker


class FirewallConnectionStatisticBroker(Broker):
    controller = "firewall_connection_statistics"

    def index(self, **kwargs):
        """Lists the available firewall connection statistics. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which firewall connection statistics information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which firewall connection statistics information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the firewall connection statistics with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the firewall connection statistics with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of firewall connection statistic methods. The listed methods will be called on each firewall connection statistic returned and included in the output. Available methods are: device.
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
            |  ``default:`` FWCSID

             :param sort: The data field(s) to use for sorting the output. Default is FWCSID. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex.
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

             :param select: The list of attributes to return for each FirewallConnectionStatistic. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex. If empty or omitted, all attributes will be returned.
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

             :return firewall_connection_statistics: An array of the FirewallConnectionStatistic objects that match the specified input criteria.
             :rtype firewall_connection_statistics: Array of FirewallConnectionStatistic

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified firewall connection statistic.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of firewall connection statistic methods. The listed methods will be called on each firewall connection statistic returned and included in the output. Available methods are: device.
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

             :return firewall_connection_statistic: The firewall connection statistic identified by the specified FWCSID.
             :rtype firewall_connection_statistic: FirewallConnectionStatistic

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available firewall connection statistics matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which firewall connection statistics information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which firewall connection statistics information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSCurrentInUse: Currently in used firewall connection statistics.
             :type FWCSCurrentInUse: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSCurrentInUse: Currently in used firewall connection statistics.
             :type FWCSCurrentInUse: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSHigh: High level of firewall connection statistics.
             :type FWCSHigh: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSHigh: High level of firewall connection statistics.
             :type FWCSHigh: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param fwIndex: The current index of the local interface of firewall.
             :type fwIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fwIndex: The current index of the local interface of firewall.
             :type fwIndex: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the firewall connection statistics with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the firewall connection statistics with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of firewall connection statistic methods. The listed methods will be called on each firewall connection statistic returned and included in the output. Available methods are: device.
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
            |  ``default:`` FWCSID

             :param sort: The data field(s) to use for sorting the output. Default is FWCSID. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex.
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

             :param select: The list of attributes to return for each FirewallConnectionStatistic. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against firewall connection statistics, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, EndTime, FWCSCurrentInUse, FWCSHigh, FWCSID, StartTime, fwIndex.
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

             :return firewall_connection_statistics: An array of the FirewallConnectionStatistic objects that match the specified input criteria.
             :rtype firewall_connection_statistics: Array of FirewallConnectionStatistic

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available firewall connection statistics matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, EndTime, FWCSCurrentInUse, FWCSHigh, FWCSID, StartTime, fwIndex.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which firewall connection statistics information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_EndTime: The operator to apply to the field EndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndTime: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndTime: If op_EndTime is specified, the field named in this input will be compared to the value in EndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndTime must be specified if op_EndTime is specified.
             :type val_f_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndTime: If op_EndTime is specified, this value will be compared to the value in EndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndTime must be specified if op_EndTime is specified.
             :type val_c_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FWCSCurrentInUse: The operator to apply to the field FWCSCurrentInUse. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FWCSCurrentInUse: Currently in used firewall connection statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FWCSCurrentInUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FWCSCurrentInUse: If op_FWCSCurrentInUse is specified, the field named in this input will be compared to the value in FWCSCurrentInUse using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FWCSCurrentInUse must be specified if op_FWCSCurrentInUse is specified.
             :type val_f_FWCSCurrentInUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FWCSCurrentInUse: If op_FWCSCurrentInUse is specified, this value will be compared to the value in FWCSCurrentInUse using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FWCSCurrentInUse must be specified if op_FWCSCurrentInUse is specified.
             :type val_c_FWCSCurrentInUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FWCSHigh: The operator to apply to the field FWCSHigh. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FWCSHigh: High level of firewall connection statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FWCSHigh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FWCSHigh: If op_FWCSHigh is specified, the field named in this input will be compared to the value in FWCSHigh using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FWCSHigh must be specified if op_FWCSHigh is specified.
             :type val_f_FWCSHigh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FWCSHigh: If op_FWCSHigh is specified, this value will be compared to the value in FWCSHigh using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FWCSHigh must be specified if op_FWCSHigh is specified.
             :type val_c_FWCSHigh: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FWCSID: The operator to apply to the field FWCSID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FWCSID: The internal NetMRI identifier for this firewall connection statistics entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FWCSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FWCSID: If op_FWCSID is specified, the field named in this input will be compared to the value in FWCSID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FWCSID must be specified if op_FWCSID is specified.
             :type val_f_FWCSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FWCSID: If op_FWCSID is specified, this value will be compared to the value in FWCSID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FWCSID must be specified if op_FWCSID is specified.
             :type val_c_FWCSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_fwIndex: The operator to apply to the field fwIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. fwIndex: The current index of the local interface of firewall. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_fwIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_fwIndex: If op_fwIndex is specified, the field named in this input will be compared to the value in fwIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_fwIndex must be specified if op_fwIndex is specified.
             :type val_f_fwIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_fwIndex: If op_fwIndex is specified, this value will be compared to the value in fwIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_fwIndex must be specified if op_fwIndex is specified.
             :type val_c_fwIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the firewall connection statistics with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the firewall connection statistics with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of firewall connection statistic methods. The listed methods will be called on each firewall connection statistic returned and included in the output. Available methods are: device.
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
            |  ``default:`` FWCSID

             :param sort: The data field(s) to use for sorting the output. Default is FWCSID. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex.
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

             :param select: The list of attributes to return for each FirewallConnectionStatistic. Valid values are FWCSID, DeviceID, StartTime, EndTime, FWCSCurrentInUse, FWCSHigh, DataSourceID, fwIndex. If empty or omitted, all attributes will be returned.
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

             :return firewall_connection_statistics: An array of the FirewallConnectionStatistic objects that match the specified input criteria.
             :rtype firewall_connection_statistics: Array of FirewallConnectionStatistic

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

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

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param FWCSID: The internal NetMRI identifier for this firewall connection statistics entry.
             :type FWCSID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
