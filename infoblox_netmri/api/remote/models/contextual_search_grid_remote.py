from ..remote import RemoteModel


class ContextualSearchGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``ObjName:`` none
    |  ``attribute type:`` string

    |  ``ObjectID:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``Position:`` none
    |  ``attribute type:`` string

    |  ``Category:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "ObjName",
                  "ObjectID",
                  "DeviceID",
                  "Position",
                  "Category",
                  )
