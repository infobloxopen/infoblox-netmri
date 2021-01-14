from ..broker import Broker


class CollectorDataSyncBroker(Broker):
    controller = "collector_data_sync"

    def get_data_from_oc(self, **kwargs):
        """Gets collector sync data as a tarball from OC. This call must be made from a collector.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param unit_id: The collector (probe) id
             :type unit_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_data_from_oc"), kwargs)

    def send_data_to_collector(self, **kwargs):
        """Sends collector sync data in a tarball from OC to Collector. This call must be made from OC.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param unit_id: The collector (probe) id
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param unit_ip: The collector (probe) IP Address
             :type unit_ip: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port: The http port to connect collector. Augusta uses port 82 and NetMRI uses default port, 80.
             :type port: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return archive_file: The file path that sync data has been packaged to
             :rtype archive_file: String

            """

        return self.api_request(self._get_method_fullname("send_data_to_collector"), kwargs)

    def import_data(self, **kwargs):
        """Imports the downloaded collector sync data into database. This call must be made from a collector.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import_data"), kwargs)
