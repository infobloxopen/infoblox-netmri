from ..remote import RemoteModel


class ScriptModuleRemote(RemoteModel):
    """
    Script module library information.


    |  ``id:`` The internal NetMRI identifier of the Script Module.
    |  ``attribute type:`` number

    |  ``name:`` The unique name of the of the Script Module.
    |  ``attribute type:`` string

    |  ``category:`` User defined category of the Script Module.
    |  ``attribute type:`` string

    |  ``description:`` A description for the Script Module.
    |  ``attribute type:`` string

    |  ``created_by:`` Indicates by whom Script Module was created.
    |  ``attribute type:`` string

    |  ``updated_by:`` Indicates by whom Script Module was updated.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the Script Module was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the Script Module was updated.
    |  ``attribute type:`` datetime

    |  ``language:`` The language of the script module
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "category",
                  "description",
                  "created_by",
                  "updated_by",
                  "created_at",
                  "updated_at",
                  "language",
                  )
