from ..remote import RemoteModel


class ScanInterfacesGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``scanID:`` none
    |  ``attribute type:`` string

    |  ``unit_id:`` none
    |  ``attribute type:`` string

    |  ``unit_name:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``physical_if_id:`` none
    |  ``attribute type:`` string

    |  ``ipv4_address:`` none
    |  ``attribute type:`` string

    |  ``ipv4_address_formated:`` none
    |  ``attribute type:`` string

    |  ``ipv4_mask:`` none
    |  ``attribute type:`` string

    |  ``ipv4_gateway:`` none
    |  ``attribute type:`` string

    |  ``ipv6_address:`` none
    |  ``attribute type:`` string

    |  ``ipv6_address_formated:`` none
    |  ``attribute type:`` string

    |  ``ipv6_prefix:`` none
    |  ``attribute type:`` string

    |  ``ipv6_gateway:`` none
    |  ``attribute type:`` string

    |  ``encap_tag:`` none
    |  ``attribute type:`` string

    |  ``search_domains:`` none
    |  ``attribute type:`` string

    |  ``virtual_network_id:`` none
    |  ``attribute type:`` string

    |  ``if_dev:`` none
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``Network:`` none
    |  ``attribute type:`` string

    |  ``primary_dns_server:`` none
    |  ``attribute type:`` string

    |  ``secondary_dns_server:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "scanID",
                  "unit_id",
                  "unit_name",
                  "name",
                  "physical_if_id",
                  "ipv4_address",
                  "ipv4_address_formated",
                  "ipv4_mask",
                  "ipv4_gateway",
                  "ipv6_address",
                  "ipv6_address_formated",
                  "ipv6_prefix",
                  "ipv6_gateway",
                  "encap_tag",
                  "search_domains",
                  "virtual_network_id",
                  "if_dev",
                  "VirtualNetworkID",
                  "Network",
                  "primary_dns_server",
                  "secondary_dns_server",
                  )
