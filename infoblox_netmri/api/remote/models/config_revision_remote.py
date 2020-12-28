from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class ConfigRevisionRemote(RemoteModel):
    """
    Device configuration file revisions.


    |  ``ConfigDiffs:`` A measure of the amount of differences between this configuration revision and the previous revision.
    |  ``attribute type:`` number

    |  ``ConfigRevision:`` The revision number of the file; used internally by NetMRI.
    |  ``attribute type:`` string

    |  ``ConfigRevisionID:`` The internal NetMRI identifier for the configuration file revision.
    |  ``attribute type:`` number

    |  ``ConfigTimestamp:`` The date/time this configuration revision was first collected (i.e., the starting effective time of the configuration).
    |  ``attribute type:`` datetime

    |  ``ConfigType:`` The type of the configuration file: Running or Saved.
    |  ``attribute type:`` string

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device from which this configuration revision was collected.
    |  ``attribute type:`` number

    |  ``LastCollected:`` The last time this revision was collected from the device.
    |  ``attribute type:`` datetime

    |  ``PreviousTimestamp:`` The date/time that the previous configuration revision was first collected.
    |  ``attribute type:`` datetime

    |  ``edited_by:`` The user(s) that modified the file between the last revision and this one.
    |  ``attribute type:`` string



    |  ``text:`` Returns the text of the configuration file.
    |  ``attribute type:`` string



    """

    properties = ("ConfigDiffs",
                  "ConfigRevision",
                  "ConfigRevisionID",
                  "ConfigTimestamp",
                  "ConfigType",
                  "DataSourceID",
                  "DeviceID",
                  "LastCollected",
                  "PreviousTimestamp",
                  "edited_by",
                  "text",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"ConfigRevisionID": self.ConfigRevisionID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this configuration revision was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"ConfigRevisionID": self.ConfigRevisionID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this configuration revision was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"ConfigRevisionID": self.ConfigRevisionID})

    @property
    @check_api_availability
    def devicesetting(self):
        """
        The device setting from which this configuration revision was collected.
        ``attribute type:`` model
        """
        return self.broker.devicesetting(**{"ConfigRevisionID": self.ConfigRevisionID})
