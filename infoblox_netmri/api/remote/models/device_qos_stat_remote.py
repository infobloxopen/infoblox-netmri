from ..remote import RemoteModel


class DeviceQosStatRemote(RemoteModel):
    """
    This table list out the entries of Qos statistics of each device.


    |  ``DeviceQosID:`` The internal NetMRI identifier for the Device Quality of Service.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of each device from which Qos was calculated or collected.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier of the local interface of the Device Qos Statistics.
    |  ``attribute type:`` number

    |  ``StartTime:`` The date and time the record is initially created in the NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``QosPolicyIndex:`` The policy value of Quality of service in each device.
    |  ``attribute type:`` string

    |  ``QosObjectsIndex:`` The object index of Qos statistics of each device.
    |  ``attribute type:`` string

    |  ``QosConfigIndex:`` The config value of Qos statistics of each device.
    |  ``attribute type:`` string

    |  ``QosObjectsType:`` The NetMRI-determined the object type of Device Qos Statistics.
    |  ``attribute type:`` string

    |  ``QosCMName:`` The common name of Qos statistics of each device.
    |  ``attribute type:`` string

    |  ``QosCMDesc:`` The common description of Qos Statistics of each device.
    |  ``attribute type:`` string

    |  ``QosCMInfo:`` The common information of Device Qos Statistics.
    |  ``attribute type:`` string

    |  ``QosIfType:`` The type of Device Qos Statistics.
    |  ``attribute type:`` string

    |  ``QosPolicyDirection:`` Describes the direction of policy defined in the Qos.
    |  ``attribute type:`` string

    |  ``QosIfIndex:`` The current value of the Device Qos Statistics.
    |  ``attribute type:`` string

    |  ``QosCMPrePolicyPkt:`` The number of common policy packet defined in the Qos statistics of each device.
    |  ``attribute type:`` string

    |  ``QosCMDropPkt:`` The number of common drop packet defined in the Qos statistics of each device.
    |  ``attribute type:`` string

    |  ``QosSetCfgIpDSCPValue:`` Defines the configuration IP address of device statistics.
    |  ``attribute type:`` string

    |  ``QosSetCfgIpPrecedenceValue:`` The precedence value of configuration IP address.
    |  ``attribute type:`` string

    """

    properties = ("DeviceQosID",
                  "DeviceID",
                  "InterfaceID",
                  "StartTime",
                  "EndTime",
                  "QosPolicyIndex",
                  "QosObjectsIndex",
                  "QosConfigIndex",
                  "QosObjectsType",
                  "QosCMName",
                  "QosCMDesc",
                  "QosCMInfo",
                  "QosIfType",
                  "QosPolicyDirection",
                  "QosIfIndex",
                  "QosCMPrePolicyPkt",
                  "QosCMDropPkt",
                  "QosSetCfgIpDSCPValue",
                  "QosSetCfgIpPrecedenceValue",
                  )
