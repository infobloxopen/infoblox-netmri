from ..broker import Broker


class PartitionCalendarBroker(Broker):
    controller = "partition_calendar"

    def get_minimal_date(self, **kwargs):
        """Returns minimal calendar date.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_minimal_date"), kwargs)
