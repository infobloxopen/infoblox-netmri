from ..broker import Broker


class ScriptBroker(Broker):
    controller = "scripts"

    def index(self, **kwargs):
        """Lists the available scripts. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Array of Integer

            |  ``api version min:`` 2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: String

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of this script.
             :type name: Array of String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind.
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

             :param select: The list of attributes to return for each Script. Valid values are id, name, module, visible, description, created_by, updated_by, language, risk_level, created_at, updated_at, category, read_only, taskflow_create, taskflow_edit, taskflow_revert, target_mapping, transactional_ind. If empty or omitted, all attributes will be returned.
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

             :return scripts: An array of the Script objects that match the specified input criteria.
             :rtype scripts: Array of Script

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified script.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the script.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return script: The script identified by the specified id.
             :rtype script: Script

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """Create a CCS/Perl/Python script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param script_file: The script file contents.
             :type script_file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` True

             :param overwrite: Overwrite any existing version of the script with the same name.
             :type overwrite: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` CCS

             :param language: The language the script is written in (CCS, Perl, Python).
             :type language: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Update a CCS/Perl/Python script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to update.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param script_file: The script file contents.
             :type script_file: String

            |  ``api version min:`` 2.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` CCS

             :param language: The language the script is written in (CCS, Perl, Python).
             :type language: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1

             :param overwrite: Overwrite any existing version of the script with the same name.
             :type overwrite: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Delete a CCS script on NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to delete.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def run(self, **kwargs):
        """Run a script immediately with specified input. In addition to the listed parameters, optional parameters can be passed. Any parameter name starting with \$ will be passed as Script-Variable to the script.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.1
            |  ``required:`` True
            |  ``default:`` None

             :param id: The ID of the script to run.
             :type id: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The ID of the script to run. Required unless name is specified.
             :type id: Integer

            |  ``api version min:`` 2.1.1
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the script to run. Required unless ID is specified.
             :type name: String

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param wait: Maximum number of seconds to wait for script completion before returning the job result. Using a value of 0 will cause the call to schedule the job and return immediately. Requires that the target is one single device.
             :type wait: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_ids: An array of device group ids. Can be blank if not using device groups.
             :type device_group_ids: Array of Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_ids: An array of device ids. Can be blank if ONLY using device groups.
             :type device_ids: Array of Integer

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

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param job_name: Optional name for this run of a job.
             :type job_name: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return JobID: The JobID of the running script.
             :rtype JobID: Integer

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return status: The status of the job, if the call input wait parameter had a non zero value. Status Pending or Running indicates the call timed out and the job is still in processing.
             :rtype status: String

            |  ``api version min:`` 2.4
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return payload: The JSON payload of the script output, if any. Only set if Status is set and its value is OK.
             :rtype payload: String

            """

        return self.api_request(self._get_method_fullname("run"), kwargs)
