from ..remote import RemoteModel


class StorageMgmtGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``StorageCategory:`` none
    |  ``attribute type:`` string

    |  ``VolumeSize:`` none
    |  ``attribute type:`` string

    |  ``Locked:`` none
    |  ``attribute type:`` string

    |  ``FreeGB:`` none
    |  ``attribute type:`` string

    |  ``FreePercent:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "StorageCategory",
                  "VolumeSize",
                  "Locked",
                  "FreeGB",
                  "FreePercent",
                  )
