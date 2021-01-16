from ..broker import Broker


class GuiStateBroker(Broker):
    controller = "gui_states"

    def show(self, **kwargs):
        """Shows the details for the specified gui state.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the gui state.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return gui_state: The gui state identified by the specified id.
             :rtype gui_state: GuiState

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available gui states. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, object_name, view_name, auth_user_id, object_state, created_at, updated_at, shared, desc, default.
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

             :param select: The list of attributes to return for each GuiState. Valid values are id, object_name, view_name, auth_user_id, object_state, created_at, updated_at, shared, desc, default. If empty or omitted, all attributes will be returned.
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

             :return gui_states: An array of the GuiState objects that match the specified input criteria.
             :rtype gui_states: Array of GuiState

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def find(self, **kwargs):
        """Lists the available gui states matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: auth_user_id, created_at, default, desc, id, object_name, object_state, shared, updated_at, view_name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_user_id: The operator to apply to the field auth_user_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_user_id: No description is available for auth_user_id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_user_id: If op_auth_user_id is specified, the field named in this input will be compared to the value in auth_user_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_user_id must be specified if op_auth_user_id is specified.
             :type val_f_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_user_id: If op_auth_user_id is specified, this value will be compared to the value in auth_user_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_user_id must be specified if op_auth_user_id is specified.
             :type val_c_auth_user_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: No description is available for created_at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_default: The operator to apply to the field default. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. default: No description is available for default. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_default: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_default: If op_default is specified, the field named in this input will be compared to the value in default using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_default must be specified if op_default is specified.
             :type val_f_default: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_default: If op_default is specified, this value will be compared to the value in default using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_default must be specified if op_default is specified.
             :type val_c_default: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_desc: The operator to apply to the field desc. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. desc: No description is available for desc. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_desc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_desc: If op_desc is specified, the field named in this input will be compared to the value in desc using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_desc must be specified if op_desc is specified.
             :type val_f_desc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_desc: If op_desc is specified, this value will be compared to the value in desc using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_desc must be specified if op_desc is specified.
             :type val_c_desc: String

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

             :param op_object_name: The operator to apply to the field object_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. object_name: No description is available for object_name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_object_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_object_name: If op_object_name is specified, the field named in this input will be compared to the value in object_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_object_name must be specified if op_object_name is specified.
             :type val_f_object_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_object_name: If op_object_name is specified, this value will be compared to the value in object_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_object_name must be specified if op_object_name is specified.
             :type val_c_object_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_object_state: The operator to apply to the field object_state. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. object_state: No description is available for object_state. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_object_state: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_object_state: If op_object_state is specified, the field named in this input will be compared to the value in object_state using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_object_state must be specified if op_object_state is specified.
             :type val_f_object_state: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_object_state: If op_object_state is specified, this value will be compared to the value in object_state using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_object_state must be specified if op_object_state is specified.
             :type val_c_object_state: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_shared: The operator to apply to the field shared. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. shared: No description is available for shared. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_shared: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_shared: If op_shared is specified, the field named in this input will be compared to the value in shared using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_shared must be specified if op_shared is specified.
             :type val_f_shared: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_shared: If op_shared is specified, this value will be compared to the value in shared using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_shared must be specified if op_shared is specified.
             :type val_c_shared: String

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

             :param op_view_name: The operator to apply to the field view_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. view_name: No description is available for view_name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_view_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_view_name: If op_view_name is specified, the field named in this input will be compared to the value in view_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_view_name must be specified if op_view_name is specified.
             :type val_f_view_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_view_name: If op_view_name is specified, this value will be compared to the value in view_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_view_name must be specified if op_view_name is specified.
             :type val_c_view_name: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, object_name, view_name, auth_user_id, object_state, created_at, updated_at, shared, desc, default.
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

             :param select: The list of attributes to return for each GuiState. Valid values are id, object_name, view_name, auth_user_id, object_state, created_at, updated_at, shared, desc, default. If empty or omitted, all attributes will be returned.
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

             :return gui_states: An array of the GuiState objects that match the specified input criteria.
             :rtype gui_states: Array of GuiState

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def default(self, **kwargs):
        """Get default view

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_name: Internal identifier of a grid
             :type object_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("default"), kwargs)

    def create(self, **kwargs):
        """Create view

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_name: Internal identifier of a grid
             :type object_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param view_name: Name
             :type view_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param desc: Description
             :type desc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param set_default: Set this view as default for the grid
             :type set_default: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param shared: Make this view accessible to other users
             :type shared: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_state: Configuration of the grid
             :type object_state: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Update existing view

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Internal identifier of grid view
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param view_name: Name
             :type view_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param desc: Description
             :type desc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param set_default: Set this view as default for the grid
             :type set_default: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param shared: Make this view accessible to other users
             :type shared: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param object_state: Configuration of the grid
             :type object_state: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def delete(self, **kwargs):
        """Delete gui state

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Internal identifier of gui state
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)
