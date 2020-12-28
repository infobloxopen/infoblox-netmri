from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class AccessChangeAccountingRemote(RemoteModel):
    """
    Accounting information on provisioning activity with SDC


    |  ``AccessChangeAccountingID:`` The internal NetMRI identifier for this access accounting element.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device for which we count the access statistics.
    |  ``attribute type:`` number

    |  ``FilterSetAll:`` The number of all rule lists defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``FilterSetUnused:`` The number of unused rule lists defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``FilterSetAdded:`` The number of rule lists added by provisioning with NetMRI.
    |  ``attribute type:`` number

    |  ``FilterSetRemoved:`` The number of rule lists removed by provisioning with NetMRI (including remediation).
    |  ``attribute type:`` number

    |  ``FilterAll:`` The number of all rules defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``FilterUnused:`` The number of unused rules defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``FilterAdded:`` The number of rules added by provisioning with NetMRI (including rollback operations).
    |  ``attribute type:`` number

    |  ``FilterRemoved:`` The number of rules removed by provisioning with NetMRI (including remediation).
    |  ``attribute type:`` number

    |  ``IPObjectAll:`` The number of network objects defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``IPObjectUnused:`` The number of network objects defined in the device's configuration that are not used in the configuration.
    |  ``attribute type:`` number

    |  ``IPObjectAdded:`` The number of network objects added by provisioning with NetMRI.
    |  ``attribute type:`` number

    |  ``IPObjectRemoved:`` The number of network objects removed by provisioning with NetMRI (including remediation).
    |  ``attribute type:`` number

    |  ``ServiceAll:`` The number of service objects defined in the device's configuration.
    |  ``attribute type:`` number

    |  ``ServiceUnused:`` The number of service objects defined in the device's configuration that are not used in the configuration.
    |  ``attribute type:`` number

    |  ``ServiceAdded:`` The number of service objects added by provisioning with NetMRI.
    |  ``attribute type:`` number

    |  ``ServiceRemoved:`` The number of service objects removed by provisioning with NetMRI (including remediation).
    |  ``attribute type:`` number

    |  ``ACAFirstSeenTime:`` The timestamp of when NetMRI recorded its first access statistic for this device.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``ACAStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ACAEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ACATimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``ACAChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("AccessChangeAccountingID",
                  "DeviceID",
                  "FilterSetAll",
                  "FilterSetUnused",
                  "FilterSetAdded",
                  "FilterSetRemoved",
                  "FilterAll",
                  "FilterUnused",
                  "FilterAdded",
                  "FilterRemoved",
                  "IPObjectAll",
                  "IPObjectUnused",
                  "IPObjectAdded",
                  "IPObjectRemoved",
                  "ServiceAll",
                  "ServiceUnused",
                  "ServiceAdded",
                  "ServiceRemoved",
                  "ACAFirstSeenTime",
                  "DataSourceID",
                  "ACAStartTime",
                  "ACAEndTime",
                  "ACATimestamp",
                  "ACAChangedCols",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"AccessChangeAccountingID": self.AccessChangeAccountingID})
