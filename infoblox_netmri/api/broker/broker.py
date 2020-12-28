from infoblox_netmri.utils.utils import locate, to_snake
from infoblox_netmri.api.exceptions.netmri_exceptions import NotImplementedException


class Broker(object):
    """ Base class for broker instances, provides methods for API requests.
        And return responces wrapped with specific class

        :param client: InfobloxNetMRI client
    """

    controller = None

    def __init__(self, client):
        self.client = client

    def api_request(self, method_name, params):
        """ Make api request and return single wrapped object

            :param method_name: name of API methods
            :param params: dict-wrapped params for specific API call
        """
        data = self.client.api_request(method_name, params)

        if isinstance(data, dict) and len(data) > 1:
            for x in data.keys():
                data[x] = self._get_return_object_type(data.get(x))
            return data

        class_name = to_snake(self.__class__.__name__.replace("Broker", ""))

        if class_name in data:
            result_name = class_name
        else:
            result_name = method_name.split('/')[-1]
            if result_name not in data:
                return data

        return self._get_return_object_type(data.get(result_name))

    # See NETMRI-31545
    def api_mixed_request(self, method_name, params):
        """ Make api request and download a file and return
            JSON response or request status dictionary

            :param method_name: name of API methods
            :param params: dict-wrapped params for specific API call
        """
        data = self.client.api_request(method_name, params, downloadable=True)

        class_name = to_snake(self.__class__.__name__.replace("Broker", ""))

        if class_name in data:
            result_name = class_name
        else:
            result_name = method_name.split('/')[-1]
            if result_name not in data:
                return data

        return self._get_return_object_type(data.get(result_name))

    def api_list_request(self, method_name, params):
        """ Make api request and return list of wrapped objects

            :param method_name: name of API methods
            :param params: dict-wrapped params for specific API call
        """
        data = self.client.api_request(method_name, params)

        if not data:
            return None
        try:
            return [self._get_return_object_type(x) for x in data[self.controller]]
        except KeyError:
            print("Sorry, this method will be implemented in the\
                  future versions of NetMRI")
            raise NotImplementedException(self.controller, method_name)

    def _get_method_fullname(self, method):
        """ Returns full API method name using controller name

            **Input**
            :param method: method name
            :return: full API path
        """
        return "{}/{}".format(self.controller, method)

    def _get_return_object_type(self, data):
        """ Returns wrapped response which inherits from RemoteModel class

            :param data: API responce data
            :return: RemoteModel child class
        """
        if not data or not isinstance(data, dict):
            return data

        class_name = data.get("_class")
        obj_class = locate(self._get_remote_class_name(class_name))

        return obj_class(data, self.client)

    def _get_remote_class_name(self, name):
        """ Generate full path to specific RemoteModel instance

            :param name: name of model
            :return: full path for model
        """
        return "infoblox_netmri.api.remote.models.{pckg}_remote.{name}Remote".format(
            pckg=to_snake(name),
            name=name
        )
