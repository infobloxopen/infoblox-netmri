from infoblox_netmri.utils.utils import locate, to_snake, to_underscore_notation


class RemoteModel(object):
    properties = ()

    def __init__(self, obj_data, client):
        super(RemoteModel, self).__init__()
        self.broker = self._get_broker(client)
        for prop in self.properties:
            setattr(self, prop, obj_data.get(prop))
        for key in obj_data.keys():
            if key.startswith('custom_'):
                setattr(self, key, obj_data.get(key))

    def _get_method_fullname(self, method):
        return "{}/{}".format(self.broker.controller, method)

    def _get_broker(self, client):
        name = self.__class__.__name__.replace("Remote", "")
        return locate(self._get_broker_package(name, client))(client)

    def _get_broker_package(self, name, client):
        version = to_underscore_notation(client.api_version)
        return "infoblox_netmri.api.broker.{ver}.{pckg}_broker.{name}Broker".format(
            ver=version,
            pckg=to_snake(name),
            name=name
        )
