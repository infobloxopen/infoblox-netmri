from ..remote import RemoteModel


class AdvSettingRemote(RemoteModel):
    """
    This table list out the entries of Advance Settings in the Setting option within the NetMRI.


    |  ``id:`` The internal NetMRI identifier of an advance setting.
    |  ``attribute type:`` number

    |  ``adv_setting_def_id:`` The internal NetMRI identifier of an advance setting definition.
    |  ``attribute type:`` number

    |  ``value:`` The value of a n advance setting.
    |  ``attribute type:`` string

    |  ``secure_version:`` Internal version of what encryption used.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "adv_setting_def_id",
                  "value",
                  "secure_version",
                  )
