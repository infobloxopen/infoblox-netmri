from ..broker import Broker


class CollectionScheduleBroker(Broker):
    controller = "collection_schedules"

    def index(self, **kwargs):
        """Lists the available collection schedules. Any of the inputs listed may be be used to narrow the list; other inputs will be ignored. Of the various ways to query lists, using this method is most efficient.

            **Inputs**

            |  ``api version min:`` 2.2
            |  ``api version max:`` 2.4
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_id: The internal NetMRI identifier for device group.
             :type device_group_id: Integer

            |  ``api version min:`` 2.5
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_id: The internal NetMRI identifier for device group.
             :type device_group_id: Array of Integer

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

             :param sort: The data field(s) to use for sorting the output. Default is id. Valid values are id, device_group_id, device_id, schedule, schedule_type.
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

             :param select: The list of attributes to return for each CollectionSchedule. Valid values are id, device_group_id, device_id, schedule, schedule_type. If empty or omitted, all attributes will be returned.
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

             :return collection_schedules: An array of the CollectionSchedule objects that match the specified input criteria.
             :rtype collection_schedules: Array of CollectionSchedule

            """

        return self.api_list_request(self._get_method_fullname("index"), kwargs)

    def destroy(self, **kwargs):
        """Deletes the specified collection schedule from NetMRI.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: The internal NetMRI identifier for schedule.
             :type id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def update(self, **kwargs):
        """Updates a device group specific polling schedule.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param id: Id of the polling schedule to update.
             :type id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_cron: Either the cron entry (cron schedule string), or a number that denotes the frequency (in minutes) polling should run.
             :type schedule_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_json: NetMRI internal parameters generated by 'cronscheduler' form transmitted in json format for setting cron schedule string.
             :type schedule_json: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def create(self, **kwargs):
        """Creates device group specific polling schedule.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_group_id: Device group Id polling schedule belongs to.
             :type device_group_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param device_id: Device Id polling schedule belongs to.
             :type device_id: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_cron: Either the cron entry (cron schedule string), or a number that denotes the frequency (in minutes) polling should run.
             :type schedule_cron: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param schedule_json: NetMRI internal parameters generated by 'cronscheduler' form transmitted in json format for setting cron schedule string.
             :type schedule_json: String

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def spm_schedules(self, **kwargs):
        """Lists the Switch Port Management polling schedule entries for a device group.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_group_id: Device group ID for the requested polling schedules.
             :type device_group_id: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("spm_schedules"), kwargs)
