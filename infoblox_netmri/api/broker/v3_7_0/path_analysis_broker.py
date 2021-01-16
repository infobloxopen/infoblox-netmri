from ..broker import Broker


class PathAnalysisBroker(Broker):
    controller = "path_analysis"

    def create(self, **kwargs):
        """Initiates a path calculation.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param sources: The source address specifications.
             :type sources: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param destinations: The destination address specifications.
             :type destinations: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param virtual_network_id: The internal identifier for the network which the device is associated to.
             :type virtual_network_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device.
             :type DeviceID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return path_calculation_id: The identifier for this path calculation.
             :rtype path_calculation_id: String

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def continue_path(self, **kwargs):
        """Continues a path calculation.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_analysis_id: The identifier for the row from set of paths.
             :type path_analysis_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier for the device to continue the path from.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param virtual_network_id: The internal NetMRI identifier for the network view which device belongs to
             :type virtual_network_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return path_calculation_id: The identifier for this path calculation.
             :rtype path_calculation_id: String

            """

        return self.api_request(self._get_method_fullname("continue_path"), kwargs)

    def row_status(self, **kwargs):
        """The current status of a row from set of paths.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PathAnalysisID: The identifier for the row from set of paths.
             :type PathAnalysisID: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The current status of a row from set of paths (Running, Ready, Error).
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("row_status"), kwargs)

    def status(self, **kwargs):
        """The overall status of a path calculation.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The overall status of a path calculation (Running, Ready, Error).
             :rtype status: String

            """

        return self.api_request(self._get_method_fullname("status"), kwargs)

    def cancel(self, **kwargs):
        """Cancel calculation of paths.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("cancel"), kwargs)

    def compute_rule_list(self, **kwargs):
        """Compute rule list for any link on selected path.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_analysis_id: The identifier for the row from set of paths.
             :type path_analysis_id: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return rule_list: The list of rule-list associated with a record.
             :rtype rule_list: Array

            """

        return self.api_request(self._get_method_fullname("compute_rule_list"), kwargs)

    def compute_and_save_rule_list(self, **kwargs):
        """Compute rule list for any link on selected path and save it to the selected workbook.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_analysis_id: The identifier for the row from set of paths.
             :type path_analysis_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param workbook_id: The internal NetMRI identifier of the workbook.
             :type workbook_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("compute_and_save_rule_list"), kwargs)

    def compare_computed_rule_list(self, **kwargs):
        """Compare computed rule list for any link to the selected workbook.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_analysis_id: The identifier for the row from set of paths.
             :type path_analysis_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param workbook_id: The internal NetMRI identifier of the workbook.
             :type workbook_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("compare_computed_rule_list"), kwargs)

    def build_path_tree(self, **kwargs):
        """Build tree representation of computed path.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param path_calculation_id: The identifier for the path calculation.
             :type path_calculation_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param PathAnalysisID: The identifier for the row from set of paths.
             :type PathAnalysisID: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return path_tree: Computed path in the tree view
             :rtype path_tree: String

            """

        return self.api_request(self._get_method_fullname("build_path_tree"), kwargs)
