from ..broker import Broker


class DetectedChangeBroker(Broker):
    controller = "detected_changes"

    def show(self, **kwargs):
        """Shows the details for the specified detected change.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of detected change methods. The listed methods will be called on each detected change returned and included in the output. Available methods are: meta, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detected_change: The detected change identified by the specified ChangeID.
             :rtype detected_change: DetectedChange

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available detected changes. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTime: The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
             :type ChangeTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTime: The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
             :type ChangeTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeUser: The user that made the change, if available.
             :type ChangeUser: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeUser: The user that made the change, if available.
             :type ChangeUser: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that changed.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that changed.
             :type DeviceID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the detected changes with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the detected changes with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of detected change methods. The listed methods will be called on each detected change returned and included in the output. Available methods are: meta, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device.
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
            |  ``default:`` ChangeID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeID. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID.
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

             :param select: The list of attributes to return for each DetectedChange. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID. If empty or omitted, all attributes will be returned.
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

             :return detected_changes: An array of the DetectedChange objects that match the specified input criteria.
             :rtype detected_changes: Array of DetectedChange

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available detected changes matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AccessInd: A flag indicating an access (Security Filtering) change.
             :type AccessInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessInd: A flag indicating an access (Security Filtering) change.
             :type AccessInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param AdminInd: A flag indicating an administrative change.
             :type AdminInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AdminInd: A flag indicating an administrative change.
             :type AdminInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeAuthorizedInd: A flag indicating if the change is authorized or not.
             :type ChangeAuthorizedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeAuthorizedInd: A flag indicating if the change is authorized or not.
             :type ChangeAuthorizedInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeDesc: A description of the change.
             :type ChangeDesc: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeDesc: A description of the change.
             :type ChangeDesc: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeDetectedTime: The date/time the change was detected. That is, the end time of the Change Window.
             :type ChangeDetectedTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeDetectedTime: The date/time the change was detected. That is, the end time of the Change Window.
             :type ChangeDetectedTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTime: The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
             :type ChangeTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTime: The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
             :type ChangeTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTimeActualInd: A flag indicating if the ChangeTime field is the same as the ChangeDetectedTime field.
             :type ChangeTimeActualInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTimeActualInd: A flag indicating if the ChangeTime field is the same as the ChangeDetectedTime field.
             :type ChangeTimeActualInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier of the FIRST change trace that generated this change.
             :type ChangeTraceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeTraceID: The internal NetMRI identifier of the FIRST change trace that generated this change.
             :type ChangeTraceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeUser: The user that made the change, if available.
             :type ChangeUser: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChangeUser: The user that made the change, if available.
             :type ChangeUser: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigPollInd: A flag indicating that this change was detected, at least in part, by differences found between configuration file retrievals.
             :type ConfigPollInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigPollInd: A flag indicating that this change was detected, at least in part, by differences found between configuration file retrievals.
             :type ConfigPollInd: Array of Boolean

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that changed.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that changed.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ExternalInd: A flag indicating an external change.
             :type ExternalInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ExternalInd: A flag indicating an external change.
             :type ExternalInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param HardwareInd: A flag indicating a hardware change.
             :type HardwareInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param HardwareInd: A flag indicating a hardware change.
             :type HardwareInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPollInd: A flag indicating that this change was detected, at least in part, via differences between SNMP polls.
             :type SNMPPollInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPPollInd: A flag indicating that this change was detected, at least in part, via differences between SNMP polls.
             :type SNMPPollInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPTrapInd: A flag indicating that this change was detected, at least in part, via an SNMP trap (not currently supported).
             :type SNMPTrapInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SNMPTrapInd: A flag indicating that this change was detected, at least in part, via an SNMP trap (not currently supported).
             :type SNMPTrapInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SoftwareInd: A flag indicating a software change.
             :type SoftwareInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SoftwareInd: A flag indicating a software change.
             :type SoftwareInd: Array of Boolean

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogInd: A flag indicating that this change was detected, at least in part, via a Syslog message.
             :type SyslogInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SyslogInd: A flag indicating that this change was detected, at least in part, via a Syslog message.
             :type SyslogInd: Array of Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the detected changes with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the detected changes with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of detected change methods. The listed methods will be called on each detected change returned and included in the output. Available methods are: meta, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device.
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
            |  ``default:`` ChangeID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeID. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID.
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

             :param select: The list of attributes to return for each DetectedChange. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against detected changes, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: AccessInd, AdminInd, ChangeAuthorizedInd, ChangeDesc, ChangeDetectedTime, ChangeID, ChangeTime, ChangeTimeActualInd, ChangeTraceID, ChangeUser, ConfigPollInd, DataSourceID, DeviceID, ExternalInd, HardwareInd, SNMPPollInd, SNMPTrapInd, SoftwareInd, SyslogInd.
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

             :return detected_changes: An array of the DetectedChange objects that match the specified input criteria.
             :rtype detected_changes: Array of DetectedChange

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available detected changes matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: AccessInd, AdminInd, ChangeAuthorizedInd, ChangeDesc, ChangeDetectedTime, ChangeID, ChangeTime, ChangeTimeActualInd, ChangeTraceID, ChangeUser, ConfigPollInd, DataSourceID, DeviceID, ExternalInd, HardwareInd, SNMPPollInd, SNMPTrapInd, SoftwareInd, SyslogInd.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AccessInd: The operator to apply to the field AccessInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AccessInd: A flag indicating an access (Security Filtering) change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AccessInd: If op_AccessInd is specified, the field named in this input will be compared to the value in AccessInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AccessInd must be specified if op_AccessInd is specified.
             :type val_f_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AccessInd: If op_AccessInd is specified, this value will be compared to the value in AccessInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AccessInd must be specified if op_AccessInd is specified.
             :type val_c_AccessInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AdminInd: The operator to apply to the field AdminInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AdminInd: A flag indicating an administrative change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AdminInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AdminInd: If op_AdminInd is specified, the field named in this input will be compared to the value in AdminInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AdminInd must be specified if op_AdminInd is specified.
             :type val_f_AdminInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AdminInd: If op_AdminInd is specified, this value will be compared to the value in AdminInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AdminInd must be specified if op_AdminInd is specified.
             :type val_c_AdminInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeAuthorizedInd: The operator to apply to the field ChangeAuthorizedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeAuthorizedInd: A flag indicating if the change is authorized or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeAuthorizedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeAuthorizedInd: If op_ChangeAuthorizedInd is specified, the field named in this input will be compared to the value in ChangeAuthorizedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeAuthorizedInd must be specified if op_ChangeAuthorizedInd is specified.
             :type val_f_ChangeAuthorizedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeAuthorizedInd: If op_ChangeAuthorizedInd is specified, this value will be compared to the value in ChangeAuthorizedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeAuthorizedInd must be specified if op_ChangeAuthorizedInd is specified.
             :type val_c_ChangeAuthorizedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeDesc: The operator to apply to the field ChangeDesc. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeDesc: A description of the change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeDesc: If op_ChangeDesc is specified, the field named in this input will be compared to the value in ChangeDesc using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeDesc must be specified if op_ChangeDesc is specified.
             :type val_f_ChangeDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeDesc: If op_ChangeDesc is specified, this value will be compared to the value in ChangeDesc using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeDesc must be specified if op_ChangeDesc is specified.
             :type val_c_ChangeDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeDetectedTime: The operator to apply to the field ChangeDetectedTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeDetectedTime: The date/time the change was detected. That is, the end time of the Change Window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeDetectedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeDetectedTime: If op_ChangeDetectedTime is specified, the field named in this input will be compared to the value in ChangeDetectedTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeDetectedTime must be specified if op_ChangeDetectedTime is specified.
             :type val_f_ChangeDetectedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeDetectedTime: If op_ChangeDetectedTime is specified, this value will be compared to the value in ChangeDetectedTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeDetectedTime must be specified if op_ChangeDetectedTime is specified.
             :type val_c_ChangeDetectedTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeID: The operator to apply to the field ChangeID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeID: The internal NetMRI identifier for this change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeID: If op_ChangeID is specified, the field named in this input will be compared to the value in ChangeID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeID must be specified if op_ChangeID is specified.
             :type val_f_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeID: If op_ChangeID is specified, this value will be compared to the value in ChangeID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeID must be specified if op_ChangeID is specified.
             :type val_c_ChangeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTime: The operator to apply to the field ChangeTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTime: The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTime: If op_ChangeTime is specified, the field named in this input will be compared to the value in ChangeTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTime must be specified if op_ChangeTime is specified.
             :type val_f_ChangeTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTime: If op_ChangeTime is specified, this value will be compared to the value in ChangeTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTime must be specified if op_ChangeTime is specified.
             :type val_c_ChangeTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTimeActualInd: The operator to apply to the field ChangeTimeActualInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTimeActualInd: A flag indicating if the ChangeTime field is the same as the ChangeDetectedTime field. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTimeActualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTimeActualInd: If op_ChangeTimeActualInd is specified, the field named in this input will be compared to the value in ChangeTimeActualInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTimeActualInd must be specified if op_ChangeTimeActualInd is specified.
             :type val_f_ChangeTimeActualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTimeActualInd: If op_ChangeTimeActualInd is specified, this value will be compared to the value in ChangeTimeActualInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTimeActualInd must be specified if op_ChangeTimeActualInd is specified.
             :type val_c_ChangeTimeActualInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeTraceID: The operator to apply to the field ChangeTraceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeTraceID: The internal NetMRI identifier of the FIRST change trace that generated this change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeTraceID: If op_ChangeTraceID is specified, the field named in this input will be compared to the value in ChangeTraceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeTraceID must be specified if op_ChangeTraceID is specified.
             :type val_f_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeTraceID: If op_ChangeTraceID is specified, this value will be compared to the value in ChangeTraceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeTraceID must be specified if op_ChangeTraceID is specified.
             :type val_c_ChangeTraceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChangeUser: The operator to apply to the field ChangeUser. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChangeUser: The user that made the change, if available. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChangeUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChangeUser: If op_ChangeUser is specified, the field named in this input will be compared to the value in ChangeUser using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChangeUser must be specified if op_ChangeUser is specified.
             :type val_f_ChangeUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChangeUser: If op_ChangeUser is specified, this value will be compared to the value in ChangeUser using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChangeUser must be specified if op_ChangeUser is specified.
             :type val_c_ChangeUser: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigPollInd: The operator to apply to the field ConfigPollInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigPollInd: A flag indicating that this change was detected, at least in part, by differences found between configuration file retrievals. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigPollInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigPollInd: If op_ConfigPollInd is specified, the field named in this input will be compared to the value in ConfigPollInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigPollInd must be specified if op_ConfigPollInd is specified.
             :type val_f_ConfigPollInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigPollInd: If op_ConfigPollInd is specified, this value will be compared to the value in ConfigPollInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigPollInd must be specified if op_ConfigPollInd is specified.
             :type val_c_ConfigPollInd: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device that changed. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_ExternalInd: The operator to apply to the field ExternalInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ExternalInd: A flag indicating an external change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ExternalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ExternalInd: If op_ExternalInd is specified, the field named in this input will be compared to the value in ExternalInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ExternalInd must be specified if op_ExternalInd is specified.
             :type val_f_ExternalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ExternalInd: If op_ExternalInd is specified, this value will be compared to the value in ExternalInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ExternalInd must be specified if op_ExternalInd is specified.
             :type val_c_ExternalInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_HardwareInd: The operator to apply to the field HardwareInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. HardwareInd: A flag indicating a hardware change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_HardwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_HardwareInd: If op_HardwareInd is specified, the field named in this input will be compared to the value in HardwareInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_HardwareInd must be specified if op_HardwareInd is specified.
             :type val_f_HardwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_HardwareInd: If op_HardwareInd is specified, this value will be compared to the value in HardwareInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_HardwareInd must be specified if op_HardwareInd is specified.
             :type val_c_HardwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPPollInd: The operator to apply to the field SNMPPollInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPPollInd: A flag indicating that this change was detected, at least in part, via differences between SNMP polls. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPPollInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPPollInd: If op_SNMPPollInd is specified, the field named in this input will be compared to the value in SNMPPollInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPPollInd must be specified if op_SNMPPollInd is specified.
             :type val_f_SNMPPollInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPPollInd: If op_SNMPPollInd is specified, this value will be compared to the value in SNMPPollInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPPollInd must be specified if op_SNMPPollInd is specified.
             :type val_c_SNMPPollInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SNMPTrapInd: The operator to apply to the field SNMPTrapInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SNMPTrapInd: A flag indicating that this change was detected, at least in part, via an SNMP trap (not currently supported). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SNMPTrapInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SNMPTrapInd: If op_SNMPTrapInd is specified, the field named in this input will be compared to the value in SNMPTrapInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SNMPTrapInd must be specified if op_SNMPTrapInd is specified.
             :type val_f_SNMPTrapInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SNMPTrapInd: If op_SNMPTrapInd is specified, this value will be compared to the value in SNMPTrapInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SNMPTrapInd must be specified if op_SNMPTrapInd is specified.
             :type val_c_SNMPTrapInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SoftwareInd: The operator to apply to the field SoftwareInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SoftwareInd: A flag indicating a software change. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SoftwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SoftwareInd: If op_SoftwareInd is specified, the field named in this input will be compared to the value in SoftwareInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SoftwareInd must be specified if op_SoftwareInd is specified.
             :type val_f_SoftwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SoftwareInd: If op_SoftwareInd is specified, this value will be compared to the value in SoftwareInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SoftwareInd must be specified if op_SoftwareInd is specified.
             :type val_c_SoftwareInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SyslogInd: The operator to apply to the field SyslogInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SyslogInd: A flag indicating that this change was detected, at least in part, via a Syslog message. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SyslogInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SyslogInd: If op_SyslogInd is specified, the field named in this input will be compared to the value in SyslogInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SyslogInd must be specified if op_SyslogInd is specified.
             :type val_f_SyslogInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SyslogInd: If op_SyslogInd is specified, this value will be compared to the value in SyslogInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SyslogInd must be specified if op_SyslogInd is specified.
             :type val_c_SyslogInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The data returned will represent the detected changes with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the detected changes with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of detected change methods. The listed methods will be called on each detected change returned and included in the output. Available methods are: meta, data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta, data_source, device.
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
            |  ``default:`` ChangeID

             :param sort: The data field(s) to use for sorting the output. Default is ChangeID. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID.
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

             :param select: The list of attributes to return for each DetectedChange. Valid values are DataSourceID, ChangeID, DeviceID, ChangeTime, ChangeDetectedTime, ChangeTimeActualInd, ChangeUser, HardwareInd, AdminInd, SoftwareInd, ExternalInd, AccessInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, ChangeDesc, ChangeAuthorizedInd, ChangeTraceID. If empty or omitted, all attributes will be returned.
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

             :return detected_changes: An array of the DetectedChange objects that match the specified input criteria.
             :rtype detected_changes: Array of DetectedChange

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing detected change.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated detected change.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated detected change.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated detected change.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detected_change: The updated detected change.
             :rtype detected_change: DetectedChange

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The NetMRI device that collected this record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def infradevice(self, **kwargs):
        """The device that changed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device that changed.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device that changed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ChangeID: The internal NetMRI identifier for this change.
             :type ChangeID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device that changed.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def count_device_changes(self, **kwargs):
        """Returns a count of detected changes for a specified device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal NetMRI identifier of the device.
             :type device_id: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The start date for which to retrieve the changes.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` now

             :param endtime: The end date for which to retrieve the changes.
             :type endtime: DateTime

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detected_changes_per_device: Array of hashes that contain a Total, Authorized, Unauthorized, and DeviceID.
             :rtype detected_changes_per_device: Array

            """

        return self.api_request(self._get_method_fullname("count_device_changes"), kwargs)

    def detected_changes_chart_data(self, **kwargs):
        """Returns changes data by type to buid ExtJS chart.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal NetMRI identifier of the device.
             :type device_id: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The start date for which to retrieve the changes.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` now

             :param endtime: The end date for which to retrieve the changes.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` Weekly

             :param TimePeriod: The time period for which to retrieve the changes.
             :type TimePeriod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param group_ids: The internal NetMRI group identifiers, seporated by commas.
             :type group_ids: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param change_ids: The internal NetMRI changes identifiers, seporated by commas.
             :type change_ids: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param gromit: A flag indicating to show changes only for security control devices.
             :type gromit: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("detected_changes_chart_data"), kwargs)

    def top_ten_chart_data(self, **kwargs):
        """Returns changes data for top ten changing devices to buid ExtJS chart.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: The internal NetMRI identifier of the device.
             :type device_id: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 30 days ago

             :param starttime: The start date for which to retrieve the changes.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` now

             :param endtime: The end date for which to retrieve the changes.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` ChangeUser

             :param top_ten_type: The type to group changes by (user or device), valid values are 'Devices' and 'ChangeUser'.
             :type top_ten_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` Weekly

             :param TimePeriod: The time period for which to retrieve the changes.
             :type TimePeriod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param group_ids: The internal NetMRI group identifiers, seporated by commas.
             :type group_ids: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param change_ids: The internal NetMRI changes identifiers, seporated by commas.
             :type change_ids: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("top_ten_chart_data"), kwargs)
