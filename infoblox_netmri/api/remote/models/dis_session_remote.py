from ..remote import RemoteModel


class DisSessionRemote(RemoteModel):
    """
    Represents a DIS session.


    |  ``SessionID:`` The NetMRI internal identifier for the session.
    |  ``attribute type:`` string

    |  ``RemoteIPAddress:`` The IP address that initiated the session.
    |  ``attribute type:`` string

    |  ``RemoteUsername:`` The username that initiated the session.
    |  ``attribute type:`` string

    |  ``JobID:`` The NetMRI internal identifier for the job.
    |  ``attribute type:`` number

    |  ``Timestamp:`` The date and time at which the session was updated.
    |  ``attribute type:`` string

    |  ``UnitIDList:`` An array of internal identifiers for the session's collectors.
    |  ``attribute type:`` string

    """

    properties = ("SessionID",
                  "RemoteIPAddress",
                  "RemoteUsername",
                  "JobID",
                  "Timestamp",
                  "UnitIDList",
                  )
