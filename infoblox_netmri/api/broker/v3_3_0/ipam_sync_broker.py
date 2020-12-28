from ..broker import Broker


class IpamSyncBroker(Broker):
    controller = "ipam_sync"

    def status(self, **kwargs):
        """Gets the highest SeqNo available currently of a given IPAM object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param type: The ipam object type to indicate either "network" or "ip".
             :type type: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return seq_no: The highest sequence number of a given IPAM object
             :rtype seq_no: Integer

            """

        return self.api_request(self._get_method_fullname("status"), kwargs)

    def send_refresh(self, **kwargs):
        """Sends refresh message to ipam sync queue consumed by ipam_syncd.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param type: The ipam object type to indicate either "network" or "ip".
             :type type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param since_seq_no: sequence number to start from to send ipam objects
             :type since_seq_no: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("send_refresh"), kwargs)

    def send_ip_objects_by_range(self, **kwargs):
        """Sends refresh message to ipam ip sync queue consumed by ipam_ip_syncd.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param network_view_id: network view id
             :type network_view_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ip_start: start of ip address range
             :type ip_start: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ip_end: end of ip address range
             :type ip_end: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("send_ip_objects_by_range"), kwargs)
