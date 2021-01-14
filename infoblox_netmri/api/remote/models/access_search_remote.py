from ..remote import RemoteModel


class AccessSearchRemote(RemoteModel):
    """
    Active and recently completed access search requests.


    |  ``id:`` The internal natural identifier for this search operation.
    |  ``attribute type:`` number

    |  ``user_name:`` The name of owner of this search.
    |  ``attribute type:`` string

    |  ``search_set_key:`` The internal random generated key that identify this search operation.
    |  ``attribute type:`` string

    |  ``status:`` The current status of the search operation. A value within : 'Starting', 'Running', 'Cancelled', 'Done', 'Error'.
    |  ``attribute type:`` string

    |  ``rules_json:`` The rules definition of the multi-search criteria in a json format.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``errors:`` The last error that occurred in this search operation.
    |  ``attribute type:`` string

    |  ``general_errors:`` The list or errors occurred during the search operation.
    |  ``attribute type:`` string

    |  ``summary:`` The summary information for this provisioning operation.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "user_name",
                  "search_set_key",
                  "status",
                  "rules_json",
                  "created_at",
                  "updated_at",
                  "errors",
                  "general_errors",
                  "summary",
                  )
