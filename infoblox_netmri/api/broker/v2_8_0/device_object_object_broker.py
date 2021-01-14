from ..broker import Broker


class DeviceObjectObjectBroker(Broker):
    controller = "device_object_objects"

    def show(self, **kwargs):
        """Shows the details for the specified device object object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object object methods. The listed methods will be called on each device object object returned and included in the output. Available methods are: parent_device_object, child_device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_object, child_device_object, data_source, device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_object_object: The device object object identified by the specified DeviceObjectObjectID.
             :rtype device_object_object: DeviceObjectObject

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device object objects. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this network objects.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Array of Integer

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

             :param timestamp: The data returned will represent the device object objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object object methods. The listed methods will be called on each device object object returned and included in the output. Available methods are: parent_device_object, child_device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_object, child_device_object, data_source, device.
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
            |  ``default:`` DeviceObjectObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectObjectID. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData.
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

             :param select: The list of attributes to return for each DeviceObjectObject. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_object_objects: An array of the DeviceObjectObject objects that match the specified input criteria.
             :rtype device_object_objects: Array of DeviceObjectObject

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device object objects matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ChildDeviceObjectID: The internal NetMRI identifier of the child network object (the used service).
             :type ChildDeviceObjectID: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device to which belongs this network objects.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type OoChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoEndTime: The ending effective time of this record, or empty if still in effect.
             :type OoEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoFirstSeenTime: The timestamp of when NetMRI saw for the first time this relationship.
             :type OoFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoProvisionData: Internal data - do not modify, may change without warning.
             :type OoProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoStartTime: The starting effective time of this record.
             :type OoStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param OoTimestamp: The date and time this record was collected or calculated.
             :type OoTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ParentDeviceObjectID: The internal NetMRI identifier of the parent network object (the user).
             :type ParentDeviceObjectID: Array of Integer

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

             :param timestamp: The data returned will represent the device object objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object object methods. The listed methods will be called on each device object object returned and included in the output. Available methods are: parent_device_object, child_device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_object, child_device_object, data_source, device.
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
            |  ``default:`` DeviceObjectObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectObjectID. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData.
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

             :param select: The list of attributes to return for each DeviceObjectObject. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device object objects, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ChildDeviceObjectID, DataSourceID, DeviceID, DeviceObjectObjectID, OoChangedCols, OoEndTime, OoFirstSeenTime, OoProvisionData, OoStartTime, OoTimestamp, ParentDeviceObjectID.
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

             :return device_object_objects: An array of the DeviceObjectObject objects that match the specified input criteria.
             :rtype device_object_objects: Array of DeviceObjectObject

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device object objects matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ChildDeviceObjectID, DataSourceID, DeviceID, DeviceObjectObjectID, OoChangedCols, OoEndTime, OoFirstSeenTime, OoProvisionData, OoStartTime, OoTimestamp, ParentDeviceObjectID.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ChildDeviceObjectID: The operator to apply to the field ChildDeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ChildDeviceObjectID: The internal NetMRI identifier of the child network object (the used service). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ChildDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ChildDeviceObjectID: If op_ChildDeviceObjectID is specified, the field named in this input will be compared to the value in ChildDeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ChildDeviceObjectID must be specified if op_ChildDeviceObjectID is specified.
             :type val_f_ChildDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ChildDeviceObjectID: If op_ChildDeviceObjectID is specified, this value will be compared to the value in ChildDeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ChildDeviceObjectID must be specified if op_ChildDeviceObjectID is specified.
             :type val_c_ChildDeviceObjectID: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which belongs this network objects. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceObjectObjectID: The operator to apply to the field DeviceObjectObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceObjectObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceObjectObjectID: If op_DeviceObjectObjectID is specified, the field named in this input will be compared to the value in DeviceObjectObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceObjectObjectID must be specified if op_DeviceObjectObjectID is specified.
             :type val_f_DeviceObjectObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceObjectObjectID: If op_DeviceObjectObjectID is specified, this value will be compared to the value in DeviceObjectObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceObjectObjectID must be specified if op_DeviceObjectObjectID is specified.
             :type val_c_DeviceObjectObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoChangedCols: The operator to apply to the field OoChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoChangedCols: If op_OoChangedCols is specified, the field named in this input will be compared to the value in OoChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoChangedCols must be specified if op_OoChangedCols is specified.
             :type val_f_OoChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoChangedCols: If op_OoChangedCols is specified, this value will be compared to the value in OoChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoChangedCols must be specified if op_OoChangedCols is specified.
             :type val_c_OoChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoEndTime: The operator to apply to the field OoEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoEndTime: If op_OoEndTime is specified, the field named in this input will be compared to the value in OoEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoEndTime must be specified if op_OoEndTime is specified.
             :type val_f_OoEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoEndTime: If op_OoEndTime is specified, this value will be compared to the value in OoEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoEndTime must be specified if op_OoEndTime is specified.
             :type val_c_OoEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoFirstSeenTime: The operator to apply to the field OoFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoFirstSeenTime: The timestamp of when NetMRI saw for the first time this relationship. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoFirstSeenTime: If op_OoFirstSeenTime is specified, the field named in this input will be compared to the value in OoFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoFirstSeenTime must be specified if op_OoFirstSeenTime is specified.
             :type val_f_OoFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoFirstSeenTime: If op_OoFirstSeenTime is specified, this value will be compared to the value in OoFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoFirstSeenTime must be specified if op_OoFirstSeenTime is specified.
             :type val_c_OoFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoProvisionData: The operator to apply to the field OoProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoProvisionData: If op_OoProvisionData is specified, the field named in this input will be compared to the value in OoProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoProvisionData must be specified if op_OoProvisionData is specified.
             :type val_f_OoProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoProvisionData: If op_OoProvisionData is specified, this value will be compared to the value in OoProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoProvisionData must be specified if op_OoProvisionData is specified.
             :type val_c_OoProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoStartTime: The operator to apply to the field OoStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoStartTime: If op_OoStartTime is specified, the field named in this input will be compared to the value in OoStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoStartTime must be specified if op_OoStartTime is specified.
             :type val_f_OoStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoStartTime: If op_OoStartTime is specified, this value will be compared to the value in OoStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoStartTime must be specified if op_OoStartTime is specified.
             :type val_c_OoStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_OoTimestamp: The operator to apply to the field OoTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. OoTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_OoTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_OoTimestamp: If op_OoTimestamp is specified, the field named in this input will be compared to the value in OoTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_OoTimestamp must be specified if op_OoTimestamp is specified.
             :type val_f_OoTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_OoTimestamp: If op_OoTimestamp is specified, this value will be compared to the value in OoTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_OoTimestamp must be specified if op_OoTimestamp is specified.
             :type val_c_OoTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ParentDeviceObjectID: The operator to apply to the field ParentDeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ParentDeviceObjectID: The internal NetMRI identifier of the parent network object (the user). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ParentDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ParentDeviceObjectID: If op_ParentDeviceObjectID is specified, the field named in this input will be compared to the value in ParentDeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ParentDeviceObjectID must be specified if op_ParentDeviceObjectID is specified.
             :type val_f_ParentDeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ParentDeviceObjectID: If op_ParentDeviceObjectID is specified, this value will be compared to the value in ParentDeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ParentDeviceObjectID must be specified if op_ParentDeviceObjectID is specified.
             :type val_c_ParentDeviceObjectID: String

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

             :param timestamp: The data returned will represent the device object objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object object methods. The listed methods will be called on each device object object returned and included in the output. Available methods are: parent_device_object, child_device_object, data_source, device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: parent_device_object, child_device_object, data_source, device.
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
            |  ``default:`` DeviceObjectObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectObjectID. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData.
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

             :param select: The list of attributes to return for each DeviceObjectObject. Valid values are DeviceObjectObjectID, DeviceID, DataSourceID, ParentDeviceObjectID, ChildDeviceObjectID, OoFirstSeenTime, OoStartTime, OoEndTime, OoTimestamp, OoChangedCols, OoProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_object_objects: An array of the DeviceObjectObject objects that match the specified input criteria.
             :rtype device_object_objects: Array of DeviceObjectObject

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def parent_device_object(self, **kwargs):
        """The parent network object of this relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The parent network object of this relationship.
             :rtype : DeviceObject

            """

        return self.api_request(self._get_method_fullname("parent_device_object"), kwargs)

    def child_device_object(self, **kwargs):
        """The child network object of this relationship.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The child network object of this relationship.
             :rtype : DeviceObject

            """

        return self.api_request(self._get_method_fullname("child_device_object"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Integer

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

             :param DeviceObjectObjectID: The internal NetMRI identifier of this usage relationship between network objects.
             :type DeviceObjectObjectID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
