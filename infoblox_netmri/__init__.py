# Copyright 2015 Infoblox Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import json
import requests
import re
from os.path import isfile

__author__ = 'John Belamaric'
__email__ = 'jbelamaric@infoblox.com'
__version__ = '0.1.2'


class InfobloxNetMRI(object):
    def __init__(self, host, username, password, api_version="auto",
                 use_ssl=True, ssl_verify=True, http_pool_connections=5,
                 http_pool_maxsize=10, max_retries=5):

        if isinstance(ssl_verify, bool):
            self.ssl_verify = ssl_verify
        else:
            opt = str(ssl_verify).lower()
            if opt in ['yes', 'on', 'true']:
                self.ssl_verify = True
            elif opt in ['no', 'off', 'false']:
                self.ssl_verify = False
            else:
                if isfile(ssl_verify):
                    self.ssl_verify = ssl_verify
                else:
                    raise ValueError("ssl_verify is not a valid boolean value,"
                                     "nor a valid path to a CA bundle file")

        if re.match(r"^[\w.-]+$", host):
            self.host = host
        else:
            raise ValueError("Hostname is not a valid hostname")

        self.username = username
        self.password = password

        if use_ssl:
            self.protocol = "https"
        else:
            self.protocol = "http"

        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            max_retries=max_retries,
            pool_connections=http_pool_connections,
            pool_maxsize=http_pool_maxsize)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.session.verify = self.ssl_verify

        # We must authenticate before determining the latest API version
        self._authenticate()

        if re.match('^[0-9.]$', api_version):
            self.api_version = api_version
        elif api_version.lower() == "auto":
            self.api_version = self._get_api_version()
        else:
            raise ValueError("Incorrect API version")

    def _make_request(self, url, method="get", data=None, extra_headers=None):
        """Performs a given request and returns a json object

        Args:
            url (str): URL of the request
            method (str): Any of "get", "post", "delete"
            data (any): Possible extra data to send with the request
            extra_headers (dict): Possible extra headers to send along in the request
        Returns:
            dict
        """
        headers = {'Content-type': 'application/json'}
        if isinstance(extra_headers, dict):
            headers.update(extra_headers)

        r = self.session.request(method, url, headers=headers, data=data)
        r.raise_for_status()
        return r.json()

    def _get_api_version(self):
        url = self._server_info_url()
        server_info = self._make_request(url=url, method="get")
        return server_info["latest_api_version"]

    def _authenticate(self):
        url = self._authenticate_url()
        data = json.dumps({'username': self.username, "password": self.password})
        self._make_request(url, method="post", data=data)
        return True

    def _controller_name(self, objtype):
        # would be better to use inflect.pluralize here, but would add
        # a dependency
        if objtype.endswith('y'):
            return objtype[:-1] + 'ies'

        if objtype[-1] in 'sx' or objtype[-2:] in ['sh', 'ch']:
            return objtype + 'es'

        if objtype.endswith('an'):
            return objtype[:-2] + 'en'

        return objtype + 's'

    def _base_url(self):
        return "{proto}://{host}".format(proto=self.protocol,
                                         host=self.host)

    def _controller_url(self, objtype):
        return "{base_url}/api/{api_version}/{controller}".format(base_url=self._base_url(),
                                                                  api_version=self.api_version,
                                                                  controller=self._controller_name(objtype))

    def _object_url(self, objtype, objid):
        return "{}/{}".format(self._controller_url(objtype), objid)

    def _method_url(self, method_name):
        return "{base_url}/api/{api}/{method}".format(base_url=self._base_url(),
                                                      api=self.api_version,
                                                      method=method_name)

    def _authenticate_url(self):
        return "{base_url}/api/authenticate".format(base_url=self._base_url())

    def _server_info_url(self):
        return "{base_url}/api/server_info".format(base_url=self._base_url())

    def api_request(self, method_name, params):
        """Execute an arbitrary method.

        Args:
            method_name (str): include the controller name: 'devices/search'
            params (dict): the method parameters
        Returns:
            A dict with the response
        Raises:
            requests.exceptions.HTTPError
        """
        url = self._method_url(method_name)
        data = json.dumps(params)
        return self._make_request(url=url, method="post", data=data)

    def show(self, objtype, objid):
        """Query for a specific resource by ID

        Args:
            objtype (str): object type, e.g. 'device', 'interface'
            objid (int): object ID (DeviceID, etc.)
        Returns:
            A dict with that object
        Raises:
            requests.exceptions.HTTPError
        """
        url = self._object_url(objtype, int(objid))
        return self._make_request(url, method="get")

    def delete(self, objtype, objid):
        """Destroy a specific resource by ID

        Args:
            objtype  (str): object type, e.g. 'script'
            objid (int): object ID
        Returns:
            A dict with the response
        Raises:
            requests.exceptions.HTTPError
        """
        url = self._object_url(objtype, int(objid))
        return self._make_request(url, method="delete")
