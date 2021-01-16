from ..remote import RemoteModel


class ConfigTemplateRemote(RemoteModel):
    """
    Configuration templates information.


    |  ``id:`` The internal NetMRI identifier of the configuration template.
    |  ``attribute type:`` number

    |  ``name:`` The name of the config template.
    |  ``attribute type:`` string

    |  ``vendor:`` The device vendor name associated with the config template.
    |  ``attribute type:`` string

    |  ``model:`` The device model name associated with the config template.
    |  ``attribute type:`` string

    |  ``version:`` The device OS version associated with the config template.
    |  ``attribute type:`` string

    |  ``device_type:`` The device type associated with the config template.
    |  ``attribute type:`` string

    |  ``description:`` A description for the config template.
    |  ``attribute type:`` string

    |  ``created_by:`` The user that created the config template.
    |  ``attribute type:`` string

    |  ``updated_by:`` The user that last updated the config template.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the config template was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the config template was updated.
    |  ``attribute type:`` datetime

    |  ``template_type:`` The template type denotes whether devices or interfaces should be specified when the template job is scheduled or run. The value could be either 'Device' or 'Interface'.
    |  ``attribute type:`` string

    |  ``risk_level:`` The user-specified risk level for the template. Possible levels are 1 (low), 2 (medium), and 3 (high).  To run higher risk templates, higher privileges are required.
    |  ``attribute type:`` number

    |  ``template_text:`` The text of the config template.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "vendor",
                  "model",
                  "version",
                  "device_type",
                  "description",
                  "created_by",
                  "updated_by",
                  "created_at",
                  "updated_at",
                  "template_type",
                  "risk_level",
                  "template_text",
                  )
