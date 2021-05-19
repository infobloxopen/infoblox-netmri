from ..broker import Broker


class IfPerfHourlyBroker(Broker):
    controller = "if_perf_hourlies"

    def index(self, **kwargs):
        """Lists the available if perf hourlies. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which interface hourly performance information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which interface hourly performance information was collected.
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
            |  ``default:`` today

             :param starttime: The data returned will represent the if perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the if perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions.
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

             :param select: The list of attributes to return for each IfPerfHourly. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions. If empty or omitted, all attributes will be returned.
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

             :return if_perf_hourlies: An array of the IfPerfHourly objects that match the specified input criteria.
             :rtype if_perf_hourlies: Array of IfPerfHourly

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available if perf hourlies matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device from which interface hourly performance information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which interface hourly performance information was collected.
             :type DeviceID: Array of Integer

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

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record was initially created in NetMRI.
             :type StartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifAlignmentErrors: The number of alignment errors of each packet in the interface.
             :type ifAlignmentErrors: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifAlignmentErrors: The number of alignment errors of each packet in the interface.
             :type ifAlignmentErrors: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifFCSErrors: The number of FCS errors of each packet in the interface.
             :type ifFCSErrors: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifFCSErrors: The number of FCS errors of each packet in the interface.
             :type ifFCSErrors: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInBroadcastPkts: The number of incoming broadcast packets.
             :type ifInBroadcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInBroadcastPkts: The number of incoming broadcast packets.
             :type ifInBroadcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInDiscards: The number of incoming discarded packets.
             :type ifInDiscards: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInDiscards: The number of incoming discarded packets.
             :type ifInDiscards: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInErrors: The number of incoming errors in each packet of an interface.
             :type ifInErrors: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInErrors: The number of incoming errors in each packet of an interface.
             :type ifInErrors: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInMulticastPkts: The number of incoming multicast packets.
             :type ifInMulticastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInMulticastPkts: The number of incoming multicast packets.
             :type ifInMulticastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInNUcastPkts: The number of non unicasting packets.
             :type ifInNUcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInNUcastPkts: The number of non unicasting packets.
             :type ifInNUcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInOctets: The total number of incoming octets.
             :type ifInOctets: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInOctets: The total number of incoming octets.
             :type ifInOctets: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifInUcastPkts: The number of incoming unicast packets.
             :type ifInUcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifInUcastPkts: The number of incoming unicast packets.
             :type ifInUcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The current index of hourly performance of an interface.
             :type ifIndex: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifIndex: The current index of hourly performance of an interface.
             :type ifIndex: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifLateCollisions: The number of late collisions occurs while sending the packets.
             :type ifLateCollisions: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifLateCollisions: The number of late collisions occurs while sending the packets.
             :type ifLateCollisions: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutBroadcastPkts: The number of outgoing broadcast packets of an interface.
             :type ifOutBroadcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutBroadcastPkts: The number of outgoing broadcast packets of an interface.
             :type ifOutBroadcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutDiscards: The number of outgoing discarded packets.
             :type ifOutDiscards: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutDiscards: The number of outgoing discarded packets.
             :type ifOutDiscards: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutErrors: The number of outgoing error packets.
             :type ifOutErrors: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutErrors: The number of outgoing error packets.
             :type ifOutErrors: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutMulticastPkts: The number of outgoing multicast packets of an interface.
             :type ifOutMulticastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutMulticastPkts: The number of outgoing multicast packets of an interface.
             :type ifOutMulticastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutNUcastPkts: The number of outgoing non unicast packets of an interface.
             :type ifOutNUcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutNUcastPkts: The number of outgoing non unicast packets of an interface.
             :type ifOutNUcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutOctets: The number of outgoing octets of an interface.
             :type ifOutOctets: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutOctets: The number of outgoing octets of an interface.
             :type ifOutOctets: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutUcastPkts: The number of outgoing unicast packets of an interface.
             :type ifOutUcastPkts: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifOutUcastPkts: The number of outgoing unicast packets of an interface.
             :type ifOutUcastPkts: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifSpeed: The speed of packets sends per hour.
             :type ifSpeed: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifSpeed: The speed of packets sends per hour.
             :type ifSpeed: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifTotalChanges: The total number of changes occurs in each hour of an interface.
             :type ifTotalChanges: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifTotalChanges: The total number of changes occurs in each hour of an interface.
             :type ifTotalChanges: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the if perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the if perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions.
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

             :param select: The list of attributes to return for each IfPerfHourly. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if perf hourlies, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, EndTime, StartTime, ifAlignmentErrors, ifFCSErrors, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifInMulticastPkts, ifInNUcastPkts, ifInOctets, ifInUcastPkts, ifIndex, ifLateCollisions, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifOutMulticastPkts, ifOutNUcastPkts, ifOutOctets, ifOutUcastPkts, ifSpeed, ifTotalChanges.
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

             :return if_perf_hourlies: An array of the IfPerfHourly objects that match the specified input criteria.
             :rtype if_perf_hourlies: Array of IfPerfHourly

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if perf hourlies matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, EndTime, StartTime, ifAlignmentErrors, ifFCSErrors, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifInMulticastPkts, ifInNUcastPkts, ifInOctets, ifInUcastPkts, ifIndex, ifLateCollisions, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifOutMulticastPkts, ifOutNUcastPkts, ifOutOctets, ifOutUcastPkts, ifSpeed, ifTotalChanges.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which interface hourly performance information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_StartTime: If op_StartTime is specified, the field named in this input will be compared to the value in StartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_StartTime must be specified if op_StartTime is specified.
             :type val_f_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_StartTime: If op_StartTime is specified, this value will be compared to the value in StartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_StartTime must be specified if op_StartTime is specified.
             :type val_c_StartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifAlignmentErrors: The operator to apply to the field ifAlignmentErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifAlignmentErrors: The number of alignment errors of each packet in the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifAlignmentErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifAlignmentErrors: If op_ifAlignmentErrors is specified, the field named in this input will be compared to the value in ifAlignmentErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifAlignmentErrors must be specified if op_ifAlignmentErrors is specified.
             :type val_f_ifAlignmentErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifAlignmentErrors: If op_ifAlignmentErrors is specified, this value will be compared to the value in ifAlignmentErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifAlignmentErrors must be specified if op_ifAlignmentErrors is specified.
             :type val_c_ifAlignmentErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifFCSErrors: The operator to apply to the field ifFCSErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifFCSErrors: The number of FCS errors of each packet in the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifFCSErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifFCSErrors: If op_ifFCSErrors is specified, the field named in this input will be compared to the value in ifFCSErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifFCSErrors must be specified if op_ifFCSErrors is specified.
             :type val_f_ifFCSErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifFCSErrors: If op_ifFCSErrors is specified, this value will be compared to the value in ifFCSErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifFCSErrors must be specified if op_ifFCSErrors is specified.
             :type val_c_ifFCSErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInBroadcastPkts: The operator to apply to the field ifInBroadcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInBroadcastPkts: The number of incoming broadcast packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInBroadcastPkts: If op_ifInBroadcastPkts is specified, the field named in this input will be compared to the value in ifInBroadcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInBroadcastPkts must be specified if op_ifInBroadcastPkts is specified.
             :type val_f_ifInBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInBroadcastPkts: If op_ifInBroadcastPkts is specified, this value will be compared to the value in ifInBroadcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInBroadcastPkts must be specified if op_ifInBroadcastPkts is specified.
             :type val_c_ifInBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInDiscards: The operator to apply to the field ifInDiscards. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInDiscards: The number of incoming discarded packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInDiscards: If op_ifInDiscards is specified, the field named in this input will be compared to the value in ifInDiscards using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInDiscards must be specified if op_ifInDiscards is specified.
             :type val_f_ifInDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInDiscards: If op_ifInDiscards is specified, this value will be compared to the value in ifInDiscards using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInDiscards must be specified if op_ifInDiscards is specified.
             :type val_c_ifInDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInErrors: The operator to apply to the field ifInErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInErrors: The number of incoming errors in each packet of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInErrors: If op_ifInErrors is specified, the field named in this input will be compared to the value in ifInErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInErrors must be specified if op_ifInErrors is specified.
             :type val_f_ifInErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInErrors: If op_ifInErrors is specified, this value will be compared to the value in ifInErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInErrors must be specified if op_ifInErrors is specified.
             :type val_c_ifInErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInMulticastPkts: The operator to apply to the field ifInMulticastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInMulticastPkts: The number of incoming multicast packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInMulticastPkts: If op_ifInMulticastPkts is specified, the field named in this input will be compared to the value in ifInMulticastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInMulticastPkts must be specified if op_ifInMulticastPkts is specified.
             :type val_f_ifInMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInMulticastPkts: If op_ifInMulticastPkts is specified, this value will be compared to the value in ifInMulticastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInMulticastPkts must be specified if op_ifInMulticastPkts is specified.
             :type val_c_ifInMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInNUcastPkts: The operator to apply to the field ifInNUcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInNUcastPkts: The number of non unicasting packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInNUcastPkts: If op_ifInNUcastPkts is specified, the field named in this input will be compared to the value in ifInNUcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInNUcastPkts must be specified if op_ifInNUcastPkts is specified.
             :type val_f_ifInNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInNUcastPkts: If op_ifInNUcastPkts is specified, this value will be compared to the value in ifInNUcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInNUcastPkts must be specified if op_ifInNUcastPkts is specified.
             :type val_c_ifInNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInOctets: The operator to apply to the field ifInOctets. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInOctets: The total number of incoming octets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInOctets: If op_ifInOctets is specified, the field named in this input will be compared to the value in ifInOctets using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInOctets must be specified if op_ifInOctets is specified.
             :type val_f_ifInOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInOctets: If op_ifInOctets is specified, this value will be compared to the value in ifInOctets using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInOctets must be specified if op_ifInOctets is specified.
             :type val_c_ifInOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifInUcastPkts: The operator to apply to the field ifInUcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifInUcastPkts: The number of incoming unicast packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifInUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifInUcastPkts: If op_ifInUcastPkts is specified, the field named in this input will be compared to the value in ifInUcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifInUcastPkts must be specified if op_ifInUcastPkts is specified.
             :type val_f_ifInUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifInUcastPkts: If op_ifInUcastPkts is specified, this value will be compared to the value in ifInUcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifInUcastPkts must be specified if op_ifInUcastPkts is specified.
             :type val_c_ifInUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifIndex: The operator to apply to the field ifIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifIndex: The current index of hourly performance of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifIndex: If op_ifIndex is specified, the field named in this input will be compared to the value in ifIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifIndex must be specified if op_ifIndex is specified.
             :type val_f_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifIndex: If op_ifIndex is specified, this value will be compared to the value in ifIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifIndex must be specified if op_ifIndex is specified.
             :type val_c_ifIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifLateCollisions: The operator to apply to the field ifLateCollisions. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifLateCollisions: The number of late collisions occurs while sending the packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifLateCollisions: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifLateCollisions: If op_ifLateCollisions is specified, the field named in this input will be compared to the value in ifLateCollisions using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifLateCollisions must be specified if op_ifLateCollisions is specified.
             :type val_f_ifLateCollisions: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifLateCollisions: If op_ifLateCollisions is specified, this value will be compared to the value in ifLateCollisions using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifLateCollisions must be specified if op_ifLateCollisions is specified.
             :type val_c_ifLateCollisions: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutBroadcastPkts: The operator to apply to the field ifOutBroadcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutBroadcastPkts: The number of outgoing broadcast packets of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutBroadcastPkts: If op_ifOutBroadcastPkts is specified, the field named in this input will be compared to the value in ifOutBroadcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutBroadcastPkts must be specified if op_ifOutBroadcastPkts is specified.
             :type val_f_ifOutBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutBroadcastPkts: If op_ifOutBroadcastPkts is specified, this value will be compared to the value in ifOutBroadcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutBroadcastPkts must be specified if op_ifOutBroadcastPkts is specified.
             :type val_c_ifOutBroadcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutDiscards: The operator to apply to the field ifOutDiscards. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutDiscards: The number of outgoing discarded packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutDiscards: If op_ifOutDiscards is specified, the field named in this input will be compared to the value in ifOutDiscards using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutDiscards must be specified if op_ifOutDiscards is specified.
             :type val_f_ifOutDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutDiscards: If op_ifOutDiscards is specified, this value will be compared to the value in ifOutDiscards using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutDiscards must be specified if op_ifOutDiscards is specified.
             :type val_c_ifOutDiscards: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutErrors: The operator to apply to the field ifOutErrors. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutErrors: The number of outgoing error packets. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutErrors: If op_ifOutErrors is specified, the field named in this input will be compared to the value in ifOutErrors using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutErrors must be specified if op_ifOutErrors is specified.
             :type val_f_ifOutErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutErrors: If op_ifOutErrors is specified, this value will be compared to the value in ifOutErrors using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutErrors must be specified if op_ifOutErrors is specified.
             :type val_c_ifOutErrors: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutMulticastPkts: The operator to apply to the field ifOutMulticastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutMulticastPkts: The number of outgoing multicast packets of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutMulticastPkts: If op_ifOutMulticastPkts is specified, the field named in this input will be compared to the value in ifOutMulticastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutMulticastPkts must be specified if op_ifOutMulticastPkts is specified.
             :type val_f_ifOutMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutMulticastPkts: If op_ifOutMulticastPkts is specified, this value will be compared to the value in ifOutMulticastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutMulticastPkts must be specified if op_ifOutMulticastPkts is specified.
             :type val_c_ifOutMulticastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutNUcastPkts: The operator to apply to the field ifOutNUcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutNUcastPkts: The number of outgoing non unicast packets of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutNUcastPkts: If op_ifOutNUcastPkts is specified, the field named in this input will be compared to the value in ifOutNUcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutNUcastPkts must be specified if op_ifOutNUcastPkts is specified.
             :type val_f_ifOutNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutNUcastPkts: If op_ifOutNUcastPkts is specified, this value will be compared to the value in ifOutNUcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutNUcastPkts must be specified if op_ifOutNUcastPkts is specified.
             :type val_c_ifOutNUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutOctets: The operator to apply to the field ifOutOctets. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutOctets: The number of outgoing octets of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutOctets: If op_ifOutOctets is specified, the field named in this input will be compared to the value in ifOutOctets using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutOctets must be specified if op_ifOutOctets is specified.
             :type val_f_ifOutOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutOctets: If op_ifOutOctets is specified, this value will be compared to the value in ifOutOctets using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutOctets must be specified if op_ifOutOctets is specified.
             :type val_c_ifOutOctets: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifOutUcastPkts: The operator to apply to the field ifOutUcastPkts. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifOutUcastPkts: The number of outgoing unicast packets of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifOutUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifOutUcastPkts: If op_ifOutUcastPkts is specified, the field named in this input will be compared to the value in ifOutUcastPkts using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifOutUcastPkts must be specified if op_ifOutUcastPkts is specified.
             :type val_f_ifOutUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifOutUcastPkts: If op_ifOutUcastPkts is specified, this value will be compared to the value in ifOutUcastPkts using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifOutUcastPkts must be specified if op_ifOutUcastPkts is specified.
             :type val_c_ifOutUcastPkts: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifSpeed: The operator to apply to the field ifSpeed. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifSpeed: The speed of packets sends per hour. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifSpeed: If op_ifSpeed is specified, the field named in this input will be compared to the value in ifSpeed using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifSpeed must be specified if op_ifSpeed is specified.
             :type val_f_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifSpeed: If op_ifSpeed is specified, this value will be compared to the value in ifSpeed using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifSpeed must be specified if op_ifSpeed is specified.
             :type val_c_ifSpeed: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifTotalChanges: The operator to apply to the field ifTotalChanges. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifTotalChanges: The total number of changes occurs in each hour of an interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifTotalChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifTotalChanges: If op_ifTotalChanges is specified, the field named in this input will be compared to the value in ifTotalChanges using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifTotalChanges must be specified if op_ifTotalChanges is specified.
             :type val_f_ifTotalChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifTotalChanges: If op_ifTotalChanges is specified, this value will be compared to the value in ifTotalChanges using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifTotalChanges must be specified if op_ifTotalChanges is specified.
             :type val_c_ifTotalChanges: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the if perf hourlies with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the if perf hourlies with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

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
            |  ``default:`` DeviceID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceID. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions.
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

             :param select: The list of attributes to return for each IfPerfHourly. Valid values are DataSourceID, StartTime, EndTime, DeviceID, ifIndex, ifSpeed, ifTotalChanges, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInMulticastPkts, ifInBroadcastPkts, ifInDiscards, ifInErrors, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutMulticastPkts, ifOutBroadcastPkts, ifOutDiscards, ifOutErrors, ifAlignmentErrors, ifFCSErrors, ifLateCollisions. If empty or omitted, all attributes will be returned.
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

             :return if_perf_hourlies: An array of the IfPerfHourly objects that match the specified input criteria.
             :rtype if_perf_hourlies: Array of IfPerfHourly

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
