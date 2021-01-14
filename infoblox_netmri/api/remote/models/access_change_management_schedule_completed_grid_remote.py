from ..remote import RemoteModel


class AccessChangeManagementScheduleCompletedGridRemote(RemoteModel):
    """
    list of executed jobs for provisioning purposes


    |  ``BatchID:`` The internal NetMRI Identifier of the job executed.
    |  ``attribute type:`` number

    |  ``Status:`` The ending status of the job.
    |  ``attribute type:`` string

    |  ``Name:`` The name of the job.
    |  ``attribute type:`` string

    |  ``Script:`` The name of the script that was executed by this job.
    |  ``attribute type:`` string

    |  ``Approver:`` The name of the user that approved the execution of the job.
    |  ``attribute type:`` string

    |  ``StartTime:`` The date and time of starting execution for this job.
    |  ``attribute type:`` datetime

    |  ``EndTime:`` The date and time of ending execution for this job.
    |  ``attribute type:`` datetime

    |  ``JobCount:`` The number of execution of job launched.
    |  ``attribute type:`` number

    |  ``MinJobID:`` The internal NetMRI identifier of the first execution.
    |  ``attribute type:`` number

    |  ``taskflowCreate:`` The script's task_flow_create indicator that leads to determine if the job is SDC or not.
    |  ``attribute type:`` string

    |  ``description:`` The description of the job.
    |  ``attribute type:`` string

    |  ``device_ids:`` List of internal identifiers for the Devices which the completed job was run against.
    |  ``attribute type:`` string

    """

    properties = ("BatchID",
                  "Status",
                  "Name",
                  "Script",
                  "Approver",
                  "StartTime",
                  "EndTime",
                  "JobCount",
                  "MinJobID",
                  "taskflowCreate",
                  "description",
                  "device_ids",
                  )
