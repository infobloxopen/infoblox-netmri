from ..remote import RemoteModel


class SpmHistoryDeviceHistoryGridRemote(RemoteModel):
    """
    This table lists the SPM device history within the user specified period of time for a given device.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this device.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this device.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The NetMRI internal identifier for the device.
    |  ``attribute type:`` number

    |  ``DeviceName:`` The NetMRI name of the device; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``DeviceDNSName:`` The device name as reported by DNS.
    |  ``attribute type:`` string

    |  ``DeviceSysLocation:`` The device sysLocation as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceSysDescr:`` The device sysDescr as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` The device vendor name.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The device model name.
    |  ``attribute type:`` string

    |  ``PhysicalSerialNum:`` The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present).
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``PollDuration:`` Number of seconds it took to poll the device.
    |  ``attribute type:`` number

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``Network:`` Indicates the network view which the device is associated to.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "FirstSeen",
                  "LastSeen",
                  "DeviceID",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceDNSName",
                  "DeviceSysLocation",
                  "DeviceSysDescr",
                  "DeviceVendor",
                  "DeviceModel",
                  "PhysicalSerialNum",
                  "DeviceType",
                  "PollDuration",
                  "VirtualNetworkID",
                  "Network",
                  )
