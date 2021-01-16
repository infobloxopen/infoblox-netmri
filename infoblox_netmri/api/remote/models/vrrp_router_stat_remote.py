from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VrrpRouterStatRemote(RemoteModel):
    """
    This table list out the entries of the Vrrp router statistics.


    |  ``VrrpRouterStatsID:`` The internal NetMRI identifier of the Vrrp Router Statistics.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which Vrrp Routes statistics information was collected.
    |  ``attribute type:`` number

    |  ``IprgMemberID:`` The internal NetMRI identifier of Iprg member in the vrrp router statistics.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for the local interface for this Vrrp Router Statistics table entry.
    |  ``attribute type:`` number

    |  ``StartTime:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``ifIndex:`` The SNMP index for the local interface for this Vrrp router statistics table entry.
    |  ``attribute type:`` string

    |  ``IprgNumber:`` The unique IprgNumber in the Vrrp router.
    |  ``attribute type:`` string

    |  ``VrrpBecomeMaster:`` The master of the Vrrp Router Statistics.
    |  ``attribute type:`` string

    |  ``VrrpAdvertiseRcvd:`` The received advertise of the Vrrp router statistics.
    |  ``attribute type:`` string

    |  ``VrrpAdvertiseIntervalErrors:`` The total number of interval errors in the Vrrp Router Statistics.
    |  ``attribute type:`` string

    |  ``VrrpAuthFailures:`` The total number of authentication failures occurred in the Vrrp router statistics.
    |  ``attribute type:`` string

    |  ``VrrpIpTtlErrors:`` The total number of IP address error occurred in the Vrrp Router Statistics.
    |  ``attribute type:`` string

    |  ``VrrpPriorityZeroPktsRcvd:`` The packet received with priority zero.
    |  ``attribute type:`` string

    |  ``VrrpPriorityZeroPktsSent:`` The packet sent with priority zero.
    |  ``attribute type:`` string

    |  ``VrrpInvalidTypePktsRcvd:`` The packet received with Invalid Type.
    |  ``attribute type:`` string

    |  ``VrrpAddressListErrors:`` The number of address list errors in the Vrrp router statistic
    |  ``attribute type:`` string

    |  ``VrrpInvalidAuthType:`` The Invalid Authentication type of Vrrp Router Statistics.
    |  ``attribute type:`` string

    |  ``VrrpAuthTypeMismatch:`` The mismatch authentication type.
    |  ``attribute type:`` string

    |  ``VrrpPacketLengthErrors:`` The number of packet length errors in the Vrrp Router Statistics.
    |  ``attribute type:`` string



    """

    properties = ("VrrpRouterStatsID",
                  "DeviceID",
                  "IprgMemberID",
                  "InterfaceID",
                  "StartTime",
                  "EndTime",
                  "ifIndex",
                  "IprgNumber",
                  "VrrpBecomeMaster",
                  "VrrpAdvertiseRcvd",
                  "VrrpAdvertiseIntervalErrors",
                  "VrrpAuthFailures",
                  "VrrpIpTtlErrors",
                  "VrrpPriorityZeroPktsRcvd",
                  "VrrpPriorityZeroPktsSent",
                  "VrrpInvalidTypePktsRcvd",
                  "VrrpAddressListErrors",
                  "VrrpInvalidAuthType",
                  "VrrpAuthTypeMismatch",
                  "VrrpPacketLengthErrors",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"VrrpRouterStatsID": self.VrrpRouterStatsID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"VrrpRouterStatsID": self.VrrpRouterStatsID})
