from ..remote import RemoteModel


class PolicyRemote(RemoteModel):
    """
    This table list out the entries of policies definitions.


    |  ``id:`` The internal NetMRI identifier of a policy.
    |  ``attribute type:`` number

    |  ``name:`` The name of a policy.
    |  ``attribute type:`` string

    |  ``description:`` The description of a policy.
    |  ``attribute type:`` string

    |  ``author:`` The name of an author defined in a policy.
    |  ``attribute type:`` string

    |  ``set_filter:`` The filter defined in a policy.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``schedule_mode:`` The scheduled mode of a policy.
    |  ``attribute type:`` string

    |  ``short_name:`` The short name of a policy.
    |  ``attribute type:`` string

    |  ``read_only:`` The read-only mode of a policy.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "name",
                  "description",
                  "author",
                  "set_filter",
                  "created_at",
                  "updated_at",
                  "schedule_mode",
                  "short_name",
                  "read_only",
                  )
