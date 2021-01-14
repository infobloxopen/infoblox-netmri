from ..remote import RemoteModel


class DeviceViewerSecurityAclsCkpGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceFilterSetID:`` none
    |  ``attribute type:`` string

    |  ``AccessList:`` none
    |  ``attribute type:`` string

    |  ``Direction:`` none
    |  ``attribute type:`` string

    |  ``policyName:`` none
    |  ``attribute type:`` string

    |  ``Firewall:`` none
    |  ``attribute type:`` string

    |  ``Status:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceFilterSetID",
                  "AccessList",
                  "Direction",
                  "policyName",
                  "Firewall",
                  "Status",
                  )
