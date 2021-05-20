from ..broker import Broker


class ApicSettingBroker(Broker):
    controller = "apic_settings"

    def index(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("index"), kwargs)

    def search(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("search"), kwargs)

    def find(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("find"), kwargs)

    def show(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("show"), kwargs)

    def create(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("create"), kwargs)

    def update(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("update"), kwargs)

    def destroy(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy"), kwargs)

    def destroy_many(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("destroy_many"), kwargs)

    def dump_apic_controllers(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("dump_apic_controllers"), kwargs)

    def import_controllers(self, **kwargs):
        """This method is no longer exists. Please use such method from SDN Settings

            **Inputs**

            **Outputs**

            """

        return self.api_request(self._get_method_fullname("import_controllers"), kwargs)
