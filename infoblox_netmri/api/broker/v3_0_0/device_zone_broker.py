from ..broker import Broker


class DeviceZoneBroker(Broker):
    controller = "device_zones"

    def show(self, **kwargs):
        """Shows the details for the specified device zone.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device zone methods. The listed methods will be called on each device zone returned and included in the output. Available methods are: zone_interface, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: zone_interface, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_zone: The device zone identified by the specified DeviceZoneID.
             :rtype device_zone: DeviceZone

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device zones. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this zone belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Array of Integer

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

             :param timestamp: The data returned will represent the device zones as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device zone methods. The listed methods will be called on each device zone returned and included in the output. Available methods are: zone_interface, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: zone_interface, data_source, device.
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
            |  ``default:`` DeviceZoneID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceZoneID. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd.
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

             :param select: The list of attributes to return for each DeviceZone. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd. If empty or omitted, all attributes will be returned.
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

             :return device_zones: An array of the DeviceZone objects that match the specified input criteria.
             :rtype device_zones: Array of DeviceZone

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device zones matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this zone belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneArtificialInd: A flag indicating that this zone has no counterpart in the device configuration.
             :type ZoneArtificialInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ZoneChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneEndTime: The ending effective time of this record, or empty if still in effect.
             :type ZoneEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneFirstSeenTime: The timestamp of when NetMRI first discovered this service.
             :type ZoneFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneInterfaceCount: The total number of interfaces connected to this zone.
             :type ZoneInterfaceCount: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneInterfaceID: The internal NetMRI identifier of that interface, if only one interface connected to this zone.
             :type ZoneInterfaceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneName: The name of the zone.
             :type ZoneName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneProvisionData: Internal data - do not modify, may change without warning.
             :type ZoneProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneStartTime: The starting effective time of this record.
             :type ZoneStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ZoneTimestamp: The date and time this record was collected or calculated.
             :type ZoneTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the device zones as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device zone methods. The listed methods will be called on each device zone returned and included in the output. Available methods are: zone_interface, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: zone_interface, data_source, device.
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
            |  ``default:`` DeviceZoneID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceZoneID. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd.
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

             :param select: The list of attributes to return for each DeviceZone. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device zones, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, DeviceZoneID, ZoneArtificialInd, ZoneChangedCols, ZoneEndTime, ZoneFirstSeenTime, ZoneInterfaceCount, ZoneInterfaceID, ZoneName, ZoneProvisionData, ZoneStartTime, ZoneTimestamp.
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

             :return device_zones: An array of the DeviceZone objects that match the specified input criteria.
             :rtype device_zones: Array of DeviceZone

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device zones matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, DeviceZoneID, ZoneArtificialInd, ZoneChangedCols, ZoneEndTime, ZoneFirstSeenTime, ZoneInterfaceCount, ZoneInterfaceID, ZoneName, ZoneProvisionData, ZoneStartTime, ZoneTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which this zone belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceZoneID: The operator to apply to the field DeviceZoneID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceZoneID: The internal NetMRI identifier for this filtering zone. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceZoneID: If op_DeviceZoneID is specified, the field named in this input will be compared to the value in DeviceZoneID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceZoneID must be specified if op_DeviceZoneID is specified.
             :type val_f_DeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceZoneID: If op_DeviceZoneID is specified, this value will be compared to the value in DeviceZoneID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceZoneID must be specified if op_DeviceZoneID is specified.
             :type val_c_DeviceZoneID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneArtificialInd: The operator to apply to the field ZoneArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneArtificialInd: A flag indicating that this zone has no counterpart in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneArtificialInd: If op_ZoneArtificialInd is specified, the field named in this input will be compared to the value in ZoneArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneArtificialInd must be specified if op_ZoneArtificialInd is specified.
             :type val_f_ZoneArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneArtificialInd: If op_ZoneArtificialInd is specified, this value will be compared to the value in ZoneArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneArtificialInd must be specified if op_ZoneArtificialInd is specified.
             :type val_c_ZoneArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneChangedCols: The operator to apply to the field ZoneChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneChangedCols: If op_ZoneChangedCols is specified, the field named in this input will be compared to the value in ZoneChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneChangedCols must be specified if op_ZoneChangedCols is specified.
             :type val_f_ZoneChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneChangedCols: If op_ZoneChangedCols is specified, this value will be compared to the value in ZoneChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneChangedCols must be specified if op_ZoneChangedCols is specified.
             :type val_c_ZoneChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneEndTime: The operator to apply to the field ZoneEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneEndTime: If op_ZoneEndTime is specified, the field named in this input will be compared to the value in ZoneEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneEndTime must be specified if op_ZoneEndTime is specified.
             :type val_f_ZoneEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneEndTime: If op_ZoneEndTime is specified, this value will be compared to the value in ZoneEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneEndTime must be specified if op_ZoneEndTime is specified.
             :type val_c_ZoneEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneFirstSeenTime: The operator to apply to the field ZoneFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneFirstSeenTime: The timestamp of when NetMRI first discovered this service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneFirstSeenTime: If op_ZoneFirstSeenTime is specified, the field named in this input will be compared to the value in ZoneFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneFirstSeenTime must be specified if op_ZoneFirstSeenTime is specified.
             :type val_f_ZoneFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneFirstSeenTime: If op_ZoneFirstSeenTime is specified, this value will be compared to the value in ZoneFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneFirstSeenTime must be specified if op_ZoneFirstSeenTime is specified.
             :type val_c_ZoneFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneInterfaceCount: The operator to apply to the field ZoneInterfaceCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneInterfaceCount: The total number of interfaces connected to this zone. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneInterfaceCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneInterfaceCount: If op_ZoneInterfaceCount is specified, the field named in this input will be compared to the value in ZoneInterfaceCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneInterfaceCount must be specified if op_ZoneInterfaceCount is specified.
             :type val_f_ZoneInterfaceCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneInterfaceCount: If op_ZoneInterfaceCount is specified, this value will be compared to the value in ZoneInterfaceCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneInterfaceCount must be specified if op_ZoneInterfaceCount is specified.
             :type val_c_ZoneInterfaceCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneInterfaceID: The operator to apply to the field ZoneInterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneInterfaceID: The internal NetMRI identifier of that interface, if only one interface connected to this zone. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneInterfaceID: If op_ZoneInterfaceID is specified, the field named in this input will be compared to the value in ZoneInterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneInterfaceID must be specified if op_ZoneInterfaceID is specified.
             :type val_f_ZoneInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneInterfaceID: If op_ZoneInterfaceID is specified, this value will be compared to the value in ZoneInterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneInterfaceID must be specified if op_ZoneInterfaceID is specified.
             :type val_c_ZoneInterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneName: The operator to apply to the field ZoneName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneName: The name of the zone. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneName: If op_ZoneName is specified, the field named in this input will be compared to the value in ZoneName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneName must be specified if op_ZoneName is specified.
             :type val_f_ZoneName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneName: If op_ZoneName is specified, this value will be compared to the value in ZoneName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneName must be specified if op_ZoneName is specified.
             :type val_c_ZoneName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneProvisionData: The operator to apply to the field ZoneProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneProvisionData: If op_ZoneProvisionData is specified, the field named in this input will be compared to the value in ZoneProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneProvisionData must be specified if op_ZoneProvisionData is specified.
             :type val_f_ZoneProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneProvisionData: If op_ZoneProvisionData is specified, this value will be compared to the value in ZoneProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneProvisionData must be specified if op_ZoneProvisionData is specified.
             :type val_c_ZoneProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneStartTime: The operator to apply to the field ZoneStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneStartTime: If op_ZoneStartTime is specified, the field named in this input will be compared to the value in ZoneStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneStartTime must be specified if op_ZoneStartTime is specified.
             :type val_f_ZoneStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneStartTime: If op_ZoneStartTime is specified, this value will be compared to the value in ZoneStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneStartTime must be specified if op_ZoneStartTime is specified.
             :type val_c_ZoneStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ZoneTimestamp: The operator to apply to the field ZoneTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ZoneTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ZoneTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ZoneTimestamp: If op_ZoneTimestamp is specified, the field named in this input will be compared to the value in ZoneTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ZoneTimestamp must be specified if op_ZoneTimestamp is specified.
             :type val_f_ZoneTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ZoneTimestamp: If op_ZoneTimestamp is specified, this value will be compared to the value in ZoneTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ZoneTimestamp must be specified if op_ZoneTimestamp is specified.
             :type val_c_ZoneTimestamp: String

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

             :param timestamp: The data returned will represent the device zones as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device zone methods. The listed methods will be called on each device zone returned and included in the output. Available methods are: zone_interface, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: zone_interface, data_source, device.
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
            |  ``default:`` DeviceZoneID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceZoneID. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd.
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

             :param select: The list of attributes to return for each DeviceZone. Valid values are DeviceZoneID, DeviceID, DataSourceID, ZoneFirstSeenTime, ZoneStartTime, ZoneEndTime, ZoneTimestamp, ZoneChangedCols, ZoneName, ZoneProvisionData, ZoneInterfaceCount, ZoneInterfaceID, ZoneArtificialInd. If empty or omitted, all attributes will be returned.
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

             :return device_zones: An array of the DeviceZone objects that match the specified input criteria.
             :rtype device_zones: Array of DeviceZone

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def zone_interface(self, **kwargs):
        """The Interface linked to this zone (if only one interface linked to this zone)

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Interface linked to this zone (if only one interface linked to this zone)
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("zone_interface"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceZoneID: The internal NetMRI identifier for this filtering zone.
             :type DeviceZoneID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
