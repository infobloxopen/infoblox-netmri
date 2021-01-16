from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VirtualNetworkMemberRemote(RemoteModel):
    """
    The VRF configurations for each VRF on a given device. This constitutes the devices 'membership' information for that VRF.


    |  ``VirtualNetworkMemberStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``VirtualNetworkMemberEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``VirtualNetworkMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``VirtualNetworkMemberFirstTime:`` The first time this data element was seen on the network.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberID:`` The internal NetMRI identifier for this VRF membership.
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal NetMRI identifier for the VRF-based VPN related to this record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this VRF membership configuration was collected.
    |  ``attribute type:`` number


    |  ``VirtualNetworkMemberName:`` The name of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``RouteLimit:`` The maximum number of routes that this VRF is configured to contain.
    |  ``attribute type:`` number

    |  ``WarningLimit:`` The number of routes in the VRF that will trigger this device to produce a warning.
    |  ``attribute type:`` number

    |  ``CurrentCount:`` The number of routes currently in the VRF.
    |  ``attribute type:`` number

    |  ``DefaultRDType:`` The style of the default Route Distinguisher, asn or ipv4.
    |  ``attribute type:`` string

    |  ``DefaultRDLeft:`` The left-hand portion of the default Route Distinguisher; use DefaultRDType to identify if it is an AS number or and IPv4 address.
    |  ``attribute type:`` number

    |  ``DefaultRDRight:`` The right-hand portion of the default Route Distinguisher.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberDescription:`` The description of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``DefaultVPNID:`` The VPN ID assigned to this VRF, as configured on this device.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberArtificialInd:`` Indicates is this is an artificial VNM.
    |  ``attribute type:`` bool

    |  ``VirtualNetworkMemberDefaultInd:`` Indicates is this is a default VNM.
    |  ``attribute type:`` bool


    |  ``member_rd:`` The displayable VRF route distinguisher of this obkect.
    |  ``attribute type:`` string

    |  ``assigned_network_id:`` The current network view id assigned.
    |  ``attribute type:`` number

    """

    properties = ("VirtualNetworkMemberStartTime",
                  "VirtualNetworkMemberEndTime",
                  "VirtualNetworkMemberChangedCols",
                  "VirtualNetworkMemberTimestamp",
                  "VirtualNetworkMemberFirstTime",
                  "DataSourceID",
                  "VirtualNetworkMemberID",
                  "VirtualNetworkID",
                  "DeviceID",
                  "VirtualNetworkMemberName",
                  "RouteLimit",
                  "WarningLimit",
                  "CurrentCount",
                  "DefaultRDType",
                  "DefaultRDLeft",
                  "DefaultRDRight",
                  "VirtualNetworkMemberDescription",
                  "DefaultVPNID",
                  "VirtualNetworkMemberArtificialInd",
                  "VirtualNetworkMemberDefaultInd",
                  "member_rd",
                  "assigned_network_id",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this VRF membership configuration was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"VirtualNetworkMemberID": self.VirtualNetworkMemberID})

    @property
    @check_api_availability
    def virtual_network(self):
        """
        Network assigned to current VRF instance.
        ``attribute type:`` model
        """
        return self.broker.virtual_network(**{"VirtualNetworkMemberID": self.VirtualNetworkMemberID})
