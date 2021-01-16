from ..remote import RemoteModel


class DeviceViewerRouterQosGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``QosCMInfo:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``QosCMName:`` none
    |  ``attribute type:`` string

    |  ``QosPolicyDirection:`` none
    |  ``attribute type:`` string

    |  ``QosCMPrePolicyPkt:`` none
    |  ``attribute type:`` string

    |  ``QosCMDropPkt:`` none
    |  ``attribute type:`` string

    |  ``percentDrops:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "QosCMInfo",
                  "ifName",
                  "VirtualNetworkID",
                  "Network",
                  "ifNameSort",
                  "ifIndex",
                  "QosCMName",
                  "QosPolicyDirection",
                  "QosCMPrePolicyPkt",
                  "QosCMDropPkt",
                  "percentDrops",
                  "ifPortControlInd",
                  )
