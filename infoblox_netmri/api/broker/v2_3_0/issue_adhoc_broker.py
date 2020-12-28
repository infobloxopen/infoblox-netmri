from ..broker import Broker


class IssueAdhocBroker(Broker):
    controller = "issue_adhocs"

    def generate_issue(self, **kwargs):
        """Generates an instance of a custom issue.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DeviceID: The ID of the Device associated with the issue to be generated.
             :type DeviceID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param IssueTypeID: ID of the custom issue to be generated.
             :type IssueTypeID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param Severity: Severity of the issue that will be generated (Error, Warning, Info)
             :type Severity: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param BatchID: The batch id associated with the issue.
             :type BatchID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return IssueID: The IssueID designated to the generated custom issue
             :rtype IssueID: String

            """

        return self.api_request(self._get_method_fullname("generate_issue"), kwargs)
