from ..broker import Broker


class WirelessSubordinateBroker(Broker):
    controller = "wireless_subordinates"

    def index(self, **kwargs):
        """Lists the available wireless subordinates. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless subordinates was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless subordinates was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Array of Integer

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

             :param timestamp: The data returned will represent the wireless subordinates as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of wireless subordinate methods. The listed methods will be called on each wireless subordinate returned and included in the output. Available methods are: data_source, device, vlan, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, vlan.
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
            |  ``default:`` WirelessSubordinantID

             :param sort: The data field(s) to use for sorting the output. Default is WirelessSubordinantID. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion.
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

             :param select: The list of attributes to return for each WirelessSubordinate. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion. If empty or omitted, all attributes will be returned.
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

             :return wireless_subordinates: An array of the WirelessSubordinate objects that match the specified input criteria.
             :rtype wireless_subordinates: Array of WirelessSubordinate

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified wireless subordinate.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of wireless subordinate methods. The listed methods will be called on each wireless subordinate returned and included in the output. Available methods are: data_source, device, vlan, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, vlan.
             :type include: Array of String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return wireless_subordinate: The wireless subordinate identified by the specified WirelessSubordinantID.
             :rtype wireless_subordinate: WirelessSubordinate

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available wireless subordinates matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

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

             :param DeviceID: The internal NetMRI identifier for the device from which wireless subordinates was collected.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device from which wireless subordinates was collected.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubAdminStatus: The configured status(up/down) of the interface.
             :type SubAdminStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubAdminStatus: The configured status(up/down) of the interface.
             :type SubAdminStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubBootVersion: The boot version of the wireless subordinate is running on this device.
             :type SubBootVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubBootVersion: The boot version of the wireless subordinate is running on this device.
             :type SubBootVersion: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type SubChangedCols: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubDeviceID: The internal NetMRI identifier of each wireless subordinate device.
             :type SubDeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubDeviceID: The internal NetMRI identifier of each wireless subordinate device.
             :type SubDeviceID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubEndTime: The ending effective date and time of this record was collected or calculated, or empty if still in effect.
             :type SubEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubEndTime: The ending effective date and time of this record was collected or calculated, or empty if still in effect.
             :type SubEndTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubGroupVlanName: The Vlan name of the wireless subordinate group.
             :type SubGroupVlanName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubGroupVlanName: The Vlan name of the wireless subordinate group.
             :type SubGroupVlanName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubIPDotted: The management IP address of the wireless subordinate in dotted,(or colon delimited for IPv6) format.
             :type SubIPDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubIPDotted: The management IP address of the wireless subordinate in dotted,(or colon delimited for IPv6) format.
             :type SubIPDotted: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubIPNumeric: The numerical value of the wireless IP Address.
             :type SubIPNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubIPNumeric: The numerical value of the wireless IP Address.
             :type SubIPNumeric: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubLocation: The location as reported by the wireless.
             :type SubLocation: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubLocation: The location as reported by the wireless.
             :type SubLocation: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubMac: The Media Access Controller(MAC) address of the end host.
             :type SubMac: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubMac: The Media Access Controller(MAC) address of the end host.
             :type SubMac: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubModel: The wireless subordinate model name.
             :type SubModel: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubModel: The wireless subordinate model name.
             :type SubModel: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubMonitorOnlyMode: The mode operation of wireless is monitored in the NetMRI.
             :type SubMonitorOnlyMode: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubMonitorOnlyMode: The mode operation of wireless is monitored in the NetMRI.
             :type SubMonitorOnlyMode: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubName: The name of the wireless subordinates defined within NetMRI.
             :type SubName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubName: The name of the wireless subordinates defined within NetMRI.
             :type SubName: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubNumOfSlots: The required number of slots available in the wireless subordinates.
             :type SubNumOfSlots: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubNumOfSlots: The required number of slots available in the wireless subordinates.
             :type SubNumOfSlots: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubOSVersion: The operating system version of the wireless subordinate is running on this device.
             :type SubOSVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubOSVersion: The operating system version of the wireless subordinate is running on this device.
             :type SubOSVersion: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubOperationStatus: The operational status(up/down) of the wireless.
             :type SubOperationStatus: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubOperationStatus: The operational status(up/down) of the wireless.
             :type SubOperationStatus: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubSerialNumber: The vendor-specific serial number string for the wireless subordinates.The preferred value is the serial number string actually printed on the component itself(if present).
             :type SubSerialNumber: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubSerialNumber: The vendor-specific serial number string for the wireless subordinates.The preferred value is the serial number string actually printed on the component itself(if present).
             :type SubSerialNumber: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubSoftwareVersion: The software version is running on this device.
             :type SubSoftwareVersion: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubSoftwareVersion: The software version is running on this device.
             :type SubSoftwareVersion: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubStartTime: The starting effective date and time this record was collected or calculated.
             :type SubStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubStartTime: The starting effective date and time this record was collected or calculated.
             :type SubStartTime: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubTimestamp: The date and time this record was collected or calculated.
             :type SubTimestamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubTimestamp: The date and time this record was collected or calculated.
             :type SubTimestamp: Array of DateTime

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param SubType: The NetMRI-determined subordinate type of the wireless.
             :type SubType: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param SubType: The NetMRI-determined subordinate type of the wireless.
             :type SubType: Array of String

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the Vlan.
             :type VlanID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param VlanID: The internal NetMRI identifier of the Vlan.
             :type VlanID: Array of Integer

            |  ``api version min:`` 2.3
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Array of Integer

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

             :param timestamp: The data returned will represent the wireless subordinates as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of wireless subordinate methods. The listed methods will be called on each wireless subordinate returned and included in the output. Available methods are: data_source, device, vlan, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, vlan.
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
            |  ``default:`` WirelessSubordinantID

             :param sort: The data field(s) to use for sorting the output. Default is WirelessSubordinantID. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion.
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

             :param select: The list of attributes to return for each WirelessSubordinate. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against wireless subordinates, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, SubAdminStatus, SubBootVersion, SubChangedCols, SubDeviceID, SubEndTime, SubGroupVlanName, SubIPDotted, SubIPNumeric, SubLocation, SubMac, SubModel, SubMonitorOnlyMode, SubName, SubNumOfSlots, SubOSVersion, SubOperationStatus, SubSerialNumber, SubSoftwareVersion, SubStartTime, SubTimestamp, SubType, VlanID, WirelessSubordinantID.
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

             :return wireless_subordinates: An array of the WirelessSubordinate objects that match the specified input criteria.
             :rtype wireless_subordinates: Array of WirelessSubordinate

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available wireless subordinates matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, SubAdminStatus, SubBootVersion, SubChangedCols, SubDeviceID, SubEndTime, SubGroupVlanName, SubIPDotted, SubIPNumeric, SubLocation, SubMac, SubModel, SubMonitorOnlyMode, SubName, SubNumOfSlots, SubOSVersion, SubOperationStatus, SubSerialNumber, SubSoftwareVersion, SubStartTime, SubTimestamp, SubType, VlanID, WirelessSubordinantID.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier for the device from which wireless subordinates was collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_SubAdminStatus: The operator to apply to the field SubAdminStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubAdminStatus: The configured status(up/down) of the interface. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubAdminStatus: If op_SubAdminStatus is specified, the field named in this input will be compared to the value in SubAdminStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubAdminStatus must be specified if op_SubAdminStatus is specified.
             :type val_f_SubAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubAdminStatus: If op_SubAdminStatus is specified, this value will be compared to the value in SubAdminStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubAdminStatus must be specified if op_SubAdminStatus is specified.
             :type val_c_SubAdminStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubBootVersion: The operator to apply to the field SubBootVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubBootVersion: The boot version of the wireless subordinate is running on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubBootVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubBootVersion: If op_SubBootVersion is specified, the field named in this input will be compared to the value in SubBootVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubBootVersion must be specified if op_SubBootVersion is specified.
             :type val_f_SubBootVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubBootVersion: If op_SubBootVersion is specified, this value will be compared to the value in SubBootVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubBootVersion must be specified if op_SubBootVersion is specified.
             :type val_c_SubBootVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubChangedCols: The operator to apply to the field SubChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubChangedCols: If op_SubChangedCols is specified, the field named in this input will be compared to the value in SubChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubChangedCols must be specified if op_SubChangedCols is specified.
             :type val_f_SubChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubChangedCols: If op_SubChangedCols is specified, this value will be compared to the value in SubChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubChangedCols must be specified if op_SubChangedCols is specified.
             :type val_c_SubChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubDeviceID: The operator to apply to the field SubDeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubDeviceID: The internal NetMRI identifier of each wireless subordinate device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubDeviceID: If op_SubDeviceID is specified, the field named in this input will be compared to the value in SubDeviceID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubDeviceID must be specified if op_SubDeviceID is specified.
             :type val_f_SubDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubDeviceID: If op_SubDeviceID is specified, this value will be compared to the value in SubDeviceID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubDeviceID must be specified if op_SubDeviceID is specified.
             :type val_c_SubDeviceID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubEndTime: The operator to apply to the field SubEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubEndTime: The ending effective date and time of this record was collected or calculated, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubEndTime: If op_SubEndTime is specified, the field named in this input will be compared to the value in SubEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubEndTime must be specified if op_SubEndTime is specified.
             :type val_f_SubEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubEndTime: If op_SubEndTime is specified, this value will be compared to the value in SubEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubEndTime must be specified if op_SubEndTime is specified.
             :type val_c_SubEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubGroupVlanName: The operator to apply to the field SubGroupVlanName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubGroupVlanName: The Vlan name of the wireless subordinate group. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubGroupVlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubGroupVlanName: If op_SubGroupVlanName is specified, the field named in this input will be compared to the value in SubGroupVlanName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubGroupVlanName must be specified if op_SubGroupVlanName is specified.
             :type val_f_SubGroupVlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubGroupVlanName: If op_SubGroupVlanName is specified, this value will be compared to the value in SubGroupVlanName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubGroupVlanName must be specified if op_SubGroupVlanName is specified.
             :type val_c_SubGroupVlanName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubIPDotted: The operator to apply to the field SubIPDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubIPDotted: The management IP address of the wireless subordinate in dotted,(or colon delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubIPDotted: If op_SubIPDotted is specified, the field named in this input will be compared to the value in SubIPDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubIPDotted must be specified if op_SubIPDotted is specified.
             :type val_f_SubIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubIPDotted: If op_SubIPDotted is specified, this value will be compared to the value in SubIPDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubIPDotted must be specified if op_SubIPDotted is specified.
             :type val_c_SubIPDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubIPNumeric: The operator to apply to the field SubIPNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubIPNumeric: The numerical value of the wireless IP Address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubIPNumeric: If op_SubIPNumeric is specified, the field named in this input will be compared to the value in SubIPNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubIPNumeric must be specified if op_SubIPNumeric is specified.
             :type val_f_SubIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubIPNumeric: If op_SubIPNumeric is specified, this value will be compared to the value in SubIPNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubIPNumeric must be specified if op_SubIPNumeric is specified.
             :type val_c_SubIPNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubLocation: The operator to apply to the field SubLocation. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubLocation: The location as reported by the wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubLocation: If op_SubLocation is specified, the field named in this input will be compared to the value in SubLocation using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubLocation must be specified if op_SubLocation is specified.
             :type val_f_SubLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubLocation: If op_SubLocation is specified, this value will be compared to the value in SubLocation using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubLocation must be specified if op_SubLocation is specified.
             :type val_c_SubLocation: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubMac: The operator to apply to the field SubMac. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubMac: The Media Access Controller(MAC) address of the end host. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubMac: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubMac: If op_SubMac is specified, the field named in this input will be compared to the value in SubMac using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubMac must be specified if op_SubMac is specified.
             :type val_f_SubMac: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubMac: If op_SubMac is specified, this value will be compared to the value in SubMac using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubMac must be specified if op_SubMac is specified.
             :type val_c_SubMac: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubModel: The operator to apply to the field SubModel. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubModel: The wireless subordinate model name. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubModel: If op_SubModel is specified, the field named in this input will be compared to the value in SubModel using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubModel must be specified if op_SubModel is specified.
             :type val_f_SubModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubModel: If op_SubModel is specified, this value will be compared to the value in SubModel using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubModel must be specified if op_SubModel is specified.
             :type val_c_SubModel: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubMonitorOnlyMode: The operator to apply to the field SubMonitorOnlyMode. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubMonitorOnlyMode: The mode operation of wireless is monitored in the NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubMonitorOnlyMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubMonitorOnlyMode: If op_SubMonitorOnlyMode is specified, the field named in this input will be compared to the value in SubMonitorOnlyMode using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubMonitorOnlyMode must be specified if op_SubMonitorOnlyMode is specified.
             :type val_f_SubMonitorOnlyMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubMonitorOnlyMode: If op_SubMonitorOnlyMode is specified, this value will be compared to the value in SubMonitorOnlyMode using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubMonitorOnlyMode must be specified if op_SubMonitorOnlyMode is specified.
             :type val_c_SubMonitorOnlyMode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubName: The operator to apply to the field SubName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubName: The name of the wireless subordinates defined within NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubName: If op_SubName is specified, the field named in this input will be compared to the value in SubName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubName must be specified if op_SubName is specified.
             :type val_f_SubName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubName: If op_SubName is specified, this value will be compared to the value in SubName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubName must be specified if op_SubName is specified.
             :type val_c_SubName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubNumOfSlots: The operator to apply to the field SubNumOfSlots. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubNumOfSlots: The required number of slots available in the wireless subordinates. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubNumOfSlots: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubNumOfSlots: If op_SubNumOfSlots is specified, the field named in this input will be compared to the value in SubNumOfSlots using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubNumOfSlots must be specified if op_SubNumOfSlots is specified.
             :type val_f_SubNumOfSlots: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubNumOfSlots: If op_SubNumOfSlots is specified, this value will be compared to the value in SubNumOfSlots using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubNumOfSlots must be specified if op_SubNumOfSlots is specified.
             :type val_c_SubNumOfSlots: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubOSVersion: The operator to apply to the field SubOSVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubOSVersion: The operating system version of the wireless subordinate is running on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubOSVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubOSVersion: If op_SubOSVersion is specified, the field named in this input will be compared to the value in SubOSVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubOSVersion must be specified if op_SubOSVersion is specified.
             :type val_f_SubOSVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubOSVersion: If op_SubOSVersion is specified, this value will be compared to the value in SubOSVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubOSVersion must be specified if op_SubOSVersion is specified.
             :type val_c_SubOSVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubOperationStatus: The operator to apply to the field SubOperationStatus. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubOperationStatus: The operational status(up/down) of the wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubOperationStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubOperationStatus: If op_SubOperationStatus is specified, the field named in this input will be compared to the value in SubOperationStatus using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubOperationStatus must be specified if op_SubOperationStatus is specified.
             :type val_f_SubOperationStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubOperationStatus: If op_SubOperationStatus is specified, this value will be compared to the value in SubOperationStatus using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubOperationStatus must be specified if op_SubOperationStatus is specified.
             :type val_c_SubOperationStatus: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubSerialNumber: The operator to apply to the field SubSerialNumber. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubSerialNumber: The vendor-specific serial number string for the wireless subordinates.The preferred value is the serial number string actually printed on the component itself(if present). For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubSerialNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubSerialNumber: If op_SubSerialNumber is specified, the field named in this input will be compared to the value in SubSerialNumber using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubSerialNumber must be specified if op_SubSerialNumber is specified.
             :type val_f_SubSerialNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubSerialNumber: If op_SubSerialNumber is specified, this value will be compared to the value in SubSerialNumber using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubSerialNumber must be specified if op_SubSerialNumber is specified.
             :type val_c_SubSerialNumber: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubSoftwareVersion: The operator to apply to the field SubSoftwareVersion. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubSoftwareVersion: The software version is running on this device. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubSoftwareVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubSoftwareVersion: If op_SubSoftwareVersion is specified, the field named in this input will be compared to the value in SubSoftwareVersion using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubSoftwareVersion must be specified if op_SubSoftwareVersion is specified.
             :type val_f_SubSoftwareVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubSoftwareVersion: If op_SubSoftwareVersion is specified, this value will be compared to the value in SubSoftwareVersion using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubSoftwareVersion must be specified if op_SubSoftwareVersion is specified.
             :type val_c_SubSoftwareVersion: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubStartTime: The operator to apply to the field SubStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubStartTime: The starting effective date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubStartTime: If op_SubStartTime is specified, the field named in this input will be compared to the value in SubStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubStartTime must be specified if op_SubStartTime is specified.
             :type val_f_SubStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubStartTime: If op_SubStartTime is specified, this value will be compared to the value in SubStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubStartTime must be specified if op_SubStartTime is specified.
             :type val_c_SubStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubTimestamp: The operator to apply to the field SubTimestamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubTimestamp: The date and time this record was collected or calculated. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubTimestamp: If op_SubTimestamp is specified, the field named in this input will be compared to the value in SubTimestamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubTimestamp must be specified if op_SubTimestamp is specified.
             :type val_f_SubTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubTimestamp: If op_SubTimestamp is specified, this value will be compared to the value in SubTimestamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubTimestamp must be specified if op_SubTimestamp is specified.
             :type val_c_SubTimestamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_SubType: The operator to apply to the field SubType. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. SubType: The NetMRI-determined subordinate type of the wireless. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_SubType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_SubType: If op_SubType is specified, the field named in this input will be compared to the value in SubType using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_SubType must be specified if op_SubType is specified.
             :type val_f_SubType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_SubType: If op_SubType is specified, this value will be compared to the value in SubType using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_SubType must be specified if op_SubType is specified.
             :type val_c_SubType: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_VlanID: The operator to apply to the field VlanID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. VlanID: The internal NetMRI identifier of the Vlan. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_WirelessSubordinantID: The operator to apply to the field WirelessSubordinantID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_WirelessSubordinantID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_WirelessSubordinantID: If op_WirelessSubordinantID is specified, the field named in this input will be compared to the value in WirelessSubordinantID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_WirelessSubordinantID must be specified if op_WirelessSubordinantID is specified.
             :type val_f_WirelessSubordinantID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_WirelessSubordinantID: If op_WirelessSubordinantID is specified, this value will be compared to the value in WirelessSubordinantID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_WirelessSubordinantID must be specified if op_WirelessSubordinantID is specified.
             :type val_c_WirelessSubordinantID: String

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

             :param timestamp: The data returned will represent the wireless subordinates as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of wireless subordinate methods. The listed methods will be called on each wireless subordinate returned and included in the output. Available methods are: data_source, device, vlan, infradevice.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include: A list of associated object types to include in the output. The listed associations will be returned as outputs named according to the association name (see outputs below). Available includes are: data_source, device, vlan.
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
            |  ``default:`` WirelessSubordinantID

             :param sort: The data field(s) to use for sorting the output. Default is WirelessSubordinantID. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion.
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

             :param select: The list of attributes to return for each WirelessSubordinate. Valid values are WirelessSubordinantID, DataSourceID, DeviceID, SubStartTime, SubEndTime, SubChangedCols, SubTimestamp, SubMac, SubDeviceID, SubNumOfSlots, SubName, SubLocation, SubMonitorOnlyMode, SubOperationStatus, SubSoftwareVersion, SubBootVersion, SubModel, SubSerialNumber, SubIPNumeric, SubIPDotted, SubType, SubGroupVlanName, VlanID, SubAdminStatus, SubOSVersion. If empty or omitted, all attributes will be returned.
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

             :return wireless_subordinates: An array of the WirelessSubordinate objects that match the specified input criteria.
             :rtype wireless_subordinates: Array of WirelessSubordinate

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

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

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : Device

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)

    def vlan(self, **kwargs):
        """vlan

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

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

             :param WirelessSubordinantID: The internal NetMRI identifier of the WirelessSubordinantID
             :type WirelessSubordinantID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
