from ..remote import RemoteModel


class PartitionDefinitionGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``PartitionTableName:`` none
    |  ``attribute type:`` string

    |  ``PartitionColumn:`` none
    |  ``attribute type:`` string

    |  ``PartitionType:`` none
    |  ``attribute type:`` string

    |  ``TypeCategory:`` none
    |  ``attribute type:`` string

    |  ``HistoryType:`` none
    |  ``attribute type:`` string

    |  ``HistoryEnabled:`` none
    |  ``attribute type:`` string

    |  ``ColumnPrefix:`` none
    |  ``attribute type:`` string

    |  ``Description:`` none
    |  ``attribute type:`` string

    |  ``ArchiveAgeDays:`` none
    |  ``attribute type:`` string

    |  ``MaxDataAgeDays:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "PartitionTableName",
                  "PartitionColumn",
                  "PartitionType",
                  "TypeCategory",
                  "HistoryType",
                  "HistoryEnabled",
                  "ColumnPrefix",
                  "Description",
                  "ArchiveAgeDays",
                  "MaxDataAgeDays",
                  )
