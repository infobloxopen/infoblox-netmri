from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class VrfRouteTargetRemote(RemoteModel):
    """
    The import and export route targets for a Virtual Network Member.


    |  ``VrfRouteTargetStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``VrfRouteTargetEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``VrfRouteTargetChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``VrfRouteTargetTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``VrfRouteTargetFirstTime:`` The first time this data element was seen on the network.
    |  ``attribute type:`` datetime


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this data was collected.
    |  ``attribute type:`` number


    |  ``VrfDirection:`` The direction of the RT (import or export).
    |  ``attribute type:`` string

    |  ``VrfMemberID:`` The NetMRI internal identifier for the VRF membership record to which this route target applies.
    |  ``attribute type:`` number

    |  ``VirtualNetworkMemberID:`` The internal NetMRI identifier for the Virtual Network Member that corresponds to this VRF route target.
    |  ``attribute type:`` number

    |  ``VrfRouteTargetID:`` The internal NetMRI identifier for this VRF route target.
    |  ``attribute type:`` number

    |  ``RTType:`` The style of the route target, asn or ipv4.
    |  ``attribute type:`` string

    |  ``RTLeftSide:`` The left-hand portion of the route target; use Type to identify if it is an AS number or and IPv4 address.
    |  ``attribute type:`` number

    |  ``RTRightSide:`` The right-hand portion of the route target.
    |  ``attribute type:`` number

    """

    properties = ("VrfRouteTargetStartTime",
                  "VrfRouteTargetEndTime",
                  "VrfRouteTargetChangedCols",
                  "VrfRouteTargetTimestamp",
                  "VrfRouteTargetFirstTime",
                  "DataSourceID",
                  "DeviceID",
                  "VrfDirection",
                  "VrfMemberID",
                  "VirtualNetworkMemberID",
                  "VrfRouteTargetID",
                  "RTType",
                  "RTLeftSide",
                  "RTRightSide",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The internal NetMRI identifier for the collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"VrfRouteTargetID": self.VrfRouteTargetID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this VRF route target configuration was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"VrfRouteTargetID": self.VrfRouteTargetID})
