from ..remote import RemoteModel


class PolicyRuleAgainstExistingDeviceGridRemote(RemoteModel):
    """



    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` none
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``DeviceName:`` none
    |  ``attribute type:`` string

    |  ``DeviceType:`` none
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` none
    |  ``attribute type:`` string

    |  ``DeviceModel:`` none
    |  ``attribute type:`` string

    |  ``DeviceVersion:`` none
    |  ``attribute type:`` string

    """

    properties = ("DeviceID",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "VirtualNetworkID",
                  "Network",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceVersion",
                  )
