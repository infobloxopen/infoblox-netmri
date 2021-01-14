from ..remote import RemoteModel


class AccessChangeManagementScheduleUpcomingGridRemote(RemoteModel):
    """
    list of scheduled jobs not yet executed for provisioning purposes


    |  ``job_id:`` The internal NetMRI identifier of the job scheduled.
    |  ``attribute type:`` number

    |  ``script:`` The name of the script that was executed by this job.
    |  ``attribute type:`` string

    |  ``name:`` The name of the job.
    |  ``attribute type:`` string

    |  ``approved_by_name:`` The user that approved the execution of the job.
    |  ``attribute type:`` string

    |  ``schedule_hash:`` The schedule information.
    |  ``attribute type:`` string

    |  ``status:`` The status of the scheduled job.
    |  ``attribute type:`` string

    |  ``last_run_start:`` The date and time this job was last time ran.
    |  ``attribute type:`` string

    |  ``last_run_status:`` The last execution status for this job when already ran.
    |  ``attribute type:`` string

    |  ``description:`` The description of the job.
    |  ``attribute type:`` string

    |  ``approved_by:`` The user that approve the job.
    |  ``attribute type:`` string

    |  ``created_by:`` The user that creates the job.
    |  ``attribute type:`` string

    |  ``approved_timestamp:`` The date and time when the job was approved.
    |  ``attribute type:`` string

    |  ``last_run_BatchID:`` The internal NetMRI identifier of last job's execution.
    |  ``attribute type:`` number

    |  ``config_template_id:`` The internal NetMRI identifier of the template used to create that job.
    |  ``attribute type:`` number

    |  ``job_type:`` The type of job : 'script', 'template'.
    |  ``attribute type:`` string

    |  ``taskflowCreate:`` The internal tag of workflow for script.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` string

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.SpmInterfacesDefaultGridSpmInterfacesDefaultGrid
    |  ``attribute type:`` string

    |  ``device_ids:`` List of internal identifiers for the devices which the upcoming jobs will be run against.
    |  ``attribute type:`` string

    """

    properties = ("job_id",
                  "script",
                  "name",
                  "approved_by_name",
                  "schedule_hash",
                  "status",
                  "last_run_start",
                  "last_run_status",
                  "description",
                  "approved_by",
                  "created_by",
                  "approved_timestamp",
                  "last_run_BatchID",
                  "config_template_id",
                  "job_type",
                  "taskflowCreate",
                  "created_at",
                  "updated_at",
                  "device_ids",
                  )
