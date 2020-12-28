from ..remote import RemoteModel


class IprgNetworkExplorerSummariesSectionGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberID:`` none
    |  ``attribute type:`` string

    |  ``IprgID:`` none
    |  ``attribute type:`` string

    |  ``IprgIPDotted:`` none
    |  ``attribute type:`` string

    |  ``IprgIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``IprgNumber:`` none
    |  ``attribute type:`` string

    |  ``IprgType:`` none
    |  ``attribute type:`` string

    |  ``IprgCount:`` none
    |  ``attribute type:`` string

    |  ``ActiveIprgMemberID:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "IprgMemberID",
                  "IprgID",
                  "IprgIPDotted",
                  "IprgIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "IprgNumber",
                  "IprgType",
                  "IprgCount",
                  "ActiveIprgMemberID",
                  )
