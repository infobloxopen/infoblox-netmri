from ..remote import RemoteModel


class DeviceViewerSecurityAclsGridRemote(RemoteModel):
    """
    list of device traffic rule lists


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The NetMRI internal identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier of the rule list.
    |  ``attribute type:`` number

    |  ``AccessList:`` The name of the rule list.
    |  ``attribute type:`` string

    |  ``ifName:`` The name of this interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` number

    |  ``Direction:`` The direction
    |  ``attribute type:`` string

    |  ``ifNameSort:`` The internal NetMRI name of this interface for sorting purpose.
    |  ``attribute type:`` string

    |  ``policyName:`` Only for management server or managed devices. The policy name associated with this usage of the rulelist.
    |  ``attribute type:`` string

    |  ``Firewall:`` Only for management server. The name of the managed device that really holds this rulelist.
    |  ``attribute type:`` string

    |  ``Status:`` Only for management server or managed devices. The status of this policy name on the managed device: 'Active' or 'Non Active'.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "DeviceFilterSetID",
                  "AccessList",
                  "ifName",
                  "ifIndex",
                  "Direction",
                  "ifNameSort",
                  "policyName",
                  "Firewall",
                  "Status",
                  )
