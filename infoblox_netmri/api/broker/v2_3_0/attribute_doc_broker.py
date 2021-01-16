from ..broker import Broker


class AttributeDocBroker(Broker):
    controller = "attribute_docs"

    def show(self, **kwargs):
        """Shows the details for the specified attribute doc.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this attribute.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return attribute_doc: The attribute doc identified by the specified id.
             :rtype attribute_doc: AttributeDoc

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available attribute docs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this attribute.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this attribute.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list.
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

             :param select: The list of attributes to return for each AttributeDoc. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list. If empty or omitted, all attributes will be returned.
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

             :return attribute_docs: An array of the AttributeDoc objects that match the specified input criteria.
             :rtype attribute_docs: Array of AttributeDoc

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available attribute docs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param attribute: Attribute name for this record.
             :type attribute: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param attribute: Attribute name for this record.
             :type attribute: Array of String

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param default_column_ind: A flag indicating if this is default column/
             :type default_column_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param default_column_ind: A flag indicating if this is default column/
             :type default_column_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param default_sort_desc_ind: A flag indicating if default sort order is descending.
             :type default_sort_desc_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param default_sort_desc_ind: A flag indicating if default sort order is descending.
             :type default_sort_desc_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param description: Attribute description
             :type description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Attribute description
             :type description: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param gui_type: Data type used in GUI to handle the attribute.
             :type gui_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param gui_type: Data type used in GUI to handle the attribute.
             :type gui_type: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param hidden_ind: A flag indicating if attribute is hidden
             :type hidden_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param hidden_ind: A flag indicating if attribute is hidden
             :type hidden_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this attribute.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this attribute.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param method_ind: A flag indicating if attribute is method
             :type method_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param method_ind: A flag indicating if attribute is method
             :type method_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param method_param_list: Parameter list for method
             :type method_param_list: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param method_param_list: Parameter list for method
             :type method_param_list: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param model_doc_id: The internal NetMRI identifier of Model the attribute is assigned to.
             :type model_doc_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param model_doc_id: The internal NetMRI identifier of Model the attribute is assigned to.
             :type model_doc_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: Human readable attribute name.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: Human readable attribute name.
             :type name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param return_model_doc_id: The internal NetMRI identifier of Model returned by method.
             :type return_model_doc_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param return_model_doc_id: The internal NetMRI identifier of Model returned by method.
             :type return_model_doc_id: Array of Integer

            |  ``api version min:`` 2.3
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list.
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

             :param select: The list of attributes to return for each AttributeDoc. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against attribute docs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: attribute, created_at, default_column_ind, default_sort_desc_ind, description, gui_type, hidden_ind, id, method_ind, method_param_list, model_doc_id, name, return_model_doc_id, updated_at.
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

             :return attribute_docs: An array of the AttributeDoc objects that match the specified input criteria.
             :rtype attribute_docs: Array of AttributeDoc

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available attribute docs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: attribute, created_at, default_column_ind, default_sort_desc_ind, description, gui_type, hidden_ind, id, method_ind, method_param_list, model_doc_id, name, return_model_doc_id, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_attribute: The operator to apply to the field attribute. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. attribute: Attribute name for this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_attribute: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_attribute: If op_attribute is specified, the field named in this input will be compared to the value in attribute using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_attribute must be specified if op_attribute is specified.
             :type val_f_attribute: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_attribute: If op_attribute is specified, this value will be compared to the value in attribute using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_attribute must be specified if op_attribute is specified.
             :type val_c_attribute: String

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

             :param op_default_column_ind: The operator to apply to the field default_column_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. default_column_ind: A flag indicating if this is default column/ For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_default_column_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_default_column_ind: If op_default_column_ind is specified, the field named in this input will be compared to the value in default_column_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_default_column_ind must be specified if op_default_column_ind is specified.
             :type val_f_default_column_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_default_column_ind: If op_default_column_ind is specified, this value will be compared to the value in default_column_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_default_column_ind must be specified if op_default_column_ind is specified.
             :type val_c_default_column_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_default_sort_desc_ind: The operator to apply to the field default_sort_desc_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. default_sort_desc_ind: A flag indicating if default sort order is descending. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_default_sort_desc_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_default_sort_desc_ind: If op_default_sort_desc_ind is specified, the field named in this input will be compared to the value in default_sort_desc_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_default_sort_desc_ind must be specified if op_default_sort_desc_ind is specified.
             :type val_f_default_sort_desc_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_default_sort_desc_ind: If op_default_sort_desc_ind is specified, this value will be compared to the value in default_sort_desc_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_default_sort_desc_ind must be specified if op_default_sort_desc_ind is specified.
             :type val_c_default_sort_desc_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: Attribute description For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_gui_type: The operator to apply to the field gui_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. gui_type: Data type used in GUI to handle the attribute. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_gui_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_gui_type: If op_gui_type is specified, the field named in this input will be compared to the value in gui_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_gui_type must be specified if op_gui_type is specified.
             :type val_f_gui_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_gui_type: If op_gui_type is specified, this value will be compared to the value in gui_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_gui_type must be specified if op_gui_type is specified.
             :type val_c_gui_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_hidden_ind: The operator to apply to the field hidden_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. hidden_ind: A flag indicating if attribute is hidden For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this attribute. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_method_ind: The operator to apply to the field method_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. method_ind: A flag indicating if attribute is method For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_method_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_method_ind: If op_method_ind is specified, the field named in this input will be compared to the value in method_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_method_ind must be specified if op_method_ind is specified.
             :type val_f_method_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_method_ind: If op_method_ind is specified, this value will be compared to the value in method_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_method_ind must be specified if op_method_ind is specified.
             :type val_c_method_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_method_param_list: The operator to apply to the field method_param_list. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. method_param_list: Parameter list for method For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_method_param_list: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_method_param_list: If op_method_param_list is specified, the field named in this input will be compared to the value in method_param_list using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_method_param_list must be specified if op_method_param_list is specified.
             :type val_f_method_param_list: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_method_param_list: If op_method_param_list is specified, this value will be compared to the value in method_param_list using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_method_param_list must be specified if op_method_param_list is specified.
             :type val_c_method_param_list: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_model_doc_id: The operator to apply to the field model_doc_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. model_doc_id: The internal NetMRI identifier of Model the attribute is assigned to. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_model_doc_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_model_doc_id: If op_model_doc_id is specified, the field named in this input will be compared to the value in model_doc_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_model_doc_id must be specified if op_model_doc_id is specified.
             :type val_f_model_doc_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_model_doc_id: If op_model_doc_id is specified, this value will be compared to the value in model_doc_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_model_doc_id must be specified if op_model_doc_id is specified.
             :type val_c_model_doc_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: Human readable attribute name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_return_model_doc_id: The operator to apply to the field return_model_doc_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. return_model_doc_id: The internal NetMRI identifier of Model returned by method. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_return_model_doc_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_return_model_doc_id: If op_return_model_doc_id is specified, the field named in this input will be compared to the value in return_model_doc_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_return_model_doc_id must be specified if op_return_model_doc_id is specified.
             :type val_f_return_model_doc_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_return_model_doc_id: If op_return_model_doc_id is specified, this value will be compared to the value in return_model_doc_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_return_model_doc_id must be specified if op_return_model_doc_id is specified.
             :type val_c_return_model_doc_id: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list.
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

             :param select: The list of attributes to return for each AttributeDoc. Valid values are id, model_doc_id, attribute, description, created_at, updated_at, gui_type, method_ind, hidden_ind, name, default_sort_desc_ind, default_column_ind, return_model_doc_id, method_param_list. If empty or omitted, all attributes will be returned.
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

             :return attribute_docs: An array of the AttributeDoc objects that match the specified input criteria.
             :rtype attribute_docs: Array of AttributeDoc

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
