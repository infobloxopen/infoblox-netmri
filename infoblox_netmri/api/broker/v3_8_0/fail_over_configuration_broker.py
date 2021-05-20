from ..broker import Broker


class FailOverConfigurationBroker(Broker):
    controller = "fail_over_configurations"

    def get_config(self, **kwargs):
        """Get the failover configuration for the specified unit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. While not set in OC environment, the API request returns the failover configuration of all units.
             :type unit_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return failover_progress: The id of the failover action output file.
             :rtype failover_progress: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return fail_over_configuration: Text (json,xml or csv) interpretation of current failover configuration.
             :rtype fail_over_configuration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sync_ok: Success indicator of sync to neighbour operation.
             :rtype sync_ok: Boolean

            """

        return self.api_request(self._get_method_fullname("get_config"), kwargs)

    def action_status(self, **kwargs):
        """Shows failover action progress for specified unit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment. Default value is 0.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The id of the session output file.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: File offset to show
             :type read: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return read: Offset in bytes from the start of the file, to be used in the next get_progress call, in order to retrieve the next lines of the output.
             :rtype read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return output: Result of the failover action.
             :rtype output: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the remaining output data to dump: 0 - no data to dump, 1 - more data is available
             :rtype status: Integer

            """

        return self.api_request(self._get_method_fullname("action_status"), kwargs)

    def action(self, **kwargs):
        """Performs the failover action (enable or disable) for the specified unit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment. Default value is 0.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: Failover action name, possible values: 'enable', 'disable'
             :type name: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return failover_progress: The internal id of the failover action progress.
             :rtype failover_progress: String

            """

        return self.api_request(self._get_method_fullname("action"), kwargs)

    def failover(self, **kwargs):
        """Switches the specified unit to the secondary role.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment. Default value is 0.
             :type unit_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Text (json,xml or csv) interpretation of the operation result. Contains just unit_id and current status.
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("failover"), kwargs)

    def set_config(self, **kwargs):
        """Sets the failover configuration for the specified unit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment. Default value is 0.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param primary_index: Primary index. It indicates who is primary now (1-first, 2-second).
             :type primary_index: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_ip: Virtual IP address.
             :type virtual_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param virtual_hostname: Virtual hostname.
             :type virtual_hostname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param replication_direct_connect: Indicates if replication uses a direct connection through HA port. Default value is true.
             :type replication_direct_connect: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param replication_port: Replication port. Required for non direct connection replication.
             :type replication_port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_replication_ip: First replication IP. Required for non direct connection replication.
             :type first_replication_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_management_ip: First management IP. Required for secondary peer.
             :type first_management_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_management_hostname: First management hostname. Required for secondary peer.
             :type first_management_hostname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param first_replication_subnet: First replication subnet. Required for non direct connection replication.
             :type first_replication_subnet: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param second_replication_ip: Second replication IP. Required for non direct connection replication.
             :type second_replication_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param second_management_ip: Second management IP. Required for secondary peer.
             :type second_management_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param second_management_hostname: Second management hostname. Required for secondary peer.
             :type second_management_hostname: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param second_replication_subnet: Second replication subnet. Required for non direct connection replication.
             :type second_replication_subnet: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return fail_over_configuration: Text (json,xml or csv) interpretation of current failover configuration for the specified unit.
             :rtype fail_over_configuration: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return sync_ok: Success indicator of sync to neighbour operation.
             :rtype sync_ok: Boolean

            """

        return self.api_request(self._get_method_fullname("set_config"), kwargs)

    def status(self, **kwargs):
        """Get detailed failover replication and connection status for the specified unit.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment. Default value is 0.
             :type unit_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: JSON structure with the status information.
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("status"), kwargs)

    def reset_config_for_collector(self, **kwargs):
        """Drop failover collector on the collector to re-fetch it next time failover preferences are opened

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit ID. Should be specified in OC/Collector environment
             :type unit_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: Status of the operation
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("reset_config_for_collector"), kwargs)
