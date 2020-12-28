from ..broker import Broker


class DisSessionBroker(Broker):
    controller = "dis_sessions"

    def open(self, **kwargs):
        """Opens a DIS session.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_id: The NetMRI internal identifier for the job.
             :type job_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return dis_session: The DIS Session object.
             :rtype dis_session: DisSession

            """

        return self.api_request(self._get_method_fullname("open"), kwargs)

    def close(self, **kwargs):
        """Closes an open DIS session and all underlying connections.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return command_response: The response to closing the session.
             :rtype command_response: String

            """

        return self.api_request(self._get_method_fullname("close"), kwargs)

    def open_connection(self, **kwargs):
        """Opens a CLI connection with the device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The DIS session id.
             :type id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The NetMRI internal identifier for the device.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return cli_connection: The CLI connection with the device.
             :rtype cli_connection: CliConnection

            """

        return self.api_request(self._get_method_fullname("open_connection"), kwargs)
