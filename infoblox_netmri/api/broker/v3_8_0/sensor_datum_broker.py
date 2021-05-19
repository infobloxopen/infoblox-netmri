from ..broker import Broker


class SensorDatumBroker(Broker):
    controller = "sensor_data"

    def index(self, **kwargs):
        """Lists the available sensor data. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param data_source_id: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type data_source_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param data_source_id: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type data_source_id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the table entry.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the table entry.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen.
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

             :param select: The list of attributes to return for each SensorDatum. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen. If empty or omitted, all attributes will be returned.
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

             :return sensor_data: An array of the SensorDatum objects that match the specified input criteria.
             :rtype sensor_data: Array of SensorDatum

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available sensor data matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param category: The type of sensor data.
             :type category: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: The type of sensor data.
             :type category: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param data_source_id: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type data_source_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param data_source_id: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type data_source_id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param details: The description of the status of the sensor data.
             :type details: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param details: The description of the status of the sensor data.
             :type details: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param first_seen: The time when the failure was first detected.
             :type first_seen: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_seen: The time when the failure was first detected.
             :type first_seen: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the table entry.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the table entry.
             :type id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param label: The label for the sensor data.
             :type label: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param label: The label for the sensor data.
             :type label: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the sensor data.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the sensor data.
             :type name: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name_index: The index for all data with a given name.
             :type name_index: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name_index: The index for all data with a given name.
             :type name_index: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param status: The status of the sensor data.
             :type status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: The status of the sensor data.
             :type status: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param units: The units the value of the sensor data is in.
             :type units: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param units: The units the value of the sensor data is in.
             :type units: Array of String

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

             :param value: The value of the sensor data.
             :type value: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param value: The value of the sensor data.
             :type value: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen.
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

             :param select: The list of attributes to return for each SensorDatum. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against sensor data, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: category, data_source_id, details, first_seen, id, label, name, name_index, status, units, updated_at, value.
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

             :return sensor_data: An array of the SensorDatum objects that match the specified input criteria.
             :rtype sensor_data: Array of SensorDatum

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available sensor data matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: category, data_source_id, details, first_seen, id, label, name, name_index, status, units, updated_at, value.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: The type of sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_data_source_id: The operator to apply to the field data_source_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. data_source_id: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_data_source_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_data_source_id: If op_data_source_id is specified, the field named in this input will be compared to the value in data_source_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_data_source_id must be specified if op_data_source_id is specified.
             :type val_f_data_source_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_data_source_id: If op_data_source_id is specified, this value will be compared to the value in data_source_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_data_source_id must be specified if op_data_source_id is specified.
             :type val_c_data_source_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_details: The operator to apply to the field details. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. details: The description of the status of the sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_details: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_details: If op_details is specified, the field named in this input will be compared to the value in details using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_details must be specified if op_details is specified.
             :type val_f_details: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_details: If op_details is specified, this value will be compared to the value in details using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_details must be specified if op_details is specified.
             :type val_c_details: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_first_seen: The operator to apply to the field first_seen. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. first_seen: The time when the failure was first detected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_first_seen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_first_seen: If op_first_seen is specified, the field named in this input will be compared to the value in first_seen using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_first_seen must be specified if op_first_seen is specified.
             :type val_f_first_seen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_first_seen: If op_first_seen is specified, this value will be compared to the value in first_seen using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_first_seen must be specified if op_first_seen is specified.
             :type val_c_first_seen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_label: The operator to apply to the field label. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. label: The label for the sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_label: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_label: If op_label is specified, the field named in this input will be compared to the value in label using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_label must be specified if op_label is specified.
             :type val_f_label: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_label: If op_label is specified, this value will be compared to the value in label using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_label must be specified if op_label is specified.
             :type val_c_label: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of the sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_name: If op_name is specified, the field named in this input will be compared to the value in name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_name must be specified if op_name is specified.
             :type val_f_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_name: If op_name is specified, this value will be compared to the value in name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_name must be specified if op_name is specified.
             :type val_c_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name_index: The operator to apply to the field name_index. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name_index: The index for all data with a given name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_name_index: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_name_index: If op_name_index is specified, the field named in this input will be compared to the value in name_index using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_name_index must be specified if op_name_index is specified.
             :type val_f_name_index: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_name_index: If op_name_index is specified, this value will be compared to the value in name_index using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_name_index must be specified if op_name_index is specified.
             :type val_c_name_index: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_status: The operator to apply to the field status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. status: The status of the sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_units: The operator to apply to the field units. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. units: The units the value of the sensor data is in. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_units: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_units: If op_units is specified, the field named in this input will be compared to the value in units using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_units must be specified if op_units is specified.
             :type val_f_units: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_units: If op_units is specified, this value will be compared to the value in units using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_units must be specified if op_units is specified.
             :type val_c_units: String

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

             :param op_value: The operator to apply to the field value. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. value: The value of the sensor data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_value: If op_value is specified, the field named in this input will be compared to the value in value using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_value must be specified if op_value is specified.
             :type val_f_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_value: If op_value is specified, this value will be compared to the value in value using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_value must be specified if op_value is specified.
             :type val_c_value: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen.
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

             :param select: The list of attributes to return for each SensorDatum. Valid values are id, data_source_id, name, name_index, label, category, value, status, units, details, updated_at, first_seen. If empty or omitted, all attributes will be returned.
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

             :return sensor_data: An array of the SensorDatum objects that match the specified input criteria.
             :rtype sensor_data: Array of SensorDatum

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified sensor datum.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the table entry.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sensor_datum: The sensor datum identified by the specified id.
             :rtype sensor_datum: SensorDatum

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def failures(self, **kwargs):
        """List of sensor data which indicates an error condition.

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sensor_data: An array of the SensorDataum objects with a failure condition.
             :rtype sensor_data: Array of SensorDatum

            """

        return self.api_request(self._get_method_fullname("failures"), kwargs)

    def raid(self, **kwargs):
        """Summary of the status of the RAID as a whole.

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The most serious RAID status condition.
             :rtype status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detail: Detail on the status condition.
             :rtype detail: String

            """

        return self.api_request(self._get_method_fullname("raid"), kwargs)

    def fan(self, **kwargs):
        """Status for individual fans.

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return statuses: List of status for each fan, either OK or Failed.
             :rtype statuses: Array of String

            """

        return self.api_request(self._get_method_fullname("fan"), kwargs)

    def power_supply(self, **kwargs):
        """Status for the power supplies

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return statuses: List of status for each power supply, eitehr OK or Failed.
             :rtype statuses: Array of String

            """

        return self.api_request(self._get_method_fullname("power_supply"), kwargs)
