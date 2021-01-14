from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePolicyRuleRemote(RemoteModel):
    """
    The policy rule status for each device, per policy, per rule.


    |  ``DevicePolicyRuleID:`` The internal NetMRI identifier for this device policy rule status.
    |  ``attribute type:`` number

    |  ``DevicePolicyID:`` The internal NetMRI identifier for the corresponding device policy status.
    |  ``attribute type:`` number

    |  ``DevicePolicyRuleStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DevicePolicyRuleEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DevicePolicyRuleChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DevicePolicyRuleTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``PolicyRuleID:`` The internal NetMRI identifier for the effective Policy Rule object.
    |  ``attribute type:`` number

    |  ``PolicyRuleStatus:`` The policy rule status result for the evaluation of the specified rule against the corresponding device (see DevicePolicy to retrieve the device).
    |  ``attribute type:`` string

    |  ``PolicyRuleMessage:`` The textual message associated with this policy rule status.
    |  ``attribute type:`` string

    |  ``PolicyRuleLineNo:`` For configuration file rule violations, the line number in the device configuration file on which the violation occurs.
    |  ``attribute type:`` string

    |  ``PolicyRuleContext:`` The specific lines within the device configuration file that surround and include the line in violation.
    |  ``attribute type:`` string


    |  ``policy_name:`` The policy name associated with this usage of the rulelist.
    |  ``attribute type:`` string

    |  ``policy_rule_name:`` The rule name.
    |  ``attribute type:`` string

    |  ``policy_rule_short_name:`` The short rule name.
    |  ``attribute type:`` string

    |  ``policy_rule_severity:`` The rule severity.
    |  ``attribute type:`` string

    """

    properties = ("DevicePolicyRuleID",
                  "DevicePolicyID",
                  "DevicePolicyRuleStartTime",
                  "DevicePolicyRuleEndTime",
                  "DevicePolicyRuleChangedCols",
                  "DevicePolicyRuleTimestamp",
                  "DataSourceID",
                  "PolicyRuleID",
                  "PolicyRuleStatus",
                  "PolicyRuleMessage",
                  "PolicyRuleLineNo",
                  "PolicyRuleContext",
                  "policy_name",
                  "policy_rule_name",
                  "policy_rule_short_name",
                  "policy_rule_severity",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePolicyRuleID": self.DevicePolicyRuleID})

    @property
    @check_api_availability
    def device(self):
        """
        The device to which this policy rule is attached.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePolicyRuleID": self.DevicePolicyRuleID})
