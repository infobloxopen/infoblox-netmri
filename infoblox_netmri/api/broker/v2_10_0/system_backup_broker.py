from ..broker import Broker


class SystemBackupBroker(Broker):
    controller = "system_backup"

    def create_archive(self, **kwargs):
        """Creates backup of current system database.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include_date: Defines whether include date in file name or not.
             :type include_date: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param init: Defines whether to initially create the archive.
             :type init: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param async_ind: When false, backup creating will be run synchronously, and the API call will block until it is complete. When true, backup creating id will be returned to use for subsequent calls
             :type async_ind: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create_archive"), kwargs)

    def create_archive_status(self, **kwargs):
        """Backup database status.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create_archive_status"), kwargs)

    def ssh_authentication_test(self, **kwargs):
        """Test SSH authentication.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param host: Host name or IP address of the system where archive will be copied.
             :type host: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port: Number of open SSH port on the system where archive will be delivered. Default value is 22 (used if no port number specified).
             :type port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param user_name: Name of the existing user on the system where archive will be copied.
             :type user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param password: User password on the system where archive will be copied.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param use_ssh_keys: Specifies whether to use SSH keys.
             :type use_ssh_keys: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param directory: Remote host directory where archive will be stored.
             :type directory: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("ssh_authentication_test"), kwargs)

    def move_archive_to_remote_host(self, **kwargs):
        """Moves database archive to remote host via SSH. Note that archive will be removed from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param host: Host name or IP address of the system where archive will be copied. Required if init is set to true.
             :type host: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port: Number of open SSH port on the system where archive will be delivered. Default value is 22 (used if no port number specified).
             :type port: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_name: Name of the existing user on the system where archive will be copied. Required if init is set to true.
             :type user_name: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param password: User password on the system where archive will be copied. Required if init is set to true.
             :type password: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param use_ssh_keys: Specifies whether to use SSH keys.
             :type use_ssh_keys: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param directory: Specifies directory where archive will be stored on remote host. Default is user home directory.
             :type directory: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param init: Set to true to initialize moving archive
             :type init: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("move_archive_to_remote_host"), kwargs)

    def download_archive(self, **kwargs):
        """Download database archive.

            **Inputs**

            **Outputs**

            """

        return self.api_mixed_request(self._get_method_fullname("download_archive"), kwargs)

    def download_archive_md5_sum(self, **kwargs):
        """Download database archive md5 checksum.

            **Inputs**

            **Outputs**

            """

        return self.api_mixed_request(self._get_method_fullname("download_archive_md5_sum"), kwargs)

    def remove_archive(self, **kwargs):
        """Database archive is stored in temporary directory on NetMRI. It's removed on schedule but you may choose to force remove it.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("remove_archive"), kwargs)

    def schedule_archiving(self, **kwargs):
        """Schedule NetMRI database archiving. Archive will be stored on up to 2 systems supporting SCP.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param enable: Specifies whether scheduled archiving should be enabled or not. If parameter is not specified then scheduled archiving is set disabled.
             :type enable: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param host_1: Host name or IP address of the system where archive will be copied.
             :type host_1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port_1: Number of open SSH port on the system where archive will be delivered. Default value is 22 (used if no port number specified).
             :type port_1: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_name_1: Name of the existing user on the system where archive will be copied.
             :type user_name_1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param password_1: User password on the system where archive will be copied.
             :type password_1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param use_ssh_keys_1: Specifies whether to use SSH keys.
             :type use_ssh_keys_1: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param directory_1: Specifies directory where archive will be stored on remote host. Default is user home directory.
             :type directory_1: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param host_2: Host name or IP address of the system where archive will be copied.
             :type host_2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param port_2: Number of open SSH port on the system where archive will be delivered. Default value is 22 (used if no port number specified).
             :type port_2: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param user_name_2: Name of the existing user on the system where archive will be copied.
             :type user_name_2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param password_2: User password on the system where archive will be copied.
             :type password_2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param use_ssh_keys_2: Specifies whether to use SSH keys.
             :type use_ssh_keys_2: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param directory_2: Specifies directory where archive will be stored on remote host. Default is user home directory.
             :type directory_2: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include_date_1: Specifies whether to put current date into archive file name or not while saving on remote host 1.
             :type include_date_1: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param include_date_2: Specifies whether to put current date into archive file name or not while saving on remote host 2.
             :type include_date_2: Boolean

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_cron: Cron schedule string.
             :type schedule_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_json: NetMRI internal parameters generated by 'cronscheduler' form transmitted in json format for setting cron schedule string.
             :type schedule_json: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` False

             :param force_save: If true, changes will be saved even if credentials test failed
             :type force_save: Boolean

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("schedule_archiving"), kwargs)

    def upload_archive(self, **kwargs):
        """Upload database archive to NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param archive: NetMRI database archive file.
             :type archive: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param md5: NetMRI database archive MD5 checksum file.
             :type md5: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("upload_archive"), kwargs)

    def restore_database(self, **kwargs):
        """Restores database from the archive which should have been uploaded to NetMRI.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("restore_database"), kwargs)
