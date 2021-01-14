from ..broker import Broker


class AuthServiceBroker(Broker):
    controller = "auth_services"

    def show(self, **kwargs):
        """Shows the details for the specified auth service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the authentication service.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_service: The auth service identified by the specified id.
             :rtype auth_service: AuthService

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available auth services. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the authentication service.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthService. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return auth_services: An array of the AuthService objects that match the specified input criteria.
             :rtype auth_services: Array of AuthService

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available auth services matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_method: The Authentication method of the service. One of (local, radius, tacacs, ldap, activedirectory).
             :type auth_method: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param context_params_json: Additional specific authentication method parameters are stored in this field using a json format. (such as 'base_dn' for LDAP method, Vendor Specific Attribute ID for Radius,...).
             :type context_params_json: Array of String

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

             :param description: Description/comment about this authentication service
             :type description: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_authz_ind: A flag indicating whether this service is used for computing privileges for the remote users.
             :type enabled_authz_ind: Array of Boolean

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_ind: A flag indicating whether the authentication service settings is enabled or disabled.
             :type enabled_ind: Array of Boolean

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the authentication service.
             :type id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param priority: The priority assigned to this Authentication Service.
             :type priority: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param service_name: The name of the Authentication Service.
             :type service_name: Array of String

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timeout: The timeout interval of the service authentication servers.
             :type timeout: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthService. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against auth services, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: auth_method, context_params_json, created_at, description, enabled_authz_ind, enabled_ind, id, priority, service_name, timeout, updated_at.
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

             :return auth_services: An array of the AuthService objects that match the specified input criteria.
             :rtype auth_services: Array of AuthService

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available auth services matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: auth_method, context_params_json, created_at, description, enabled_authz_ind, enabled_ind, id, priority, service_name, timeout, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_method: The operator to apply to the field auth_method. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_method: The Authentication method of the service. One of (local, radius, tacacs, ldap, activedirectory). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_method: If op_auth_method is specified, the field named in this input will be compared to the value in auth_method using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_method must be specified if op_auth_method is specified.
             :type val_f_auth_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_method: If op_auth_method is specified, this value will be compared to the value in auth_method using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_method must be specified if op_auth_method is specified.
             :type val_c_auth_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_context_params_json: The operator to apply to the field context_params_json. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. context_params_json: Additional specific authentication method parameters are stored in this field using a json format. (such as 'base_dn' for LDAP method, Vendor Specific Attribute ID for Radius,...). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_context_params_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_context_params_json: If op_context_params_json is specified, the field named in this input will be compared to the value in context_params_json using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_context_params_json must be specified if op_context_params_json is specified.
             :type val_f_context_params_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_context_params_json: If op_context_params_json is specified, this value will be compared to the value in context_params_json using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_context_params_json must be specified if op_context_params_json is specified.
             :type val_c_context_params_json: String

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

             :param op_description: The operator to apply to the field description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. description: Description/comment about this authentication service For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_enabled_authz_ind: The operator to apply to the field enabled_authz_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. enabled_authz_ind: A flag indicating whether this service is used for computing privileges for the remote users. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_enabled_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_enabled_authz_ind: If op_enabled_authz_ind is specified, the field named in this input will be compared to the value in enabled_authz_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_enabled_authz_ind must be specified if op_enabled_authz_ind is specified.
             :type val_f_enabled_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_enabled_authz_ind: If op_enabled_authz_ind is specified, this value will be compared to the value in enabled_authz_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_enabled_authz_ind must be specified if op_enabled_authz_ind is specified.
             :type val_c_enabled_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_enabled_ind: The operator to apply to the field enabled_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. enabled_ind: A flag indicating whether the authentication service settings is enabled or disabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_enabled_ind: If op_enabled_ind is specified, the field named in this input will be compared to the value in enabled_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_enabled_ind must be specified if op_enabled_ind is specified.
             :type val_f_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_enabled_ind: If op_enabled_ind is specified, this value will be compared to the value in enabled_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_enabled_ind must be specified if op_enabled_ind is specified.
             :type val_c_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The id of the authentication service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_priority: The operator to apply to the field priority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. priority: The priority assigned to this Authentication Service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_priority: If op_priority is specified, the field named in this input will be compared to the value in priority using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_priority must be specified if op_priority is specified.
             :type val_f_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_priority: If op_priority is specified, this value will be compared to the value in priority using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_priority must be specified if op_priority is specified.
             :type val_c_priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_service_name: The operator to apply to the field service_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. service_name: The name of the Authentication Service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_service_name: If op_service_name is specified, the field named in this input will be compared to the value in service_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_service_name must be specified if op_service_name is specified.
             :type val_f_service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_service_name: If op_service_name is specified, this value will be compared to the value in service_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_service_name must be specified if op_service_name is specified.
             :type val_c_service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_timeout: The operator to apply to the field timeout. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. timeout: The timeout interval of the service authentication servers. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_timeout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_timeout: If op_timeout is specified, the field named in this input will be compared to the value in timeout using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_timeout must be specified if op_timeout is specified.
             :type val_f_timeout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_timeout: If op_timeout is specified, this value will be compared to the value in timeout using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_timeout must be specified if op_timeout is specified.
             :type val_c_timeout: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthService. Valid values are id, service_name, auth_method, description, priority, context_params_json, enabled_ind, enabled_authz_ind, timeout, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return auth_services: An array of the AuthService objects that match the specified input criteria.
             :rtype auth_services: Array of AuthService

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified auth service from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the authentication service.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Create a new Authentication Service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param service_name: The name of the authentication service, must be unique
             :type service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param auth_method: The authentication method of the service. One of (local, radius, tacacs, ldap, activedirectory).
             :type auth_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param priority: The priority assigned to this authentication service
             :type priority: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Description/comment about this authentication service
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param enabled_ind: A flag indicating whether the authentication service settings is enabled or disabled
             :type enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param enabled_authz_ind: A flag indicating whether this service is used for computing privileges for the remote users
             :type enabled_authz_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 5

             :param timeout: The timeout interval of the service authentication servers
             :type timeout: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_domain: Authentication Active Directory Domain name or LDAP BaseDN to use for search. (required for LDAP & Active Directory methods)
             :type auth_domain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` cn

             :param user_attr: User attribute ID for LDAP authentication method (required for LDAP methods).
             :type user_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` memberOf

             :param group_attr: Group membership attribute ID for LDAP authentication method. The LDAP server has to be configured to use memberOf Overlay.
             :type group_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param auth_type: A flag indicating whether the search request to the LDAP server is performed anonymously or needs authentication using a privileged bind User and Password. (values: 'true' for Authenticated, 'false' for anonymous')
             :type auth_type: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param bind_user: The bind User complete 'dn' in case LDAP Authenticated connection is needed to request search to find user
             :type bind_user: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param bind_passwd: The bind User password in case LDAP Authenticated connection is needed to request search to find user
             :type bind_passwd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` subtree

             :param search_scope: Specify the scope of the LDAP search.<br>
       - 'base': Search only the base object.<br>       - 'one': Search the entries immediately below the base object.<br>       - 'subtree': Search the whole tree below (and including) the base object. This is the default.
             :type search_scope: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` infoblox

             :param tacacs_service: The name of the defined custom service for Infoblox.<br>        group = GR_1{<br>            service = infoblox { na-group-info = MY_GROUP_1 }<br>        }
             :type tacacs_service: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` na-group-info

             :param tacacs_group_attr: The name of the group attribute defined in the Tacacs+ server to retrieve the user's groups list.<br>        group = GR_1{<br>            service = infoblox { na-group-info = MY_GROUP_1 }<br>        }
             :type tacacs_group_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 7779

             :param radius_vendor_id: The Infoblox Vendor ID defined in the radius dictionary.<br>        VENDOR infoblox 7779
             :type radius_vendor_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 10

             :param radius_vsa_id: The Vendor Specific Attribute ID as defined in the radius server dictionary to retrieve the user's groups list.<br>        ATTRIBUTE       na-group-info          10    string   infoblox
             :type radius_vsa_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_id: The new authentication service id.
             :rtype service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_name: The new authentication service name.
             :rtype service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_description: The new authentication service description.
             :rtype service_description: String

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Update an existing Authentication Service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the authentication service to modify
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param service_name: The name of the authentication service, must be unique
             :type service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_method: The authentication method of the service. One of (local, radius, tacacs, ldap, activedirectory).
             :type auth_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param priority: The priority assigned to this authentication service
             :type priority: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: Description/comment of this authentication service
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_ind: A flag indicating whether the authentication service settings is enabled or disabled
             :type enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_authz_ind: A flag indicating whether this service is used for computing privileges for the remote users
             :type enabled_authz_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timeout: The timeout interval of the service authentication servers
             :type timeout: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_domain: Authentication Active Directory Domain name or LDAP BaseDN to use for search. (required for LDAP & Active Directory methods)
             :type auth_domain: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_attr: User attribute ID for LDAP authentication method (required for LDAP methods).
             :type user_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param group_attr: Group membership attribute ID for LDAP authentication method. The LDAP server has to be configured to use memberOf Overlay.
             :type group_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_type: A flag indicating whether the search request to the LDAP server is performed anonymously or needs authentication using a privileged bind User and Password. (values: 'true' for Authenticated, 'false' for anonymous')
             :type auth_type: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param bind_user: The bind User complete 'dn' in case LDAP Authenticated connection is needed to request search to find user
             :type bind_user: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param bind_passwd: The bind User password in case LDAP Authenticated connection is needed to request search to find user
             :type bind_passwd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param search_scope: Specify the scope of the LDAP search.<br>
       - 'base': Search only the base object.<br>       - 'one': Search the entries immediately below the base object.<br>       - 'subtree': Search the whole tree below (and including) the base object. This is the default.
             :type search_scope: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tacacs_service: The name of the defined custom service for Infoblox.<br>        group = GR_1{<br>            service = infoblox { na-group-info = MY_GROUP_1 }<br>        }
             :type tacacs_service: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param tacacs_group_attr: The name of the group attribute defined in the Tacacs+ server to retrieve the user's groups list.<br>        group = GR_1{<br>            service = infoblox { na-group-info = MY_GROUP_1 }<br>        }
             :type tacacs_group_attr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param radius_vendor_id: The Infoblox Vendor ID defined in the radius dictionary.<br>        VENDOR infoblox 7779
             :type radius_vendor_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param radius_vsa_id: The Vendor Specific Attribute ID as defined in the radius server dictionary to retrieve the user's groups list.<br>        ATTRIBUTE       na-group-info          10    string   infoblox
             :type radius_vsa_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_id: The new authentication service id.
             :rtype service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_name: The new authentication service name.
             :rtype service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_description: The new authentication service description.
             :rtype service_description: String

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def duplicate(self, **kwargs):
        """Duplicate an authentication service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the authentication service.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_id: The new authentication service id.
             :rtype service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_name: The new authentication service name.
             :rtype service_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return service_description: The new authentication service description.
             :rtype service_description: String

            """

        return self.api_request(self._get_method_fullname("duplicate"), kwargs)

    def auth_servers(self, **kwargs):
        """List all servers defined for the requested Authentication Service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the authentication service to list the servers for
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("auth_servers"), kwargs)

    def auth_test_creds(self, **kwargs):
        """Test credentials for this service Authentication Servers that are stored in db.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param service_id: The id of the authentication service to test
             :type service_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: The login of the user to test
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: The password of the user to test
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param nohtml: Convert output to simple text
             :type nohtml: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the session output file to display.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param read: Offset in bytes from the start of the file.
             :type read: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the session output file.
             :rtype id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return read: Offset in bytes from the start of the file, to be used in the next auth_test_creds call, in order to retrieve the next lines of the output.
             :rtype read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return output: Result of the credential test.
             :rtype output: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the remaining output data to dump:
        <br><dd> 0: if the dump of the credential test output is completed.
        <br><dd> 1: if there is still output data to dump.
             :rtype status: Integer

            """

        return self.api_request(self._get_method_fullname("auth_test_creds"), kwargs)
