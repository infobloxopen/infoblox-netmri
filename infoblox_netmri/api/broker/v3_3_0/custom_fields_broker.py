from ..broker import Broker


class CustomFieldsBroker(Broker):
    controller = "custom_fields"

    def list(self, **kwargs):
        """Returns list of custom fields defined for requested model or list of custom fields defined for model object if id parameter is passed.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: Id of the object to get custom fields for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param fields: Array of attributes to use while searching.
             :type fields: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: Search pattern.
             :type query: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param allow_blank: Flag which defines whether to return blank custom fields for model object or not.
             :type allow_blank: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param limit: Limit the number of records returned.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start: Record to begin return with.
             :type start: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("list"), kwargs)

    def list_undefined(self, **kwargs):
        """Returns list of undefined custom field for specified object.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Object id.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("list_undefined"), kwargs)

    def import_data(self, **kwargs):
        """Allows importing custom field data using CSV format.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file_name: The contents of the CSV file with the custom field data to be imported.
             :type file_name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def create_field(self, **kwargs):
        """Allows creating new custom field for specified model.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Name of new custom field.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param type: Type of new custom field (integer, datetime, date, string).
             :type type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create_field"), kwargs)

    def update_field(self, **kwargs):
        """Allows updating properties of custom field assosiated with specified model (changing name, type).

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Old custom field name.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param new_name: New name for custom field.
             :type new_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param type: Old or new custom field type (integer, datetime, date, string).
             :type type: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_field"), kwargs)

    def delete_field(self, **kwargs):
        """Allows deleting custom field assosiated with specified model.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param model: Name of the model to work with. Valid values are Device, Interface, JobSpecification, DetectedChange, DevicePhysical, IssueDesc.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Name of custom field to delete.
             :type name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete_field"), kwargs)
