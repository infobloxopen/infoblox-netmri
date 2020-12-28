from ..broker import Broker


class AuthServerBroker(Broker):
    controller = "auth_servers"

    def show(self, **kwargs):
        """Shows the details for the specified auth server.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The authentication server identifier.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_server: The auth server identified by the specified id.
             :rtype auth_server: AuthServer

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available auth servers. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the authentication service, this server is member of.
             :type auth_service_id: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The authentication server identifier.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version.
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

             :param select: The list of attributes to return for each AuthServer. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version. If empty or omitted, all attributes will be returned.
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

             :return auth_servers: An array of the AuthServer objects that match the specified input criteria.
             :rtype auth_servers: Array of AuthServer

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available auth servers matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_cert: The SSL certificate of an Authentication Server. (Required for Active Directory method).
             :type auth_cert: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_encryption: The Encryption method (none or SSL) (required for Active Directory method).
             :type auth_encryption: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_port: Authentication Port (required for Active Directory method).
             :type auth_port: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_protocol: The password exchange protocol to use for authentication. One of (PAP, CHAP)
             :type auth_protocol: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_server: Authentication Server Name (required for Radius, Tacacs, LDAP and Active Directory methods).
             :type auth_server: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the authentication service, this server is member of.
             :type auth_service_id: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_shared_secret: The shared secret of an authentication server (required for Radius and Tacacs methods).
             :type auth_shared_secret: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_version: The version use for the authentication (LDAP).
             :type auth_version: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enabled_ind: A flag indicating whether the authentication server settings is enabled or disabled.
             :type enabled_ind: Array of Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The authentication server identifier.
             :type id: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param priority: Priority assigned to an authentication server.
             :type priority: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secure_version: Internal encrypt version used for any auth_shared_secret
             :type secure_version: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_interface_id: The NetMRI interface to use as source of the packets sent to the authentication server.
             :type source_interface_id: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version.
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

             :param select: The list of attributes to return for each AuthServer. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against auth servers, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: auth_cert, auth_encryption, auth_port, auth_protocol, auth_server, auth_service_id, auth_shared_secret, auth_version, created_at, enabled_ind, id, priority, secure_version, source_interface_id, updated_at.
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

             :return auth_servers: An array of the AuthServer objects that match the specified input criteria.
             :rtype auth_servers: Array of AuthServer

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available auth servers matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: auth_cert, auth_encryption, auth_port, auth_protocol, auth_server, auth_service_id, auth_shared_secret, auth_version, created_at, enabled_ind, id, priority, secure_version, source_interface_id, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_cert: The operator to apply to the field auth_cert. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_cert: The SSL certificate of an Authentication Server. (Required for Active Directory method). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_cert: If op_auth_cert is specified, the field named in this input will be compared to the value in auth_cert using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_cert must be specified if op_auth_cert is specified.
             :type val_f_auth_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_cert: If op_auth_cert is specified, this value will be compared to the value in auth_cert using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_cert must be specified if op_auth_cert is specified.
             :type val_c_auth_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_encryption: The operator to apply to the field auth_encryption. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_encryption: The Encryption method (none or SSL) (required for Active Directory method). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_encryption: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_encryption: If op_auth_encryption is specified, the field named in this input will be compared to the value in auth_encryption using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_encryption must be specified if op_auth_encryption is specified.
             :type val_f_auth_encryption: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_encryption: If op_auth_encryption is specified, this value will be compared to the value in auth_encryption using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_encryption must be specified if op_auth_encryption is specified.
             :type val_c_auth_encryption: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_port: The operator to apply to the field auth_port. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_port: Authentication Port (required for Active Directory method). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_port: If op_auth_port is specified, the field named in this input will be compared to the value in auth_port using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_port must be specified if op_auth_port is specified.
             :type val_f_auth_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_port: If op_auth_port is specified, this value will be compared to the value in auth_port using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_port must be specified if op_auth_port is specified.
             :type val_c_auth_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_protocol: The operator to apply to the field auth_protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_protocol: The password exchange protocol to use for authentication. One of (PAP, CHAP) For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_protocol: If op_auth_protocol is specified, the field named in this input will be compared to the value in auth_protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_protocol must be specified if op_auth_protocol is specified.
             :type val_f_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_protocol: If op_auth_protocol is specified, this value will be compared to the value in auth_protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_protocol must be specified if op_auth_protocol is specified.
             :type val_c_auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_server: The operator to apply to the field auth_server. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_server: Authentication Server Name (required for Radius, Tacacs, LDAP and Active Directory methods). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_server: If op_auth_server is specified, the field named in this input will be compared to the value in auth_server using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_server must be specified if op_auth_server is specified.
             :type val_f_auth_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_server: If op_auth_server is specified, this value will be compared to the value in auth_server using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_server must be specified if op_auth_server is specified.
             :type val_c_auth_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_service_id: The operator to apply to the field auth_service_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_service_id: The id of the authentication service, this server is member of. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_service_id: If op_auth_service_id is specified, the field named in this input will be compared to the value in auth_service_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_service_id must be specified if op_auth_service_id is specified.
             :type val_f_auth_service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_service_id: If op_auth_service_id is specified, this value will be compared to the value in auth_service_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_service_id must be specified if op_auth_service_id is specified.
             :type val_c_auth_service_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_shared_secret: The operator to apply to the field auth_shared_secret. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_shared_secret: The shared secret of an authentication server (required for Radius and Tacacs methods). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_shared_secret: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_shared_secret: If op_auth_shared_secret is specified, the field named in this input will be compared to the value in auth_shared_secret using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_shared_secret must be specified if op_auth_shared_secret is specified.
             :type val_f_auth_shared_secret: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_shared_secret: If op_auth_shared_secret is specified, this value will be compared to the value in auth_shared_secret using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_shared_secret must be specified if op_auth_shared_secret is specified.
             :type val_c_auth_shared_secret: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_version: The operator to apply to the field auth_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_version: The version use for the authentication (LDAP). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_version: If op_auth_version is specified, the field named in this input will be compared to the value in auth_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_version must be specified if op_auth_version is specified.
             :type val_f_auth_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_version: If op_auth_version is specified, this value will be compared to the value in auth_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_version must be specified if op_auth_version is specified.
             :type val_c_auth_version: String

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

             :param op_enabled_ind: The operator to apply to the field enabled_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. enabled_ind: A flag indicating whether the authentication server settings is enabled or disabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The authentication server identifier. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_priority: The operator to apply to the field priority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. priority: Priority assigned to an authentication server. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_secure_version: The operator to apply to the field secure_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. secure_version: Internal encrypt version used for any auth_shared_secret For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_secure_version: If op_secure_version is specified, the field named in this input will be compared to the value in secure_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_secure_version must be specified if op_secure_version is specified.
             :type val_f_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_secure_version: If op_secure_version is specified, this value will be compared to the value in secure_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_secure_version must be specified if op_secure_version is specified.
             :type val_c_secure_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_source_interface_id: The operator to apply to the field source_interface_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. source_interface_id: The NetMRI interface to use as source of the packets sent to the authentication server. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_source_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_source_interface_id: If op_source_interface_id is specified, the field named in this input will be compared to the value in source_interface_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_source_interface_id must be specified if op_source_interface_id is specified.
             :type val_f_source_interface_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_source_interface_id: If op_source_interface_id is specified, this value will be compared to the value in source_interface_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_source_interface_id must be specified if op_source_interface_id is specified.
             :type val_c_source_interface_id: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version.
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

             :param select: The list of attributes to return for each AuthServer. Valid values are id, priority, enabled_ind, auth_server, auth_port, auth_shared_secret, auth_encryption, auth_cert, created_at, updated_at, secure_version, auth_service_id, auth_protocol, source_interface_id, auth_version. If empty or omitted, all attributes will be returned.
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

             :return auth_servers: An array of the AuthServer objects that match the specified input criteria.
             :rtype auth_servers: Array of AuthServer

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing auth server.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The authentication server identifier.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_cert: The SSL certificate of an Authentication Server. (Required for Active Directory method). If omitted, this field will not be updated.
             :type auth_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_encryption: The Encryption method (none or SSL) (required for Active Directory method). If omitted, this field will not be updated.
             :type auth_encryption: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_port: Authentication Port (required for Active Directory method). If omitted, this field will not be updated.
             :type auth_port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_protocol: The password exchange protocol to use for authentication. One of (PAP, CHAP) If omitted, this field will not be updated.
             :type auth_protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_server: Authentication Server Name (required for Radius, Tacacs, LDAP and Active Directory methods). If omitted, this field will not be updated.
             :type auth_server: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the authentication service, this server is member of. If omitted, this field will not be updated.
             :type auth_service_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_shared_secret: The shared secret of an authentication server (required for Radius and Tacacs methods). If omitted, this field will not be updated.
             :type auth_shared_secret: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_version: The version use for the authentication (LDAP). If omitted, this field will not be updated.
             :type auth_version: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param enabled_ind: A flag indicating whether the authentication server settings is enabled or disabled. If omitted, this field will be updated to the default value.
             :type enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param priority: Priority assigned to an authentication server. If omitted, this field will not be updated.
             :type priority: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param source_interface_id: The NetMRI interface to use as source of the packets sent to the authentication server. If omitted, this field will not be updated.
             :type source_interface_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated auth server.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated auth server.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated auth server.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_server: The updated auth server.
             :rtype auth_server: AuthServer

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified auth server from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The authentication server identifier.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)
