from ..broker import Broker


class DeviceEnvironmentMonitorBroker(Broker):
    controller = "device_environment_monitors"

    def index(self, **kwargs):
        """Lists the available device environment monitors. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device environment information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device environment information was collected.
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
            |  ``default:`` None

             :param timestamp: The data returned will represent the device environment monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device environment monitor methods. The listed methods will be called on each device environment monitor returned and included in the output. Available methods are: device.
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
            |  ``default:`` DevEnvMonID

             :param sort: The data field(s) to use for sorting the output. Default is DevEnvMonID. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert.
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

             :param select: The list of attributes to return for each DeviceEnvironmentMonitor. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert. If empty or omitted, all attributes will be returned.
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

             :return device_environment_monitors: An array of the DeviceEnvironmentMonitor objects that match the specified input criteria.
             :rtype device_environment_monitors: Array of DeviceEnvironmentMonitor

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device environment monitor.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device environment monitor methods. The listed methods will be called on each device environment monitor returned and included in the output. Available methods are: device.
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

             :return device_environment_monitor: The device environment monitor identified by the specified DevEnvMonID.
             :rtype device_environment_monitor: DeviceEnvironmentMonitor

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device environment monitors matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DevEnvMonChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevEnvMonChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DevEnvMonChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonDescr: The NetMRI-determined description of the device environment monitor.
             :type DevEnvMonDescr: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonDescr: The NetMRI-determined description of the device environment monitor.
             :type DevEnvMonDescr: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevEnvMonEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonEndTime: The ending effective time of this record, or empty if still in effect.
             :type DevEnvMonEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonHighShutdown: The high value of the shut down process in the device environment monitor.
             :type DevEnvMonHighShutdown: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonHighShutdown: The high value of the shut down process in the device environment monitor.
             :type DevEnvMonHighShutdown: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonHighWarnVal: The high value of the warning message in the device environment monitor.
             :type DevEnvMonHighWarnVal: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonHighWarnVal: The high value of the warning message in the device environment monitor.
             :type DevEnvMonHighWarnVal: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonIndex: The index of the device in the device environment.
             :type DevEnvMonIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonIndex: The index of the device in the device environment.
             :type DevEnvMonIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonLowShutdown: The low value of the shut down process in the device environment monitor.
             :type DevEnvMonLowShutdown: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonLowShutdown: The low value of the shut down process in the device environment monitor.
             :type DevEnvMonLowShutdown: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonLowWarnVal: The low value of the warning message in the device environment monitor.
             :type DevEnvMonLowWarnVal: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonLowWarnVal: The low value of the warning message in the device environment monitor.
             :type DevEnvMonLowWarnVal: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonMeasure: The measure of the device environment monitor.
             :type DevEnvMonMeasure: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonMeasure: The measure of the device environment monitor.
             :type DevEnvMonMeasure: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStartTime: The starting effective time of this record.
             :type DevEnvMonStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStartTime: The starting effective time of this record.
             :type DevEnvMonStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonState: The current state of the device in the device environment monitor.
             :type DevEnvMonState: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonState: The current state of the device in the device environment monitor.
             :type DevEnvMonState: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatus: The status of the device in the Device Environment Monitor.
             :type DevEnvMonStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatus: The status of the device in the Device Environment Monitor.
             :type DevEnvMonStatus: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatusAlert: The alert status of the device environment monitor.
             :type DevEnvMonStatusAlert: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatusAlert: The alert status of the device environment monitor.
             :type DevEnvMonStatusAlert: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatusMessage: The status message of the device environment monitor.
             :type DevEnvMonStatusMessage: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonStatusMessage: The status message of the device environment monitor.
             :type DevEnvMonStatusMessage: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonTimestamp: The date and time this record was collected or calculated.
             :type DevEnvMonTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonTimestamp: The date and time this record was collected or calculated.
             :type DevEnvMonTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonType: The NetMRI-determined monitor type of Device Environment.
             :type DevEnvMonType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevEnvMonType: The NetMRI-determined monitor type of Device Environment.
             :type DevEnvMonType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device environment information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which device environment information was collected.
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
            |  ``default:`` None

             :param timestamp: The data returned will represent the device environment monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device environment monitor methods. The listed methods will be called on each device environment monitor returned and included in the output. Available methods are: device.
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
            |  ``default:`` DevEnvMonID

             :param sort: The data field(s) to use for sorting the output. Default is DevEnvMonID. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert.
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

             :param select: The list of attributes to return for each DeviceEnvironmentMonitor. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device environment monitors, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DevEnvMonChangedCols, DevEnvMonDescr, DevEnvMonEndTime, DevEnvMonHighShutdown, DevEnvMonHighWarnVal, DevEnvMonID, DevEnvMonIndex, DevEnvMonLowShutdown, DevEnvMonLowWarnVal, DevEnvMonMeasure, DevEnvMonStartTime, DevEnvMonState, DevEnvMonStatus, DevEnvMonStatusAlert, DevEnvMonStatusMessage, DevEnvMonTimestamp, DevEnvMonType, DeviceID.
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

             :return device_environment_monitors: An array of the DeviceEnvironmentMonitor objects that match the specified input criteria.
             :rtype device_environment_monitors: Array of DeviceEnvironmentMonitor

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device environment monitors matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DevEnvMonChangedCols, DevEnvMonDescr, DevEnvMonEndTime, DevEnvMonHighShutdown, DevEnvMonHighWarnVal, DevEnvMonID, DevEnvMonIndex, DevEnvMonLowShutdown, DevEnvMonLowWarnVal, DevEnvMonMeasure, DevEnvMonStartTime, DevEnvMonState, DevEnvMonStatus, DevEnvMonStatusAlert, DevEnvMonStatusMessage, DevEnvMonTimestamp, DevEnvMonType, DeviceID.

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

             :param op_DevEnvMonChangedCols: The operator to apply to the field DevEnvMonChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonChangedCols: If op_DevEnvMonChangedCols is specified, the field named in this input will be compared to the value in DevEnvMonChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonChangedCols must be specified if op_DevEnvMonChangedCols is specified.
             :type val_f_DevEnvMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonChangedCols: If op_DevEnvMonChangedCols is specified, this value will be compared to the value in DevEnvMonChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonChangedCols must be specified if op_DevEnvMonChangedCols is specified.
             :type val_c_DevEnvMonChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonDescr: The operator to apply to the field DevEnvMonDescr. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonDescr: The NetMRI-determined description of the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonDescr: If op_DevEnvMonDescr is specified, the field named in this input will be compared to the value in DevEnvMonDescr using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonDescr must be specified if op_DevEnvMonDescr is specified.
             :type val_f_DevEnvMonDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonDescr: If op_DevEnvMonDescr is specified, this value will be compared to the value in DevEnvMonDescr using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonDescr must be specified if op_DevEnvMonDescr is specified.
             :type val_c_DevEnvMonDescr: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonEndTime: The operator to apply to the field DevEnvMonEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonEndTime: If op_DevEnvMonEndTime is specified, the field named in this input will be compared to the value in DevEnvMonEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonEndTime must be specified if op_DevEnvMonEndTime is specified.
             :type val_f_DevEnvMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonEndTime: If op_DevEnvMonEndTime is specified, this value will be compared to the value in DevEnvMonEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonEndTime must be specified if op_DevEnvMonEndTime is specified.
             :type val_c_DevEnvMonEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonHighShutdown: The operator to apply to the field DevEnvMonHighShutdown. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonHighShutdown: The high value of the shut down process in the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonHighShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonHighShutdown: If op_DevEnvMonHighShutdown is specified, the field named in this input will be compared to the value in DevEnvMonHighShutdown using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonHighShutdown must be specified if op_DevEnvMonHighShutdown is specified.
             :type val_f_DevEnvMonHighShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonHighShutdown: If op_DevEnvMonHighShutdown is specified, this value will be compared to the value in DevEnvMonHighShutdown using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonHighShutdown must be specified if op_DevEnvMonHighShutdown is specified.
             :type val_c_DevEnvMonHighShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonHighWarnVal: The operator to apply to the field DevEnvMonHighWarnVal. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonHighWarnVal: The high value of the warning message in the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonHighWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonHighWarnVal: If op_DevEnvMonHighWarnVal is specified, the field named in this input will be compared to the value in DevEnvMonHighWarnVal using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonHighWarnVal must be specified if op_DevEnvMonHighWarnVal is specified.
             :type val_f_DevEnvMonHighWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonHighWarnVal: If op_DevEnvMonHighWarnVal is specified, this value will be compared to the value in DevEnvMonHighWarnVal using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonHighWarnVal must be specified if op_DevEnvMonHighWarnVal is specified.
             :type val_c_DevEnvMonHighWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonID: The operator to apply to the field DevEnvMonID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonID: The internal NetMRI identifier of Device Environment. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonID: If op_DevEnvMonID is specified, the field named in this input will be compared to the value in DevEnvMonID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonID must be specified if op_DevEnvMonID is specified.
             :type val_f_DevEnvMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonID: If op_DevEnvMonID is specified, this value will be compared to the value in DevEnvMonID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonID must be specified if op_DevEnvMonID is specified.
             :type val_c_DevEnvMonID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonIndex: The operator to apply to the field DevEnvMonIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonIndex: The index of the device in the device environment. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonIndex: If op_DevEnvMonIndex is specified, the field named in this input will be compared to the value in DevEnvMonIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonIndex must be specified if op_DevEnvMonIndex is specified.
             :type val_f_DevEnvMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonIndex: If op_DevEnvMonIndex is specified, this value will be compared to the value in DevEnvMonIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonIndex must be specified if op_DevEnvMonIndex is specified.
             :type val_c_DevEnvMonIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonLowShutdown: The operator to apply to the field DevEnvMonLowShutdown. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonLowShutdown: The low value of the shut down process in the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonLowShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonLowShutdown: If op_DevEnvMonLowShutdown is specified, the field named in this input will be compared to the value in DevEnvMonLowShutdown using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonLowShutdown must be specified if op_DevEnvMonLowShutdown is specified.
             :type val_f_DevEnvMonLowShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonLowShutdown: If op_DevEnvMonLowShutdown is specified, this value will be compared to the value in DevEnvMonLowShutdown using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonLowShutdown must be specified if op_DevEnvMonLowShutdown is specified.
             :type val_c_DevEnvMonLowShutdown: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonLowWarnVal: The operator to apply to the field DevEnvMonLowWarnVal. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonLowWarnVal: The low value of the warning message in the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonLowWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonLowWarnVal: If op_DevEnvMonLowWarnVal is specified, the field named in this input will be compared to the value in DevEnvMonLowWarnVal using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonLowWarnVal must be specified if op_DevEnvMonLowWarnVal is specified.
             :type val_f_DevEnvMonLowWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonLowWarnVal: If op_DevEnvMonLowWarnVal is specified, this value will be compared to the value in DevEnvMonLowWarnVal using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonLowWarnVal must be specified if op_DevEnvMonLowWarnVal is specified.
             :type val_c_DevEnvMonLowWarnVal: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonMeasure: The operator to apply to the field DevEnvMonMeasure. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonMeasure: The measure of the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonMeasure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonMeasure: If op_DevEnvMonMeasure is specified, the field named in this input will be compared to the value in DevEnvMonMeasure using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonMeasure must be specified if op_DevEnvMonMeasure is specified.
             :type val_f_DevEnvMonMeasure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonMeasure: If op_DevEnvMonMeasure is specified, this value will be compared to the value in DevEnvMonMeasure using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonMeasure must be specified if op_DevEnvMonMeasure is specified.
             :type val_c_DevEnvMonMeasure: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonStartTime: The operator to apply to the field DevEnvMonStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonStartTime: If op_DevEnvMonStartTime is specified, the field named in this input will be compared to the value in DevEnvMonStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonStartTime must be specified if op_DevEnvMonStartTime is specified.
             :type val_f_DevEnvMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonStartTime: If op_DevEnvMonStartTime is specified, this value will be compared to the value in DevEnvMonStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonStartTime must be specified if op_DevEnvMonStartTime is specified.
             :type val_c_DevEnvMonStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonState: The operator to apply to the field DevEnvMonState. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonState: The current state of the device in the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonState: If op_DevEnvMonState is specified, the field named in this input will be compared to the value in DevEnvMonState using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonState must be specified if op_DevEnvMonState is specified.
             :type val_f_DevEnvMonState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonState: If op_DevEnvMonState is specified, this value will be compared to the value in DevEnvMonState using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonState must be specified if op_DevEnvMonState is specified.
             :type val_c_DevEnvMonState: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonStatus: The operator to apply to the field DevEnvMonStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonStatus: The status of the device in the Device Environment Monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonStatus: If op_DevEnvMonStatus is specified, the field named in this input will be compared to the value in DevEnvMonStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonStatus must be specified if op_DevEnvMonStatus is specified.
             :type val_f_DevEnvMonStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonStatus: If op_DevEnvMonStatus is specified, this value will be compared to the value in DevEnvMonStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonStatus must be specified if op_DevEnvMonStatus is specified.
             :type val_c_DevEnvMonStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonStatusAlert: The operator to apply to the field DevEnvMonStatusAlert. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonStatusAlert: The alert status of the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonStatusAlert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonStatusAlert: If op_DevEnvMonStatusAlert is specified, the field named in this input will be compared to the value in DevEnvMonStatusAlert using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonStatusAlert must be specified if op_DevEnvMonStatusAlert is specified.
             :type val_f_DevEnvMonStatusAlert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonStatusAlert: If op_DevEnvMonStatusAlert is specified, this value will be compared to the value in DevEnvMonStatusAlert using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonStatusAlert must be specified if op_DevEnvMonStatusAlert is specified.
             :type val_c_DevEnvMonStatusAlert: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonStatusMessage: The operator to apply to the field DevEnvMonStatusMessage. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonStatusMessage: The status message of the device environment monitor. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonStatusMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonStatusMessage: If op_DevEnvMonStatusMessage is specified, the field named in this input will be compared to the value in DevEnvMonStatusMessage using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonStatusMessage must be specified if op_DevEnvMonStatusMessage is specified.
             :type val_f_DevEnvMonStatusMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonStatusMessage: If op_DevEnvMonStatusMessage is specified, this value will be compared to the value in DevEnvMonStatusMessage using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonStatusMessage must be specified if op_DevEnvMonStatusMessage is specified.
             :type val_c_DevEnvMonStatusMessage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonTimestamp: The operator to apply to the field DevEnvMonTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonTimestamp: If op_DevEnvMonTimestamp is specified, the field named in this input will be compared to the value in DevEnvMonTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonTimestamp must be specified if op_DevEnvMonTimestamp is specified.
             :type val_f_DevEnvMonTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonTimestamp: If op_DevEnvMonTimestamp is specified, this value will be compared to the value in DevEnvMonTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonTimestamp must be specified if op_DevEnvMonTimestamp is specified.
             :type val_c_DevEnvMonTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DevEnvMonType: The operator to apply to the field DevEnvMonType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevEnvMonType: The NetMRI-determined monitor type of Device Environment. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevEnvMonType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevEnvMonType: If op_DevEnvMonType is specified, the field named in this input will be compared to the value in DevEnvMonType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevEnvMonType must be specified if op_DevEnvMonType is specified.
             :type val_f_DevEnvMonType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevEnvMonType: If op_DevEnvMonType is specified, this value will be compared to the value in DevEnvMonType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevEnvMonType must be specified if op_DevEnvMonType is specified.
             :type val_c_DevEnvMonType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which device environment information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timestamp: The data returned will represent the device environment monitors as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device environment monitor methods. The listed methods will be called on each device environment monitor returned and included in the output. Available methods are: device.
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
            |  ``default:`` DevEnvMonID

             :param sort: The data field(s) to use for sorting the output. Default is DevEnvMonID. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert.
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

             :param select: The list of attributes to return for each DeviceEnvironmentMonitor. Valid values are DevEnvMonID, DeviceID, DataSourceID, DevEnvMonStartTime, DevEnvMonEndTime, DevEnvMonTimestamp, DevEnvMonChangedCols, DevEnvMonIndex, DevEnvMonType, DevEnvMonDescr, DevEnvMonState, DevEnvMonStatus, DevEnvMonMeasure, DevEnvMonLowWarnVal, DevEnvMonLowShutdown, DevEnvMonHighWarnVal, DevEnvMonHighShutdown, DevEnvMonStatusMessage, DevEnvMonStatusAlert. If empty or omitted, all attributes will be returned.
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

             :return device_environment_monitors: An array of the DeviceEnvironmentMonitor objects that match the specified input criteria.
             :rtype device_environment_monitors: Array of DeviceEnvironmentMonitor

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

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

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

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

             :param DevEnvMonID: The internal NetMRI identifier of Device Environment.
             :type DevEnvMonID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
