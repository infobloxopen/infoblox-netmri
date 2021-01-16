from ..remote import RemoteModel


class CdpNeighborDeviceViewerGridRemote(RemoteModel):
    """
    This table lists all the CDP Neighbors for a device.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of the device.
    |  ``attribute type:`` number

    |  ``ifName:`` The name of this interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``ifIndex:`` The SNMP interface index of the interface configured with this address.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface configured with this address.
    |  ``attribute type:`` number

    |  ``CDPNeighborIPDotted:`` The management IP address of the neighbor, in dotted (or colon-delimited for IPv6) format, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborIPNumeric:`` The numerical value of the management IP address that was reported by CDP.
    |  ``attribute type:`` number

    |  ``CDPNeighborDeviceID:`` The internal NetMRI identifier for the neighbor device reported by CDP, if available.
    |  ``attribute type:`` number

    |  ``CDPNeighborDeviceType:`` The NetMRI-determined device type for the neighbor.
    |  ``attribute type:`` string

    |  ``CDPNeighborDescription:`` The description of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborIfName:`` The name of the neighbor's interface. This is typically the short name of the interface as it is identified in the console.
    |  ``attribute type:`` string

    |  ``CDPNeighborInterfaceID:`` The internal NetMRI identifier for the neighbor interface reported by CDP, if available.
    |  ``attribute type:`` number

    |  ``CDPNeighborVersion:`` The version of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborIfIndex:`` The SNMP index for the neighbor interface reported by CDP, if available.
    |  ``attribute type:`` number

    |  ``CDPNeighborPlatform:`` The platform description of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborCapabilities:`` The neighbor capabilities, as reported by CDP.
    |  ``attribute type:`` string

    |  ``CDPNeighborMAC:`` The Media Access Controller (MAC) address of the neighbor, as reported by CDP.
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` A flag indicating whether or not this interface is available for port control actions.
    |  ``attribute type:`` bool

    |  ``ifNameSort:`` The internal NetMRI name of this interface for sorting purpose.
    |  ``attribute type:`` string

    |  ``CDPNeighborIfNameSort:`` The internal NetMRI name of this interface for sorting purpose.
    |  ``attribute type:`` string

    |  ``Network:`` Indicates the Network view which the interface is associated to.
    |  ``attribute type:`` string

    |  ``CDPNeighborIfNetwork:`` Indicates the Network view which the neighbor's interface is associated to.
    |  ``attribute type:`` string

    |  ``VirtualNetworkMemberName:`` The name of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``CDPVirtualNetworkMemberName:`` The name of the VRF as configured on this device.
    |  ``attribute type:`` string

    |  ``CDPNeighborIfVirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "ifIndex",
                  "InterfaceID",
                  "CDPNeighborIPDotted",
                  "CDPNeighborIPNumeric",
                  "CDPNeighborDeviceID",
                  "CDPNeighborDeviceType",
                  "CDPNeighborDescription",
                  "CDPNeighborIfName",
                  "CDPNeighborInterfaceID",
                  "CDPNeighborVersion",
                  "CDPNeighborIfIndex",
                  "CDPNeighborPlatform",
                  "CDPNeighborCapabilities",
                  "CDPNeighborMAC",
                  "ifPortControlInd",
                  "ifNameSort",
                  "CDPNeighborIfNameSort",
                  "Network",
                  "CDPNeighborIfNetwork",
                  "VirtualNetworkMemberName",
                  "VirtualNetworkID",
                  "CDPVirtualNetworkMemberName",
                  "CDPNeighborIfVirtualNetworkID",
                  )
