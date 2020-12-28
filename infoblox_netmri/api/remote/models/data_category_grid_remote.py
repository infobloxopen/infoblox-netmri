from ..remote import RemoteModel


class DataCategoryGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryID:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryName:`` none
    |  ``attribute type:`` string

    |  ``DataCategoryDescription:`` none
    |  ``attribute type:`` string

    |  ``ArchiveAgeDays:`` none
    |  ``attribute type:`` string

    |  ``MaxDataAgeDays:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DataCategoryID",
                  "DataCategoryName",
                  "DataCategoryDescription",
                  "ArchiveAgeDays",
                  "MaxDataAgeDays",
                  )
