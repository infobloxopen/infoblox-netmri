from ..remote import RemoteModel


class ChangesDeviceViewerGridRemote(RemoteModel):
    """
    list of device changes


    |  ``id:`` The internal NetMRI identifier of the grid entry.
    |  ``attribute type:`` number

    |  ``ChangeTime:`` The EARLIEST date/time that this change MAY have occurred. That is, the beginning time of the Change Window.
    |  ``attribute type:`` string

    |  ``ChangeDetectedTime:`` The date/time the change was detected. That is, the end time of the Change Window.
    |  ``attribute type:`` datetime

    |  ``ChangeID:`` The internal NetMRI identifier for this change.
    |  ``attribute type:`` number

    |  ``HardwareInd:`` A flag indicating a hardware change.
    |  ``attribute type:`` bool

    |  ``SoftwareInd:`` A flag indicating a software change.
    |  ``attribute type:`` bool

    |  ``AdminInd:`` A flag indicating an administrative change.
    |  ``attribute type:`` bool

    |  ``ExternalInd:`` A flag indicating an external change.
    |  ``attribute type:`` bool

    |  ``SNMPPollInd:`` A flag indicating that this change was detected, at least in part, via differences between SNMP polls.
    |  ``attribute type:`` bool

    |  ``SNMPTrapInd:`` A flag indicating that this change was detected, at least in part, via an SNMP trap (not currently supported).
    |  ``attribute type:`` bool

    |  ``SyslogInd:`` A flag indicating that this change was detected, at least in part, via a Syslog message.
    |  ``attribute type:`` bool

    |  ``ConfigPollInd:`` A flag indicating that this change was detected, at least in part, by differences found between configuration file retrievals.
    |  ``attribute type:`` bool

    |  ``DeviceID:`` The internal NetMRI identifier for the device that changed.
    |  ``attribute type:`` number

    |  ``DeviceIPDotted:`` The management IP address of the device that changed, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the device that changed; this will be either the same as DeviceSysName or DeviceDNSName, depending on your NetMRI configuration.
    |  ``attribute type:`` string

    |  ``DeviceVendor:`` The vendor name of the device that changed.
    |  ``attribute type:`` string

    |  ``DeviceModel:`` The model name of the device that changed
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the IP address of the device that changed.
    |  ``attribute type:`` number

    |  ``DeviceType:`` The NetMRI-determined device type of the device that changed.
    |  ``attribute type:`` string

    |  ``ChangeUser:`` The user that made the change, if available.
    |  ``attribute type:`` string

    |  ``ChangeAuthorizedInd:``  flag indicating if the change is authorized or not.
    |  ``attribute type:`` bool

    |  ``ChangeMethod:`` The method used to make the change.
    |  ``attribute type:`` string

    |  ``ChangeType:`` The type of change made.
    |  ``attribute type:`` string

    |  ``RunningChangedRev:`` The running change revision of the change.
    |  ``attribute type:`` string

    |  ``SavedChangedRev:`` The saved change revision.
    |  ``attribute type:`` string

    |  ``HideRunning:`` Flag indicating there is a running revision.
    |  ``attribute type:`` number

    |  ``HideSaved:`` Flag indicating there is a saved change revision.
    |  ``attribute type:`` number

    |  ``DeviceAssurance:`` The assurance level of the device type value.
    |  ``attribute type:`` number

    |  ``HideAccess:`` A flag indicating whether or not access diff viewer is available for this entry.
    |  ``attribute type:`` number

    |  ``configstate:`` The state of configuration change.
    |  ``attribute type:`` string

    |  ``CustomFieldsEditInd:`` A flag indicating whether the user can edit custom fields for this object.
    |  ``attribute type:`` bool

    |  ``Network:`` The Virtual Network to which the management address of this device belongs.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal NetMRI identifier of the Virtual Network to which the management address of this device belongs.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "ChangeTime",
                  "ChangeDetectedTime",
                  "ChangeID",
                  "HardwareInd",
                  "SoftwareInd",
                  "AdminInd",
                  "ExternalInd",
                  "SNMPPollInd",
                  "SNMPTrapInd",
                  "SyslogInd",
                  "ConfigPollInd",
                  "DeviceID",
                  "DeviceIPDotted",
                  "DeviceName",
                  "DeviceVendor",
                  "DeviceModel",
                  "DeviceIPNumeric",
                  "DeviceType",
                  "ChangeUser",
                  "ChangeAuthorizedInd",
                  "ChangeMethod",
                  "ChangeType",
                  "RunningChangedRev",
                  "SavedChangedRev",
                  "HideRunning",
                  "HideSaved",
                  "DeviceAssurance",
                  "HideAccess",
                  "configstate",
                  "CustomFieldsEditInd",
                  "Network",
                  "VirtualNetworkID",
                  )
