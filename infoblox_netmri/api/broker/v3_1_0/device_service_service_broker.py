from ..broker import Broker


class DeviceServiceServiceBroker(Broker):
    controller = "device_service_services"

    def show(self, **kwargs):
        """Shows the details for the specified device service service.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service service methods. The listed methods will be called on each device service service returned and included in the output. Available methods are: parent_device_service, child_device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_service, child_device_service, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_service_service: The device service service identified by the specified DeviceServiceServiceID.
             :rtype device_service_service: DeviceServiceService

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device service services. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this services.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Array of Integer

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

             :param timestamp: The data returned will represent the device service services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service service methods. The listed methods will be called on each device service service returned and included in the output. Available methods are: parent_device_service, child_device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_service, child_device_service, data_source, device.
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
            |  ``default:`` DeviceServiceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceServiceID. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData.
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

             :param select: The list of attributes to return for each DeviceServiceService. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_service_services: An array of the DeviceServiceService objects that match the specified input criteria.
             :rtype device_service_services: Array of DeviceServiceService

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device service services matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChildDeviceServiceID: The internal NetMRI identifier of the child service (the used service).
             :type ChildDeviceServiceID: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this services.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceServiceID: The internal NetMRI identifier of the parent service (the user).
             :type ParentDeviceServiceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SvsvChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvEndTime: The ending effective time of this record, or empty if still in effect.
             :type SvsvEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvFirstSeenTime: The timestamp of when NetMRI saw for the first time this relationship.
             :type SvsvFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvProvisionData: Internal data - do not modify, may change without warning.
             :type SvsvProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvStartTime: The starting effective time of this record.
             :type SvsvStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvTimestamp: The date and time this record was collected or calculated.
             :type SvsvTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SvsvUsage: An indicator of the kind of relationship. One of : child, protID, srcPrtID, dstPrtID, protDstID. The regular indicator is 'child'.
             :type SvsvUsage: Array of String

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

             :param timestamp: The data returned will represent the device service services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service service methods. The listed methods will be called on each device service service returned and included in the output. Available methods are: parent_device_service, child_device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_service, child_device_service, data_source, device.
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
            |  ``default:`` DeviceServiceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceServiceID. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData.
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

             :param select: The list of attributes to return for each DeviceServiceService. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device service services, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ChildDeviceServiceID, DataSourceID, DeviceID, DeviceServiceServiceID, ParentDeviceServiceID, SvsvChangedCols, SvsvEndTime, SvsvFirstSeenTime, SvsvProvisionData, SvsvStartTime, SvsvTimestamp, SvsvUsage.
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

             :return device_service_services: An array of the DeviceServiceService objects that match the specified input criteria.
             :rtype device_service_services: Array of DeviceServiceService

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device service services matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ChildDeviceServiceID, DataSourceID, DeviceID, DeviceServiceServiceID, ParentDeviceServiceID, SvsvChangedCols, SvsvEndTime, SvsvFirstSeenTime, SvsvProvisionData, SvsvStartTime, SvsvTimestamp, SvsvUsage.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChildDeviceServiceID: The operator to apply to the field ChildDeviceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChildDeviceServiceID: The internal NetMRI identifier of the child service (the used service). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChildDeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChildDeviceServiceID: If op_ChildDeviceServiceID is specified, the field named in this input will be compared to the value in ChildDeviceServiceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChildDeviceServiceID must be specified if op_ChildDeviceServiceID is specified.
             :type val_f_ChildDeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChildDeviceServiceID: If op_ChildDeviceServiceID is specified, this value will be compared to the value in ChildDeviceServiceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChildDeviceServiceID must be specified if op_ChildDeviceServiceID is specified.
             :type val_c_ChildDeviceServiceID: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which belongs this services. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceServiceServiceID: The operator to apply to the field DeviceServiceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceServiceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceServiceServiceID: If op_DeviceServiceServiceID is specified, the field named in this input will be compared to the value in DeviceServiceServiceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceServiceServiceID must be specified if op_DeviceServiceServiceID is specified.
             :type val_f_DeviceServiceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceServiceServiceID: If op_DeviceServiceServiceID is specified, this value will be compared to the value in DeviceServiceServiceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceServiceServiceID must be specified if op_DeviceServiceServiceID is specified.
             :type val_c_DeviceServiceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ParentDeviceServiceID: The operator to apply to the field ParentDeviceServiceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ParentDeviceServiceID: The internal NetMRI identifier of the parent service (the user). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ParentDeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ParentDeviceServiceID: If op_ParentDeviceServiceID is specified, the field named in this input will be compared to the value in ParentDeviceServiceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ParentDeviceServiceID must be specified if op_ParentDeviceServiceID is specified.
             :type val_f_ParentDeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ParentDeviceServiceID: If op_ParentDeviceServiceID is specified, this value will be compared to the value in ParentDeviceServiceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ParentDeviceServiceID must be specified if op_ParentDeviceServiceID is specified.
             :type val_c_ParentDeviceServiceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvChangedCols: The operator to apply to the field SvsvChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvChangedCols: If op_SvsvChangedCols is specified, the field named in this input will be compared to the value in SvsvChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvChangedCols must be specified if op_SvsvChangedCols is specified.
             :type val_f_SvsvChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvChangedCols: If op_SvsvChangedCols is specified, this value will be compared to the value in SvsvChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvChangedCols must be specified if op_SvsvChangedCols is specified.
             :type val_c_SvsvChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvEndTime: The operator to apply to the field SvsvEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvEndTime: If op_SvsvEndTime is specified, the field named in this input will be compared to the value in SvsvEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvEndTime must be specified if op_SvsvEndTime is specified.
             :type val_f_SvsvEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvEndTime: If op_SvsvEndTime is specified, this value will be compared to the value in SvsvEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvEndTime must be specified if op_SvsvEndTime is specified.
             :type val_c_SvsvEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvFirstSeenTime: The operator to apply to the field SvsvFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvFirstSeenTime: The timestamp of when NetMRI saw for the first time this relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvFirstSeenTime: If op_SvsvFirstSeenTime is specified, the field named in this input will be compared to the value in SvsvFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvFirstSeenTime must be specified if op_SvsvFirstSeenTime is specified.
             :type val_f_SvsvFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvFirstSeenTime: If op_SvsvFirstSeenTime is specified, this value will be compared to the value in SvsvFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvFirstSeenTime must be specified if op_SvsvFirstSeenTime is specified.
             :type val_c_SvsvFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvProvisionData: The operator to apply to the field SvsvProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvProvisionData: If op_SvsvProvisionData is specified, the field named in this input will be compared to the value in SvsvProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvProvisionData must be specified if op_SvsvProvisionData is specified.
             :type val_f_SvsvProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvProvisionData: If op_SvsvProvisionData is specified, this value will be compared to the value in SvsvProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvProvisionData must be specified if op_SvsvProvisionData is specified.
             :type val_c_SvsvProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvStartTime: The operator to apply to the field SvsvStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvStartTime: If op_SvsvStartTime is specified, the field named in this input will be compared to the value in SvsvStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvStartTime must be specified if op_SvsvStartTime is specified.
             :type val_f_SvsvStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvStartTime: If op_SvsvStartTime is specified, this value will be compared to the value in SvsvStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvStartTime must be specified if op_SvsvStartTime is specified.
             :type val_c_SvsvStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvTimestamp: The operator to apply to the field SvsvTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvTimestamp: If op_SvsvTimestamp is specified, the field named in this input will be compared to the value in SvsvTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvTimestamp must be specified if op_SvsvTimestamp is specified.
             :type val_f_SvsvTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvTimestamp: If op_SvsvTimestamp is specified, this value will be compared to the value in SvsvTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvTimestamp must be specified if op_SvsvTimestamp is specified.
             :type val_c_SvsvTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SvsvUsage: The operator to apply to the field SvsvUsage. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SvsvUsage: An indicator of the kind of relationship. One of : child, protID, srcPrtID, dstPrtID, protDstID. The regular indicator is 'child'. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SvsvUsage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SvsvUsage: If op_SvsvUsage is specified, the field named in this input will be compared to the value in SvsvUsage using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SvsvUsage must be specified if op_SvsvUsage is specified.
             :type val_f_SvsvUsage: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SvsvUsage: If op_SvsvUsage is specified, this value will be compared to the value in SvsvUsage using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SvsvUsage must be specified if op_SvsvUsage is specified.
             :type val_c_SvsvUsage: String

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

             :param timestamp: The data returned will represent the device service services as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device service service methods. The listed methods will be called on each device service service returned and included in the output. Available methods are: parent_device_service, child_device_service, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_service, child_device_service, data_source, device.
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
            |  ``default:`` DeviceServiceServiceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceServiceServiceID. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData.
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

             :param select: The list of attributes to return for each DeviceServiceService. Valid values are DeviceServiceServiceID, DeviceID, DataSourceID, ParentDeviceServiceID, ChildDeviceServiceID, SvsvFirstSeenTime, SvsvStartTime, SvsvEndTime, SvsvTimestamp, SvsvChangedCols, SvsvUsage, SvsvProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_service_services: An array of the DeviceServiceService objects that match the specified input criteria.
             :rtype device_service_services: Array of DeviceServiceService

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def parent_device_service(self, **kwargs):
        """The parent service object of this relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The parent service object of this relationship.
             :rtype : DeviceService

            """

        return self.api_request(self._get_method_fullname("parent_device_service"), kwargs)

    def child_device_service(self, **kwargs):
        """The child service object of this relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The child service object of this relationship.
             :rtype : DeviceService

            """

        return self.api_request(self._get_method_fullname("child_device_service"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Integer

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

             :param DeviceServiceServiceID: The internal NetMRI identifier of this usage relationship between service objects.
             :type DeviceServiceServiceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
