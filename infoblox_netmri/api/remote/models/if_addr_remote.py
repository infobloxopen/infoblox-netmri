from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfAddrRemote(RemoteModel):
    """
    The IP addresses on interfaces.


    |  ``AddrChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``AddrEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``AddrStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``AddrTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device containing the interface configured with this address.
    |  ``attribute type:`` number

    |  ``IfAddrID:`` The internal NetMRI identifier for this interface address (the specific address configured on this specific interface).
    |  ``attribute type:`` number

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` number

    |  ``ifIPDotted:`` The IP address in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``ifIPNumeric:`` The numerical value of the IP address.
    |  ``attribute type:`` number

    |  ``ifNetMaskDotted:`` The network mask value in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``ifNetMaskNumeric:`` The numerical value of the network mask.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface configured with this address.
    |  ``attribute type:`` number

    |  ``SubnetIPDotted:`` The network portion of the IP address in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SubnetIPNumeric:`` The numerical value of the network portion of the IP address.
    |  ``attribute type:`` number





    |  ``network_id:`` The Network View ID assigned to the interface.
    |  ``attribute type:`` number

    |  ``vrf_name:`` The VRF name assigned to the interface.
    |  ``attribute type:`` string

    |  ``vrf_description:`` The VRF description of the vrf assigned to the interface.
    |  ``attribute type:`` string

    |  ``vrf_rd:`` The VRF route distinguisher of the vrf  assigned to the interface.
    |  ``attribute type:`` string

    |  ``AciBdID:`` ID of ACI bridge domain the device is assigned to
    |  ``attribute type:`` number

    |  ``AciEpgID:`` ID of ACI EPG the device is assigned to
    |  ``attribute type:`` number

    |  ``cap_if_net_provisioning_ipv4_ind:`` Capability to provision an ipv4 network on this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_provisioning_ipv6_ind:`` Capability to provision an ipv6 network on this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_deprovisioning_ipv4_ind:`` Capability of de-provisioning an ipv4 network from this interface.
    |  ``attribute type:`` bool

    |  ``cap_if_net_deprovisioning_ipv6_ind:`` Capability of de-provisioning an ipv6 network from this interface.
    |  ``attribute type:`` bool


    """

    properties = ("AddrChangedCols",
                  "AddrEndTime",
                  "AddrStartTime",
                  "AddrTimestamp",
                  "DataSourceID",
                  "DeviceID",
                  "IfAddrID",
                  "ifIndex",
                  "ifIPDotted",
                  "ifIPNumeric",
                  "ifNetMaskDotted",
                  "ifNetMaskNumeric",
                  "InterfaceID",
                  "SubnetIPDotted",
                  "SubnetIPNumeric",
                  "network_id",
                  "vrf_name",
                  "vrf_description",
                  "vrf_rd",
                  "AciBdID",
                  "AciEpgID",
                  "cap_if_net_provisioning_ipv4_ind",
                  "cap_if_net_provisioning_ipv6_ind",
                  "cap_if_net_deprovisioning_ipv4_ind",
                  "cap_if_net_deprovisioning_ipv6_ind",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfAddrID": self.IfAddrID})

    @property
    @check_api_availability
    def device(self):
        """
        The device containing the interface configured with this address.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfAddrID": self.IfAddrID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface configured with this address.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfAddrID": self.IfAddrID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device containing the interface configured with this address.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfAddrID": self.IfAddrID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"IfAddrID": self.IfAddrID})
