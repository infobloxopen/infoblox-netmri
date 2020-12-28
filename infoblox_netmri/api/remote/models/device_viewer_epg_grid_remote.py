from ..remote import RemoteModel


class DeviceViewerEpgGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``tenant_name:`` none
    |  ``attribute type:`` string

    |  ``tenant_dn:`` none
    |  ``attribute type:`` string

    |  ``app_profile_name:`` none
    |  ``attribute type:`` string

    |  ``app_profile_dn:`` none
    |  ``attribute type:`` string

    |  ``epg_name:`` none
    |  ``attribute type:`` string

    |  ``epg_dn:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "tenant_name",
                  "tenant_dn",
                  "app_profile_name",
                  "app_profile_dn",
                  "epg_name",
                  "epg_dn",
                  )
