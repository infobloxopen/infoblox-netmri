from ..remote import RemoteModel


class VrfNeVnSectionGridRemote(RemoteModel):
    """



    |  ``VrfID:`` none
    |  ``attribute type:`` string

    |  ``VrfName:`` none
    |  ``attribute type:`` string

    |  ``router_count:`` none
    |  ``attribute type:`` string

    """

    properties = ("VrfID",
                  "VrfName",
                  "router_count",
                  )
