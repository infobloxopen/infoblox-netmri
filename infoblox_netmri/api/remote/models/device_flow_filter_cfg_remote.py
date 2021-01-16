from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceFlowFilterCfgRemote(RemoteModel):
    """
    Network traffic flow configuration, definition of a path of ip flow to rule


    |  ``DeviceFlowFilterCfgID:`` The internal NetMRI identifier for this ip packet flow definition.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this ip packet flow definition
    |  ``attribute type:`` number

    |  ``FfcFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this ip packet flow definition
    |  ``attribute type:`` datetime

    |  ``SrcDeviceZoneID:`` The internal NetMRI identifier of the Zone that is source point for this ip packet flow definition
    |  ``attribute type:`` number

    |  ``DestDeviceZoneID:`` The internal NetMRI identifier of the Zone that is destination point for this ip packet flow definition.
    |  ``attribute type:`` number

    |  ``FfcType:`` The type of operation applied on this ip packet flow definition. One of : 'filter', 'nat', 'vpn',
    |  ``attribute type:`` string

    |  ``FfcDisplayText:`` The associated text for display.
    |  ``attribute type:`` string

    |  ``FfcConfigText:`` The text that was defined in the configuration for this ip packet flow definition.
    |  ``attribute type:`` string

    |  ``FfcProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string





    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``FfcStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``FfcEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``FfcTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``FfcChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``FfcName:`` The name associated with this usage of the rulelist.
    |  ``attribute type:`` string

    |  ``FfcData:`` Extra data for this usage of the rulelist. May depend on the vendor implementation.
    |  ``attribute type:`` string

    """

    properties = ("DeviceFlowFilterCfgID",
                  "DeviceID",
                  "FfcFirstSeenTime",
                  "SrcDeviceZoneID",
                  "DestDeviceZoneID",
                  "FfcType",
                  "FfcDisplayText",
                  "FfcConfigText",
                  "FfcProvisionData",
                  "DataSourceID",
                  "FfcStartTime",
                  "FfcEndTime",
                  "FfcTimestamp",
                  "FfcChangedCols",
                  "FfcName",
                  "FfcData",
                  )

    @property
    @check_api_availability
    def src_device_zone(self):
        """
        The DeviceZone that is source point for this ip packet flow definition.
        ``attribute type:`` model
        """
        return self.broker.src_device_zone(**{"DeviceFlowFilterCfgID": self.DeviceFlowFilterCfgID})

    @property
    @check_api_availability
    def dest_device_zone(self):
        """
        The DeviceZone that is destination point for this ip packet flow definition.
        ``attribute type:`` model
        """
        return self.broker.dest_device_zone(**{"DeviceFlowFilterCfgID": self.DeviceFlowFilterCfgID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceFlowFilterCfgID": self.DeviceFlowFilterCfgID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceFlowFilterCfgID": self.DeviceFlowFilterCfgID})
