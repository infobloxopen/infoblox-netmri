from ..remote import RemoteModel


class SdnSettingRemote(RemoteModel):
    """
    This table list out the entries of SDN controller setting within NetMRI.


    |  ``id:`` The internal NetMRI identifier for this setting.
    |  ``attribute type:`` number

    |  ``virtual_network_id:`` The internal NetMRI identifier of the Virtual Network on which this controller is defined.
    |  ``attribute type:`` number

    |  ``controller_address:`` Controller IP address or hostname.
    |  ``attribute type:`` string

    |  ``protocol:`` Protocol used to communicate with controller.
    |  ``attribute type:`` string

    |  ``sdn_username:`` Username used to connect SDN controller.
    |  ``attribute type:`` string

    |  ``sdn_password:`` Password used to connect SDN controller.
    |  ``attribute type:`` string

    |  ``SecureVersion:`` Internal version of the encryption method
    |  ``attribute type:`` number

    |  ``created_at:`` The date and time when the record was initially created in NetMRI.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time when the record was last modified in NetMRI.
    |  ``attribute type:`` datetime

    |  ``UnitID:`` The internal NetMRI identifier for collector assigned to the SDN Setting
    |  ``attribute type:`` number

    |  ``sdn_type:`` Type of SDN controller. Allowed values are CISCO_APIC, MERAKI, VELOCLOUD, SILVER_PEAK, VIPTELA
    |  ``attribute type:`` string

    |  ``api_key:`` API key to access the SDN controller (MERAKI)
    |  ``attribute type:`` string

    |  ``on_prem:`` True if controller is on premises. Otherwise we consider it is in cloud.
    |  ``attribute type:`` bool

    |  ``use_global_proxy:`` Use global proxy settings to access SDN controller.
    |  ``attribute type:`` bool

    |  ``handle:`` Unique handle for single configuration
    |  ``attribute type:`` string

    |  ``scan_interface_id:`` ID of scan interface which used for controller connection
    |  ``attribute type:`` number

    |  ``ca_cert_id:`` ID of custom CA certificate.
    |  ``attribute type:`` number

    |  ``ca_cert_content:`` Content of custom CA certificate.
    |  ``attribute type:`` string

    |  ``start_blackout_schedule:`` The blackout start time in cron format.
    |  ``attribute type:`` string

    |  ``blackout_duration:`` The blackout duration in minutes.
    |  ``attribute type:`` number

    |  ``max_requests_per_second:`` Maximum Requests per Second.
    |  ``attribute type:`` number

    |  ``collect_offline_devices:`` Collect Devices In Offline Status
    |  ``attribute type:`` bool

    """

    properties = ("id",
                  "virtual_network_id",
                  "controller_address",
                  "protocol",
                  "sdn_username",
                  "sdn_password",
                  "SecureVersion",
                  "created_at",
                  "updated_at",
                  "UnitID",
                  "sdn_type",
                  "api_key",
                  "on_prem",
                  "use_global_proxy",
                  "handle",
                  "scan_interface_id",
                  "ca_cert_id",
                  "ca_cert_content",
                  "start_blackout_schedule",
                  "blackout_duration",
                  "max_requests_per_second",
                  "collect_offline_devices",
                  )
