from ..broker import Broker


class NiosGridMemberBroker(Broker):
    controller = "nios_grid_members"

    def index(self, **kwargs):
        """Lists the available nios grid members. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which NIOS GridMember entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which NIOS GridMember entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberDeviceID: The internal NetMRI identifier of each device in the NIOS GridMember.
             :type GridMemberDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberDeviceID: The internal NetMRI identifier of each device in the NIOS GridMember.
             :type GridMemberDeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPDotted: The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
             :type GridMemberIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPDotted: The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
             :type GridMemberIPDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Array of Integer

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

             :param timestamp: The data returned will represent the nios grid members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of nios grid member methods. The listed methods will be called on each nios grid member returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` GridMemberStatusID

             :param sort: The data field(s) to use for sorting the output. Default is GridMemberStatusID. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster.
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

             :param select: The list of attributes to return for each NiosGridMember. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster. If empty or omitted, all attributes will be returned.
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

             :return nios_grid_members: An array of the NiosGridMember objects that match the specified input criteria.
             :rtype nios_grid_members: Array of NiosGridMember

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified nios grid member.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of nios grid member methods. The listed methods will be called on each nios grid member returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return nios_grid_member: The nios grid member identified by the specified GridMemberStatusID.
             :rtype nios_grid_member: NiosGridMember

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available nios grid members matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

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

             :param DeviceID: The internal NetMRI identifier for the device from which NIOS GridMember entry was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which NIOS GridMember entry was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type GridMemberChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type GridMemberChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberDeviceID: The internal NetMRI identifier of each device in the NIOS GridMember.
             :type GridMemberDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberDeviceID: The internal NetMRI identifier of each device in the NIOS GridMember.
             :type GridMemberDeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberEndTime: The ending effective time of this record, or empty if still in effect.
             :type GridMemberEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberEndTime: The ending effective time of this record, or empty if still in effect.
             :type GridMemberEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberFirstSeenTime: The timestamp of when NetMRI first discovered this interface in the NIOS GridMember.
             :type GridMemberFirstSeenTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberFirstSeenTime: The timestamp of when NetMRI first discovered this interface in the NIOS GridMember.
             :type GridMemberFirstSeenTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPDotted: The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
             :type GridMemberIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPDotted: The management IP address of the switch, in dotted (or colon-delimited for IPv6) format.
             :type GridMemberIPDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPNumeric: The numerical value of the GridMember.
             :type GridMemberIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberIPNumeric: The numerical value of the GridMember.
             :type GridMemberIPNumeric: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberLastRepTimeFromMaster: The last response time returned from master in the NIOS GridMember.
             :type GridMemberLastRepTimeFromMaster: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberLastRepTimeFromMaster: The last response time returned from master in the NIOS GridMember.
             :type GridMemberLastRepTimeFromMaster: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberLastRepTimeToMaster: The last response time sent to master of the NIOS grid member.
             :type GridMemberLastRepTimeToMaster: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberLastRepTimeToMaster: The last response time sent to master of the NIOS grid member.
             :type GridMemberLastRepTimeToMaster: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberQueueFromMaster: The grid member queue return from master in the NIOS GridMember.
             :type GridMemberQueueFromMaster: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberQueueFromMaster: The grid member queue return from master in the NIOS GridMember.
             :type GridMemberQueueFromMaster: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberQueueToMaster: The grid member queue sent to master in the NIOs GridMember.
             :type GridMemberQueueToMaster: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberQueueToMaster: The grid member queue sent to master in the NIOs GridMember.
             :type GridMemberQueueToMaster: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStartTime: The starting effective time of this record.
             :type GridMemberStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStartTime: The starting effective time of this record.
             :type GridMemberStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatus: The status of the NIOS GridMember.
             :type GridMemberStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatus: The status of the NIOS GridMember.
             :type GridMemberStatus: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberTimestamp: The date and time this record was collected or calculated.
             :type GridMemberTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param GridMemberTimestamp: The date and time this record was collected or calculated.
             :type GridMemberTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the nios grid members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of nios grid member methods. The listed methods will be called on each nios grid member returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` GridMemberStatusID

             :param sort: The data field(s) to use for sorting the output. Default is GridMemberStatusID. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster.
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

             :param select: The list of attributes to return for each NiosGridMember. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against nios grid members, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, GridMemberChangedCols, GridMemberDeviceID, GridMemberEndTime, GridMemberFirstSeenTime, GridMemberIPDotted, GridMemberIPNumeric, GridMemberLastRepTimeFromMaster, GridMemberLastRepTimeToMaster, GridMemberQueueFromMaster, GridMemberQueueToMaster, GridMemberStartTime, GridMemberStatus, GridMemberStatusID, GridMemberTimestamp.
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

             :return nios_grid_members: An array of the NiosGridMember objects that match the specified input criteria.
             :rtype nios_grid_members: Array of NiosGridMember

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available nios grid members matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, GridMemberChangedCols, GridMemberDeviceID, GridMemberEndTime, GridMemberFirstSeenTime, GridMemberIPDotted, GridMemberIPNumeric, GridMemberLastRepTimeFromMaster, GridMemberLastRepTimeToMaster, GridMemberQueueFromMaster, GridMemberQueueToMaster, GridMemberStartTime, GridMemberStatus, GridMemberStatusID, GridMemberTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which NIOS GridMember entry was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_GridMemberChangedCols: The operator to apply to the field GridMemberChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberChangedCols: If op_GridMemberChangedCols is specified, the field named in this input will be compared to the value in GridMemberChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberChangedCols must be specified if op_GridMemberChangedCols is specified.
             :type val_f_GridMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberChangedCols: If op_GridMemberChangedCols is specified, this value will be compared to the value in GridMemberChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberChangedCols must be specified if op_GridMemberChangedCols is specified.
             :type val_c_GridMemberChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberDeviceID: The operator to apply to the field GridMemberDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberDeviceID: The internal NetMRI identifier of each device in the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberDeviceID: If op_GridMemberDeviceID is specified, the field named in this input will be compared to the value in GridMemberDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberDeviceID must be specified if op_GridMemberDeviceID is specified.
             :type val_f_GridMemberDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberDeviceID: If op_GridMemberDeviceID is specified, this value will be compared to the value in GridMemberDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberDeviceID must be specified if op_GridMemberDeviceID is specified.
             :type val_c_GridMemberDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberEndTime: The operator to apply to the field GridMemberEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberEndTime: If op_GridMemberEndTime is specified, the field named in this input will be compared to the value in GridMemberEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberEndTime must be specified if op_GridMemberEndTime is specified.
             :type val_f_GridMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberEndTime: If op_GridMemberEndTime is specified, this value will be compared to the value in GridMemberEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberEndTime must be specified if op_GridMemberEndTime is specified.
             :type val_c_GridMemberEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberFirstSeenTime: The operator to apply to the field GridMemberFirstSeenTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberFirstSeenTime: The timestamp of when NetMRI first discovered this interface in the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberFirstSeenTime: If op_GridMemberFirstSeenTime is specified, the field named in this input will be compared to the value in GridMemberFirstSeenTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberFirstSeenTime must be specified if op_GridMemberFirstSeenTime is specified.
             :type val_f_GridMemberFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberFirstSeenTime: If op_GridMemberFirstSeenTime is specified, this value will be compared to the value in GridMemberFirstSeenTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberFirstSeenTime must be specified if op_GridMemberFirstSeenTime is specified.
             :type val_c_GridMemberFirstSeenTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberIPDotted: The operator to apply to the field GridMemberIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberIPDotted: The management IP address of the switch, in dotted (or colon-delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberIPDotted: If op_GridMemberIPDotted is specified, the field named in this input will be compared to the value in GridMemberIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberIPDotted must be specified if op_GridMemberIPDotted is specified.
             :type val_f_GridMemberIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberIPDotted: If op_GridMemberIPDotted is specified, this value will be compared to the value in GridMemberIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberIPDotted must be specified if op_GridMemberIPDotted is specified.
             :type val_c_GridMemberIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberIPNumeric: The operator to apply to the field GridMemberIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberIPNumeric: The numerical value of the GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberIPNumeric: If op_GridMemberIPNumeric is specified, the field named in this input will be compared to the value in GridMemberIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberIPNumeric must be specified if op_GridMemberIPNumeric is specified.
             :type val_f_GridMemberIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberIPNumeric: If op_GridMemberIPNumeric is specified, this value will be compared to the value in GridMemberIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberIPNumeric must be specified if op_GridMemberIPNumeric is specified.
             :type val_c_GridMemberIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberLastRepTimeFromMaster: The operator to apply to the field GridMemberLastRepTimeFromMaster. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberLastRepTimeFromMaster: The last response time returned from master in the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberLastRepTimeFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberLastRepTimeFromMaster: If op_GridMemberLastRepTimeFromMaster is specified, the field named in this input will be compared to the value in GridMemberLastRepTimeFromMaster using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberLastRepTimeFromMaster must be specified if op_GridMemberLastRepTimeFromMaster is specified.
             :type val_f_GridMemberLastRepTimeFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberLastRepTimeFromMaster: If op_GridMemberLastRepTimeFromMaster is specified, this value will be compared to the value in GridMemberLastRepTimeFromMaster using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberLastRepTimeFromMaster must be specified if op_GridMemberLastRepTimeFromMaster is specified.
             :type val_c_GridMemberLastRepTimeFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberLastRepTimeToMaster: The operator to apply to the field GridMemberLastRepTimeToMaster. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberLastRepTimeToMaster: The last response time sent to master of the NIOS grid member. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberLastRepTimeToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberLastRepTimeToMaster: If op_GridMemberLastRepTimeToMaster is specified, the field named in this input will be compared to the value in GridMemberLastRepTimeToMaster using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberLastRepTimeToMaster must be specified if op_GridMemberLastRepTimeToMaster is specified.
             :type val_f_GridMemberLastRepTimeToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberLastRepTimeToMaster: If op_GridMemberLastRepTimeToMaster is specified, this value will be compared to the value in GridMemberLastRepTimeToMaster using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberLastRepTimeToMaster must be specified if op_GridMemberLastRepTimeToMaster is specified.
             :type val_c_GridMemberLastRepTimeToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberQueueFromMaster: The operator to apply to the field GridMemberQueueFromMaster. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberQueueFromMaster: The grid member queue return from master in the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberQueueFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberQueueFromMaster: If op_GridMemberQueueFromMaster is specified, the field named in this input will be compared to the value in GridMemberQueueFromMaster using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberQueueFromMaster must be specified if op_GridMemberQueueFromMaster is specified.
             :type val_f_GridMemberQueueFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberQueueFromMaster: If op_GridMemberQueueFromMaster is specified, this value will be compared to the value in GridMemberQueueFromMaster using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberQueueFromMaster must be specified if op_GridMemberQueueFromMaster is specified.
             :type val_c_GridMemberQueueFromMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberQueueToMaster: The operator to apply to the field GridMemberQueueToMaster. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberQueueToMaster: The grid member queue sent to master in the NIOs GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberQueueToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberQueueToMaster: If op_GridMemberQueueToMaster is specified, the field named in this input will be compared to the value in GridMemberQueueToMaster using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberQueueToMaster must be specified if op_GridMemberQueueToMaster is specified.
             :type val_f_GridMemberQueueToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberQueueToMaster: If op_GridMemberQueueToMaster is specified, this value will be compared to the value in GridMemberQueueToMaster using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberQueueToMaster must be specified if op_GridMemberQueueToMaster is specified.
             :type val_c_GridMemberQueueToMaster: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberStartTime: The operator to apply to the field GridMemberStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberStartTime: If op_GridMemberStartTime is specified, the field named in this input will be compared to the value in GridMemberStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberStartTime must be specified if op_GridMemberStartTime is specified.
             :type val_f_GridMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberStartTime: If op_GridMemberStartTime is specified, this value will be compared to the value in GridMemberStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberStartTime must be specified if op_GridMemberStartTime is specified.
             :type val_c_GridMemberStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberStatus: The operator to apply to the field GridMemberStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberStatus: The status of the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberStatus: If op_GridMemberStatus is specified, the field named in this input will be compared to the value in GridMemberStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberStatus must be specified if op_GridMemberStatus is specified.
             :type val_f_GridMemberStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberStatus: If op_GridMemberStatus is specified, this value will be compared to the value in GridMemberStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberStatus must be specified if op_GridMemberStatus is specified.
             :type val_c_GridMemberStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberStatusID: The operator to apply to the field GridMemberStatusID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberStatusID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberStatusID: If op_GridMemberStatusID is specified, the field named in this input will be compared to the value in GridMemberStatusID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberStatusID must be specified if op_GridMemberStatusID is specified.
             :type val_f_GridMemberStatusID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberStatusID: If op_GridMemberStatusID is specified, this value will be compared to the value in GridMemberStatusID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberStatusID must be specified if op_GridMemberStatusID is specified.
             :type val_c_GridMemberStatusID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_GridMemberTimestamp: The operator to apply to the field GridMemberTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. GridMemberTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_GridMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_GridMemberTimestamp: If op_GridMemberTimestamp is specified, the field named in this input will be compared to the value in GridMemberTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_GridMemberTimestamp must be specified if op_GridMemberTimestamp is specified.
             :type val_f_GridMemberTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_GridMemberTimestamp: If op_GridMemberTimestamp is specified, this value will be compared to the value in GridMemberTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_GridMemberTimestamp must be specified if op_GridMemberTimestamp is specified.
             :type val_c_GridMemberTimestamp: String

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

             :param timestamp: The data returned will represent the nios grid members as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of nios grid member methods. The listed methods will be called on each nios grid member returned and included in the output. Available methods are: device.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device.
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
            |  ``default:`` GridMemberStatusID

             :param sort: The data field(s) to use for sorting the output. Default is GridMemberStatusID. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster.
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

             :param select: The list of attributes to return for each NiosGridMember. Valid values are DataSourceID, GridMemberStatusID, GridMemberStartTime, GridMemberEndTime, GridMemberChangedCols, GridMemberTimestamp, GridMemberFirstSeenTime, DeviceID, GridMemberDeviceID, GridMemberIPDotted, GridMemberIPNumeric, GridMemberStatus, GridMemberQueueFromMaster, GridMemberLastRepTimeFromMaster, GridMemberQueueToMaster, GridMemberLastRepTimeToMaster. If empty or omitted, all attributes will be returned.
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

             :return nios_grid_members: An array of the NiosGridMember objects that match the specified input criteria.
             :rtype nios_grid_members: Array of NiosGridMember

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

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

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param GridMemberStatusID: The internal NetMRI identifier of the status in the NIOS GridMember.
             :type GridMemberStatusID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
