from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DataCollectionStatusRemote(RemoteModel):
    """
    status and time of last collections


    |  ``DeviceID:`` The internal NetMRI identifier for the device on which collection applied.
    |  ``attribute type:`` number

    |  ``SystemInd:`` The indicator of collection of system information.
    |  ``attribute type:`` string

    |  ``CPUInd:`` The indicator of collection of cpu information.
    |  ``attribute type:`` string

    |  ``MemoryInd:`` The indicator of collection of memory information.
    |  ``attribute type:`` string

    |  ``VlansInd:`` The indicator of collection of virtual LAN information.
    |  ``attribute type:`` string

    |  ``ForwardingInd:`` The indicator of collection of forwarding information.
    |  ``attribute type:`` string

    |  ``EnvironmentalInd:`` The indicator of collection of environmental information.
    |  ``attribute type:`` string

    |  ``InventoryInd:`` The indicator of collection of the inventory information.
    |  ``attribute type:`` string

    |  ``ARPInd:`` The indicator of collection of the arp information.
    |  ``attribute type:`` string

    |  ``RouteInd:`` The indicator of collection of the route information.
    |  ``attribute type:`` string

    |  ``NeighborInd:`` The indicator of collection of the neighborhood information.
    |  ``attribute type:`` string

    |  ``ConfigInd:`` The indicator of collection of the configuration information.
    |  ``attribute type:`` string

    |  ``AccessInd:`` The indicator of collection of the filtering access information.
    |  ``attribute type:`` string

    |  ``SystemTimestamp:`` The date and time of last collect of the system information.
    |  ``attribute type:`` datetime

    |  ``CPUTimestamp:`` The date and time of last collect of the cpu information.
    |  ``attribute type:`` datetime

    |  ``MemoryTimestamp:`` The date and time of last collect of the memory information.
    |  ``attribute type:`` datetime

    |  ``VlansTimestamp:`` The date and time of last collect of the virtual LAN information.
    |  ``attribute type:`` datetime

    |  ``ForwardingTimestamp:`` The date and time of last collect of the forwarding information.
    |  ``attribute type:`` datetime

    |  ``EnvironmentalTimestamp:`` The date and time of last collect of the environmental information.
    |  ``attribute type:`` datetime

    |  ``InventoryTimestamp:`` The date and time of last collect of the inventory information.
    |  ``attribute type:`` datetime

    |  ``ARPTimestamp:`` The date and time of last collect of the arp information.
    |  ``attribute type:`` datetime

    |  ``RouteTimestamp:`` The date and time of last collect of the route information.
    |  ``attribute type:`` datetime

    |  ``NeighborTimestamp:`` The date and time of last collect of the neighborhood information.
    |  ``attribute type:`` datetime

    |  ``ConfigTimestamp:`` The date and time of last collect of the configuration information.
    |  ``attribute type:`` datetime

    |  ``AccessTimestamp:`` The date and time of last collect of the filtering access information.
    |  ``attribute type:`` datetime

    |  ``system:`` The indicator of collection of system information.
    |  ``attribute type:`` bool

    |  ``cpu:`` The indicator of collection of cpu information.
    |  ``attribute type:`` bool

    |  ``memory:`` The indicator of collection of memory information.
    |  ``attribute type:`` bool

    |  ``vlans:`` The indicator of collection of virtual LAN information.
    |  ``attribute type:`` bool

    |  ``forwarding:`` The indicator of collection of forwarding information.
    |  ``attribute type:`` bool

    |  ``environmental:`` The indicator of collection of environmental information.
    |  ``attribute type:`` bool

    |  ``inventory:`` The indicator of collection of the inventory information.
    |  ``attribute type:`` bool

    |  ``arp:`` The indicator of collection of the arp information.
    |  ``attribute type:`` bool

    |  ``route:`` The indicator of collection of the route information.
    |  ``attribute type:`` bool

    |  ``neighbor:`` The indicator of collection of the neighborhood information.
    |  ``attribute type:`` bool

    |  ``config:`` The indicator of collection of the configuration information.
    |  ``attribute type:`` bool

    |  ``access:`` The indicator of collection of the filtering access information.
    |  ``attribute type:`` bool


    |  ``VrfInd:`` The indicator of collection of virtual network information.
    |  ``attribute type:`` string

    |  ``VrfTimestamp:`` The date and time of last collect of the virtual network information.
    |  ``attribute type:`` datetime

    """

    properties = ("DeviceID",
                  "SystemInd",
                  "CPUInd",
                  "MemoryInd",
                  "VlansInd",
                  "ForwardingInd",
                  "EnvironmentalInd",
                  "InventoryInd",
                  "ARPInd",
                  "RouteInd",
                  "NeighborInd",
                  "ConfigInd",
                  "AccessInd",
                  "SystemTimestamp",
                  "CPUTimestamp",
                  "MemoryTimestamp",
                  "VlansTimestamp",
                  "ForwardingTimestamp",
                  "EnvironmentalTimestamp",
                  "InventoryTimestamp",
                  "ARPTimestamp",
                  "RouteTimestamp",
                  "NeighborTimestamp",
                  "ConfigTimestamp",
                  "AccessTimestamp",
                  "system",
                  "cpu",
                  "memory",
                  "vlans",
                  "forwarding",
                  "environmental",
                  "inventory",
                  "arp",
                  "route",
                  "neighbor",
                  "config",
                  "access",
                  "VrfInd",
                  "VrfTimestamp",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceID": self.DeviceID})
