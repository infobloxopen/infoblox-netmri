from ..remote import RemoteModel


class ApicSettingRemote(RemoteModel):
    """



    |  ``id:`` none
    |  ``attribute type:`` string

    |  ``virtual_network_id:`` none
    |  ``attribute type:`` string

    |  ``controller_address:`` none
    |  ``attribute type:`` string

    |  ``protocol:`` none
    |  ``attribute type:`` string

    |  ``sdn_username:`` none
    |  ``attribute type:`` string

    |  ``sdn_password:`` none
    |  ``attribute type:`` string

    |  ``SecureVersion:`` none
    |  ``attribute type:`` string

    |  ``created_at:`` none
    |  ``attribute type:`` string

    |  ``updated_at:`` none
    |  ``attribute type:`` string

    |  ``UnitID:`` none
    |  ``attribute type:`` string

    |  ``sdn_type:`` none
    |  ``attribute type:`` string

    |  ``api_key:`` none
    |  ``attribute type:`` string

    |  ``on_prem:`` none
    |  ``attribute type:`` string

    |  ``use_global_proxy:`` none
    |  ``attribute type:`` string

    |  ``handle:`` none
    |  ``attribute type:`` string

    |  ``scan_interface_id:`` none
    |  ``attribute type:`` string

    |  ``start_blackout_schedule:`` none
    |  ``attribute type:`` string

    |  ``blackout_duration:`` none
    |  ``attribute type:`` string

    |  ``max_requests_per_second:`` none
    |  ``attribute type:`` string

    |  ``collect_offline_devices:`` none
    |  ``attribute type:`` string

    |  ``ca_cert_id:`` none
    |  ``attribute type:`` string

    |  ``ca_cert_content:`` none
    |  ``attribute type:`` string

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
                  "start_blackout_schedule",
                  "blackout_duration",
                  "max_requests_per_second",
                  "collect_offline_devices",
                  "ca_cert_id",
                  "ca_cert_content",
                  )
