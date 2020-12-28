from ..remote import RemoteModel


class DeviceViewerRouterRawQosGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``StartTime:`` none
    |  ``attribute type:`` string

    |  ``EndTime:`` none
    |  ``attribute type:`` string

    |  ``QosCMInfo:`` none
    |  ``attribute type:`` string

    |  ``Interface:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``QosCMName:`` none
    |  ``attribute type:`` string

    |  ``QosPolicyDirection:`` none
    |  ``attribute type:`` string

    |  ``QosCMPrePolicyPkt:`` none
    |  ``attribute type:`` string

    |  ``QosCMDropPkt:`` none
    |  ``attribute type:`` string

    |  ``QosSetCfgIpDSCPValue:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "StartTime",
                  "EndTime",
                  "QosCMInfo",
                  "Interface",
                  "VirtualNetworkID",
                  "Network",
                  "ifNameSort",
                  "QosCMName",
                  "QosPolicyDirection",
                  "QosCMPrePolicyPkt",
                  "QosCMDropPkt",
                  "QosSetCfgIpDSCPValue",
                  "ifPortControlInd",
                  )
