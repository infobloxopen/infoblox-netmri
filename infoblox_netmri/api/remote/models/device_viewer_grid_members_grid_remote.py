from ..remote import RemoteModel


class DeviceViewerGridMembersGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIP:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceModel:`` none
    |  ``attribute type:`` string

    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string

    |  ``GridMemberFirstSeenTime:`` none
    |  ``attribute type:`` string

    |  ``GridMemberQueueFromMaster:`` none
    |  ``attribute type:`` string

    |  ``GridMemberLastRepTimeFromMaster:`` none
    |  ``attribute type:`` string

    |  ``GridMemberQueueToMaster:`` none
    |  ``attribute type:`` string

    |  ``GridMemberLastRepTimeToMaster:`` none
    |  ``attribute type:`` string

    |  ``GridMemberStatus:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceIP",
                  "DeviceName",
                  "DeviceModel",
                  "DeviceVersion",
                  "GridMemberFirstSeenTime",
                  "GridMemberQueueFromMaster",
                  "GridMemberLastRepTimeFromMaster",
                  "GridMemberQueueToMaster",
                  "GridMemberLastRepTimeToMaster",
                  "GridMemberStatus",
                  )
