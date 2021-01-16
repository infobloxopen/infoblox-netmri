from ..remote import RemoteModel


class SettingsDeviceSupportBundlesGridRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``name:`` none
    |  ``attribute type:`` string

    |  ``version:`` none
    |  ``attribute type:`` string

    |  ``author:`` none
    |  ``attribute type:`` string

    |  ``neighbor_ind:`` none
    |  ``attribute type:`` string

    |  ``inventory_ind:`` none
    |  ``attribute type:`` string

    |  ``environmental_ind:`` none
    |  ``attribute type:`` string

    |  ``cpu_ind:`` none
    |  ``attribute type:`` string

    |  ``memory_ind:`` none
    |  ``attribute type:`` string

    |  ``vlan_ind:`` none
    |  ``attribute type:`` string

    |  ``forwarding_ind:`` none
    |  ``attribute type:`` string

    |  ``port_ind:`` none
    |  ``attribute type:`` string

    |  ``config_ind:`` none
    |  ``attribute type:`` string

    |  ``valid_ind:`` none
    |  ``attribute type:`` string

    |  ``unit_tests:`` none
    |  ``attribute type:`` string

    |  ``status:`` none
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "name",
                  "version",
                  "author",
                  "neighbor_ind",
                  "inventory_ind",
                  "environmental_ind",
                  "cpu_ind",
                  "memory_ind",
                  "vlan_ind",
                  "forwarding_ind",
                  "port_ind",
                  "config_ind",
                  "valid_ind",
                  "unit_tests",
                  "status",
                  )
