from ..remote import RemoteModel


class AdvSettingDefRemote(RemoteModel):
    """
    This table list out the advance setting definitions.


    |  ``allow_empty:`` A flag indicating if this setting can be empty.
    |  ``attribute type:`` bool

    |  ``category:`` The category of this setting.
    |  ``attribute type:`` string

    |  ``default_value:`` Default value for this setting.
    |  ``attribute type:`` string

    |  ``description:`` Description for this setting.
    |  ``attribute type:`` string

    |  ``display_hints:`` Hints to display for this setting.
    |  ``attribute type:`` string

    |  ``feature:`` The feature this setting definition is related to.
    |  ``attribute type:`` string

    |  ``id:`` The internal NetMRI identifier for this setting definition.
    |  ``attribute type:`` number

    |  ``name:`` The name of this setting.
    |  ``attribute type:`` string

    |  ``setting_type:`` The type of this setting.
    |  ``attribute type:`` string

    |  ``ui_name:`` The UI name of this setting.
    |  ``attribute type:`` string

    |  ``visible:`` A flag indicating if this setting visible.
    |  ``attribute type:`` bool

    """

    properties = ("allow_empty",
                  "category",
                  "default_value",
                  "description",
                  "display_hints",
                  "feature",
                  "id",
                  "name",
                  "setting_type",
                  "ui_name",
                  "visible",
                  )
