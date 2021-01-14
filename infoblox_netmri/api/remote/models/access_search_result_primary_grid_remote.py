from ..remote import RemoteModel


class AccessSearchResultPrimaryGridRemote(RemoteModel):
    """
    list of elementary search for one search request


    |  ``id:`` The internal NetMRI identifier for this search element.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``Status:`` The status of the search for this elementary.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The internal NetMRI identifier for the device on which was processes this elementary search.
    |  ``attribute type:`` number

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` The assurance level of the device type value.
    |  ``attribute type:`` number

    |  ``DeviceDNSName:`` The device name as reported by DNS.
    |  ``attribute type:`` string

    |  ``DeviceName:`` The NetMRI name of the device.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier for the rule list against which was processed this elementary search.
    |  ``attribute type:`` string

    |  ``ESearchID:`` The internal NetMRI identifier for this elementary search operation.
    |  ``attribute type:`` string

    |  ``DeviceFilterSetName:`` The name of the rule list.
    |  ``attribute type:`` string

    |  ``Access:`` The global result of the search : 'N/A', 'Blocker', 'Partial', 'Full'.
    |  ``attribute type:`` string

    |  ``RuleID:`` The identifier of the rule that describe the search that was launched against this rule list.
    |  ``attribute type:`` number

    |  ``MatchCount:`` The number of rules on the configuration that matches exactly the criteria defined in rule.
    |  ``attribute type:`` number

    |  ``StatusPct:`` The percentage of already processed search.
    |  ``attribute type:`` string

    |  ``ErrorMsg:`` The error message returned by analysis if error was thrown.
    |  ``attribute type:`` string

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "Network",
                  "Status",
                  "DeviceID",
                  "DeviceType",
                  "DeviceAssurance",
                  "DeviceDNSName",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceFilterSetID",
                  "ESearchID",
                  "DeviceFilterSetName",
                  "Access",
                  "RuleID",
                  "MatchCount",
                  "StatusPct",
                  "ErrorMsg",
                  "updated_at",
                  "VirtualNetworkID",
                  )
