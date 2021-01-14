from ..remote import RemoteModel


class DiscoverySettingRemote(RemoteModel):
    """
    Discovery settings used by the NetMRI discovery engine.


    |  ``id:`` The internal NetMRI identifier for the discovery setting.
    |  ``attribute type:`` number

    |  ``range_value:`` The discovery setting value.
    |  ``attribute type:`` string

    |  ``range_start:`` The starting IP address for the discovery setting.
    |  ``attribute type:`` string

    |  ``range_end:`` The ending IP address for the discovery setting.
    |  ``attribute type:`` string

    |  ``range_start_numeric:`` The starting IP address numeric value for the discovery setting.
    |  ``attribute type:`` number

    |  ``range_end_numeric:`` The ending IP address numeric value for the discovery setting.ange_end_numeric.
    |  ``attribute type:`` number

    |  ``range_mask:`` The CIDR mask for the discovery setting.
    |  ``attribute type:`` number

    |  ``range_type:`` The discovery setting range type (CIDR, RANGE, SEED, STATIC, WILDCARD).
    |  ``attribute type:`` string

    |  ``discovery_status:`` The discovery mode of the discovery setting (INCLUDE, EXCLUDE, IGNORE).
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the discovery setting was created.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the discovery setting was updated.
    |  ``attribute type:`` datetime

    |  ``UnitID:`` The internal NetMRI identifier collector assigned to the discovery setting.
    |  ``attribute type:`` number

    |  ``created_by:`` The user that created the discovery setting.
    |  ``attribute type:`` string

    |  ``updated_by:`` The user that last updated the discovery setting.
    |  ``attribute type:`` string

    |  ``ping_sweep_ind:`` A flag indicating if ping sweeps are used on the discovery setting.
    |  ``attribute type:`` bool

    |  ``smart_ping_sweep_ind:`` A flag indicating if smart ping sweep should be used on the discovery setting.
    |  ``attribute type:`` bool

    |  ``start_blackout_schedule:`` The blackout start time in cron format.
    |  ``attribute type:`` string

    |  ``blackout_duration:`` The blackout duration in minutes.
    |  ``attribute type:`` number

    |  ``virtual_network_id:`` A Virtual Network identifier assigned to the discovery setting.
    |  ``attribute type:`` number

    |  ``start_port_control_blackout_schedule:`` Port Control Blackout schedule in CRON format
    |  ``attribute type:`` string

    |  ``port_control_blackout_duration:`` Port Control Blackout duration in minutes
    |  ``attribute type:`` number

    |  ``cidr_count:`` Number of CIDRs in discovery range.
    |  ``attribute type:`` number

    """

    properties = ("id",
                  "range_value",
                  "range_start",
                  "range_end",
                  "range_start_numeric",
                  "range_end_numeric",
                  "range_mask",
                  "range_type",
                  "discovery_status",
                  "created_at",
                  "updated_at",
                  "UnitID",
                  "created_by",
                  "updated_by",
                  "ping_sweep_ind",
                  "smart_ping_sweep_ind",
                  "start_blackout_schedule",
                  "blackout_duration",
                  "virtual_network_id",
                  "start_port_control_blackout_schedule",
                  "port_control_blackout_duration",
                  "cidr_count",
                  )
