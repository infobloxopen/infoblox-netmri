from ..broker import Broker


class IprgBroker(Broker):
    controller = "iprgs"

    def show(self, **kwargs):
        """Shows the details for the specified iprg.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg methods. The listed methods will be called on each iprg returned and included in the output. Available methods are: active_member, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_member, data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return iprg: The iprg identified by the specified IprgID.
             :rtype iprg: Iprg

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available iprgs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The HSRP or VRRP group number.
             :type IprgNumber: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The HSRP or VRRP group number.
             :type IprgNumber: Array of Integer

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

             :param timestamp: The data returned will represent the iprgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg methods. The listed methods will be called on each iprg returned and included in the output. Available methods are: active_member, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_member, data_source.
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
            |  ``default:`` IprgID

             :param sort: The data field(s) to use for sorting the output. Default is IprgID. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged.
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

             :param select: The list of attributes to return for each Iprg. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged. If empty or omitted, all attributes will be returned.
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

             :return iprgs: An array of the Iprg objects that match the specified input criteria.
             :rtype iprgs: Array of Iprg

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available iprgs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ActiveIprgMemberID: The internal NetMRI identifier for the HSRP/VRRP group membership details of the active router.
             :type ActiveIprgMemberID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ActiveIprgMemberID: The internal NetMRI identifier for the HSRP/VRRP group membership details of the active router.
             :type ActiveIprgMemberID: Array of Integer

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

             :param IprgActiveLastChanged: The date and time of the last change of the active or master router for this group.
             :type IprgActiveLastChanged: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgActiveLastChanged: The date and time of the last change of the active or master router for this group.
             :type IprgActiveLastChanged: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgAuth: The authentication method for this HSRP or VRRP group.
             :type IprgAuth: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgAuth: The authentication method for this HSRP or VRRP group.
             :type IprgAuth: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IprgChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type IprgChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IprgEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgEndTime: The ending effective time of this revision of this record, or empty if still in effect.
             :type IprgEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPDotted: The virtual IP address for this HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
             :type IprgIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPDotted: The virtual IP address for this HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
             :type IprgIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgIPNumeric: The numerical value of the HSRP/VRRP virtual IP address.
             :type IprgIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMAC: The virtual MAC for this HSRP or VRRP group.
             :type IprgMAC: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgMAC: The virtual MAC for this HSRP or VRRP group.
             :type IprgMAC: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The HSRP or VRRP group number.
             :type IprgNumber: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgNumber: The HSRP or VRRP group number.
             :type IprgNumber: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgStartTime: The starting effective time of this revision of the record.
             :type IprgStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgStartTime: The starting effective time of this revision of the record.
             :type IprgStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgTimestamp: The date and time this record was collected or calculated.
             :type IprgTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgTimestamp: The date and time this record was collected or calculated.
             :type IprgTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IprgType: Designates if this is an HSRP group or a VRRP group.
             :type IprgType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IprgType: Designates if this is an HSRP group or a VRRP group.
             :type IprgType: Array of String

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

             :param timestamp: The data returned will represent the iprgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg methods. The listed methods will be called on each iprg returned and included in the output. Available methods are: active_member, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_member, data_source.
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
            |  ``default:`` IprgID

             :param sort: The data field(s) to use for sorting the output. Default is IprgID. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged.
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

             :param select: The list of attributes to return for each Iprg. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against iprgs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: ActiveIprgMemberID, DataSourceID, IprgActiveLastChanged, IprgAuth, IprgChangedCols, IprgEndTime, IprgID, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgNumber, IprgStartTime, IprgTimestamp, IprgType.
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

             :return iprgs: An array of the Iprg objects that match the specified input criteria.
             :rtype iprgs: Array of Iprg

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available iprgs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: ActiveIprgMemberID, DataSourceID, IprgActiveLastChanged, IprgAuth, IprgChangedCols, IprgEndTime, IprgID, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgNumber, IprgStartTime, IprgTimestamp, IprgType.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ActiveIprgMemberID: The operator to apply to the field ActiveIprgMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ActiveIprgMemberID: The internal NetMRI identifier for the HSRP/VRRP group membership details of the active router. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ActiveIprgMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ActiveIprgMemberID: If op_ActiveIprgMemberID is specified, the field named in this input will be compared to the value in ActiveIprgMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ActiveIprgMemberID must be specified if op_ActiveIprgMemberID is specified.
             :type val_f_ActiveIprgMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ActiveIprgMemberID: If op_ActiveIprgMemberID is specified, this value will be compared to the value in ActiveIprgMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ActiveIprgMemberID must be specified if op_ActiveIprgMemberID is specified.
             :type val_c_ActiveIprgMemberID: String

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

             :param op_IprgActiveLastChanged: The operator to apply to the field IprgActiveLastChanged. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgActiveLastChanged: The date and time of the last change of the active or master router for this group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgActiveLastChanged: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgActiveLastChanged: If op_IprgActiveLastChanged is specified, the field named in this input will be compared to the value in IprgActiveLastChanged using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgActiveLastChanged must be specified if op_IprgActiveLastChanged is specified.
             :type val_f_IprgActiveLastChanged: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgActiveLastChanged: If op_IprgActiveLastChanged is specified, this value will be compared to the value in IprgActiveLastChanged using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgActiveLastChanged must be specified if op_IprgActiveLastChanged is specified.
             :type val_c_IprgActiveLastChanged: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgAuth: The operator to apply to the field IprgAuth. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgAuth: The authentication method for this HSRP or VRRP group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgAuth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgAuth: If op_IprgAuth is specified, the field named in this input will be compared to the value in IprgAuth using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgAuth must be specified if op_IprgAuth is specified.
             :type val_f_IprgAuth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgAuth: If op_IprgAuth is specified, this value will be compared to the value in IprgAuth using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgAuth must be specified if op_IprgAuth is specified.
             :type val_c_IprgAuth: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgChangedCols: The operator to apply to the field IprgChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgChangedCols: If op_IprgChangedCols is specified, the field named in this input will be compared to the value in IprgChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgChangedCols must be specified if op_IprgChangedCols is specified.
             :type val_f_IprgChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgChangedCols: If op_IprgChangedCols is specified, this value will be compared to the value in IprgChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgChangedCols must be specified if op_IprgChangedCols is specified.
             :type val_c_IprgChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgEndTime: The operator to apply to the field IprgEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgEndTime: The ending effective time of this revision of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgEndTime: If op_IprgEndTime is specified, the field named in this input will be compared to the value in IprgEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgEndTime must be specified if op_IprgEndTime is specified.
             :type val_f_IprgEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgEndTime: If op_IprgEndTime is specified, this value will be compared to the value in IprgEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgEndTime must be specified if op_IprgEndTime is specified.
             :type val_c_IprgEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgID: The operator to apply to the field IprgID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgID: The internal NetMRI identifier for this HSRP/VRRP Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgID: If op_IprgID is specified, the field named in this input will be compared to the value in IprgID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgID must be specified if op_IprgID is specified.
             :type val_f_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgID: If op_IprgID is specified, this value will be compared to the value in IprgID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgID must be specified if op_IprgID is specified.
             :type val_c_IprgID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgIPDotted: The operator to apply to the field IprgIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgIPDotted: The virtual IP address for this HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgIPDotted: If op_IprgIPDotted is specified, the field named in this input will be compared to the value in IprgIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgIPDotted must be specified if op_IprgIPDotted is specified.
             :type val_f_IprgIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgIPDotted: If op_IprgIPDotted is specified, this value will be compared to the value in IprgIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgIPDotted must be specified if op_IprgIPDotted is specified.
             :type val_c_IprgIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgIPNumeric: The operator to apply to the field IprgIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgIPNumeric: The numerical value of the HSRP/VRRP virtual IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgIPNumeric: If op_IprgIPNumeric is specified, the field named in this input will be compared to the value in IprgIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgIPNumeric must be specified if op_IprgIPNumeric is specified.
             :type val_f_IprgIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgIPNumeric: If op_IprgIPNumeric is specified, this value will be compared to the value in IprgIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgIPNumeric must be specified if op_IprgIPNumeric is specified.
             :type val_c_IprgIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgMAC: The operator to apply to the field IprgMAC. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgMAC: The virtual MAC for this HSRP or VRRP group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgMAC: If op_IprgMAC is specified, the field named in this input will be compared to the value in IprgMAC using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgMAC must be specified if op_IprgMAC is specified.
             :type val_f_IprgMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgMAC: If op_IprgMAC is specified, this value will be compared to the value in IprgMAC using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgMAC must be specified if op_IprgMAC is specified.
             :type val_c_IprgMAC: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgNumber: The operator to apply to the field IprgNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgNumber: The HSRP or VRRP group number. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgNumber: If op_IprgNumber is specified, the field named in this input will be compared to the value in IprgNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgNumber must be specified if op_IprgNumber is specified.
             :type val_f_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgNumber: If op_IprgNumber is specified, this value will be compared to the value in IprgNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgNumber must be specified if op_IprgNumber is specified.
             :type val_c_IprgNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgStartTime: The operator to apply to the field IprgStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgStartTime: The starting effective time of this revision of the record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgStartTime: If op_IprgStartTime is specified, the field named in this input will be compared to the value in IprgStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgStartTime must be specified if op_IprgStartTime is specified.
             :type val_f_IprgStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgStartTime: If op_IprgStartTime is specified, this value will be compared to the value in IprgStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgStartTime must be specified if op_IprgStartTime is specified.
             :type val_c_IprgStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgTimestamp: The operator to apply to the field IprgTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgTimestamp: If op_IprgTimestamp is specified, the field named in this input will be compared to the value in IprgTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgTimestamp must be specified if op_IprgTimestamp is specified.
             :type val_f_IprgTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgTimestamp: If op_IprgTimestamp is specified, this value will be compared to the value in IprgTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgTimestamp must be specified if op_IprgTimestamp is specified.
             :type val_c_IprgTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IprgType: The operator to apply to the field IprgType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IprgType: Designates if this is an HSRP group or a VRRP group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IprgType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IprgType: If op_IprgType is specified, the field named in this input will be compared to the value in IprgType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IprgType must be specified if op_IprgType is specified.
             :type val_f_IprgType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IprgType: If op_IprgType is specified, this value will be compared to the value in IprgType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IprgType must be specified if op_IprgType is specified.
             :type val_c_IprgType: String

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

             :param timestamp: The data returned will represent the iprgs as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of iprg methods. The listed methods will be called on each iprg returned and included in the output. Available methods are: active_member, data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: active_member, data_source.
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
            |  ``default:`` IprgID

             :param sort: The data field(s) to use for sorting the output. Default is IprgID. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged.
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

             :param select: The list of attributes to return for each Iprg. Valid values are IprgID, DataSourceID, IprgStartTime, IprgEndTime, IprgTimestamp, IprgChangedCols, ActiveIprgMemberID, IprgNumber, IprgIPDotted, IprgIPNumeric, IprgMAC, IprgAuth, IprgType, IprgActiveLastChanged. If empty or omitted, all attributes will be returned.
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

             :return iprgs: An array of the Iprg objects that match the specified input criteria.
             :rtype iprgs: Array of Iprg

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)

    def active_member(self, **kwargs):
        """The HSRP/VRRP group membership details of the active router.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IprgID: The internal NetMRI identifier for this HSRP/VRRP Group.
             :type IprgID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The HSRP/VRRP group membership details of the active router.
             :rtype : IprgMember

            """

        return self.api_request(self._get_method_fullname("active_member"), kwargs)
