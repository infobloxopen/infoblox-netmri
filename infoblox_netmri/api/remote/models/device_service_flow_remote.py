from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceServiceFlowRemote(RemoteModel):
    """
    Network flow definition - protocol and ports


    |  ``DeviceServiceFlowID:`` The internal NetMRI identifier for this flow description.
    |  ``attribute type:`` number

    |  ``DeviceServiceID:`` The internal NetMRI identifier for the service to which belongs this flow.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this flow.
    |  ``attribute type:`` number

    |  ``SvfFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this flow.
    |  ``attribute type:`` datetime

    |  ``SvfProtocolNum:`` The protocol number of the flow. A value between 0 to 255, 0 is for generic ip protocol.
    |  ``attribute type:`` number

    |  ``SvfProtocolName:`` The protocol name.
    |  ``attribute type:`` string

    |  ``SvfSrcDisplayText:`` The text that was defined in the configuration for the source port part of this flow.
    |  ``attribute type:`` string

    |  ``SvfSrcPortMin:`` The numeric value for the source port range min value. -1 if no meaning.
    |  ``attribute type:`` number

    |  ``SvfSrcPortMax:`` The numeric value for the source port range max value. -1 if no meaning.
    |  ``attribute type:`` number

    |  ``SvfDestDisplayText:`` The text that was defined in the configuration for the destination port part of this flow.
    |  ``attribute type:`` string

    |  ``SvfDestPortMin:`` The numeric value for the destination port range min value. -1 if no meaning.
    |  ``attribute type:`` number

    |  ``SvfDestPortMax:`` The numeric value for the destination port range max value. -1 if no meaning.
    |  ``attribute type:`` number




    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``SvfStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``SvfEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SvfTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SvfChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceServiceFlowID",
                  "DeviceServiceID",
                  "DeviceID",
                  "SvfFirstSeenTime",
                  "SvfProtocolNum",
                  "SvfProtocolName",
                  "SvfSrcDisplayText",
                  "SvfSrcPortMin",
                  "SvfSrcPortMax",
                  "SvfDestDisplayText",
                  "SvfDestPortMin",
                  "SvfDestPortMax",
                  "DataSourceID",
                  "SvfStartTime",
                  "SvfEndTime",
                  "SvfTimestamp",
                  "SvfChangedCols",
                  )

    @property
    @check_api_availability
    def device_service(self):
        """
        The service object to which this flow belongs.
        ``attribute type:`` model
        """
        return self.broker.device_service(**{"DeviceServiceFlowID": self.DeviceServiceFlowID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceServiceFlowID": self.DeviceServiceFlowID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceServiceFlowID": self.DeviceServiceFlowID})
