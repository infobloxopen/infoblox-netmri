from ..broker import Broker


class JobHandlerBroker(Broker):
    controller = "job_handlers"

    def index(self, **kwargs):
        """Lists the available job handlers. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at.
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

             :param select: The list of attributes to return for each JobHandler. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return job_handlers: An array of the JobHandler objects that match the specified input criteria.
             :rtype job_handlers: Array of JobHandler

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified job handler.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the job handler.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_handler: The job handler identified by the specified id.
             :rtype job_handler: JobHandler

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available job handlers matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_admin_queue: No description is available for broker_admin_queue.
             :type broker_admin_queue: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_exchange: No description is available for broker_exchange.
             :type broker_exchange: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_password_secure: No description is available for broker_password_secure.
             :type broker_password_secure: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_password_version: No description is available for broker_password_version.
             :type broker_password_version: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_queue: No description is available for broker_queue.
             :type broker_queue: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param broker_user_name: No description is available for broker_user_name.
             :type broker_user_name: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param concurrent_limit: No description is available for concurrent_limit.
             :type concurrent_limit: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: No description is available for created_at.
             :type created_at: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: No description is available for created_by.
             :type created_by: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param current_bid: No description is available for current_bid.
             :type current_bid: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: No description is available for id.
             :type id: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param last_status_at: No description is available for last_status_at.
             :type last_status_at: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param status: No description is available for status.
             :type status: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: No description is available for unit_id.
             :type unit_id: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: No description is available for updated_at.
             :type updated_at: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at.
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

             :param select: The list of attributes to return for each JobHandler. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against job handlers, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: broker_admin_queue, broker_exchange, broker_password_secure, broker_password_version, broker_queue, broker_user_name, concurrent_limit, created_at, created_by, current_bid, id, last_status_at, status, unit_id, updated_at.
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

             :return job_handlers: An array of the JobHandler objects that match the specified input criteria.
             :rtype job_handlers: Array of JobHandler

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available job handlers matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: broker_admin_queue, broker_exchange, broker_password_secure, broker_password_version, broker_queue, broker_user_name, concurrent_limit, created_at, created_by, current_bid, id, last_status_at, status, unit_id, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_admin_queue: The operator to apply to the field broker_admin_queue. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_admin_queue: No description is available for broker_admin_queue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_admin_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_admin_queue: If op_broker_admin_queue is specified, the field named in this input will be compared to the value in broker_admin_queue using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_admin_queue must be specified if op_broker_admin_queue is specified.
             :type val_f_broker_admin_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_admin_queue: If op_broker_admin_queue is specified, this value will be compared to the value in broker_admin_queue using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_admin_queue must be specified if op_broker_admin_queue is specified.
             :type val_c_broker_admin_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_exchange: The operator to apply to the field broker_exchange. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_exchange: No description is available for broker_exchange. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_exchange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_exchange: If op_broker_exchange is specified, the field named in this input will be compared to the value in broker_exchange using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_exchange must be specified if op_broker_exchange is specified.
             :type val_f_broker_exchange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_exchange: If op_broker_exchange is specified, this value will be compared to the value in broker_exchange using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_exchange must be specified if op_broker_exchange is specified.
             :type val_c_broker_exchange: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_password_secure: The operator to apply to the field broker_password_secure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_password_secure: No description is available for broker_password_secure. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_password_secure: If op_broker_password_secure is specified, the field named in this input will be compared to the value in broker_password_secure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_password_secure must be specified if op_broker_password_secure is specified.
             :type val_f_broker_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_password_secure: If op_broker_password_secure is specified, this value will be compared to the value in broker_password_secure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_password_secure must be specified if op_broker_password_secure is specified.
             :type val_c_broker_password_secure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_password_version: The operator to apply to the field broker_password_version. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_password_version: No description is available for broker_password_version. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_password_version: If op_broker_password_version is specified, the field named in this input will be compared to the value in broker_password_version using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_password_version must be specified if op_broker_password_version is specified.
             :type val_f_broker_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_password_version: If op_broker_password_version is specified, this value will be compared to the value in broker_password_version using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_password_version must be specified if op_broker_password_version is specified.
             :type val_c_broker_password_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_queue: The operator to apply to the field broker_queue. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_queue: No description is available for broker_queue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_queue: If op_broker_queue is specified, the field named in this input will be compared to the value in broker_queue using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_queue must be specified if op_broker_queue is specified.
             :type val_f_broker_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_queue: If op_broker_queue is specified, this value will be compared to the value in broker_queue using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_queue must be specified if op_broker_queue is specified.
             :type val_c_broker_queue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_broker_user_name: The operator to apply to the field broker_user_name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. broker_user_name: No description is available for broker_user_name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_broker_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_broker_user_name: If op_broker_user_name is specified, the field named in this input will be compared to the value in broker_user_name using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_broker_user_name must be specified if op_broker_user_name is specified.
             :type val_f_broker_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_broker_user_name: If op_broker_user_name is specified, this value will be compared to the value in broker_user_name using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_broker_user_name must be specified if op_broker_user_name is specified.
             :type val_c_broker_user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_concurrent_limit: The operator to apply to the field concurrent_limit. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. concurrent_limit: No description is available for concurrent_limit. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_concurrent_limit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_concurrent_limit: If op_concurrent_limit is specified, the field named in this input will be compared to the value in concurrent_limit using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_concurrent_limit must be specified if op_concurrent_limit is specified.
             :type val_f_concurrent_limit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_concurrent_limit: If op_concurrent_limit is specified, this value will be compared to the value in concurrent_limit using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_concurrent_limit must be specified if op_concurrent_limit is specified.
             :type val_c_concurrent_limit: String

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

             :param op_created_by: The operator to apply to the field created_by. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_by: No description is available for created_by. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_by: If op_created_by is specified, the field named in this input will be compared to the value in created_by using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_by must be specified if op_created_by is specified.
             :type val_f_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_by: If op_created_by is specified, this value will be compared to the value in created_by using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_by must be specified if op_created_by is specified.
             :type val_c_created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_current_bid: The operator to apply to the field current_bid. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. current_bid: No description is available for current_bid. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_current_bid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_current_bid: If op_current_bid is specified, the field named in this input will be compared to the value in current_bid using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_current_bid must be specified if op_current_bid is specified.
             :type val_f_current_bid: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_current_bid: If op_current_bid is specified, this value will be compared to the value in current_bid using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_current_bid must be specified if op_current_bid is specified.
             :type val_c_current_bid: String

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

             :param op_last_status_at: The operator to apply to the field last_status_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. last_status_at: No description is available for last_status_at. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_last_status_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_last_status_at: If op_last_status_at is specified, the field named in this input will be compared to the value in last_status_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_last_status_at must be specified if op_last_status_at is specified.
             :type val_f_last_status_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_last_status_at: If op_last_status_at is specified, this value will be compared to the value in last_status_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_last_status_at must be specified if op_last_status_at is specified.
             :type val_c_last_status_at: String

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

             :param op_unit_id: The operator to apply to the field unit_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. unit_id: No description is available for unit_id. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_unit_id: If op_unit_id is specified, the field named in this input will be compared to the value in unit_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_unit_id must be specified if op_unit_id is specified.
             :type val_f_unit_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_unit_id: If op_unit_id is specified, this value will be compared to the value in unit_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_unit_id must be specified if op_unit_id is specified.
             :type val_c_unit_id: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at.
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

             :param select: The list of attributes to return for each JobHandler. Valid values are id, created_by, unit_id, broker_user_name, broker_password_secure, broker_password_version, broker_exchange, broker_queue, broker_admin_queue, concurrent_limit, current_bid, status, last_status_at, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return job_handlers: An array of the JobHandler objects that match the specified input criteria.
             :rtype job_handlers: Array of JobHandler

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified job handler from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the job handler.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Create and register a Job Handler

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param remote_ip: The IP address from which connectivity will be made.  Defaults to the request IP.
             :type remote_ip: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return broker_url: The URL used to connect to AMQP
             :rtype broker_url: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return broker_password: The password used to connect to AMQP
             :rtype broker_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_handler: The JobHandler
             :rtype job_handler: JobHandler

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def download_config(self, **kwargs):
        """Download Job Handler Configuration Archive

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config: The config archive contents. It will be presented as type "application/octet-stream".
             :rtype config: String

            """

        return self.api_mixed_request(self._get_method_fullname("download_config"), kwargs)
