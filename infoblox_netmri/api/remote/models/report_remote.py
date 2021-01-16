from ..remote import RemoteModel


class ReportRemote(RemoteModel):
    """
    Standard and custom reports that are available in the current NetMRI instance.


    |  ``id:`` The id of the report
    |  ``attribute type:`` number

    |  ``name:`` The name of the report
    |  ``attribute type:`` string

    |  ``file_name:`` The file name where the report is defined
    |  ``attribute type:`` string

    |  ``description:`` Description of the report
    |  ``attribute type:`` string

    |  ``category_id:`` Id of the report category
    |  ``attribute type:`` number

    |  ``thumbnail_url:`` url of the report image displayed in the Reports &gt; Report Gallery view
    |  ``attribute type:`` string

    |  ``image_url:`` (always nil)
    |  ``attribute type:`` string

    |  ``report_url:`` report url
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``report_type:`` The type of the report
    |  ``attribute type:`` string

    |  ``hidden_ind:`` A flag indicating whether the report is hidden or not.
    |  ``attribute type:`` bool

    |  ``pre_packaged_ind:`` A flag indicating whether the report is prepackaged or not.
    |  ``attribute type:`` bool

    |  ``short_headings_ind:`` A flag indicating whether the report uses short headings or not.
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "name",
                  "file_name",
                  "description",
                  "category_id",
                  "thumbnail_url",
                  "image_url",
                  "report_url",
                  "created_at",
                  "updated_at",
                  "report_type",
                  "hidden_ind",
                  "pre_packaged_ind",
                  "short_headings_ind",
                  )
