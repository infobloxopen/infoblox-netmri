from ..remote import RemoteModel


class WirelessHotStandbyGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbTimestamp:`` none
    |  ``attribute type:`` string

    |  ``MonitoredIPDotted:`` none
    |  ``attribute type:`` string

    |  ``MonitoredIPNumeric:`` none
    |  ``attribute type:`` string

    |  ``MonitoredDevice:`` none
    |  ``attribute type:`` string

    |  ``MonitoredDeviceID:`` none
    |  ``attribute type:`` string

    |  ``MonitoredDeviceType:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbMAC:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbInd:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbStatus:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbState:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbPollingFeq:`` none
    |  ``attribute type:`` string

    |  ``WlsHotSbPollingTimeout:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "WlsHotSbTimestamp",
                  "MonitoredIPDotted",
                  "MonitoredIPNumeric",
                  "MonitoredDevice",
                  "MonitoredDeviceID",
                  "MonitoredDeviceType",
                  "WlsHotSbMAC",
                  "WlsHotSbInd",
                  "WlsHotSbStatus",
                  "WlsHotSbState",
                  "WlsHotSbPollingFeq",
                  "WlsHotSbPollingTimeout",
                  )
