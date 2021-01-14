from ..remote import RemoteModel


class DeviceCertificateRemote(RemoteModel):
    """
    This table list out the device certificates.


    |  ``id:`` The internal NetMRI identifier for this device certificate.
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``certificate:`` The certificate BLOB data.
    |  ``attribute type:`` string

    |  ``certificate_parameter:`` The certificate parameters.
    |  ``attribute type:`` string

    |  ``certificate_type:`` The type of certificate.
    |  ``attribute type:`` string

    |  ``UnitID:`` The internal NetMRI identifier for collector.
    |  ``attribute type:`` number

    |  ``ip_address_dotted:`` The IP address as string.
    |  ``attribute type:`` string

    |  ``ip_address_numeric:`` The IP address as number.
    |  ``attribute type:`` number

    |  ``name:`` The certificate name.
    |  ``attribute type:`` string

    |  ``username:`` The username for certificate.
    |  ``attribute type:`` string

    |  ``password:`` The password for certificate.
    |  ``attribute type:`` string

    |  ``passphrase:`` The passphrase for certificate.
    |  ``attribute type:`` string

    |  ``port:`` Port number to use for connection with this certificate.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "created_at",
                  "updated_at",
                  "certificate",
                  "certificate_parameter",
                  "certificate_type",
                  "UnitID",
                  "ip_address_dotted",
                  "ip_address_numeric",
                  "name",
                  "username",
                  "password",
                  "passphrase",
                  "port",
                  )
