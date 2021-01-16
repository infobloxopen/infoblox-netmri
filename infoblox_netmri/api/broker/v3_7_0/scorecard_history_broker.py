from ..broker import Broker


class ScorecardHistoryBroker(Broker):
    controller = "scorecard_histories"

    def index(self, **kwargs):
        """Lists the available scorecard histories. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: Array of DateTime

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
            |  ``default:`` Component

             :param sort: The data field(s) to use for sorting the output. Default is Component. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails.
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

             :param select: The list of attributes to return for each ScorecardHistory. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails. If empty or omitted, all attributes will be returned.
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

             :return scorecard_histories: An array of the ScorecardHistory objects that match the specified input criteria.
             :rtype scorecard_histories: Array of ScorecardHistory

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available scorecard histories matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this issue in the scorecard history.
             :type Correctness: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this issue in the scorecard history.
             :type Correctness: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Error: The error of the scorecard history.
             :type Error: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Error: The error of the scorecard history.
             :type Error: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ErrorDetails: The error details of the scorecard history.
             :type ErrorDetails: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ErrorDetails: The error details of the scorecard history.
             :type ErrorDetails: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Info: The information details of the scorecard history.
             :type Info: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Info: The information details of the scorecard history.
             :type Info: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InfoDetails: The information details of the scorecard history.
             :type InfoDetails: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InfoDetails: The information details of the scorecard history.
             :type InfoDetails: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this issue in the scorecard history.
             :type Stability: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this issue in the scorecard history.
             :type Stability: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Warn: The warning details of the scorecard history.
             :type Warn: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Warn: The warning details of the scorecard history.
             :type Warn: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WarnDetails: The warning details of the scorecard history.
             :type WarnDetails: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WarnDetails: The warning details of the scorecard history.
             :type WarnDetails: Array of String

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
            |  ``default:`` Component

             :param sort: The data field(s) to use for sorting the output. Default is Component. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails.
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

             :param select: The list of attributes to return for each ScorecardHistory. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against scorecard histories, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: Component, Correctness, Error, ErrorDetails, Info, InfoDetails, Stability, Timestamp, Warn, WarnDetails.
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

             :return scorecard_histories: An array of the ScorecardHistory objects that match the specified input criteria.
             :rtype scorecard_histories: Array of ScorecardHistory

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available scorecard histories matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: Component, Correctness, Error, ErrorDetails, Info, InfoDetails, Stability, Timestamp, Warn, WarnDetails.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Component: The operator to apply to the field Component. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Component: The issue component (Devices, Configuration, VLANs, etc.). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Component: If op_Component is specified, the field named in this input will be compared to the value in Component using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Component must be specified if op_Component is specified.
             :type val_f_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Component: If op_Component is specified, this value will be compared to the value in Component using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Component must be specified if op_Component is specified.
             :type val_c_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Correctness: The operator to apply to the field Correctness. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Correctness: The correctness contribution for this issue in the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Correctness: If op_Correctness is specified, the field named in this input will be compared to the value in Correctness using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Correctness must be specified if op_Correctness is specified.
             :type val_f_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Correctness: If op_Correctness is specified, this value will be compared to the value in Correctness using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Correctness must be specified if op_Correctness is specified.
             :type val_c_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Error: The operator to apply to the field Error. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Error: The error of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Error: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Error: If op_Error is specified, the field named in this input will be compared to the value in Error using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Error must be specified if op_Error is specified.
             :type val_f_Error: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Error: If op_Error is specified, this value will be compared to the value in Error using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Error must be specified if op_Error is specified.
             :type val_c_Error: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ErrorDetails: The operator to apply to the field ErrorDetails. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ErrorDetails: The error details of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ErrorDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ErrorDetails: If op_ErrorDetails is specified, the field named in this input will be compared to the value in ErrorDetails using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ErrorDetails must be specified if op_ErrorDetails is specified.
             :type val_f_ErrorDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ErrorDetails: If op_ErrorDetails is specified, this value will be compared to the value in ErrorDetails using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ErrorDetails must be specified if op_ErrorDetails is specified.
             :type val_c_ErrorDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Info: The operator to apply to the field Info. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Info: The information details of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Info: If op_Info is specified, the field named in this input will be compared to the value in Info using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Info must be specified if op_Info is specified.
             :type val_f_Info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Info: If op_Info is specified, this value will be compared to the value in Info using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Info must be specified if op_Info is specified.
             :type val_c_Info: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InfoDetails: The operator to apply to the field InfoDetails. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InfoDetails: The information details of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InfoDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InfoDetails: If op_InfoDetails is specified, the field named in this input will be compared to the value in InfoDetails using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InfoDetails must be specified if op_InfoDetails is specified.
             :type val_f_InfoDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InfoDetails: If op_InfoDetails is specified, this value will be compared to the value in InfoDetails using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InfoDetails must be specified if op_InfoDetails is specified.
             :type val_c_InfoDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Stability: The operator to apply to the field Stability. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Stability: The stability contribution for this issue in the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Stability: If op_Stability is specified, the field named in this input will be compared to the value in Stability using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Stability must be specified if op_Stability is specified.
             :type val_f_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Stability: If op_Stability is specified, this value will be compared to the value in Stability using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Stability must be specified if op_Stability is specified.
             :type val_c_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Timestamp: The operator to apply to the field Timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Timestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Timestamp: If op_Timestamp is specified, the field named in this input will be compared to the value in Timestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Timestamp must be specified if op_Timestamp is specified.
             :type val_f_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Timestamp: If op_Timestamp is specified, this value will be compared to the value in Timestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Timestamp must be specified if op_Timestamp is specified.
             :type val_c_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Warn: The operator to apply to the field Warn. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Warn: The warning details of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Warn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Warn: If op_Warn is specified, the field named in this input will be compared to the value in Warn using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Warn must be specified if op_Warn is specified.
             :type val_f_Warn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Warn: If op_Warn is specified, this value will be compared to the value in Warn using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Warn must be specified if op_Warn is specified.
             :type val_c_Warn: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WarnDetails: The operator to apply to the field WarnDetails. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WarnDetails: The warning details of the scorecard history. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WarnDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WarnDetails: If op_WarnDetails is specified, the field named in this input will be compared to the value in WarnDetails using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WarnDetails must be specified if op_WarnDetails is specified.
             :type val_f_WarnDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WarnDetails: If op_WarnDetails is specified, this value will be compared to the value in WarnDetails using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WarnDetails must be specified if op_WarnDetails is specified.
             :type val_c_WarnDetails: String

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
            |  ``default:`` Component

             :param sort: The data field(s) to use for sorting the output. Default is Component. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails.
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

             :param select: The list of attributes to return for each ScorecardHistory. Valid values are Component, Timestamp, Correctness, Stability, Info, Warn, Error, InfoDetails, WarnDetails, ErrorDetails. If empty or omitted, all attributes will be returned.
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

             :return scorecard_histories: An array of the ScorecardHistory objects that match the specified input criteria.
             :rtype scorecard_histories: Array of ScorecardHistory

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
