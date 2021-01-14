from ..remote import RemoteModel


class FailOverConfigurationGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``unit_id:`` none
    |  ``attribute type:`` string

    |  ``virtual_ip:`` none
    |  ``attribute type:`` string

    |  ``virtual_hostname:`` none
    |  ``attribute type:`` string

    |  ``connection_mode:`` none
    |  ``attribute type:`` string

    |  ``first_management_ip:`` none
    |  ``attribute type:`` string

    |  ``second_management_ip:`` none
    |  ``attribute type:`` string

    |  ``first_management_hostname:`` none
    |  ``attribute type:`` string

    |  ``second_management_hostname:`` none
    |  ``attribute type:`` string

    |  ``first_replication_ip:`` none
    |  ``attribute type:`` string

    |  ``second_replication_ip:`` none
    |  ``attribute type:`` string

    |  ``replication_port:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "unit_id",
                  "virtual_ip",
                  "virtual_hostname",
                  "connection_mode",
                  "first_management_ip",
                  "second_management_ip",
                  "first_management_hostname",
                  "second_management_hostname",
                  "first_replication_ip",
                  "second_replication_ip",
                  "replication_port",
                  "status",
                  )
