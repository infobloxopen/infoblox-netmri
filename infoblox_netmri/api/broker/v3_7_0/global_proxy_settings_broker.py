from ..broker import Broker


class GlobalProxySettingsBroker(Broker):
    controller = "global_proxy_settings"

    def index(self, **kwargs):
        """Returns Global Proxy Settings.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("index"), kwargs)

    def decoded_index(self, **kwargs):
        """Returns Global Proxy Settings with password decoded.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("decoded_index"), kwargs)

    def collector_proxy(self, **kwargs):
        """Returns Collector Proxy Settings,

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param UnitID: ID of the collector to send the request to, OC only.
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("collector_proxy"), kwargs)

    def update_collector(self, **kwargs):
        """Updates proxy settings on collector.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param UnitID: ID of the collector to send the request to, OC only.
             :type UnitID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: Username.
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: Password.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_port: Proxy port to set for Global Proxy Settings.
             :type proxy_port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_address: Proxy address to set for Global Proxy Settings.
             :type proxy_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param use_global_proxy: Flag which identifies usage of global proxy settings.
             :type use_global_proxy: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_collector"), kwargs)

    def update(self, **kwargs):
        """Updates Global Proxy Settings.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: Username.
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: Password.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_port: Proxy port to set for Global Proxy Settings.
             :type proxy_port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param proxy_address: Proxy address to set for Global Proxy Settings.
             :type proxy_address: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param use_global_proxy: Flag which identifies usage of global proxy settings.
             :type use_global_proxy: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: ID of the collector to send the request to, OC only.
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)
