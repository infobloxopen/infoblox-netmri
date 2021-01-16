from ..broker import Broker


class NotificationBroker(Broker):
    controller = "notifications"

    def index(self, **kwargs):
        """Lists the available notifications. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the notification.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run.
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

             :param select: The list of attributes to return for each Notification. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run. If empty or omitted, all attributes will be returned.
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

             :return notifications: An array of the Notification objects that match the specified input criteria.
             :rtype notifications: Array of Notification

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified notification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the notification.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return notification: The notification identified by the specified id.
             :rtype notification: Notification

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available notifications matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_device_groups_ind: Do not restrict notification to particular device groups.
             :type all_device_groups_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_in_category_ind: Notify for all in the category.
             :type all_in_category_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_interface_groups_ind: Do not restrict notification to particular interface groups.
             :type all_interface_groups_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_user_id: User ID of the creator.
             :type auth_user_id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: A category of the notification. Possible values are 'issue','change','job','systemalert'.
             :type category: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cron: Schedule for summary notifications in cron format.
             :type cron: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param delivery_method: Delivery method of the notification. Possible values are 'email', 'syslog', 'snmp'.
             :type delivery_method: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param details_template: Notification details template.
             :type details_template: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param event_type: List of events that we subscribe to. Default is all events.
             :type event_type: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from: Notification e-mail 'from:' field.
             :type from: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from_name: Name for the 'from:' field.
             :type from_name: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the notification.
             :type id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_run: Last run.
             :type last_run: Array of DateTime

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message_template: Notification message template.
             :type message_template: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mime: Message MIME type. Possible values are 'html' or 'text'.
             :type mime: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param send_clearing_ind: Whether to send a notification on issue clearing.
             :type send_clearing_ind: Array of Boolean

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param severity: Severity level from 1 to 3.
             :type severity: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param subject: Subject of the notification e-mail.
             :type subject: Array of String

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param time_window_id: Time window id.
             :type time_window_id: Array of Integer

            |  ``api version min:`` 2.9
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param to: Notification e-mail 'To:' field.
             :type to: Array of String

            |  ``api version min:`` 2.9
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run.
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

             :param select: The list of attributes to return for each Notification. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against notifications, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: all_device_groups_ind, all_in_category_ind, all_interface_groups_ind, auth_user_id, category, created_at, cron, delivery_method, details_template, event_type, from, from_name, id, last_run, message_template, mime, send_clearing_ind, severity, subject, time_window_id, to, updated_at.
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

             :return notifications: An array of the Notification objects that match the specified input criteria.
             :rtype notifications: Array of Notification

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available notifications matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: all_device_groups_ind, all_in_category_ind, all_interface_groups_ind, auth_user_id, category, created_at, cron, delivery_method, details_template, event_type, from, from_name, id, last_run, message_template, mime, send_clearing_ind, severity, subject, time_window_id, to, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_all_device_groups_ind: The operator to apply to the field all_device_groups_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. all_device_groups_ind: Do not restrict notification to particular device groups. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_all_device_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_all_device_groups_ind: If op_all_device_groups_ind is specified, the field named in this input will be compared to the value in all_device_groups_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_all_device_groups_ind must be specified if op_all_device_groups_ind is specified.
             :type val_f_all_device_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_all_device_groups_ind: If op_all_device_groups_ind is specified, this value will be compared to the value in all_device_groups_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_all_device_groups_ind must be specified if op_all_device_groups_ind is specified.
             :type val_c_all_device_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_all_in_category_ind: The operator to apply to the field all_in_category_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. all_in_category_ind: Notify for all in the category. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_all_in_category_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_all_in_category_ind: If op_all_in_category_ind is specified, the field named in this input will be compared to the value in all_in_category_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_all_in_category_ind must be specified if op_all_in_category_ind is specified.
             :type val_f_all_in_category_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_all_in_category_ind: If op_all_in_category_ind is specified, this value will be compared to the value in all_in_category_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_all_in_category_ind must be specified if op_all_in_category_ind is specified.
             :type val_c_all_in_category_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_all_interface_groups_ind: The operator to apply to the field all_interface_groups_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. all_interface_groups_ind: Do not restrict notification to particular interface groups.  For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_all_interface_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_all_interface_groups_ind: If op_all_interface_groups_ind is specified, the field named in this input will be compared to the value in all_interface_groups_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_all_interface_groups_ind must be specified if op_all_interface_groups_ind is specified.
             :type val_f_all_interface_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_all_interface_groups_ind: If op_all_interface_groups_ind is specified, this value will be compared to the value in all_interface_groups_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_all_interface_groups_ind must be specified if op_all_interface_groups_ind is specified.
             :type val_c_all_interface_groups_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_user_id: The operator to apply to the field auth_user_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_user_id: User ID of the creator. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_category: The operator to apply to the field category. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. category: A category of the notification. Possible values are 'issue','change','job','systemalert'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_cron: The operator to apply to the field cron. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. cron: Schedule for summary notifications in cron format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_cron: If op_cron is specified, the field named in this input will be compared to the value in cron using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_cron must be specified if op_cron is specified.
             :type val_f_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_cron: If op_cron is specified, this value will be compared to the value in cron using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_cron must be specified if op_cron is specified.
             :type val_c_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_delivery_method: The operator to apply to the field delivery_method. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. delivery_method: Delivery method of the notification. Possible values are 'email', 'syslog', 'snmp'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_delivery_method: If op_delivery_method is specified, the field named in this input will be compared to the value in delivery_method using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_delivery_method must be specified if op_delivery_method is specified.
             :type val_f_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_delivery_method: If op_delivery_method is specified, this value will be compared to the value in delivery_method using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_delivery_method must be specified if op_delivery_method is specified.
             :type val_c_delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_details_template: The operator to apply to the field details_template. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. details_template: Notification details template. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_details_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_details_template: If op_details_template is specified, the field named in this input will be compared to the value in details_template using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_details_template must be specified if op_details_template is specified.
             :type val_f_details_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_details_template: If op_details_template is specified, this value will be compared to the value in details_template using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_details_template must be specified if op_details_template is specified.
             :type val_c_details_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_event_type: The operator to apply to the field event_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. event_type: List of events that we subscribe to. Default is all events. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_event_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_event_type: If op_event_type is specified, the field named in this input will be compared to the value in event_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_event_type must be specified if op_event_type is specified.
             :type val_f_event_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_event_type: If op_event_type is specified, this value will be compared to the value in event_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_event_type must be specified if op_event_type is specified.
             :type val_c_event_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_from: The operator to apply to the field from. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. from: Notification e-mail 'from:' field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_from: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_from: If op_from is specified, the field named in this input will be compared to the value in from using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_from must be specified if op_from is specified.
             :type val_f_from: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_from: If op_from is specified, this value will be compared to the value in from using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_from must be specified if op_from is specified.
             :type val_c_from: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_from_name: The operator to apply to the field from_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. from_name: Name for the 'from:' field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_from_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_from_name: If op_from_name is specified, the field named in this input will be compared to the value in from_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_from_name must be specified if op_from_name is specified.
             :type val_f_from_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_from_name: If op_from_name is specified, this value will be compared to the value in from_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_from_name must be specified if op_from_name is specified.
             :type val_c_from_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for the notification. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_last_run: The operator to apply to the field last_run. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_run: Last run. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_run: If op_last_run is specified, the field named in this input will be compared to the value in last_run using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_run must be specified if op_last_run is specified.
             :type val_f_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_run: If op_last_run is specified, this value will be compared to the value in last_run using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_run must be specified if op_last_run is specified.
             :type val_c_last_run: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_message_template: The operator to apply to the field message_template. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. message_template: Notification message template. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_message_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_message_template: If op_message_template is specified, the field named in this input will be compared to the value in message_template using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_message_template must be specified if op_message_template is specified.
             :type val_f_message_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_message_template: If op_message_template is specified, this value will be compared to the value in message_template using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_message_template must be specified if op_message_template is specified.
             :type val_c_message_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_mime: The operator to apply to the field mime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. mime: Message MIME type. Possible values are 'html' or 'text'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_mime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_mime: If op_mime is specified, the field named in this input will be compared to the value in mime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_mime must be specified if op_mime is specified.
             :type val_f_mime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_mime: If op_mime is specified, this value will be compared to the value in mime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_mime must be specified if op_mime is specified.
             :type val_c_mime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_send_clearing_ind: The operator to apply to the field send_clearing_ind. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. send_clearing_ind: Whether to send a notification on issue clearing. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_send_clearing_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_send_clearing_ind: If op_send_clearing_ind is specified, the field named in this input will be compared to the value in send_clearing_ind using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_send_clearing_ind must be specified if op_send_clearing_ind is specified.
             :type val_f_send_clearing_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_send_clearing_ind: If op_send_clearing_ind is specified, this value will be compared to the value in send_clearing_ind using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_send_clearing_ind must be specified if op_send_clearing_ind is specified.
             :type val_c_send_clearing_ind: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_severity: The operator to apply to the field severity. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. severity: Severity level from 1 to 3. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_severity: If op_severity is specified, the field named in this input will be compared to the value in severity using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_severity must be specified if op_severity is specified.
             :type val_f_severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_severity: If op_severity is specified, this value will be compared to the value in severity using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_severity must be specified if op_severity is specified.
             :type val_c_severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_subject: The operator to apply to the field subject. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. subject: Subject of the notification e-mail. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_subject: If op_subject is specified, the field named in this input will be compared to the value in subject using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_subject must be specified if op_subject is specified.
             :type val_f_subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_subject: If op_subject is specified, this value will be compared to the value in subject using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_subject must be specified if op_subject is specified.
             :type val_c_subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_time_window_id: The operator to apply to the field time_window_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. time_window_id: Time window id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_time_window_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_time_window_id: If op_time_window_id is specified, the field named in this input will be compared to the value in time_window_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_time_window_id must be specified if op_time_window_id is specified.
             :type val_f_time_window_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_time_window_id: If op_time_window_id is specified, this value will be compared to the value in time_window_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_time_window_id must be specified if op_time_window_id is specified.
             :type val_c_time_window_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_to: The operator to apply to the field to. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. to: Notification e-mail 'To:' field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_to: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_to: If op_to is specified, the field named in this input will be compared to the value in to using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_to must be specified if op_to is specified.
             :type val_f_to: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_to: If op_to is specified, this value will be compared to the value in to using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_to must be specified if op_to is specified.
             :type val_c_to: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run.
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

             :param select: The list of attributes to return for each Notification. Valid values are id, auth_user_id, category, delivery_method, mime, subject, message_template, details_template, to, created_at, updated_at, from, from_name, severity, all_in_category_ind, all_device_groups_ind, all_interface_groups_ind, time_window_id, event_type, send_clearing_ind, cron, last_run. If empty or omitted, all attributes will be returned.
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

             :return notifications: An array of the Notification objects that match the specified input criteria.
             :rtype notifications: Array of Notification

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified notification from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the notification.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Creates a new notification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_device_groups_ind: Do not restrict notification to particular device groups.
             :type all_device_groups_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_in_category_ind: Notify for all in the category.
             :type all_in_category_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_interface_groups_ind: Do not restrict notification to particular interface groups.
             :type all_interface_groups_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_user_id: User ID of the creator.
             :type auth_user_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param category: A category of the notification. Possible values are 'issue','change','job','systemalert'.
             :type category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cron: Schedule for summary notifications in cron format.
             :type cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param delivery_method: Delivery method of the notification. Possible values are 'email', 'syslog', 'snmp'.
             :type delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param details_template: Notification details template.
             :type details_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param event_type: List of events that we subscribe to. Default is all events.
             :type event_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from: Notification e-mail 'from:' field.
             :type from: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from_name: Name for the 'from:' field.
             :type from_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message_template: Notification message template.
             :type message_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mime: Message MIME type. Possible values are 'html' or 'text'.
             :type mime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param send_clearing_ind: Whether to send a notification on issue clearing.
             :type send_clearing_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param severity: Severity level from 1 to 3.
             :type severity: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param subject: Subject of the notification e-mail.
             :type subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param time_window_id: Time window id.
             :type time_window_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param to: Notification e-mail 'To:' field.
             :type to: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A list of Device Group IDs to which the notification belongs
             :type device_group_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param if_group_ids: A list of Interface Group IDs
             :type if_group_ids: Array of Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created notification.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created notification.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created notification.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return notification: The newly created notification.
             :rtype notification: Notification

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing notification.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the notification.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_device_groups_ind: Do not restrict notification to particular device groups. If omitted, this field will not be updated.
             :type all_device_groups_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_in_category_ind: Notify for all in the category. If omitted, this field will not be updated.
             :type all_in_category_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param all_interface_groups_ind: Do not restrict notification to particular interface groups.  If omitted, this field will not be updated.
             :type all_interface_groups_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_user_id: User ID of the creator. If omitted, this field will not be updated.
             :type auth_user_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param category: A category of the notification. Possible values are 'issue','change','job','systemalert'.
             :type category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cron: Schedule for summary notifications in cron format. If omitted, this field will not be updated.
             :type cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param delivery_method: Delivery method of the notification. Possible values are 'email', 'syslog', 'snmp'.
             :type delivery_method: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param details_template: Notification details template. If omitted, this field will not be updated.
             :type details_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param event_type: List of events that we subscribe to. Default is all events. If omitted, this field will not be updated.
             :type event_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from: Notification e-mail 'from:' field. If omitted, this field will not be updated.
             :type from: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param from_name: Name for the 'from:' field. If omitted, this field will not be updated.
             :type from_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param message_template: Notification message template. If omitted, this field will not be updated.
             :type message_template: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param mime: Message MIME type. Possible values are 'html' or 'text'. If omitted, this field will not be updated.
             :type mime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param send_clearing_ind: Whether to send a notification on issue clearing. If omitted, this field will not be updated.
             :type send_clearing_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param severity: Severity level from 1 to 3.
             :type severity: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param subject: Subject of the notification e-mail. If omitted, this field will not be updated.
             :type subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param time_window_id: Time window id. If omitted, this field will not be updated.
             :type time_window_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param to: Notification e-mail 'To:' field. If omitted, this field will not be updated.
             :type to: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A list of Device Group IDs to which the notification belongs
             :type device_group_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param if_group_ids: A list of Interface Group IDs
             :type if_group_ids: Array of Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated notification.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated notification.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated notification.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return notification: The updated notification.
             :rtype notification: Notification

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def test(self, **kwargs):
        """Test the specified notification

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the notification to test
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return result: Test result
             :rtype result: String

            """

        return self.api_request(self._get_method_fullname("test"), kwargs)

    def update_settings(self, **kwargs):
        """Update the global notifications settings.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPServer: SNMP server name for SNMP notifications.
             :type SNMPServer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPort: SNMP port for SNMP notifications.
             :type SNMPPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPCommunity: SNMP community string for notifications.
             :type SNMPCommunity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPTrapType: SNMP trap type for notifications
             :type SNMPTrapType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailSMTPServer: SMTP server for e-mail notifications.
             :type EmailSMTPServer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailPort: Port of remote SMTP server to connect
             :type EmailPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailUsername: User name for SMTP server.
             :type EmailUsername: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailPassword: SMTP server password.
             :type EmailPassword: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailFromUser: Username for notification e-mail.
             :type EmailFromUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EmailFromAddr: From address for the notification e-mails.
             :type EmailFromAddr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailSubject: E-mail subject for System notifications.
             :type SystemEmailSubject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailFormat: E-mail format for System notifications. Should be either 'text' or 'html'.
             :type SystemEmailFormat: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailPlainTextMessage: Message template for System notifications in plain text format.
             :type SystemEmailPlainTextMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailPlainTextDetails: Details template for System notifications in plain text format.
             :type SystemEmailPlainTextDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailHtmlMessage: Message template for System notifications in html format.
             :type SystemEmailHtmlMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemEmailHtmlDetails: Details template for System notifications in html format.
             :type SystemEmailHtmlDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailSubject: E-mail subject for Change notifications.
             :type ChangeEmailSubject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailFormat: E-mail format for Change notifications. Should be either 'text' or 'html'.
             :type ChangeEmailFormat: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailPlainTextMessage: Message template for Change notifications in plain text format.
             :type ChangeEmailPlainTextMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailPlainTextDetails: Details template for Change notifications in plain text format.
             :type ChangeEmailPlainTextDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailHtmlMessage: Message template for Change notifications in html format.
             :type ChangeEmailHtmlMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeEmailHtmlDetails: Details template for Change notifications in html format.
             :type ChangeEmailHtmlDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailSubject: E-mail subject for Issue notifications.
             :type IssueEmailSubject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailFormat: E-mail format for Issue notifications. Should be either 'text' or 'html'.
             :type IssueEmailFormat: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailPlainTextMessage: Message template for Issue notifications in plain text format.
             :type IssueEmailPlainTextMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailPlainTextDetails: Details template for Issue notifications in plain text format.
             :type IssueEmailPlainTextDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailHtmlMessage: Message template for Issue notifications in html format.
             :type IssueEmailHtmlMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueEmailHtmlDetails: Details template for Issue notifications in html format.
             :type IssueEmailHtmlDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailSubject: E-mail subject for Job notifications.
             :type JobEmailSubject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailFormat: E-mail format for Job notifications. Should be either 'text' or 'html'.
             :type JobEmailFormat: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailPlainTextMessage: Message template for Job notifications in plain text format.
             :type JobEmailPlainTextMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailPlainTextDetails: Details template for Job notifications in plain text format.
             :type JobEmailPlainTextDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailHtmlMessage: Message template for Job notifications in html format.
             :type JobEmailHtmlMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobEmailHtmlDetails: Details template for Job notifications in html format.
             :type JobEmailHtmlDetails: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogServer: Syslog server name.
             :type SyslogServer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogPort: Syslog port.
             :type SyslogPort: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogFacility: Syslog Facility.
             :type SyslogFacility: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogSeverityInfoMapping: Mapping of Info messages to syslog level (0-7).
             :type SyslogSeverityInfoMapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogSeverityWarningMapping: Mapping of Warning messages to syslog level (0-7).
             :type SyslogSeverityWarningMapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogSeverityErrorMapping: Mapping of Error messages to syslog level (0-7).
             :type SyslogSeverityErrorMapping: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SystemSyslogMessage: Syslog message template for system notifications.
             :type SystemSyslogMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeSyslogMessage: Syslog message template for change notifications.
             :type ChangeSyslogMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueSyslogMessage: Syslog message template for issue notifications.
             :type IssueSyslogMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param JobSyslogMessage: Syslog message template for job notifications.
             :type JobSyslogMessage: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_settings"), kwargs)

    def reset_settings(self, **kwargs):
        """Reset the global notifications settings to defaults.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("reset_settings"), kwargs)
