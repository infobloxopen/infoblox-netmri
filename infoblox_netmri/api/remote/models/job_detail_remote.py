from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class JobDetailRemote(RemoteModel):
    """
    Detailed per device job status information.


    |  ``JobDetailID:`` The internal NetMRI identifier for this job detail.
    |  ``attribute type:`` number

    |  ``JobID:`` The internal NetMRI identifier for the job associated with this job detail.
    |  ``attribute type:`` number

    |  ``Script:`` The name of the script associated with this job detail.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The internal NetMRI identifier for the device associated with this job detail.
    |  ``attribute type:`` number

    |  ``Status:`` The status of this job detail. That is, the status of this execution of the script against this device.
    |  ``attribute type:`` string

    |  ``LastUpdate:`` The last time the status changed for this job detail.
    |  ``attribute type:`` datetime

    |  ``StartTime:`` The time this job began execution against this specific device.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The time this job completed execution against this specific device.
    |  ``attribute type:`` datetime

    |  ``Module:`` The internal NetMRI subsystem that created this job detail record.
    |  ``attribute type:`` string

    |  ``Visible:`` Shows if this job detail record was user initiated.
    |  ``attribute type:`` string

    |  ``job_specification_id:`` The internal NetMRI identifier of corresponding JobSpecification
    |  ``attribute type:`` number



    |  ``ScriptDisplayName:`` The title of the script.
    |  ``attribute type:`` string


    """

    properties = ("JobDetailID",
                  "JobID",
                  "Script",
                  "DeviceID",
                  "Status",
                  "LastUpdate",
                  "StartTime",
                  "EndTime",
                  "Module",
                  "Visible",
                  "job_specification_id",
                  "ScriptDisplayName",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device against which the job was run.
        ``attribute type:`` model
        """
        return self.broker.device(**{"JobDetailID": self.JobDetailID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device against which the job was run.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"JobDetailID": self.JobDetailID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"JobDetailID": self.JobDetailID})
