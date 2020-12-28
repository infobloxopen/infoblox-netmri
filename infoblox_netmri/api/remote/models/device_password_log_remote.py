from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePasswordLogRemote(RemoteModel):
    """
    This table list out entries of DevicePasswordLog


    |  ``DevicePwLogID:`` The internal NetMRI identifier for the device password log.
    |  ``attribute type:`` number

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``DeviceID:`` The internal NetMRI identifier for the device from which device password log table information was collected.
    |  ``attribute type:`` number

    |  ``DevicePwLogTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DevicePwLogProtocol:`` The protocol of the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogPassword:`` The password of the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogSNMPAuthProto:`` The SNMP password is authenticated for the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogSNMPPrivProto:`` The SNMP private password protocol of the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogStatus:`` The status of the device password log.
    |  ``attribute type:`` string


    |  ``DevicePwLogPasswordSecure:`` The password of the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogUsernameSecure:`` The username of the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogEnablePasswordSecure:`` The password is enabled for device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogSNMPAuthPWSecure:`` The SNMP password is authenticated for the device password log.
    |  ``attribute type:`` string

    |  ``DevicePwLogSNMPPrivPWSecure:`` The SNMP private password of the device password log.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` The encryption version of the username and passwords.
    |  ``attribute type:`` number


    """

    properties = ("DevicePwLogID",
                  "DataSourceID",
                  "DeviceID",
                  "DevicePwLogTimestamp",
                  "DevicePwLogProtocol",
                  "DevicePwLogPassword",
                  "DevicePwLogSNMPAuthProto",
                  "DevicePwLogSNMPPrivProto",
                  "DevicePwLogStatus",
                  "DevicePwLogPasswordSecure",
                  "DevicePwLogUsernameSecure",
                  "DevicePwLogEnablePasswordSecure",
                  "DevicePwLogSNMPAuthPWSecure",
                  "DevicePwLogSNMPPrivPWSecure",
                  "SecureVersion",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePwLogID": self.DevicePwLogID})

    @property
    @check_api_availability
    def device(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePwLogID": self.DevicePwLogID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device from which this data was collected.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePwLogID": self.DevicePwLogID})
