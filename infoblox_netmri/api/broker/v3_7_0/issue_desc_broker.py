from ..broker import Broker


class IssueDescBroker(Broker):
    controller = "issue_descs"

    def show(self, **kwargs):
        """Shows the details for the specified issue desc.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IssueDescID: The internal NetMRI identifier for this issue description.
             :type IssueDescID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue desc methods. The listed methods will be called on each issue desc returned and included in the output. Available methods are: meta, severity.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return issue_desc: The issue desc identified by the specified IssueDescID.
             :rtype issue_desc: IssueDesc

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available issue descs. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for this type of issue.
             :type IssueTypeID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for this type of issue.
             :type IssueTypeID: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue desc methods. The listed methods will be called on each issue desc returned and included in the output. Available methods are: meta, severity.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
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
            |  ``default:`` IssueDescID

             :param sort: The data field(s) to use for sorting the output. Default is IssueDescID. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID.
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

             :param select: The list of attributes to return for each IssueDesc. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID. If empty or omitted, all attributes will be returned.
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

             :return issue_descs: An array of the IssueDesc objects that match the specified input criteria.
             :rtype issue_descs: Array of IssueDesc

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available issue descs matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Component: The issue component (Devices, Configuration, VLANs, etc.).
             :type Component: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Context: For internal use only.
             :type Context: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Context: For internal use only.
             :type Context: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this issue.
             :type Correctness: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Correctness: The correctness contribution for this issue.
             :type Correctness: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Description: A detailed description of the issue.
             :type Description: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Description: A detailed description of the issue.
             :type Description: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Frequency: The time in seconds of how often the analysis engine checks for issues of this type.
             :type Frequency: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Frequency: The time in seconds of how often the analysis engine checks for issues of this type.
             :type Frequency: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueDescID: The internal NetMRI identifier for this issue description.
             :type IssueDescID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueDescID: The internal NetMRI identifier for this issue description.
             :type IssueDescID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueType: The source of the issue (S = built into system, C = custom issue, P = policy violation issue, E = event analysis issue).
             :type IssueType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueType: The source of the issue (S = built into system, C = custom issue, P = policy violation issue, E = event analysis issue).
             :type IssueType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for this type of issue.
             :type IssueTypeID: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IssueTypeID: The internal NetMRI identifier for this type of issue.
             :type IssueTypeID: Array of String

            |  ``api version min:`` 2.3
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityID: The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
             :type SeverityID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SeverityID: The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
             :type SeverityID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this issue.
             :type Stability: Float

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Stability: The stability contribution for this issue.
             :type Stability: Array of Float

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Timeout: The period in seconds in which the issue instance is expired if it isn't reported again.
             :type Timeout: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Timeout: The period in seconds in which the issue instance is expired if it isn't reported again.
             :type Timeout: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param Title: The descriptive name of the issue type.
             :type Title: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param Title: The descriptive name of the issue type.
             :type Title: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of issue desc methods. The listed methods will be called on each issue desc returned and included in the output. Available methods are: meta, severity.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
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
            |  ``default:`` IssueDescID

             :param sort: The data field(s) to use for sorting the output. Default is IssueDescID. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID.
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

             :param select: The list of attributes to return for each IssueDesc. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against issue descs, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: Component, Context, Correctness, Description, Frequency, IssueDescID, IssueType, IssueTypeID, PriorityID, SeverityID, Stability, Timeout, Title.
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

             :return issue_descs: An array of the IssueDesc objects that match the specified input criteria.
             :rtype issue_descs: Array of IssueDesc

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available issue descs matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: Component, Context, Correctness, Description, Frequency, IssueDescID, IssueType, IssueTypeID, PriorityID, SeverityID, Stability, Timeout, Title.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Component: The operator to apply to the field Component. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Component: The issue component (Devices, Configuration, VLANs, etc.). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Context: The operator to apply to the field Context. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Context: For internal use only. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Context: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Context: If op_Context is specified, the field named in this input will be compared to the value in Context using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Context must be specified if op_Context is specified.
             :type val_f_Context: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Context: If op_Context is specified, this value will be compared to the value in Context using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Context must be specified if op_Context is specified.
             :type val_c_Context: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Correctness: The operator to apply to the field Correctness. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Correctness: The correctness contribution for this issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Description: The operator to apply to the field Description. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Description: A detailed description of the issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Description: If op_Description is specified, the field named in this input will be compared to the value in Description using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Description must be specified if op_Description is specified.
             :type val_f_Description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Description: If op_Description is specified, this value will be compared to the value in Description using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Description must be specified if op_Description is specified.
             :type val_c_Description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Frequency: The operator to apply to the field Frequency. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Frequency: The time in seconds of how often the analysis engine checks for issues of this type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Frequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Frequency: If op_Frequency is specified, the field named in this input will be compared to the value in Frequency using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Frequency must be specified if op_Frequency is specified.
             :type val_f_Frequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Frequency: If op_Frequency is specified, this value will be compared to the value in Frequency using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Frequency must be specified if op_Frequency is specified.
             :type val_c_Frequency: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IssueDescID: The operator to apply to the field IssueDescID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IssueDescID: The internal NetMRI identifier for this issue description. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IssueDescID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IssueDescID: If op_IssueDescID is specified, the field named in this input will be compared to the value in IssueDescID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IssueDescID must be specified if op_IssueDescID is specified.
             :type val_f_IssueDescID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IssueDescID: If op_IssueDescID is specified, this value will be compared to the value in IssueDescID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IssueDescID must be specified if op_IssueDescID is specified.
             :type val_c_IssueDescID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IssueType: The operator to apply to the field IssueType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IssueType: The source of the issue (S = built into system, C = custom issue, P = policy violation issue, E = event analysis issue). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IssueType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IssueType: If op_IssueType is specified, the field named in this input will be compared to the value in IssueType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IssueType must be specified if op_IssueType is specified.
             :type val_f_IssueType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IssueType: If op_IssueType is specified, this value will be compared to the value in IssueType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IssueType must be specified if op_IssueType is specified.
             :type val_c_IssueType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_IssueTypeID: The operator to apply to the field IssueTypeID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IssueTypeID: The internal NetMRI identifier for this type of issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SeverityID: The operator to apply to the field SeverityID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SeverityID: The issue severity ID (1 = Error, 2 = Warning, 3 = Info). Useful for sorting. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Stability: The operator to apply to the field Stability. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Stability: The stability contribution for this issue. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_Timeout: The operator to apply to the field Timeout. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Timeout: The period in seconds in which the issue instance is expired if it isn't reported again. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_Timeout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_Timeout: If op_Timeout is specified, the field named in this input will be compared to the value in Timeout using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_Timeout must be specified if op_Timeout is specified.
             :type val_f_Timeout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_Timeout: If op_Timeout is specified, this value will be compared to the value in Timeout using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_Timeout must be specified if op_Timeout is specified.
             :type val_c_Timeout: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_Title: The operator to apply to the field Title. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. Title: The descriptive name of the issue type. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param methods: A list of issue desc methods. The listed methods will be called on each issue desc returned and included in the output. Available methods are: meta, severity.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: meta.
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
            |  ``default:`` IssueDescID

             :param sort: The data field(s) to use for sorting the output. Default is IssueDescID. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID.
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

             :param select: The list of attributes to return for each IssueDesc. Valid values are IssueTypeID, Title, Description, Component, SeverityID, PriorityID, Correctness, Stability, Context, IssueType, Frequency, Timeout, IssueDescID. If empty or omitted, all attributes will be returned.
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

             :return issue_descs: An array of the IssueDesc objects that match the specified input criteria.
             :rtype issue_descs: Array of IssueDesc

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def update(self, **kwargs):
        """Updates an existing issue desc.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IssueDescID: The internal NetMRI identifier for this issue description.
             :type IssueDescID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated issue desc.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated issue desc.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated issue desc.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return issue_desc: The updated issue desc.
             :rtype issue_desc: IssueDesc

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)
