from ..broker import Broker


class SwitchPortMgmtBroker(Broker):
    controller = "switch_port_mgmt"

    def start_poll(self, **kwargs):
        """Start Switch Port Management polling

            **Inputs**

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` All

             :param type: Parameter to specify type of device list items: DeviceIDs/DeviceGroupsIDs/IPAddresses
             :type type: String

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` []

             :param list: Array of device IDs/device group IDs/IP addresses to be polled
             :type list: Array

            |  ``api version min:`` None
            |  ``api version max:`` None
            |  ``required:`` False
            |  ``default:`` None

             :param UnitID: ID of the collector to send the request to, OC only
             :type UnitID: Integer

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("start_poll"), kwargs)
