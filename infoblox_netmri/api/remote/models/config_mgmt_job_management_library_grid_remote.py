from ..remote import RemoteModel


class ConfigMgmtJobManagementLibraryGridRemote(RemoteModel):
    """



    |  ``scriptid:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``language:`` none
    |  ``attribute type:`` string

    |  ``category:`` none
    |  ``attribute type:`` string

    |  ``description:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    """

    properties = ("scriptid",
                  "name",
                  "language",
                  "category",
                  "description",
                  "created_by",
                  "created_at",
                  "updated_by",
                  "updated_at",
                  )
