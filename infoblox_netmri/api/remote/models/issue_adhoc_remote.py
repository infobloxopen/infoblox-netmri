from ..remote import RemoteModel


class IssueAdhocRemote(RemoteModel):
    """



    |  ``IssueTypeID:`` none
    |  ``attribute type:`` string

    |  ``Title:`` none
    |  ``attribute type:`` string

    |  ``Description:`` none
    |  ``attribute type:`` string

    |  ``Component:`` none
    |  ``attribute type:`` string

    |  ``Correctness:`` none
    |  ``attribute type:`` string

    |  ``Stability:`` none
    |  ``attribute type:`` string

    |  ``Module:`` none
    |  ``attribute type:`` string

    |  ``Visible:`` none
    |  ``attribute type:`` string

    |  ``IssueSource:`` none
    |  ``attribute type:`` string

    |  ``IssueAdHocID:`` none
    |  ``attribute type:`` string

    """

    properties = ("IssueTypeID",
                  "Title",
                  "Description",
                  "Component",
                  "Correctness",
                  "Stability",
                  "Module",
                  "Visible",
                  "IssueSource",
                  "IssueAdHocID",
                  )
