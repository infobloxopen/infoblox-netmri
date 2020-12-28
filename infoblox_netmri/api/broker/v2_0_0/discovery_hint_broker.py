from ..broker import Broker


class DiscoveryHintBroker(Broker):
    controller = "discovery_hints"

    def index(self, **kwargs):
        """Lists the available discovery hints. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each DiscoveryHint. Valid values are id, hint, device_type, UnitID, created_by, updated_by, created_at, updated_at, cli_user_name_secure_ssh, cli_user_password_secure_ssh, snmp_protocol, snmp_community_secure, snmp_auth_protocol, snmp_auth_password_secure, snmp_private_protocol, snmp_private_password_secure, secure_version, cli_user_name_secure_telnet, cli_user_password_secure_telnet, cli_enable_password_secure. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hints: An array of the DiscoveryHint objects that match the specified input criteria.
             :rtype discovery_hints: Array of DiscoveryHint

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The discovery hint identified by the specified id.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Creates a new discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param hint: The hint used the by discovery engine.
             :type hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_type: The device type applied to the given discovery hint.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint.
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created discovery hint.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created discovery hint.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created discovery hint.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The newly created discovery hint.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing discovery hint.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param hint: The hint used the by discovery engine. If omitted, this field will not be updated.
             :type hint: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_type: The device type applied to the given discovery hint. If omitted, this field will not be updated.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param UnitID: The internal NetMRI identifier collector assigned to the discovery hint. If omitted, this field will be updated to the default value.
             :type UnitID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated discovery hint.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated discovery hint.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated discovery hint.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return discovery_hint: The updated discovery hint.
             :rtype discovery_hint: DiscoveryHint

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified discovery hint from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the discovery hint.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)
