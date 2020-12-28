from ..remote import RemoteModel


class CliConnectionRemote(RemoteModel):
    """
    Represents a CLI connection with a device.


    |  ``SessionID:`` The NetMRI internal identifier for the session.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The NetMRI internal identifier for the device to which the session corresponds.
    |  ``attribute type:`` string

    |  ``CommandType:`` The last command type for the session.
    |  ``attribute type:`` string

    |  ``CommandDetail:`` The last command detail for the session.
    |  ``attribute type:`` string

    |  ``Timestamp:`` The date and time at which the session was updated.
    |  ``attribute type:`` string

    """

    properties = ("SessionID",
                  "DeviceID",
                  "CommandType",
                  "CommandDetail",
                  "Timestamp",
                  )
