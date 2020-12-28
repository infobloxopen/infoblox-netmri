from ..remote import RemoteModel


class UploadedCertificateGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``certificate_id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``issuer:`` none
    |  ``attribute type:`` string

    |  ``validFrom:`` none
    |  ``attribute type:`` string

    |  ``validUntil:`` none
    |  ``attribute type:`` string

    |  ``subject:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "certificate_id",
                  "name",
                  "issuer",
                  "validFrom",
                  "validUntil",
                  "subject",
                  )
