from ..remote import RemoteModel


class IfGroupDefnRemote(RemoteModel):
    """
    This table list out the entries of Interface Group Definitions.


    |  ``GroupID:`` The internal NetMRI identifier of an interface group.
    |  ``attribute type:`` number

    |  ``GroupName:`` The name of the group in the Interface.
    |  ``attribute type:`` string

    |  ``Criteria:`` The group belongs to defined criteria in an interface group.
    |  ``attribute type:`` string

    |  ``Rank:`` The rank specified for the group in an interface.
    |  ``attribute type:`` number

    |  ``SNMPPolling:`` The SNMP polling state in an interface group definition.
    |  ``attribute type:`` number

    |  ``FlowCollection:`` The level of flow collection in an interface group.
    |  ``attribute type:`` number

    |  ``PerfFrequency:`` The performance frequency level in an interface group.
    |  ``attribute type:`` number

    |  ``Timestamp:`` The date and time this record was collected.
    |  ``attribute type:`` datetime

    |  ``MemberCount:`` The total number of member in an interface group.
    |  ``attribute type:`` number

    |  ``UpdatedAt:`` The date and time this record was last modified.
    |  ``attribute type:`` datetime

    """

    properties = ("GroupID",
                  "GroupName",
                  "Criteria",
                  "Rank",
                  "SNMPPolling",
                  "FlowCollection",
                  "PerfFrequency",
                  "Timestamp",
                  "MemberCount",
                  "UpdatedAt",
                  )
