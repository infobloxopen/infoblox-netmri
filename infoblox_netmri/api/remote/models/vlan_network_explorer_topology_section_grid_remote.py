from ..remote import RemoteModel


class VlanNetworkExplorerTopologySectionGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``VlanID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``VlanIndex:`` none
    |  ``attribute type:`` string

    |  ``VlanName:`` none
    |  ``attribute type:`` string

    |  ``root_bridge:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "VlanID",
                  "DeviceID",
                  "VlanIndex",
                  "VlanName",
                  "root_bridge",
                  )
