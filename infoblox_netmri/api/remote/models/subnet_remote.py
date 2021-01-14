from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SubnetRemote(RemoteModel):
    """
    Subnets found in the network.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``SubnetChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``SubnetCIDR:`` The subnet in CIDR format.
    |  ``attribute type:`` string

    |  ``SubnetEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SubnetID:`` The internal NetMRI identifier for this subnet.
    |  ``attribute type:`` number

    |  ``SubnetIPDotted:`` The subnet network address in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SubnetIPNumeric:`` The numerical value of the network address.
    |  ``attribute type:`` number

    |  ``SubnetLastIPNumeric:`` The last IP address in the subnet. All IPs in the subnet will be between SubnetIPNumeric (Network Address, Numerical) and SubnetLastIPNumeric (Last IP Address, Numerical), inclusive.
    |  ``attribute type:`` number

    |  ``SubnetLocation:`` If the subnet is located within the NetMRI's configured CIDR blocks, it is identified as 'internal'. Otherwise, it is identified as 'external'.
    |  ``attribute type:`` string

    |  ``SubnetNetMaskDotted:`` The subnet network mask in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``SubnetNetMaskNumeric:`` The numerical value of the network mask.
    |  ``attribute type:`` number

    |  ``SubnetSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``SubnetStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``SubnetTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN on which this subnet is defined, or blank if this cannot be determined.
    |  ``attribute type:`` number



    |  ``RouteTimestamp:`` The date and time that this subnet was last seen on any router.
    |  ``attribute type:`` datetime

    |  ``VirtualNetworkID:`` The internal NetMRI identifier of the Virtual Network on which this subnet is defined, or blank if this cannot be determined.
    |  ``attribute type:`` number

    |  ``network_name:`` A Network View assigned to the subnet.
    |  ``attribute type:`` string

    |  ``SubnetConsumerBd:`` ID of ACI bridge domain the device is assigned to
    |  ``attribute type:`` number

    |  ``SubnetConsumerEpg:`` ID of ACI EPG the device is assigned to
    |  ``attribute type:`` number

    |  ``SubnetSdnInd:`` A flag indicating if this subnet collected from some SDN controller.
    |  ``attribute type:`` bool

    """

    properties = ("DataSourceID",
                  "SubnetChangedCols",
                  "SubnetCIDR",
                  "SubnetEndTime",
                  "SubnetID",
                  "SubnetIPDotted",
                  "SubnetIPNumeric",
                  "SubnetLastIPNumeric",
                  "SubnetLocation",
                  "SubnetNetMaskDotted",
                  "SubnetNetMaskNumeric",
                  "SubnetSource",
                  "SubnetStartTime",
                  "SubnetTimestamp",
                  "VlanID",
                  "RouteTimestamp",
                  "VirtualNetworkID",
                  "network_name",
                  "SubnetConsumerBd",
                  "SubnetConsumerEpg",
                  "SubnetSdnInd",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"SubnetID": self.SubnetID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The VLAN on which this subnet is defined, or blank if this cannot be determined.
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"SubnetID": self.SubnetID})
