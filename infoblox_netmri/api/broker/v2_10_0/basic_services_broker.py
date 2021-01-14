from ..broker import Broker


class BasicServicesBroker(Broker):
    controller = "basic_services"

    def authenticate(self, **kwargs):
        """Authenticates the user with NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param username: The username of the user as whom to login.
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param password: The password of the user as whom to login.
             :type password: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` %Y-%m-%d %H:%M:%S

             :param datetime_format: The format to use for date/time input and output.
             :type datetime_format: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param timezone: Date/time input and output will be performed in the specified timezone. Should be specified as HH:MM offset from GMT. For example, -05:00 specified US Eastern Time, whereas +09:00 specifies Tokyo time. Alternatively, a timezone name may be used. See the API Data Structures page for details. If omitted, the server's configured timezone will be used.
             :type timezone: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("authenticate"), kwargs)

    def base_uri(self, **kwargs):
        """Returns the base URI for the specified version.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param version: The API version for which the base_uri is needed.
             :type version: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("base_uri"), kwargs)

    def license_info(self, **kwargs):
        """Returns license information for this NetMRI server.

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return serial_number: NetMRI serial number.
             :rtype serial_number: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return license_id: NetMRI License identifier.
             :rtype license_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return license_expiration: NetMRI License expiration.
             :rtype license_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return license_type: NetMRI License type
             :rtype license_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return mode: NetMRI operation mode. One of 'standalone', 'master' or 'collector'.
             :rtype mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return maintenance_expiration: Maintenance expiration for appliance.
             :rtype maintenance_expiration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_limit: Licensed limit of devices.
             :rtype device_limit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return interface_limit: Licensed limit of interfaces.
             :rtype interface_limit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return spm_limit: Licensed limit of number of ports controlled by SPM.
             :rtype spm_limit: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return modules_short_name: Short symbolic names of licensed features.
             :rtype modules_short_name: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return modules_support: Support statuses for corresponding modules in modules_short_names.
             :rtype modules_support: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return modules_expiration: Expiration times for corresponding modules in modules_short_names.
             :rtype modules_expiration: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return modules_name: Long names for corresponding modules in modules_short_names.
             :rtype modules_name: Array of String

            """

        return self.api_request(self._get_method_fullname("license_info"), kwargs)

    def server_info(self, **kwargs):
        """Returns basic information regarding this NetMRI server.

            **Inputs**

            |  ``api version min:`` 2.6
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param api_versions_only_ind: Only include API version information in the output.
             :type api_versions_only_ind: Boolean

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return netmri_version: The NetMRI version number running on this appliance or virtual machine.
             :rtype netmri_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return latest_api_version: The most recent API version supported by this NetMRI.
             :rtype latest_api_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return requested_api_version: The API version that executed this call.
             :rtype requested_api_version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return host_name: The configured host name of the NetMRI appliance.
             :rtype host_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return operating_mode: Indicates if the NetMRI is running in standalone, collector, or operations center mode.
             :rtype operating_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return mgmt_ip: The IPv4 management address of this NetMRI, if configured.
             :rtype mgmt_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return mgmt_ip6: The IPv6 management address of this NetMRI, if configured.
             :rtype mgmt_ip6: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return scan_ip: The IPv4 SCAN (analysis) address of this NetMRI, if configured.
             :rtype scan_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return scan_ip6: The IPv6 SCAN (analysis) address of this NetMRI, if configured.
             :rtype scan_ip6: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return operational_status: The status of NetMRI. Usually ready, can also be upgrading. Values might change in the future.
             :rtype operational_status: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return supported_api_versions: All API versions supported by this NetMRI.
             :rtype supported_api_versions: Array of String

            """

        return self.api_request(self._get_method_fullname("server_info"), kwargs)

    def server_time(self, **kwargs):
        """Returns the current system time of this NetMRI server.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("server_time"), kwargs)

    def restart(self, **kwargs):
        """Restarts the application.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("restart"), kwargs)

    def consolidate(self, **kwargs):
        """Runs consolidation

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param managers: Comma-separated list of consolidator managers. Must be one of Aggregate, Config, Event, Group, Issue, Job, Normal, Policy, Routing, Settings, Stats, Subnet, Switching, Time, Topology, Voip, Vulnerability, Wireless
             :type managers: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param collector: Collector name. In case when this method called on OC this parameter is required
             :type collector: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("consolidate"), kwargs)

    def settings_generate(self, **kwargs):
        """Generates xml with current configuration data

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param version: The version of xml to be generated
             :type version: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return xml: A string containing the full xml as collected from the running config.
             :rtype xml: String

            """

        return self.api_request(self._get_method_fullname("settings_generate"), kwargs)

    def settings_current(self, **kwargs):
        """Reports the status of an xml configuration file

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return xml: A string containing the full xml as collected from the running config.
             :rtype xml: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return messages: An array of hashes that contain details about the validation process
             :rtype messages: Array of Hash

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: A string representation of the status of the request. Will be one of; success, error, pending
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("settings_current"), kwargs)

    def settings_apply(self, **kwargs):
        """Parses the xml provided by config_id, then applies the changes. You should not need to call this directly!

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param config_id: The configuration id reported when the xml was uploaded to the unit
             :type config_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param mods: Modifications for applying
             :type mods: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return xml: A string containing the full xml as collected from the running config.
             :rtype xml: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return messages: An array of hashes that contain details about the validation process
             :rtype messages: Array of Hash

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: A string representation of the status of the request. Will be one of; success, error, pending
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("settings_apply"), kwargs)

    def settings_status(self, **kwargs):
        """Reports the status of an xml configuration file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param config_id: The configuration id reported when the xml was uploaded to the unit
             :type config_id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return messages: An array of hashes that contain details about the validation process
             :rtype messages: Array of Hash

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: A string representation of the status of the validation. Will be one of; success, error, pending
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("settings_status"), kwargs)

    def settings_info(self, **kwargs):
        """Shows probe info, running_config, candidate_config, and list of installed dsb

            **Inputs**

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return grid_members: Hash of grid members info including master and slaves (probes)
             :rtype grid_members: String

            """

        return self.api_request(self._get_method_fullname("settings_info"), kwargs)

    def set_session_value(self, **kwargs):
        """save data in a cache that is session wise

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key: key associated with that value - will be used to retrieve the same value
             :type key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param value: value to save in the session cache
             :type value: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("set_session_value"), kwargs)

    def get_session_value(self, **kwargs):
        """retrieve data in the session cache that formerly saved

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key: key associated with that value - will be used to retrieve the same value
             :type key: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param default_value: Default value in case key/value does not exist in session. If key does not exist and default value is nil the response is 400 with record not found message
             :type default_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return value: value associated with that key
             :rtype value: String

            """

        return self.api_request(self._get_method_fullname("get_session_value"), kwargs)

    def set_time_zone(self, **kwargs):
        """Sets a Time Zone for the system.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param time_zone: A valid Time Zone in "Area/Location" format.
             :type time_zone: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("set_time_zone"), kwargs)
