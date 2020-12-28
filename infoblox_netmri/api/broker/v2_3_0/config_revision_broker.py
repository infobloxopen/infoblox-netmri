from ..broker import Broker


class ConfigRevisionBroker(Broker):
    controller = "config_revisions"

    def device(self, **kwargs):
        """The device from which this configuration revision was collected.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier for the configuration file revision.
             :type ConfigRevisionID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device: The device from which this configuration revision was collected.
             :rtype device: DeviceConfig

            """

        return self.api_request(self._get_method_fullname("device"), kwargs)
