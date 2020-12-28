from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceFilterSetRemote(RemoteModel):
    """
    Network traffic rule lists; on most routers and firewalls, this corresponds to an access control list. In JunOS packet mode configurations, it corresponds to a rule-set.


    |  ``DeviceFilterSetID:`` The internal NetMRI identifier for this rule list.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which this rule list belongs.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``FltSetFirstSeenTime:`` The timestamp of when NetMRI first discovered this rule list.
    |  ``attribute type:`` datetime

    |  ``FltSetStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``FltSetEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``FltSetTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``FltSetChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``FltSetName:`` The name of this rule-list.
    |  ``attribute type:`` string

    |  ``FltSetIPVersion:`` the IP version of the packets filtered by this rule list - default is 4.
    |  ``attribute type:`` number

    |  ``FltSetUseCount:`` The number of usage of this rule list inside the configuration (may be for filtering or for NAT, vpn etc).
    |  ``attribute type:`` number

    |  ``FltSetArtificialInd:`` A flag indicating that this rule list has no counterpart in the device configuration.
    |  ``attribute type:`` bool

    |  ``FltSetConfigText:`` The original text of the definition of this rule list in the device configuration.
    |  ``attribute type:`` string

    |  ``FltSetProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string


    """

    properties = ("DeviceFilterSetID",
                  "DeviceID",
                  "DataSourceID",
                  "FltSetFirstSeenTime",
                  "FltSetStartTime",
                  "FltSetEndTime",
                  "FltSetTimestamp",
                  "FltSetChangedCols",
                  "FltSetName",
                  "FltSetIPVersion",
                  "FltSetUseCount",
                  "FltSetArtificialInd",
                  "FltSetConfigText",
                  "FltSetProvisionData",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceFilterSetID": self.DeviceFilterSetID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceFilterSetID": self.DeviceFilterSetID})
