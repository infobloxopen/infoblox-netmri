from ..broker import Broker


class DeviceObjectBroker(Broker):
    controller = "device_objects"

    def show(self, **kwargs):
        """Shows the details for the specified device object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object methods. The listed methods will be called on each device object returned and included in the output. Available methods are: device_cfg_context, data_source, device.
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

             :return device_object: The device object identified by the specified DeviceObjectID.
             :rtype device_object: DeviceObject

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available device objects. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this network object belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjName: Name of this network object.
             :type ObjName: Array of String

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

             :param timestamp: The data returned will represent the device objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object methods. The listed methods will be called on each device object returned and included in the output. Available methods are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectID. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData.
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

             :param select: The list of attributes to return for each DeviceObject. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_objects: An array of the DeviceObject objects that match the specified input criteria.
             :rtype device_objects: Array of DeviceObject

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available device objects matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceCfgContextID: The internal NetMRI identifier of the Configuration context of declaration of this network object.
             :type DeviceCfgContextID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to which this network object belongs.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjArtificialInd: Flag indicating this object network does not exist in the device configuration.
             :type ObjArtificialInd: Array of Boolean

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ObjChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjConfigText: Original text of the definition of his network object in the device configuration.
             :type ObjConfigText: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjEndTime: The ending effective time of this record, or empty if still in effect.
             :type ObjEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjFirstSeenTime: The timestamp of when NetMRI first discovered this network object.
             :type ObjFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjName: Name of this network object.
             :type ObjName: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjProvisionData: Internal data - do not modify, may change without warning.
             :type ObjProvisionData: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjStartTime: The starting effective time of this record.
             :type ObjStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjTimestamp: The date and time this record was collected or calculated.
             :type ObjTimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ObjUseCount: Total count of usage of this network by other elements of the configuration (rules, other network objects).
             :type ObjUseCount: Array of Integer

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

             :param timestamp: The data returned will represent the device objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object methods. The listed methods will be called on each device object returned and included in the output. Available methods are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectID. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData.
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

             :param select: The list of attributes to return for each DeviceObject. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device objects, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceCfgContextID, DeviceID, DeviceObjectID, ObjArtificialInd, ObjChangedCols, ObjConfigText, ObjEndTime, ObjFirstSeenTime, ObjName, ObjProvisionData, ObjStartTime, ObjTimestamp, ObjUseCount.
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

             :return device_objects: An array of the DeviceObject objects that match the specified input criteria.
             :rtype device_objects: Array of DeviceObject

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device objects matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceCfgContextID, DeviceID, DeviceObjectID, ObjArtificialInd, ObjChangedCols, ObjConfigText, ObjEndTime, ObjFirstSeenTime, ObjName, ObjProvisionData, ObjStartTime, ObjTimestamp, ObjUseCount.

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

             :param op_DeviceCfgContextID: The operator to apply to the field DeviceCfgContextID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceCfgContextID: The internal NetMRI identifier of the Configuration context of declaration of this network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device to which this network object belongs. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceObjectID: The operator to apply to the field DeviceObjectID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceObjectID: The internal NetMRI identifier for this network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceObjectID: If op_DeviceObjectID is specified, the field named in this input will be compared to the value in DeviceObjectID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceObjectID must be specified if op_DeviceObjectID is specified.
             :type val_f_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceObjectID: If op_DeviceObjectID is specified, this value will be compared to the value in DeviceObjectID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceObjectID must be specified if op_DeviceObjectID is specified.
             :type val_c_DeviceObjectID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjArtificialInd: The operator to apply to the field ObjArtificialInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjArtificialInd: Flag indicating this object network does not exist in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjArtificialInd: If op_ObjArtificialInd is specified, the field named in this input will be compared to the value in ObjArtificialInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjArtificialInd must be specified if op_ObjArtificialInd is specified.
             :type val_f_ObjArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjArtificialInd: If op_ObjArtificialInd is specified, this value will be compared to the value in ObjArtificialInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjArtificialInd must be specified if op_ObjArtificialInd is specified.
             :type val_c_ObjArtificialInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjChangedCols: The operator to apply to the field ObjChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjChangedCols: If op_ObjChangedCols is specified, the field named in this input will be compared to the value in ObjChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjChangedCols must be specified if op_ObjChangedCols is specified.
             :type val_f_ObjChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjChangedCols: If op_ObjChangedCols is specified, this value will be compared to the value in ObjChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjChangedCols must be specified if op_ObjChangedCols is specified.
             :type val_c_ObjChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjConfigText: The operator to apply to the field ObjConfigText. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjConfigText: Original text of the definition of his network object in the device configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjConfigText: If op_ObjConfigText is specified, the field named in this input will be compared to the value in ObjConfigText using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjConfigText must be specified if op_ObjConfigText is specified.
             :type val_f_ObjConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjConfigText: If op_ObjConfigText is specified, this value will be compared to the value in ObjConfigText using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjConfigText must be specified if op_ObjConfigText is specified.
             :type val_c_ObjConfigText: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjEndTime: The operator to apply to the field ObjEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjEndTime: If op_ObjEndTime is specified, the field named in this input will be compared to the value in ObjEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjEndTime must be specified if op_ObjEndTime is specified.
             :type val_f_ObjEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjEndTime: If op_ObjEndTime is specified, this value will be compared to the value in ObjEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjEndTime must be specified if op_ObjEndTime is specified.
             :type val_c_ObjEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjFirstSeenTime: The operator to apply to the field ObjFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjFirstSeenTime: The timestamp of when NetMRI first discovered this network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjFirstSeenTime: If op_ObjFirstSeenTime is specified, the field named in this input will be compared to the value in ObjFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjFirstSeenTime must be specified if op_ObjFirstSeenTime is specified.
             :type val_f_ObjFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjFirstSeenTime: If op_ObjFirstSeenTime is specified, this value will be compared to the value in ObjFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjFirstSeenTime must be specified if op_ObjFirstSeenTime is specified.
             :type val_c_ObjFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjName: The operator to apply to the field ObjName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjName: Name of this network object. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjName: If op_ObjName is specified, the field named in this input will be compared to the value in ObjName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjName must be specified if op_ObjName is specified.
             :type val_f_ObjName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjName: If op_ObjName is specified, this value will be compared to the value in ObjName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjName must be specified if op_ObjName is specified.
             :type val_c_ObjName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjProvisionData: The operator to apply to the field ObjProvisionData. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjProvisionData: Internal data - do not modify, may change without warning. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjProvisionData: If op_ObjProvisionData is specified, the field named in this input will be compared to the value in ObjProvisionData using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjProvisionData must be specified if op_ObjProvisionData is specified.
             :type val_f_ObjProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjProvisionData: If op_ObjProvisionData is specified, this value will be compared to the value in ObjProvisionData using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjProvisionData must be specified if op_ObjProvisionData is specified.
             :type val_c_ObjProvisionData: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjStartTime: The operator to apply to the field ObjStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjStartTime: If op_ObjStartTime is specified, the field named in this input will be compared to the value in ObjStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjStartTime must be specified if op_ObjStartTime is specified.
             :type val_f_ObjStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjStartTime: If op_ObjStartTime is specified, this value will be compared to the value in ObjStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjStartTime must be specified if op_ObjStartTime is specified.
             :type val_c_ObjStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjTimestamp: The operator to apply to the field ObjTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjTimestamp: If op_ObjTimestamp is specified, the field named in this input will be compared to the value in ObjTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjTimestamp must be specified if op_ObjTimestamp is specified.
             :type val_f_ObjTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjTimestamp: If op_ObjTimestamp is specified, this value will be compared to the value in ObjTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjTimestamp must be specified if op_ObjTimestamp is specified.
             :type val_c_ObjTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ObjUseCount: The operator to apply to the field ObjUseCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ObjUseCount: Total count of usage of this network by other elements of the configuration (rules, other network objects). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ObjUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ObjUseCount: If op_ObjUseCount is specified, the field named in this input will be compared to the value in ObjUseCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ObjUseCount must be specified if op_ObjUseCount is specified.
             :type val_f_ObjUseCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ObjUseCount: If op_ObjUseCount is specified, this value will be compared to the value in ObjUseCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ObjUseCount must be specified if op_ObjUseCount is specified.
             :type val_c_ObjUseCount: String

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

             :param timestamp: The data returned will represent the device objects as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of device object methods. The listed methods will be called on each device object returned and included in the output. Available methods are: device_cfg_context, data_source, device.
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
            |  ``default:`` DeviceObjectID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceObjectID. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData.
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

             :param select: The list of attributes to return for each DeviceObject. Valid values are DeviceObjectID, DeviceID, DeviceCfgContextID, DataSourceID, ObjFirstSeenTime, ObjStartTime, ObjEndTime, ObjTimestamp, ObjChangedCols, ObjName, ObjUseCount, ObjArtificialInd, ObjConfigText, ObjProvisionData. If empty or omitted, all attributes will be returned.
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

             :return device_objects: An array of the DeviceObject objects that match the specified input criteria.
             :rtype device_objects: Array of DeviceObject

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def device_cfg_context(self, **kwargs):
        """The configuration context to which this network object belongs.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The configuration context to which this network object belongs.
             :rtype : DeviceCfgContext

            """

        return self.api_request(self._get_method_fullname("device_cfg_context"), kwargs)

    def device(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceObjectID: The internal NetMRI identifier for this network object.
             :type DeviceObjectID: Integer

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
        """Returns the deail for an object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param object_id: None
             :type object_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param view: 0=tostring, 1=tooltip, 2-popup
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
