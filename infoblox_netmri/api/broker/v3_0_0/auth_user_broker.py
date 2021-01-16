from ..broker import Broker


class AuthUserBroker(Broker):
    controller = "auth_users"

    def index(self, **kwargs):
        """Lists the available auth users. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure.
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

             :param select: The list of attributes to return for each AuthUser. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure. If empty or omitted, all attributes will be returned.
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

             :return auth_users: An array of the AuthUser objects that match the specified input criteria.
             :rtype auth_users: Array of AuthUser

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified auth user.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_user: The auth user identified by the specified id.
             :rtype auth_user: AuthUser

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available auth users matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param account_disabled: A flag indicating whether this user's account has been administratively disabled.
             :type account_disabled: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param account_disabled: A flag indicating whether this user's account has been administratively disabled.
             :type account_disabled: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param account_disabled_date: The date and time that the user's account was disabled.
             :type account_disabled_date: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param account_disabled_date: The date and time that the user's account was disabled.
             :type account_disabled_date: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param account_locked: A flag indicating whether or not this account is locked due to failed login attempts.
             :type account_locked: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param account_locked: A flag indicating whether or not this account is locked due to failed login attempts.
             :type account_locked: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param account_locked_date: The date and time that the user's account was locked.
             :type account_locked_date: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param account_locked_date: The date and time that the user's account was locked.
             :type account_locked_date: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the last authentication service where this user was authenticated.
             :type auth_service_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the last authentication service where this user was authenticated.
             :type auth_service_id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param cert: Client Certificate stored on clinet success authorization when CAC is enabled
             :type cert: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cert: Client Certificate stored on clinet success authorization when CAC is enabled
             :type cert: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param cli_creds_enabled_ind: A flag indicating whether or not to use this user's individual CLI credentials for device interaction.
             :type cli_creds_enabled_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_creds_enabled_ind: A flag indicating whether or not to use this user's individual CLI credentials for device interaction.
             :type cli_creds_enabled_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param consecutive_failed_logins: The number of failed logins since the last successful login.
             :type consecutive_failed_logins: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param consecutive_failed_logins: The number of failed logins since the last successful login.
             :type consecutive_failed_logins: Array of Integer

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

             :param db_creds_enabled_ind: A flag which indicates that the user has database credentials enabled.
             :type db_creds_enabled_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param db_creds_enabled_ind: A flag which indicates that the user has database credentials enabled.
             :type db_creds_enabled_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param db_username: Username for MySQL Database.
             :type db_username: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param db_username: Username for MySQL Database.
             :type db_username: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param email: The user's email address.
             :type email: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param email: The user's email address.
             :type email: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param expiration: The expiration date for this user's password.
             :type expiration: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param expiration: The expiration date for this user's password.
             :type expiration: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param first_name: The user's first name.
             :type first_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_name: The user's first name.
             :type first_name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param force_local_ind: A flag indicating whether user is forced to use local authorisation or not.
             :type force_local_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param force_local_ind: A flag indicating whether user is forced to use local authorisation or not.
             :type force_local_ind: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param is_system: A flag indicating whether this is a built-in user. Built-in users cannot be removed.
             :type is_system: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param is_system: A flag indicating whether this is a built-in user. Built-in users cannot be removed.
             :type is_system: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_local_authz_ind: The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local
             :type last_local_authz_ind: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_local_authz_ind: The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local
             :type last_local_authz_ind: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_login: The date and time this use last logged into the NetMRI.
             :type last_login: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_login: The date and time this use last logged into the NetMRI.
             :type last_login: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param last_name: The user's last name.
             :type last_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_name: The user's last name.
             :type last_name: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param notes: Notes on the user, as entered by the administrator.
             :type notes: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param notes: Notes on the user, as entered by the administrator.
             :type notes: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param password_version: version of encryption used to encrypt password
             :type password_version: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password_version: version of encryption used to encrypt password
             :type password_version: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param secure_version: The encryption version of the username and passwords.
             :type secure_version: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param secure_version: The encryption version of the username and passwords.
             :type secure_version: Array of Integer

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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param user_name: The user's login name.
             :type user_name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_name: The user's login name.
             :type user_name: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure.
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

             :param select: The list of attributes to return for each AuthUser. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against auth users, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: account_disabled, account_disabled_date, account_locked, account_locked_date, auth_service_id, cert, cli_creds_enabled_ind, consecutive_failed_logins, created_at, db_creds_enabled_ind, db_username, email, expiration, first_name, force_local_ind, id, is_system, last_local_authz_ind, last_login, last_name, notes, password_version, secure_version, updated_at, user_name.
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

             :return auth_users: An array of the AuthUser objects that match the specified input criteria.
             :rtype auth_users: Array of AuthUser

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available auth users matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: account_disabled, account_disabled_date, account_locked, account_locked_date, auth_service_id, cert, cli_creds_enabled_ind, consecutive_failed_logins, created_at, db_creds_enabled_ind, db_username, email, expiration, first_name, force_local_ind, id, is_system, last_local_authz_ind, last_login, last_name, notes, password_version, secure_version, updated_at, user_name.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_account_disabled: The operator to apply to the field account_disabled. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. account_disabled: A flag indicating whether this user's account has been administratively disabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_account_disabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_account_disabled: If op_account_disabled is specified, the field named in this input will be compared to the value in account_disabled using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_account_disabled must be specified if op_account_disabled is specified.
             :type val_f_account_disabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_account_disabled: If op_account_disabled is specified, this value will be compared to the value in account_disabled using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_account_disabled must be specified if op_account_disabled is specified.
             :type val_c_account_disabled: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_account_disabled_date: The operator to apply to the field account_disabled_date. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. account_disabled_date: The date and time that the user's account was disabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_account_disabled_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_account_disabled_date: If op_account_disabled_date is specified, the field named in this input will be compared to the value in account_disabled_date using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_account_disabled_date must be specified if op_account_disabled_date is specified.
             :type val_f_account_disabled_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_account_disabled_date: If op_account_disabled_date is specified, this value will be compared to the value in account_disabled_date using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_account_disabled_date must be specified if op_account_disabled_date is specified.
             :type val_c_account_disabled_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_account_locked: The operator to apply to the field account_locked. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. account_locked: A flag indicating whether or not this account is locked due to failed login attempts. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_account_locked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_account_locked: If op_account_locked is specified, the field named in this input will be compared to the value in account_locked using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_account_locked must be specified if op_account_locked is specified.
             :type val_f_account_locked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_account_locked: If op_account_locked is specified, this value will be compared to the value in account_locked using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_account_locked must be specified if op_account_locked is specified.
             :type val_c_account_locked: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_account_locked_date: The operator to apply to the field account_locked_date. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. account_locked_date: The date and time that the user's account was locked. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_account_locked_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_account_locked_date: If op_account_locked_date is specified, the field named in this input will be compared to the value in account_locked_date using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_account_locked_date must be specified if op_account_locked_date is specified.
             :type val_f_account_locked_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_account_locked_date: If op_account_locked_date is specified, this value will be compared to the value in account_locked_date using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_account_locked_date must be specified if op_account_locked_date is specified.
             :type val_c_account_locked_date: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_service_id: The operator to apply to the field auth_service_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_service_id: The id of the last authentication service where this user was authenticated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cert: The operator to apply to the field cert. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cert: Client Certificate stored on clinet success authorization when CAC is enabled For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cert: If op_cert is specified, the field named in this input will be compared to the value in cert using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cert must be specified if op_cert is specified.
             :type val_f_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cert: If op_cert is specified, this value will be compared to the value in cert using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cert must be specified if op_cert is specified.
             :type val_c_cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_cli_creds_enabled_ind: The operator to apply to the field cli_creds_enabled_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cli_creds_enabled_ind: A flag indicating whether or not to use this user's individual CLI credentials for device interaction. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cli_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cli_creds_enabled_ind: If op_cli_creds_enabled_ind is specified, the field named in this input will be compared to the value in cli_creds_enabled_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cli_creds_enabled_ind must be specified if op_cli_creds_enabled_ind is specified.
             :type val_f_cli_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cli_creds_enabled_ind: If op_cli_creds_enabled_ind is specified, this value will be compared to the value in cli_creds_enabled_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cli_creds_enabled_ind must be specified if op_cli_creds_enabled_ind is specified.
             :type val_c_cli_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_consecutive_failed_logins: The operator to apply to the field consecutive_failed_logins. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. consecutive_failed_logins: The number of failed logins since the last successful login. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_consecutive_failed_logins: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_consecutive_failed_logins: If op_consecutive_failed_logins is specified, the field named in this input will be compared to the value in consecutive_failed_logins using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_consecutive_failed_logins must be specified if op_consecutive_failed_logins is specified.
             :type val_f_consecutive_failed_logins: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_consecutive_failed_logins: If op_consecutive_failed_logins is specified, this value will be compared to the value in consecutive_failed_logins using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_consecutive_failed_logins must be specified if op_consecutive_failed_logins is specified.
             :type val_c_consecutive_failed_logins: String

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

             :param op_db_creds_enabled_ind: The operator to apply to the field db_creds_enabled_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. db_creds_enabled_ind: A flag which indicates that the user has database credentials enabled. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_db_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_db_creds_enabled_ind: If op_db_creds_enabled_ind is specified, the field named in this input will be compared to the value in db_creds_enabled_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_db_creds_enabled_ind must be specified if op_db_creds_enabled_ind is specified.
             :type val_f_db_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_db_creds_enabled_ind: If op_db_creds_enabled_ind is specified, this value will be compared to the value in db_creds_enabled_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_db_creds_enabled_ind must be specified if op_db_creds_enabled_ind is specified.
             :type val_c_db_creds_enabled_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_db_username: The operator to apply to the field db_username. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. db_username: Username for MySQL Database. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_db_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_db_username: If op_db_username is specified, the field named in this input will be compared to the value in db_username using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_db_username must be specified if op_db_username is specified.
             :type val_f_db_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_db_username: If op_db_username is specified, this value will be compared to the value in db_username using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_db_username must be specified if op_db_username is specified.
             :type val_c_db_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_email: The operator to apply to the field email. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. email: The user's email address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_email: If op_email is specified, the field named in this input will be compared to the value in email using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_email must be specified if op_email is specified.
             :type val_f_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_email: If op_email is specified, this value will be compared to the value in email using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_email must be specified if op_email is specified.
             :type val_c_email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_expiration: The operator to apply to the field expiration. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. expiration: The expiration date for this user's password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_expiration: If op_expiration is specified, the field named in this input will be compared to the value in expiration using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_expiration must be specified if op_expiration is specified.
             :type val_f_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_expiration: If op_expiration is specified, this value will be compared to the value in expiration using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_expiration must be specified if op_expiration is specified.
             :type val_c_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_first_name: The operator to apply to the field first_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. first_name: The user's first name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_first_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_first_name: If op_first_name is specified, the field named in this input will be compared to the value in first_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_first_name must be specified if op_first_name is specified.
             :type val_f_first_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_first_name: If op_first_name is specified, this value will be compared to the value in first_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_first_name must be specified if op_first_name is specified.
             :type val_c_first_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_force_local_ind: The operator to apply to the field force_local_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. force_local_ind: A flag indicating whether user is forced to use local authorisation or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_force_local_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_force_local_ind: If op_force_local_ind is specified, the field named in this input will be compared to the value in force_local_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_force_local_ind must be specified if op_force_local_ind is specified.
             :type val_f_force_local_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_force_local_ind: If op_force_local_ind is specified, this value will be compared to the value in force_local_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_force_local_ind must be specified if op_force_local_ind is specified.
             :type val_c_force_local_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this user. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_is_system: The operator to apply to the field is_system. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. is_system: A flag indicating whether this is a built-in user. Built-in users cannot be removed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_is_system: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_is_system: If op_is_system is specified, the field named in this input will be compared to the value in is_system using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_is_system must be specified if op_is_system is specified.
             :type val_f_is_system: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_is_system: If op_is_system is specified, this value will be compared to the value in is_system using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_is_system must be specified if op_is_system is specified.
             :type val_c_is_system: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_last_local_authz_ind: The operator to apply to the field last_local_authz_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_local_authz_ind: The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_local_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_local_authz_ind: If op_last_local_authz_ind is specified, the field named in this input will be compared to the value in last_local_authz_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_local_authz_ind must be specified if op_last_local_authz_ind is specified.
             :type val_f_last_local_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_local_authz_ind: If op_last_local_authz_ind is specified, this value will be compared to the value in last_local_authz_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_local_authz_ind must be specified if op_last_local_authz_ind is specified.
             :type val_c_last_local_authz_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_last_login: The operator to apply to the field last_login. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_login: The date and time this use last logged into the NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_login: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_login: If op_last_login is specified, the field named in this input will be compared to the value in last_login using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_login must be specified if op_last_login is specified.
             :type val_f_last_login: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_login: If op_last_login is specified, this value will be compared to the value in last_login using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_login must be specified if op_last_login is specified.
             :type val_c_last_login: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_last_name: The operator to apply to the field last_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_name: The user's last name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_name: If op_last_name is specified, the field named in this input will be compared to the value in last_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_name must be specified if op_last_name is specified.
             :type val_f_last_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_name: If op_last_name is specified, this value will be compared to the value in last_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_name must be specified if op_last_name is specified.
             :type val_c_last_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_notes: The operator to apply to the field notes. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. notes: Notes on the user, as entered by the administrator. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_notes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_notes: If op_notes is specified, the field named in this input will be compared to the value in notes using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_notes must be specified if op_notes is specified.
             :type val_f_notes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_notes: If op_notes is specified, this value will be compared to the value in notes using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_notes must be specified if op_notes is specified.
             :type val_c_notes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_password_version: The operator to apply to the field password_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. password_version: version of encryption used to encrypt password For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_password_version: If op_password_version is specified, the field named in this input will be compared to the value in password_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_password_version must be specified if op_password_version is specified.
             :type val_f_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_password_version: If op_password_version is specified, this value will be compared to the value in password_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_password_version must be specified if op_password_version is specified.
             :type val_c_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_secure_version: The operator to apply to the field secure_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. secure_version: The encryption version of the username and passwords. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_user_name: The operator to apply to the field user_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. user_name: The user's login name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_user_name: If op_user_name is specified, the field named in this input will be compared to the value in user_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_user_name must be specified if op_user_name is specified.
             :type val_f_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_user_name: If op_user_name is specified, this value will be compared to the value in user_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_user_name must be specified if op_user_name is specified.
             :type val_c_user_name: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure.
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

             :param select: The list of attributes to return for each AuthUser. Valid values are id, user_name, email, notes, created_at, updated_at, first_name, last_name, is_system, last_login, expiration, consecutive_failed_logins, account_locked, account_locked_date, account_disabled, account_disabled_date, cli_creds_enabled_ind, password_secure, password_version, cli_user_name_secure, cli_password_secure, cli_enable_password_secure, secure_version, auth_service_id, force_local_ind, last_local_authz_ind, cert, db_creds_enabled_ind, db_username, db_password_secure. If empty or omitted, all attributes will be returned.
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

             :return auth_users: An array of the AuthUser objects that match the specified input criteria.
             :rtype auth_users: Array of AuthUser

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a new auth user.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param account_disabled: A flag indicating whether this user's account has been administratively disabled.
             :type account_disabled: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param auth_service_id: The id of the last authentication service where this user was authenticated.
             :type auth_service_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cert: Client Certificate stored on clinet success authorization when CAC is enabled
             :type cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param cli_creds_enabled_ind: A flag indicating whether or not to use this user's individual CLI credentials for device interaction.
             :type cli_creds_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param cli_enable_password: No description is available for cli_enable_password.
             :type cli_enable_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param cli_password: No description is available for cli_password.
             :type cli_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param cli_user_name: No description is available for cli_user_name.
             :type cli_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param email: The user's email address.
             :type email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param first_name: The user's first name.
             :type first_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param force_local_ind: A flag indicating whether user is forced to use local authorisation or not.
             :type force_local_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_local_authz_ind: The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local
             :type last_local_authz_ind: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param last_name: The user's last name.
             :type last_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param notes: Notes on the user, as entered by the administrator.
             :type notes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: The user's password (required for local authentication).
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param user_name: The user's login name.
             :type user_name: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created auth user.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created auth user.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created auth user.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_user: The newly created auth user.
             :rtype auth_user: AuthUser

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing auth user.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param account_disabled: A flag indicating whether this user's account has been administratively disabled. If omitted, this field will not be updated.
             :type account_disabled: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_service_id: The id of the last authentication service where this user was authenticated. If omitted, this field will not be updated.
             :type auth_service_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cert: Client Certificate stored on clinet success authorization when CAC is enabled If omitted, this field will not be updated.
             :type cert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_creds_enabled_ind: A flag indicating whether or not to use this user's individual CLI credentials for device interaction. If omitted, this field will not be updated.
             :type cli_creds_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_enable_password: No description is available for cli_enable_password. If omitted, this field will not be updated.
             :type cli_enable_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_password: No description is available for cli_password. If omitted, this field will not be updated.
             :type cli_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cli_user_name: No description is available for cli_user_name. If omitted, this field will not be updated.
             :type cli_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param db_creds_enabled_ind: A flag which indicates that the user has database credentials enabled. If omitted, this field will not be updated.
             :type db_creds_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param db_password: No description is available for db_password. If omitted, this field will not be updated.
             :type db_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param db_username: Username for MySQL Database. If omitted, this field will not be updated.
             :type db_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param email: The user's email address. If omitted, this field will not be updated.
             :type email: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_name: The user's first name. If omitted, this field will not be updated.
             :type first_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param force_local_ind: A flag indicating whether user is forced to use local authorisation or not. If omitted, this field will not be updated.
             :type force_local_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_local_authz_ind: The source where the last authorization came from. May be 0 - Remote, 1 - Local, 2 - Forced Local If omitted, this field will not be updated.
             :type last_local_authz_ind: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_name: The user's last name. If omitted, this field will not be updated.
             :type last_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param notes: Notes on the user, as entered by the administrator. If omitted, this field will not be updated.
             :type notes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: The user's password (required for local authentication). If omitted, this field will not be updated.
             :type password: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated auth user.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated auth user.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated auth user.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_user: The updated auth user.
             :rtype auth_user: AuthUser

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified auth user from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this user.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def auth_roles(self, **kwargs):
        """Returns the roles associated with the user, and the device groups to which they apply.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the user.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles: The roles the assigned to the user, along with an extra 'device_group_ids' attribute, listing the device groups for which the role applies.
             :rtype auth_roles: Array of AuthRole

            """

        return self.api_request(self._get_method_fullname("auth_roles"), kwargs)

    def add_auth_role(self, **kwargs):
        """Assigns a specified role to a user within a specified list of device groups.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the user.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param auth_role_id: The internal NetMRI identifier for the user role.
             :type auth_role_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_group_ids: The internal NetMRI identifiers for the device groups in which to assign the role to this user. A value of 0 represents all groups. The user will be assigned the role for the groups listed here for which the currently authenticated user has user_admin privileges. The role will be revoked for those groups that the authenticated user has 'user_admin' privileges, but are not listed.
             :type device_group_ids: Array of Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_user: The user to which the role has been assigned.
             :rtype auth_user: AuthUser

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_role: The roles which has been assigned.
             :rtype auth_role: AuthUser

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_group_ids: The current list of device group IDs assigned for this role and user, subject to the permissions of the authenticated user.
             :rtype device_group_ids: Array of DeviceGroup

            """

        return self.api_request(self._get_method_fullname("add_auth_role"), kwargs)

    def remove_auth_role(self, **kwargs):
        """Removes a specified role from a user for all device groups for which the current user has 'user_admin' privilege.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the user.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param auth_role_id: The internal NetMRI identifier for the user role.
             :type auth_role_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_user: The user from which the role has been removed.
             :rtype auth_user: AuthUser

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_role: The role which has been removed.
             :rtype auth_role: AuthUser

            """

        return self.api_request(self._get_method_fullname("remove_auth_role"), kwargs)
