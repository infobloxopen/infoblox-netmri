from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceFilterRemote(RemoteModel):
    """
    Network traffic rules; on most routers and firewalls, this corresponds to an access control list entry. In JunOS packet mode configurations, it corresponds to a rule (a collection of terms).


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number




    |  ``DeviceFilterID:`` The internal NetMRI identifier for the rule.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which this rule belongs.
    |  ``attribute type:`` number

    |  ``DeviceServiceID:`` The internal NetMRI identifier for the service (ports, protocol).
    |  ``attribute type:`` number

    |  ``SrcDeviceObjectID:`` The internal NetMRI identifier for the source network object.
    |  ``attribute type:`` number

    |  ``DestDeviceObjectID:`` The internal NetMRI identifier for the destination network object.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier for the  rule to which this rule belongs.
    |  ``attribute type:`` number

    |  ``FltFirstSeenTime:`` The timestamp of when NetMRI first discovered this rule.
    |  ``attribute type:`` datetime

    |  ``FltStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``FltEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``FltTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``FltChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``FltOrder:`` The numerical order of this rule in its rule list.
    |  ``attribute type:`` number

    |  ``FltKey:`` The computed key value that identifies this rule against text configuration.
    |  ``attribute type:`` string

    |  ``FltAllowInd:`` A flag indicator for allowance of rule.
    |  ``attribute type:`` bool

    |  ``FltRelevantInd:`` A flag indicating whether this rule is relevant for search operations.
    |  ``attribute type:`` bool

    |  ``FltEnabledInd:`` A flag indicating whether this rule is enabled in the configuration or not.
    |  ``attribute type:`` bool

    |  ``FltEstablishedInd:`` A flag indicating whether this rule has the option 'established' (cisco specific).
    |  ``attribute type:`` bool

    |  ``FltArtificialInd:`` A flag indicating that this rule has no counterpart in the device configuration.
    |  ``attribute type:`` bool

    |  ``FltConfigText:`` The original text of the configuration from witch this rule is built.
    |  ``attribute type:`` string

    |  ``FltProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string




    """

    properties = ("DataSourceID",
                  "DeviceFilterID",
                  "DeviceID",
                  "DeviceServiceID",
                  "SrcDeviceObjectID",
                  "DestDeviceObjectID",
                  "DeviceFilterSetID",
                  "FltFirstSeenTime",
                  "FltStartTime",
                  "FltEndTime",
                  "FltTimestamp",
                  "FltChangedCols",
                  "FltOrder",
                  "FltKey",
                  "FltAllowInd",
                  "FltRelevantInd",
                  "FltEnabledInd",
                  "FltEstablishedInd",
                  "FltArtificialInd",
                  "FltConfigText",
                  "FltProvisionData",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceFilterID": self.DeviceFilterID})

    @property
    @check_api_availability
    def src_device_object(self):
        """
        The network object for the source of the filtered traffic.
        ``attribute type:`` model
        """
        return self.broker.src_device_object(**{"DeviceFilterID": self.DeviceFilterID})

    @property
    @check_api_availability
    def dest_device_object(self):
        """
        The network object for the destination of the filtered traffic.
        ``attribute type:`` model
        """
        return self.broker.dest_device_object(**{"DeviceFilterID": self.DeviceFilterID})

    @property
    @check_api_availability
    def device_service(self):
        """
        The service object of this rule
        ``attribute type:`` model
        """
        return self.broker.device_service(**{"DeviceFilterID": self.DeviceFilterID})

    @property
    @check_api_availability
    def device_filter_set(self):
        """
        The rule list to which that rule belongs
        ``attribute type:`` model
        """
        return self.broker.device_filter_set(**{"DeviceFilterID": self.DeviceFilterID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceFilterID": self.DeviceFilterID})
