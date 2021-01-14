from ..remote import RemoteModel


class AccessChangeRemote(RemoteModel):
    """
    Active and recently completed access change (provisioning)requests.


    |  ``id:`` The internal NetMRI identifier for this provisioning operation.
    |  ``attribute type:`` number

    |  ``user_name:`` The name of the user that created this provisioning operation.
    |  ``attribute type:`` string

    |  ``change_set_key:`` The random generated key that identify this provisioning operation.
    |  ``attribute type:`` string

    |  ``edit_status:`` The status of edition for this provisioning : one of 'Starting', 'Running', 'Cancelled', 'Done', 'Error'.
    |  ``attribute type:`` string

    |  ``proposal_json:`` The proposals for provisioning (at the last edition) - json format.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``change_status:`` The status of workflow of this provisioning, one of : 'Init', 'Edit', 'JobRunning', 'JobAchieved'.
    |  ``attribute type:`` string

    |  ``general_errors:`` The list of all errors computed at last analysis - pipe separated.
    |  ``attribute type:`` string

    |  ``history_json:`` The history of the whole workflow for this provisioning - json format.
    |  ``attribute type:`` string

    |  ``user_proposal_json:`` The proposals accepted and modified by user, last sent to analysis - json format.
    |  ``attribute type:`` string

    |  ``warning_count:`` The total number of warning raised in the last analysis.
    |  ``attribute type:`` number

    |  ``error_count:`` The total number of errors raised in last analysis.
    |  ``attribute type:`` number

    |  ``job_specification_id:`` The internal NetMRI identifier of the job that hold the provisioning.
    |  ``attribute type:`` number

    |  ``job_id:`` The internal NetMRI identifier of execution of job.
    |  ``attribute type:`` number

    |  ``former_proposal_json:`` The one level history of the proposals, aka proposals of the former analysis - json format.
    |  ``attribute type:`` string

    |  ``reversible:`` The state of reversibility of the current provisioning, one of : 'full', 'partial', 'none'.
    |  ``attribute type:`` string

    |  ``summary:`` The summary information for this search operation.
    |  ``attribute type:`` string

    |  ``deployable:`` String containing list of firewalls on which new rules can be deployed.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "user_name",
                  "change_set_key",
                  "edit_status",
                  "proposal_json",
                  "created_at",
                  "updated_at",
                  "change_status",
                  "general_errors",
                  "history_json",
                  "user_proposal_json",
                  "warning_count",
                  "error_count",
                  "job_specification_id",
                  "job_id",
                  "former_proposal_json",
                  "reversible",
                  "summary",
                  "deployable",
                  )
