from ..remote import RemoteModel


class IfSettingRemote(RemoteModel):
    """
    This table list out the interface settings.


    |  ``CollectionInd:`` A flag indicating if data collection enabled on this interface.
    |  ``attribute type:`` bool

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``DeviceID:`` The internal NetMRI identifier for device.
    |  ``attribute type:`` number

    |  ``InterfaceID:`` The internal NetMRI identifier for interface.
    |  ``attribute type:`` number

    |  ``SPMExcludedInd:`` A flag indicating if interface excluded from Switch Port Management.
    |  ``attribute type:`` bool

    |  ``id:`` The internal NetMRI identifier for interface setting.
    |  ``attribute type:`` number

    |  ``ifIndex:`` The index of interface.
    |  ``attribute type:`` number

    """

    properties = ("CollectionInd",
                  "created_at",
                  "updated_at",
                  "DeviceID",
                  "InterfaceID",
                  "SPMExcludedInd",
                  "id",
                  "ifIndex",
                  )
