from ..broker import Broker


class SnmpMibBroker(Broker):
    controller = "snmp_mibs"

    def delete(self, **kwargs):
        """Delete a MIB specified by name

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: Unique MIB name
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the delete output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete"), kwargs)

    def import_data(self, **kwargs):
        """Import MIB in bulk via file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param file: MIB file contents to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The id of the output file
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read from the import output
             :type read: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def export(self, **kwargs):
        """Export MIB via file

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: MIB file name to be exported
             :type name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("export"), kwargs)
