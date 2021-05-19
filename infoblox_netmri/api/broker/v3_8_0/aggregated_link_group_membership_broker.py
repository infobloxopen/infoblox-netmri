from ..broker import Broker


class AggregatedLinkGroupMembershipBroker(Broker):
    controller = "aggregated_link_group_memberships"

    def show(self, **kwargs):
        """Shows the details for the specified aggregated link group membership.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param aggLinkGroupMemberID: The internal NetMRI identifier of the aggregated link group membership.
             :type aggLinkGroupMemberID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of aggregated link group membership methods. The listed methods will be called on each aggregated link group membership returned and included in the output. Available methods are: data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return aggregated_link_group_membership: The aggregated link group membership identified by the specified aggLinkGroupMemberID.
             :rtype aggregated_link_group_membership: AggregatedLinkGroupMembership

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available aggregated link group memberships. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: No description is available for DeviceID.
             :type DeviceID: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberID: No description is available for aggLinkGroupMemberID.
             :type aggLinkGroupMemberID: Array of String

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

             :param timestamp: The data returned will represent the aggregated link group memberships as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of aggregated link group membership methods. The listed methods will be called on each aggregated link group membership returned and included in the output. Available methods are: data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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
            |  ``default:`` aggLinkGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is aggLinkGroupMemberID. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols.
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

             :param select: The list of attributes to return for each AggregatedLinkGroupMembership. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols. If empty or omitted, all attributes will be returned.
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

             :return aggregated_link_group_memberships: An array of the AggregatedLinkGroupMembership objects that match the specified input criteria.
             :rtype aggregated_link_group_memberships: Array of AggregatedLinkGroupMembership

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available aggregated link group memberships matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DataSourceID: No description is available for DataSourceID.
             :type DataSourceID: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: No description is available for DeviceID.
             :type DeviceID: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberAggregateInterface: No description is available for aggLinkGroupMemberAggregateInterface.
             :type aggLinkGroupMemberAggregateInterface: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberChangedCols: No description is available for aggLinkGroupMemberChangedCols.
             :type aggLinkGroupMemberChangedCols: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberEndTime: No description is available for aggLinkGroupMemberEndTime.
             :type aggLinkGroupMemberEndTime: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberGroupIndex: No description is available for aggLinkGroupMemberGroupIndex.
             :type aggLinkGroupMemberGroupIndex: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberGroupName: No description is available for aggLinkGroupMemberGroupName.
             :type aggLinkGroupMemberGroupName: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberID: No description is available for aggLinkGroupMemberID.
             :type aggLinkGroupMemberID: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberPhysicalInterface: No description is available for aggLinkGroupMemberPhysicalInterface.
             :type aggLinkGroupMemberPhysicalInterface: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberStartTime: No description is available for aggLinkGroupMemberStartTime.
             :type aggLinkGroupMemberStartTime: Array of String

            |  ``api version min:`` 3.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param aggLinkGroupMemberTimestamp: No description is available for aggLinkGroupMemberTimestamp.
             :type aggLinkGroupMemberTimestamp: Array of String

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

             :param timestamp: The data returned will represent the aggregated link group memberships as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of aggregated link group membership methods. The listed methods will be called on each aggregated link group membership returned and included in the output. Available methods are: data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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
            |  ``default:`` aggLinkGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is aggLinkGroupMemberID. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols.
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

             :param select: The list of attributes to return for each AggregatedLinkGroupMembership. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against aggregated link group memberships, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberChangedCols, aggLinkGroupMemberEndTime, aggLinkGroupMemberGroupIndex, aggLinkGroupMemberGroupName, aggLinkGroupMemberID, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberTimestamp.
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

             :return aggregated_link_group_memberships: An array of the AggregatedLinkGroupMembership objects that match the specified input criteria.
             :rtype aggregated_link_group_memberships: Array of AggregatedLinkGroupMembership

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available aggregated link group memberships matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberChangedCols, aggLinkGroupMemberEndTime, aggLinkGroupMemberGroupIndex, aggLinkGroupMemberGroupName, aggLinkGroupMemberID, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberTimestamp.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DataSourceID: The operator to apply to the field DataSourceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DataSourceID: No description is available for DataSourceID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: No description is available for DeviceID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_aggLinkGroupMemberAggregateInterface: The operator to apply to the field aggLinkGroupMemberAggregateInterface. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberAggregateInterface: No description is available for aggLinkGroupMemberAggregateInterface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberAggregateInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberAggregateInterface: If op_aggLinkGroupMemberAggregateInterface is specified, the field named in this input will be compared to the value in aggLinkGroupMemberAggregateInterface using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberAggregateInterface must be specified if op_aggLinkGroupMemberAggregateInterface is specified.
             :type val_f_aggLinkGroupMemberAggregateInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberAggregateInterface: If op_aggLinkGroupMemberAggregateInterface is specified, this value will be compared to the value in aggLinkGroupMemberAggregateInterface using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberAggregateInterface must be specified if op_aggLinkGroupMemberAggregateInterface is specified.
             :type val_c_aggLinkGroupMemberAggregateInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberChangedCols: The operator to apply to the field aggLinkGroupMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberChangedCols: No description is available for aggLinkGroupMemberChangedCols. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberChangedCols: If op_aggLinkGroupMemberChangedCols is specified, the field named in this input will be compared to the value in aggLinkGroupMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberChangedCols must be specified if op_aggLinkGroupMemberChangedCols is specified.
             :type val_f_aggLinkGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberChangedCols: If op_aggLinkGroupMemberChangedCols is specified, this value will be compared to the value in aggLinkGroupMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberChangedCols must be specified if op_aggLinkGroupMemberChangedCols is specified.
             :type val_c_aggLinkGroupMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberEndTime: The operator to apply to the field aggLinkGroupMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberEndTime: No description is available for aggLinkGroupMemberEndTime. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberEndTime: If op_aggLinkGroupMemberEndTime is specified, the field named in this input will be compared to the value in aggLinkGroupMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberEndTime must be specified if op_aggLinkGroupMemberEndTime is specified.
             :type val_f_aggLinkGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberEndTime: If op_aggLinkGroupMemberEndTime is specified, this value will be compared to the value in aggLinkGroupMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberEndTime must be specified if op_aggLinkGroupMemberEndTime is specified.
             :type val_c_aggLinkGroupMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberGroupIndex: The operator to apply to the field aggLinkGroupMemberGroupIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberGroupIndex: No description is available for aggLinkGroupMemberGroupIndex. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberGroupIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberGroupIndex: If op_aggLinkGroupMemberGroupIndex is specified, the field named in this input will be compared to the value in aggLinkGroupMemberGroupIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberGroupIndex must be specified if op_aggLinkGroupMemberGroupIndex is specified.
             :type val_f_aggLinkGroupMemberGroupIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberGroupIndex: If op_aggLinkGroupMemberGroupIndex is specified, this value will be compared to the value in aggLinkGroupMemberGroupIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberGroupIndex must be specified if op_aggLinkGroupMemberGroupIndex is specified.
             :type val_c_aggLinkGroupMemberGroupIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberGroupName: The operator to apply to the field aggLinkGroupMemberGroupName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberGroupName: No description is available for aggLinkGroupMemberGroupName. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberGroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberGroupName: If op_aggLinkGroupMemberGroupName is specified, the field named in this input will be compared to the value in aggLinkGroupMemberGroupName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberGroupName must be specified if op_aggLinkGroupMemberGroupName is specified.
             :type val_f_aggLinkGroupMemberGroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberGroupName: If op_aggLinkGroupMemberGroupName is specified, this value will be compared to the value in aggLinkGroupMemberGroupName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberGroupName must be specified if op_aggLinkGroupMemberGroupName is specified.
             :type val_c_aggLinkGroupMemberGroupName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberID: The operator to apply to the field aggLinkGroupMemberID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberID: No description is available for aggLinkGroupMemberID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberID: If op_aggLinkGroupMemberID is specified, the field named in this input will be compared to the value in aggLinkGroupMemberID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberID must be specified if op_aggLinkGroupMemberID is specified.
             :type val_f_aggLinkGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberID: If op_aggLinkGroupMemberID is specified, this value will be compared to the value in aggLinkGroupMemberID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberID must be specified if op_aggLinkGroupMemberID is specified.
             :type val_c_aggLinkGroupMemberID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberPhysicalInterface: The operator to apply to the field aggLinkGroupMemberPhysicalInterface. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberPhysicalInterface: No description is available for aggLinkGroupMemberPhysicalInterface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberPhysicalInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberPhysicalInterface: If op_aggLinkGroupMemberPhysicalInterface is specified, the field named in this input will be compared to the value in aggLinkGroupMemberPhysicalInterface using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberPhysicalInterface must be specified if op_aggLinkGroupMemberPhysicalInterface is specified.
             :type val_f_aggLinkGroupMemberPhysicalInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberPhysicalInterface: If op_aggLinkGroupMemberPhysicalInterface is specified, this value will be compared to the value in aggLinkGroupMemberPhysicalInterface using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberPhysicalInterface must be specified if op_aggLinkGroupMemberPhysicalInterface is specified.
             :type val_c_aggLinkGroupMemberPhysicalInterface: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberStartTime: The operator to apply to the field aggLinkGroupMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberStartTime: No description is available for aggLinkGroupMemberStartTime. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberStartTime: If op_aggLinkGroupMemberStartTime is specified, the field named in this input will be compared to the value in aggLinkGroupMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberStartTime must be specified if op_aggLinkGroupMemberStartTime is specified.
             :type val_f_aggLinkGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberStartTime: If op_aggLinkGroupMemberStartTime is specified, this value will be compared to the value in aggLinkGroupMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberStartTime must be specified if op_aggLinkGroupMemberStartTime is specified.
             :type val_c_aggLinkGroupMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_aggLinkGroupMemberTimestamp: The operator to apply to the field aggLinkGroupMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. aggLinkGroupMemberTimestamp: No description is available for aggLinkGroupMemberTimestamp. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_aggLinkGroupMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_aggLinkGroupMemberTimestamp: If op_aggLinkGroupMemberTimestamp is specified, the field named in this input will be compared to the value in aggLinkGroupMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_aggLinkGroupMemberTimestamp must be specified if op_aggLinkGroupMemberTimestamp is specified.
             :type val_f_aggLinkGroupMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_aggLinkGroupMemberTimestamp: If op_aggLinkGroupMemberTimestamp is specified, this value will be compared to the value in aggLinkGroupMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_aggLinkGroupMemberTimestamp must be specified if op_aggLinkGroupMemberTimestamp is specified.
             :type val_c_aggLinkGroupMemberTimestamp: String

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

             :param timestamp: The data returned will represent the aggregated link group memberships as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of aggregated link group membership methods. The listed methods will be called on each aggregated link group membership returned and included in the output. Available methods are: data_source, device, interface.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, interface.
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
            |  ``default:`` aggLinkGroupMemberID

             :param sort: The data field(s) to use for sorting the output. Default is aggLinkGroupMemberID. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols.
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

             :param select: The list of attributes to return for each AggregatedLinkGroupMembership. Valid values are DataSourceID, aggLinkGroupMemberID, aggLinkGroupMemberGroupName, aggLinkGroupMemberGroupIndex, DeviceID, aggLinkGroupMemberAggregateInterface, aggLinkGroupMemberPhysicalInterface, aggLinkGroupMemberStartTime, aggLinkGroupMemberEndTime, aggLinkGroupMemberTimestamp, aggLinkGroupMemberChangedCols. If empty or omitted, all attributes will be returned.
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

             :return aggregated_link_group_memberships: An array of the AggregatedLinkGroupMembership objects that match the specified input criteria.
             :rtype aggregated_link_group_memberships: Array of AggregatedLinkGroupMembership

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def get_aggergation_group_by_interface(self, **kwargs):
        """Get aggregation group (vPC) the interface belongs to

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param physical_interface_id: Internal identifier of physical interface
             :type physical_interface_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_aggergation_group_by_interface"), kwargs)
