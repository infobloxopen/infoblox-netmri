from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DevicePolicyRemote(RemoteModel):
    """
    The policy status for each device, per policy.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number

    |  ``DeviceID:`` The internal NetMRI identifier for the device whose policy status this record represents.
    |  ``attribute type:`` number

    |  ``DevicePolicyChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DevicePolicyEndTime:`` The ending effective time of this revision of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DevicePolicyID:`` The internal NetMRI identifier for this device policy status record.
    |  ``attribute type:`` number

    |  ``DevicePolicyStartTime:`` The starting effective time of this revision of the record.
    |  ``attribute type:`` datetime

    |  ``DevicePolicyTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``PolicyID:`` The internal NetMRI identifier for the policy whose status this record represents.
    |  ``attribute type:`` number

    |  ``PolicyRulesChecked:`` The total number of rules that were checked against this device for this policy. Invalid rules and rules that are skipped due to the device not matching the rule filter are not counted as 'checked' rules.
    |  ``attribute type:`` number

    |  ``PolicyRulesError:`` The total number of rules in this policy that the device failed with error status.
    |  ``attribute type:`` number

    |  ``PolicyRulesFailed:`` The total number of rules in this policy that the device failed with info, warning, or error status.
    |  ``attribute type:`` number

    |  ``PolicyRulesInfo:`` The total number of rules in this policy that the device failed with info status.
    |  ``attribute type:`` number

    |  ``PolicyRulesInvalid:`` The total number of invalid rules that were in this policy at the time the policy was executed against this device.
    |  ``attribute type:`` number

    |  ``PolicyRulesPassed:`` The total number of rules in this policy that the device passed successfully.
    |  ``attribute type:`` number

    |  ``PolicyRulesSkipped:`` The total number of rules in this policy that were skipped due to the device not matching the rule filters.
    |  ``attribute type:`` number

    |  ``PolicyRulesTotal:`` The total number of rules that in this policy at the time the policy was executed against this device.
    |  ``attribute type:`` number

    |  ``PolicyRulesUnknown:`` The total number of rules that could not be fully evaluated because information needed for the rule was not available (for example, the configuration file has not been collected for the device).
    |  ``attribute type:`` number

    |  ``PolicyRulesValid:`` The total number of valid rules that were in this policy at the time the policy was executed against this device. An invalid rule generally only occurs if the XML rule build has been used and an improper XML format has been specified.
    |  ``attribute type:`` number

    |  ``PolicyRulesWarning:`` The total number of rules in this policy that the device failed with warning status.
    |  ``attribute type:`` number

    |  ``PolicyStatus:`` The current status of this policy for this device.
    |  ``attribute type:`` string




    |  ``policy_name:`` The policy name.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "DeviceID",
                  "DevicePolicyChangedCols",
                  "DevicePolicyEndTime",
                  "DevicePolicyID",
                  "DevicePolicyStartTime",
                  "DevicePolicyTimestamp",
                  "PolicyID",
                  "PolicyRulesChecked",
                  "PolicyRulesError",
                  "PolicyRulesFailed",
                  "PolicyRulesInfo",
                  "PolicyRulesInvalid",
                  "PolicyRulesPassed",
                  "PolicyRulesSkipped",
                  "PolicyRulesTotal",
                  "PolicyRulesUnknown",
                  "PolicyRulesValid",
                  "PolicyRulesWarning",
                  "PolicyStatus",
                  "policy_name",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The NetMRI device that collected this record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DevicePolicyID": self.DevicePolicyID})

    @property
    @check_api_availability
    def device(self):
        """
        The device whose policy status this record represents.
        ``attribute type:`` model
        """
        return self.broker.device(**{"DevicePolicyID": self.DevicePolicyID})

    @property
    @check_api_availability
    def infradevice(self):
        """
        The device whose policy status this record represents.
        ``attribute type:`` model
        """
        return self.broker.infradevice(**{"DevicePolicyID": self.DevicePolicyID})
