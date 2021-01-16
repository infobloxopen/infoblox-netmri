from ..remote import RemoteModel


class AccessSearchResultSecondaryGridRemote(RemoteModel):
    """
    list of rules impacted by an elementary search


    |  ``id:`` The internal NetMRI identifier for this search result detailed.
    |  ``attribute type:`` number

    |  ``ESearchID:`` The internal NetMRI randomized identifier for this search result detailed.
    |  ``attribute type:`` string

    |  ``DeviceFilterSetID:`` The internal NetMRI identifier for this rule list to which this rule belongs.
    |  ``attribute type:`` number

    |  ``DeviceFilterID:`` The internal NetMRI identifier for this rule.
    |  ``attribute type:`` string

    |  ``DeviceServiceID:`` The internal NetMRI identifier for the Device to which belongs all the elements of this result.
    |  ``attribute type:`` number

    |  ``SrcDeviceObjectID:`` The internal NetMRI identifier for the source ip address element of the rule.
    |  ``attribute type:`` number

    |  ``DestDeviceObjectID:`` The internal NetMRI identifier for the destination ip address element of the rule.
    |  ``attribute type:`` number

    |  ``FltOrder:`` The rule order in the rule list.
    |  ``attribute type:`` number

    |  ``DeviceConfigSummary:`` The original text of the configuration from witch this rule is built.
    |  ``attribute type:`` string

    |  ``DeviceConfigHasDetailInd:`` A flag indicating if the original text has been shorten.
    |  ``attribute type:`` bool

    |  ``SrcObjName:`` The name of the source network object element of this rule.
    |  ``attribute type:`` string

    |  ``SrcObjSummary:`` The description of the source network object element of the rule.
    |  ``attribute type:`` string

    |  ``SrcObjHasDetailInd:`` A flag indicating whether the description of the source network object has been shorten or not.
    |  ``attribute type:`` bool

    |  ``DestObjName:`` The name of the destination network object element of this rule.
    |  ``attribute type:`` string

    |  ``DestObjSummary:`` The description of the destination network object element of the rule.
    |  ``attribute type:`` string

    |  ``DestObjHasDetailInd:`` A flag indicating whether the description of the destination network object has been shorten or not.
    |  ``attribute type:`` bool

    |  ``SvcProtocol:`` The name of the protocol, part of the service element of this rule.
    |  ``attribute type:`` string

    |  ``SvcProtocolSummary:`` The description of the protocol element of the rule.
    |  ``attribute type:`` string

    |  ``SvcProtocolHasDetailInd:`` A flag indicating whether the description of the protocol has been shorten or not.
    |  ``attribute type:`` bool

    |  ``SvcSourcePort:`` The text of the source ports, part of the service element of this rule.
    |  ``attribute type:`` string

    |  ``SvcSourcePortSummary:`` The description of the source-port element of the rule.
    |  ``attribute type:`` string

    |  ``SvcSourceHasDetailInd:`` A flag indicating whether the source-port has been shorten or not.
    |  ``attribute type:`` bool

    |  ``SvcName:`` The description of the service element of the rule.
    |  ``attribute type:`` string

    |  ``SvcSummary:`` The description of the service element of the rule.
    |  ``attribute type:`` string

    |  ``SvcHasDetailInd:`` A flag indicating whether the service has been shorten or not.
    |  ``attribute type:`` bool

    |  ``HitCount:`` The number of hit count collected on this rule.
    |  ``attribute type:`` number

    |  ``AccessType:`` The allowance of the rule : Allow or Deny.
    |  ``attribute type:`` string

    |  ``MatchType:`` The result of comparison of the criteria against this rule.
    |  ``attribute type:`` string

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "ESearchID",
                  "DeviceFilterSetID",
                  "DeviceFilterID",
                  "DeviceServiceID",
                  "SrcDeviceObjectID",
                  "DestDeviceObjectID",
                  "FltOrder",
                  "DeviceConfigSummary",
                  "DeviceConfigHasDetailInd",
                  "SrcObjName",
                  "SrcObjSummary",
                  "SrcObjHasDetailInd",
                  "DestObjName",
                  "DestObjSummary",
                  "DestObjHasDetailInd",
                  "SvcProtocol",
                  "SvcProtocolSummary",
                  "SvcProtocolHasDetailInd",
                  "SvcSourcePort",
                  "SvcSourcePortSummary",
                  "SvcSourceHasDetailInd",
                  "SvcName",
                  "SvcSummary",
                  "SvcHasDetailInd",
                  "HitCount",
                  "AccessType",
                  "MatchType",
                  "updated_at",
                  )
