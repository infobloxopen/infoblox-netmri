from ..broker import Broker


class SecuritySettingsBroker(Broker):
    controller = "security_settings"

    def index(self, **kwargs):
        """Show the settings of HTTP, SSH, SNMP, and contents of HTTPS and IFMAP Client certificates

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("index"), kwargs)

    def update_http(self, **kwargs):
        """Update HTTP settings and restart the service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param http_enabled_ind: Availability of HTTP
             :type http_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param https_enabled_ind: Availability of HTTPS
             :type https_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param cipher_suites: Comma-separated list of cipher suites to use for HTTPS service
             :type cipher_suites: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_http"), kwargs)

    def update_ssh(self, **kwargs):
        """Update SSH settings and restart the service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh1_client_enabled_ind: Availability of SSH1 client
             :type ssh1_client_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh2_client_enabled_ind: Availability of SSH2 client
             :type ssh2_client_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh1_server_enabled_ind: Availability of SSH2 server
             :type ssh1_server_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh2_server_enabled_ind: Availability of SSH2 server
             :type ssh2_server_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh1_client_cipher: Cipher to be used for SSH1 client
             :type ssh1_client_cipher: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param ssh2_server_ciphers: Comma-separated list of cipher suites to use for SSH2 server
             :type ssh2_server_ciphers: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_ssh"), kwargs)

    def update_snmp(self, **kwargs):
        """Update SNMP settings and restart the service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_1_2_enabled_ind: Availability of SNMP Versions 1 and 2
             :type snmp_1_2_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param snmp_3_enabled_ind: Availability of SNMP Version 3
             :type snmp_3_enabled_ind: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param community: SNMP Versions 1 and 2 community string
             :type community: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param passphrase: SNMP Version 3 passphrase
             :type passphrase: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_snmp"), kwargs)

    def activate_certificate(self, **kwargs):
        """Activate HTTPS or IFMAP client certificate. HTTPS certificate activation restarts HTTPS service

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param certificate_file: Certificate file contents to be imported
             :type certificate_file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param certificate_type: Certificate type ifmap-client or https
             :type certificate_type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("activate_certificate"), kwargs)
