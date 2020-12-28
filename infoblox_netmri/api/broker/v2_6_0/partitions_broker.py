from ..broker import Broker


class PartitionsBroker(Broker):
    controller = "partitions"

    def generate(self, **kwargs):
        """Generates the required partition.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param table_name: Source table name. For partition SPMDevicesPresent_D_20121212 it's SPMDevicesPresent.
             :type table_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param start_time: Period start date. For partition SPMDevicesPresent_D_20121212 it's 2012-12-12.
             :type start_time: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param period: Period name. Acceptable are Daily (D in partition name), Weekly (W), Monthly (M), 7-Day (7), 30-Day (30). For partition SPMDevicesPresent_D_20121212 it's Daily (D).
             :type period: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("generate"), kwargs)
