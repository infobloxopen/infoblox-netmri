from ..remote import RemoteModel


class DeviceSupportBundleRemote(RemoteModel):
    """
    Describes supported devices, except core supported devices.


    |  ``id:`` The internal NetMRI identifier of the Device Support Bundle.
    |  ``attribute type:`` number

    |  ``name:`` The unique name of the Device Support Bundle.
    |  ``attribute type:`` string

    |  ``version:`` The version of the Device Support Bundle.
    |  ``attribute type:`` string

    |  ``author:`` The author of the Device Support Bundle.
    |  ``attribute type:`` string

    |  ``enabled_ind:`` A flag indicating if the Device Support Bundle is enabled.
    |  ``attribute type:`` bool

    |  ``system_ind:`` A flag indicating if system information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``neighbor_ind:`` A flag indicating if neighbor information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``inventory_ind:`` A flag indicating if inventory information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``environmental_ind:`` A flag indicating if environmental information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``cpu_ind:`` A flag indicating if CPU information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``memory_ind:`` A flag indicating if memory information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``vlan_ind:`` A flag indicating if VLAN information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``forwarding_ind:`` A flag indicating if forwarding information is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``port_ind:`` A flag indicating if port config is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``config_ind:`` A flag indicating if configuration is shown in Device Viewer for devices.
    |  ``attribute type:`` bool

    |  ``created_by:`` Indicates by whom Device Support Bundle was created.
    |  ``attribute type:`` string

    |  ``updated_by:`` Indicates by whom the Device Support Bundle was updated.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the Device Support Bundle was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the Device Support Bundle was updated.
    |  ``attribute type:`` datetime

    |  ``valid_ind:`` A flag indicating whether the Device Support Bundle is valid.
    |  ``attribute type:`` bool

    |  ``unit_tests:`` The current state of unit testing for the Device Support Bundle.
    |  ``attribute type:`` string

    |  ``status:`` The current editing state of the Device Support Bundle.
    |  ``attribute type:`` string

    |  ``integrated_ind:`` A flag indicating if the Device Support Bundle is integrated.
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "name",
                  "version",
                  "author",
                  "enabled_ind",
                  "system_ind",
                  "neighbor_ind",
                  "inventory_ind",
                  "environmental_ind",
                  "cpu_ind",
                  "memory_ind",
                  "vlan_ind",
                  "forwarding_ind",
                  "port_ind",
                  "config_ind",
                  "created_by",
                  "updated_by",
                  "created_at",
                  "updated_at",
                  "valid_ind",
                  "unit_tests",
                  "status",
                  "integrated_ind",
                  )
