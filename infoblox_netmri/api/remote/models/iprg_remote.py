from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IprgRemote(RemoteModel):
    """
    The HSRP/VRRP groups present on the network (IPRG stands for IP Redundancy Group).



    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``IprgStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``IprgEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``IprgTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``IprgChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``IprgID:`` The internal NetMRI identifier for this HSRP/VRRP Group.
    |  ``attribute type:`` number

    |  ``IprgNumber:`` The HSRP or VRRP group number.
    |  ``attribute type:`` number

    |  ``IprgIPDotted:`` The virtual IP address for this HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``IprgIPNumeric:`` The numerical value of the HSRP/VRRP virtual IP address.
    |  ``attribute type:`` number

    |  ``IprgMAC:`` The virtual MAC for this HSRP or VRRP group.
    |  ``attribute type:`` string

    |  ``IprgType:`` Designates if this is an HSRP group or a VRRP group.
    |  ``attribute type:`` string

    |  ``IprgAuth:`` The authentication method for this HSRP or VRRP group.
    |  ``attribute type:`` string

    |  ``IprgActiveLastChanged:`` The date and time of the last change of the active or master router for this group.
    |  ``attribute type:`` datetime

    |  ``ActiveIprgMemberID:`` The internal NetMRI identifier for the HSRP/VRRP group membership details of the active router.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "IprgStartTime",
                  "IprgEndTime",
                  "IprgTimestamp",
                  "IprgChangedCols",
                  "IprgID",
                  "IprgNumber",
                  "IprgIPDotted",
                  "IprgIPNumeric",
                  "IprgMAC",
                  "IprgType",
                  "IprgAuth",
                  "IprgActiveLastChanged",
                  "ActiveIprgMemberID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IprgID": self.IprgID})

    @property
    @check_api_availability
    def active_member(self):
        """
        The HSRP/VRRP group membership details of the active router.
        ``attribute type:`` model
        """
        return self.broker.active_member(**{"IprgID": self.IprgID})
