from ..remote import RemoteModel


class FailOverConfigurationRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``unit_id:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    |  ``virtual_ip:`` none
    |  ``attribute type:`` string

    |  ``virtual_hostname:`` none
    |  ``attribute type:`` string

    |  ``replication_direct_connect:`` none
    |  ``attribute type:`` string

    |  ``primary_index:`` none
    |  ``attribute type:`` string

    |  ``first_management_ip:`` none
    |  ``attribute type:`` string

    |  ``first_management_hostname:`` none
    |  ``attribute type:`` string

    |  ``second_management_ip:`` none
    |  ``attribute type:`` string

    |  ``second_management_hostname:`` none
    |  ``attribute type:`` string

    |  ``replication_port:`` none
    |  ``attribute type:`` string

    |  ``first_replication_ip:`` none
    |  ``attribute type:`` string

    |  ``first_replication_subnet:`` none
    |  ``attribute type:`` string

    |  ``second_replication_ip:`` none
    |  ``attribute type:`` string

    |  ``second_replication_subnet:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "unit_id",
                  "status",
                  "virtual_ip",
                  "virtual_hostname",
                  "replication_direct_connect",
                  "primary_index",
                  "first_management_ip",
                  "first_management_hostname",
                  "second_management_ip",
                  "second_management_hostname",
                  "replication_port",
                  "first_replication_ip",
                  "first_replication_subnet",
                  "second_replication_ip",
                  "second_replication_subnet",
                  )
