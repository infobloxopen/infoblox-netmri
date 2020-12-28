from ..remote import RemoteModel


class LldpNeighborDeviceViewerGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``DeviceID:`` none
    |  ``attribute type:`` string

    |  ``ifName:`` none
    |  ``attribute type:`` string

    |  ``LLPDNeighborIfVirtualNetworkID:`` none
    |  ``attribute type:`` string

    |  ``LLPDNeighborIfNetwork:`` none
    |  ``attribute type:`` string

    |  ``LLPDNeighborIfNetworkMemberName:`` none
    |  ``attribute type:`` string

    |  ``ifNameSort:`` none
    |  ``attribute type:`` string

    |  ``ifIndex:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborPrimaryIPDotted:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborPrimaryIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborPrimaryDeviceID:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborName:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborIfName:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborIfNameSort:`` none
    |  ``attribute type:`` string

    |  ``NeighborDeviceID:`` none
    |  ``attribute type:`` string

    |  ``NeighborIfIndex:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborDescription:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborCapabilities:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborMAC:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborVersion:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborIfIndex:`` none
    |  ``attribute type:`` string

    |  ``LLDPNeighborSecondaryIPDotted:`` none
    |  ``attribute type:`` string

    |  ``ifPortControlInd:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "DeviceID",
                  "ifName",
                  "LLPDNeighborIfVirtualNetworkID",
                  "LLPDNeighborIfNetwork",
                  "LLPDNeighborIfNetworkMemberName",
                  "ifNameSort",
                  "ifIndex",
                  "LLDPNeighborPrimaryIPDotted",
                  "LLDPNeighborPrimaryIPNumeric",
                  "LLDPNeighborPrimaryDeviceID",
                  "LLDPNeighborName",
                  "LLDPNeighborIfName",
                  "LLDPNeighborIfNameSort",
                  "NeighborDeviceID",
                  "NeighborIfIndex",
                  "LLDPNeighborDescription",
                  "LLDPNeighborCapabilities",
                  "LLDPNeighborMAC",
                  "LLDPNeighborVersion",
                  "LLDPNeighborIfIndex",
                  "LLDPNeighborSecondaryIPDotted",
                  "ifPortControlInd",
                  )
