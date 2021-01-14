from ..broker import Broker


class DeviceServiceBroker(Broker):
    controller = "device_services"

    def show(self, **kwargs):
        """Shows the details for the specified device service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service methods. The listed methods will be called on each device service returned and included in the output. Available methods are: device_cfg_context, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_cfg_context, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_service: The device service identified by the specified DeviceServiceID.
             :rtype device_service: DeviceService

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device services. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that holds this service.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcName: Name of this service.
             :type SvcName: Array of String

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

             :param timestamp: The data returned will represent the device services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service methods. The listed methods will be called on each device service returned and included in the output. Available methods are: device_cfg_context, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceID. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData.
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

             :param select: The list of attributes to return for each DeviceService. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_services: An array of the DeviceService objects that match the specified input criteria.
             :rtype device_services: Array of DeviceService

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device services matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceCfgContextID: The internal NetMRI identifier of the Configuration context of declaration of this service.
             :type DeviceCfgContextID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device that holds this service.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcArtificialInd: Flag indicating this service does not exist in the device configuration.
             :type SvcArtificialInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SvcChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcConfigText: Original text of the definition of this service in the device configuration.
             :type SvcConfigText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcEndTime: The ending effective time of this record, or empty if still in effect.
             :type SvcEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcFirstSeenTime: The timestamp of when NetMRI first discovered this service.
             :type SvcFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcName: Name of this service.
             :type SvcName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcProvisionData: Internal data - do not modify, may change without warning.
             :type SvcProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcStartTime: The starting effective time of this record.
             :type SvcStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcTimestamp: The date and time this record was collected or calculated.
             :type SvcTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcType: A string indicating the kind of service that element is describing. One of : service, container, protLst, prtLst, protPrtLst.
             :type SvcType: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvcUseCount: Total count of usage of this service by other elements of the configuration (rules, other services).
             :type SvcUseCount: Array of Integer

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

             :param timestamp: The data returned will represent the device services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service methods. The listed methods will be called on each device service returned and included in the output. Available methods are: device_cfg_context, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceID. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData.
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

             :param select: The list of attributes to return for each DeviceService. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device services, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceCfgContextID, DeviceID, DeviceServiceID, SvcArtificialInd, SvcChangedCols, SvcConfigText, SvcEndTime, SvcFirstSeenTime, SvcName, SvcProvisionData, SvcStartTime, SvcTimestamp, SvcType, SvcUseCount.
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

             :return device_services: An array of the DeviceService objects that match the specified input criteria.
             :rtype device_services: Array of DeviceService

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device services matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceCfgContextID, DeviceID, DeviceServiceID, SvcArtificialInd, SvcChangedCols, SvcConfigText, SvcEndTime, SvcFirstSeenTime, SvcName, SvcProvisionData, SvcStartTime, SvcTimestamp, SvcType, SvcUseCount.

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

             :param op_DeviceCfgContextID: The operator to apply to the field DeviceCfgContextID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCfgContextID: The internal NetMRI identifier of the Configuration context of declaration of this service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceCfgContextID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceCfgContextID: If op_DeviceCfgContextID is specified, the field named in this input will be compared to the value in DeviceCfgContextID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceCfgContextID must be specified if op_DeviceCfgContextID is specified.
             :type val_f_DeviceCfgContextID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceCfgContextID: If op_DeviceCfgContextID is specified, this value will be compared to the value in DeviceCfgContextID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceCfgContextID must be specified if op_DeviceCfgContextID is specified.
             :type val_c_DeviceCfgContextID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device that holds this service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceServiceID: The operator to apply to the field DeviceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceServiceID: The internal NetMRI identifier for the Service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceServiceID: If op_DeviceServiceID is specified, the field named in this input will be compared to the value in DeviceServiceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceServiceID must be specified if op_DeviceServiceID is specified.
             :type val_f_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceServiceID: If op_DeviceServiceID is specified, this value will be compared to the value in DeviceServiceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceServiceID must be specified if op_DeviceServiceID is specified.
             :type val_c_DeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcArtificialInd: The operator to apply to the field SvcArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcArtificialInd: Flag indicating this service does not exist in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcArtificialInd: If op_SvcArtificialInd is specified, the field named in this input will be compared to the value in SvcArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcArtificialInd must be specified if op_SvcArtificialInd is specified.
             :type val_f_SvcArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcArtificialInd: If op_SvcArtificialInd is specified, this value will be compared to the value in SvcArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcArtificialInd must be specified if op_SvcArtificialInd is specified.
             :type val_c_SvcArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcChangedCols: The operator to apply to the field SvcChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcChangedCols: If op_SvcChangedCols is specified, the field named in this input will be compared to the value in SvcChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcChangedCols must be specified if op_SvcChangedCols is specified.
             :type val_f_SvcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcChangedCols: If op_SvcChangedCols is specified, this value will be compared to the value in SvcChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcChangedCols must be specified if op_SvcChangedCols is specified.
             :type val_c_SvcChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcConfigText: The operator to apply to the field SvcConfigText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcConfigText: Original text of the definition of this service in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcConfigText: If op_SvcConfigText is specified, the field named in this input will be compared to the value in SvcConfigText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcConfigText must be specified if op_SvcConfigText is specified.
             :type val_f_SvcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcConfigText: If op_SvcConfigText is specified, this value will be compared to the value in SvcConfigText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcConfigText must be specified if op_SvcConfigText is specified.
             :type val_c_SvcConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcEndTime: The operator to apply to the field SvcEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcEndTime: If op_SvcEndTime is specified, the field named in this input will be compared to the value in SvcEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcEndTime must be specified if op_SvcEndTime is specified.
             :type val_f_SvcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcEndTime: If op_SvcEndTime is specified, this value will be compared to the value in SvcEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcEndTime must be specified if op_SvcEndTime is specified.
             :type val_c_SvcEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcFirstSeenTime: The operator to apply to the field SvcFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcFirstSeenTime: The timestamp of when NetMRI first discovered this service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcFirstSeenTime: If op_SvcFirstSeenTime is specified, the field named in this input will be compared to the value in SvcFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcFirstSeenTime must be specified if op_SvcFirstSeenTime is specified.
             :type val_f_SvcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcFirstSeenTime: If op_SvcFirstSeenTime is specified, this value will be compared to the value in SvcFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcFirstSeenTime must be specified if op_SvcFirstSeenTime is specified.
             :type val_c_SvcFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcName: The operator to apply to the field SvcName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcName: Name of this service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcName: If op_SvcName is specified, the field named in this input will be compared to the value in SvcName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcName must be specified if op_SvcName is specified.
             :type val_f_SvcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcName: If op_SvcName is specified, this value will be compared to the value in SvcName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcName must be specified if op_SvcName is specified.
             :type val_c_SvcName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcProvisionData: The operator to apply to the field SvcProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcProvisionData: If op_SvcProvisionData is specified, the field named in this input will be compared to the value in SvcProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcProvisionData must be specified if op_SvcProvisionData is specified.
             :type val_f_SvcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcProvisionData: If op_SvcProvisionData is specified, this value will be compared to the value in SvcProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcProvisionData must be specified if op_SvcProvisionData is specified.
             :type val_c_SvcProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcStartTime: The operator to apply to the field SvcStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcStartTime: If op_SvcStartTime is specified, the field named in this input will be compared to the value in SvcStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcStartTime must be specified if op_SvcStartTime is specified.
             :type val_f_SvcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcStartTime: If op_SvcStartTime is specified, this value will be compared to the value in SvcStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcStartTime must be specified if op_SvcStartTime is specified.
             :type val_c_SvcStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcTimestamp: The operator to apply to the field SvcTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcTimestamp: If op_SvcTimestamp is specified, the field named in this input will be compared to the value in SvcTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcTimestamp must be specified if op_SvcTimestamp is specified.
             :type val_f_SvcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcTimestamp: If op_SvcTimestamp is specified, this value will be compared to the value in SvcTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcTimestamp must be specified if op_SvcTimestamp is specified.
             :type val_c_SvcTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcType: The operator to apply to the field SvcType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcType: A string indicating the kind of service that element is describing. One of : service, container, protLst, prtLst, protPrtLst. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcType: If op_SvcType is specified, the field named in this input will be compared to the value in SvcType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcType must be specified if op_SvcType is specified.
             :type val_f_SvcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcType: If op_SvcType is specified, this value will be compared to the value in SvcType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcType must be specified if op_SvcType is specified.
             :type val_c_SvcType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvcUseCount: The operator to apply to the field SvcUseCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvcUseCount: Total count of usage of this service by other elements of the configuration (rules, other services). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvcUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvcUseCount: If op_SvcUseCount is specified, the field named in this input will be compared to the value in SvcUseCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvcUseCount must be specified if op_SvcUseCount is specified.
             :type val_f_SvcUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvcUseCount: If op_SvcUseCount is specified, this value will be compared to the value in SvcUseCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvcUseCount must be specified if op_SvcUseCount is specified.
             :type val_c_SvcUseCount: String

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

             :param timestamp: The data returned will represent the device services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service methods. The listed methods will be called on each device service returned and included in the output. Available methods are: device_cfg_context, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceID. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData.
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

             :param select: The list of attributes to return for each DeviceService. Valid values are DeviceServiceID, DeviceID, DeviceCfgContextID, DataSourceID, SvcFirstSeenTime, SvcStartTime, SvcEndTime, SvcTimestamp, SvcChangedCols, SvcName, SvcUseCount, SvcArtificialInd, SvcType, SvcConfigText, SvcProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_services: An array of the DeviceService objects that match the specified input criteria.
             :rtype device_services: Array of DeviceService

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def device_cfg_context(self, **kwargs):
        """The Configuration context of declaration of this service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The Configuration context of declaration of this service.
             :rtype : DeviceCfgContext

            """

        return self.api_request(self._get_method_fullname("device_cfg_context"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Integer

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

             :param DeviceServiceID: The internal NetMRI identifier for the Service.
             :type DeviceServiceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def to_detail(self, **kwargs):
        """Returns the deail for an service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: None
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param view: 0=tostring, 1=tooltip, 2-popup, 3=tostring/field, 4=tooltip/field, 5=popup/field
             :type view: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return detail: None
             :rtype detail: String

            """

        return self.api_request(self._get_method_fullname("to_detail"), kwargs)
