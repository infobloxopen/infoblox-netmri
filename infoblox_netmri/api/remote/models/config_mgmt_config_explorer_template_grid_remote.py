from ..remote import RemoteModel


class ConfigMgmtConfigExplorerTemplateGridRemote(RemoteModel):
    """



    |  ``template_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``vendor:`` none
    |  ``attribute type:`` string

    |  ``model:`` none
    |  ``attribute type:`` string

    |  ``version:`` none
    |  ``attribute type:`` string

    |  ``device_type:`` none
    |  ``attribute type:`` string

    |  ``created_by:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_by:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    """

    properties = ("template_id",
                  "name",
                  "vendor",
                  "model",
                  "version",
                  "device_type",
                  "created_by",
                  "created_at",
                  "updated_by",
                  "updated_at",
                  )
