from ..remote import RemoteModel


class ConfigErrorRemote(RemoteModel):
    """
    This table lists out all the entries of Configuration Error.


    |  ``ConfigErrorID:`` The internal NetMRI identifier of the Configuration Error.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which configuration error was collected.
    |  ``attribute type:`` number

    |  ``Timestamp:`` The date and time at which the session was updated.
    |  ``attribute type:`` datetime

    |  ``ErrMsg:`` The total inbound and outbound error message of the device configuration.
    |  ``attribute type:`` string

    |  ``DatasourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    """

    properties = ("ConfigErrorID",
                  "DeviceID",
                  "Timestamp",
                  "ErrMsg",
                  "DatasourceID",
                  )
