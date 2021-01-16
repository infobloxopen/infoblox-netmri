from ..broker import Broker


class IssueListBroker(Broker):
    controller = "issue_lists"

    def show(self, **kwargs):
        """Shows the details for the specified issue list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue list methods. The listed methods will be called on each issue list returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return issue_list: The issue list identified by the specified GroupSetID.
             :rtype issue_list: IssueList

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available issue lists. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the issue lists with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the issue lists with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue list methods. The listed methods will be called on each issue list returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupSetID

             :param sort: The data field(s) to use for sorting the output. Default is GroupSetID. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID.
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

             :param select: The list of attributes to return for each IssueList. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID. If empty or omitted, all attributes will be returned.
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

             :return issue_lists: An array of the IssueList objects that match the specified input criteria.
             :rtype issue_lists: Array of IssueList

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available issue lists matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Adds: Added a new type of issue in the list.
             :type Adds: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Adds: Added a new type of issue in the list.
             :type Adds: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Device,Configuration,VLANs,etc.)
             :type Component: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Device,Configuration,VLANs,etc.)
             :type Component: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this device.
             :type Correctness: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this device.
             :type Correctness: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Count: The total number of issues captured within NetMRI.
             :type Count: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Count: The total number of issues captured within NetMRI.
             :type Count: Array of Integer

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

             :param Deletes: Remove a issue from the list.
             :type Deletes: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Deletes: Remove a issue from the list.
             :type Deletes: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DimDate: The dimensional date and time was found.
             :type DimDate: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DimDate: The dimensional date and time was found.
             :type DimDate: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param EndTime: The date and time the record was last modified in NetMRI.
             :type EndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param FirstSeen: The timestamp of when NetMRI first discovered this NetMRI.
             :type FirstSeen: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param FirstSeen: The timestamp of when NetMRI first discovered this NetMRI.
             :type FirstSeen: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTimestamp: The date and time of Issues was collected or calculated.
             :type IssueTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTimestamp: The date and time of Issues was collected or calculated.
             :type IssueTimestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier of the Issue Type.
             :type IssueTypeID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier of the Issue Type.
             :type IssueTypeID: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param PriorityID: Not currently used.
             :type PriorityID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param PriorityID: Not currently used.
             :type PriorityID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Same: Maintain the issues as in the list.
             :type Same: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Same: Maintain the issues as in the list.
             :type Same: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityID: The issue severity ID (1 = Error , 2 = Warning ,3 = Info).Useful for sorting.
             :type SeverityID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityID: The issue severity ID (1 = Error , 2 = Warning ,3 = Info).Useful for sorting.
             :type SeverityID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityName: The severity name in the issue list.
             :type SeverityName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityName: The severity name in the issue list.
             :type SeverityName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ShortDate: The short date and time defined in the device statistics.
             :type ShortDate: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ShortDate: The short date and time defined in the device statistics.
             :type ShortDate: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this device.
             :type Stability: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this device.
             :type Stability: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Status: Status of the issue.
             :type Status: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Status: Status of the issue.
             :type Status: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Suppressed: A flag indicates whether a issue is suppressed or not.
             :type Suppressed: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Suppressed: A flag indicates whether a issue is suppressed or not.
             :type Suppressed: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timestamp: The date and time this record was collected or calculated.
             :type Timestamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Title: The descriptive name of the issue.
             :type Title: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Title: The descriptive name of the issue.
             :type Title: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param TotalCount: The total number of issues in the list.
             :type TotalCount: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param TotalCount: The total number of issues in the list.
             :type TotalCount: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnixDimDate: The unique dimensional date and time od device statistics.
             :type UnixDimDate: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnixDimDate: The unique dimensional date and time od device statistics.
             :type UnixDimDate: Array of DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the issue lists with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the issue lists with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue list methods. The listed methods will be called on each issue list returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupSetID

             :param sort: The data field(s) to use for sorting the output. Default is GroupSetID. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID.
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

             :param select: The list of attributes to return for each IssueList. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against issue lists, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: Adds, Component, Correctness, Count, DataSourceID, Deletes, DimDate, EndTime, FirstSeen, GroupSetID, IssueTimestamp, IssueTypeID, PriorityID, Same, SeverityID, SeverityName, ShortDate, Stability, Status, Suppressed, Timestamp, Title, TotalCount, UnixDimDate.
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

             :return issue_lists: An array of the IssueList objects that match the specified input criteria.
             :rtype issue_lists: Array of IssueList

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available issue lists matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: Adds, Component, Correctness, Count, DataSourceID, Deletes, DimDate, EndTime, FirstSeen, GroupSetID, IssueTimestamp, IssueTypeID, PriorityID, Same, SeverityID, SeverityName, ShortDate, Stability, Status, Suppressed, Timestamp, Title, TotalCount, UnixDimDate.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Adds: The operator to apply to the field Adds. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Adds: Added a new type of issue in the list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Adds: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Adds: If op_Adds is specified, the field named in this input will be compared to the value in Adds using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Adds must be specified if op_Adds is specified.
             :type val_f_Adds: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Adds: If op_Adds is specified, this value will be compared to the value in Adds using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Adds must be specified if op_Adds is specified.
             :type val_c_Adds: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Component: The operator to apply to the field Component. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Component: The issue component (Device,Configuration,VLANs,etc.) For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Component: If op_Component is specified, the field named in this input will be compared to the value in Component using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Component must be specified if op_Component is specified.
             :type val_f_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Component: If op_Component is specified, this value will be compared to the value in Component using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Component must be specified if op_Component is specified.
             :type val_c_Component: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Correctness: The operator to apply to the field Correctness. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Correctness: The correctness contribution for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Correctness: If op_Correctness is specified, the field named in this input will be compared to the value in Correctness using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Correctness must be specified if op_Correctness is specified.
             :type val_f_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Correctness: If op_Correctness is specified, this value will be compared to the value in Correctness using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Correctness must be specified if op_Correctness is specified.
             :type val_c_Correctness: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Count: The operator to apply to the field Count. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Count: The total number of issues captured within NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Count: If op_Count is specified, the field named in this input will be compared to the value in Count using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Count must be specified if op_Count is specified.
             :type val_f_Count: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Count: If op_Count is specified, this value will be compared to the value in Count using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Count must be specified if op_Count is specified.
             :type val_c_Count: String

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

             :param op_Deletes: The operator to apply to the field Deletes. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Deletes: Remove a issue from the list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Deletes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Deletes: If op_Deletes is specified, the field named in this input will be compared to the value in Deletes using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Deletes must be specified if op_Deletes is specified.
             :type val_f_Deletes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Deletes: If op_Deletes is specified, this value will be compared to the value in Deletes using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Deletes must be specified if op_Deletes is specified.
             :type val_c_Deletes: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DimDate: The operator to apply to the field DimDate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DimDate: The dimensional date and time was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DimDate: If op_DimDate is specified, the field named in this input will be compared to the value in DimDate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DimDate must be specified if op_DimDate is specified.
             :type val_f_DimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DimDate: If op_DimDate is specified, this value will be compared to the value in DimDate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DimDate must be specified if op_DimDate is specified.
             :type val_c_DimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_EndTime: The operator to apply to the field EndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. EndTime: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_EndTime: If op_EndTime is specified, the field named in this input will be compared to the value in EndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_EndTime must be specified if op_EndTime is specified.
             :type val_f_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_EndTime: If op_EndTime is specified, this value will be compared to the value in EndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_EndTime must be specified if op_EndTime is specified.
             :type val_c_EndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_FirstSeen: The operator to apply to the field FirstSeen. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. FirstSeen: The timestamp of when NetMRI first discovered this NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_FirstSeen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_FirstSeen: If op_FirstSeen is specified, the field named in this input will be compared to the value in FirstSeen using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_FirstSeen must be specified if op_FirstSeen is specified.
             :type val_f_FirstSeen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_FirstSeen: If op_FirstSeen is specified, this value will be compared to the value in FirstSeen using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_FirstSeen must be specified if op_FirstSeen is specified.
             :type val_c_FirstSeen: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GroupSetID: The operator to apply to the field GroupSetID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GroupSetID: The internal NetMRI identifier of the Group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GroupSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GroupSetID: If op_GroupSetID is specified, the field named in this input will be compared to the value in GroupSetID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GroupSetID must be specified if op_GroupSetID is specified.
             :type val_f_GroupSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GroupSetID: If op_GroupSetID is specified, this value will be compared to the value in GroupSetID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GroupSetID must be specified if op_GroupSetID is specified.
             :type val_c_GroupSetID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IssueTimestamp: The operator to apply to the field IssueTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IssueTimestamp: The date and time of Issues was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IssueTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IssueTimestamp: If op_IssueTimestamp is specified, the field named in this input will be compared to the value in IssueTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IssueTimestamp must be specified if op_IssueTimestamp is specified.
             :type val_f_IssueTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IssueTimestamp: If op_IssueTimestamp is specified, this value will be compared to the value in IssueTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IssueTimestamp must be specified if op_IssueTimestamp is specified.
             :type val_c_IssueTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IssueTypeID: The operator to apply to the field IssueTypeID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IssueTypeID: The internal NetMRI identifier of the Issue Type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IssueTypeID: If op_IssueTypeID is specified, the field named in this input will be compared to the value in IssueTypeID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IssueTypeID must be specified if op_IssueTypeID is specified.
             :type val_f_IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IssueTypeID: If op_IssueTypeID is specified, this value will be compared to the value in IssueTypeID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IssueTypeID must be specified if op_IssueTypeID is specified.
             :type val_c_IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_PriorityID: The operator to apply to the field PriorityID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. PriorityID: Not currently used. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_PriorityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_PriorityID: If op_PriorityID is specified, the field named in this input will be compared to the value in PriorityID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_PriorityID must be specified if op_PriorityID is specified.
             :type val_f_PriorityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_PriorityID: If op_PriorityID is specified, this value will be compared to the value in PriorityID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_PriorityID must be specified if op_PriorityID is specified.
             :type val_c_PriorityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Same: The operator to apply to the field Same. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Same: Maintain the issues as in the list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Same: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Same: If op_Same is specified, the field named in this input will be compared to the value in Same using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Same must be specified if op_Same is specified.
             :type val_f_Same: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Same: If op_Same is specified, this value will be compared to the value in Same using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Same must be specified if op_Same is specified.
             :type val_c_Same: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SeverityID: The operator to apply to the field SeverityID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SeverityID: The issue severity ID (1 = Error , 2 = Warning ,3 = Info).Useful for sorting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SeverityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SeverityID: If op_SeverityID is specified, the field named in this input will be compared to the value in SeverityID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SeverityID must be specified if op_SeverityID is specified.
             :type val_f_SeverityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SeverityID: If op_SeverityID is specified, this value will be compared to the value in SeverityID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SeverityID must be specified if op_SeverityID is specified.
             :type val_c_SeverityID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SeverityName: The operator to apply to the field SeverityName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SeverityName: The severity name in the issue list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SeverityName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SeverityName: If op_SeverityName is specified, the field named in this input will be compared to the value in SeverityName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SeverityName must be specified if op_SeverityName is specified.
             :type val_f_SeverityName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SeverityName: If op_SeverityName is specified, this value will be compared to the value in SeverityName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SeverityName must be specified if op_SeverityName is specified.
             :type val_c_SeverityName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ShortDate: The operator to apply to the field ShortDate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ShortDate: The short date and time defined in the device statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ShortDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ShortDate: If op_ShortDate is specified, the field named in this input will be compared to the value in ShortDate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ShortDate must be specified if op_ShortDate is specified.
             :type val_f_ShortDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ShortDate: If op_ShortDate is specified, this value will be compared to the value in ShortDate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ShortDate must be specified if op_ShortDate is specified.
             :type val_c_ShortDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Stability: The operator to apply to the field Stability. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Stability: The stability contribution for this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Stability: If op_Stability is specified, the field named in this input will be compared to the value in Stability using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Stability must be specified if op_Stability is specified.
             :type val_f_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Stability: If op_Stability is specified, this value will be compared to the value in Stability using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Stability must be specified if op_Stability is specified.
             :type val_c_Stability: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Status: The operator to apply to the field Status. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Status: Status of the issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Status: If op_Status is specified, the field named in this input will be compared to the value in Status using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Status must be specified if op_Status is specified.
             :type val_f_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Status: If op_Status is specified, this value will be compared to the value in Status using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Status must be specified if op_Status is specified.
             :type val_c_Status: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Suppressed: The operator to apply to the field Suppressed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Suppressed: A flag indicates whether a issue is suppressed or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Suppressed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Suppressed: If op_Suppressed is specified, the field named in this input will be compared to the value in Suppressed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Suppressed must be specified if op_Suppressed is specified.
             :type val_f_Suppressed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Suppressed: If op_Suppressed is specified, this value will be compared to the value in Suppressed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Suppressed must be specified if op_Suppressed is specified.
             :type val_c_Suppressed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Timestamp: The operator to apply to the field Timestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Timestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Timestamp: If op_Timestamp is specified, the field named in this input will be compared to the value in Timestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Timestamp must be specified if op_Timestamp is specified.
             :type val_f_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Timestamp: If op_Timestamp is specified, this value will be compared to the value in Timestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Timestamp must be specified if op_Timestamp is specified.
             :type val_c_Timestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Title: The operator to apply to the field Title. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Title: The descriptive name of the issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Title: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Title: If op_Title is specified, the field named in this input will be compared to the value in Title using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Title must be specified if op_Title is specified.
             :type val_f_Title: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Title: If op_Title is specified, this value will be compared to the value in Title using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Title must be specified if op_Title is specified.
             :type val_c_Title: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_TotalCount: The operator to apply to the field TotalCount. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. TotalCount: The total number of issues in the list. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_TotalCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_TotalCount: If op_TotalCount is specified, the field named in this input will be compared to the value in TotalCount using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_TotalCount must be specified if op_TotalCount is specified.
             :type val_f_TotalCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_TotalCount: If op_TotalCount is specified, this value will be compared to the value in TotalCount using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_TotalCount must be specified if op_TotalCount is specified.
             :type val_c_TotalCount: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_UnixDimDate: The operator to apply to the field UnixDimDate. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. UnixDimDate: The unique dimensional date and time od device statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_UnixDimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_UnixDimDate: If op_UnixDimDate is specified, the field named in this input will be compared to the value in UnixDimDate using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_UnixDimDate must be specified if op_UnixDimDate is specified.
             :type val_f_UnixDimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_UnixDimDate: If op_UnixDimDate is specified, this value will be compared to the value in UnixDimDate using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_UnixDimDate must be specified if op_UnixDimDate is specified.
             :type val_c_UnixDimDate: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the issue lists with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the issue lists with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue list methods. The listed methods will be called on each issue list returned and included in the output. Available methods are: data_source.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source.
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
            |  ``default:`` GroupSetID

             :param sort: The data field(s) to use for sorting the output. Default is GroupSetID. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID.
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

             :param select: The list of attributes to return for each IssueList. Valid values are IssueTimestamp, GroupSetID, IssueTypeID, DataSourceID, Count, Adds, Deletes, Same, Suppressed, FirstSeen, Timestamp, EndTime, TotalCount, DimDate, ShortDate, UnixDimDate, Component, SeverityID, SeverityName, Correctness, Stability, Status, Title, PriorityID. If empty or omitted, all attributes will be returned.
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

             :return issue_lists: An array of the IssueList objects that match the specified input criteria.
             :rtype issue_lists: Array of IssueList

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GroupSetID: The internal NetMRI identifier of the Group.
             :type GroupSetID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The collector NetMRI that collected this data record.
             :rtype : DataSource

            """

        return self.api_request(self._get_method_fullname("data_source"), kwargs)
