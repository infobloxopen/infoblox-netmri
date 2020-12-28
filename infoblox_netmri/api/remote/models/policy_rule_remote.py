from ..remote import RemoteModel


class PolicyRuleRemote(RemoteModel):
    """
    This table list out the entries of policy rule definitions within the NetMRI.


    |  ``id:`` The internal NetMRI identifier of a policy rule.
    |  ``attribute type:`` number

    |  ``name:`` The name of a policy rule.
    |  ``attribute type:`` string

    |  ``description:`` The description of a policy rule.
    |  ``attribute type:`` string

    |  ``author:`` The name of an author defined in a policy rule.
    |  ``attribute type:`` string

    |  ``set_filter:`` The filter defined in a policy rule.
    |  ``attribute type:`` string

    |  ``rule_logic:`` The logical rules defined in a policy rule.
    |  ``attribute type:`` string

    |  ``severity:`` The issue severity (1 = Error, 2 = Warning, 3 = Info). Useful for sorting.
    |  ``attribute type:`` string

    |  ``action_after_exec:`` The action occurred after execution of a policy rule.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``remediation:`` The remediation of a policy rule.
    |  ``attribute type:`` string

    |  ``short_name:`` The short name of a policy.
    |  ``attribute type:`` string

    |  ``read_only:`` The read only mode of a policy.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "name",
                  "description",
                  "author",
                  "set_filter",
                  "rule_logic",
                  "severity",
                  "action_after_exec",
                  "created_at",
                  "updated_at",
                  "remediation",
                  "short_name",
                  "read_only",
                  )
