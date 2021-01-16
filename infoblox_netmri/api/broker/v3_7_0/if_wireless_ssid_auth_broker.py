from ..broker import Broker


class IfWirelessSSIDAuthBroker(Broker):
    controller = "if_wireless_ssid_auths"

    def index(self, **kwargs):
        """Lists the available if wireless ssid auths. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless SSID information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless SSID information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Array of Integer

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

             :param timestamp: The data returned will represent the if wireless ssid auths as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid auth methods. The listed methods will be called on each if wireless ssid auth returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDAuthID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDAuthID. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm.
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

             :param select: The list of attributes to return for each IfWirelessSSIDAuth. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm. If empty or omitted, all attributes will be returned.
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

             :return if_wireless_ssid_auths: An array of the IfWirelessSSIDAuth objects that match the specified input criteria.
             :rtype if_wireless_ssid_auths: Array of IfWirelessSSIDAuth

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified if wireless ssid auth.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid auth methods. The listed methods will be called on each if wireless ssid auth returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return if_wireless_ssid_auth: The if wireless ssid auth identified by the specified IfWirelessSSIDAuthID.
             :rtype if_wireless_ssid_auth: IfWirelessSSIDAuth

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available if wireless ssid auths matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier for the device from which wireless SSID information was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless SSID information was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this Wireless SSID table entry.
             :type InterfaceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param InterfaceID: The internal NetMRI identifier for the local interface for this Wireless SSID table entry.
             :type InterfaceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAlgorithmIndex: The SSID algorithm index of the wireless SSID.
             :type SSIDAlgorithmIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAlgorithmIndex: The SSID algorithm index of the wireless SSID.
             :type SSIDAlgorithmIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAuthAlgorithm: The SSID Authentication algorithm in the interface wireless.
             :type SSIDAuthAlgorithm: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAuthAlgorithm: The SSID Authentication algorithm in the interface wireless.
             :type SSIDAuthAlgorithm: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAuthEnabledInd: A flag indicates SSID Authentication is enabled or not.
             :type SSIDAuthEnabledInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDAuthEnabledInd: A flag indicates SSID Authentication is enabled or not.
             :type SSIDAuthEnabledInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDDefaultVlanIndex: The default VLAN index of the local interface of the Wireless SSID.
             :type SSIDDefaultVlanIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDDefaultVlanIndex: The default VLAN index of the local interface of the Wireless SSID.
             :type SSIDDefaultVlanIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDEAPMethod: The Extensible Authentication Protocol Method is used in theWirelessSSIDAuth.
             :type SSIDEAPMethod: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDEAPMethod: The Extensible Authentication Protocol Method is used in theWirelessSSIDAuth.
             :type SSIDEAPMethod: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDEAPRequiredInd: A flag indicates whether a extensible authentication protocol is required or not.
             :type SSIDEAPRequiredInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDEAPRequiredInd: A flag indicates whether a extensible authentication protocol is required or not.
             :type SSIDEAPRequiredInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDIndex: The SSID index of the local interface for this Wireless SSID.
             :type SSIDIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDIndex: The SSID index of the local interface for this Wireless SSID.
             :type SSIDIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMACAuthMethod: The Media Access Controller(MAC) authentication method in the Wireless SSID.
             :type SSIDMACAuthMethod: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMACAuthMethod: The Media Access Controller(MAC) authentication method in the Wireless SSID.
             :type SSIDMACAuthMethod: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMACAuthRequiredInd: A flag indicates the SSID Media Access Controller(MAC) is required the authentication or not.
             :type SSIDMACAuthRequiredInd: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SSIDMACAuthRequiredInd: A flag indicates the SSID Media Access Controller(MAC) is required the authentication or not.
             :type SSIDMACAuthRequiredInd: Array of Boolean

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the VLAN.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifWirelessSSIDAuthChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type ifWirelessSSIDAuthChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifWirelessSSIDAuthEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthEndTime: The ending effective time of this record, or empty if still in effect.
             :type ifWirelessSSIDAuthEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthStartTime: The starting effective time of this record.
             :type ifWirelessSSIDAuthStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthStartTime: The starting effective time of this record.
             :type ifWirelessSSIDAuthStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthTimestamp: The date and time this record was collected or calculated.
             :type ifWirelessSSIDAuthTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ifWirelessSSIDAuthTimestamp: The date and time this record was collected or calculated.
             :type ifWirelessSSIDAuthTimestamp: Array of DateTime

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

             :param timestamp: The data returned will represent the if wireless ssid auths as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid auth methods. The listed methods will be called on each if wireless ssid auth returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDAuthID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDAuthID. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm.
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

             :param select: The list of attributes to return for each IfWirelessSSIDAuth. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against if wireless ssid auths, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, IfWirelessSSIDAuthID, InterfaceID, SSIDAlgorithmIndex, SSIDAuthAlgorithm, SSIDAuthEnabledInd, SSIDDefaultVlanIndex, SSIDEAPMethod, SSIDEAPRequiredInd, SSIDIndex, SSIDMACAuthMethod, SSIDMACAuthRequiredInd, VlanID, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthTimestamp.
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

             :return if_wireless_ssid_auths: An array of the IfWirelessSSIDAuth objects that match the specified input criteria.
             :rtype if_wireless_ssid_auths: Array of IfWirelessSSIDAuth

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available if wireless ssid auths matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, IfWirelessSSIDAuthID, InterfaceID, SSIDAlgorithmIndex, SSIDAuthAlgorithm, SSIDAuthEnabledInd, SSIDDefaultVlanIndex, SSIDEAPMethod, SSIDEAPRequiredInd, SSIDIndex, SSIDMACAuthMethod, SSIDMACAuthRequiredInd, VlanID, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthTimestamp.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which wireless SSID information was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_IfWirelessSSIDAuthID: The operator to apply to the field IfWirelessSSIDAuthID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_IfWirelessSSIDAuthID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_IfWirelessSSIDAuthID: If op_IfWirelessSSIDAuthID is specified, the field named in this input will be compared to the value in IfWirelessSSIDAuthID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_IfWirelessSSIDAuthID must be specified if op_IfWirelessSSIDAuthID is specified.
             :type val_f_IfWirelessSSIDAuthID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_IfWirelessSSIDAuthID: If op_IfWirelessSSIDAuthID is specified, this value will be compared to the value in IfWirelessSSIDAuthID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_IfWirelessSSIDAuthID must be specified if op_IfWirelessSSIDAuthID is specified.
             :type val_c_IfWirelessSSIDAuthID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_InterfaceID: The operator to apply to the field InterfaceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. InterfaceID: The internal NetMRI identifier for the local interface for this Wireless SSID table entry. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SSIDAlgorithmIndex: The operator to apply to the field SSIDAlgorithmIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDAlgorithmIndex: The SSID algorithm index of the wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDAlgorithmIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDAlgorithmIndex: If op_SSIDAlgorithmIndex is specified, the field named in this input will be compared to the value in SSIDAlgorithmIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDAlgorithmIndex must be specified if op_SSIDAlgorithmIndex is specified.
             :type val_f_SSIDAlgorithmIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDAlgorithmIndex: If op_SSIDAlgorithmIndex is specified, this value will be compared to the value in SSIDAlgorithmIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDAlgorithmIndex must be specified if op_SSIDAlgorithmIndex is specified.
             :type val_c_SSIDAlgorithmIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDAuthAlgorithm: The operator to apply to the field SSIDAuthAlgorithm. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDAuthAlgorithm: The SSID Authentication algorithm in the interface wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDAuthAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDAuthAlgorithm: If op_SSIDAuthAlgorithm is specified, the field named in this input will be compared to the value in SSIDAuthAlgorithm using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDAuthAlgorithm must be specified if op_SSIDAuthAlgorithm is specified.
             :type val_f_SSIDAuthAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDAuthAlgorithm: If op_SSIDAuthAlgorithm is specified, this value will be compared to the value in SSIDAuthAlgorithm using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDAuthAlgorithm must be specified if op_SSIDAuthAlgorithm is specified.
             :type val_c_SSIDAuthAlgorithm: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDAuthEnabledInd: The operator to apply to the field SSIDAuthEnabledInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDAuthEnabledInd: A flag indicates SSID Authentication is enabled or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDAuthEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDAuthEnabledInd: If op_SSIDAuthEnabledInd is specified, the field named in this input will be compared to the value in SSIDAuthEnabledInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDAuthEnabledInd must be specified if op_SSIDAuthEnabledInd is specified.
             :type val_f_SSIDAuthEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDAuthEnabledInd: If op_SSIDAuthEnabledInd is specified, this value will be compared to the value in SSIDAuthEnabledInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDAuthEnabledInd must be specified if op_SSIDAuthEnabledInd is specified.
             :type val_c_SSIDAuthEnabledInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDDefaultVlanIndex: The operator to apply to the field SSIDDefaultVlanIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDDefaultVlanIndex: The default VLAN index of the local interface of the Wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDDefaultVlanIndex: If op_SSIDDefaultVlanIndex is specified, the field named in this input will be compared to the value in SSIDDefaultVlanIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDDefaultVlanIndex must be specified if op_SSIDDefaultVlanIndex is specified.
             :type val_f_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDDefaultVlanIndex: If op_SSIDDefaultVlanIndex is specified, this value will be compared to the value in SSIDDefaultVlanIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDDefaultVlanIndex must be specified if op_SSIDDefaultVlanIndex is specified.
             :type val_c_SSIDDefaultVlanIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDEAPMethod: The operator to apply to the field SSIDEAPMethod. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDEAPMethod: The Extensible Authentication Protocol Method is used in theWirelessSSIDAuth. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDEAPMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDEAPMethod: If op_SSIDEAPMethod is specified, the field named in this input will be compared to the value in SSIDEAPMethod using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDEAPMethod must be specified if op_SSIDEAPMethod is specified.
             :type val_f_SSIDEAPMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDEAPMethod: If op_SSIDEAPMethod is specified, this value will be compared to the value in SSIDEAPMethod using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDEAPMethod must be specified if op_SSIDEAPMethod is specified.
             :type val_c_SSIDEAPMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDEAPRequiredInd: The operator to apply to the field SSIDEAPRequiredInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDEAPRequiredInd: A flag indicates whether a extensible authentication protocol is required or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDEAPRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDEAPRequiredInd: If op_SSIDEAPRequiredInd is specified, the field named in this input will be compared to the value in SSIDEAPRequiredInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDEAPRequiredInd must be specified if op_SSIDEAPRequiredInd is specified.
             :type val_f_SSIDEAPRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDEAPRequiredInd: If op_SSIDEAPRequiredInd is specified, this value will be compared to the value in SSIDEAPRequiredInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDEAPRequiredInd must be specified if op_SSIDEAPRequiredInd is specified.
             :type val_c_SSIDEAPRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDIndex: The operator to apply to the field SSIDIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDIndex: The SSID index of the local interface for this Wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDIndex: If op_SSIDIndex is specified, the field named in this input will be compared to the value in SSIDIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDIndex must be specified if op_SSIDIndex is specified.
             :type val_f_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDIndex: If op_SSIDIndex is specified, this value will be compared to the value in SSIDIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDIndex must be specified if op_SSIDIndex is specified.
             :type val_c_SSIDIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDMACAuthMethod: The operator to apply to the field SSIDMACAuthMethod. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDMACAuthMethod: The Media Access Controller(MAC) authentication method in the Wireless SSID. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDMACAuthMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDMACAuthMethod: If op_SSIDMACAuthMethod is specified, the field named in this input will be compared to the value in SSIDMACAuthMethod using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDMACAuthMethod must be specified if op_SSIDMACAuthMethod is specified.
             :type val_f_SSIDMACAuthMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDMACAuthMethod: If op_SSIDMACAuthMethod is specified, this value will be compared to the value in SSIDMACAuthMethod using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDMACAuthMethod must be specified if op_SSIDMACAuthMethod is specified.
             :type val_c_SSIDMACAuthMethod: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SSIDMACAuthRequiredInd: The operator to apply to the field SSIDMACAuthRequiredInd. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SSIDMACAuthRequiredInd: A flag indicates the SSID Media Access Controller(MAC) is required the authentication or not. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SSIDMACAuthRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SSIDMACAuthRequiredInd: If op_SSIDMACAuthRequiredInd is specified, the field named in this input will be compared to the value in SSIDMACAuthRequiredInd using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SSIDMACAuthRequiredInd must be specified if op_SSIDMACAuthRequiredInd is specified.
             :type val_f_SSIDMACAuthRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SSIDMACAuthRequiredInd: If op_SSIDMACAuthRequiredInd is specified, this value will be compared to the value in SSIDMACAuthRequiredInd using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SSIDMACAuthRequiredInd must be specified if op_SSIDMACAuthRequiredInd is specified.
             :type val_c_SSIDMACAuthRequiredInd: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier of the VLAN. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_VlanID: If op_VlanID is specified, the field named in this input will be compared to the value in VlanID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_VlanID must be specified if op_VlanID is specified.
             :type val_f_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_VlanID: If op_VlanID is specified, this value will be compared to the value in VlanID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_VlanID must be specified if op_VlanID is specified.
             :type val_c_VlanID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDAuthChangedCols: The operator to apply to the field ifWirelessSSIDAuthChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDAuthChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDAuthChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDAuthChangedCols: If op_ifWirelessSSIDAuthChangedCols is specified, the field named in this input will be compared to the value in ifWirelessSSIDAuthChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDAuthChangedCols must be specified if op_ifWirelessSSIDAuthChangedCols is specified.
             :type val_f_ifWirelessSSIDAuthChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDAuthChangedCols: If op_ifWirelessSSIDAuthChangedCols is specified, this value will be compared to the value in ifWirelessSSIDAuthChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDAuthChangedCols must be specified if op_ifWirelessSSIDAuthChangedCols is specified.
             :type val_c_ifWirelessSSIDAuthChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDAuthEndTime: The operator to apply to the field ifWirelessSSIDAuthEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDAuthEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDAuthEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDAuthEndTime: If op_ifWirelessSSIDAuthEndTime is specified, the field named in this input will be compared to the value in ifWirelessSSIDAuthEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDAuthEndTime must be specified if op_ifWirelessSSIDAuthEndTime is specified.
             :type val_f_ifWirelessSSIDAuthEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDAuthEndTime: If op_ifWirelessSSIDAuthEndTime is specified, this value will be compared to the value in ifWirelessSSIDAuthEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDAuthEndTime must be specified if op_ifWirelessSSIDAuthEndTime is specified.
             :type val_c_ifWirelessSSIDAuthEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDAuthStartTime: The operator to apply to the field ifWirelessSSIDAuthStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDAuthStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDAuthStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDAuthStartTime: If op_ifWirelessSSIDAuthStartTime is specified, the field named in this input will be compared to the value in ifWirelessSSIDAuthStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDAuthStartTime must be specified if op_ifWirelessSSIDAuthStartTime is specified.
             :type val_f_ifWirelessSSIDAuthStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDAuthStartTime: If op_ifWirelessSSIDAuthStartTime is specified, this value will be compared to the value in ifWirelessSSIDAuthStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDAuthStartTime must be specified if op_ifWirelessSSIDAuthStartTime is specified.
             :type val_c_ifWirelessSSIDAuthStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_ifWirelessSSIDAuthTimestamp: The operator to apply to the field ifWirelessSSIDAuthTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. ifWirelessSSIDAuthTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_ifWirelessSSIDAuthTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_ifWirelessSSIDAuthTimestamp: If op_ifWirelessSSIDAuthTimestamp is specified, the field named in this input will be compared to the value in ifWirelessSSIDAuthTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_ifWirelessSSIDAuthTimestamp must be specified if op_ifWirelessSSIDAuthTimestamp is specified.
             :type val_f_ifWirelessSSIDAuthTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_ifWirelessSSIDAuthTimestamp: If op_ifWirelessSSIDAuthTimestamp is specified, this value will be compared to the value in ifWirelessSSIDAuthTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_ifWirelessSSIDAuthTimestamp must be specified if op_ifWirelessSSIDAuthTimestamp is specified.
             :type val_c_ifWirelessSSIDAuthTimestamp: String

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

             :param timestamp: The data returned will represent the if wireless ssid auths as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of if wireless ssid auth methods. The listed methods will be called on each if wireless ssid auth returned and included in the output. Available methods are: device, interface, vlan.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: device, interface, vlan.
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
            |  ``default:`` IfWirelessSSIDAuthID

             :param sort: The data field(s) to use for sorting the output. Default is IfWirelessSSIDAuthID. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm.
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

             :param select: The list of attributes to return for each IfWirelessSSIDAuth. Valid values are IfWirelessSSIDAuthID, DataSourceID, DeviceID, InterfaceID, ifWirelessSSIDAuthStartTime, ifWirelessSSIDAuthEndTime, ifWirelessSSIDAuthChangedCols, ifWirelessSSIDAuthTimestamp, SSIDIndex, SSIDAlgorithmIndex, SSIDAuthEnabledInd, SSIDEAPRequiredInd, SSIDEAPMethod, SSIDMACAuthRequiredInd, SSIDMACAuthMethod, SSIDDefaultVlanIndex, VlanID, SSIDAuthAlgorithm. If empty or omitted, all attributes will be returned.
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

             :return if_wireless_ssid_auths: An array of the IfWirelessSSIDAuth objects that match the specified input criteria.
             :rtype if_wireless_ssid_auths: Array of IfWirelessSSIDAuth

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

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

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def interface(self, **kwargs):
        """interface

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : interface
             :rtype : Interface

            """

        return self.api_request(self._get_method_fullname("interface"), kwargs)

    def vlan(self, **kwargs):
        """vlan

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : vlan
             :rtype : Vlan

            """

        return self.api_request(self._get_method_fullname("vlan"), kwargs)

    def infradevice(self, **kwargs):
        """The device from which this data was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IfWirelessSSIDAuthID: The internal NetMRI identifier of the Wireless SSID Authentication.
             :type IfWirelessSSIDAuthID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
