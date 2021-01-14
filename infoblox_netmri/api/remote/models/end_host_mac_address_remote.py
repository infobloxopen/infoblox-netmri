from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class EndHostMacAddressRemote(RemoteModel):
    """
    MAC Addresses of end hosts on the network.


    |  ``EndHostMACAddressID:`` The internal NetMRI identifier for the End Host MAC Address entry.
    |  ``attribute type:`` number

    |  ``NetworkID:`` The internal NetMRI identifier of the associated network.
    |  ``attribute type:`` number

    |  ``MACAddress:`` The MAC address of the end host.
    |  ``attribute type:`` string

    |  ``IPAddress:`` The IP address of the end host.
    |  ``attribute type:`` string

    |  ``IPAddressNumeric:`` The IP address of the end host, in numerical form.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceType:`` The determined type of the end host.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The determined name of the end host.
    |  ``attribute type:`` string

    |  ``DeviceNetBIOSName:`` The NetBIOS name of the end host.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The internal NetMRI identifier for the associated Device record.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The interface index on which the end host was found.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the interface on which the end host was found.
    |  ``attribute type:`` number

    |  ``InfraDeviceID:`` The internal NetMRI identifier for the InfraDevice on which the end host was found.
    |  ``attribute type:`` number

    |  ``NeighborID:`` The internal NetMRI identifier for the associated Neighbor record.
    |  ``attribute type:`` number

    |  ``EndHostMACAddressTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``FirstSeenTime:`` The date and time this record was first seen.
    |  ``attribute type:`` datetime

    |  ``EndHostMACAddressStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``EndHostMACAddressEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``EndHostMACAddressChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    """

    properties = ("EndHostMACAddressID",
                  "NetworkID",
                  "MACAddress",
                  "IPAddress",
                  "IPAddressNumeric",
                  "DataSourceID",
                  "DeviceType",
                  "DeviceName",
                  "DeviceNetBIOSName",
                  "DeviceID",
                  "ifIndex",
                  "InterfaceID",
                  "InfraDeviceID",
                  "NeighborID",
                  "EndHostMACAddressTimestamp",
                  "FirstSeenTime",
                  "EndHostMACAddressStartTime",
                  "EndHostMACAddressEndTime",
                  "EndHostMACAddressChangedCols",
                  "Network",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"EndHostMACAddressID": self.EndHostMACAddressID})
