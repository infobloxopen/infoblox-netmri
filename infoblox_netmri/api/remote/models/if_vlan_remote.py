from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IfVlanRemote(RemoteModel):
    """
    VLANs that an interface is in along with the STP state of the interface.  Also includes SVIs (VlanInterfaceInd = 1) and peer interfaces attached to access ports (VlanExtensionInd = 1).


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of the device to which the interface belongs.
    |  ``attribute type:`` number

    |  ``ifVlanChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ifVlanEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``IfVlanID:`` The internal NetMRI identifier for the interface-in-VLAN record.
    |  ``attribute type:`` number

    |  ``ifVlanSource:`` Internal tracking information for NetMRI algorithms.
    |  ``attribute type:`` string

    |  ``ifVlanStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``ifVlanTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``InterfaceID:`` The internal NetMRI identifier of the interface participating in the VLAN.
    |  ``attribute type:`` number

    |  ``StpPortDesignatedBridge:`` The Spanning Tree Protocol designated bridge address of this interface for this VLAN.
    |  ``attribute type:`` string

    |  ``StpPortState:`` The Spanning Tree Protocol state of this interface for this VLAN.
    |  ``attribute type:`` string

    |  ``VlanExtensionInd:`` A flag indicating if this record represents an interface attached to an access port rather than on a participating bridge.
    |  ``attribute type:`` bool

    |  ``VlanID:`` The internal NetMRI identifier of the VLAN.
    |  ``attribute type:`` number

    |  ``VlanInterfaceInd:`` A flag indicating if this record represents the SVI for the VLAN on this device.
    |  ``attribute type:`` bool

    |  ``VlanMemberID:`` The internal NetMRI identifier for the VlanMember record of the device to which the interface belongs, for this VLAN.
    |  ``attribute type:`` number








    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "ifVlanChangedCols",
                  "ifVlanEndTime",
                  "IfVlanID",
                  "ifVlanSource",
                  "ifVlanStartTime",
                  "ifVlanTimestamp",
                  "InterfaceID",
                  "StpPortDesignatedBridge",
                  "StpPortState",
                  "VlanExtensionInd",
                  "VlanID",
                  "VlanInterfaceInd",
                  "VlanMemberID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def device(self):
        """
        The device to which the interface belongs.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface participating in the VLAN.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def vlan(self):
        """
        The VLAN to which this interface VLAN membership belongs.
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def vlan_member(self):
        """
        The VLAN membership record of the device to which the interface belongs, for this VLAN.
        ``attribute type:`` model
        """
        return self.broker.vlan_member(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device to which the interface belongs.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IfVlanID": self.IfVlanID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"IfVlanID": self.IfVlanID})
