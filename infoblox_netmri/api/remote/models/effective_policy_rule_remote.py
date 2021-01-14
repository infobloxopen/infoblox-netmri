from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class EffectivePolicyRuleRemote(RemoteModel):
    """
    The policy rules, as they were defined at the time of policy evaluation. The rules described in here correspond to the policy rule results expressed in the DevicePolicyRule and other results models.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``PolicyRuleID:`` The internal NetMRI identifier for this effective policy rule.
    |  ``attribute type:`` number

    |  ``PolicyRuleStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``PolicyRuleEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``PolicyRuleChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``PolicyRuleTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``PolicyRuleFirstSeenTime:`` The date and time when this policy rule was first seen on the NetMRI.
    |  ``attribute type:`` datetime

    |  ``PolicyRuleName:`` The long name of the policy rule.
    |  ``attribute type:`` string

    |  ``PolicyRuleDescription:`` The description of the policy rule at the time of evaluation.
    |  ``attribute type:`` string

    |  ``PolicyRuleAuthor:`` The author of the policy rule at the time of evaluation.
    |  ``attribute type:`` string

    |  ``PolicyRuleSetFilter:`` The XML SetFilter used to determine if this rule applies to a specific device.
    |  ``attribute type:`` string

    |  ``PolicyRuleRuleLogic:`` The XML policy rule logic.
    |  ``attribute type:`` string

    |  ``PolicyRuleSeverity:`` The severity level (info, warning, or error) for a violation of this rule.
    |  ``attribute type:`` string

    |  ``PolicyRuleActionAfterExec:`` Not used.
    |  ``attribute type:`` string

    |  ``PolicyRuleCreatedAt:`` The date and time the policy rule was first added to NetMRI.
    |  ``attribute type:`` string

    |  ``PolicyRuleUpdatedAt:`` The date and time the policy rule was last updated in NetMRI.
    |  ``attribute type:`` string

    |  ``PolicyRuleRemediation:`` The textual remediation description associated with the rule.
    |  ``attribute type:`` string

    |  ``PolicyRuleShortName:`` The policy rule short name, used on the policy status display.
    |  ``attribute type:`` string

    |  ``PolicyRuleReadOnlyInd:`` A flag indicating whether this is a read-only policy rule.
    |  ``attribute type:`` bool


    |  ``policy_rule_set_filter_text:`` Returns a human-readable text version of the policy rule set filter.
    |  ``attribute type:`` string

    |  ``policy_rule_rule_logic_text:`` Returns a human readable text version of the policy rule logic.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "PolicyRuleID",
                  "PolicyRuleStartTime",
                  "PolicyRuleEndTime",
                  "PolicyRuleChangedCols",
                  "PolicyRuleTimestamp",
                  "PolicyRuleFirstSeenTime",
                  "PolicyRuleName",
                  "PolicyRuleDescription",
                  "PolicyRuleAuthor",
                  "PolicyRuleSetFilter",
                  "PolicyRuleRuleLogic",
                  "PolicyRuleSeverity",
                  "PolicyRuleActionAfterExec",
                  "PolicyRuleCreatedAt",
                  "PolicyRuleUpdatedAt",
                  "PolicyRuleRemediation",
                  "PolicyRuleShortName",
                  "PolicyRuleReadOnlyInd",
                  "policy_rule_set_filter_text",
                  "policy_rule_rule_logic_text",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"PolicyRuleID": self.PolicyRuleID})

    @property
    @check_api_availability
    def devices(self):
        """
        The devices against which this rule was evaluated.
        ``attribute type:`` model
        """
        return self.broker.devices(**{"PolicyRuleID": self.PolicyRuleID})
