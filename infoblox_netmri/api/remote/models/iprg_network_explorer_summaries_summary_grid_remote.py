from ..remote import RemoteModel


class IprgNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``IprgID:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberState:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberPriority:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberPreemptDelay:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberLearnedHelloTime:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberConfiguredHelloTime:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberLearnedHoldTime:`` none
    |  ``attribute type:`` string

    |  ``IprgNumber:`` none
    |  ``attribute type:`` string

    |  ``IprgIPDotted:`` none
    |  ``attribute type:`` string

    |  ``IprgIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``IprgType:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "IprgID",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceIPNumeric",
                  "DeviceIPDotted",
                  "ifDescr",
                  "VirtualNetworkMemberName",
                  "ifIndex",
                  "IprgMemberState",
                  "IprgMemberPriority",
                  "IprgMemberPreemptDelay",
                  "IprgMemberLearnedHelloTime",
                  "IprgMemberConfiguredHelloTime",
                  "IprgMemberLearnedHoldTime",
                  "IprgNumber",
                  "IprgIPDotted",
                  "IprgIPNumeric",
                  "IprgType",
                  )
