from ..broker import Broker


class SpmInterfacesHubLocatorGridBroker(Broker):
    controller = "spm_interfaces_hub_locator_grids"

    def index(self, **kwargs):
        """Lists the available spm interfaces hub locator grids. Any of the inputs listed may be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param GroupID: The internal NetMRI identifier of the device groups to which to limit the results.
             :type GroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` today

             :param starttime: The data returned will represent the spm interfaces hub locator grids with this date and time as lower boundary. If omitted, the result will indicate the most recently collected data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` tomorrow

             :param endtime: The data returned will represent the spm interfaces hub locator grids with this date and time as upper boundary. If omitted, the result will indicate the most recently collected data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` Daily

             :param TimePeriod: The time period for which to retrieve the changes. Valid values are 'Daily', 'Weekly', 'Monthly', '7-Day', '30-Day'.
             :type TimePeriod: String

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
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Valid values are id, VirtualNetworkID, DeviceID, DeviceType, DeviceName, DeviceIPDotted, DeviceIPNumeric, Network, InterfaceID, ifName, VirtualNetworkMemberName, ifIndex, ifDescr, ifAlias, ifType, ifMAC, ifTrunkStatus, ifAdminStatus, ifOperStatus, ifSpeed, ifAdminDuplex, ifDuplex, PoEPower, PoEStatus, VlanIndex, VlanName, VlanID, VTPDomain, EndHostCount, PortStatus, Packets, Errors, ErrorPercentage, FirstSeen, LastSeen, ifPortControlInd, ifSwitchPortMgmtInd.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each SpmInterfacesHubLocatorGrid. Valid values are id, VirtualNetworkID, DeviceID, DeviceType, DeviceName, DeviceIPDotted, DeviceIPNumeric, Network, InterfaceID, ifName, VirtualNetworkMemberName, ifIndex, ifDescr, ifAlias, ifType, ifMAC, ifTrunkStatus, ifAdminStatus, ifOperStatus, ifSpeed, ifAdminDuplex, ifDuplex, PoEPower, PoEStatus, VlanIndex, VlanName, VlanID, VTPDomain, EndHostCount, PortStatus, Packets, Errors, ErrorPercentage, FirstSeen, LastSeen, ifPortControlInd, ifSwitchPortMgmtInd. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param refresh_ind: If true, the grid will be regenerated, rather than using any available cached grid data.
             :type refresh_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param async_ind: If true and if grid data is not yet available, it will return immediately with 202 status. User should retry again later.
             :type async_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return spm_interfaces_hub_locator_grids: An array of the SpmInterfacesHubLocatorGrid objects that match the specified input criteria.
             :rtype spm_interfaces_hub_locator_grids: Array of SpmInterfacesHubLocatorGrid

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return summary: A summary of calculation of selected columns, when applicable.
             :rtype summary: Hash

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def data_partitions(self, **kwargs):
        """Returns data partitions with their statuses for specified grid. 0 - data not available for that date, 1 - data available but must be prepared, 2 - data prepared and immediately available

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("data_partitions"), kwargs)
