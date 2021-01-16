from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class AccessProvisioningDevicesGridRemote(RemoteModel):
    """
    list of devices available for provisioning


    |  ``id:`` The internal NetMRI identifier for this used rule list for a device.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier of the device to which belongs the rule list.
    |  ``attribute type:`` string

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``Collector:`` The NetMRI device that raised this issue.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``DeviceName:`` The NetMRI name of the device.
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` The device vendor name.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The device model name.
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` The assurance level of the device type value.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier of the rule list.
    |  ``attribute type:`` string

    |  ``FltSetName:`` The name the rule list.
    |  ``attribute type:`` string

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``Collector:`` The NetMRI device that raised this issue.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "DeviceID",
                  "Network",
                  "Collector",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceName",
                  "DeviceType",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceAssurance",
                  "DeviceFilterSetID",
                  "FltSetName",
                  "Network",
                  "Collector",
                  "DataSourceID",
                  "VirtualNetworkID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"id": self.id})
