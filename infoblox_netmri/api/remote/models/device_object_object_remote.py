from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceObjectObjectRemote(RemoteModel):
    """
    Network Objects cross usage


    |  ``DeviceObjectObjectID:`` The internal NetMRI identifier of this usage relationship between network objects.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this network objects.
    |  ``attribute type:`` number

    |  ``ParentDeviceObjectID:`` The internal NetMRI identifier of the parent network object (the user).
    |  ``attribute type:`` number

    |  ``ChildDeviceObjectID:`` The internal NetMRI identifier of the child network object (the used service).
    |  ``attribute type:`` number

    |  ``OoFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this relationship.
    |  ``attribute type:`` datetime

    |  ``OoProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string





    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``OoStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``OoEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``OoTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``OoChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceObjectObjectID",
                  "DeviceID",
                  "ParentDeviceObjectID",
                  "ChildDeviceObjectID",
                  "OoFirstSeenTime",
                  "OoProvisionData",
                  "DataSourceID",
                  "OoStartTime",
                  "OoEndTime",
                  "OoTimestamp",
                  "OoChangedCols",
                  )

    @property
    @check_api_availability
    def parent_device_object(self):
        """
        The parent network object of this relationship.
        ``attribute type:`` model
        """
        return self.broker.parent_device_object(**{"DeviceObjectObjectID": self.DeviceObjectObjectID})

    @property
    @check_api_availability
    def child_device_object(self):
        """
        The child network object of this relationship.
        ``attribute type:`` model
        """
        return self.broker.child_device_object(**{"DeviceObjectObjectID": self.DeviceObjectObjectID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceObjectObjectID": self.DeviceObjectObjectID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceObjectObjectID": self.DeviceObjectObjectID})
