from ..broker import Broker


class DeviceCertificateBroker(Broker):
    controller = "device_certificates"

    def find(self, **kwargs):
        """Lists the available device certificates matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: UnitID, certificate, certificate_parameter, certificate_type, created_at, id, ip_address_dotted, ip_address_numeric, name, passphrase, password, port, updated_at, username.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier for collector. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UnitID: If op_UnitID is specified, the field named in this input will be compared to the value in UnitID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UnitID must be specified if op_UnitID is specified.
             :type val_f_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UnitID: If op_UnitID is specified, this value will be compared to the value in UnitID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UnitID must be specified if op_UnitID is specified.
             :type val_c_UnitID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_certificate: The operator to apply to the field certificate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. certificate: The certificate BLOB data. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_certificate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_certificate: If op_certificate is specified, the field named in this input will be compared to the value in certificate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_certificate must be specified if op_certificate is specified.
             :type val_f_certificate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_certificate: If op_certificate is specified, this value will be compared to the value in certificate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_certificate must be specified if op_certificate is specified.
             :type val_c_certificate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_certificate_parameter: The operator to apply to the field certificate_parameter. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. certificate_parameter: The certificate parameters. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_certificate_parameter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_certificate_parameter: If op_certificate_parameter is specified, the field named in this input will be compared to the value in certificate_parameter using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_certificate_parameter must be specified if op_certificate_parameter is specified.
             :type val_f_certificate_parameter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_certificate_parameter: If op_certificate_parameter is specified, this value will be compared to the value in certificate_parameter using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_certificate_parameter must be specified if op_certificate_parameter is specified.
             :type val_c_certificate_parameter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_certificate_type: The operator to apply to the field certificate_type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. certificate_type: The type of certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_certificate_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_certificate_type: If op_certificate_type is specified, the field named in this input will be compared to the value in certificate_type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_certificate_type must be specified if op_certificate_type is specified.
             :type val_f_certificate_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_certificate_type: If op_certificate_type is specified, this value will be compared to the value in certificate_type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_certificate_type must be specified if op_certificate_type is specified.
             :type val_c_certificate_type: String

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

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this device certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ip_address_dotted: The operator to apply to the field ip_address_dotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ip_address_dotted: The IP address as string. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ip_address_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ip_address_dotted: If op_ip_address_dotted is specified, the field named in this input will be compared to the value in ip_address_dotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ip_address_dotted must be specified if op_ip_address_dotted is specified.
             :type val_f_ip_address_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ip_address_dotted: If op_ip_address_dotted is specified, this value will be compared to the value in ip_address_dotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ip_address_dotted must be specified if op_ip_address_dotted is specified.
             :type val_c_ip_address_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ip_address_numeric: The operator to apply to the field ip_address_numeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ip_address_numeric: The IP address as number. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ip_address_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ip_address_numeric: If op_ip_address_numeric is specified, the field named in this input will be compared to the value in ip_address_numeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ip_address_numeric must be specified if op_ip_address_numeric is specified.
             :type val_f_ip_address_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ip_address_numeric: If op_ip_address_numeric is specified, this value will be compared to the value in ip_address_numeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ip_address_numeric must be specified if op_ip_address_numeric is specified.
             :type val_c_ip_address_numeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_name: The operator to apply to the field name. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. name: The certificate name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_passphrase: The operator to apply to the field passphrase. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. passphrase: The passphrase for certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_passphrase: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_passphrase: If op_passphrase is specified, the field named in this input will be compared to the value in passphrase using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_passphrase must be specified if op_passphrase is specified.
             :type val_f_passphrase: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_passphrase: If op_passphrase is specified, this value will be compared to the value in passphrase using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_passphrase must be specified if op_passphrase is specified.
             :type val_c_passphrase: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_password: The operator to apply to the field password. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. password: The password for certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_password: If op_password is specified, the field named in this input will be compared to the value in password using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_password must be specified if op_password is specified.
             :type val_f_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_password: If op_password is specified, this value will be compared to the value in password using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_password must be specified if op_password is specified.
             :type val_c_password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_port: The operator to apply to the field port. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. port: Port number to use for connection with this certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_port: If op_port is specified, the field named in this input will be compared to the value in port using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_port must be specified if op_port is specified.
             :type val_f_port: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_port: If op_port is specified, this value will be compared to the value in port using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_port must be specified if op_port is specified.
             :type val_c_port: String

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

             :param op_username: The operator to apply to the field username. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. username: The username for certificate. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_username: If op_username is specified, the field named in this input will be compared to the value in username using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_username must be specified if op_username is specified.
             :type val_f_username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_username: If op_username is specified, this value will be compared to the value in username using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_username must be specified if op_username is specified.
             :type val_c_username: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at.
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

             :param select: The list of attributes to return for each DeviceCertificate. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return device_certificates: An array of the DeviceCertificate objects that match the specified input criteria.
             :rtype device_certificates: Array of DeviceCertificate

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def index(self, **kwargs):
        """Lists the available device certificates. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this device certificate.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at.
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

             :param select: The list of attributes to return for each DeviceCertificate. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return device_certificates: An array of the DeviceCertificate objects that match the specified input criteria.
             :rtype device_certificates: Array of DeviceCertificate

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device certificates matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for collector.
             :type UnitID: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate: The certificate BLOB data.
             :type certificate: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate_parameter: The certificate parameters.
             :type certificate_parameter: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate_type: The type of certificate.
             :type certificate_type: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this device certificate.
             :type id: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address_dotted: The IP address as string.
             :type ip_address_dotted: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address_numeric: The IP address as number.
             :type ip_address_numeric: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The certificate name.
             :type name: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param passphrase: The passphrase for certificate.
             :type passphrase: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: The password for certificate.
             :type password: Array of String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port: Port number to use for connection with this certificate.
             :type port: Array of Integer

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: The username for certificate.
             :type username: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at.
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

             :param select: The list of attributes to return for each DeviceCertificate. Valid values are id, ip_address_dotted, ip_address_numeric, UnitID, certificate_type, name, port, passphrase, username, password, certificate, certificate_parameter, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device certificates, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: UnitID, certificate, certificate_parameter, certificate_type, created_at, id, ip_address_dotted, ip_address_numeric, name, passphrase, password, port, updated_at, username.
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

             :return device_certificates: An array of the DeviceCertificate objects that match the specified input criteria.
             :rtype device_certificates: Array of DeviceCertificate

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified device certificate from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this device certificate.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Creates a new device certificate.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier for collector.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate: The certificate BLOB data.
             :type certificate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate_parameter: The certificate parameters.
             :type certificate_parameter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param certificate_type: The type of certificate.
             :type certificate_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ip_address_dotted: The IP address as string.
             :type ip_address_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address_numeric: The IP address as number.
             :type ip_address_numeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The certificate name.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param passphrase: The passphrase for certificate.
             :type passphrase: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param password: The password for certificate.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param port: Port number to use for connection with this certificate.
             :type port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param username: The username for certificate.
             :type username: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created device certificate.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created device certificate.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created device certificate.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_certificate: The newly created device certificate.
             :rtype device_certificate: DeviceCertificate

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing device certificate.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this device certificate.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier for collector. If omitted, this field will be updated to the default value.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate: The certificate BLOB data. If omitted, this field will not be updated.
             :type certificate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param certificate_parameter: The certificate parameters. If omitted, this field will not be updated.
             :type certificate_parameter: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param certificate_type: The type of certificate.
             :type certificate_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ip_address_dotted: The IP address as string.
             :type ip_address_dotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ip_address_numeric: The IP address as number. If omitted, this field will not be updated.
             :type ip_address_numeric: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The certificate name. If omitted, this field will not be updated.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param passphrase: The passphrase for certificate. If omitted, this field will not be updated.
             :type passphrase: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param password: The password for certificate.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param port: Port number to use for connection with this certificate.
             :type port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param username: The username for certificate.
             :type username: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated device certificate.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated device certificate.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated device certificate.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_certificate: The updated device certificate.
             :rtype device_certificate: DeviceCertificate

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def get_certificate_content(self, **kwargs):
        """Decodes and displays the certificate used for authentication

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: ID of the device certificate credential
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return issuer: Issuer of the certificate
             :rtype issuer: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return subject: Subject of the certificate
             :rtype subject: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return expiry_time: Expiration date of the certificate
             :rtype expiry_time: DateTime

            """

        return self.api_request(self._get_method_fullname("get_certificate_content"), kwargs)

    def test_credentials(self, **kwargs):
        """Tests the assigned device credentials

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: ID of the device certificate credential
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return message: Message returned by the device
             :rtype message: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return test_result: Result of the test : TRUE value means test OK
             :rtype test_result: Boolean

            """

        return self.api_request(self._get_method_fullname("test_credentials"), kwargs)
