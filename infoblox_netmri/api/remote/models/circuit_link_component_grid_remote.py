from ..remote import RemoteModel


class CircuitLinkComponentGridRemote(RemoteModel):
    """



    |  ``CLinkCompID:`` none
    |  ``attribute type:`` string

    |  ``CLinkCompDtgIndex:`` none
    |  ``attribute type:`` string

    |  ``CLinkCompCounter:`` none
    |  ``attribute type:`` string

    |  ``CLinkCompType:`` none
    |  ``attribute type:`` string

    |  ``CLinkCompUnitNumber:`` none
    |  ``attribute type:`` string

    |  ``CLinkCompState:`` none
    |  ``attribute type:`` string

    """

    properties = ("CLinkCompID",
                  "CLinkCompDtgIndex",
                  "CLinkCompCounter",
                  "CLinkCompType",
                  "CLinkCompUnitNumber",
                  "CLinkCompState",
                  )
