from ..broker import Broker


class ReportBroker(Broker):
    controller = "reports"

    def index(self, **kwargs):
        """Lists the available reports. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the report
             :type id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the report
             :type name: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind.
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

             :param select: The list of attributes to return for each Report. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind. If empty or omitted, all attributes will be returned.
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

             :return reports: An array of the Report objects that match the specified input criteria.
             :rtype reports: Array of Report

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available reports matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category_id: Id of the report category
             :type category_id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Description of the report
             :type description: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param file_name: The file name where the report is defined
             :type file_name: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param hidden_ind: A flag indicating whether the report is hidden or not.
             :type hidden_ind: Array of Boolean

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the report
             :type id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param image_url: (always nil)
             :type image_url: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the report
             :type name: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param pre_packaged_ind: A flag indicating whether the report is prepackaged or not.
             :type pre_packaged_ind: Array of Boolean

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param report_type: The type of the report
             :type report_type: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param report_url: report url
             :type report_url: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param short_headings_ind: A flag indicating whether the report uses short headings or not.
             :type short_headings_ind: Array of Boolean

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param thumbnail_url: url of the report image displayed in the Reports &gt; Report Gallery view
             :type thumbnail_url: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind.
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

             :param select: The list of attributes to return for each Report. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against reports, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: category_id, created_at, description, file_name, hidden_ind, id, image_url, name, pre_packaged_ind, report_type, report_url, short_headings_ind, thumbnail_url, updated_at.
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

             :return reports: An array of the Report objects that match the specified input criteria.
             :rtype reports: Array of Report

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available reports matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: category_id, created_at, description, file_name, hidden_ind, id, image_url, name, pre_packaged_ind, report_type, report_url, short_headings_ind, thumbnail_url, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category_id: The operator to apply to the field category_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category_id: Id of the report category  For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_category_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_category_id: If op_category_id is specified, the field named in this input will be compared to the value in category_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_category_id must be specified if op_category_id is specified.
             :type val_f_category_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_category_id: If op_category_id is specified, this value will be compared to the value in category_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_category_id must be specified if op_category_id is specified.
             :type val_c_category_id: String

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

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: Description of the report For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_description: If op_description is specified, the field named in this input will be compared to the value in description using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_description must be specified if op_description is specified.
             :type val_f_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_description: If op_description is specified, this value will be compared to the value in description using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_description must be specified if op_description is specified.
             :type val_c_description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_file_name: The operator to apply to the field file_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. file_name: The file name where the report is defined For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_file_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_file_name: If op_file_name is specified, the field named in this input will be compared to the value in file_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_file_name must be specified if op_file_name is specified.
             :type val_f_file_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_file_name: If op_file_name is specified, this value will be compared to the value in file_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_file_name must be specified if op_file_name is specified.
             :type val_c_file_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_hidden_ind: The operator to apply to the field hidden_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. hidden_ind: A flag indicating whether the report is hidden or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_hidden_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_hidden_ind: If op_hidden_ind is specified, the field named in this input will be compared to the value in hidden_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_hidden_ind must be specified if op_hidden_ind is specified.
             :type val_f_hidden_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_hidden_ind: If op_hidden_ind is specified, this value will be compared to the value in hidden_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_hidden_ind must be specified if op_hidden_ind is specified.
             :type val_c_hidden_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The id of the report For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_image_url: The operator to apply to the field image_url. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. image_url: (always nil)  For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_image_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_image_url: If op_image_url is specified, the field named in this input will be compared to the value in image_url using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_image_url must be specified if op_image_url is specified.
             :type val_f_image_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_image_url: If op_image_url is specified, this value will be compared to the value in image_url using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_image_url must be specified if op_image_url is specified.
             :type val_c_image_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of the report For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_pre_packaged_ind: The operator to apply to the field pre_packaged_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. pre_packaged_ind: A flag indicating whether the report is prepackaged or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_pre_packaged_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_pre_packaged_ind: If op_pre_packaged_ind is specified, the field named in this input will be compared to the value in pre_packaged_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_pre_packaged_ind must be specified if op_pre_packaged_ind is specified.
             :type val_f_pre_packaged_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_pre_packaged_ind: If op_pre_packaged_ind is specified, this value will be compared to the value in pre_packaged_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_pre_packaged_ind must be specified if op_pre_packaged_ind is specified.
             :type val_c_pre_packaged_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_report_type: The operator to apply to the field report_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. report_type: The type of the report For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_report_type: If op_report_type is specified, the field named in this input will be compared to the value in report_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_report_type must be specified if op_report_type is specified.
             :type val_f_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_report_type: If op_report_type is specified, this value will be compared to the value in report_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_report_type must be specified if op_report_type is specified.
             :type val_c_report_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_report_url: The operator to apply to the field report_url. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. report_url: report url For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_report_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_report_url: If op_report_url is specified, the field named in this input will be compared to the value in report_url using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_report_url must be specified if op_report_url is specified.
             :type val_f_report_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_report_url: If op_report_url is specified, this value will be compared to the value in report_url using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_report_url must be specified if op_report_url is specified.
             :type val_c_report_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_short_headings_ind: The operator to apply to the field short_headings_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. short_headings_ind: A flag indicating whether the report uses short headings or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_short_headings_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_short_headings_ind: If op_short_headings_ind is specified, the field named in this input will be compared to the value in short_headings_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_short_headings_ind must be specified if op_short_headings_ind is specified.
             :type val_f_short_headings_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_short_headings_ind: If op_short_headings_ind is specified, this value will be compared to the value in short_headings_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_short_headings_ind must be specified if op_short_headings_ind is specified.
             :type val_c_short_headings_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_thumbnail_url: The operator to apply to the field thumbnail_url. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. thumbnail_url: url of the report image displayed in the Reports &gt; Report Gallery view For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_thumbnail_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_thumbnail_url: If op_thumbnail_url is specified, the field named in this input will be compared to the value in thumbnail_url using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_thumbnail_url must be specified if op_thumbnail_url is specified.
             :type val_f_thumbnail_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_thumbnail_url: If op_thumbnail_url is specified, this value will be compared to the value in thumbnail_url using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_thumbnail_url must be specified if op_thumbnail_url is specified.
             :type val_c_thumbnail_url: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind.
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

             :param select: The list of attributes to return for each Report. Valid values are id, name, file_name, description, category_id, thumbnail_url, image_url, report_url, created_at, updated_at, report_type, hidden_ind, pre_packaged_ind, short_headings_ind. If empty or omitted, all attributes will be returned.
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

             :return reports: An array of the Report objects that match the specified input criteria.
             :rtype reports: Array of Report

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified report.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the report
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return report: The report identified by the specified id.
             :rtype report: Report

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)
