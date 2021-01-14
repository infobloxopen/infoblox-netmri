from ..broker import Broker


class DevicePasswordLogBroker(Broker):
    controller = "device_password_logs"

    def index(self, **kwargs):
        """Lists the available device password logs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device password log table information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device password log table information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device password logs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device password log methods. The listed methods will be called on each device password log returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

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
            |  ``default:`` DevicePwLogID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePwLogID. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion.
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

             :param select: The list of attributes to return for each DevicePasswordLog. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion. If empty or omitted, all attributes will be returned.
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

             :return device_password_logs: An array of the DevicePasswordLog objects that match the specified input criteria.
             :rtype device_password_logs: Array of DevicePasswordLog

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device password log.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device password log methods. The listed methods will be called on each device password log returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_password_log: The device password log identified by the specified DevicePwLogID.
             :rtype device_password_log: DevicePasswordLog

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device password logs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device password log table information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device password log table information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogEnablePasswordSecure: The password is enabled for device password log.
             :type DevicePwLogEnablePasswordSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogEnablePasswordSecure: The password is enabled for device password log.
             :type DevicePwLogEnablePasswordSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogPasswordSecure: The password of the device password log.
             :type DevicePwLogPasswordSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogPasswordSecure: The password of the device password log.
             :type DevicePwLogPasswordSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogProtocol: The protocol of the device password log.
             :type DevicePwLogProtocol: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogProtocol: The protocol of the device password log.
             :type DevicePwLogProtocol: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPAuthPWSecure: The SNMP password is authenticated for the device password log.
             :type DevicePwLogSNMPAuthPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPAuthPWSecure: The SNMP password is authenticated for the device password log.
             :type DevicePwLogSNMPAuthPWSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPAuthProto: The SNMP password is authenticated for the device password log.
             :type DevicePwLogSNMPAuthProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPAuthProto: The SNMP password is authenticated for the device password log.
             :type DevicePwLogSNMPAuthProto: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPPrivPWSecure: The SNMP private password of the device password log.
             :type DevicePwLogSNMPPrivPWSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPPrivPWSecure: The SNMP private password of the device password log.
             :type DevicePwLogSNMPPrivPWSecure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPPrivProto: The SNMP private password protocol of the device password log.
             :type DevicePwLogSNMPPrivProto: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogSNMPPrivProto: The SNMP private password protocol of the device password log.
             :type DevicePwLogSNMPPrivProto: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogStatus: The status of the device password log.
             :type DevicePwLogStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogStatus: The status of the device password log.
             :type DevicePwLogStatus: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogTimestamp: The date and time this record was collected or calculated.
             :type DevicePwLogTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogTimestamp: The date and time this record was collected or calculated.
             :type DevicePwLogTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogUsernameSecure: The username of the device password log.
             :type DevicePwLogUsernameSecure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePwLogUsernameSecure: The username of the device password log.
             :type DevicePwLogUsernameSecure: Array of String

            |  ``api version min:`` 2.4
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

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device password logs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device password log methods. The listed methods will be called on each device password log returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

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
            |  ``default:`` DevicePwLogID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePwLogID. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion.
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

             :param select: The list of attributes to return for each DevicePasswordLog. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device password logs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DevicePwLogEnablePasswordSecure, DevicePwLogID, DevicePwLogPasswordSecure, DevicePwLogProtocol, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivPWSecure, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogTimestamp, DevicePwLogUsernameSecure, SecureVersion.
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

             :return device_password_logs: An array of the DevicePasswordLog objects that match the specified input criteria.
             :rtype device_password_logs: Array of DevicePasswordLog

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device password logs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DevicePwLogEnablePasswordSecure, DevicePwLogID, DevicePwLogPasswordSecure, DevicePwLogProtocol, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivPWSecure, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogTimestamp, DevicePwLogUsernameSecure, SecureVersion.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DataSourceID: If op_DataSourceID is specified, the field named in this input will be compared to the value in DataSourceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_f_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DataSourceID: If op_DataSourceID is specified, this value will be compared to the value in DataSourceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DataSourceID must be specified if op_DataSourceID is specified.
             :type val_c_DataSourceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which device password log table information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceID: If op_DeviceID is specified, the field named in this input will be compared to the value in DeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceID must be specified if op_DeviceID is specified.
             :type val_f_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceID: If op_DeviceID is specified, this value will be compared to the value in DeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceID must be specified if op_DeviceID is specified.
             :type val_c_DeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogEnablePasswordSecure: The operator to apply to the field DevicePwLogEnablePasswordSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogEnablePasswordSecure: The password is enabled for device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogEnablePasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogEnablePasswordSecure: If op_DevicePwLogEnablePasswordSecure is specified, the field named in this input will be compared to the value in DevicePwLogEnablePasswordSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogEnablePasswordSecure must be specified if op_DevicePwLogEnablePasswordSecure is specified.
             :type val_f_DevicePwLogEnablePasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogEnablePasswordSecure: If op_DevicePwLogEnablePasswordSecure is specified, this value will be compared to the value in DevicePwLogEnablePasswordSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogEnablePasswordSecure must be specified if op_DevicePwLogEnablePasswordSecure is specified.
             :type val_c_DevicePwLogEnablePasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogID: The operator to apply to the field DevicePwLogID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogID: The internal NetMRI identifier for the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogID: If op_DevicePwLogID is specified, the field named in this input will be compared to the value in DevicePwLogID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogID must be specified if op_DevicePwLogID is specified.
             :type val_f_DevicePwLogID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogID: If op_DevicePwLogID is specified, this value will be compared to the value in DevicePwLogID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogID must be specified if op_DevicePwLogID is specified.
             :type val_c_DevicePwLogID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogPasswordSecure: The operator to apply to the field DevicePwLogPasswordSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogPasswordSecure: The password of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogPasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogPasswordSecure: If op_DevicePwLogPasswordSecure is specified, the field named in this input will be compared to the value in DevicePwLogPasswordSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogPasswordSecure must be specified if op_DevicePwLogPasswordSecure is specified.
             :type val_f_DevicePwLogPasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogPasswordSecure: If op_DevicePwLogPasswordSecure is specified, this value will be compared to the value in DevicePwLogPasswordSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogPasswordSecure must be specified if op_DevicePwLogPasswordSecure is specified.
             :type val_c_DevicePwLogPasswordSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogProtocol: The operator to apply to the field DevicePwLogProtocol. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogProtocol: The protocol of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogProtocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogProtocol: If op_DevicePwLogProtocol is specified, the field named in this input will be compared to the value in DevicePwLogProtocol using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogProtocol must be specified if op_DevicePwLogProtocol is specified.
             :type val_f_DevicePwLogProtocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogProtocol: If op_DevicePwLogProtocol is specified, this value will be compared to the value in DevicePwLogProtocol using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogProtocol must be specified if op_DevicePwLogProtocol is specified.
             :type val_c_DevicePwLogProtocol: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogSNMPAuthPWSecure: The operator to apply to the field DevicePwLogSNMPAuthPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogSNMPAuthPWSecure: The SNMP password is authenticated for the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogSNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogSNMPAuthPWSecure: If op_DevicePwLogSNMPAuthPWSecure is specified, the field named in this input will be compared to the value in DevicePwLogSNMPAuthPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogSNMPAuthPWSecure must be specified if op_DevicePwLogSNMPAuthPWSecure is specified.
             :type val_f_DevicePwLogSNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogSNMPAuthPWSecure: If op_DevicePwLogSNMPAuthPWSecure is specified, this value will be compared to the value in DevicePwLogSNMPAuthPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogSNMPAuthPWSecure must be specified if op_DevicePwLogSNMPAuthPWSecure is specified.
             :type val_c_DevicePwLogSNMPAuthPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogSNMPAuthProto: The operator to apply to the field DevicePwLogSNMPAuthProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogSNMPAuthProto: The SNMP password is authenticated for the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogSNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogSNMPAuthProto: If op_DevicePwLogSNMPAuthProto is specified, the field named in this input will be compared to the value in DevicePwLogSNMPAuthProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogSNMPAuthProto must be specified if op_DevicePwLogSNMPAuthProto is specified.
             :type val_f_DevicePwLogSNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogSNMPAuthProto: If op_DevicePwLogSNMPAuthProto is specified, this value will be compared to the value in DevicePwLogSNMPAuthProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogSNMPAuthProto must be specified if op_DevicePwLogSNMPAuthProto is specified.
             :type val_c_DevicePwLogSNMPAuthProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogSNMPPrivPWSecure: The operator to apply to the field DevicePwLogSNMPPrivPWSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogSNMPPrivPWSecure: The SNMP private password of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogSNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogSNMPPrivPWSecure: If op_DevicePwLogSNMPPrivPWSecure is specified, the field named in this input will be compared to the value in DevicePwLogSNMPPrivPWSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogSNMPPrivPWSecure must be specified if op_DevicePwLogSNMPPrivPWSecure is specified.
             :type val_f_DevicePwLogSNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogSNMPPrivPWSecure: If op_DevicePwLogSNMPPrivPWSecure is specified, this value will be compared to the value in DevicePwLogSNMPPrivPWSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogSNMPPrivPWSecure must be specified if op_DevicePwLogSNMPPrivPWSecure is specified.
             :type val_c_DevicePwLogSNMPPrivPWSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogSNMPPrivProto: The operator to apply to the field DevicePwLogSNMPPrivProto. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogSNMPPrivProto: The SNMP private password protocol of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogSNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogSNMPPrivProto: If op_DevicePwLogSNMPPrivProto is specified, the field named in this input will be compared to the value in DevicePwLogSNMPPrivProto using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogSNMPPrivProto must be specified if op_DevicePwLogSNMPPrivProto is specified.
             :type val_f_DevicePwLogSNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogSNMPPrivProto: If op_DevicePwLogSNMPPrivProto is specified, this value will be compared to the value in DevicePwLogSNMPPrivProto using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogSNMPPrivProto must be specified if op_DevicePwLogSNMPPrivProto is specified.
             :type val_c_DevicePwLogSNMPPrivProto: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogStatus: The operator to apply to the field DevicePwLogStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogStatus: The status of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogStatus: If op_DevicePwLogStatus is specified, the field named in this input will be compared to the value in DevicePwLogStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogStatus must be specified if op_DevicePwLogStatus is specified.
             :type val_f_DevicePwLogStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogStatus: If op_DevicePwLogStatus is specified, this value will be compared to the value in DevicePwLogStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogStatus must be specified if op_DevicePwLogStatus is specified.
             :type val_c_DevicePwLogStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogTimestamp: The operator to apply to the field DevicePwLogTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogTimestamp: If op_DevicePwLogTimestamp is specified, the field named in this input will be compared to the value in DevicePwLogTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogTimestamp must be specified if op_DevicePwLogTimestamp is specified.
             :type val_f_DevicePwLogTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogTimestamp: If op_DevicePwLogTimestamp is specified, this value will be compared to the value in DevicePwLogTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogTimestamp must be specified if op_DevicePwLogTimestamp is specified.
             :type val_c_DevicePwLogTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevicePwLogUsernameSecure: The operator to apply to the field DevicePwLogUsernameSecure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePwLogUsernameSecure: The username of the device password log. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePwLogUsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePwLogUsernameSecure: If op_DevicePwLogUsernameSecure is specified, the field named in this input will be compared to the value in DevicePwLogUsernameSecure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePwLogUsernameSecure must be specified if op_DevicePwLogUsernameSecure is specified.
             :type val_f_DevicePwLogUsernameSecure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePwLogUsernameSecure: If op_DevicePwLogUsernameSecure is specified, this value will be compared to the value in DevicePwLogUsernameSecure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePwLogUsernameSecure must be specified if op_DevicePwLogUsernameSecure is specified.
             :type val_c_DevicePwLogUsernameSecure: String

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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device password logs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device password log methods. The listed methods will be called on each device password log returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

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
            |  ``default:`` DevicePwLogID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePwLogID. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion.
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

             :param select: The list of attributes to return for each DevicePasswordLog. Valid values are DevicePwLogID, DataSourceID, DeviceID, DevicePwLogTimestamp, DevicePwLogProtocol, DevicePwLogSNMPAuthProto, DevicePwLogSNMPPrivProto, DevicePwLogStatus, DevicePwLogUsernameSecure, DevicePwLogPasswordSecure, DevicePwLogEnablePasswordSecure, DevicePwLogSNMPAuthPWSecure, DevicePwLogSNMPPrivPWSecure, SecureVersion. If empty or omitted, all attributes will be returned.
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

             :return device_password_logs: An array of the DevicePasswordLog objects that match the specified input criteria.
             :rtype device_password_logs: Array of DevicePasswordLog

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePwLogID: The internal NetMRI identifier for the device password log.
             :type DevicePwLogID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
