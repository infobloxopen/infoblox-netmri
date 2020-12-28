from ..remote import RemoteModel


class AggregatedLinkGroupMembershipRemote(RemoteModel):
    """



    |  ``DataSourceID:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberID:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberGroupName:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberGroupIndex:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberAggregateInterface:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberPhysicalInterface:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberStartTime:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberEndTime:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberTimestamp:`` none
    |  ``attribute type:`` string

    |  ``aggLinkGroupMemberChangedCols:`` none
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "aggLinkGroupMemberID",
                  "aggLinkGroupMemberGroupName",
                  "aggLinkGroupMemberGroupIndex",
                  "DeviceID",
                  "aggLinkGroupMemberAggregateInterface",
                  "aggLinkGroupMemberPhysicalInterface",
                  "aggLinkGroupMemberStartTime",
                  "aggLinkGroupMemberEndTime",
                  "aggLinkGroupMemberTimestamp",
                  "aggLinkGroupMemberChangedCols",
                  )
