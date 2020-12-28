from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DefaultPasswordFoundRemote(RemoteModel):
    """
    This table list out entries of DefaultPasswordFound


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which default password found information was collected.
    |  ``attribute type:`` number

    |  ``Timestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``Protocol:`` The name of the protocol.
    |  ``attribute type:`` string


    |  ``UsernameSecure:`` The username of the device in the default password found table.
    |  ``attribute type:`` string

    |  ``PasswordSecure:`` The password of the device in the default password found table.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number


    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "Timestamp",
                  "Protocol",
                  "UsernameSecure",
                  "PasswordSecure",
                  "SecureVersion",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DataSourceID": self.DataSourceID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DataSourceID": self.DataSourceID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DataSourceID": self.DataSourceID})
