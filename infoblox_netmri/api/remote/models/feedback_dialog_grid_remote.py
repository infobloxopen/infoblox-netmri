from ..remote import RemoteModel


class FeedbackDialogGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``ProcessID:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceName",
                  "ProcessID",
                  "Status",
                  )
