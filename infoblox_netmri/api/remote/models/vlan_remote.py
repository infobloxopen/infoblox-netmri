from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VlanRemote(RemoteModel):
    """
    Distinct VLANs in the network.  Note that <i>VlanID</i> refers to NetMRI internal ID for the Vlan.  The <i>VlanIndex</i> is the network VLAN ID.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector assigned to this VLAN (members may come from more than one collector).
    |  ``attribute type:`` number

    |  ``RootBridgeAddress:`` The bridge address of the root bridge.
    |  ``attribute type:`` string

    |  ``RootVlanMemberID:`` The internal NetMRI identifier for the VlanMember record of the VLAN root bridge.
    |  ``attribute type:`` number

    |  ``StpEnabledInd:`` A flag indicating whether this VLAN is participating in Spanning Tree.
    |  ``attribute type:`` bool

    |  ``VlanChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``VlanEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``VlanID:`` The internal NetMRI identifier for this VLAN. Note that this is different from the device's view of VLAN ID, which can be found in VlanIndex.
    |  ``attribute type:`` number

    |  ``VlanIndex:`` The numerical VLAN number (VLAN ID).
    |  ``attribute type:`` number

    |  ``VlanName:`` The name of the VLAN on the root bridge.
    |  ``attribute type:`` string

    |  ``VlanStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``VlanTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime




    |  ``root_bridge:`` The name of the root bridge, if available; otherwise, the root bridge address.
    |  ``attribute type:`` string

    |  ``VTPDomain:`` Management domain name if VLAN is VTP managed.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "RootBridgeAddress",
                  "RootVlanMemberID",
                  "StpEnabledInd",
                  "VlanChangedCols",
                  "VlanEndTime",
                  "VlanID",
                  "VlanIndex",
                  "VlanName",
                  "VlanStartTime",
                  "VlanTimestamp",
                  "root_bridge",
                  "VTPDomain",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"VlanID": self.VlanID})

    @property
    @check_api_availability
    def root_member(self):
        """
        The VLAN membership record of the VLAN root bridge.
        ``attribute type:`` model
        """
        return self.broker.root_member(**{"VlanID": self.VlanID})

    @property
    @check_api_availability
    def root_device(self):
        """
        The Device object for the root bridge, if available.
        ``attribute type:`` model
        """
        return self.broker.root_device(**{"VlanID": self.VlanID})
