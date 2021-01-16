from ..broker import Broker


class AccessChangeAccountingBroker(Broker):
    controller = "access_change_accountings"

    def show(self, **kwargs):
        """Shows the details for the specified access change accounting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param AccessChangeAccountingID: The internal NetMRI identifier for this access accounting element.
             :type AccessChangeAccountingID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return access_change_accounting: The access change accounting identified by the specified AccessChangeAccountingID.
             :rtype access_change_accounting: AccessChangeAccounting

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available access change accountings. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessChangeAccountingID: The internal NetMRI identifier for this access accounting element.
             :type AccessChangeAccountingID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device for which we count the access statistics.
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

             :param timestamp: The data returned will represent the access change accountings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` AccessChangeAccountingID

             :param sort: The data field(s) to use for sorting the output. Default is AccessChangeAccountingID. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols.
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

             :param select: The list of attributes to return for each AccessChangeAccounting. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols. If empty or omitted, all attributes will be returned.
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

             :return access_change_accountings: An array of the AccessChangeAccounting objects that match the specified input criteria.
             :rtype access_change_accountings: Array of AccessChangeAccounting

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available access change accountings matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ACAChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ACAChangedCols: Array of String

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ACAEndTime: The ending effective time of this record, or empty if still in effect.
             :type ACAEndTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ACAFirstSeenTime: The timestamp of when NetMRI recorded its first access statistic for this device.
             :type ACAFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ACAStartTime: The starting effective time of this record.
             :type ACAStartTime: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ACATimestamp: The date and time this record was collected or calculated.
             :type ACATimestamp: Array of DateTime

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param AccessChangeAccountingID: The internal NetMRI identifier for this access accounting element.
             :type AccessChangeAccountingID: Array of Integer

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

             :param DeviceID: The internal NetMRI identifier for the device for which we count the access statistics.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterAdded: The number of rules added by provisioning with NetMRI (including rollback operations).
             :type FilterAdded: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterAll: The number of all rules defined in the device's configuration.
             :type FilterAll: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterRemoved: The number of rules removed by provisioning with NetMRI (including remediation).
             :type FilterRemoved: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterSetAdded: The number of rule lists added by provisioning with NetMRI.
             :type FilterSetAdded: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterSetAll: The number of all rule lists defined in the device's configuration.
             :type FilterSetAll: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterSetRemoved: The number of rule lists removed by provisioning with NetMRI (including remediation).
             :type FilterSetRemoved: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterSetUnused: The number of unused rule lists defined in the device's configuration.
             :type FilterSetUnused: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FilterUnused: The number of unused rules defined in the device's configuration.
             :type FilterUnused: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPObjectAdded: The number of network objects added by provisioning with NetMRI.
             :type IPObjectAdded: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPObjectAll: The number of network objects defined in the device's configuration.
             :type IPObjectAll: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPObjectRemoved: The number of network objects removed by provisioning with NetMRI (including remediation).
             :type IPObjectRemoved: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IPObjectUnused: The number of network objects defined in the device's configuration that are not used in the configuration.
             :type IPObjectUnused: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ServiceAdded: The number of service objects added by provisioning with NetMRI.
             :type ServiceAdded: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ServiceAll: The number of service objects defined in the device's configuration.
             :type ServiceAll: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ServiceRemoved: The number of service objects removed by provisioning with NetMRI (including remediation).
             :type ServiceRemoved: Array of Integer

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ServiceUnused: The number of service objects defined in the device's configuration that are not used in the configuration.
             :type ServiceUnused: Array of Integer

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

             :param timestamp: The data returned will represent the access change accountings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` AccessChangeAccountingID

             :param sort: The data field(s) to use for sorting the output. Default is AccessChangeAccountingID. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols.
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

             :param select: The list of attributes to return for each AccessChangeAccounting. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against access change accountings, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ACAChangedCols, ACAEndTime, ACAFirstSeenTime, ACAStartTime, ACATimestamp, AccessChangeAccountingID, DataSourceID, DeviceID, FilterAdded, FilterAll, FilterRemoved, FilterSetAdded, FilterSetAll, FilterSetRemoved, FilterSetUnused, FilterUnused, IPObjectAdded, IPObjectAll, IPObjectRemoved, IPObjectUnused, ServiceAdded, ServiceAll, ServiceRemoved, ServiceUnused.
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

             :return access_change_accountings: An array of the AccessChangeAccounting objects that match the specified input criteria.
             :rtype access_change_accountings: Array of AccessChangeAccounting

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available access change accountings matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ACAChangedCols, ACAEndTime, ACAFirstSeenTime, ACAStartTime, ACATimestamp, AccessChangeAccountingID, DataSourceID, DeviceID, FilterAdded, FilterAll, FilterRemoved, FilterSetAdded, FilterSetAll, FilterSetRemoved, FilterSetUnused, FilterUnused, IPObjectAdded, IPObjectAll, IPObjectRemoved, IPObjectUnused, ServiceAdded, ServiceAll, ServiceRemoved, ServiceUnused.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ACAChangedCols: The operator to apply to the field ACAChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ACAChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ACAChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ACAChangedCols: If op_ACAChangedCols is specified, the field named in this input will be compared to the value in ACAChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ACAChangedCols must be specified if op_ACAChangedCols is specified.
             :type val_f_ACAChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ACAChangedCols: If op_ACAChangedCols is specified, this value will be compared to the value in ACAChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ACAChangedCols must be specified if op_ACAChangedCols is specified.
             :type val_c_ACAChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ACAEndTime: The operator to apply to the field ACAEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ACAEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ACAEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ACAEndTime: If op_ACAEndTime is specified, the field named in this input will be compared to the value in ACAEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ACAEndTime must be specified if op_ACAEndTime is specified.
             :type val_f_ACAEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ACAEndTime: If op_ACAEndTime is specified, this value will be compared to the value in ACAEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ACAEndTime must be specified if op_ACAEndTime is specified.
             :type val_c_ACAEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ACAFirstSeenTime: The operator to apply to the field ACAFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ACAFirstSeenTime: The timestamp of when NetMRI recorded its first access statistic for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ACAFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ACAFirstSeenTime: If op_ACAFirstSeenTime is specified, the field named in this input will be compared to the value in ACAFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ACAFirstSeenTime must be specified if op_ACAFirstSeenTime is specified.
             :type val_f_ACAFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ACAFirstSeenTime: If op_ACAFirstSeenTime is specified, this value will be compared to the value in ACAFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ACAFirstSeenTime must be specified if op_ACAFirstSeenTime is specified.
             :type val_c_ACAFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ACAStartTime: The operator to apply to the field ACAStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ACAStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ACAStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ACAStartTime: If op_ACAStartTime is specified, the field named in this input will be compared to the value in ACAStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ACAStartTime must be specified if op_ACAStartTime is specified.
             :type val_f_ACAStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ACAStartTime: If op_ACAStartTime is specified, this value will be compared to the value in ACAStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ACAStartTime must be specified if op_ACAStartTime is specified.
             :type val_c_ACAStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ACATimestamp: The operator to apply to the field ACATimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ACATimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ACATimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ACATimestamp: If op_ACATimestamp is specified, the field named in this input will be compared to the value in ACATimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ACATimestamp must be specified if op_ACATimestamp is specified.
             :type val_f_ACATimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ACATimestamp: If op_ACATimestamp is specified, this value will be compared to the value in ACATimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ACATimestamp must be specified if op_ACATimestamp is specified.
             :type val_c_ACATimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_AccessChangeAccountingID: The operator to apply to the field AccessChangeAccountingID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. AccessChangeAccountingID: The internal NetMRI identifier for this access accounting element. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_AccessChangeAccountingID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_AccessChangeAccountingID: If op_AccessChangeAccountingID is specified, the field named in this input will be compared to the value in AccessChangeAccountingID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_AccessChangeAccountingID must be specified if op_AccessChangeAccountingID is specified.
             :type val_f_AccessChangeAccountingID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_AccessChangeAccountingID: If op_AccessChangeAccountingID is specified, this value will be compared to the value in AccessChangeAccountingID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_AccessChangeAccountingID must be specified if op_AccessChangeAccountingID is specified.
             :type val_c_AccessChangeAccountingID: String

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device for which we count the access statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_FilterAdded: The operator to apply to the field FilterAdded. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterAdded: The number of rules added by provisioning with NetMRI (including rollback operations). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterAdded: If op_FilterAdded is specified, the field named in this input will be compared to the value in FilterAdded using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterAdded must be specified if op_FilterAdded is specified.
             :type val_f_FilterAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterAdded: If op_FilterAdded is specified, this value will be compared to the value in FilterAdded using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterAdded must be specified if op_FilterAdded is specified.
             :type val_c_FilterAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterAll: The operator to apply to the field FilterAll. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterAll: The number of all rules defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterAll: If op_FilterAll is specified, the field named in this input will be compared to the value in FilterAll using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterAll must be specified if op_FilterAll is specified.
             :type val_f_FilterAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterAll: If op_FilterAll is specified, this value will be compared to the value in FilterAll using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterAll must be specified if op_FilterAll is specified.
             :type val_c_FilterAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterRemoved: The operator to apply to the field FilterRemoved. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterRemoved: The number of rules removed by provisioning with NetMRI (including remediation). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterRemoved: If op_FilterRemoved is specified, the field named in this input will be compared to the value in FilterRemoved using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterRemoved must be specified if op_FilterRemoved is specified.
             :type val_f_FilterRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterRemoved: If op_FilterRemoved is specified, this value will be compared to the value in FilterRemoved using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterRemoved must be specified if op_FilterRemoved is specified.
             :type val_c_FilterRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterSetAdded: The operator to apply to the field FilterSetAdded. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterSetAdded: The number of rule lists added by provisioning with NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterSetAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterSetAdded: If op_FilterSetAdded is specified, the field named in this input will be compared to the value in FilterSetAdded using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterSetAdded must be specified if op_FilterSetAdded is specified.
             :type val_f_FilterSetAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterSetAdded: If op_FilterSetAdded is specified, this value will be compared to the value in FilterSetAdded using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterSetAdded must be specified if op_FilterSetAdded is specified.
             :type val_c_FilterSetAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterSetAll: The operator to apply to the field FilterSetAll. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterSetAll: The number of all rule lists defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterSetAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterSetAll: If op_FilterSetAll is specified, the field named in this input will be compared to the value in FilterSetAll using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterSetAll must be specified if op_FilterSetAll is specified.
             :type val_f_FilterSetAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterSetAll: If op_FilterSetAll is specified, this value will be compared to the value in FilterSetAll using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterSetAll must be specified if op_FilterSetAll is specified.
             :type val_c_FilterSetAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterSetRemoved: The operator to apply to the field FilterSetRemoved. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterSetRemoved: The number of rule lists removed by provisioning with NetMRI (including remediation). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterSetRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterSetRemoved: If op_FilterSetRemoved is specified, the field named in this input will be compared to the value in FilterSetRemoved using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterSetRemoved must be specified if op_FilterSetRemoved is specified.
             :type val_f_FilterSetRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterSetRemoved: If op_FilterSetRemoved is specified, this value will be compared to the value in FilterSetRemoved using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterSetRemoved must be specified if op_FilterSetRemoved is specified.
             :type val_c_FilterSetRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterSetUnused: The operator to apply to the field FilterSetUnused. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterSetUnused: The number of unused rule lists defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterSetUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterSetUnused: If op_FilterSetUnused is specified, the field named in this input will be compared to the value in FilterSetUnused using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterSetUnused must be specified if op_FilterSetUnused is specified.
             :type val_f_FilterSetUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterSetUnused: If op_FilterSetUnused is specified, this value will be compared to the value in FilterSetUnused using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterSetUnused must be specified if op_FilterSetUnused is specified.
             :type val_c_FilterSetUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FilterUnused: The operator to apply to the field FilterUnused. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FilterUnused: The number of unused rules defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FilterUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FilterUnused: If op_FilterUnused is specified, the field named in this input will be compared to the value in FilterUnused using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FilterUnused must be specified if op_FilterUnused is specified.
             :type val_f_FilterUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FilterUnused: If op_FilterUnused is specified, this value will be compared to the value in FilterUnused using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FilterUnused must be specified if op_FilterUnused is specified.
             :type val_c_FilterUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPObjectAdded: The operator to apply to the field IPObjectAdded. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPObjectAdded: The number of network objects added by provisioning with NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPObjectAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPObjectAdded: If op_IPObjectAdded is specified, the field named in this input will be compared to the value in IPObjectAdded using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPObjectAdded must be specified if op_IPObjectAdded is specified.
             :type val_f_IPObjectAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPObjectAdded: If op_IPObjectAdded is specified, this value will be compared to the value in IPObjectAdded using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPObjectAdded must be specified if op_IPObjectAdded is specified.
             :type val_c_IPObjectAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPObjectAll: The operator to apply to the field IPObjectAll. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPObjectAll: The number of network objects defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPObjectAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPObjectAll: If op_IPObjectAll is specified, the field named in this input will be compared to the value in IPObjectAll using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPObjectAll must be specified if op_IPObjectAll is specified.
             :type val_f_IPObjectAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPObjectAll: If op_IPObjectAll is specified, this value will be compared to the value in IPObjectAll using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPObjectAll must be specified if op_IPObjectAll is specified.
             :type val_c_IPObjectAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPObjectRemoved: The operator to apply to the field IPObjectRemoved. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPObjectRemoved: The number of network objects removed by provisioning with NetMRI (including remediation). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPObjectRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPObjectRemoved: If op_IPObjectRemoved is specified, the field named in this input will be compared to the value in IPObjectRemoved using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPObjectRemoved must be specified if op_IPObjectRemoved is specified.
             :type val_f_IPObjectRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPObjectRemoved: If op_IPObjectRemoved is specified, this value will be compared to the value in IPObjectRemoved using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPObjectRemoved must be specified if op_IPObjectRemoved is specified.
             :type val_c_IPObjectRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IPObjectUnused: The operator to apply to the field IPObjectUnused. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IPObjectUnused: The number of network objects defined in the device's configuration that are not used in the configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IPObjectUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IPObjectUnused: If op_IPObjectUnused is specified, the field named in this input will be compared to the value in IPObjectUnused using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IPObjectUnused must be specified if op_IPObjectUnused is specified.
             :type val_f_IPObjectUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IPObjectUnused: If op_IPObjectUnused is specified, this value will be compared to the value in IPObjectUnused using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IPObjectUnused must be specified if op_IPObjectUnused is specified.
             :type val_c_IPObjectUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ServiceAdded: The operator to apply to the field ServiceAdded. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ServiceAdded: The number of service objects added by provisioning with NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ServiceAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ServiceAdded: If op_ServiceAdded is specified, the field named in this input will be compared to the value in ServiceAdded using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ServiceAdded must be specified if op_ServiceAdded is specified.
             :type val_f_ServiceAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ServiceAdded: If op_ServiceAdded is specified, this value will be compared to the value in ServiceAdded using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ServiceAdded must be specified if op_ServiceAdded is specified.
             :type val_c_ServiceAdded: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ServiceAll: The operator to apply to the field ServiceAll. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ServiceAll: The number of service objects defined in the device's configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ServiceAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ServiceAll: If op_ServiceAll is specified, the field named in this input will be compared to the value in ServiceAll using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ServiceAll must be specified if op_ServiceAll is specified.
             :type val_f_ServiceAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ServiceAll: If op_ServiceAll is specified, this value will be compared to the value in ServiceAll using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ServiceAll must be specified if op_ServiceAll is specified.
             :type val_c_ServiceAll: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ServiceRemoved: The operator to apply to the field ServiceRemoved. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ServiceRemoved: The number of service objects removed by provisioning with NetMRI (including remediation). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ServiceRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ServiceRemoved: If op_ServiceRemoved is specified, the field named in this input will be compared to the value in ServiceRemoved using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ServiceRemoved must be specified if op_ServiceRemoved is specified.
             :type val_f_ServiceRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ServiceRemoved: If op_ServiceRemoved is specified, this value will be compared to the value in ServiceRemoved using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ServiceRemoved must be specified if op_ServiceRemoved is specified.
             :type val_c_ServiceRemoved: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ServiceUnused: The operator to apply to the field ServiceUnused. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ServiceUnused: The number of service objects defined in the device's configuration that are not used in the configuration. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ServiceUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ServiceUnused: If op_ServiceUnused is specified, the field named in this input will be compared to the value in ServiceUnused using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ServiceUnused must be specified if op_ServiceUnused is specified.
             :type val_f_ServiceUnused: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ServiceUnused: If op_ServiceUnused is specified, this value will be compared to the value in ServiceUnused using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ServiceUnused must be specified if op_ServiceUnused is specified.
             :type val_c_ServiceUnused: String

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

             :param timestamp: The data returned will represent the access change accountings as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

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
            |  ``default:`` AccessChangeAccountingID

             :param sort: The data field(s) to use for sorting the output. Default is AccessChangeAccountingID. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols.
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

             :param select: The list of attributes to return for each AccessChangeAccounting. Valid values are AccessChangeAccountingID, DataSourceID, DeviceID, FilterSetAll, FilterSetUnused, FilterSetAdded, FilterSetRemoved, FilterAll, FilterUnused, FilterAdded, FilterRemoved, IPObjectAll, IPObjectUnused, IPObjectAdded, IPObjectRemoved, ServiceAll, ServiceUnused, ServiceAdded, ServiceRemoved, ACAFirstSeenTime, ACAStartTime, ACAEndTime, ACATimestamp, ACAChangedCols. If empty or omitted, all attributes will be returned.
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

             :return access_change_accountings: An array of the AccessChangeAccounting objects that match the specified input criteria.
             :rtype access_change_accountings: Array of AccessChangeAccounting

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def summary(self, **kwargs):
        """Returns a summary of accounting.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param starttime: time of starting period for summary computations
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: time of ending period for summary computations
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_set_ids: IDs of the group we want the summary for
             :type device_group_set_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: IDs of the group we want the summary for
             :type device_ids: Array of Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return values: a hash containing summary-names and their numeric values.
             :rtype values: Hash

            """

        return self.api_request(self._get_method_fullname("summary"), kwargs)
