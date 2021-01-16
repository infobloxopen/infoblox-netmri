from ..remote import RemoteModel


class AccessProvisioningAlertsRulesGridRemote(RemoteModel):
    """
    list of alerts


    |  ``id:`` The internal NetMRI identifier for this alert view.
    |  ``attribute type:`` number

    |  ``issue_meta_type_id:`` The name of the meta type of this alert. One of 'WhiteList', 'BlackList'.
    |  ``attribute type:`` string

    |  ``name:`` The name for this search alert.
    |  ``attribute type:`` string

    |  ``sources:`` The list of source network objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``destinations:`` The list of destination network objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``source_ports:`` The list of service objects used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``services:`` The list of source ports used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``access:`` The allowance of rule used as criteria for this search alert.
    |  ``attribute type:`` string

    |  ``workbook_id:`` The internal NetMRI identifier of the workbook of rule lists on which the searches for this alert should applied.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "issue_meta_type_id",
                  "name",
                  "sources",
                  "destinations",
                  "source_ports",
                  "services",
                  "access",
                  "workbook_id",
                  )
