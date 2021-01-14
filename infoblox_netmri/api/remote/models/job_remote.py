from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class JobRemote(RemoteModel):
    """
    Running and completed job information.


    |  ``JobID:`` The internal NetMRI identifier for this job.
    |  ``attribute type:`` number

    |  ``Name:`` The name of this job, as entered when the job specification was defined, or when the job was executed from a script.
    |  ``attribute type:`` string

    |  ``Type:`` The type of job. This can be Scheduled, Ad Hoc, or Run Now.
    |  ``attribute type:`` string

    |  ``Status:`` The current status of this job, based upon all of the statuses for each device in the job.
    |  ``attribute type:`` string

    |  ``StartTime:`` The time this job started execution.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The time this job completed execution against all devices.
    |  ``attribute type:`` datetime

    |  ``id:`` The internal NetMRI identifier for this job.
    |  ``attribute type:`` number

    |  ``name:`` The name of this job, as entered when the job specification was defined, or when the job was executed from a script.
    |  ``attribute type:`` string

    |  ``job_type:`` The type of job. This can be Scheduled, Ad Hoc, or Run Now.
    |  ``attribute type:`` string

    |  ``status:`` The current status of this job, based upon all of the statuses for each device in the job.
    |  ``attribute type:`` string

    |  ``started_at:`` The time this job started execution.
    |  ``attribute type:`` datetime

    |  ``completed_at:`` The time this job completed execution against all devices.
    |  ``attribute type:`` datetime

    |  ``category:`` The job category.
    |  ``attribute type:`` string

    |  ``taskflow_revert:`` The internal workflow name for job reversion using the script.
    |  ``attribute type:`` string

    |  ``script_id:`` The internal identifier for the script.
    |  ``attribute type:`` number

    |  ``config_template_id:`` The internal identifier for the config template.
    |  ``attribute type:`` number

    |  ``description:`` The description of the job.
    |  ``attribute type:`` string

    |  ``created_by:`` The user that created the job.
    |  ``attribute type:`` string

    |  ``run_as:`` The user that run the job.
    |  ``attribute type:`` string

    |  ``credential_source:`` The source of a device credential.
    |  ``attribute type:`` string

    |  ``approved_by:`` The user that approved the job.
    |  ``attribute type:`` string

    |  ``approval_note:`` The approval note.
    |  ``attribute type:`` string

    |  ``provision_data:`` Internal data for provisioning jobs.
    |  ``attribute type:`` string

    |  ``input_data:`` The input data for the job.
    |  ``attribute type:`` string

    |  ``transactional_ind:`` Flag indicating if devices should be reserved during execution of this job.
    |  ``attribute type:`` bool

    |  ``last_status_at:`` The time when the job status was updated.
    |  ``attribute type:`` datetime

    |  ``created_at:`` The time when the job was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The time when the job was updated.
    |  ``attribute type:`` datetime

    |  ``approved_at:`` The time when the job was approved.
    |  ``attribute type:`` datetime

    |  ``script_text:`` The content of the script.
    |  ``attribute type:`` string

    |  ``script_language:`` The language of the script.
    |  ``attribute type:`` string

    |  ``config_template_text:`` The content of the config template.
    |  ``attribute type:`` string

    |  ``job_specification_id:`` The internal identifier for the associated Job Specification.
    |  ``attribute type:`` number


    """

    properties = ("JobID",
                  "Name",
                  "Type",
                  "Status",
                  "StartTime",
                  "EndTime",
                  "id",
                  "name",
                  "job_type",
                  "status",
                  "started_at",
                  "completed_at",
                  "category",
                  "taskflow_revert",
                  "script_id",
                  "config_template_id",
                  "description",
                  "created_by",
                  "run_as",
                  "credential_source",
                  "approved_by",
                  "approval_note",
                  "provision_data",
                  "input_data",
                  "transactional_ind",
                  "last_status_at",
                  "created_at",
                  "updated_at",
                  "approved_at",
                  "script_text",
                  "script_language",
                  "config_template_text",
                  "job_specification_id",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"id": self.id})
