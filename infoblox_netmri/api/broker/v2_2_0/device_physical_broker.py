from ..broker import Broker


class DevicePhysicalBroker(Broker):
    controller = "device_physicals"

    def update(self, **kwargs):
        """Updates an existing device physical.

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` True
            |  ``default:`` None

             :param DevicePhysicalID: The internal NetMRI identifier for this physical component.
             :type DevicePhysicalID: Integer

            **Outputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return id: The id of the updated device physical.
             :rtype id: Integer

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return model: The class name of the updated device physical.
             :rtype model: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return uri: A URI that may be used to retrieve the updated device physical.
             :rtype uri: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :return device_physical: The updated device physical.
             :rtype device_physical: DevicePhysical

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)
