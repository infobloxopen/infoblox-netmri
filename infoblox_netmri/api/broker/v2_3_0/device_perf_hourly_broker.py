from ..broker import Broker


class DevicePerfHourlyBroker(Broker):
    controller = "device_perf_hourlies"

    def index(self, **kwargs):
        """Lists the available device perf hourlies. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The starting date/time of the one hour interval.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The starting date/time of the one hour interval.
             :type StartTime: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the device perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device perf hourly methods. The listed methods will be called on each device perf hourly returned and included in the output. Available methods are: data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePerfHourlyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePerfHourlyID. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max.
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

             :param select: The list of attributes to return for each DevicePerfHourly. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max. If empty or omitted, all attributes will be returned.
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

             :return device_perf_hourlies: An array of the DevicePerfHourly objects that match the specified input criteria.
             :rtype device_perf_hourlies: Array of DevicePerfHourly

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device perf hourly.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device perf hourly methods. The listed methods will be called on each device perf hourly returned and included in the output. Available methods are: data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_perf_hourly: The device perf hourly identified by the specified DevicePerfHourlyID.
             :rtype device_perf_hourly: DevicePerfHourly

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device perf hourlies matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyAvg: The mean CPU busy reading during the hour.
             :type CpuBusyAvg: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyAvg: The mean CPU busy reading during the hour.
             :type CpuBusyAvg: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyMax: The maximum CPU busy reading during the hour.
             :type CpuBusyMax: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyMax: The maximum CPU busy reading during the hour.
             :type CpuBusyMax: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyMin: The minimum CPU busy reading during the hour.
             :type CpuBusyMin: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param CpuBusyMin: The minimum CPU busy reading during the hour.
             :type CpuBusyMin: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this data was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemAvg: The mean free memory reading during the hour.
             :type FreeMemAvg: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemAvg: The mean free memory reading during the hour.
             :type FreeMemAvg: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemMax: The maximum free memory reading during the hour.
             :type FreeMemMax: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemMax: The maximum free memory reading during the hour.
             :type FreeMemMax: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemMin: The minimum free memory reading during the hour.
             :type FreeMemMin: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FreeMemMin: The minimum free memory reading during the hour.
             :type FreeMemMin: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Avg: The mean five-minute memory utilization reading during the hour.
             :type MemUtil5Avg: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Avg: The mean five-minute memory utilization reading during the hour.
             :type MemUtil5Avg: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Max: The maximum five-minute memory utilization reading during the hour.
             :type MemUtil5Max: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Max: The maximum five-minute memory utilization reading during the hour.
             :type MemUtil5Max: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Min: The minimum five-minute memory utilization reading during the hour.
             :type MemUtil5Min: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param MemUtil5Min: The minimum five-minute memory utilization reading during the hour.
             :type MemUtil5Min: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The starting date/time of the one hour interval.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The starting date/time of the one hour interval.
             :type StartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemAvg: The average used memory reading during the hour.
             :type UsedMemAvg: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemAvg: The average used memory reading during the hour.
             :type UsedMemAvg: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemMax: The maximum used memory reading during the hour.
             :type UsedMemMax: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemMax: The maximum used memory reading during the hour.
             :type UsedMemMax: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemMin: The minimum used memory reading during the hour.
             :type UsedMemMin: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UsedMemMin: The minimum used memory reading during the hour.
             :type UsedMemMin: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the device perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device perf hourly methods. The listed methods will be called on each device perf hourly returned and included in the output. Available methods are: data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePerfHourlyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePerfHourlyID. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max.
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

             :param select: The list of attributes to return for each DevicePerfHourly. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device perf hourlies, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: CpuBusyAvg, CpuBusyMax, CpuBusyMin, DataSourceID, DeviceID, DevicePerfHourlyID, FreeMemAvg, FreeMemMax, FreeMemMin, MemUtil5Avg, MemUtil5Max, MemUtil5Min, StartTime, UsedMemAvg, UsedMemMax, UsedMemMin.
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

             :return device_perf_hourlies: An array of the DevicePerfHourly objects that match the specified input criteria.
             :rtype device_perf_hourlies: Array of DevicePerfHourly

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device perf hourlies matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: CpuBusyAvg, CpuBusyMax, CpuBusyMin, DataSourceID, DeviceID, DevicePerfHourlyID, FreeMemAvg, FreeMemMax, FreeMemMin, MemUtil5Avg, MemUtil5Max, MemUtil5Min, StartTime, UsedMemAvg, UsedMemMax, UsedMemMin.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CpuBusyAvg: The operator to apply to the field CpuBusyAvg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CpuBusyAvg: The mean CPU busy reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CpuBusyAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CpuBusyAvg: If op_CpuBusyAvg is specified, the field named in this input will be compared to the value in CpuBusyAvg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CpuBusyAvg must be specified if op_CpuBusyAvg is specified.
             :type val_f_CpuBusyAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CpuBusyAvg: If op_CpuBusyAvg is specified, this value will be compared to the value in CpuBusyAvg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CpuBusyAvg must be specified if op_CpuBusyAvg is specified.
             :type val_c_CpuBusyAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CpuBusyMax: The operator to apply to the field CpuBusyMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CpuBusyMax: The maximum CPU busy reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CpuBusyMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CpuBusyMax: If op_CpuBusyMax is specified, the field named in this input will be compared to the value in CpuBusyMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CpuBusyMax must be specified if op_CpuBusyMax is specified.
             :type val_f_CpuBusyMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CpuBusyMax: If op_CpuBusyMax is specified, this value will be compared to the value in CpuBusyMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CpuBusyMax must be specified if op_CpuBusyMax is specified.
             :type val_c_CpuBusyMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_CpuBusyMin: The operator to apply to the field CpuBusyMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. CpuBusyMin: The minimum CPU busy reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_CpuBusyMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_CpuBusyMin: If op_CpuBusyMin is specified, the field named in this input will be compared to the value in CpuBusyMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_CpuBusyMin must be specified if op_CpuBusyMin is specified.
             :type val_f_CpuBusyMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_CpuBusyMin: If op_CpuBusyMin is specified, this value will be compared to the value in CpuBusyMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_CpuBusyMin must be specified if op_CpuBusyMin is specified.
             :type val_c_CpuBusyMin: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this data was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DevicePerfHourlyID: The operator to apply to the field DevicePerfHourlyID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DevicePerfHourlyID: The internal NetMRI identifier for this performance record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DevicePerfHourlyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DevicePerfHourlyID: If op_DevicePerfHourlyID is specified, the field named in this input will be compared to the value in DevicePerfHourlyID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DevicePerfHourlyID must be specified if op_DevicePerfHourlyID is specified.
             :type val_f_DevicePerfHourlyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DevicePerfHourlyID: If op_DevicePerfHourlyID is specified, this value will be compared to the value in DevicePerfHourlyID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DevicePerfHourlyID must be specified if op_DevicePerfHourlyID is specified.
             :type val_c_DevicePerfHourlyID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FreeMemAvg: The operator to apply to the field FreeMemAvg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FreeMemAvg: The mean free memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FreeMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FreeMemAvg: If op_FreeMemAvg is specified, the field named in this input will be compared to the value in FreeMemAvg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FreeMemAvg must be specified if op_FreeMemAvg is specified.
             :type val_f_FreeMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FreeMemAvg: If op_FreeMemAvg is specified, this value will be compared to the value in FreeMemAvg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FreeMemAvg must be specified if op_FreeMemAvg is specified.
             :type val_c_FreeMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FreeMemMax: The operator to apply to the field FreeMemMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FreeMemMax: The maximum free memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FreeMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FreeMemMax: If op_FreeMemMax is specified, the field named in this input will be compared to the value in FreeMemMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FreeMemMax must be specified if op_FreeMemMax is specified.
             :type val_f_FreeMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FreeMemMax: If op_FreeMemMax is specified, this value will be compared to the value in FreeMemMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FreeMemMax must be specified if op_FreeMemMax is specified.
             :type val_c_FreeMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FreeMemMin: The operator to apply to the field FreeMemMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FreeMemMin: The minimum free memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FreeMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FreeMemMin: If op_FreeMemMin is specified, the field named in this input will be compared to the value in FreeMemMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FreeMemMin must be specified if op_FreeMemMin is specified.
             :type val_f_FreeMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FreeMemMin: If op_FreeMemMin is specified, this value will be compared to the value in FreeMemMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FreeMemMin must be specified if op_FreeMemMin is specified.
             :type val_c_FreeMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemUtil5Avg: The operator to apply to the field MemUtil5Avg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemUtil5Avg: The mean five-minute memory utilization reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemUtil5Avg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemUtil5Avg: If op_MemUtil5Avg is specified, the field named in this input will be compared to the value in MemUtil5Avg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemUtil5Avg must be specified if op_MemUtil5Avg is specified.
             :type val_f_MemUtil5Avg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemUtil5Avg: If op_MemUtil5Avg is specified, this value will be compared to the value in MemUtil5Avg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemUtil5Avg must be specified if op_MemUtil5Avg is specified.
             :type val_c_MemUtil5Avg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemUtil5Max: The operator to apply to the field MemUtil5Max. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemUtil5Max: The maximum five-minute memory utilization reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemUtil5Max: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemUtil5Max: If op_MemUtil5Max is specified, the field named in this input will be compared to the value in MemUtil5Max using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemUtil5Max must be specified if op_MemUtil5Max is specified.
             :type val_f_MemUtil5Max: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemUtil5Max: If op_MemUtil5Max is specified, this value will be compared to the value in MemUtil5Max using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemUtil5Max must be specified if op_MemUtil5Max is specified.
             :type val_c_MemUtil5Max: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_MemUtil5Min: The operator to apply to the field MemUtil5Min. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. MemUtil5Min: The minimum five-minute memory utilization reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_MemUtil5Min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_MemUtil5Min: If op_MemUtil5Min is specified, the field named in this input will be compared to the value in MemUtil5Min using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_MemUtil5Min must be specified if op_MemUtil5Min is specified.
             :type val_f_MemUtil5Min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_MemUtil5Min: If op_MemUtil5Min is specified, this value will be compared to the value in MemUtil5Min using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_MemUtil5Min must be specified if op_MemUtil5Min is specified.
             :type val_c_MemUtil5Min: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The starting date/time of the one hour interval. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UsedMemAvg: The operator to apply to the field UsedMemAvg. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UsedMemAvg: The average used memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UsedMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UsedMemAvg: If op_UsedMemAvg is specified, the field named in this input will be compared to the value in UsedMemAvg using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UsedMemAvg must be specified if op_UsedMemAvg is specified.
             :type val_f_UsedMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UsedMemAvg: If op_UsedMemAvg is specified, this value will be compared to the value in UsedMemAvg using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UsedMemAvg must be specified if op_UsedMemAvg is specified.
             :type val_c_UsedMemAvg: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UsedMemMax: The operator to apply to the field UsedMemMax. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UsedMemMax: The maximum used memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UsedMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UsedMemMax: If op_UsedMemMax is specified, the field named in this input will be compared to the value in UsedMemMax using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UsedMemMax must be specified if op_UsedMemMax is specified.
             :type val_f_UsedMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UsedMemMax: If op_UsedMemMax is specified, this value will be compared to the value in UsedMemMax using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UsedMemMax must be specified if op_UsedMemMax is specified.
             :type val_c_UsedMemMax: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UsedMemMin: The operator to apply to the field UsedMemMin. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UsedMemMin: The minimum used memory reading during the hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UsedMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UsedMemMin: If op_UsedMemMin is specified, the field named in this input will be compared to the value in UsedMemMin using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UsedMemMin must be specified if op_UsedMemMin is specified.
             :type val_f_UsedMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UsedMemMin: If op_UsedMemMin is specified, this value will be compared to the value in UsedMemMin using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UsedMemMin must be specified if op_UsedMemMin is specified.
             :type val_c_UsedMemMin: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the device perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device perf hourly methods. The listed methods will be called on each device perf hourly returned and included in the output. Available methods are: data_source, device, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device.
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
            |  ``default:`` DevicePerfHourlyID

             :param sort: The data field(s) to use for sorting the output. Default is DevicePerfHourlyID. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max.
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

             :param select: The list of attributes to return for each DevicePerfHourly. Valid values are DevicePerfHourlyID, DataSourceID, DeviceID, StartTime, CpuBusyMin, CpuBusyAvg, CpuBusyMax, UsedMemMin, UsedMemAvg, UsedMemMax, FreeMemMin, FreeMemAvg, FreeMemMax, MemUtil5Min, MemUtil5Avg, MemUtil5Max. If empty or omitted, all attributes will be returned.
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

             :return device_perf_hourlies: An array of the DevicePerfHourly objects that match the specified input criteria.
             :rtype device_perf_hourlies: Array of DevicePerfHourly

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePerfHourlyID: The internal NetMRI identifier for this performance record.
             :type DevicePerfHourlyID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device from which this data was collected.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
