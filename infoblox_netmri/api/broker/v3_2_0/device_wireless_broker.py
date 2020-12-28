from ..broker import Broker


class DeviceWirelessBroker(Broker):
    controller = "device_wirelesses"

    def index(self, **kwargs):
        """Lists the available device wirelesses. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which wireless setting was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which wireless setting was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of a local interface for the device wireless.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of a local interface for the device wireless.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StationID: The internal NetMRI identifier of a station.
             :type StationID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StationID: The internal NetMRI identifier of a station.
             :type StationID: Array of String

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

             :param timestamp: The data returned will represent the device wirelesses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device wireless methods. The listed methods will be called on each device wireless returned and included in the output. Available methods are: device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface.
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
            |  ``default:`` DeviceWirelessID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceWirelessID. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4.
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

             :param select: The list of attributes to return for each DeviceWireless. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4. If empty or omitted, all attributes will be returned.
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

             :return device_wirelesses: An array of the DeviceWireless objects that match the specified input criteria.
             :rtype device_wirelesses: Array of DeviceWireless

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device wireless.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device wireless methods. The listed methods will be called on each device wireless returned and included in the output. Available methods are: device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_wireless: The device wireless identified by the specified DeviceWirelessID.
             :rtype device_wireless: DeviceWireless

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device wirelesses matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DesiredSSID: The service set identifier(SSID) of desired wireless device.
             :type DesiredSSID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DesiredSSID: The service set identifier(SSID) of desired wireless device.
             :type DesiredSSID: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which wireless setting was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which wireless setting was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceWirelessChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type DeviceWirelessChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceWirelessEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessEndTime: The ending effective time of this record, or empty if still in effect.
             :type DeviceWirelessEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessStartTime: The starting effective time of this record.
             :type DeviceWirelessStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessStartTime: The starting effective time of this record.
             :type DeviceWirelessStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessTimestamp: The date and time this record was collected or calculated.
             :type DeviceWirelessTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceWirelessTimestamp: The date and time this record was collected or calculated.
             :type DeviceWirelessTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of a local interface for the device wireless.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of a local interface for the device wireless.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StationID: The internal NetMRI identifier of a station.
             :type StationID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StationID: The internal NetMRI identifier of a station.
             :type StationID: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StationRole: The role name of the station.
             :type StationRole: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StationRole: The role name of the station.
             :type StationRole: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPAllowedInd: A flag indicates whether a wired equivalent privacy is allowed or not?
             :type WEPAllowedInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPAllowedInd: A flag indicates whether a wired equivalent privacy is allowed or not?
             :type WEPAllowedInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen1: The initial default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen1: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen1: The initial default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen1: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen2: The second default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen2: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen2: The second default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen2: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen3: The third default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen3: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen3: The third default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen3: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen4: The fourth default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen4: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPDefaultKeyLen4: The fourth default key length of wired equivalent privacy.
             :type WEPDefaultKeyLen4: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPEnabledInd: A flag indicates whether a wired equivalent privacy is enabled or not?
             :type WEPEnabledInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPEnabledInd: A flag indicates whether a wired equivalent privacy is enabled or not?
             :type WEPEnabledInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPICVErrorCount: The total number of integrity check errors in WEP.
             :type WEPICVErrorCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPICVErrorCount: The total number of integrity check errors in WEP.
             :type WEPICVErrorCount: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WEPOnlyTrafficInd: A flag indicates whether a wired equivalent privacy is traffic or not?
             :type WEPOnlyTrafficInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WEPOnlyTrafficInd: A flag indicates whether a wired equivalent privacy is traffic or not?
             :type WEPOnlyTrafficInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index of a local interface for the device wireless table entry.
             :type ifIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The SNMP index of a local interface for the device wireless table entry.
             :type ifIndex: Array of String

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

             :param timestamp: The data returned will represent the device wirelesses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device wireless methods. The listed methods will be called on each device wireless returned and included in the output. Available methods are: device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface.
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
            |  ``default:`` DeviceWirelessID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceWirelessID. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4.
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

             :param select: The list of attributes to return for each DeviceWireless. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device wirelesses, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DesiredSSID, DeviceID, DeviceWirelessChangedCols, DeviceWirelessEndTime, DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessTimestamp, InterfaceID, StationID, StationRole, WEPAllowedInd, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4, WEPEnabledInd, WEPICVErrorCount, WEPOnlyTrafficInd, ifIndex.
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

             :return device_wirelesses: An array of the DeviceWireless objects that match the specified input criteria.
             :rtype device_wirelesses: Array of DeviceWireless

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device wirelesses matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DesiredSSID, DeviceID, DeviceWirelessChangedCols, DeviceWirelessEndTime, DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessTimestamp, InterfaceID, StationID, StationRole, WEPAllowedInd, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4, WEPEnabledInd, WEPICVErrorCount, WEPOnlyTrafficInd, ifIndex.

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

             :param op_DesiredSSID: The operator to apply to the field DesiredSSID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DesiredSSID: The service set identifier(SSID) of desired wireless device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DesiredSSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DesiredSSID: If op_DesiredSSID is specified, the field named in this input will be compared to the value in DesiredSSID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DesiredSSID must be specified if op_DesiredSSID is specified.
             :type val_f_DesiredSSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DesiredSSID: If op_DesiredSSID is specified, this value will be compared to the value in DesiredSSID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DesiredSSID must be specified if op_DesiredSSID is specified.
             :type val_c_DesiredSSID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which wireless setting was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceWirelessChangedCols: The operator to apply to the field DeviceWirelessChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceWirelessChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceWirelessChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceWirelessChangedCols: If op_DeviceWirelessChangedCols is specified, the field named in this input will be compared to the value in DeviceWirelessChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceWirelessChangedCols must be specified if op_DeviceWirelessChangedCols is specified.
             :type val_f_DeviceWirelessChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceWirelessChangedCols: If op_DeviceWirelessChangedCols is specified, this value will be compared to the value in DeviceWirelessChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceWirelessChangedCols must be specified if op_DeviceWirelessChangedCols is specified.
             :type val_c_DeviceWirelessChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceWirelessEndTime: The operator to apply to the field DeviceWirelessEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceWirelessEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceWirelessEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceWirelessEndTime: If op_DeviceWirelessEndTime is specified, the field named in this input will be compared to the value in DeviceWirelessEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceWirelessEndTime must be specified if op_DeviceWirelessEndTime is specified.
             :type val_f_DeviceWirelessEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceWirelessEndTime: If op_DeviceWirelessEndTime is specified, this value will be compared to the value in DeviceWirelessEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceWirelessEndTime must be specified if op_DeviceWirelessEndTime is specified.
             :type val_c_DeviceWirelessEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceWirelessID: The operator to apply to the field DeviceWirelessID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceWirelessID: The internal NetMRI identifier of the device wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceWirelessID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceWirelessID: If op_DeviceWirelessID is specified, the field named in this input will be compared to the value in DeviceWirelessID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceWirelessID must be specified if op_DeviceWirelessID is specified.
             :type val_f_DeviceWirelessID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceWirelessID: If op_DeviceWirelessID is specified, this value will be compared to the value in DeviceWirelessID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceWirelessID must be specified if op_DeviceWirelessID is specified.
             :type val_c_DeviceWirelessID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceWirelessStartTime: The operator to apply to the field DeviceWirelessStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceWirelessStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceWirelessStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceWirelessStartTime: If op_DeviceWirelessStartTime is specified, the field named in this input will be compared to the value in DeviceWirelessStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceWirelessStartTime must be specified if op_DeviceWirelessStartTime is specified.
             :type val_f_DeviceWirelessStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceWirelessStartTime: If op_DeviceWirelessStartTime is specified, this value will be compared to the value in DeviceWirelessStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceWirelessStartTime must be specified if op_DeviceWirelessStartTime is specified.
             :type val_c_DeviceWirelessStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceWirelessTimestamp: The operator to apply to the field DeviceWirelessTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceWirelessTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceWirelessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceWirelessTimestamp: If op_DeviceWirelessTimestamp is specified, the field named in this input will be compared to the value in DeviceWirelessTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceWirelessTimestamp must be specified if op_DeviceWirelessTimestamp is specified.
             :type val_f_DeviceWirelessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceWirelessTimestamp: If op_DeviceWirelessTimestamp is specified, this value will be compared to the value in DeviceWirelessTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceWirelessTimestamp must be specified if op_DeviceWirelessTimestamp is specified.
             :type val_c_DeviceWirelessTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of a local interface for the device wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StationID: The operator to apply to the field StationID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StationID: The internal NetMRI identifier of a station. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StationID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StationID: If op_StationID is specified, the field named in this input will be compared to the value in StationID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StationID must be specified if op_StationID is specified.
             :type val_f_StationID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StationID: If op_StationID is specified, this value will be compared to the value in StationID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StationID must be specified if op_StationID is specified.
             :type val_c_StationID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StationRole: The operator to apply to the field StationRole. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StationRole: The role name of the station. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StationRole: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StationRole: If op_StationRole is specified, the field named in this input will be compared to the value in StationRole using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StationRole must be specified if op_StationRole is specified.
             :type val_f_StationRole: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StationRole: If op_StationRole is specified, this value will be compared to the value in StationRole using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StationRole must be specified if op_StationRole is specified.
             :type val_c_StationRole: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPAllowedInd: The operator to apply to the field WEPAllowedInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPAllowedInd: A flag indicates whether a wired equivalent privacy is allowed or not? For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPAllowedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPAllowedInd: If op_WEPAllowedInd is specified, the field named in this input will be compared to the value in WEPAllowedInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPAllowedInd must be specified if op_WEPAllowedInd is specified.
             :type val_f_WEPAllowedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPAllowedInd: If op_WEPAllowedInd is specified, this value will be compared to the value in WEPAllowedInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPAllowedInd must be specified if op_WEPAllowedInd is specified.
             :type val_c_WEPAllowedInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPDefaultKeyLen1: The operator to apply to the field WEPDefaultKeyLen1. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPDefaultKeyLen1: The initial default key length of wired equivalent privacy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPDefaultKeyLen1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPDefaultKeyLen1: If op_WEPDefaultKeyLen1 is specified, the field named in this input will be compared to the value in WEPDefaultKeyLen1 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPDefaultKeyLen1 must be specified if op_WEPDefaultKeyLen1 is specified.
             :type val_f_WEPDefaultKeyLen1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPDefaultKeyLen1: If op_WEPDefaultKeyLen1 is specified, this value will be compared to the value in WEPDefaultKeyLen1 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPDefaultKeyLen1 must be specified if op_WEPDefaultKeyLen1 is specified.
             :type val_c_WEPDefaultKeyLen1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPDefaultKeyLen2: The operator to apply to the field WEPDefaultKeyLen2. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPDefaultKeyLen2: The second default key length of wired equivalent privacy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPDefaultKeyLen2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPDefaultKeyLen2: If op_WEPDefaultKeyLen2 is specified, the field named in this input will be compared to the value in WEPDefaultKeyLen2 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPDefaultKeyLen2 must be specified if op_WEPDefaultKeyLen2 is specified.
             :type val_f_WEPDefaultKeyLen2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPDefaultKeyLen2: If op_WEPDefaultKeyLen2 is specified, this value will be compared to the value in WEPDefaultKeyLen2 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPDefaultKeyLen2 must be specified if op_WEPDefaultKeyLen2 is specified.
             :type val_c_WEPDefaultKeyLen2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPDefaultKeyLen3: The operator to apply to the field WEPDefaultKeyLen3. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPDefaultKeyLen3: The third default key length of wired equivalent privacy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPDefaultKeyLen3: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPDefaultKeyLen3: If op_WEPDefaultKeyLen3 is specified, the field named in this input will be compared to the value in WEPDefaultKeyLen3 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPDefaultKeyLen3 must be specified if op_WEPDefaultKeyLen3 is specified.
             :type val_f_WEPDefaultKeyLen3: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPDefaultKeyLen3: If op_WEPDefaultKeyLen3 is specified, this value will be compared to the value in WEPDefaultKeyLen3 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPDefaultKeyLen3 must be specified if op_WEPDefaultKeyLen3 is specified.
             :type val_c_WEPDefaultKeyLen3: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPDefaultKeyLen4: The operator to apply to the field WEPDefaultKeyLen4. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPDefaultKeyLen4: The fourth default key length of wired equivalent privacy. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPDefaultKeyLen4: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPDefaultKeyLen4: If op_WEPDefaultKeyLen4 is specified, the field named in this input will be compared to the value in WEPDefaultKeyLen4 using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPDefaultKeyLen4 must be specified if op_WEPDefaultKeyLen4 is specified.
             :type val_f_WEPDefaultKeyLen4: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPDefaultKeyLen4: If op_WEPDefaultKeyLen4 is specified, this value will be compared to the value in WEPDefaultKeyLen4 using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPDefaultKeyLen4 must be specified if op_WEPDefaultKeyLen4 is specified.
             :type val_c_WEPDefaultKeyLen4: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPEnabledInd: The operator to apply to the field WEPEnabledInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPEnabledInd: A flag indicates whether a wired equivalent privacy is enabled or not? For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPEnabledInd: If op_WEPEnabledInd is specified, the field named in this input will be compared to the value in WEPEnabledInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPEnabledInd must be specified if op_WEPEnabledInd is specified.
             :type val_f_WEPEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPEnabledInd: If op_WEPEnabledInd is specified, this value will be compared to the value in WEPEnabledInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPEnabledInd must be specified if op_WEPEnabledInd is specified.
             :type val_c_WEPEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPICVErrorCount: The operator to apply to the field WEPICVErrorCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPICVErrorCount: The total number of integrity check errors in WEP. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPICVErrorCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPICVErrorCount: If op_WEPICVErrorCount is specified, the field named in this input will be compared to the value in WEPICVErrorCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPICVErrorCount must be specified if op_WEPICVErrorCount is specified.
             :type val_f_WEPICVErrorCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPICVErrorCount: If op_WEPICVErrorCount is specified, this value will be compared to the value in WEPICVErrorCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPICVErrorCount must be specified if op_WEPICVErrorCount is specified.
             :type val_c_WEPICVErrorCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_WEPOnlyTrafficInd: The operator to apply to the field WEPOnlyTrafficInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WEPOnlyTrafficInd: A flag indicates whether a wired equivalent privacy is traffic or not? For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WEPOnlyTrafficInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WEPOnlyTrafficInd: If op_WEPOnlyTrafficInd is specified, the field named in this input will be compared to the value in WEPOnlyTrafficInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WEPOnlyTrafficInd must be specified if op_WEPOnlyTrafficInd is specified.
             :type val_f_WEPOnlyTrafficInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WEPOnlyTrafficInd: If op_WEPOnlyTrafficInd is specified, this value will be compared to the value in WEPOnlyTrafficInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WEPOnlyTrafficInd must be specified if op_WEPOnlyTrafficInd is specified.
             :type val_c_WEPOnlyTrafficInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The SNMP index of a local interface for the device wireless table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

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

             :param timestamp: The data returned will represent the device wirelesses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device wireless methods. The listed methods will be called on each device wireless returned and included in the output. Available methods are: device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface.
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
            |  ``default:`` DeviceWirelessID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceWirelessID. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4.
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

             :param select: The list of attributes to return for each DeviceWireless. Valid values are DeviceWirelessID, DeviceWirelessStartTime, DeviceWirelessEndTime, DeviceWirelessChangedCols, DeviceWirelessTimestamp, DataSourceID, DeviceID, ifIndex, InterfaceID, StationID, DesiredSSID, StationRole, WEPEnabledInd, WEPAllowedInd, WEPOnlyTrafficInd, WEPICVErrorCount, WEPDefaultKeyLen1, WEPDefaultKeyLen2, WEPDefaultKeyLen3, WEPDefaultKeyLen4. If empty or omitted, all attributes will be returned.
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

             :return device_wirelesses: An array of the DeviceWireless objects that match the specified input criteria.
             :rtype device_wirelesses: Array of DeviceWireless

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

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

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def interface(self, **kwargs):
        """interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : interface
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceWirelessID: The internal NetMRI identifier of the device wireless.
             :type DeviceWirelessID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
