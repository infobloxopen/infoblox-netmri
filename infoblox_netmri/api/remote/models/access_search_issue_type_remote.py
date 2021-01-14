from ..remote import RemoteModel


class AccessSearchIssueTypeRemote(RemoteModel):
    """
    Alerts (whitelist or Blacklist) definition


    |  ``id:`` The internal NetMRI identifier for this access search alert.
    |  ``attribute type:`` number

    |  ``issue_meta_type_id:`` The name of meta type of issue associated with this alert. One of 'WhiteList' or 'BlackList'.
    |  ``attribute type:`` string

    |  ``name:`` The name of this alert..
    |  ``attribute type:`` string

    |  ``sources:`` The list of source network objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``destinations:`` The list of destination network objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``source_ports:`` The list of service objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``services:`` The list of source ports used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``access:`` The allowance of rule used as criteria for this search alert. One if 'Allow', 'Deny' or 'Any.
    |  ``attribute type:`` string

    |  ``exact_match:`` A flag indicating whether only rules that match exactly the criteria should be returned.
    |  ``attribute type:`` number

    |  ``workbook_id:`` The internal NetMRI identifier of the workbook of rule lists on which the searches for this alert should applied.
    |  ``attribute type:`` string

    |  ``issue_type_id:`` The internal NetMRI identifier computed for this search alert, which is also a type of issue.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    """

    properties = ("id",
                  "issue_meta_type_id",
                  "name",
                  "sources",
                  "destinations",
                  "source_ports",
                  "services",
                  "access",
                  "exact_match",
                  "workbook_id",
                  "issue_type_id",
                  "created_at",
                  "updated_at",
                  )
