from ..remote import RemoteModel


class AttributeDocRemote(RemoteModel):
    """
    Documentation for model attributes.


    |  ``id:`` The internal NetMRI identifier for this attribute.
    |  ``attribute type:`` number

    |  ``attribute:`` Attribute name for this record.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``default_column_ind:`` A flag indicating if this is default column/
    |  ``attribute type:`` bool

    |  ``default_sort_desc_ind:`` A flag indicating if default sort order is descending.
    |  ``attribute type:`` bool

    |  ``description:`` Attribute description
    |  ``attribute type:`` string

    |  ``gui_type:`` Data type used in GUI to handle the attribute.
    |  ``attribute type:`` string

    |  ``hidden_ind:`` A flag indicating if attribute is hidden
    |  ``attribute type:`` bool

    |  ``method_ind:`` A flag indicating if attribute is method
    |  ``attribute type:`` bool

    |  ``method_param_list:`` Parameter list for method
    |  ``attribute type:`` string

    |  ``model_doc_id:`` The internal NetMRI identifier of Model the attribute is assigned to.
    |  ``attribute type:`` number

    |  ``name:`` Human readable attribute name.
    |  ``attribute type:`` string

    |  ``return_model_doc_id:`` The internal NetMRI identifier of Model returned by method.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "attribute",
                  "created_at",
                  "updated_at",
                  "default_column_ind",
                  "default_sort_desc_ind",
                  "description",
                  "gui_type",
                  "hidden_ind",
                  "method_ind",
                  "method_param_list",
                  "model_doc_id",
                  "name",
                  "return_model_doc_id",
                  )
