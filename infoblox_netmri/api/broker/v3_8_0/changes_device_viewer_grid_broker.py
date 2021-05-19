from ..broker import Broker


class ChangesDeviceViewerGridBroker(Broker):
    controller = "changes_device_viewer_grids"

    def index(self, **kwargs):
        """Lists the available changes device viewer grids. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, ChangeTime, ChangeDetectedTime, ChangeID, HardwareInd, SoftwareInd, AdminInd, ExternalInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, DeviceID, DeviceIPDotted, Network, VirtualNetworkID, DeviceName, DeviceVendor, DeviceModel, DeviceIPNumeric, DeviceType, ChangeUser, ChangeAuthorizedInd, ChangeMethod, ChangeType, RunningChangedRev, SavedChangedRev, HideRunning, HideSaved, DeviceAssurance, HideAccess, configstate, CustomFieldsEditInd.
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

             :param select: The list of attributes to return for each ChangesDeviceViewerGrid. Valid values are id, ChangeTime, ChangeDetectedTime, ChangeID, HardwareInd, SoftwareInd, AdminInd, ExternalInd, SNMPPollInd, SNMPTrapInd, SyslogInd, ConfigPollInd, DeviceID, DeviceIPDotted, Network, VirtualNetworkID, DeviceName, DeviceVendor, DeviceModel, DeviceIPNumeric, DeviceType, ChangeUser, ChangeAuthorizedInd, ChangeMethod, ChangeType, RunningChangedRev, SavedChangedRev, HideRunning, HideSaved, DeviceAssurance, HideAccess, configstate, CustomFieldsEditInd. If empty or omitted, all attributes will be returned.
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

             :return changes_device_viewer_grids: An array of the ChangesDeviceViewerGrid objects that match the specified input criteria.
             :rtype changes_device_viewer_grids: Array of ChangesDeviceViewerGrid

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return summary: A summary of calculation of selected columns, when applicable.
             :rtype summary: Hash

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)
