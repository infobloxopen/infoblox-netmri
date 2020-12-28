from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class JobProcessRemote(RemoteModel):
    """
    Within a Job, execution of a script against a specific device.


    |  ``process_type:`` The kind of process_type.
    |  ``attribute type:`` string

    |  ``user_name:`` The name of the user that ran this execution.
    |  ``attribute type:`` string

    |  ``job_handler_id:`` The internal identifier of the Runner that handled the execution of this process.
    |  ``attribute type:`` number

    |  ``job_id:`` The internal identifier of job that process belongs to.
    |  ``attribute type:`` number

    |  ``input_data:`` Data parameters for the execution.
    |  ``attribute type:`` string

    |  ``status:`` The last known execution status for this target.
    |  ``attribute type:`` string

    |  ``last_status_at:`` The date and time the status was updated.
    |  ``attribute type:`` datetime

    |  ``started_at:`` The date and time the execution of this process was started.
    |  ``attribute type:`` datetime

    |  ``completed_at:`` The date and time the execution of this process was completed.
    |  ``attribute type:`` datetime

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``job_target_id:`` unused - invalid.
    |  ``attribute type:`` number

    |  ``revert_ind:`` Indication that this process must be re-executed for reversion if it is completed with an error.
    |  ``attribute type:`` bool

    |  ``deploy_ind:`` Indication that this process must be re-executed for post-deploy operation when completed with success.
    |  ``attribute type:`` bool

    |  ``device_id:`` The internal identifier of the device that this process is running against.
    |  ``attribute type:`` number

    |  ``id:`` The internal identifier of this process.
    |  ``attribute type:`` number


    """

    properties = ("process_type",
                  "user_name",
                  "job_handler_id",
                  "job_id",
                  "input_data",
                  "status",
                  "last_status_at",
                  "started_at",
                  "completed_at",
                  "created_at",
                  "updated_at",
                  "job_target_id",
                  "revert_ind",
                  "deploy_ind",
                  "device_id",
                  "id",
                  )

    @property
    @check_api_availability
    def device(self):
        """
        The device against which this Process will be executed.
        ``attribute type:`` model
        """
        return self.broker.device(**{"id": self.id})
