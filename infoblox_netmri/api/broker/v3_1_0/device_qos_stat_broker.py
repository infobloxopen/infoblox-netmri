from ..broker import Broker


class DeviceQosStatBroker(Broker):
    controller = "device_qos_stats"

    def index(self, **kwargs):
        """Lists the available device qos stats. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Qos was calculated or collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Qos was calculated or collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceQosID: The internal NetMRI identifier for the Device Quality of Service.
             :type DeviceQosID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceQosID: The internal NetMRI identifier for the Device Quality of Service.
             :type DeviceQosID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the local interface of the Device Qos Statistics.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the local interface of the Device Qos Statistics.
             :type InterfaceID: Array of Integer

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

             :param starttime: The data returned will represent the device qos stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device qos stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
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
            |  ``default:`` DeviceQosID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceQosID. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue.
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

             :param select: The list of attributes to return for each DeviceQosStat. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue. If empty or omitted, all attributes will be returned.
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

             :return device_qos_stats: An array of the DeviceQosStat objects that match the specified input criteria.
             :rtype device_qos_stats: Array of DeviceQosStat

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified device qos stat.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceQosID: The internal NetMRI identifier for the Device Quality of Service.
             :type DeviceQosID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_qos_stat: The device qos stat identified by the specified DeviceQosID.
             :rtype device_qos_stat: DeviceQosStat

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available device qos stats matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Qos was calculated or collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which Qos was calculated or collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceQosID: The internal NetMRI identifier for the Device Quality of Service.
             :type DeviceQosID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceQosID: The internal NetMRI identifier for the Device Quality of Service.
             :type DeviceQosID: Array of Integer

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

             :param InterfaceID: The internal NetMRI identifier of the local interface of the Device Qos Statistics.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier of the local interface of the Device Qos Statistics.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMDesc: The common description of Qos Statistics of each device.
             :type QosCMDesc: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMDesc: The common description of Qos Statistics of each device.
             :type QosCMDesc: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMDropPkt: The number of common drop packet defined in the Qos statistics of each device.
             :type QosCMDropPkt: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMDropPkt: The number of common drop packet defined in the Qos statistics of each device.
             :type QosCMDropPkt: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMInfo: The common information of Device Qos Statistics.
             :type QosCMInfo: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMInfo: The common information of Device Qos Statistics.
             :type QosCMInfo: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMName: The common name of Qos statistics of each device.
             :type QosCMName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMName: The common name of Qos statistics of each device.
             :type QosCMName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMPrePolicyPkt: The number of common policy packet defined in the Qos statistics of each device.
             :type QosCMPrePolicyPkt: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosCMPrePolicyPkt: The number of common policy packet defined in the Qos statistics of each device.
             :type QosCMPrePolicyPkt: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosConfigIndex: The config value of Qos statistics of each device.
             :type QosConfigIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosConfigIndex: The config value of Qos statistics of each device.
             :type QosConfigIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosIfIndex: The current value of the Device Qos Statistics.
             :type QosIfIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosIfIndex: The current value of the Device Qos Statistics.
             :type QosIfIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosIfType: The type of Device Qos Statistics.
             :type QosIfType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosIfType: The type of Device Qos Statistics.
             :type QosIfType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosObjectsIndex: The object index of Qos statistics of each device.
             :type QosObjectsIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosObjectsIndex: The object index of Qos statistics of each device.
             :type QosObjectsIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosObjectsType: The NetMRI-determined the object type of Device Qos Statistics.
             :type QosObjectsType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosObjectsType: The NetMRI-determined the object type of Device Qos Statistics.
             :type QosObjectsType: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosPolicyDirection: Describes the direction of policy defined in the Qos.
             :type QosPolicyDirection: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosPolicyDirection: Describes the direction of policy defined in the Qos.
             :type QosPolicyDirection: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosPolicyIndex: The policy value of Quality of service in each device.
             :type QosPolicyIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosPolicyIndex: The policy value of Quality of service in each device.
             :type QosPolicyIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosSetCfgIpDSCPValue: Defines the configuration IP address of device statistics.
             :type QosSetCfgIpDSCPValue: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosSetCfgIpDSCPValue: Defines the configuration IP address of device statistics.
             :type QosSetCfgIpDSCPValue: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param QosSetCfgIpPrecedenceValue: The precedence value of configuration IP address.
             :type QosSetCfgIpPrecedenceValue: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param QosSetCfgIpPrecedenceValue: The precedence value of configuration IP address.
             :type QosSetCfgIpPrecedenceValue: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record is initially created in the NetMRI.
             :type StartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param StartTime: The date and time the record is initially created in the NetMRI.
             :type StartTime: Array of DateTime

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

             :param starttime: The data returned will represent the device qos stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device qos stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
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
            |  ``default:`` DeviceQosID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceQosID. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue.
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

             :param select: The list of attributes to return for each DeviceQosStat. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against device qos stats, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DeviceID, DeviceQosID, EndTime, InterfaceID, QosCMDesc, QosCMDropPkt, QosCMInfo, QosCMName, QosCMPrePolicyPkt, QosConfigIndex, QosIfIndex, QosIfType, QosObjectsIndex, QosObjectsType, QosPolicyDirection, QosPolicyIndex, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue, StartTime.
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

             :return device_qos_stats: An array of the DeviceQosStat objects that match the specified input criteria.
             :rtype device_qos_stats: Array of DeviceQosStat

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available device qos stats matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DeviceID, DeviceQosID, EndTime, InterfaceID, QosCMDesc, QosCMDropPkt, QosCMInfo, QosCMName, QosCMPrePolicyPkt, QosConfigIndex, QosIfIndex, QosIfType, QosObjectsIndex, QosObjectsType, QosPolicyDirection, QosPolicyIndex, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue, StartTime.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which Qos was calculated or collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_DeviceQosID: The operator to apply to the field DeviceQosID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceQosID: The internal NetMRI identifier for the Device Quality of Service. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceQosID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceQosID: If op_DeviceQosID is specified, the field named in this input will be compared to the value in DeviceQosID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceQosID must be specified if op_DeviceQosID is specified.
             :type val_f_DeviceQosID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceQosID: If op_DeviceQosID is specified, this value will be compared to the value in DeviceQosID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceQosID must be specified if op_DeviceQosID is specified.
             :type val_c_DeviceQosID: String

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

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier of the local interface of the Device Qos Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_InterfaceID: If op_InterfaceID is specified, the field named in this input will be compared to the value in InterfaceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_f_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_InterfaceID: If op_InterfaceID is specified, this value will be compared to the value in InterfaceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_InterfaceID must be specified if op_InterfaceID is specified.
             :type val_c_InterfaceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosCMDesc: The operator to apply to the field QosCMDesc. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosCMDesc: The common description of Qos Statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosCMDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosCMDesc: If op_QosCMDesc is specified, the field named in this input will be compared to the value in QosCMDesc using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosCMDesc must be specified if op_QosCMDesc is specified.
             :type val_f_QosCMDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosCMDesc: If op_QosCMDesc is specified, this value will be compared to the value in QosCMDesc using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosCMDesc must be specified if op_QosCMDesc is specified.
             :type val_c_QosCMDesc: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosCMDropPkt: The operator to apply to the field QosCMDropPkt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosCMDropPkt: The number of common drop packet defined in the Qos statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosCMDropPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosCMDropPkt: If op_QosCMDropPkt is specified, the field named in this input will be compared to the value in QosCMDropPkt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosCMDropPkt must be specified if op_QosCMDropPkt is specified.
             :type val_f_QosCMDropPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosCMDropPkt: If op_QosCMDropPkt is specified, this value will be compared to the value in QosCMDropPkt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosCMDropPkt must be specified if op_QosCMDropPkt is specified.
             :type val_c_QosCMDropPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosCMInfo: The operator to apply to the field QosCMInfo. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosCMInfo: The common information of Device Qos Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosCMInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosCMInfo: If op_QosCMInfo is specified, the field named in this input will be compared to the value in QosCMInfo using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosCMInfo must be specified if op_QosCMInfo is specified.
             :type val_f_QosCMInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosCMInfo: If op_QosCMInfo is specified, this value will be compared to the value in QosCMInfo using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosCMInfo must be specified if op_QosCMInfo is specified.
             :type val_c_QosCMInfo: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosCMName: The operator to apply to the field QosCMName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosCMName: The common name of Qos statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosCMName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosCMName: If op_QosCMName is specified, the field named in this input will be compared to the value in QosCMName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosCMName must be specified if op_QosCMName is specified.
             :type val_f_QosCMName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosCMName: If op_QosCMName is specified, this value will be compared to the value in QosCMName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosCMName must be specified if op_QosCMName is specified.
             :type val_c_QosCMName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosCMPrePolicyPkt: The operator to apply to the field QosCMPrePolicyPkt. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosCMPrePolicyPkt: The number of common policy packet defined in the Qos statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosCMPrePolicyPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosCMPrePolicyPkt: If op_QosCMPrePolicyPkt is specified, the field named in this input will be compared to the value in QosCMPrePolicyPkt using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosCMPrePolicyPkt must be specified if op_QosCMPrePolicyPkt is specified.
             :type val_f_QosCMPrePolicyPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosCMPrePolicyPkt: If op_QosCMPrePolicyPkt is specified, this value will be compared to the value in QosCMPrePolicyPkt using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosCMPrePolicyPkt must be specified if op_QosCMPrePolicyPkt is specified.
             :type val_c_QosCMPrePolicyPkt: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosConfigIndex: The operator to apply to the field QosConfigIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosConfigIndex: The config value of Qos statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosConfigIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosConfigIndex: If op_QosConfigIndex is specified, the field named in this input will be compared to the value in QosConfigIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosConfigIndex must be specified if op_QosConfigIndex is specified.
             :type val_f_QosConfigIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosConfigIndex: If op_QosConfigIndex is specified, this value will be compared to the value in QosConfigIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosConfigIndex must be specified if op_QosConfigIndex is specified.
             :type val_c_QosConfigIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosIfIndex: The operator to apply to the field QosIfIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosIfIndex: The current value of the Device Qos Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosIfIndex: If op_QosIfIndex is specified, the field named in this input will be compared to the value in QosIfIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosIfIndex must be specified if op_QosIfIndex is specified.
             :type val_f_QosIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosIfIndex: If op_QosIfIndex is specified, this value will be compared to the value in QosIfIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosIfIndex must be specified if op_QosIfIndex is specified.
             :type val_c_QosIfIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosIfType: The operator to apply to the field QosIfType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosIfType: The type of Device Qos Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosIfType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosIfType: If op_QosIfType is specified, the field named in this input will be compared to the value in QosIfType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosIfType must be specified if op_QosIfType is specified.
             :type val_f_QosIfType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosIfType: If op_QosIfType is specified, this value will be compared to the value in QosIfType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosIfType must be specified if op_QosIfType is specified.
             :type val_c_QosIfType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosObjectsIndex: The operator to apply to the field QosObjectsIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosObjectsIndex: The object index of Qos statistics of each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosObjectsIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosObjectsIndex: If op_QosObjectsIndex is specified, the field named in this input will be compared to the value in QosObjectsIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosObjectsIndex must be specified if op_QosObjectsIndex is specified.
             :type val_f_QosObjectsIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosObjectsIndex: If op_QosObjectsIndex is specified, this value will be compared to the value in QosObjectsIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosObjectsIndex must be specified if op_QosObjectsIndex is specified.
             :type val_c_QosObjectsIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosObjectsType: The operator to apply to the field QosObjectsType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosObjectsType: The NetMRI-determined the object type of Device Qos Statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosObjectsType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosObjectsType: If op_QosObjectsType is specified, the field named in this input will be compared to the value in QosObjectsType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosObjectsType must be specified if op_QosObjectsType is specified.
             :type val_f_QosObjectsType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosObjectsType: If op_QosObjectsType is specified, this value will be compared to the value in QosObjectsType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosObjectsType must be specified if op_QosObjectsType is specified.
             :type val_c_QosObjectsType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosPolicyDirection: The operator to apply to the field QosPolicyDirection. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosPolicyDirection: Describes the direction of policy defined in the Qos. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosPolicyDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosPolicyDirection: If op_QosPolicyDirection is specified, the field named in this input will be compared to the value in QosPolicyDirection using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosPolicyDirection must be specified if op_QosPolicyDirection is specified.
             :type val_f_QosPolicyDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosPolicyDirection: If op_QosPolicyDirection is specified, this value will be compared to the value in QosPolicyDirection using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosPolicyDirection must be specified if op_QosPolicyDirection is specified.
             :type val_c_QosPolicyDirection: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosPolicyIndex: The operator to apply to the field QosPolicyIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosPolicyIndex: The policy value of Quality of service in each device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosPolicyIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosPolicyIndex: If op_QosPolicyIndex is specified, the field named in this input will be compared to the value in QosPolicyIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosPolicyIndex must be specified if op_QosPolicyIndex is specified.
             :type val_f_QosPolicyIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosPolicyIndex: If op_QosPolicyIndex is specified, this value will be compared to the value in QosPolicyIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosPolicyIndex must be specified if op_QosPolicyIndex is specified.
             :type val_c_QosPolicyIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosSetCfgIpDSCPValue: The operator to apply to the field QosSetCfgIpDSCPValue. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosSetCfgIpDSCPValue: Defines the configuration IP address of device statistics. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosSetCfgIpDSCPValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosSetCfgIpDSCPValue: If op_QosSetCfgIpDSCPValue is specified, the field named in this input will be compared to the value in QosSetCfgIpDSCPValue using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosSetCfgIpDSCPValue must be specified if op_QosSetCfgIpDSCPValue is specified.
             :type val_f_QosSetCfgIpDSCPValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosSetCfgIpDSCPValue: If op_QosSetCfgIpDSCPValue is specified, this value will be compared to the value in QosSetCfgIpDSCPValue using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosSetCfgIpDSCPValue must be specified if op_QosSetCfgIpDSCPValue is specified.
             :type val_c_QosSetCfgIpDSCPValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_QosSetCfgIpPrecedenceValue: The operator to apply to the field QosSetCfgIpPrecedenceValue. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. QosSetCfgIpPrecedenceValue: The precedence value of configuration IP address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_QosSetCfgIpPrecedenceValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_QosSetCfgIpPrecedenceValue: If op_QosSetCfgIpPrecedenceValue is specified, the field named in this input will be compared to the value in QosSetCfgIpPrecedenceValue using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_QosSetCfgIpPrecedenceValue must be specified if op_QosSetCfgIpPrecedenceValue is specified.
             :type val_f_QosSetCfgIpPrecedenceValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_QosSetCfgIpPrecedenceValue: If op_QosSetCfgIpPrecedenceValue is specified, this value will be compared to the value in QosSetCfgIpPrecedenceValue using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_QosSetCfgIpPrecedenceValue must be specified if op_QosSetCfgIpPrecedenceValue is specified.
             :type val_c_QosSetCfgIpPrecedenceValue: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_StartTime: The operator to apply to the field StartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. StartTime: The date and time the record is initially created in the NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param DeviceGroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the device qos stats with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the device qos stats with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
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
            |  ``default:`` DeviceQosID

             :param sort: The data field(s) to use for sorting the output. Default is DeviceQosID. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue.
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

             :param select: The list of attributes to return for each DeviceQosStat. Valid values are DeviceQosID, DeviceID, InterfaceID, StartTime, EndTime, QosPolicyIndex, QosObjectsIndex, QosConfigIndex, QosObjectsType, QosCMName, QosCMDesc, QosCMInfo, QosIfType, QosPolicyDirection, QosIfIndex, QosCMPrePolicyPkt, QosCMDropPkt, QosSetCfgIpDSCPValue, QosSetCfgIpPrecedenceValue. If empty or omitted, all attributes will be returned.
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

             :return device_qos_stats: An array of the DeviceQosStat objects that match the specified input criteria.
             :rtype device_qos_stats: Array of DeviceQosStat

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)
