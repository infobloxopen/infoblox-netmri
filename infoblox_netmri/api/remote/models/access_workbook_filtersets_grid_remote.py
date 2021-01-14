from ..remote import RemoteModel


class AccessWorkbookFiltersetsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Collector:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``DeviceModel:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    |  ``DeviceFilterSetID:`` none
    |  ``attribute type:`` string

    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``FltSetFirstSeenTime:`` none
    |  ``attribute type:`` string

    |  ``FltSetStartTime:`` none
    |  ``attribute type:`` string

    |  ``FltSetEndTime:`` none
    |  ``attribute type:`` string

    |  ``FltSetTimestamp:`` none
    |  ``attribute type:`` string

    |  ``FltSetName:`` none
    |  ``attribute type:`` string

    |  ``FltSetIPVersion:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "Network",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceAssurance",
                  "DeviceFilterSetID",
                  "DataSourceID",
                  "FltSetFirstSeenTime",
                  "FltSetStartTime",
                  "FltSetEndTime",
                  "FltSetTimestamp",
                  "FltSetName",
                  "FltSetIPVersion",
                  )
