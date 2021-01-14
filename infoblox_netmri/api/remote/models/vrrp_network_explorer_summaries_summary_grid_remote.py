from ..remote import RemoteModel


class VrrpNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``IprgID:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberState:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberPriority:`` none
    |  ``attribute type:`` string

    |  ``IprgMemberConfiguredHelloTime:`` none
    |  ``attribute type:`` string

    |  ``IprgType:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "IprgID",
                  "DeviceName",
                  "DeviceIPNumeric",
                  "DeviceIPDotted",
                  "ifDescr",
                  "ifIndex",
                  "IprgMemberState",
                  "IprgMemberPriority",
                  "IprgMemberConfiguredHelloTime",
                  "IprgType",
                  )
