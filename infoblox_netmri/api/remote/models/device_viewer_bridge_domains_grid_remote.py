from ..remote import RemoteModel


class DeviceViewerBridgeDomainsGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``tenant_name:`` none
    |  ``attribute type:`` string

    |  ``tenant_dn:`` none
    |  ``attribute type:`` string

    |  ``bridge_domain:`` none
    |  ``attribute type:`` string

    |  ``bridge_domain_dn:`` none
    |  ``attribute type:`` string

    |  ``vrf_name:`` none
    |  ``attribute type:`` string

    |  ``vrf_dn:`` none
    |  ``attribute type:`` string

    |  ``epg_name:`` none
    |  ``attribute type:`` string

    |  ``epg_dn:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "tenant_name",
                  "tenant_dn",
                  "bridge_domain",
                  "bridge_domain_dn",
                  "vrf_name",
                  "vrf_dn",
                  "epg_name",
                  "epg_dn",
                  )
