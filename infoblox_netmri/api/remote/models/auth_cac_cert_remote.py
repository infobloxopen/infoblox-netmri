from ..remote import RemoteModel


class AuthCacCertRemote(RemoteModel):
    """
    CAC certificates for CAC auth and mapping to OSCP servers


    |  ``id:`` Record ID
    |  ``attribute type:`` number

    |  ``auth_server_id:`` ID of auth server of OCSP auth service
    |  ``attribute type:`` number

    |  ``uploaded_certificate_id:`` ID of linked uploaded certificate
    |  ``attribute type:`` number

    |  ``is_ocsp_cert:`` Use cert in OCSP requests if TRUE
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "auth_server_id",
                  "uploaded_certificate_id",
                  "is_ocsp_cert",
                  )
