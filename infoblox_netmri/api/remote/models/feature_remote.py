from ..remote import RemoteModel


class FeatureRemote(RemoteModel):
    """
    The features licensed within this NetMRI deployment.


    |  ``name:`` The feature name. This is the same name shown on the API documentation pages for the required feature.
    |  ``attribute type:`` string

    """

    properties = ("name",
                  )
