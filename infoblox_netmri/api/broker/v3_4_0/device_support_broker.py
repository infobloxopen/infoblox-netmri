from ..broker import Broker


class DeviceSupportBroker(Broker):
    controller = "device_support"

    def get_device_support_info(self, **kwargs):
        """This method retrieves all the device support information and the data collection status for a particular device.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param device_id: The internal NetMRI identifier of the device.
             :type device_id: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_data_collection_status: Array of hashes that contains a DataSource and EndTime.
             :rtype device_data_collection_status: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_support_info: Array of hashes that contains a Function, Supported, Available and Value.
             :rtype device_support_info: Array

            """

        return self.api_request(self._get_method_fullname("get_device_support_info"), kwargs)
