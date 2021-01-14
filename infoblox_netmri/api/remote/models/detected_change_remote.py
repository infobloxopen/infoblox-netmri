from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DetectedChangeRemote(RemoteModel):
    """
    The changes identified by NetMRI.


    |  ``AdminInd:`` A flag indicating an administrative change.
    |  ``attribute type:`` bool

    |  ``ChangeAuthorizedInd:`` A flag indicating if the change is authorized or not.
    |  ``attribute type:`` bool

    |  ``ChangeDesc:`` A description of the change.
    |  ``attribute type:`` string

    |  ``ChangeDetectedTime:`` The date/time the change was detected. That is, the end time of the Change Window.
    |  ``attribute type:`` datetime

    |  ``ChangeID:`` The internal NetMRI identifier for this change.
    |  ``attribute type:`` number

    |  ``ChangeTime:`` The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
    |  ``attribute type:`` datetime

    |  ``ChangeTimeActualInd:`` A flag indicating if the ChangeTime field is the same as the ChangeDetectedTime field.
    |  ``attribute type:`` bool

    |  ``ChangeTraceID:`` The internal NetMRI identifier of the FIRST change trace that generated this change.
    |  ``attribute type:`` number

    |  ``ChangeUser:`` The user that made the change, if available.
    |  ``attribute type:`` string

    |  ``ConfigPollInd:`` A flag indicating that this change was detected, at least in part, by differences found between configuration file retrievals.
    |  ``attribute type:`` bool

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device that changed.
    |  ``attribute type:`` number

    |  ``ExternalInd:`` A flag indicating an external change.
    |  ``attribute type:`` bool

    |  ``HardwareInd:`` A flag indicating a hardware change.
    |  ``attribute type:`` bool

    |  ``SNMPPollInd:`` A flag indicating that this change was detected, at least in part, via differences between SNMP polls.
    |  ``attribute type:`` bool

    |  ``SNMPTrapInd:`` A flag indicating that this change was detected, at least in part, via an SNMP trap (not currently supported).
    |  ``attribute type:`` bool

    |  ``SoftwareInd:`` A flag indicating a software change.
    |  ``attribute type:`` bool

    |  ``SyslogInd:`` A flag indicating that this change was detected, at least in part, via a Syslog message.
    |  ``attribute type:`` bool




    |  ``AccessInd:`` A flag indicating an access (Security Filtering) change.
    |  ``attribute type:`` bool


    """

    properties = ("AdminInd",
                  "ChangeAuthorizedInd",
                  "ChangeDesc",
                  "ChangeDetectedTime",
                  "ChangeID",
                  "ChangeTime",
                  "ChangeTimeActualInd",
                  "ChangeTraceID",
                  "ChangeUser",
                  "ConfigPollInd",
                  "DataSourceID",
                  "DeviceID",
                  "ExternalInd",
                  "HardwareInd",
                  "SNMPPollInd",
                  "SNMPTrapInd",
                  "SoftwareInd",
                  "SyslogInd",
                  "AccessInd",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"ChangeID": self.ChangeID})

    @property
    @check_api_availability
    def device(self):
        """
        The device that changed.
        ``attribute type:`` model
        """
        return self.broker.device(**{"ChangeID": self.ChangeID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device that changed.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"ChangeID": self.ChangeID})

    @property
    @check_api_availability
    def meta(self):
        """
        User custom fields
        ``attribute type:`` model
        """
        return self.broker.meta(**{"ChangeID": self.ChangeID})
