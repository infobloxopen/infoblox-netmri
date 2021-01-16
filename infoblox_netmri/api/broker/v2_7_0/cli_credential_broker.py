from ..broker import Broker


class CLICredentialBroker(Broker):
    controller = "cli_credentials"

    def index(self, **kwargs):
        """Lists the available cli credentials. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each CLICredential. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return cli_credentials: An array of the CLICredential objects that match the specified input criteria.
             :rtype cli_credentials: Array of CLICredential

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified cli credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_credential: The cli credential identified by the specified id.
             :rtype cli_credential: CLICredential

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available cli credentials matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param HitCount: The number of successful uses of this credential.
             :type HitCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param HitCount: The number of successful uses of this credential.
             :type HitCount: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Origination: Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential.
             :type Origination: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Origination: Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential.
             :type Origination: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordSecure: The password portion of the credential.
             :type PasswordSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordSecure: The password portion of the credential.
             :type PasswordSecure: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Priority: The priority order in which to attempt this credential.
             :type Priority: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Priority: The priority order in which to attempt this credential.
             :type Priority: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Protocol: The protocol for which to use this credential.
             :type Protocol: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Protocol: The protocol for which to use this credential.
             :type Protocol: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and password.
             :type SecureVersion: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and password.
             :type SecureVersion: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UPWUse: Determines the function of the credential. 'GUESS' indicates that this will only be used if vendor default credential collection is enabled, whereas 'LOCAL' means that this credential will be used in all guessing.
             :type UPWUse: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UPWUse: Determines the function of the credential. 'GUESS' indicates that this will only be used if vendor default credential collection is enabled, whereas 'LOCAL' means that this credential will be used in all guessing.
             :type UPWUse: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UsernameSecure: The username portion of the credential.
             :type UsernameSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsernameSecure: The username portion of the credential.
             :type UsernameSecure: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each CLICredential. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against cli credentials, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: CredentialGroupID, HitCount, Origination, PasswordSecure, Priority, Protocol, SecureVersion, UPWUse, UnitID, UsernameSecure, Vendor, id.
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

             :return cli_credentials: An array of the CLICredential objects that match the specified input criteria.
             :rtype cli_credentials: Array of CLICredential

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available cli credentials matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: CredentialGroupID, HitCount, Origination, PasswordSecure, Priority, Protocol, SecureVersion, UPWUse, UnitID, UsernameSecure, Vendor, id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CredentialGroupID: The operator to apply to the field CredentialGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CredentialGroupID: The unique identifier of the credential group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CredentialGroupID: If op_CredentialGroupID is specified, the field named in this input will be compared to the value in CredentialGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CredentialGroupID must be specified if op_CredentialGroupID is specified.
             :type val_f_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CredentialGroupID: If op_CredentialGroupID is specified, this value will be compared to the value in CredentialGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CredentialGroupID must be specified if op_CredentialGroupID is specified.
             :type val_c_CredentialGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_HitCount: The operator to apply to the field HitCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. HitCount: The number of successful uses of this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_HitCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_HitCount: If op_HitCount is specified, the field named in this input will be compared to the value in HitCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_HitCount must be specified if op_HitCount is specified.
             :type val_f_HitCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_HitCount: If op_HitCount is specified, this value will be compared to the value in HitCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_HitCount must be specified if op_HitCount is specified.
             :type val_c_HitCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Origination: The operator to apply to the field Origination. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Origination: Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Origination: If op_Origination is specified, the field named in this input will be compared to the value in Origination using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Origination must be specified if op_Origination is specified.
             :type val_f_Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Origination: If op_Origination is specified, this value will be compared to the value in Origination using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Origination must be specified if op_Origination is specified.
             :type val_c_Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PasswordSecure: The operator to apply to the field PasswordSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PasswordSecure: The password portion of the credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PasswordSecure: If op_PasswordSecure is specified, the field named in this input will be compared to the value in PasswordSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PasswordSecure must be specified if op_PasswordSecure is specified.
             :type val_f_PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PasswordSecure: If op_PasswordSecure is specified, this value will be compared to the value in PasswordSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PasswordSecure must be specified if op_PasswordSecure is specified.
             :type val_c_PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Priority: The operator to apply to the field Priority. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Priority: The priority order in which to attempt this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Priority: If op_Priority is specified, the field named in this input will be compared to the value in Priority using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Priority must be specified if op_Priority is specified.
             :type val_f_Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Priority: If op_Priority is specified, this value will be compared to the value in Priority using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Priority must be specified if op_Priority is specified.
             :type val_c_Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Protocol: The operator to apply to the field Protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Protocol: The protocol for which to use this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Protocol: If op_Protocol is specified, the field named in this input will be compared to the value in Protocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Protocol must be specified if op_Protocol is specified.
             :type val_f_Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Protocol: If op_Protocol is specified, this value will be compared to the value in Protocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Protocol must be specified if op_Protocol is specified.
             :type val_c_Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SecureVersion: The operator to apply to the field SecureVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SecureVersion: The encryption version of the username and password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SecureVersion: If op_SecureVersion is specified, the field named in this input will be compared to the value in SecureVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_f_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SecureVersion: If op_SecureVersion is specified, this value will be compared to the value in SecureVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SecureVersion must be specified if op_SecureVersion is specified.
             :type val_c_SecureVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UPWUse: The operator to apply to the field UPWUse. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UPWUse: Determines the function of the credential. 'GUESS' indicates that this will only be used if vendor default credential collection is enabled, whereas 'LOCAL' means that this credential will be used in all guessing. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UPWUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UPWUse: If op_UPWUse is specified, the field named in this input will be compared to the value in UPWUse using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UPWUse must be specified if op_UPWUse is specified.
             :type val_f_UPWUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UPWUse: If op_UPWUse is specified, this value will be compared to the value in UPWUse using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UPWUse must be specified if op_UPWUse is specified.
             :type val_c_UPWUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnitID: The operator to apply to the field UnitID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_UsernameSecure: The operator to apply to the field UsernameSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UsernameSecure: The username portion of the credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UsernameSecure: If op_UsernameSecure is specified, the field named in this input will be compared to the value in UsernameSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UsernameSecure must be specified if op_UsernameSecure is specified.
             :type val_f_UsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UsernameSecure: If op_UsernameSecure is specified, this value will be compared to the value in UsernameSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UsernameSecure must be specified if op_UsernameSecure is specified.
             :type val_c_UsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Vendor: The operator to apply to the field Vendor. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Vendor: The vendor devices against which to try this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Vendor: If op_Vendor is specified, the field named in this input will be compared to the value in Vendor using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Vendor must be specified if op_Vendor is specified.
             :type val_f_Vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Vendor: If op_Vendor is specified, this value will be compared to the value in Vendor using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Vendor must be specified if op_Vendor is specified.
             :type val_c_Vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each CLICredential. Valid values are UnitID, Protocol, Origination, UPWUse, HitCount, Vendor, id, Priority, UsernameSecure, PasswordSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return cli_credentials: An array of the CLICredential objects that match the specified input criteria.
             :rtype cli_credentials: Array of CLICredential

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a new cli credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` USER

             :param Origination: Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential.
             :type Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PasswordSecure: The password portion of the credential.
             :type PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Priority: The priority order in which to attempt this credential.
             :type Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` ANY

             :param Protocol: The protocol for which to use this credential.
             :type Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` LOCAL

             :param UPWUse: Determines the function of the credential. 'GUESS' indicates that this will only be used if vendor default credential collection is enabled, whereas 'LOCAL' means that this credential will be used in all guessing.
             :type UPWUse: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsernameSecure: The username portion of the credential.
             :type UsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` ANY

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created cli credential.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created cli credential.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created cli credential.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_credential: The newly created cli credential.
             :rtype cli_credential: CLICredential

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing cli credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CredentialGroupID: The unique identifier of the credential group. If omitted, this field will not be updated.
             :type CredentialGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Origination: Identifies the source of the credential. 'NETC' indicates an internal credential that may be modified or removed during upgrade processes. 'USER' indicates a user-entered credential. If omitted, this field will not be updated.
             :type Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordSecure: The password portion of the credential. If omitted, this field will not be updated.
             :type PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Priority: The priority order in which to attempt this credential. If omitted, this field will not be updated.
             :type Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Protocol: The protocol for which to use this credential. If omitted, this field will not be updated.
             :type Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured. If omitted, this field will not be updated.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsernameSecure: The username portion of the credential. If omitted, this field will not be updated.
             :type UsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Vendor: The vendor devices against which to try this credential. If omitted, this field will not be updated.
             :type Vendor: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated cli credential.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated cli credential.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated cli credential.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_credential: The updated cli credential.
             :rtype cli_credential: CLICredential

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified cli credential from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this credential.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)
