from ..broker import Broker


class AdvSettingDefBroker(Broker):
    controller = "adv_setting_defs"

    def show(self, **kwargs):
        """Shows the details for the specified adv setting def.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting definition.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return adv_setting_def: The adv setting def identified by the specified id.
             :rtype adv_setting_def: AdvSettingDef

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available adv setting defs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting definition.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting definition.
             :type id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this setting.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this setting.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name.
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

             :param select: The list of attributes to return for each AdvSettingDef. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name. If empty or omitted, all attributes will be returned.
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

             :return adv_setting_defs: An array of the AdvSettingDef objects that match the specified input criteria.
             :rtype adv_setting_defs: Array of AdvSettingDef

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available adv setting defs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param allow_empty: A flag indicating if this setting can be empty.
             :type allow_empty: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param allow_empty: A flag indicating if this setting can be empty.
             :type allow_empty: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param category: The category of this setting.
             :type category: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: The category of this setting.
             :type category: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param default_value: Default value for this setting.
             :type default_value: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param default_value: Default value for this setting.
             :type default_value: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param description: Description for this setting.
             :type description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Description for this setting.
             :type description: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param display_hints: Hints to display for this setting.
             :type display_hints: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param display_hints: Hints to display for this setting.
             :type display_hints: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param feature: The feature this setting definition is related to.
             :type feature: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param feature: The feature this setting definition is related to.
             :type feature: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting definition.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this setting definition.
             :type id: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this setting.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this setting.
             :type name: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param setting_type: The type of this setting.
             :type setting_type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param setting_type: The type of this setting.
             :type setting_type: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ui_name: The UI name of this setting.
             :type ui_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ui_name: The UI name of this setting.
             :type ui_name: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param visible: A flag indicating if this setting visible.
             :type visible: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param visible: A flag indicating if this setting visible.
             :type visible: Array of Boolean

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name.
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

             :param select: The list of attributes to return for each AdvSettingDef. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against adv setting defs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: allow_empty, category, default_value, description, display_hints, feature, id, name, setting_type, ui_name, visible.
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

             :return adv_setting_defs: An array of the AdvSettingDef objects that match the specified input criteria.
             :rtype adv_setting_defs: Array of AdvSettingDef

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available adv setting defs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: allow_empty, category, default_value, description, display_hints, feature, id, name, setting_type, ui_name, visible.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_allow_empty: The operator to apply to the field allow_empty. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. allow_empty: A flag indicating if this setting can be empty. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_allow_empty: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_allow_empty: If op_allow_empty is specified, the field named in this input will be compared to the value in allow_empty using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_allow_empty must be specified if op_allow_empty is specified.
             :type val_f_allow_empty: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_allow_empty: If op_allow_empty is specified, this value will be compared to the value in allow_empty using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_allow_empty must be specified if op_allow_empty is specified.
             :type val_c_allow_empty: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: The category of this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_default_value: The operator to apply to the field default_value. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. default_value: Default value for this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_default_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_default_value: If op_default_value is specified, the field named in this input will be compared to the value in default_value using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_default_value must be specified if op_default_value is specified.
             :type val_f_default_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_default_value: If op_default_value is specified, this value will be compared to the value in default_value using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_default_value must be specified if op_default_value is specified.
             :type val_c_default_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: Description for this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_display_hints: The operator to apply to the field display_hints. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. display_hints: Hints to display for this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_display_hints: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_display_hints: If op_display_hints is specified, the field named in this input will be compared to the value in display_hints using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_display_hints must be specified if op_display_hints is specified.
             :type val_f_display_hints: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_display_hints: If op_display_hints is specified, this value will be compared to the value in display_hints using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_display_hints must be specified if op_display_hints is specified.
             :type val_c_display_hints: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_feature: The operator to apply to the field feature. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. feature: The feature this setting definition is related to. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_feature: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_feature: If op_feature is specified, the field named in this input will be compared to the value in feature using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_feature must be specified if op_feature is specified.
             :type val_f_feature: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_feature: If op_feature is specified, this value will be compared to the value in feature using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_feature must be specified if op_feature is specified.
             :type val_c_feature: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this setting definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The name of this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_setting_type: The operator to apply to the field setting_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. setting_type: The type of this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_setting_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_setting_type: If op_setting_type is specified, the field named in this input will be compared to the value in setting_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_setting_type must be specified if op_setting_type is specified.
             :type val_f_setting_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_setting_type: If op_setting_type is specified, this value will be compared to the value in setting_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_setting_type must be specified if op_setting_type is specified.
             :type val_c_setting_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ui_name: The operator to apply to the field ui_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ui_name: The UI name of this setting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ui_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ui_name: If op_ui_name is specified, the field named in this input will be compared to the value in ui_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ui_name must be specified if op_ui_name is specified.
             :type val_f_ui_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ui_name: If op_ui_name is specified, this value will be compared to the value in ui_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ui_name must be specified if op_ui_name is specified.
             :type val_c_ui_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_visible: The operator to apply to the field visible. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. visible: A flag indicating if this setting visible. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_visible: If op_visible is specified, the field named in this input will be compared to the value in visible using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_visible must be specified if op_visible is specified.
             :type val_f_visible: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_visible: If op_visible is specified, this value will be compared to the value in visible using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_visible must be specified if op_visible is specified.
             :type val_c_visible: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name.
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

             :param select: The list of attributes to return for each AdvSettingDef. Valid values are id, name, setting_type, category, visible, description, default_value, allow_empty, feature, display_hints, ui_name. If empty or omitted, all attributes will be returned.
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

             :return adv_setting_defs: An array of the AdvSettingDef objects that match the specified input criteria.
             :rtype adv_setting_defs: Array of AdvSettingDef

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
