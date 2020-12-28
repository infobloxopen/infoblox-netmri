from ..remote import RemoteModel


class InterfaceViewerAclsGridRemote(RemoteModel):
    """
    list of interface traffic rule lists


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The NetMRI internal identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier of the rule list.
    |  ``attribute type:`` number

    |  ``AccessList:`` The name of the rule list.
    |  ``attribute type:`` string

    |  ``Direction:`` The direction
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceFilterSetID",
                  "AccessList",
                  "Direction",
                  "ifIndex",
                  )
