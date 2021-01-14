from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class DeviceGroupPolicyRemote(RemoteModel):
    """
    The policy status per policy, per device group.


    |  ``DeviceGroupPolicyID:`` The internal NetMRI identifier for this device group policy status record.
    |  ``attribute type:`` number

    |  ``GroupID:`` The internal NetMRI identifier of the associated device group.
    |  ``attribute type:`` number

    |  ``PolicyID:`` The internal NetMRI identifier of the associated effective policy.
    |  ``attribute type:`` number

    |  ``DeviceGroupPolicyStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupPolicyEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``DeviceGroupPolicyChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``DeviceGroupPolicyTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``PolicyStatus:`` The overall status for this device group an policy.
    |  ``attribute type:`` string

    |  ``DevicesTotal:`` The number of devices in this device group against which this policy was deployed at the time of evaluation.
    |  ``attribute type:`` number

    |  ``DevicesValid:`` The number of devices in this device group for which the policy was successfully evaluated (that is, without a failure such as an invalid XML-based rule).
    |  ``attribute type:`` number

    |  ``DevicesChecked:`` The number of devices in this device group for which the policy status was checked (this excludes devices that do not meet the policy filter criteria).
    |  ``attribute type:`` number

    |  ``DevicesInvalid:`` The number of devices in this device group for which the policy evaluation failed due to an invalid rule definition or internal error for this policy.
    |  ``attribute type:`` number

    |  ``DevicesPassed:`` The number of devices in this device group for which the policy status result for this policy is Passed.
    |  ``attribute type:`` number

    |  ``DevicesFailed:`` The number of devices in this device group for which the policy status result for this policy is Error, Warning, or Info.
    |  ``attribute type:`` number

    |  ``DevicesError:`` The number of devices in this device group for which the policy status result for this policy is Error.
    |  ``attribute type:`` number

    |  ``DevicesWarning:`` The number of devices in this device group for which the policy status result for this policy is Warning.
    |  ``attribute type:`` number

    |  ``DevicesInfo:`` The number of devices in this device group for which the policy status result for this policy is Info.
    |  ``attribute type:`` number

    |  ``DevicesSkipped:`` The number of devices in this device group for which the policy status result for this policy is Skipped. This refers to devices that do not meet the policy filter criteria.
    |  ``attribute type:`` number

    |  ``DevicesUnknown:`` The number of devices in this device group for which the policy status result for this policy is Unknown. This refers to devices for which a configuration file or other necessary data is not available.
    |  ``attribute type:`` number

    |  ``policy_name:`` The policy name.
    |  ``attribute type:`` string

    |  ``group_name:`` The group name.
    |  ``attribute type:`` string

    """

    properties = ("DeviceGroupPolicyID",
                  "GroupID",
                  "PolicyID",
                  "DeviceGroupPolicyStartTime",
                  "DeviceGroupPolicyEndTime",
                  "DeviceGroupPolicyChangedCols",
                  "DeviceGroupPolicyTimestamp",
                  "DataSourceID",
                  "PolicyStatus",
                  "DevicesTotal",
                  "DevicesValid",
                  "DevicesChecked",
                  "DevicesInvalid",
                  "DevicesPassed",
                  "DevicesFailed",
                  "DevicesError",
                  "DevicesWarning",
                  "DevicesInfo",
                  "DevicesSkipped",
                  "DevicesUnknown",
                  "policy_name",
                  "group_name",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"DeviceGroupPolicyID": self.DeviceGroupPolicyID})
