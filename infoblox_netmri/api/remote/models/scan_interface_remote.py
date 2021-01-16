from ..remote import RemoteModel


class ScanInterfaceRemote(RemoteModel):
    """
    A NetMRI interface that can do discovery and other interaction with licensed devices


    |  ``unit_id:`` The internal identifier for the collector on which the scan interface exists.
    |  ``attribute type:`` number

    |  ``virtual_network_id:`` The internal NetMRI identifier of the Virtual Network in which the scan interface is present.
    |  ``attribute type:`` number

    |  ``if_dev:`` The system device name of the scan interface.
    |  ``attribute type:`` string

    |  ``name:`` The name of the scan interface.
    |  ``attribute type:`` string

    |  ``physical_if_id:`` The scan interface identifier of the physical interface, if this is a sub-interface.
    |  ``attribute type:`` string

    |  ``encap_tag:`` The 802.1Q encapsulation tag of traffic to be forwarded from the physical interface to the scan interface.
    |  ``attribute type:`` number

    |  ``ipv4_address:`` The IP address of the scan interface in dotted format.
    |  ``attribute type:`` string

    |  ``ipv4_mask:`` The network mask of the scan interface in dotted format.
    |  ``attribute type:`` string

    |  ``ipv4_gateway:`` The gateway of the scan interface in dotted format.
    |  ``attribute type:`` string

    |  ``ipv6_address:`` The IPv6 address of the scan interface in colon-delimited format.
    |  ``attribute type:`` string

    |  ``ipv6_prefix:`` The IPv6 mask of the scan interface.
    |  ``attribute type:`` string

    |  ``ipv6_gateway:`` The gateway of the scan interface in colon-delimited format IPv6.
    |  ``attribute type:`` string

    |  ``primary_dns_server:`` The IP address of the scan interface primary dns server in dotted format.
    |  ``attribute type:`` string

    |  ``secondary_dns_server:`` The IP address of the scan interface secondary dns server in dotted format.
    |  ``attribute type:`` string

    |  ``id:`` The internal NetMRI identifier of the Scan Interface.
    |  ``attribute type:`` number

    |  ``search_domains:`` Search domains for DNS resolving.
    |  ``attribute type:`` string

    """

    properties = ("unit_id",
                  "virtual_network_id",
                  "if_dev",
                  "name",
                  "physical_if_id",
                  "encap_tag",
                  "ipv4_address",
                  "ipv4_mask",
                  "ipv4_gateway",
                  "ipv6_address",
                  "ipv6_prefix",
                  "ipv6_gateway",
                  "primary_dns_server",
                  "secondary_dns_server",
                  "id",
                  "search_domains",
                  )
