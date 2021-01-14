from ..remote import RemoteModel


class SubnetNetworkExplorerSummariesSummaryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``SubnetID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``InterfaceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``Tenant:`` none
    |  ``attribute type:`` string

    |  ``BridgeDomain:`` none
    |  ``attribute type:`` string

    |  ``EPG:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``ifDescr:`` none
    |  ``attribute type:`` string

    |  ``Interface:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``ifIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``SubnetCIDR:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "SubnetID",
                  "DeviceID",
                  "InterfaceID",
                  "DeviceIPDotted",
                  "VirtualNetworkID",
                  "Network",
                  "Tenant",
                  "BridgeDomain",
                  "EPG",
                  "DeviceName",
                  "ifDescr",
                  "Interface",
                  "VirtualNetworkMemberName",
                  "ifNameSort",
                  "ifIndex",
                  "DeviceType",
                  "ifIPDotted",
                  "DeviceAssurance",
                  "DeviceIPNumeric",
                  "ifIPNumeric",
                  "SubnetCIDR",
                  )
