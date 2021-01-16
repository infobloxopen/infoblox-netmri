from ..broker import Broker


class ChangeTraceBroker(Broker):
    controller = "change_traces"

    def show(self, **kwargs):
        """Shows the details for the specified change trace.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of change trace methods. The listed methods will be called on each change trace returned and included in the output. Available methods are: data_source, detected_change.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, detected_change.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return change_trace: The change trace identified by the specified ChangeTraceID.
             :rtype change_trace: ChangeTrace

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available change traces. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for the change associated with this change trace.
             :type ChangeID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for the change associated with this change trace.
             :type ChangeID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceTime: The date/time that this change trace was identified by NetMRI.
             :type ChangeTraceTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceTime: The date/time that this change trace was identified by NetMRI.
             :type ChangeTraceTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceUser: The user name of the user whose actions generated this change trace, if available.
             :type ChangeTraceUser: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceUser: The user name of the user whose actions generated this change trace, if available.
             :type ChangeTraceUser: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the change traces with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the change traces with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of change trace methods. The listed methods will be called on each change trace returned and included in the output. Available methods are: data_source, detected_change.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, detected_change.
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
            |  ``default:`` ChangeTraceID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeTraceID. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex.
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

             :param select: The list of attributes to return for each ChangeTrace. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex. If empty or omitted, all attributes will be returned.
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

             :return change_traces: An array of the ChangeTrace objects that match the specified input criteria.
             :rtype change_traces: Array of ChangeTrace

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available change traces matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for the change associated with this change trace.
             :type ChangeID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for the change associated with this change trace.
             :type ChangeID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceDesc: A description of the change trace.
             :type ChangeTraceDesc: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceDesc: A description of the change trace.
             :type ChangeTraceDesc: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceMethod: The method through which this change trace was identified.
             :type ChangeTraceMethod: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceMethod: The method through which this change trace was identified.
             :type ChangeTraceMethod: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceTime: The date/time that this change trace was identified by NetMRI.
             :type ChangeTraceTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceTime: The date/time that this change trace was identified by NetMRI.
             :type ChangeTraceTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceType: The type of change trace (Hardware, Software, Admin, or External).
             :type ChangeTraceType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceType: The type of change trace (Hardware, Software, Admin, or External).
             :type ChangeTraceType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceUser: The user name of the user whose actions generated this change trace, if available.
             :type ChangeTraceUser: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceUser: The user name of the user whose actions generated this change trace, if available.
             :type ChangeTraceUser: Array of String

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: Currently unused.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: Currently unused.
             :type ifIndex: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the change traces with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the change traces with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of change trace methods. The listed methods will be called on each change trace returned and included in the output. Available methods are: data_source, detected_change.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, detected_change.
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
            |  ``default:`` ChangeTraceID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeTraceID. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex.
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

             :param select: The list of attributes to return for each ChangeTrace. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against change traces, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ChangeID, ChangeTraceDesc, ChangeTraceID, ChangeTraceMethod, ChangeTraceTime, ChangeTraceType, ChangeTraceUser, DataSourceID, ifIndex.
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

             :return change_traces: An array of the ChangeTrace objects that match the specified input criteria.
             :rtype change_traces: Array of ChangeTrace

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available change traces matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ChangeID, ChangeTraceDesc, ChangeTraceID, ChangeTraceMethod, ChangeTraceTime, ChangeTraceType, ChangeTraceUser, DataSourceID, ifIndex.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeID: The operator to apply to the field ChangeID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeID: The internal NetMRI identifier for the change associated with this change trace. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeID: If op_ChangeID is specified, the field named in this input will be compared to the value in ChangeID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeID must be specified if op_ChangeID is specified.
             :type val_f_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeID: If op_ChangeID is specified, this value will be compared to the value in ChangeID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeID must be specified if op_ChangeID is specified.
             :type val_c_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceDesc: The operator to apply to the field ChangeTraceDesc. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceDesc: A description of the change trace. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceDesc: If op_ChangeTraceDesc is specified, the field named in this input will be compared to the value in ChangeTraceDesc using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceDesc must be specified if op_ChangeTraceDesc is specified.
             :type val_f_ChangeTraceDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceDesc: If op_ChangeTraceDesc is specified, this value will be compared to the value in ChangeTraceDesc using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceDesc must be specified if op_ChangeTraceDesc is specified.
             :type val_c_ChangeTraceDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceID: The operator to apply to the field ChangeTraceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceID: The internal NetMRI identifier for this change trace. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceID: If op_ChangeTraceID is specified, the field named in this input will be compared to the value in ChangeTraceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceID must be specified if op_ChangeTraceID is specified.
             :type val_f_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceID: If op_ChangeTraceID is specified, this value will be compared to the value in ChangeTraceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceID must be specified if op_ChangeTraceID is specified.
             :type val_c_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceMethod: The operator to apply to the field ChangeTraceMethod. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceMethod: The method through which this change trace was identified. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceMethod: If op_ChangeTraceMethod is specified, the field named in this input will be compared to the value in ChangeTraceMethod using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceMethod must be specified if op_ChangeTraceMethod is specified.
             :type val_f_ChangeTraceMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceMethod: If op_ChangeTraceMethod is specified, this value will be compared to the value in ChangeTraceMethod using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceMethod must be specified if op_ChangeTraceMethod is specified.
             :type val_c_ChangeTraceMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceTime: The operator to apply to the field ChangeTraceTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceTime: The date/time that this change trace was identified by NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceTime: If op_ChangeTraceTime is specified, the field named in this input will be compared to the value in ChangeTraceTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceTime must be specified if op_ChangeTraceTime is specified.
             :type val_f_ChangeTraceTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceTime: If op_ChangeTraceTime is specified, this value will be compared to the value in ChangeTraceTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceTime must be specified if op_ChangeTraceTime is specified.
             :type val_c_ChangeTraceTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceType: The operator to apply to the field ChangeTraceType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceType: The type of change trace (Hardware, Software, Admin, or External). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceType: If op_ChangeTraceType is specified, the field named in this input will be compared to the value in ChangeTraceType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceType must be specified if op_ChangeTraceType is specified.
             :type val_f_ChangeTraceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceType: If op_ChangeTraceType is specified, this value will be compared to the value in ChangeTraceType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceType must be specified if op_ChangeTraceType is specified.
             :type val_c_ChangeTraceType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceUser: The operator to apply to the field ChangeTraceUser. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceUser: The user name of the user whose actions generated this change trace, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceUser: If op_ChangeTraceUser is specified, the field named in this input will be compared to the value in ChangeTraceUser using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceUser must be specified if op_ChangeTraceUser is specified.
             :type val_f_ChangeTraceUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceUser: If op_ChangeTraceUser is specified, this value will be compared to the value in ChangeTraceUser using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceUser must be specified if op_ChangeTraceUser is specified.
             :type val_c_ChangeTraceUser: String

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

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: Currently unused. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the change traces with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the change traces with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of change trace methods. The listed methods will be called on each change trace returned and included in the output. Available methods are: data_source, detected_change.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, detected_change.
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
            |  ``default:`` ChangeTraceID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeTraceID. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex.
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

             :param select: The list of attributes to return for each ChangeTrace. Valid values are DataSourceID, ChangeTraceID, ChangeID, ChangeTraceTime, ChangeTraceUser, ChangeTraceType, ChangeTraceMethod, ChangeTraceDesc, ifIndex. If empty or omitted, all attributes will be returned.
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

             :return change_traces: An array of the ChangeTrace objects that match the specified input criteria.
             :rtype change_traces: Array of ChangeTrace

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def detected_change(self, **kwargs):
        """The DetectedChange object to which this change trace contributed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier for this change trace.
             :type ChangeTraceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The DetectedChange object to which this change trace contributed.
             :rtype : DetectedChange

            """

        return self.api_request(self._get_method_fullname("detected_change"), kwargs)
