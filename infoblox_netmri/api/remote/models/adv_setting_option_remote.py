from ..remote import RemoteModel


class AdvSettingOptionRemote(RemoteModel):
    """
    This table list out the advance setting options.


    |  ``id:`` The internal NetMRI identifier for this setting option.
    |  ``attribute type:`` number

    |  ``label:`` The label for this setting option.
    |  ``attribute type:`` string

    |  ``value:`` The value for this setting option.
    |  ``attribute type:`` string

    |  ``adv_setting_def_id:`` The internal NetMRI identifier for setting definition.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "label",
                  "value",
                  "adv_setting_def_id",
                  )
