from ..remote import RemoteModel


class ExcludedDeviceRemote(RemoteModel):
    """
    Banned devices used by the NetMRI discovery engine.


    |  ``ExclusionID:`` The internal NetMRI identifier for this banned device definition.
    |  ``attribute type:`` number

    |  ``SNMPEngineID:`` The unique identifier of the banned device.
    |  ``attribute type:`` string

    |  ``IPAddress:`` The IP address of the banned device.
    |  ``attribute type:`` string

    |  ``UnitID:`` The internal NetMRI identifier for the collector on which the device is banned.
    |  ``attribute type:`` number

    |  ``LastUpdate:`` The date and time the banned device was added to the exclusion list.
    |  ``attribute type:`` timestamp

    |  ``VirtualNetworkName:`` The name of the Network View.
    |  ``attribute type:`` string

    """

    properties = ("ExclusionID",
                  "SNMPEngineID",
                  "IPAddress",
                  "UnitID",
                  "LastUpdate",
                  "VirtualNetworkName",
                  )
