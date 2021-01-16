from ..broker import Broker


class JobDetailBroker(Broker):
    controller = "job_details"

    def index(self, **kwargs):
        """Lists per-device job details. You can filter the results by Job ID, Job Name, or by Device ID.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The job id to list details for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param name: The name of the job to list details for.
             :type name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param deviceid: The Device ID to list details for.
             :type deviceid: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return as the first record.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The maximum number of records to return.
             :type limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Lists the per-device details for the associated job id.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to list details for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param start: The record number to return as the first record.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 1000

             :param limit: The maximum number of records to return.
             :type limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return job_details: An array of the JobDetail objects that match the specified input criteria.
             :rtype job_details: Array of JobDetail

            """

        return self.api_list_request(self._get_method_fullname("show"), kwargs)

    def device_files(self, **kwargs):
        """Lists/downloads the per-device files for a job. If no filename is given, a list of files for the job will be returned. If a filename is passed, and it exists, it will be downloaded as type "application/octet-stream". If the special filename "all.zip" is passed, a ZIP file containing all job files will be created and downloaded as type "application/zip"

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The job id to list files for.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param deviceid: The Device ID to list files for.
             :type deviceid: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param filename: An optional filename to download.
             :type filename: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param read: The number of bytes to read file from.
             :type read: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start: A position in the file to start transmission from. Available for log files only.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param retry_limit: Number of seconds before stopping retry efforts. Usually used when viewing a log for a new job.
             :type retry_limit: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return filenames: An array of filenames that match the specified input criteria.
             :rtype filenames: Array of String

            """

        return self.api_mixed_request(self._get_method_fullname("device_files"), kwargs)
