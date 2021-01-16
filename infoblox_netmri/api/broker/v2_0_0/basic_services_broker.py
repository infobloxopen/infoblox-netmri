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
