from ..remote import RemoteModel


class UploadedCertificateRemote(RemoteModel):
    """
    Repository of uploaded CA certificates for Active Directory, IF-MAP Server Connections, and other services.


    |  ``id:`` The internal NetMRI identifier for the certificate
    |  ``attribute type:`` number

    |  ``name:`` User-defined unique name for the certificate
    |  ``attribute type:`` string

    |  ``created_at:`` The timestamp of when the certificate was uploaded
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The timestamp of when the certificate was updated
    |  ``attribute type:`` datetime

    |  ``path:`` Internal use only
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "created_at",
                  "updated_at",
                  "path",
                  )
