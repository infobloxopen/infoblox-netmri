from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class JobSpecificationRemote(RemoteModel):
    """
    Job specifications, both approved and unapproved jobs.


    |  ``id:`` The internal NetMRI identifier for the job specification.
    |  ``attribute type:`` number

    |  ``name:`` The job name as entered when creating the job.
    |  ``attribute type:`` string

    |  ``description:`` The description of the job as entered when creating the job.
    |  ``attribute type:`` string

    |  ``script_id:`` The internal NetMRI identifier for the script associated with this job.
    |  ``attribute type:`` number

    |  ``schedule:`` The job schedule, in cron format.
    |  ``attribute type:`` string

    |  ``created_by:`` The user name of the user that created this job.
    |  ``attribute type:`` string

    |  ``approved_by:`` The user id of the user that approved this job.
    |  ``attribute type:`` number

    |  ``approved_timestamp:`` The date/time of the approval.
    |  ``attribute type:`` datetime

    |  ``created_at:`` The date/time that this job specification was created.
    |  ``attribute type:`` string

    |  ``updated_at:`` The date/time that this job specification was last updated.
    |  ``attribute type:`` string

    |  ``config_template_id:`` The internal NetMRI identifier for the associated Configuration Template.
    |  ``attribute type:`` number

    |  ``job_type:`` The base type of the job ('script' or 'template').
    |  ``attribute type:`` string

    |  ``approved_by_name:`` Name of the approver for this job.
    |  ``attribute type:`` string

    |  ``category:`` The category of this job.
    |  ``attribute type:`` string

    |  ``provision_data:`` Internal data for provisioning jobs.
    |  ``attribute type:`` string

    |  ``transactional_ind:`` Flag indicating that the job needs to be executed in a transaction.
    |  ``attribute type:`` bool

    |  ``approval_note:`` The comment associated to the approval.
    |  ``attribute type:`` string

    |  ``revertable_ind:`` Flag indicating that when failed, job must revert the already processed operations.
    |  ``attribute type:`` bool

    |  ``last_run:`` Last run start time
    |  ``attribute type:`` datetime

    |  ``push_mode:`` Defines the push mode (bulk or line by line) used for template based jobs.
    |  ``attribute type:`` string

    |  ``unapproved_notification_trigger:`` Flag that defines if approval status has changed.
    |  ``attribute type:`` number

    |  ``deployable_ind:`` Flag indicating that job must deploy the uploaded rules on firewalls.
    |  ``attribute type:`` bool

    |  ``script:`` Script name used in netmri.details_from_jobs view
    |  ``attribute type:`` string


    """

    properties = ("id",
                  "name",
                  "description",
                  "script_id",
                  "schedule",
                  "created_by",
                  "approved_by",
                  "approved_timestamp",
                  "created_at",
                  "updated_at",
                  "config_template_id",
                  "job_type",
                  "approved_by_name",
                  "category",
                  "provision_data",
                  "transactional_ind",
                  "approval_note",
                  "revertable_ind",
                  "last_run",
                  "push_mode",
                  "unapproved_notification_trigger",
                  "deployable_ind",
                  "script",
                  )

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"id": self.id})
