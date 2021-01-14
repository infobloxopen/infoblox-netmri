from ..remote import RemoteModel


class AuthServerGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``priority:`` none
    |  ``attribute type:`` string

    |  ``auth_server:`` none
    |  ``attribute type:`` string

    |  ``auth_port:`` none
    |  ``attribute type:`` string

    |  ``auth_encryption:`` none
    |  ``attribute type:`` string

    |  ``auth_cert:`` none
    |  ``attribute type:`` string

    |  ``certificate:`` none
    |  ``attribute type:`` string

    |  ``ocsp_certs:`` none
    |  ``attribute type:`` string

    |  ``interface:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``auth_shared_secret:`` none
    |  ``attribute type:`` string

    |  ``enabled_ind:`` none
    |  ``attribute type:`` string

    |  ``auth_version:`` none
    |  ``attribute type:`` string

    |  ``source_interface_id:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "priority",
                  "auth_server",
                  "auth_port",
                  "auth_encryption",
                  "auth_cert",
                  "certificate",
                  "ocsp_certs",
                  "interface",
                  "status",
                  "auth_shared_secret",
                  "enabled_ind",
                  "auth_version",
                  "source_interface_id",
                  )
