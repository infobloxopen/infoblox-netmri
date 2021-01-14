from ..broker import Broker


class ConfigRevisionBroker(Broker):
    controller = "config_revisions"

    def show(self, **kwargs):
        """Shows the details for the specified config revision.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of config revision methods. The listed methods will be called on each config revision returned and included in the output. Available methods are: text, edited_by, data_source, device, infradevice, devicesetting.
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

             :return config_revision: The config revision identified by the specified ConfigRevisionID.
             :rtype config_revision: ConfigRevision

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available config revisions. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigTimestamp: The date/time this configuration revision was first collected (i.e., the starting effective time of the configuration).
             :type ConfigTimestamp: Array of DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this configuration revision was collected.
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

             :param starttime: The data returned will represent the config revisions first collected with this date and time as lower boundary. If omitted, the result will indicate all config revisions.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: The data returned will represent the config revisions first collected with this date and time as upper boundary. If omitted, the result will indicate all config revisions.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of config revision methods. The listed methods will be called on each config revision returned and included in the output. Available methods are: text, edited_by, data_source, device, infradevice, devicesetting.
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
            |  ``default:`` ConfigRevisionID

             :param sort: The data field(s) to use for sorting the output. Default is ConfigRevisionID. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected.
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

             :param select: The list of attributes to return for each ConfigRevision. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected. If empty or omitted, all attributes will be returned.
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

             :return config_revisions: An array of the ConfigRevision objects that match the specified input criteria.
             :rtype config_revisions: Array of ConfigRevision

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available config revisions matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigDiffs: A measure of the amount of differences between this configuration revision and the previous revision.
             :type ConfigDiffs: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigRevision: The revision number of the file; used internally by NetMRI.
             :type ConfigRevision: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigTimestamp: The date/time this configuration revision was first collected (i.e., the starting effective time of the configuration).
             :type ConfigTimestamp: Array of DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ConfigType: The type of the configuration file: Running or Saved.
             :type ConfigType: Array of String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: The internal NetMRI identifier for the collector NetMRI that collected this data record.
             :type DataSourceID: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which this configuration revision was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param LastCollected: The last time this revision was collected from the device.
             :type LastCollected: Array of DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PreviousTimestamp: The date/time that the previous configuration revision was first collected.
             :type PreviousTimestamp: Array of DateTime

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

             :param starttime: The data returned will represent the config revisions first collected with this date and time as lower boundary. If omitted, the result will indicate all config revisions.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: The data returned will represent the config revisions first collected with this date and time as upper boundary. If omitted, the result will indicate all config revisions.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of config revision methods. The listed methods will be called on each config revision returned and included in the output. Available methods are: text, edited_by, data_source, device, infradevice, devicesetting.
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
            |  ``default:`` ConfigRevisionID

             :param sort: The data field(s) to use for sorting the output. Default is ConfigRevisionID. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected.
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

             :param select: The list of attributes to return for each ConfigRevision. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against config revisions, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ConfigDiffs, ConfigRevision, ConfigRevisionID, ConfigTimestamp, ConfigType, DataSourceID, DeviceID, LastCollected, PreviousTimestamp.
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

             :return config_revisions: An array of the ConfigRevision objects that match the specified input criteria.
             :rtype config_revisions: Array of ConfigRevision

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available config revisions matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ConfigDiffs, ConfigRevision, ConfigRevisionID, ConfigTimestamp, ConfigType, DataSourceID, DeviceID, LastCollected, PreviousTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigDiffs: The operator to apply to the field ConfigDiffs. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigDiffs: A measure of the amount of differences between this configuration revision and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigDiffs: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigDiffs: If op_ConfigDiffs is specified, the field named in this input will be compared to the value in ConfigDiffs using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigDiffs must be specified if op_ConfigDiffs is specified.
             :type val_f_ConfigDiffs: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigDiffs: If op_ConfigDiffs is specified, this value will be compared to the value in ConfigDiffs using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigDiffs must be specified if op_ConfigDiffs is specified.
             :type val_c_ConfigDiffs: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigRevision: The operator to apply to the field ConfigRevision. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigRevision: The revision number of the file; used internally by NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigRevision: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigRevision: If op_ConfigRevision is specified, the field named in this input will be compared to the value in ConfigRevision using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigRevision must be specified if op_ConfigRevision is specified.
             :type val_f_ConfigRevision: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigRevision: If op_ConfigRevision is specified, this value will be compared to the value in ConfigRevision using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigRevision must be specified if op_ConfigRevision is specified.
             :type val_c_ConfigRevision: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigRevisionID: The operator to apply to the field ConfigRevisionID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigRevisionID: The internal NetMRI identifier for the configuration file revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigRevisionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigRevisionID: If op_ConfigRevisionID is specified, the field named in this input will be compared to the value in ConfigRevisionID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigRevisionID must be specified if op_ConfigRevisionID is specified.
             :type val_f_ConfigRevisionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigRevisionID: If op_ConfigRevisionID is specified, this value will be compared to the value in ConfigRevisionID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigRevisionID must be specified if op_ConfigRevisionID is specified.
             :type val_c_ConfigRevisionID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigTimestamp: The operator to apply to the field ConfigTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigTimestamp: The date/time this configuration revision was first collected (i.e., the starting effective time of the configuration). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigTimestamp: If op_ConfigTimestamp is specified, the field named in this input will be compared to the value in ConfigTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigTimestamp must be specified if op_ConfigTimestamp is specified.
             :type val_f_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigTimestamp: If op_ConfigTimestamp is specified, this value will be compared to the value in ConfigTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigTimestamp must be specified if op_ConfigTimestamp is specified.
             :type val_c_ConfigTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ConfigType: The operator to apply to the field ConfigType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ConfigType: The type of the configuration file: Running or Saved. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ConfigType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ConfigType: If op_ConfigType is specified, the field named in this input will be compared to the value in ConfigType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ConfigType must be specified if op_ConfigType is specified.
             :type val_f_ConfigType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ConfigType: If op_ConfigType is specified, this value will be compared to the value in ConfigType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ConfigType must be specified if op_ConfigType is specified.
             :type val_c_ConfigType: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which this configuration revision was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_LastCollected: The operator to apply to the field LastCollected. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. LastCollected: The last time this revision was collected from the device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_LastCollected: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_LastCollected: If op_LastCollected is specified, the field named in this input will be compared to the value in LastCollected using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_LastCollected must be specified if op_LastCollected is specified.
             :type val_f_LastCollected: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_LastCollected: If op_LastCollected is specified, this value will be compared to the value in LastCollected using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_LastCollected must be specified if op_LastCollected is specified.
             :type val_c_LastCollected: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PreviousTimestamp: The operator to apply to the field PreviousTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PreviousTimestamp: The date/time that the previous configuration revision was first collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PreviousTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PreviousTimestamp: If op_PreviousTimestamp is specified, the field named in this input will be compared to the value in PreviousTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PreviousTimestamp must be specified if op_PreviousTimestamp is specified.
             :type val_f_PreviousTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PreviousTimestamp: If op_PreviousTimestamp is specified, this value will be compared to the value in PreviousTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PreviousTimestamp must be specified if op_PreviousTimestamp is specified.
             :type val_c_PreviousTimestamp: String

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

             :param starttime: The data returned will represent the config revisions first collected with this date and time as lower boundary. If omitted, the result will indicate all config revisions.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: The data returned will represent the config revisions first collected with this date and time as upper boundary. If omitted, the result will indicate all config revisions.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of config revision methods. The listed methods will be called on each config revision returned and included in the output. Available methods are: text, edited_by, data_source, device, infradevice, devicesetting.
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
            |  ``default:`` ConfigRevisionID

             :param sort: The data field(s) to use for sorting the output. Default is ConfigRevisionID. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected.
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

             :param select: The list of attributes to return for each ConfigRevision. Valid values are ConfigRevisionID, DataSourceID, DeviceID, ConfigType, ConfigRevision, ConfigTimestamp, PreviousTimestamp, ConfigDiffs, LastCollected. If empty or omitted, all attributes will be returned.
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

             :return config_revisions: An array of the ConfigRevision objects that match the specified input criteria.
             :rtype config_revisions: Array of ConfigRevision

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def text(self, **kwargs):
        """Returns the text of the configuration file.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : Returns the text of the configuration file.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("text"), kwargs)

    def edited_by(self, **kwargs):
        """The user(s) that modified the file between the last revision and this one.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The user(s) that modified the file between the last revision and this one.
             :rtype : String

            """

        return self.api_request(self._get_method_fullname("edited_by"), kwargs)

    def data_source(self, **kwargs):
        """The NetMRI device that collected this record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

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
        """The device from which this configuration revision was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this configuration revision was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)

    def devicesetting(self, **kwargs):
        """The device setting from which this configuration revision was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device setting from which this configuration revision was collected.
             :rtype : DeviceSetting

            """

        return self.api_request(self._get_method_fullname("devicesetting"), kwargs)

    def device(self, **kwargs):
        """The device from which this configuration revision was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this configuration revision was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def diffs(self, **kwargs):
        """Difference between two Config Revision.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Identifier of the config revision
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param previous_config_revision_id: Identifier of the previous config revision.
             :type previous_config_revision_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param include_intermediate_ind: Flag to indicate to check the intermediate config revision.
             :type include_intermediate_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` universal

             :param diff_format: Format should be either universal or normal.
             :type diff_format: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 3

             :param context_lines: Pass to the -C or -U cvs options.
             :type context_lines: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return text_config_revisions: Return the text files of the config revision using cvs diff command.
             :rtype text_config_revisions: Array

            """

        return self.api_request(self._get_method_fullname("diffs"), kwargs)

    def set_baseline(self, **kwargs):
        """Set a revision

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param devID: Device ID
             :type devID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param revID: Revision ID
             :type revID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("set_baseline"), kwargs)

    def clear_baseline(self, **kwargs):
        """Clear the revision.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param devID: Device ID
             :type devID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("clear_baseline"), kwargs)

    def get_configs(self, **kwargs):
        """Request on demand configuration collection for the specified device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param TrackingID: The Tracking ID. Used for internal purposes and ignored if user specified.
             :type TrackingID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return TrackingID: The TrackingID assigned to this get configs request.
             :rtype TrackingID: Integer

            """

        return self.api_request(self._get_method_fullname("get_configs"), kwargs)

    def get_configs_status(self, **kwargs):
        """Get the status of an on demand configuration collection request.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param TrackingID: The TrackingID assigned to the get configs request.
             :type TrackingID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Status: The current status of the get configs request.
             :rtype Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return Timestamp: The timestamp of the last status change.
             :rtype Timestamp: DateTime

            """

        return self.api_request(self._get_method_fullname("get_configs_status"), kwargs)
