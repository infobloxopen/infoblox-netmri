from ..broker import Broker


class ConfigListBroker(Broker):
    controller = "config_lists"

    def index(self, **kwargs):
        """Lists the available config lists. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.1
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of this configuration list.
             :type id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier of this configuration list.
             :type id: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_user_id, name, description, created_at, updated_at.
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

             :param select: The list of attributes to return for each ConfigList. Valid values are id, auth_user_id, name, description, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return config_lists: An array of the ConfigList objects that match the specified input criteria.
             :rtype config_lists: Array of ConfigList

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def show(self, **kwargs):
        """Shows the details for the specified config list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of this configuration list.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return config_list: The config list identified by the specified id.
             :rtype config_list: ConfigList

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def destroy(self, **kwargs):
        """This method will delete selected list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier of this configuration list.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def tree(self, **kwargs):
        """Generates a tree representation of lists. Tailored to ExtJS tree requirements.

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("tree"), kwargs)

    def rows(self, **kwargs):
        """This method will return all rows which are assigned to specific list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the list
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param start: The record number to return in the selected page of data. It will always appear, although it may not be the first record. See the :limit for more information.
             :type start: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param limit: The size of the page of data, that is, the maximum number of records returned. The limit size will be used to break the data up into pages and the first page with the start record will be returned (default value is 25). So if you have 100 records and use a :limit of 10 and a :start of 10, you will get records 10-19.
             :type limit: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("rows"), kwargs)

    def create(self, **kwargs):
        """This method will create a config list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description: Description of the list
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Name of the list
             :type name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """This method will update selected list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param id: The internal NetMRI identifier for the list
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param description: Description of the list
             :type description: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param name: Name of the list
             :type name: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def update_rows(self, **kwargs):
        """This method will update all rows which are assigned to selected list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param list_id: The internal NetMRI identifier for the list
             :type list_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param grid_id: The grid id string in grid config for the list grid
             :type grid_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param grid: JSON string which contains rows of the list
             :type grid: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update_rows"), kwargs)

    def delete_rows(self, **kwargs):
        """This method will delete all rows which are assigned to selected list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param list_id: The internal NetMRI identifier for the list
             :type list_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param grid: JSON string which contains rows of the list
             :type grid: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("delete_rows"), kwargs)

    def export(self, **kwargs):
        """This method will return xml data for selected list.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for the list
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("export"), kwargs)

    def import_data(self, **kwargs):
        """This method will create or replace a list with input from a CSV file.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param file: The contents of the CSV file with the list data to be imported
             :type file: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` 0

             :param overwrite_ind: An indicator to overwrite an existing list file with the same name. Overwrite if set to 1. Do not overwrite if set to 0
             :type overwrite_ind: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import"), kwargs)

    def find_column(self, **kwargs):
        """For the given list this method will find the first occurrence (row) of the value key_value in the column key_column.
                 If found, for the row, return the value in the column value_column. If not found, return default.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param list: Name or Short Name of the List
             :type list: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key_column: Key column for the search
             :type key_column: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param key_value: Value which will be seached in the column
             :type key_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:``

             :param default_value: Value which will be returned if nothing will found
             :type default_value: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param value_column: Value of column which should be returned
             :type value_column: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("find_column"), kwargs)
