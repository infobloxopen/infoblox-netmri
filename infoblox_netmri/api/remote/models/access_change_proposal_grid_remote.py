from ..remote import RemoteModel


class AccessChangeProposalGridRemote(RemoteModel):
    """
    list of proposals computed for an access change task (provisioing)


    |  ``id:`` The internal NetMRI identifier for this provisioning proposal.
    |  ``attribute type:`` number

    |  ``Network:`` The name of the Network View associated.
    |  ``attribute type:`` string

    |  ``DeviceID:`` The internal NetMRI identifier for the device on which will be applied this proposal.
    |  ``attribute type:`` number

    |  ``ProposalID:`` The internal NetMRI identifier for this provision operation.
    |  ``attribute type:`` string

    |  ``DeviceType:`` The NetMRI-determined device type.
    |  ``attribute type:`` string

    |  ``DeviceAssurance:`` The assurance level of the device type value.
    |  ``attribute type:`` number

    |  ``DeviceName:`` The NetMRI name of the device.
    |  ``attribute type:`` string

    |  ``DeviceIPDotted:`` The management IP address of the device, in dotted (or colon-delimited for IPv6) format.
    |  ``attribute type:`` string

    |  ``DeviceIPNumeric:`` The numerical value of the device IP address.
    |  ``attribute type:`` number

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier for the rule list against which was processed this elementary search.
    |  ``attribute type:`` string

    |  ``DeviceFilterSetName:`` The name of the rule list.
    |  ``attribute type:`` string

    |  ``RuleNum:`` If proposal is for adding a rule, the order of this rule within the rule list.
    |  ``attribute type:`` string

    |  ``RuleNumEditableInd:`` A flag indicating if the order of rule to add, in the rule list is editable.
    |  ``attribute type:`` bool

    |  ``SrcObjID:`` The internal NetMRI Identifier of the network object associated with this proposal (as source element if adding a rule). Value -1 if it is a new object, not already defined in the database.
    |  ``attribute type:`` number

    |  ``SrcObjName:`` The name of the network object associated as source element to the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``SrcMatchedObjNames:`` An array of available network object that can be used to define the source element of the new rule of this proposal. Each row of this array contains a couple : internal NetMRI identifier of the object, name of the object
    |  ``attribute type:`` string

    |  ``SrcObjSummary:`` A summary text for the expected value for this source element of the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``SrcObjEditableInd:`` A flag indicating that the  source element of this rule can be associated with a new object.
    |  ``attribute type:`` bool

    |  ``SrcObjHasDetailInd:`` A flag indicating that the summary has been shorten, thus more detail is available for the source network object for this rule.
    |  ``attribute type:`` bool

    |  ``DestObjID:`` The internal NetMRI Identifier of the network object associated with this proposal as destination element of the adding rule. Value -1 if it is a new object, not already defined in the database.
    |  ``attribute type:`` number

    |  ``DestObjName:`` The name of the network object associated as destination to the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``DestMatchedObjNames:`` An array of available network object that can be used to define the destination element of the new rule of this proposal. Each row of this array contains a couple : internal NetMRI identifier of the object, name of the object.
    |  ``attribute type:`` string

    |  ``DestObjSummary:`` A summary text for the expected value for this destination element of the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``DestObjEditableInd:`` A flag indicating that the  destination element of this rule can be associated with a new object.
    |  ``attribute type:`` bool

    |  ``DestObjHasDetailInd:`` A flag indicating that the summary has been shorten, thus more detail is available for the destination network object for this rule.
    |  ``attribute type:`` bool

    |  ``SvcID:`` The internal NetMRI Identifier of the service object associated with this proposal for the adding rule. Value -1 if it is a new service not already defined in the database.
    |  ``attribute type:`` number

    |  ``SvcName:`` The name of the service object associated to the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``SvcMatchedObjNames:`` An array of available service objects that can be used to define the service element of the new rule of this proposal. Each row of this array contains a couple : internal NetMRI identifier of the service, name of the service.
    |  ``attribute type:`` string

    |  ``SvcSummary:`` A summary text for the expected value for this destination element of the rule involved in this proposal.
    |  ``attribute type:`` string

    |  ``SvcEditableInd:`` A flag indicating that the  service element of this rule can be associated with a new service.
    |  ``attribute type:`` bool

    |  ``SvcHasDetailInd:`` A flag indicating that the summary has been shorten, thus more detail is available for the service object for this rule.
    |  ``attribute type:`` bool

    |  ``SrcSvcName:`` Unused
    |  ``attribute type:`` string

    |  ``Action:`` Action that proposal will apply on the configuration: one of 'ADD_FILTER', 'DELETE_FILTER', 'DELETE_OBJECT', 'DELETE_SERVICE', 'DELETE_FILTER_SET'.
    |  ``attribute type:`` string

    |  ``Warning:`` An indication of level of warnings from analysis for this proposal. One of : 'OK', 'Warning','Error' .
    |  ``attribute type:`` string

    |  ``WarningMsg:`` The list of warnings and errors thrown by analysis for this proposal.
    |  ``attribute type:`` string

    |  ``ConfigurationDetails:`` The list of device specific commands to apply on the configuration to implement that proposal.
    |  ``attribute type:`` string

    |  ``WarningMsgHasDetailInd:`` A flag indicating that the warning message has been shortened, thus more detail is available for the whole list of warnings or errors
    |  ``attribute type:`` bool

    |  ``SrcGroupTag:`` A group indicator for all source fields able to share the same selection: all fields of same group are synchronized.
    |  ``attribute type:`` string

    |  ``DestGroupTag:`` A group indicator for all destination fields able to share the same selectionDestGroupTag.
    |  ``attribute type:`` string

    |  ``SvcGroupTag:`` A group indicator for all service fields able to share the same selectionSvcGroupTag.
    |  ``attribute type:`` string

    |  ``VirtualNetworkID:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "Network",
                  "DeviceID",
                  "ProposalID",
                  "DeviceType",
                  "DeviceAssurance",
                  "DeviceName",
                  "DeviceIPDotted",
                  "DeviceIPNumeric",
                  "DeviceFilterSetID",
                  "DeviceFilterSetName",
                  "RuleNum",
                  "RuleNumEditableInd",
                  "SrcObjID",
                  "SrcObjName",
                  "SrcMatchedObjNames",
                  "SrcObjSummary",
                  "SrcObjEditableInd",
                  "SrcObjHasDetailInd",
                  "DestObjID",
                  "DestObjName",
                  "DestMatchedObjNames",
                  "DestObjSummary",
                  "DestObjEditableInd",
                  "DestObjHasDetailInd",
                  "SvcID",
                  "SvcName",
                  "SvcMatchedObjNames",
                  "SvcSummary",
                  "SvcEditableInd",
                  "SvcHasDetailInd",
                  "SrcSvcName",
                  "Action",
                  "Warning",
                  "WarningMsg",
                  "ConfigurationDetails",
                  "WarningMsgHasDetailInd",
                  "SrcGroupTag",
                  "DestGroupTag",
                  "SvcGroupTag",
                  "VirtualNetworkID",
                  )
