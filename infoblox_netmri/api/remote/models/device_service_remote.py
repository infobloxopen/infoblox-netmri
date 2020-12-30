from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceServiceRemote(RemoteModel):
    """
    Network services defined on the supported traffic filtering devices.


    |  ``DeviceServiceID:`` The internal NetMRI identifier for the Service.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device that holds this service.
    |  ``attribute type:`` number

    |  ``DeviceCfgContextID:`` The internal NetMRI identifier of the Configuration context of declaration of this service.
    |  ``attribute type:`` number

    |  ``SvcFirstSeenTime:`` The timestamp of when NetMRI first discovered this service.
    |  ``attribute type:`` datetime

    |  ``SvcName:`` Name of this service.
    |  ``attribute type:`` string

    |  ``SvcUseCount:`` Total count of usage of this service by other elements of the configuration (rules, other services).
    |  ``attribute type:`` number

    |  ``SvcArtificialInd:`` Flag indicating this service does not exist in the device configuration.
    |  ``attribute type:`` bool

    |  ``SvcType:`` A string indicating the kind of service that element is describing. One of : service, container, protLst, prtLst, protPrtLst.
    |  ``attribute type:`` string

    |  ``SvcConfigText:`` Original text of the definition of this service in the device configuration.
    |  ``attribute type:`` string

    |  ``SvcProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string




    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``SvcStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``SvcEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SvcTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SvcChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceServiceID",
                  "DeviceID",
                  "DeviceCfgContextID",
                  "SvcFirstSeenTime",
                  "SvcName",
                  "SvcUseCount",
                  "SvcArtificialInd",
                  "SvcType",
                  "SvcConfigText",
                  "SvcProvisionData",
                  "DataSourceID",
                  "SvcStartTime",
                  "SvcEndTime",
                  "SvcTimestamp",
                  "SvcChangedCols",
                  )

    @property
    @check_api_availability
    def device_cfg_context(self):
        """
        The Configuration context of declaration of this service.
        ``attribute type:`` model
        """
        return self.broker.device_cfg_context(**{"DeviceServiceID": self.DeviceServiceID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceServiceID": self.DeviceServiceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceServiceID": self.DeviceServiceID})
