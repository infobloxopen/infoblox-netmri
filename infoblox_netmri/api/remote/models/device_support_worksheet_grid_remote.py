from ..remote import RemoteModel


class DeviceSupportWorksheetGridRemote(RemoteModel):
    """
    A collection of device support data requests.


    |  ``id:`` The internal system identifier for the worksheet.
    |  ``attribute type:`` number

    |  ``LastUpdated:`` The date for the last update to the record.
    |  ``attribute type:`` string

    |  ``Status:`` The status of the request.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The Device IP address.
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` The Device Vendor.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The Device Model.
    |  ``attribute type:`` string

    |  ``OsVersion:`` The OS Version.
    |  ``attribute type:`` string

    |  ``WorksheetID:`` Internal identifier for the worksheet.
    |  ``attribute type:`` string

    |  ``StepNumber:`` The last step which the worksheet was saved at.
    |  ``attribute type:`` number

    |  ``hide_download_ind:`` Internal flag to suppress a file download button when inappropriate.
    |  ``attribute type:`` bool

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` Internal identifier for the network view.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "LastUpdated",
                  "Status",
                  "DeviceIPDotted",
                  "DeviceVendor",
                  "DeviceModel",
                  "OsVersion",
                  "WorksheetID",
                  "StepNumber",
                  "hide_download_ind",
                  "DeviceIPNumeric",
                  "Network",
                  "VirtualNetworkID",
                  )
