from ..broker import Broker


class NetscreenAddressBroker(Broker):
    controller = "netscreen_addresses"

    def index(self, **kwargs):
        """Lists the available netscreen addresses. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen address table entry was found.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen address table entry was found.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Array of Integer

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

             :param timestamp: The data returned will represent the netscreen addresses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen address methods. The listed methods will be called on each netscreen address returned and included in the output. Available methods are: device.
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
            |  ``default:`` NSAddressID

             :param sort: The data field(s) to use for sorting the output. Default is NSAddressID. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each NetscreenAddress. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return netscreen_addresses: An array of the NetscreenAddress objects that match the specified input criteria.
             :rtype netscreen_addresses: Array of NetscreenAddress

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified netscreen address.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen address methods. The listed methods will be called on each netscreen address returned and included in the output. Available methods are: device.
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

             :return netscreen_address: The netscreen address identified by the specified NSAddressID.
             :rtype netscreen_address: NetscreenAddress

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def search(self, **kwargs):
        """Lists the available netscreen addresses matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

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

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen address table entry was found.
             :type DeviceID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of each device from which netscreen address table entry was found.
             :type DeviceID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NSAddressChangedCols: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressChangedCols: The fields that changed between this revision of the record and the previous revision.
             :type NSAddressChangedCols: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressDomainDotted: The management Domain IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
             :type NSAddressDomainDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressDomainDotted: The management Domain IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
             :type NSAddressDomainDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressDomainNumeric: The numerical value of Domain IP address in the netscreen address.
             :type NSAddressDomainNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressDomainNumeric: The numerical value of Domain IP address in the netscreen address.
             :type NSAddressDomainNumeric: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressEndTime: The ending effective time of this record, or empty if still in effect.
             :type NSAddressEndTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressEndTime: The ending effective time of this record, or empty if still in effect.
             :type NSAddressEndTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIndex: The current index value of the local interface for the netscreen address.
             :type NSAddressIndex: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIndex: The current index value of the local interface for the netscreen address.
             :type NSAddressIndex: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIpDotted: The management IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
             :type NSAddressIpDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIpDotted: The management IP address of the netscreen address is dotted(or colon delimited for IPv6) format.
             :type NSAddressIpDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIpNumeric: The numerical value of the remote IP address in the netscreen address.
             :type NSAddressIpNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressIpNumeric: The numerical value of the remote IP address in the netscreen address.
             :type NSAddressIpNumeric: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressName: The name of the netscreen address.
             :type NSAddressName: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressName: The name of the netscreen address.
             :type NSAddressName: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressNetmaskDotted: The management netmask IP address of netscreen address is dotted (or colon delimited for IPv6) format.
             :type NSAddressNetmaskDotted: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressNetmaskDotted: The management netmask IP address of netscreen address is dotted (or colon delimited for IPv6) format.
             :type NSAddressNetmaskDotted: Array of String

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressNetmaskNumeric: The numerical value of netmask in the netscreen address.
             :type NSAddressNetmaskNumeric: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressNetmaskNumeric: The numerical value of netmask in the netscreen address.
             :type NSAddressNetmaskNumeric: Array of Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressStartTime: The starting effective time of this record.
             :type NSAddressStartTime: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressStartTime: The starting effective time of this record.
             :type NSAddressStartTime: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressTimeStamp: The date and time of netscreen address was calculated or collected.
             :type NSAddressTimeStamp: DateTime

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressTimeStamp: The date and time of netscreen address was calculated or collected.
             :type NSAddressTimeStamp: Array of DateTime

            |  ``api version min:`` 2.4
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressZone: The zone of the netscreen address.
             :type NSAddressZone: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param NSAddressZone: The zone of the netscreen address.
             :type NSAddressZone: Array of String

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

             :param timestamp: The data returned will represent the netscreen addresses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen address methods. The listed methods will be called on each netscreen address returned and included in the output. Available methods are: device.
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
            |  ``default:`` NSAddressID

             :param sort: The data field(s) to use for sorting the output. Default is NSAddressID. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each NetscreenAddress. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :param query: This value will be matched against netscreen addresses, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DataSourceID, DeviceID, NSAddressChangedCols, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressEndTime, NSAddressID, NSAddressIndex, NSAddressIpDotted, NSAddressIpNumeric, NSAddressName, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, NSAddressStartTime, NSAddressTimeStamp, NSAddressZone.
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

             :return netscreen_addresses: An array of the NetscreenAddress objects that match the specified input criteria.
             :rtype netscreen_addresses: Array of NetscreenAddress

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available netscreen addresses matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DataSourceID, DeviceID, NSAddressChangedCols, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressEndTime, NSAddressID, NSAddressIndex, NSAddressIpDotted, NSAddressIpNumeric, NSAddressName, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, NSAddressStartTime, NSAddressTimeStamp, NSAddressZone.

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

             :param op_DeviceID: The operator to apply to the field DeviceID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceID: The internal NetMRI identifier of each device from which netscreen address table entry was found. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
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

             :param op_NSAddressChangedCols: The operator to apply to the field NSAddressChangedCols. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressChangedCols: The fields that changed between this revision of the record and the previous revision. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressChangedCols: If op_NSAddressChangedCols is specified, the field named in this input will be compared to the value in NSAddressChangedCols using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressChangedCols must be specified if op_NSAddressChangedCols is specified.
             :type val_f_NSAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressChangedCols: If op_NSAddressChangedCols is specified, this value will be compared to the value in NSAddressChangedCols using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressChangedCols must be specified if op_NSAddressChangedCols is specified.
             :type val_c_NSAddressChangedCols: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressDomainDotted: The operator to apply to the field NSAddressDomainDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressDomainDotted: The management Domain IP address of the netscreen address is dotted(or colon delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressDomainDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressDomainDotted: If op_NSAddressDomainDotted is specified, the field named in this input will be compared to the value in NSAddressDomainDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressDomainDotted must be specified if op_NSAddressDomainDotted is specified.
             :type val_f_NSAddressDomainDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressDomainDotted: If op_NSAddressDomainDotted is specified, this value will be compared to the value in NSAddressDomainDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressDomainDotted must be specified if op_NSAddressDomainDotted is specified.
             :type val_c_NSAddressDomainDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressDomainNumeric: The operator to apply to the field NSAddressDomainNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressDomainNumeric: The numerical value of Domain IP address in the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressDomainNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressDomainNumeric: If op_NSAddressDomainNumeric is specified, the field named in this input will be compared to the value in NSAddressDomainNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressDomainNumeric must be specified if op_NSAddressDomainNumeric is specified.
             :type val_f_NSAddressDomainNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressDomainNumeric: If op_NSAddressDomainNumeric is specified, this value will be compared to the value in NSAddressDomainNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressDomainNumeric must be specified if op_NSAddressDomainNumeric is specified.
             :type val_c_NSAddressDomainNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressEndTime: The operator to apply to the field NSAddressEndTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressEndTime: The ending effective time of this record, or empty if still in effect. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressEndTime: If op_NSAddressEndTime is specified, the field named in this input will be compared to the value in NSAddressEndTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressEndTime must be specified if op_NSAddressEndTime is specified.
             :type val_f_NSAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressEndTime: If op_NSAddressEndTime is specified, this value will be compared to the value in NSAddressEndTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressEndTime must be specified if op_NSAddressEndTime is specified.
             :type val_c_NSAddressEndTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressID: The operator to apply to the field NSAddressID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressID: The internal NetMRI identifier of netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressID: If op_NSAddressID is specified, the field named in this input will be compared to the value in NSAddressID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressID must be specified if op_NSAddressID is specified.
             :type val_f_NSAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressID: If op_NSAddressID is specified, this value will be compared to the value in NSAddressID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressID must be specified if op_NSAddressID is specified.
             :type val_c_NSAddressID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressIndex: The operator to apply to the field NSAddressIndex. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressIndex: The current index value of the local interface for the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressIndex: If op_NSAddressIndex is specified, the field named in this input will be compared to the value in NSAddressIndex using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressIndex must be specified if op_NSAddressIndex is specified.
             :type val_f_NSAddressIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressIndex: If op_NSAddressIndex is specified, this value will be compared to the value in NSAddressIndex using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressIndex must be specified if op_NSAddressIndex is specified.
             :type val_c_NSAddressIndex: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressIpDotted: The operator to apply to the field NSAddressIpDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressIpDotted: The management IP address of the netscreen address is dotted(or colon delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressIpDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressIpDotted: If op_NSAddressIpDotted is specified, the field named in this input will be compared to the value in NSAddressIpDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressIpDotted must be specified if op_NSAddressIpDotted is specified.
             :type val_f_NSAddressIpDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressIpDotted: If op_NSAddressIpDotted is specified, this value will be compared to the value in NSAddressIpDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressIpDotted must be specified if op_NSAddressIpDotted is specified.
             :type val_c_NSAddressIpDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressIpNumeric: The operator to apply to the field NSAddressIpNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressIpNumeric: The numerical value of the remote IP address in the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressIpNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressIpNumeric: If op_NSAddressIpNumeric is specified, the field named in this input will be compared to the value in NSAddressIpNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressIpNumeric must be specified if op_NSAddressIpNumeric is specified.
             :type val_f_NSAddressIpNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressIpNumeric: If op_NSAddressIpNumeric is specified, this value will be compared to the value in NSAddressIpNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressIpNumeric must be specified if op_NSAddressIpNumeric is specified.
             :type val_c_NSAddressIpNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressName: The operator to apply to the field NSAddressName. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressName: The name of the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressName: If op_NSAddressName is specified, the field named in this input will be compared to the value in NSAddressName using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressName must be specified if op_NSAddressName is specified.
             :type val_f_NSAddressName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressName: If op_NSAddressName is specified, this value will be compared to the value in NSAddressName using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressName must be specified if op_NSAddressName is specified.
             :type val_c_NSAddressName: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressNetmaskDotted: The operator to apply to the field NSAddressNetmaskDotted. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressNetmaskDotted: The management netmask IP address of netscreen address is dotted (or colon delimited for IPv6) format. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressNetmaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressNetmaskDotted: If op_NSAddressNetmaskDotted is specified, the field named in this input will be compared to the value in NSAddressNetmaskDotted using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressNetmaskDotted must be specified if op_NSAddressNetmaskDotted is specified.
             :type val_f_NSAddressNetmaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressNetmaskDotted: If op_NSAddressNetmaskDotted is specified, this value will be compared to the value in NSAddressNetmaskDotted using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressNetmaskDotted must be specified if op_NSAddressNetmaskDotted is specified.
             :type val_c_NSAddressNetmaskDotted: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressNetmaskNumeric: The operator to apply to the field NSAddressNetmaskNumeric. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressNetmaskNumeric: The numerical value of netmask in the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressNetmaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressNetmaskNumeric: If op_NSAddressNetmaskNumeric is specified, the field named in this input will be compared to the value in NSAddressNetmaskNumeric using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressNetmaskNumeric must be specified if op_NSAddressNetmaskNumeric is specified.
             :type val_f_NSAddressNetmaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressNetmaskNumeric: If op_NSAddressNetmaskNumeric is specified, this value will be compared to the value in NSAddressNetmaskNumeric using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressNetmaskNumeric must be specified if op_NSAddressNetmaskNumeric is specified.
             :type val_c_NSAddressNetmaskNumeric: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressStartTime: The operator to apply to the field NSAddressStartTime. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressStartTime: The starting effective time of this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressStartTime: If op_NSAddressStartTime is specified, the field named in this input will be compared to the value in NSAddressStartTime using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressStartTime must be specified if op_NSAddressStartTime is specified.
             :type val_f_NSAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressStartTime: If op_NSAddressStartTime is specified, this value will be compared to the value in NSAddressStartTime using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressStartTime must be specified if op_NSAddressStartTime is specified.
             :type val_c_NSAddressStartTime: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressTimeStamp: The operator to apply to the field NSAddressTimeStamp. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressTimeStamp: The date and time of netscreen address was calculated or collected. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressTimeStamp: If op_NSAddressTimeStamp is specified, the field named in this input will be compared to the value in NSAddressTimeStamp using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressTimeStamp must be specified if op_NSAddressTimeStamp is specified.
             :type val_f_NSAddressTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressTimeStamp: If op_NSAddressTimeStamp is specified, this value will be compared to the value in NSAddressTimeStamp using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressTimeStamp must be specified if op_NSAddressTimeStamp is specified.
             :type val_c_NSAddressTimeStamp: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_NSAddressZone: The operator to apply to the field NSAddressZone. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. NSAddressZone: The zone of the netscreen address. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_NSAddressZone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_NSAddressZone: If op_NSAddressZone is specified, the field named in this input will be compared to the value in NSAddressZone using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_NSAddressZone must be specified if op_NSAddressZone is specified.
             :type val_f_NSAddressZone: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_NSAddressZone: If op_NSAddressZone is specified, this value will be compared to the value in NSAddressZone using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_NSAddressZone must be specified if op_NSAddressZone is specified.
             :type val_c_NSAddressZone: String

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

             :param timestamp: The data returned will represent the netscreen addresses as of this date and time. If omitted, the result will indicate the most recently collected data.
             :type timestamp: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of netscreen address methods. The listed methods will be called on each netscreen address returned and included in the output. Available methods are: device.
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
            |  ``default:`` NSAddressID

             :param sort: The data field(s) to use for sorting the output. Default is NSAddressID. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID.
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

             :param select: The list of attributes to return for each NetscreenAddress. Valid values are NSAddressID, DeviceID, NSAddressStartTime, NSAddressEndTime, NSAddressTimeStamp, NSAddressChangedCols, NSAddressIndex, NSAddressName, NSAddressZone, NSAddressIpDotted, NSAddressIpNumeric, NSAddressDomainDotted, NSAddressDomainNumeric, NSAddressNetmaskDotted, NSAddressNetmaskNumeric, DataSourceID. If empty or omitted, all attributes will be returned.
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

             :return netscreen_addresses: An array of the NetscreenAddress objects that match the specified input criteria.
             :rtype netscreen_addresses: Array of NetscreenAddress

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def data_source(self, **kwargs):
        """The collector NetMRI that collected this data record.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

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

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

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

             :param NSAddressID: The internal NetMRI identifier of netscreen address.
             :type NSAddressID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return : The device from which this data was collected.
             :rtype : InfraDevice

            """

        return self.api_request(self._get_method_fullname("infradevice"), kwargs)
