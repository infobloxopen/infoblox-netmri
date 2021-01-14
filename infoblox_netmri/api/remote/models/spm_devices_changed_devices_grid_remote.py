from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class SpmDevicesChangedDevicesGridRemote(RemoteModel):
    """
    This table lists SPM devices that have changed within the user specified period of time.


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

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

    |  ``TotalPorts:`` Total number of ports.
    |  ``attribute type:`` number

    |  ``FreePorts:`` Number of free ports.
    |  ``attribute type:`` number

    |  ``FreePortsPercentage:`` Percentage of all ports that are free.
    |  ``attribute type:`` number

    |  ``AvailPorts:`` Number of available ports.
    |  ``attribute type:`` number

    |  ``AvailPortsPercentage:`` Percentage of all ports that are available.
    |  ``attribute type:`` number

    |  ``PoEPorts:`` Number of Power-over-Ethernet ports.
    |  ``attribute type:`` number

    |  ``DeviceSysLocation:`` The device sysLocation as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` The device vendor name.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The device model name.
    |  ``attribute type:`` string

    |  ``PhysicalSerialNum:`` The vendor-specific serial number string for the physical entity. The preferred value is the serial number string actually printed on the component itself (if present).
    |  ``attribute type:`` string

    |  ``DeviceSysDescr:`` The device sysDescr as reported by SNMP.
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``FirstSeen:`` The timestamp of when NetMRI first discovered this device.
    |  ``attribute type:`` datetime

    |  ``LastSeen:`` The timestamp of when NetMRI last polled data from this device.
    |  ``attribute type:`` datetime

    |  ``LastChanged:`` The timestamp of the last change on this device.
    |  ``attribute type:`` string

    |  ``PollDuration:`` Number of seconds it took to poll the device.
    |  ``attribute type:`` number

    |  ``SwitchingInd:`` A flag indicating whether a switch port forwarding table was retrieved from this device.
    |  ``attribute type:`` bool

    |  ``DeviceAssurance:`` Internal use only
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``UsedAccessPorts:`` Used Access Ports
    |  ``attribute type:`` number

    |  ``UsedTrunkPorts:`` Used Trunk Ports
    |  ``attribute type:`` number


    """

    properties = ("id",
                  "Network",
                  "DeviceID",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceDNSName",
                  "TotalPorts",
                  "FreePorts",
                  "FreePortsPercentage",
                  "AvailPorts",
                  "AvailPortsPercentage",
                  "PoEPorts",
                  "DeviceSysLocation",
                  "DeviceVendor",
                  "DeviceModel",
                  "PhysicalSerialNum",
                  "DeviceSysDescr",
                  "DeviceType",
                  "FirstSeen",
                  "LastSeen",
                  "LastChanged",
                  "PollDuration",
                  "SwitchingInd",
                  "DeviceAssurance",
                  "VirtualNetworkID",
                  "UsedAccessPorts",
                  "UsedTrunkPorts",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"id": self.id})
