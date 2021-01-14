from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceCfgContextRemote(RemoteModel):
    """
    Filtering configuration definition context, use to defines scope of names inside a whole configuration


    |  ``DeviceCfgContextID:`` The internal NetMRI identifier of this Configuration context of declaration.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this context definition.
    |  ``attribute type:`` number

    |  ``CfgFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this context definition.
    |  ``attribute type:`` datetime

    |  ``CfgName:`` The name associated with this context.
    |  ``attribute type:`` string

    |  ``CfgProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string



    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``CfgStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``CfgEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``CfgTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``CfgChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceCfgContextID",
                  "DeviceID",
                  "CfgFirstSeenTime",
                  "CfgName",
                  "CfgProvisionData",
                  "DataSourceID",
                  "CfgStartTime",
                  "CfgEndTime",
                  "CfgTimestamp",
                  "CfgChangedCols",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceCfgContextID": self.DeviceCfgContextID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceCfgContextID": self.DeviceCfgContextID})
