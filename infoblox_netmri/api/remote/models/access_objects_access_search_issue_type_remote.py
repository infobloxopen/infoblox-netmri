from ..remote import RemoteModel


class AccessObjectsAccessSearchIssueTypeRemote(RemoteModel):
    """
    Objects, or direct values, related to Alerts (whitelist or Blacklist) definition


    |  ``id:`` The internal NetMRI identifier for this access search alert.
    |  ``attribute type:`` number

    |  ``access_search_issue_type_id:`` The internal NetMRI identifier for the access search issue type this record is associated with.
    |  ``attribute type:`` number

    |  ``access_search_issue_type_field:`` The name of the issue type field.
    |  ``attribute type:`` string

    |  ``element_type:`` The element type, DeviceObject, DeviceService, IPv4Value, or FlowValue.
    |  ``attribute type:`` string

    |  ``element_id:`` The internal NetMRI identifier for the related element_type, NULL for a direct value.
    |  ``attribute type:`` number

    |  ``name:`` The global name of the object, NULL for a direct value.
    |  ``attribute type:`` string

    |  ``value:`` The value of the object or direct value. A list of ipv4 or flow value in csv format.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "access_search_issue_type_id",
                  "access_search_issue_type_field",
                  "element_type",
                  "element_id",
                  "name",
                  "value",
                  )
