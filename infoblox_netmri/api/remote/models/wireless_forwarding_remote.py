from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class WirelessForwardingRemote(RemoteModel):
    """
    The wireless forwarding information per device was collected in the NetMRI.


    |  ``WirelessFwdID:`` The internal NetMRI identifier for this wireless forwarding.
    |  ``attribute type:`` number

    |  ``WirelessFwdStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``WirelessFwdEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``WirelessFwdChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``WirelessFwdTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI Identifier for the device from which wireless forwarding entry was collected.
    |  ``attribute type:`` number

    |  ``RemoteDeviceID:`` The internal NetMRI identifier for the remote host in the wireless relationship.
    |  ``attribute type:`` number

    |  ``RemoteMAC:`` The Media Access Controller(MAC) of the remote host.
    |  ``attribute type:`` string

    |  ``RemoteIPDotted:`` The management IP address of the wireless forwarding, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``RemoteIPNumeric:`` The numerical values of the wireless IP address.
    |  ``attribute type:`` number

    |  ``RemoteStatus:`` The operational status(up/down) of this interface.
    |  ``attribute type:`` string

    |  ``RemoteUsername:`` The username that initiated this session.
    |  ``attribute type:`` string

    |  ``RemoteClass:`` The class that initiated this session.
    |  ``attribute type:`` string

    |  ``AssociatedSSID:`` The internal NetMRI identifier of this associated wireless forwarding entry was collected.
    |  ``attribute type:`` number

    |  ``AssociatedVlan:`` The VLAN on which the wireless forwarding entry was found.
    |  ``attribute type:`` string

    |  ``VlanID:`` The internal NetMRI identifier of the  VLAN.
    |  ``attribute type:`` number

    |  ``CurrentBSS:`` The CurrentBSS of the wireless forwarding entry was found within NetMRI.
    |  ``attribute type:`` string

    |  ``CurrentBSSDeviceID:`` The internal NetMRI identifier for each device of the CurrentBSS.
    |  ``attribute type:`` number




    |  ``AccessPointMAC:`` The MAC address of the Access Point with which the remote host is associated.
    |  ``attribute type:`` string

    |  ``AccessPointDeviceID:`` The internal NetMRI identifier for each device of the AccessPointMAC.
    |  ``attribute type:`` number

    """

    properties = ("WirelessFwdID",
                  "WirelessFwdStartTime",
                  "WirelessFwdEndTime",
                  "WirelessFwdChangedCols",
                  "WirelessFwdTimestamp",
                  "DataSourceID",
                  "DeviceID",
                  "RemoteDeviceID",
                  "RemoteMAC",
                  "RemoteIPDotted",
                  "RemoteIPNumeric",
                  "RemoteStatus",
                  "RemoteUsername",
                  "RemoteClass",
                  "AssociatedSSID",
                  "AssociatedVlan",
                  "VlanID",
                  "CurrentBSS",
                  "CurrentBSSDeviceID",
                  "AccessPointMAC",
                  "AccessPointDeviceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"WirelessFwdID": self.WirelessFwdID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"WirelessFwdID": self.WirelessFwdID})

    @property
    @check_api_availability
    def vlan(self):
        """
        vlan
        ``attribute type:`` model
        """
        return self.broker.vlan(**{"WirelessFwdID": self.WirelessFwdID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"WirelessFwdID": self.WirelessFwdID})
