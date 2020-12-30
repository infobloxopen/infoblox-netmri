from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceServiceServiceRemote(RemoteModel):
    """
    Network services cross usage


    |  ``DeviceServiceServiceID:`` The internal NetMRI identifier of this usage relationship between service objects.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device to which belongs this services.
    |  ``attribute type:`` number

    |  ``ParentDeviceServiceID:`` The internal NetMRI identifier of the parent service (the user).
    |  ``attribute type:`` number

    |  ``ChildDeviceServiceID:`` The internal NetMRI identifier of the child service (the used service).
    |  ``attribute type:`` number

    |  ``SvsvFirstSeenTime:`` The timestamp of when NetMRI saw for the first time this relationship.
    |  ``attribute type:`` datetime

    |  ``SvsvUsage:`` An indicator of the kind of relationship. One of : child, protID, srcPrtID, dstPrtID, protDstID. The regular indicator is 'child'.
    |  ``attribute type:`` string

    |  ``SvsvProvisionData:`` Internal data - do not modify, may change without warning.
    |  ``attribute type:`` string





    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``SvsvStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``SvsvEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``SvsvTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``SvsvChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    """

    properties = ("DeviceServiceServiceID",
                  "DeviceID",
                  "ParentDeviceServiceID",
                  "ChildDeviceServiceID",
                  "SvsvFirstSeenTime",
                  "SvsvUsage",
                  "SvsvProvisionData",
                  "DataSourceID",
                  "SvsvStartTime",
                  "SvsvEndTime",
                  "SvsvTimestamp",
                  "SvsvChangedCols",
                  )

    @property
    @check_api_availability
    def parent_device_service(self):
        """
        The parent service object of this relationship.
        ``attribute type:`` model
        """
        return self.broker.parent_device_service(**{"DeviceServiceServiceID": self.DeviceServiceServiceID})

    @property
    @check_api_availability
    def child_device_service(self):
        """
        The child service object of this relationship.
        ``attribute type:`` model
        """
        return self.broker.child_device_service(**{"DeviceServiceServiceID": self.DeviceServiceServiceID})

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceServiceServiceID": self.DeviceServiceServiceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DeviceServiceServiceID": self.DeviceServiceServiceID})
