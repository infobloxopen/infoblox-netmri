from ..broker import Broker


class TimeWindowBroker(Broker):
    controller = "time_windows"

    def show(self, **kwargs):
        """Shows the details for the specified time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return time_window: The time window identified by the specified id.
             :rtype time_window: TimeWindow

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available time windows. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Array of Integer

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at.
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

             :param select: The list of attributes to return for each TimeWindow. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return time_windows: An array of the TimeWindow objects that match the specified input criteria.
             :rtype time_windows: Array of TimeWindow

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available time windows matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param end_date: The ending effective date of this record, or empty if still in effect.
             :type end_date: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_date: The ending effective date of this record, or empty if still in effect.
             :type end_date: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param end_min: The ending time of a time window.
             :type end_min: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_min: The ending time of a time window.
             :type end_min: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param fri_end: The end value of a Friday in time window.
             :type fri_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_end: The end value of a Friday in time window.
             :type fri_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param fri_start: The start value of a Friday in time window.
             :type fri_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_start: The start value of a Friday in time window.
             :type fri_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param interval: The time interval(minutes) of a time window.
             :type interval: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interval: The time interval(minutes) of a time window.
             :type interval: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param mon_end: The end value of a Monday in time window.
             :type mon_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_end: The end value of a Monday in time window.
             :type mon_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param mon_start: The start value of a Monday in time window.
             :type mon_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_start: The start value of a Monday in time window.
             :type mon_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ordinal: The ordinal number of a time window.
             :type ordinal: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ordinal: The ordinal number of a time window.
             :type ordinal: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param period_mins: The duration (specified in minutes) of a time window system.
             :type period_mins: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param period_mins: The duration (specified in minutes) of a time window system.
             :type period_mins: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param recur_type: The recurrence type of a time window.
             :type recur_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param recur_type: The recurrence type of a time window.
             :type recur_type: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param sat_end: The end value of a Saturday in time window.
             :type sat_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_end: The end value of a Saturday in time window.
             :type sat_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param sat_start: The start value of a Saturday in time window.
             :type sat_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_start: The start value of a Saturday in time window.
             :type sat_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_name: The schedule name of a time window.
             :type schedule_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_name: The schedule name of a time window.
             :type schedule_name: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param start_date: The starting effective date of this record.
             :type start_date: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_date: The starting effective date of this record.
             :type start_date: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param start_min: The starting time of a time window.
             :type start_min: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_min: The starting time of a time window.
             :type start_min: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param sun_end: The end value of a Sunday in time window.
             :type sun_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_end: The end value of a Sunday in time window.
             :type sun_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param sun_start: The start value of a Sunday in time window.
             :type sun_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_start: The start value of a Sunday in time window.
             :type sun_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param system_window_ind: A flag indicates whether a time zone is a system time window or not.
             :type system_window_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param system_window_ind: A flag indicates whether a time zone is a system time window or not.
             :type system_window_ind: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param thu_end: The end value of a Thursday in time window.
             :type thu_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_end: The end value of a Thursday in time window.
             :type thu_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param thu_start: The start value of a Thursday in time window.
             :type thu_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_start: The start value of a Thursday in time window.
             :type thu_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param time_zone: The time zone of a time window.
             :type time_zone: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param time_zone: The time zone of a time window.
             :type time_zone: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param tue_end: The end value of a Tuesday in a time window.
             :type tue_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_end: The end value of a Tuesday in a time window.
             :type tue_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param tue_start: The start value of a Tuesday in time window.
             :type tue_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_start: The start value of a Tuesday in time window.
             :type tue_start: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param wed_end: The end value of a Wednesday in a time window.
             :type wed_end: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_end: The end value of a Wednesday in a time window.
             :type wed_end: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param wed_start: The start value of a Wednesday in time window.
             :type wed_start: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_start: The start value of a Wednesday in time window.
             :type wed_start: Array of Integer

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at.
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

             :param select: The list of attributes to return for each TimeWindow. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against time windows, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: created_at, end_date, end_min, fri_end, fri_start, id, interval, mon_end, mon_start, ordinal, period_mins, recur_type, sat_end, sat_start, schedule_name, start_date, start_min, sun_end, sun_start, system_window_ind, thu_end, thu_start, time_zone, tue_end, tue_start, updated_at, wed_end, wed_start.
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

             :return time_windows: An array of the TimeWindow objects that match the specified input criteria.
             :rtype time_windows: Array of TimeWindow

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available time windows matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: created_at, end_date, end_min, fri_end, fri_start, id, interval, mon_end, mon_start, ordinal, period_mins, recur_type, sat_end, sat_start, schedule_name, start_date, start_min, sun_end, sun_start, system_window_ind, thu_end, thu_start, time_zone, tue_end, tue_start, updated_at, wed_end, wed_start.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_at: If op_created_at is specified, the field named in this input will be compared to the value in created_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_at must be specified if op_created_at is specified.
             :type val_f_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_at: If op_created_at is specified, this value will be compared to the value in created_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_at must be specified if op_created_at is specified.
             :type val_c_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_end_date: The operator to apply to the field end_date. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. end_date: The ending effective date of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_end_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_end_date: If op_end_date is specified, the field named in this input will be compared to the value in end_date using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_end_date must be specified if op_end_date is specified.
             :type val_f_end_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_end_date: If op_end_date is specified, this value will be compared to the value in end_date using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_end_date must be specified if op_end_date is specified.
             :type val_c_end_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_end_min: The operator to apply to the field end_min. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. end_min: The ending time of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_end_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_end_min: If op_end_min is specified, the field named in this input will be compared to the value in end_min using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_end_min must be specified if op_end_min is specified.
             :type val_f_end_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_end_min: If op_end_min is specified, this value will be compared to the value in end_min using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_end_min must be specified if op_end_min is specified.
             :type val_c_end_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_fri_end: The operator to apply to the field fri_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. fri_end: The end value of a Friday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_fri_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_fri_end: If op_fri_end is specified, the field named in this input will be compared to the value in fri_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_fri_end must be specified if op_fri_end is specified.
             :type val_f_fri_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_fri_end: If op_fri_end is specified, this value will be compared to the value in fri_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_fri_end must be specified if op_fri_end is specified.
             :type val_c_fri_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_fri_start: The operator to apply to the field fri_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. fri_start: The start value of a Friday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_fri_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_fri_start: If op_fri_start is specified, the field named in this input will be compared to the value in fri_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_fri_start must be specified if op_fri_start is specified.
             :type val_f_fri_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_fri_start: If op_fri_start is specified, this value will be compared to the value in fri_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_fri_start must be specified if op_fri_start is specified.
             :type val_c_fri_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_id: If op_id is specified, the field named in this input will be compared to the value in id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_id must be specified if op_id is specified.
             :type val_f_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_id: If op_id is specified, this value will be compared to the value in id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_id must be specified if op_id is specified.
             :type val_c_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_interval: The operator to apply to the field interval. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. interval: The time interval(minutes) of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_interval: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_interval: If op_interval is specified, the field named in this input will be compared to the value in interval using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_interval must be specified if op_interval is specified.
             :type val_f_interval: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_interval: If op_interval is specified, this value will be compared to the value in interval using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_interval must be specified if op_interval is specified.
             :type val_c_interval: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_mon_end: The operator to apply to the field mon_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. mon_end: The end value of a Monday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_mon_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_mon_end: If op_mon_end is specified, the field named in this input will be compared to the value in mon_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_mon_end must be specified if op_mon_end is specified.
             :type val_f_mon_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_mon_end: If op_mon_end is specified, this value will be compared to the value in mon_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_mon_end must be specified if op_mon_end is specified.
             :type val_c_mon_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_mon_start: The operator to apply to the field mon_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. mon_start: The start value of a Monday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_mon_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_mon_start: If op_mon_start is specified, the field named in this input will be compared to the value in mon_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_mon_start must be specified if op_mon_start is specified.
             :type val_f_mon_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_mon_start: If op_mon_start is specified, this value will be compared to the value in mon_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_mon_start must be specified if op_mon_start is specified.
             :type val_c_mon_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ordinal: The operator to apply to the field ordinal. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ordinal: The ordinal number of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ordinal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ordinal: If op_ordinal is specified, the field named in this input will be compared to the value in ordinal using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ordinal must be specified if op_ordinal is specified.
             :type val_f_ordinal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ordinal: If op_ordinal is specified, this value will be compared to the value in ordinal using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ordinal must be specified if op_ordinal is specified.
             :type val_c_ordinal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_period_mins: The operator to apply to the field period_mins. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. period_mins: The duration (specified in minutes) of a time window system. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_period_mins: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_period_mins: If op_period_mins is specified, the field named in this input will be compared to the value in period_mins using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_period_mins must be specified if op_period_mins is specified.
             :type val_f_period_mins: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_period_mins: If op_period_mins is specified, this value will be compared to the value in period_mins using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_period_mins must be specified if op_period_mins is specified.
             :type val_c_period_mins: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_recur_type: The operator to apply to the field recur_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. recur_type: The recurrence type of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_recur_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_recur_type: If op_recur_type is specified, the field named in this input will be compared to the value in recur_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_recur_type must be specified if op_recur_type is specified.
             :type val_f_recur_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_recur_type: If op_recur_type is specified, this value will be compared to the value in recur_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_recur_type must be specified if op_recur_type is specified.
             :type val_c_recur_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sat_end: The operator to apply to the field sat_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sat_end: The end value of a Saturday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sat_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sat_end: If op_sat_end is specified, the field named in this input will be compared to the value in sat_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sat_end must be specified if op_sat_end is specified.
             :type val_f_sat_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sat_end: If op_sat_end is specified, this value will be compared to the value in sat_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sat_end must be specified if op_sat_end is specified.
             :type val_c_sat_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sat_start: The operator to apply to the field sat_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sat_start: The start value of a Saturday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sat_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sat_start: If op_sat_start is specified, the field named in this input will be compared to the value in sat_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sat_start must be specified if op_sat_start is specified.
             :type val_f_sat_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sat_start: If op_sat_start is specified, this value will be compared to the value in sat_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sat_start must be specified if op_sat_start is specified.
             :type val_c_sat_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_schedule_name: The operator to apply to the field schedule_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. schedule_name: The schedule name of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_schedule_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_schedule_name: If op_schedule_name is specified, the field named in this input will be compared to the value in schedule_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_schedule_name must be specified if op_schedule_name is specified.
             :type val_f_schedule_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_schedule_name: If op_schedule_name is specified, this value will be compared to the value in schedule_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_schedule_name must be specified if op_schedule_name is specified.
             :type val_c_schedule_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_start_date: The operator to apply to the field start_date. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. start_date: The starting effective date of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_start_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_start_date: If op_start_date is specified, the field named in this input will be compared to the value in start_date using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_start_date must be specified if op_start_date is specified.
             :type val_f_start_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_start_date: If op_start_date is specified, this value will be compared to the value in start_date using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_start_date must be specified if op_start_date is specified.
             :type val_c_start_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_start_min: The operator to apply to the field start_min. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. start_min: The starting time of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_start_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_start_min: If op_start_min is specified, the field named in this input will be compared to the value in start_min using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_start_min must be specified if op_start_min is specified.
             :type val_f_start_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_start_min: If op_start_min is specified, this value will be compared to the value in start_min using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_start_min must be specified if op_start_min is specified.
             :type val_c_start_min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sun_end: The operator to apply to the field sun_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sun_end: The end value of a Sunday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sun_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sun_end: If op_sun_end is specified, the field named in this input will be compared to the value in sun_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sun_end must be specified if op_sun_end is specified.
             :type val_f_sun_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sun_end: If op_sun_end is specified, this value will be compared to the value in sun_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sun_end must be specified if op_sun_end is specified.
             :type val_c_sun_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_sun_start: The operator to apply to the field sun_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. sun_start: The start value of a Sunday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_sun_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_sun_start: If op_sun_start is specified, the field named in this input will be compared to the value in sun_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_sun_start must be specified if op_sun_start is specified.
             :type val_f_sun_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_sun_start: If op_sun_start is specified, this value will be compared to the value in sun_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_sun_start must be specified if op_sun_start is specified.
             :type val_c_sun_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_system_window_ind: The operator to apply to the field system_window_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. system_window_ind: A flag indicates whether a time zone is a system time window or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_system_window_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_system_window_ind: If op_system_window_ind is specified, the field named in this input will be compared to the value in system_window_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_system_window_ind must be specified if op_system_window_ind is specified.
             :type val_f_system_window_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_system_window_ind: If op_system_window_ind is specified, this value will be compared to the value in system_window_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_system_window_ind must be specified if op_system_window_ind is specified.
             :type val_c_system_window_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_thu_end: The operator to apply to the field thu_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. thu_end: The end value of a Thursday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_thu_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_thu_end: If op_thu_end is specified, the field named in this input will be compared to the value in thu_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_thu_end must be specified if op_thu_end is specified.
             :type val_f_thu_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_thu_end: If op_thu_end is specified, this value will be compared to the value in thu_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_thu_end must be specified if op_thu_end is specified.
             :type val_c_thu_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_thu_start: The operator to apply to the field thu_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. thu_start: The start value of a Thursday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_thu_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_thu_start: If op_thu_start is specified, the field named in this input will be compared to the value in thu_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_thu_start must be specified if op_thu_start is specified.
             :type val_f_thu_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_thu_start: If op_thu_start is specified, this value will be compared to the value in thu_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_thu_start must be specified if op_thu_start is specified.
             :type val_c_thu_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_time_zone: The operator to apply to the field time_zone. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. time_zone: The time zone of a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_time_zone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_time_zone: If op_time_zone is specified, the field named in this input will be compared to the value in time_zone using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_time_zone must be specified if op_time_zone is specified.
             :type val_f_time_zone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_time_zone: If op_time_zone is specified, this value will be compared to the value in time_zone using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_time_zone must be specified if op_time_zone is specified.
             :type val_c_time_zone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_tue_end: The operator to apply to the field tue_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. tue_end: The end value of a Tuesday in a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_tue_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_tue_end: If op_tue_end is specified, the field named in this input will be compared to the value in tue_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_tue_end must be specified if op_tue_end is specified.
             :type val_f_tue_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_tue_end: If op_tue_end is specified, this value will be compared to the value in tue_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_tue_end must be specified if op_tue_end is specified.
             :type val_c_tue_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_tue_start: The operator to apply to the field tue_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. tue_start: The start value of a Tuesday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_tue_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_tue_start: If op_tue_start is specified, the field named in this input will be compared to the value in tue_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_tue_start must be specified if op_tue_start is specified.
             :type val_f_tue_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_tue_start: If op_tue_start is specified, this value will be compared to the value in tue_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_tue_start must be specified if op_tue_start is specified.
             :type val_c_tue_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_at: If op_updated_at is specified, the field named in this input will be compared to the value in updated_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_at must be specified if op_updated_at is specified.
             :type val_f_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_at: If op_updated_at is specified, this value will be compared to the value in updated_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_at must be specified if op_updated_at is specified.
             :type val_c_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_wed_end: The operator to apply to the field wed_end. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. wed_end: The end value of a Wednesday in a time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_wed_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_wed_end: If op_wed_end is specified, the field named in this input will be compared to the value in wed_end using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_wed_end must be specified if op_wed_end is specified.
             :type val_f_wed_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_wed_end: If op_wed_end is specified, this value will be compared to the value in wed_end using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_wed_end must be specified if op_wed_end is specified.
             :type val_c_wed_end: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_wed_start: The operator to apply to the field wed_start. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. wed_start: The start value of a Wednesday in time window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_wed_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_wed_start: If op_wed_start is specified, the field named in this input will be compared to the value in wed_start using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_wed_start must be specified if op_wed_start is specified.
             :type val_f_wed_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_wed_start: If op_wed_start is specified, this value will be compared to the value in wed_start using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_wed_start must be specified if op_wed_start is specified.
             :type val_c_wed_start: String

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at.
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

             :param select: The list of attributes to return for each TimeWindow. Valid values are id, schedule_name, time_zone, system_window_ind, recur_type, start_date, end_date, interval, ordinal, period_mins, start_min, end_min, sun_start, sun_end, mon_start, mon_end, tue_start, tue_end, wed_start, wed_end, thu_start, thu_end, fri_start, fri_end, sat_start, sat_end, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return time_windows: An array of the TimeWindow objects that match the specified input criteria.
             :rtype time_windows: Array of TimeWindow

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a new time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param period_mins: The duration (specified in minutes) of a time window system.
             :type period_mins: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param time_zone: The time zone of a time window.
             :type time_zone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_name: The schedule name of a time window.
             :type schedule_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param system_window_ind: A flag indicates whether a time zone is a system time window or not.
             :type system_window_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param recur_type: The recurrence type of a time window.
             :type recur_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_date: The starting effective date of this record.
             :type start_date: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_date: The ending effective date of this record, or empty if still in effect.
             :type end_date: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interval: The time interval(minutes) of a time window.
             :type interval: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ordinal: The ordinal number of a time window.
             :type ordinal: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_min: The starting time of a time window.
             :type start_min: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_min: The ending time of a time window.
             :type end_min: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_start: The start value of a Sunday in time window.
             :type sun_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_end: The end value of a Sunday in time window.
             :type sun_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_start: The start value of a Monday in time window.
             :type mon_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_end: The end value of a Monday in time window.
             :type mon_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_start: The start value of a Tuesday in time window.
             :type tue_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_end: The end value of a Tuesday in a time window.
             :type tue_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_start: The start value of a Wednesday in time window.
             :type wed_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_end: The end value of a Wednesday in a time window.
             :type wed_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_start: The start value of a Thursday in time window.
             :type thu_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_end: The end value of a Thursday in time window.
             :type thu_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_start: The start value of a Friday in time window.
             :type fri_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_end: The end value of a Friday in time window.
             :type fri_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_start: The start value of a Saturday in time window.
             :type sat_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_end: The end value of a Saturday in time window.
             :type sat_end: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created time window.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created time window.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created time window.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return time_window: The newly created time window.
             :rtype time_window: TimeWindow

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param period_mins: The duration (specified in minutes) of a time window system. If omitted, this field will not be updated.
             :type period_mins: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param time_zone: The time zone of a time window. If omitted, this field will not be updated.
             :type time_zone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_name: The schedule name of a time window. If omitted, this field will not be updated.
             :type schedule_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param system_window_ind: A flag indicates whether a time zone is a system time window or not. If omitted, this field will not be updated.
             :type system_window_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param recur_type: The recurrence type of a time window. If omitted, this field will not be updated.
             :type recur_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_date: The starting effective date of this record. If omitted, this field will not be updated.
             :type start_date: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_date: The ending effective date of this record, or empty if still in effect. If omitted, this field will not be updated.
             :type end_date: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param interval: The time interval(minutes) of a time window. If omitted, this field will not be updated.
             :type interval: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ordinal: The ordinal number of a time window. If omitted, this field will not be updated.
             :type ordinal: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start_min: The starting time of a time window. If omitted, this field will not be updated.
             :type start_min: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param end_min: The ending time of a time window. If omitted, this field will not be updated.
             :type end_min: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_start: The start value of a Sunday in time window. If omitted, this field will not be updated.
             :type sun_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sun_end: The end value of a Sunday in time window. If omitted, this field will not be updated.
             :type sun_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_start: The start value of a Monday in time window. If omitted, this field will not be updated.
             :type mon_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mon_end: The end value of a Monday in time window. If omitted, this field will not be updated.
             :type mon_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_start: The start value of a Tuesday in time window. If omitted, this field will not be updated.
             :type tue_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tue_end: The end value of a Tuesday in a time window. If omitted, this field will not be updated.
             :type tue_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_start: The start value of a Wednesday in time window. If omitted, this field will not be updated.
             :type wed_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param wed_end: The end value of a Wednesday in a time window. If omitted, this field will not be updated.
             :type wed_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_start: The start value of a Thursday in time window. If omitted, this field will not be updated.
             :type thu_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thu_end: The end value of a Thursday in time window. If omitted, this field will not be updated.
             :type thu_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_start: The start value of a Friday in time window. If omitted, this field will not be updated.
             :type fri_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fri_end: The end value of a Friday in time window. If omitted, this field will not be updated.
             :type fri_end: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_start: The start value of a Saturday in time window. If omitted, this field will not be updated.
             :type sat_start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param sat_end: The end value of a Saturday in time window. If omitted, this field will not be updated.
             :type sat_end: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated time window.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated time window.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated time window.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return time_window: The updated time window.
             :rtype time_window: TimeWindow

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified time window from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of a time window.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def generate(self, **kwargs):
        """Generates DimTime entries for the specified time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the time window.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("generate"), kwargs)

    def enumerate(self, **kwargs):
        """Enumerate for the specified time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the time window.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 2020-11-27 08:21:47

             :param start_date: Starting date of the time period to enumerate.
             :type start_date: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 2020-12-27 08:21:47

             :param end_date: Ending date of the time period to enumerate.
             :type end_date: DateTime

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return time_window_entries: List the date/time entries for the specified time window.
             :rtype time_window_entries: Array of DateTime

            """

        return self.api_request(self._get_method_fullname("enumerate"), kwargs)

    def check(self, **kwargs):
        """Check whether given date/time exists in the specified time window.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the time window.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param timestamps: List of timestamps specified to check for their existence in the given time window .
             :type timestamps: Array

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return time_window: List the date/time entries for the specified time window.
             :rtype time_window: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return timestamps_in_window: Array of DateTime values in the TimeWindow.
             :rtype timestamps_in_window: Array

            """

        return self.api_request(self._get_method_fullname("check"), kwargs)
