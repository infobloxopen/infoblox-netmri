from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class IprgMemberRemote(RemoteModel):
    """
    Details of the HSRP/VRRP group memberships.



    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``IprgMemberStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``IprgMemberEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``IprgMemberTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``IprgMemberChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``IprgMemberID:`` The internal NetMRI identifier for this HSRP/VRRP membership.
    |  ``attribute type:`` number

    |  ``IprgID:`` The internal NetMRI identifier for the HSRP/VRRP group to which this membership pertains.
    |  ``attribute type:`` number



    |  ``InterfaceID:`` The internal NetMRI identifier of the interface configured with this HSRP/VRRP membership.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier of the device configured with this HSRP/VRRP membership.
    |  ``attribute type:`` number

    |  ``IprgMemberPriority:`` The router's priority in this HSRP or VRRP.
    |  ``attribute type:`` number

    |  ``IprgMemberPreemptInd:`` A flag indicating whether this router is configured to preempt lower priority routers.
    |  ``attribute type:`` bool

    |  ``IprgMemberPreemptDelay:`` The number of seconds after booting that preemption is enabled. This prevents a router with an unpopulated routing table from preempting until the routing table is ready.
    |  ``attribute type:`` number

    |  ``IprgMemberUseConfiguredTimersInd:`` A flag indicating whether to use the configured or learned timer values.
    |  ``attribute type:`` bool

    |  ``IprgMemberConfiguredHelloTime:`` The configured hello or advertise interval.
    |  ``attribute type:`` number

    |  ``IprgMemberConfiguredHoldTime:`` The configured hold time or master down interval.
    |  ``attribute type:`` number

    |  ``IprgMemberLearnedHelloTime:`` The learned hello or advertise interval.
    |  ``attribute type:`` number

    |  ``IprgMemberLearnedHoldTime:`` The learned hold time or master down interval.
    |  ``attribute type:`` number

    |  ``IprgMemberVirtualIPDotted:`` The virtual IP address for the associated HSRP/VRRP group, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``IprgMemberVirtualIPNumeric:`` The numerical value of the HSRP/VRRP virtual IP address.
    |  ``attribute type:`` number

    |  ``IprgMemberUseConfigVirtualIPInd:`` A flag indicating whether to use the configured or learned virtual IP value.
    |  ``attribute type:`` bool

    |  ``IprgMemberActiveIPDotted:`` The IP address for the active or master router, according to this device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``IprgMemberActiveIPNumeric:`` The numerical IP address for the active or master router, according to this device.
    |  ``attribute type:`` number


    |  ``IprgMemberActiveDeviceID:`` The internal NetMRI identifier of the device that this router believes is the current active/master router.
    |  ``attribute type:`` number

    |  ``IprgMemberStandbyIPDotted:`` The IP address for the standby or backup router, according to this device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``IprgMemberStandbyIPNumeric:`` The numerical IP address for the standby or backup router, according to this device.
    |  ``attribute type:`` number


    |  ``IprgMemberStandbyDeviceID:`` The internal NetMRI identifier of the device that this router believes is the current standby/backup router.
    |  ``attribute type:`` number

    |  ``IprgMemberState:`` The current HSRP or VRRP state of this router for this HSRP/VRRP group.
    |  ``attribute type:`` string

    |  ``IprgMemberStandbyInterfaceID:`` The internal NetMRI identifier of the interface corresponding to the standby/backup IP address, if available.
    |  ``attribute type:`` number

    |  ``IprgMemberActiveInterfaceID:`` The internal NetMRI identifier of the interface corresponding to the active/master IP address, if available.
    |  ``attribute type:`` number




    """

    properties = ("DataSourceID",
                  "IprgMemberStartTime",
                  "IprgMemberEndTime",
                  "IprgMemberTimestamp",
                  "IprgMemberChangedCols",
                  "IprgMemberID",
                  "IprgID",
                  "InterfaceID",
                  "DeviceID",
                  "IprgMemberPriority",
                  "IprgMemberPreemptInd",
                  "IprgMemberPreemptDelay",
                  "IprgMemberUseConfiguredTimersInd",
                  "IprgMemberConfiguredHelloTime",
                  "IprgMemberConfiguredHoldTime",
                  "IprgMemberLearnedHelloTime",
                  "IprgMemberLearnedHoldTime",
                  "IprgMemberVirtualIPDotted",
                  "IprgMemberVirtualIPNumeric",
                  "IprgMemberUseConfigVirtualIPInd",
                  "IprgMemberActiveIPDotted",
                  "IprgMemberActiveIPNumeric",
                  "IprgMemberActiveDeviceID",
                  "IprgMemberStandbyIPDotted",
                  "IprgMemberStandbyIPNumeric",
                  "IprgMemberStandbyDeviceID",
                  "IprgMemberState",
                  "IprgMemberStandbyInterfaceID",
                  "IprgMemberActiveInterfaceID",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def iprg(self):
        """
        The HSRP/VRRP group to which this membership pertains.
        ``attribute type:`` model
        """
        return self.broker.iprg(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def interface(self):
        """
        The interface configured with this HSRP/VRRP membership.
        ``attribute type:`` model
        """
        return self.broker.interface(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def device(self):
        """
        The device configured with this HSRP/VRRP membership.
        ``attribute type:`` model
        """
        return self.broker.device(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def active_router(self):
        """
        The device that this router believes is the current active or master device.
        ``attribute type:`` model
        """
        return self.broker.active_router(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def standby_router(self):
        """
        The device that this router believes is the current standby or backup device.
        ``attribute type:`` model
        """
        return self.broker.standby_router(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def active_interface(self):
        """
        The interface object corresponding to the active/master IP address, if available.
        ``attribute type:`` model
        """
        return self.broker.active_interface(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def standby_interface(self):
        """
        The interface object corresponding to the  standby/backup IP address, if available.
        ``attribute type:`` model
        """
        return self.broker.standby_interface(**{"IprgMemberID": self.IprgMemberID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device configured with this HSRP/VRRP membership.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"IprgMemberID": self.IprgMemberID})
