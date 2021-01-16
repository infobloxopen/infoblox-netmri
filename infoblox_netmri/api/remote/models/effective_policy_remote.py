from ..remote import RemoteModel
from infoblox_netmri.utils.utils import check_api_availability


class EffectivePolicyRemote(RemoteModel):
    """
    The policies, as they were defined at the time of policy evaluation. The policies described in here correspond to the policy results expressed in the DevicePolicy and other results models.


    |  ``DataSourceID:`` The internal NetMRI identifier for the collector NetMRI that collected this data record.
    |  ``attribute type:`` number


    |  ``PolicyID:`` The internal NetMRI identifier for this effective policy.
    |  ``attribute type:`` number

    |  ``PolicyStartTime:`` The starting effective time of this record.
    |  ``attribute type:`` datetime

    |  ``PolicyEndTime:`` The ending effective time of this record, or empty if still in effect.
    |  ``attribute type:`` datetime

    |  ``PolicyChangedCols:`` The fields that changed between this revision of the record and the previous revision.
    |  ``attribute type:`` string

    |  ``PolicyTimestamp:`` The date and time this record was collected or calculated.
    |  ``attribute type:`` datetime

    |  ``PolicyFirstSeenTime:`` The data and time this policy was first seen (as identified by the policy short name).
    |  ``attribute type:`` datetime

    |  ``PolicyName:`` The long name of the policy.
    |  ``attribute type:`` string

    |  ``PolicyDescription:`` The policy description, as entered at the time of policy execution.
    |  ``attribute type:`` string

    |  ``PolicyAuthor:`` The policy author name.
    |  ``attribute type:`` string

    |  ``PolicySetFilter:`` The XML SetFilter used to define whether this policy applies to a given device.
    |  ``attribute type:`` string

    |  ``PolicyCreatedAt:`` The date and time at which this policy was first created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``PolicyUpdatedAt:`` The date and time at which this policy was last modified.
    |  ``attribute type:`` datetime

    |  ``PolicyScheduleMode:`` Not used.
    |  ``attribute type:`` string

    |  ``PolicyShortName:`` The short name of the policy, as entered in the policy design center at the time of policy creation.
    |  ``attribute type:`` string

    |  ``PolicyReadOnlyInd:`` A flag indicating whether this policy was a read-only policy at the time of execution.
    |  ``attribute type:`` bool






    |  ``policy_set_filter_text:`` Returns a human-readable text version of the policy set filter.
    |  ``attribute type:`` string

    """

    properties = ("DataSourceID",
                  "PolicyID",
                  "PolicyStartTime",
                  "PolicyEndTime",
                  "PolicyChangedCols",
                  "PolicyTimestamp",
                  "PolicyFirstSeenTime",
                  "PolicyName",
                  "PolicyDescription",
                  "PolicyAuthor",
                  "PolicySetFilter",
                  "PolicyCreatedAt",
                  "PolicyUpdatedAt",
                  "PolicyScheduleMode",
                  "PolicyShortName",
                  "PolicyReadOnlyInd",
                  "policy_set_filter_text",
                  )

    @property
    @check_api_availability
    def data_source(self):
        """
        The collector NetMRI that collected this data record.
        ``attribute type:`` model
        """
        return self.broker.data_source(**{"PolicyID": self.PolicyID})

    @property
    @check_api_availability
    def effective_policy_rules(self):
        """
        The effective policy rules that comprise this policy.
        ``attribute type:`` model
        """
        return self.broker.effective_policy_rules(**{"PolicyID": self.PolicyID})

    @property
    @check_api_availability
    def device_policies(self):
        """
        The policy status objects associated with this policy.
        ``attribute type:`` model
        """
        return self.broker.device_policies(**{"PolicyID": self.PolicyID})

    @property
    @check_api_availability
    def devices(self):
        """
        The devices against which this policy was evaluated.
        ``attribute type:`` model
        """
        return self.broker.devices(**{"PolicyID": self.PolicyID})

    @property
    @check_api_availability
    def device_group_policies(self):
        """
        The device group policy status summaries for this policy.
        ``attribute type:`` model
        """
        return self.broker.device_group_policies(**{"PolicyID": self.PolicyID})

    @property
    @check_api_availability
    def device_groups(self):
        """
        The device groups against which this rule was evaluated.
        ``attribute type:`` model
        """
        return self.broker.device_groups(**{"PolicyID": self.PolicyID})
