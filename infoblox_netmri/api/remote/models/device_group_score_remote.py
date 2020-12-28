from ..remote import RemoteModel


class DeviceGroupScoreRemote(RemoteModel):
    """
    This table list out the entries of Device Group Score.


    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``GroupSetID:`` The identifier of a group set defined in the Device Group Score.
    |  ``attribute type:`` number

    |  ``Component:`` The issue component (Devices, Configuration, VLANs, etc.).
    |  ``attribute type:`` string

    |  ``Correctness:`` The correctness contribution for this issue.
    |  ``attribute type:`` number

    |  ``Stability:`` The stability contribution for this issue.
    |  ``attribute type:`` number

    |  ``Info:`` Information Message
    |  ``attribute type:`` number

    |  ``Warn:`` Warning Message
    |  ``attribute type:`` number

    |  ``Error:`` Error Message
    |  ``attribute type:`` number

    |  ``InfoDetails:`` Information Details of the DeviceGroupScore.
    |  ``attribute type:`` number

    |  ``WarnDetails:`` Warning Details of a DeviceGroupScore.
    |  ``attribute type:`` number

    |  ``ErrorDetails:`` Error Details of a DeviceGroupScore.
    |  ``attribute type:`` number

    """

    properties = ("Timestamp",
                  "GroupSetID",
                  "Component",
                  "Correctness",
                  "Stability",
                  "Info",
                  "Warn",
                  "Error",
                  "InfoDetails",
                  "WarnDetails",
                  "ErrorDetails",
                  )
