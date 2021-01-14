from ..broker import Broker


class SNMPCredentialBroker(Broker):
    controller = "snmp_credentials"

    def index(self, **kwargs):
        """Lists the available snmp credentials. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Array of Integer

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
            |  ``default:`` PasswordID

             :param sort: The data field(s) to use for sorting the output. Default is PasswordID. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each SNMPCredential. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return snmp_credentials: An array of the SNMPCredential objects that match the specified input criteria.
             :rtype snmp_credentials: Array of SNMPCredential

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available snmp credentials matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param Origination: Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential.
             :type Origination: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Origination: Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential.
             :type Origination: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordSecure: (alias Password) Is the community string.
             :type PasswordSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PasswordSecure: (alias Password) Is the community string.
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

             :param Protocol: The protocol for which to use this password.
             :type Protocol: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Protocol: The protocol for which to use this password.
             :type Protocol: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPWSecure: (alias SNMPAuthPW) Is the SNMPv3 authentication protocol password.
             :type SNMPAuthPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthPWSecure: (alias SNMPAuthPW) Is the SNMPv3 authentication protocol password.
             :type SNMPAuthPWSecure: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential.
             :type SNMPAuthProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential.
             :type SNMPAuthProto: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPWSecure: (alias SNMPPrivPW) Is the SNMPv3 privacy protocol password.
             :type SNMPPrivPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivPWSecure: (alias SNMPPrivPW) Is the SNMPv3 privacy protocol password.
             :type SNMPPrivPWSecure: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential.
             :type SNMPPrivProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential.
             :type SNMPPrivProto: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and passwords.
             :type SecureVersion: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SecureVersion: The encryption version of the username and passwords.
             :type SecureVersion: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Type: Whether this is a read or read/write community.
             :type Type: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Type: Whether this is a read or read/write community.
             :type Type: Array of String

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

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: Array of String

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
            |  ``default:`` PasswordID

             :param sort: The data field(s) to use for sorting the output. Default is PasswordID. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each SNMPCredential. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against snmp credentials, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: CredentialGroupID, HitCount, Origination, PasswordID, Priority, Protocol, SNMPAuthProto, SNMPPrivProto, Type, UnitID, Vendor.
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

             :return snmp_credentials: An array of the SNMPCredential objects that match the specified input criteria.
             :rtype snmp_credentials: Array of SNMPCredential

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available snmp credentials matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: CredentialGroupID, HitCount, Origination, PasswordID, PasswordSecure, Priority, Protocol, SNMPAuthPWSecure, SNMPAuthProto, SNMPPrivPWSecure, SNMPPrivProto, SecureVersion, Type, UnitID, Vendor.

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

             :param op_Origination: The operator to apply to the field Origination. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Origination: Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_PasswordID: The operator to apply to the field PasswordID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PasswordID: The internal NetMRI identifier for this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PasswordID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PasswordID: If op_PasswordID is specified, the field named in this input will be compared to the value in PasswordID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PasswordID must be specified if op_PasswordID is specified.
             :type val_f_PasswordID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PasswordID: If op_PasswordID is specified, this value will be compared to the value in PasswordID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PasswordID must be specified if op_PasswordID is specified.
             :type val_c_PasswordID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PasswordSecure: The operator to apply to the field PasswordSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PasswordSecure: (alias Password) Is the community string. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Protocol: The operator to apply to the field Protocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Protocol: The protocol for which to use this password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SNMPAuthPWSecure: The operator to apply to the field SNMPAuthPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPAuthPWSecure: (alias SNMPAuthPW) Is the SNMPv3 authentication protocol password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPAuthPWSecure: If op_SNMPAuthPWSecure is specified, the field named in this input will be compared to the value in SNMPAuthPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPAuthPWSecure must be specified if op_SNMPAuthPWSecure is specified.
             :type val_f_SNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPAuthPWSecure: If op_SNMPAuthPWSecure is specified, this value will be compared to the value in SNMPAuthPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPAuthPWSecure must be specified if op_SNMPAuthPWSecure is specified.
             :type val_c_SNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPAuthProto: The operator to apply to the field SNMPAuthProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPAuthProto: If op_SNMPAuthProto is specified, the field named in this input will be compared to the value in SNMPAuthProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPAuthProto must be specified if op_SNMPAuthProto is specified.
             :type val_f_SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPAuthProto: If op_SNMPAuthProto is specified, this value will be compared to the value in SNMPAuthProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPAuthProto must be specified if op_SNMPAuthProto is specified.
             :type val_c_SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPPrivPWSecure: The operator to apply to the field SNMPPrivPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPrivPWSecure: (alias SNMPPrivPW) Is the SNMPv3 privacy protocol password. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPPrivPWSecure: If op_SNMPPrivPWSecure is specified, the field named in this input will be compared to the value in SNMPPrivPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPPrivPWSecure must be specified if op_SNMPPrivPWSecure is specified.
             :type val_f_SNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPPrivPWSecure: If op_SNMPPrivPWSecure is specified, this value will be compared to the value in SNMPPrivPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPPrivPWSecure must be specified if op_SNMPPrivPWSecure is specified.
             :type val_c_SNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPPrivProto: The operator to apply to the field SNMPPrivProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPPrivProto: If op_SNMPPrivProto is specified, the field named in this input will be compared to the value in SNMPPrivProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPPrivProto must be specified if op_SNMPPrivProto is specified.
             :type val_f_SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPPrivProto: If op_SNMPPrivProto is specified, this value will be compared to the value in SNMPPrivProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPPrivProto must be specified if op_SNMPPrivProto is specified.
             :type val_c_SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SecureVersion: The operator to apply to the field SecureVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SecureVersion: The encryption version of the username and passwords. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Type: The operator to apply to the field Type. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Type: Whether this is a read or read/write community. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Type: If op_Type is specified, the field named in this input will be compared to the value in Type using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Type must be specified if op_Type is specified.
             :type val_f_Type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Type: If op_Type is specified, this value will be compared to the value in Type using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Type must be specified if op_Type is specified.
             :type val_c_Type: String

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
            |  ``default:`` PasswordID

             :param sort: The data field(s) to use for sorting the output. Default is PasswordID. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID.
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

             :param select: The list of attributes to return for each SNMPCredential. Valid values are PasswordID, UnitID, Protocol, Type, Origination, HitCount, Vendor, SNMPAuthProto, SNMPPrivProto, Priority, PasswordSecure, SNMPAuthPWSecure, SNMPPrivPWSecure, SecureVersion, CredentialGroupID. If empty or omitted, all attributes will be returned.
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

             :return snmp_credentials: An array of the SNMPCredential objects that match the specified input criteria.
             :rtype snmp_credentials: Array of SNMPCredential

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified snmp credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_credential: The snmp credential identified by the specified PasswordID.
             :rtype snmp_credential: SNMPCredential

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Creates a new snmp credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param CredentialGroupID: The unique identifier of the credential group.
             :type CredentialGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Origination: Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential.
             :type Origination: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PasswordSecure: (alias Password) Is the community string.
             :type PasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Priority: The priority order in which to attempt this credential.
             :type Priority: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Protocol: The protocol for which to use this password.
             :type Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPAuthPWSecure: (alias SNMPAuthPW) Is the SNMPv3 authentication protocol password.
             :type SNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential.
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPPrivPWSecure: (alias SNMPPrivPW) Is the SNMPv3 privacy protocol password.
             :type SNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential.
             :type SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Type: Whether this is a read or read/write community.
             :type Type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier for the NetMRI collector on which the credential is configured.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Vendor: The vendor devices against which to try this credential.
             :type Vendor: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created snmp credential.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created snmp credential.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created snmp credential.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_credential: The newly created snmp credential.
             :rtype snmp_credential: SNMPCredential

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing snmp credential.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Integer

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

             :param Origination: Indicates the source and use of the credential. 'User' indicates this is a user-entered password. 'Default' indicates that these are used by the Weak Password issue, and may be modified or removed on upgrade. 'Vendor' indicates a password tested in the Vendor Default Credential Guessing, and may be modified or removed on upgrade. 'Vendor (User Add)' is a user-added vendor default credential. If omitted, this field will not be updated.
             :type Origination: String

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

             :param Protocol: The protocol for which to use this password. If omitted, this field will not be updated.
             :type Protocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPAuthProto: The SNMPv3 authentication protocol to use with this credential. If omitted, this field will not be updated.
             :type SNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPrivProto: The SNMPv3 privacy protocol to use with this credential. If omitted, this field will not be updated.
             :type SNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Type: Whether this is a read or read/write community. If omitted, this field will not be updated.
             :type Type: String

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

             :param Vendor: The vendor devices against which to try this credential. If omitted, this field will not be updated.
             :type Vendor: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated snmp credential.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated snmp credential.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated snmp credential.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return snmp_credential: The updated snmp credential.
             :rtype snmp_credential: SNMPCredential

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified snmp credential from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PasswordID: The internal NetMRI identifier for this credential.
             :type PasswordID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)
