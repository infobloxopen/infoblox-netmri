from ..remote import RemoteModel


class DeviceViewerSubnetsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``cidr:`` none
    |  ``attribute type:`` string

    |  ``tenant_name:`` none
    |  ``attribute type:`` string

    |  ``vrf_name:`` none
    |  ``attribute type:`` string

    |  ``epg_name:`` none
    |  ``attribute type:`` string

    |  ``bridge_domain:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "cidr",
                  "tenant_name",
                  "vrf_name",
                  "epg_name",
                  "bridge_domain",
                  )
