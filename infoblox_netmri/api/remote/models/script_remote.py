from ..remote import RemoteModel


class ScriptRemote(RemoteModel):
    """
    Includes all scripts currently available in this NetMRI installation.


    |  ``id:`` The internal NetMRI identifier for the script.
    |  ``attribute type:`` number

    |  ``name:`` The name of this script.
    |  ``attribute type:`` string

    |  ``module:`` Currently unused.
    |  ``attribute type:`` string

    |  ``visible:`` Indicates whether this script is visible on the user interface.
    |  ``attribute type:`` bool

    |  ``description:`` Describes the purpose, function and usage of this script.
    |  ``attribute type:`` string

    |  ``created_by:`` The user that initially imported the script into NetMRI.
    |  ``attribute type:`` string

    |  ``updated_by:`` The user that last modified this script.
    |  ``attribute type:`` string

    |  ``language:`` The scripting language used; currently the only supported language is CCS.
    |  ``attribute type:`` string

    |  ``risk_level:`` The user-specified risk level for the script. Possible levels are 1 (low), 2 (medium), and 3 (high). To run higher risk scripts, higher privileges are required.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the script was initially imported into NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the script was last modified.
    |  ``attribute type:`` datetime

    |  ``category:`` Currently unused.
    |  ``attribute type:`` string

    |  ``read_only:`` Read-only scripts are not user modifiable.
    |  ``attribute type:`` bool

    |  ``taskflow_create:`` Internal workflow name for job creation using this script.
    |  ``attribute type:`` string

    |  ``taskflow_edit:`` Internal workflow name for job edition using this script.
    |  ``attribute type:`` string

    |  ``taskflow_revert:`` Internal workflow name for job reversion using this script.
    |  ``attribute type:`` string

    |  ``target_mapping:`` Kind of mapping used for this script : 'device' ...
    |  ``attribute type:`` string

    |  ``transactional_ind:`` Flag indicating if devices should be reserved during execution of this script.
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "name",
                  "module",
                  "visible",
                  "description",
                  "created_by",
                  "updated_by",
                  "language",
                  "risk_level",
                  "created_at",
                  "updated_at",
                  "category",
                  "read_only",
                  "taskflow_create",
                  "taskflow_edit",
                  "taskflow_revert",
                  "target_mapping",
                  "transactional_ind",
                  )
