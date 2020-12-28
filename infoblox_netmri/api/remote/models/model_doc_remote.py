from ..remote import RemoteModel


class ModelDocRemote(RemoteModel):
    """
    This table list out the model documentation.


    |  ``id:`` The internal NetMRI identifier for this model.
    |  ``attribute type:`` number

    |  ``category:`` The category of this model.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``description:`` The description of this model.
    |  ``attribute type:`` text

    |  ``hidden_ind:`` A flag indicating if model is hidden
    |  ``attribute type:`` bool

    |  ``history_support:`` History support.
    |  ``attribute type:`` string

    |  ``java_api_ind:`` A flag indicating if model is in java API
    |  ``attribute type:`` bool

    |  ``perl_api_ind:`` A flag indicating if model is in perl API
    |  ``attribute type:`` bool

    |  ``model_name:`` The name of model.
    |  ``attribute type:`` string

    |  ``table_name:`` The name of database table where model records are stored.
    |  ``attribute type:`` string

    |  ``title:`` The title of model.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "category",
                  "created_at",
                  "updated_at",
                  "description",
                  "hidden_ind",
                  "history_support",
                  "java_api_ind",
                  "perl_api_ind",
                  "model_name",
                  "table_name",
                  "title",
                  )
