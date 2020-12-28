from ..broker import Broker


class SystemHealthSummaryBroker(Broker):
    controller = "system_health_summaries"

    def show(self, **kwargs):
        """Shows the details for the specified system health summary.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the system health summary.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of system health summary methods. The listed methods will be called on each system health summary returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return system_health_summary: The system health summary identified by the specified id.
             :rtype system_health_summary: SystemHealthSummary

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available system health summaries. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of system health summary methods. The listed methods will be called on each system health summary returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory.
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

             :param select: The list of attributes to return for each SystemHealthSummary. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory. If empty or omitted, all attributes will be returned.
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

             :return system_health_summaries: An array of the SystemHealthSummary objects that match the specified input criteria.
             :rtype system_health_summaries: Array of SystemHealthSummary

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available system health summaries matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: No description is available for category.
             :type category: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param datasource_id: No description is available for datasource_id.
             :type datasource_id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param diagnostic: No description is available for diagnostic.
             :type diagnostic: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param entry_type: No description is available for entry_type.
             :type entry_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message: No description is available for message.
             :type message: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message_code: No description is available for message_code.
             :type message_code: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param silenceable_ind: No description is available for silenceable_ind.
             :type silenceable_ind: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param silenced_ind: No description is available for silenced_ind.
             :type silenced_ind: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: No description is available for status.
             :type status: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param subcategory: No description is available for subcategory.
             :type subcategory: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: No description is available for timestamp.
             :type timestamp: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: No description is available for updated_at.
             :type updated_at: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param visibility: No description is available for visibility.
             :type visibility: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of system health summary methods. The listed methods will be called on each system health summary returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory.
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

             :param select: The list of attributes to return for each SystemHealthSummary. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against system health summaries, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: category, datasource_id, diagnostic, entry_type, id, message, message_code, silenceable_ind, silenced_ind, status, subcategory, timestamp, updated_at, visibility.
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

             :return system_health_summaries: An array of the SystemHealthSummary objects that match the specified input criteria.
             :rtype system_health_summaries: Array of SystemHealthSummary

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available system health summaries matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: category, datasource_id, diagnostic, entry_type, id, message, message_code, silenceable_ind, silenced_ind, status, subcategory, timestamp, updated_at, visibility.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: No description is available for category. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_category: If op_category is specified, the field named in this input will be compared to the value in category using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_category must be specified if op_category is specified.
             :type val_f_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_category: If op_category is specified, this value will be compared to the value in category using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_category must be specified if op_category is specified.
             :type val_c_category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_datasource_id: The operator to apply to the field datasource_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. datasource_id: No description is available for datasource_id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_datasource_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_datasource_id: If op_datasource_id is specified, the field named in this input will be compared to the value in datasource_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_datasource_id must be specified if op_datasource_id is specified.
             :type val_f_datasource_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_datasource_id: If op_datasource_id is specified, this value will be compared to the value in datasource_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_datasource_id must be specified if op_datasource_id is specified.
             :type val_c_datasource_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_diagnostic: The operator to apply to the field diagnostic. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. diagnostic: No description is available for diagnostic. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_diagnostic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_diagnostic: If op_diagnostic is specified, the field named in this input will be compared to the value in diagnostic using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_diagnostic must be specified if op_diagnostic is specified.
             :type val_f_diagnostic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_diagnostic: If op_diagnostic is specified, this value will be compared to the value in diagnostic using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_diagnostic must be specified if op_diagnostic is specified.
             :type val_c_diagnostic: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_entry_type: The operator to apply to the field entry_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. entry_type: No description is available for entry_type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_entry_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_entry_type: If op_entry_type is specified, the field named in this input will be compared to the value in entry_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_entry_type must be specified if op_entry_type is specified.
             :type val_f_entry_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_entry_type: If op_entry_type is specified, this value will be compared to the value in entry_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_entry_type must be specified if op_entry_type is specified.
             :type val_c_entry_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: No description is available for id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_message: The operator to apply to the field message. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. message: No description is available for message. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_message: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_message: If op_message is specified, the field named in this input will be compared to the value in message using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_message must be specified if op_message is specified.
             :type val_f_message: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_message: If op_message is specified, this value will be compared to the value in message using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_message must be specified if op_message is specified.
             :type val_c_message: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_message_code: The operator to apply to the field message_code. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. message_code: No description is available for message_code. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_message_code: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_message_code: If op_message_code is specified, the field named in this input will be compared to the value in message_code using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_message_code must be specified if op_message_code is specified.
             :type val_f_message_code: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_message_code: If op_message_code is specified, this value will be compared to the value in message_code using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_message_code must be specified if op_message_code is specified.
             :type val_c_message_code: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_silenceable_ind: The operator to apply to the field silenceable_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. silenceable_ind: No description is available for silenceable_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_silenceable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_silenceable_ind: If op_silenceable_ind is specified, the field named in this input will be compared to the value in silenceable_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_silenceable_ind must be specified if op_silenceable_ind is specified.
             :type val_f_silenceable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_silenceable_ind: If op_silenceable_ind is specified, this value will be compared to the value in silenceable_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_silenceable_ind must be specified if op_silenceable_ind is specified.
             :type val_c_silenceable_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_silenced_ind: The operator to apply to the field silenced_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. silenced_ind: No description is available for silenced_ind. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_silenced_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_silenced_ind: If op_silenced_ind is specified, the field named in this input will be compared to the value in silenced_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_silenced_ind must be specified if op_silenced_ind is specified.
             :type val_f_silenced_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_silenced_ind: If op_silenced_ind is specified, this value will be compared to the value in silenced_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_silenced_ind must be specified if op_silenced_ind is specified.
             :type val_c_silenced_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: No description is available for status. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_status: If op_status is specified, the field named in this input will be compared to the value in status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_status must be specified if op_status is specified.
             :type val_f_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_status: If op_status is specified, this value will be compared to the value in status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_status must be specified if op_status is specified.
             :type val_c_status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_subcategory: The operator to apply to the field subcategory. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. subcategory: No description is available for subcategory. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_subcategory: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_subcategory: If op_subcategory is specified, the field named in this input will be compared to the value in subcategory using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_subcategory must be specified if op_subcategory is specified.
             :type val_f_subcategory: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_subcategory: If op_subcategory is specified, this value will be compared to the value in subcategory using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_subcategory must be specified if op_subcategory is specified.
             :type val_c_subcategory: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_timestamp: The operator to apply to the field timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. timestamp: No description is available for timestamp. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_timestamp: If op_timestamp is specified, the field named in this input will be compared to the value in timestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_timestamp must be specified if op_timestamp is specified.
             :type val_f_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_timestamp: If op_timestamp is specified, this value will be compared to the value in timestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_timestamp must be specified if op_timestamp is specified.
             :type val_c_timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: No description is available for updated_at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_visibility: The operator to apply to the field visibility. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. visibility: No description is available for visibility. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_visibility: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_visibility: If op_visibility is specified, the field named in this input will be compared to the value in visibility using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_visibility must be specified if op_visibility is specified.
             :type val_f_visibility: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_visibility: If op_visibility is specified, this value will be compared to the value in visibility using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_visibility must be specified if op_visibility is specified.
             :type val_c_visibility: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of system health summary methods. The listed methods will be called on each system health summary returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory.
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

             :param select: The list of attributes to return for each SystemHealthSummary. Valid values are id, datasource_id, timestamp, category, diagnostic, status, entry_type, visibility, message_code, message, silenceable_ind, silenced_ind, updated_at, subcategory. If empty or omitted, all attributes will be returned.
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

             :return system_health_summaries: An array of the SystemHealthSummary objects that match the specified input criteria.
             :rtype system_health_summaries: Array of SystemHealthSummary

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def tree(self, **kwargs):
        """Get tree of health statuses

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: Search string
             :type query: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("tree"), kwargs)

    def storage_data(self, **kwargs):
        """Available disk space data for 2 last weeks

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param datasource_id: Datasource ID
             :type datasource_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("storage_data"), kwargs)

    def silence(self, **kwargs):
        """Silence/Unsilence warnings

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Id of warning
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("silence"), kwargs)

    def overall_system_health(self, **kwargs):
        """Delivers a one-line summary of system health.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param include_silenced_ind: Indicates whether to include IDs that have been silenced by the user.
             :type include_silenced_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param include_closed_ind: Indicates whether to include IDs that have been hidden for the user's session.
             :type include_closed_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("overall_system_health"), kwargs)

    def hide_overall_system_health_bar(self, **kwargs):
        """Hides the system health status bar for the current unhealthy IDs.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("hide_overall_system_health_bar"), kwargs)

    def license_issue_summary(self, **kwargs):
        """Delivers a one-line summary of platform limit issues.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param include_closed_ind: Indicates whether to include IDs that have been hidden for the user's session.
             :type include_closed_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("license_issue_summary"), kwargs)

    def hide_license_issue_bar(self, **kwargs):
        """Hides the platform limit issue bar for the current issue IDs.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("hide_license_issue_bar"), kwargs)
