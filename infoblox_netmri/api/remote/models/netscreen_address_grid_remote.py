from ..remote import RemoteModel


class NetscreenAddressGridRemote(RemoteModel):
    """



    |  ``NSAddressID:`` none
    |  ``attribute type:`` string

    |  ``NSAddressIndex:`` none
    |  ``attribute type:`` string

    |  ``NSAddressName:`` none
    |  ``attribute type:`` string

    |  ``NSAddressZone:`` none
    |  ``attribute type:`` string

    |  ``NSAddressIpDotted:`` none
    |  ``attribute type:`` string

    |  ``NSAddressIpNumeric:`` none
    |  ``attribute type:`` string

    |  ``NSAddressDomainDotted:`` none
    |  ``attribute type:`` string

    |  ``NSAddressDomainNumeric:`` none
    |  ``attribute type:`` string

    |  ``NSAddressNetmaskDotted:`` none
    |  ``attribute type:`` string

    |  ``NSAddressTimestamp:`` none
    |  ``attribute type:`` string

    |  ``NSAddressStartTime:`` none
    |  ``attribute type:`` string

    |  ``NSAddressEndTime:`` none
    |  ``attribute type:`` string

    |  ``NSAddressChangedCols:`` none
    |  ``attribute type:`` string

    """

    properties = ("NSAddressID",
                  "NSAddressIndex",
                  "NSAddressName",
                  "NSAddressZone",
                  "NSAddressIpDotted",
                  "NSAddressIpNumeric",
                  "NSAddressDomainDotted",
                  "NSAddressDomainNumeric",
                  "NSAddressNetmaskDotted",
                  "NSAddressTimestamp",
                  "NSAddressStartTime",
                  "NSAddressEndTime",
                  "NSAddressChangedCols",
                  )
