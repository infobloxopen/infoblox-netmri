from ..broker import Broker


class PerformanceDataBroker(Broker):
    controller = "performance_data"

    def get_data(self, **kwargs):
        """Returns performance data from category for period of time listed in params.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param starttime: Starting time of period for performance data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: Ending time of period for performance data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param category: Category of performance data.
             :type category: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit id of performance data owner.
             :type unit_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_data"), kwargs)

    def get_chart_data(self, **kwargs):
        """Returns data for specific performance dashboard chart for period of time listed in params.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param starttime: Starting time of period for performance data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: Ending time of period for performance data.
             :type endtime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit id of performance data owner.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param chart: Chart to get data for.
             :type chart: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param dynamic: Flag for dynamic performance data columns
             :type dynamic: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_chart_data"), kwargs)

    def get_last_data(self, **kwargs):
        """Returns last records of selected columns.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param metric_names: Array with columns you need data for.
             :type metric_names: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit id of performance data owner.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: Ending time  of period for performance data.
             :type endtime: DateTime

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_last_data"), kwargs)

    def get_metrics_data(self, **kwargs):
        """Returns performance data for selected metric.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param metric_names: Metric names you need data for.
             :type metric_names: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param unit_id: Unit id of performance data owner.
             :type unit_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param starttime: Starting time of period for performance data.
             :type starttime: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param endtime: Ending time of period for performance data.
             :type endtime: DateTime

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("get_metrics_data"), kwargs)
