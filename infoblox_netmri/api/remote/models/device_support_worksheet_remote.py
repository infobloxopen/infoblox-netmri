from ..remote import RemoteModel


class DeviceSupportWorksheetRemote(RemoteModel):
    """
    Device Support data requests.


    |  ``id:`` The internal system identifier of the associated device support request worksheet.
    |  ``attribute type:`` number

    |  ``device_id:`` The internal system identifier of the associated device.
    |  ``attribute type:`` number

    |  ``device_ip_dotted:`` The IP address of the associated device.
    |  ``attribute type:`` string

    |  ``netmri_version:`` The NetMRI version.
    |  ``attribute type:`` string

    |  ``license_id:`` The NetMRI license identifier.
    |  ``attribute type:`` string

    |  ``license_type:`` The NetMRI license type.
    |  ``attribute type:`` string

    |  ``license_expiration:`` The expiration of the NetMRI license
    |  ``attribute type:`` string

    |  ``device_vendor:`` The vendor of the associated device as determined by the system.
    |  ``attribute type:`` string

    |  ``device_model:`` The device model of the associated device as determined by the system.
    |  ``attribute type:`` string

    |  ``os_version:`` The OS version of the associated device as determined by the system.
    |  ``attribute type:`` string

    |  ``device_type:`` The device type of the associated device as determined by system.
    |  ``attribute type:`` string

    |  ``discovery_diagnostic_collected_ind:`` Flag indicating that discovery diagnostics were collected.
    |  ``attribute type:`` bool

    |  ``snmp_data_collected_ind:`` Flag indicating that SNMP data was collected.
    |  ``attribute type:`` bool

    |  ``cli_session_collected_ind:`` Flag indicating that CLI data was collected.
    |  ``attribute type:`` bool

    |  ``priv_mode_info:`` Privileged mode information.
    |  ``attribute type:`` string

    |  ``syslogs_collected_ind:`` Flag indicating that the syslogs were collected.
    |  ``attribute type:`` bool

    |  ``admin_guide_collected_ind:`` Flag indicating that the admin guide was collected.
    |  ``attribute type:`` bool

    |  ``access_to_device:`` Information about how Infoblox will access the device for site testing.
    |  ``attribute type:`` string

    |  ``access_to_device_other:`` Other information about how Infoblox will access the device.
    |  ``attribute type:`` string

    |  ``created_at:`` The date and time the record was initially created in the system.
    |  ``attribute type:`` datetime

    |  ``updated_at:`` The date and time the record was last modified in the system.
    |  ``attribute type:`` datetime

    |  ``user_in_device_type:`` The device type as determined by the user.
    |  ``attribute type:`` string

    |  ``user_in_device_vendor:`` The device vendor as determined by the user.
    |  ``attribute type:`` string

    |  ``user_in_device_model:`` The device model as determined by the user.
    |  ``attribute type:`` string

    |  ``user_in_os_version:`` The os version as determined by the user.
    |  ``attribute type:`` string

    |  ``user_in_device_capabilities:`` The device capabilities as determined by the user.
    |  ``attribute type:`` string

    |  ``snmp_version:`` The SNMP version of the device (SNMPv1, SNMPv2, or SNMPv3).
    |  ``attribute type:`` string

    |  ``snmp_community_string:`` The SNMP community string of the device.
    |  ``attribute type:`` string

    |  ``snmp_port:`` The SNMP port of the device.
    |  ``attribute type:`` number

    |  ``snmp_auth_username:`` The SNMP authorized username of the device (SNMPv3 only).
    |  ``attribute type:`` string

    |  ``snmp_auth_password:`` The SNMP authorized password of the device (SNMPv3 only).
    |  ``attribute type:`` string

    |  ``snmp_auth_protocol:`` The SNMP authorized protocol of the device (SNMPv3 only).
    |  ``attribute type:`` string

    |  ``snmp_privacy_password:`` The SNMP privacy password of the device (SNMPv3 only).
    |  ``attribute type:`` string

    |  ``snmp_privacy_protocol:`` The SNMP privacy protocol of the device (SNMPv3 only).
    |  ``attribute type:`` string

    |  ``preferred_cli:`` The preferred CLI method (SSH, Telnet, or Other).
    |  ``attribute type:`` string

    |  ``cli_username:`` The CLI Username of the device.
    |  ``attribute type:`` string

    |  ``cli_password:`` The CLI Password of the device.
    |  ``attribute type:`` string

    |  ``secure_version:`` The encryption secure version of the credentials.
    |  ``attribute type:`` number

    |  ``package_name:`` The name of the compressed, encrypted device support data package.
    |  ``attribute type:`` string

    |  ``device_discovered_ind:`` A flag indicating that the device has been discovered by the system.
    |  ``attribute type:`` bool

    |  ``delivery_method:`` The method of delivery (sftp, email, or download) for the device support data bundle.
    |  ``attribute type:`` string

    |  ``unit_id:`` The internal identifier for the collector that is used to collect the device support data. Used in an OC only.
    |  ``attribute type:`` number

    |  ``transaction_number:`` The transaction number used to track the device support request with Infoblox.
    |  ``attribute type:`` string

    |  ``status:`` The overall status of the device support request worksheet.
    |  ``attribute type:`` string

    |  ``step_number:`` The last step which the worksheet was saved at.
    |  ``attribute type:`` number

    |  ``delivery_addl_email:`` Additional email addresses to which the device support data bundle is sent.
    |  ``attribute type:`` string

    |  ``manual_data_entry_ind:`` Flag indicating that device data is being collected in manual mode.
    |  ``attribute type:`` bool

    |  ``status_msg:`` Error message associated with worksheet status. Currently, only contain error messages for "Transfer Failed" status.
    |  ``attribute type:`` string

    |  ``virtual_network_id:`` The internal identifier for the network which the device is associated to.
    |  ``attribute type:`` number

    |  ``network_name:`` A Network View assigned to the device.
    |  ``attribute type:`` string

    |  ``contact_method:`` How the customer should be contacted (valid values are 'Email' and 'Phone').
    |  ``attribute type:`` string

    |  ``customer_name:`` Customer name.
    |  ``attribute type:`` string

    |  ``contact_name:`` A name of a person to contact.
    |  ``attribute type:`` string

    |  ``contact_value:`` E-mail address or phone that can be used to contact the customer.
    |  ``attribute type:`` string

    """

    properties = ("id",
                  "device_id",
                  "device_ip_dotted",
                  "netmri_version",
                  "license_id",
                  "license_type",
                  "license_expiration",
                  "device_vendor",
                  "device_model",
                  "os_version",
                  "device_type",
                  "discovery_diagnostic_collected_ind",
                  "snmp_data_collected_ind",
                  "cli_session_collected_ind",
                  "priv_mode_info",
                  "syslogs_collected_ind",
                  "admin_guide_collected_ind",
                  "access_to_device",
                  "access_to_device_other",
                  "created_at",
                  "updated_at",
                  "user_in_device_type",
                  "user_in_device_vendor",
                  "user_in_device_model",
                  "user_in_os_version",
                  "user_in_device_capabilities",
                  "snmp_version",
                  "snmp_community_string",
                  "snmp_port",
                  "snmp_auth_username",
                  "snmp_auth_password",
                  "snmp_auth_protocol",
                  "snmp_privacy_password",
                  "snmp_privacy_protocol",
                  "preferred_cli",
                  "cli_username",
                  "cli_password",
                  "secure_version",
                  "package_name",
                  "device_discovered_ind",
                  "delivery_method",
                  "unit_id",
                  "transaction_number",
                  "status",
                  "step_number",
                  "delivery_addl_email",
                  "manual_data_entry_ind",
                  "status_msg",
                  "virtual_network_id",
                  "network_name",
                  "contact_method",
                  "customer_name",
                  "contact_name",
                  "contact_value",
                  )
