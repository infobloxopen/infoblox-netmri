from ..broker import Broker


class ConfigTemplateBroker(Broker):
    controller = "config_templates"

    def index(self, **kwargs):
        """Lists the available config templates. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template.
             :type id: Array of Integer

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the config template.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the config template.
             :type name: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param methods: A list of config template methods. The listed methods will be called on each config template returned and included in the output. Available methods are: template_text.
             :type methods: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned. So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19. The maximum limit is 10000.
             :type limit: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` id

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, vendor, model, version, device_type, description, created_by, updated_by, created_at, updated_at, template_type, risk_level.
             :type sort: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` asc

             :param dir: The direction(s) in which to sort the data. Default is 'asc'. Valid values are 'asc' and 'desc'.
             :type dir: Array of String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param select: The list of attributes to return for each ConfigTemplate. Valid values are id, name, vendor, model, version, device_type, description, created_by, updated_by, created_at, updated_at, template_type, risk_level. If empty or omitted, all attributes will be returned.
             :type select: Array

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_field: The field name for NIOS GOTO that is used for locating a row position of records.
             :type goto_field: String

            |  ``api version min:`` 2.8
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param goto_value: The value of goto_field for NIOS GOTO that is used for locating a row position of records.
             :type goto_value: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_templates: An array of the ConfigTemplate objects that match the specified input criteria.
             :rtype config_templates: Array of ConfigTemplate

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """This method will return the specified configuration template

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template to show
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified config template from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def create(self, **kwargs):
        """Creates a new config template.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the config template was created.
             :type created_at: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_by: The user that created the config template.
             :type created_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: A description for the config template.
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_type: The device type associated with the config template.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param model: The device model name associated with the config template.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The name of the config template.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param risk_level: The user-specified risk level for the template. Possible levels are 1 (low), 2 (medium), and 3 (high).  To run higher risk templates, higher privileges are required.
             :type risk_level: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param template_type: The template type denotes whether devices or interfaces should be specified when the template job is scheduled or run. The value could be either 'Device' or 'Interface'.
             :type template_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the config template was updated.
             :type updated_at: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: The user that last updated the config template.
             :type updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param vendor: The device vendor name associated with the config template.
             :type vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param version: The device OS version associated with the config template.
             :type version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param overwrite_ind: If set to 1, overwrite existing template file. If set to 0, do not overwrite existing template file
             :type overwrite_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param template_text: Template text.
             :type template_text: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created config template.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created config template.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created config template.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_template: The newly created config template.
             :rtype config_template: ConfigTemplate

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing config template.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param description: A description for the config template. If omitted, this field will not be updated.
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_type: The device type associated with the config template. If omitted, this field will not be updated.
             :type device_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param model: The device model name associated with the config template. If omitted, this field will not be updated.
             :type model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The name of the config template.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param risk_level: The user-specified risk level for the template. Possible levels are 1 (low), 2 (medium), and 3 (high).  To run higher risk templates, higher privileges are required. If omitted, this field will not be updated.
             :type risk_level: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param template_type: The template type denotes whether devices or interfaces should be specified when the template job is scheduled or run. The value could be either 'Device' or 'Interface'.
             :type template_type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the config template was updated. If omitted, this field will not be updated.
             :type updated_at: DateTime

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_by: The user that last updated the config template. If omitted, this field will not be updated.
             :type updated_by: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param vendor: The device vendor name associated with the config template. If omitted, this field will not be updated.
             :type vendor: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param version: The device OS version associated with the config template. If omitted, this field will not be updated.
             :type version: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param overwrite_ind: An indicator to overwrite an existing template file with the same name. Overwrite if set to 1. Do not overwrite if set to 0
             :type overwrite_ind: Boolean

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param template_text: Template text.
             :type template_text: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated config template.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated config template.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated config template.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_template: The updated config template.
             :rtype config_template: ConfigTemplate

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def duplicate(self, **kwargs):
        """This method will make a copy of the specified configuration template

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template from which to make a copy
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: The name to be assigned to the new configuration template
             :type name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("duplicate"), kwargs)

    def populate_template(self, **kwargs):
        """This method populates a new configuration template with information from the selected configuration revision of a device

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param ConfigRevisionID: The internal NetMRI identifier of the specific configuration revision
             :type ConfigRevisionID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceID: The internal NetMRI identifier of the specific device
             :type DeviceID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("populate_template"), kwargs)

    def export(self, **kwargs):
        """This method exports a configuration template

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of the configuration template
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("export"), kwargs)

    def import_data(self, **kwargs):
        """This method imports a configuration template

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param template_file: The configuration template file contents
             :type template_file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param overwrite_ind: An indicator to overwrite an existing template file with the same name. Overwrite if set to 1. Do not overwrite if set to 0
             :type overwrite_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def run(self, **kwargs):
        """Run a config template immediately with specified input.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the template to run.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: A comma delimited string of device group ids. Can be blank if not using device groups.
             :type device_group_ids: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: A comma delimited string of device ids. Can be blank if ONLY using device groups.
             :type device_ids: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param template_variables: Optional variables to be passed to the template. Any variable name starting with $ will be passed through as input to the template.
             :type template_variables: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` requestor

             :param credential_mode: If user credentials are required, they may be set from additional inputs (credential_mode = 'manual'). The credentials may be looked up using requestor stored credentials (credential_mode = 'requestor').
             :type credential_mode: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param username: Username to be used if the job requires user credentials.
             :type username: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param password: Password to be used if the job requires user credentials.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enable_password: Enable password to be used if the job requires user credentials.
             :type enable_password: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return JobID: The JobID of the running template.
             :rtype JobID: Integer

            """

        return self.api_request(self._get_method_fullname("run"), kwargs)

    def variables(self, **kwargs):
        """List the variables for the specified config template (tailored for input forms)

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ConfigTemplateID of the config template from which to obtain variables
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("variables"), kwargs)
