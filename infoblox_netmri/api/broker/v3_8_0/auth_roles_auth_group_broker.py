from ..broker import Broker


class AuthRolesAuthGroupBroker(Broker):
    controller = "auth_roles_auth_groups"

    def show(self, **kwargs):
        """Shows the details for the specified auth roles auth group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this record.
             :type id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles_auth_group: The auth roles auth group identified by the specified id.
             :rtype auth_roles_auth_group: AuthRolesAuthGroup

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def index(self, **kwargs):
        """Lists the available auth roles auth groups. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this record.
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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthRolesAuthGroup. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

             :return auth_roles_auth_groups: An array of the AuthRolesAuthGroup objects that match the specified input criteria.
             :rtype auth_roles_auth_groups: Array of AuthRolesAuthGroup

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """Lists the available auth roles auth groups matching the input criteria. This method provides a more flexible search interface than the index method, but searching using this method is more demanding on the system and will not perform to the same level as the index method. The input fields listed below will be used as in the index method, to filter the result, along with the optional query string and XML filter described below.

            **Inputs**

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier for device group definition.
             :type DeviceGroupID: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_group_id: The internal NetMRI identifier for group definition.
             :type auth_group_id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_role_id: The internal NetMRI identifier for role definition.
             :type auth_role_id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param created_at: The date and time the record was initially created in NetMRI.
             :type created_at: Array of DateTime

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this record.
             :type id: Array of Integer

            |  ``api version min:`` 3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param updated_at: The date and time the record was last modified in NetMRI.
             :type updated_at: Array of DateTime

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthRolesAuthGroup. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param query: This value will be matched against auth roles auth groups, looking to see if one or more of the listed attributes contain the passed value. You may also surround the value with '/' and '/' to perform a regular expression search rather than a containment operation. Any record that matches will be returned. The attributes searched are: DeviceGroupID, auth_group_id, auth_role_id, created_at, id, updated_at.
             :type query: String

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles_auth_groups: An array of the AuthRolesAuthGroup objects that match the specified input criteria.
             :rtype auth_roles_auth_groups: Array of AuthRolesAuthGroup

            """

        return self.api_list_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """Lists the available auth roles auth groups matching the input specification. This provides the most flexible search specification of all the query mechanisms, enabling searching using comparison operations other than equality. However, it is more complex to use and will not perform as efficiently as the index or search methods. In the input descriptions below, 'field names' refers to the following fields: DeviceGroupID, auth_group_id, auth_role_id, created_at, id, updated_at.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_DeviceGroupID: The operator to apply to the field DeviceGroupID. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. DeviceGroupID: The internal NetMRI identifier for device group definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_DeviceGroupID: If op_DeviceGroupID is specified, the field named in this input will be compared to the value in DeviceGroupID using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_DeviceGroupID must be specified if op_DeviceGroupID is specified.
             :type val_f_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_DeviceGroupID: If op_DeviceGroupID is specified, this value will be compared to the value in DeviceGroupID using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_DeviceGroupID must be specified if op_DeviceGroupID is specified.
             :type val_c_DeviceGroupID: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_group_id: The operator to apply to the field auth_group_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_group_id: The internal NetMRI identifier for group definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_group_id: If op_auth_group_id is specified, the field named in this input will be compared to the value in auth_group_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_group_id must be specified if op_auth_group_id is specified.
             :type val_f_auth_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_group_id: If op_auth_group_id is specified, this value will be compared to the value in auth_group_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_group_id must be specified if op_auth_group_id is specified.
             :type val_c_auth_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_auth_role_id: The operator to apply to the field auth_role_id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. auth_role_id: The internal NetMRI identifier for role definition. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_auth_role_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_auth_role_id: If op_auth_role_id is specified, the field named in this input will be compared to the value in auth_role_id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_auth_role_id must be specified if op_auth_role_id is specified.
             :type val_f_auth_role_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_auth_role_id: If op_auth_role_id is specified, this value will be compared to the value in auth_role_id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_auth_role_id must be specified if op_auth_role_id is specified.
             :type val_c_auth_role_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_created_at: The operator to apply to the field created_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. created_at: The date and time the record was initially created in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_created_at: If op_created_at is specified, the field named in this input will be compared to the value in created_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_created_at must be specified if op_created_at is specified.
             :type val_f_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_created_at: If op_created_at is specified, this value will be compared to the value in created_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_created_at must be specified if op_created_at is specified.
             :type val_c_created_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_id: The operator to apply to the field id. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. id: The internal NetMRI identifier for this record. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_id: If op_id is specified, the field named in this input will be compared to the value in id using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_id must be specified if op_id is specified.
             :type val_f_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_id: If op_id is specified, this value will be compared to the value in id using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_id must be specified if op_id is specified.
             :type val_c_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param op_updated_at: The operator to apply to the field updated_at. Valid values are: =, <>, rlike, not rlike, >, >=, <, <=, like, not like, is null, is not null, between. updated_at: The date and time the record was last modified in NetMRI. For the between operator the value will be treated as an Array if comma delimited string is passed, and it must contain an even number of values.
             :type op_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_f_updated_at: If op_updated_at is specified, the field named in this input will be compared to the value in updated_at using the specified operator. That is, the value in this input will be treated as another field name, rather than a constant value. Either this field or val_c_updated_at must be specified if op_updated_at is specified.
             :type val_f_updated_at: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param val_c_updated_at: If op_updated_at is specified, this value will be compared to the value in updated_at using the specified operator. The value in this input will be treated as an explicit constant value. Either this field or val_f_updated_at must be specified if op_updated_at is specified.
             :type val_c_updated_at: String

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at.
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

             :param select: The list of attributes to return for each AuthRolesAuthGroup. Valid values are id, auth_role_id, auth_group_id, DeviceGroupID, created_at, updated_at. If empty or omitted, all attributes will be returned.
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

            |  ``api version min:`` 2.3
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param xml_filter: A SetFilter XML structure to further refine the search. The SetFilter will be applied AFTER any search query or field values, but before any limit options. The limit and pagination will be enforced after the filter. Remind that this kind of filter may be costly and inefficient if not associated with a database filtering.
             :type xml_filter: String

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles_auth_groups: An array of the AuthRolesAuthGroup objects that match the specified input criteria.
             :rtype auth_roles_auth_groups: Array of AuthRolesAuthGroup

            """

        return self.api_list_request(self._get_method_fullname("find"), kwargs)

    def create(self, **kwargs):
        """Creates a new auth roles auth group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier for device group definition.
             :type DeviceGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_group_id: The internal NetMRI identifier for group definition.
             :type auth_group_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_role_id: The internal NetMRI identifier for role definition.
             :type auth_role_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the newly created auth roles auth group.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the newly created auth roles auth group.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the newly created auth roles auth group.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles_auth_group: The newly created auth roles auth group.
             :rtype auth_roles_auth_group: AuthRolesAuthGroup

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """Updates an existing auth roles auth group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this record.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param DeviceGroupID: The internal NetMRI identifier for device group definition. If omitted, this field will not be updated.
             :type DeviceGroupID: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_group_id: The internal NetMRI identifier for group definition. If omitted, this field will not be updated.
             :type auth_group_id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param auth_role_id: The internal NetMRI identifier for role definition. If omitted, this field will not be updated.
             :type auth_role_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated auth roles auth group.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated auth roles auth group.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated auth roles auth group.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return auth_roles_auth_group: The updated auth roles auth group.
             :rtype auth_roles_auth_group: AuthRolesAuthGroup

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified auth roles auth group from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for this record.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def grid_update_rdg(self, **kwargs):
        """GRID:Update remote group roles.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param encodedChanges: The internal NetMRI identifier for the encodedChanges.<br> Syntax format: encodedChanges=&lt;group_id&gt;|&lt;auth_role_name&gt;|&lt;device_groups_ids separated by comma&gt;
             :type encodedChanges: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("grid_update_rdg"), kwargs)
