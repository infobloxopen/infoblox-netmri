from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceObjectRemote(RemoteModel):
    """
    Network objects defined on the supported traffic filtering devices.


    |  ``DeviceObjectID:`` The internal NetMRI identifier for this network object.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which this network object belongs.
    |  ``attribute type:`` number

    |  ``DeviceCfgContextID:`` The internal NetMRI identifier of the Configuration context of declaration of this network object.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``ObjFirstSeenTime:`` The timestamp of when NetMRI first discovered this network object.
    |  ``attribute type:`` datetime

    |  ``ObjStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``ObjEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``ObjTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``ObjChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``ObjName:`` Name of this network object.
    |  ``attribute type:`` string

    |  ``ObjUseCount:`` Total count of usage of this network by other elements of the configuration (rules, other network objects).
    |  ``attribute type:`` number

    |  ``ObjArtificialInd:`` Flag indicating this object network does not exist in the device configuration.
    |  ``attribute type:`` bool

    |  ``ObjConfigText:`` Original text of the definition of his network object in the device configuration.
    |  ``attribute type:`` string

    |  ``ObjProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string



    """

    properties = ("DeviceObjectID",
                  "DeviceID",
                  "DeviceCfgContextID",
                  "DataSourceID",
                  "ObjFirstSeenTime",
                  "ObjStartTime",
                  "ObjEndTime",
                  "ObjTimestamp",
                  "ObjChangedCols",
                  "ObjName",
                  "ObjUseCount",
                  "ObjArtificialInd",
                  "ObjConfigText",
                  "ObjProvisionData",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceObjectID": self.DeviceObjectID})

    @property
    @check_api_availability
    def device_cfg_context(self):
        """
        The configuration context to which this network object belongs.
        ``attribute type:`` model
        """
        return self.broker.device_cfg_context(**{"DeviceObjectID": self.DeviceObjectID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceObjectID": self.DeviceObjectID})
