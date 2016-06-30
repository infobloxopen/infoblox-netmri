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
import re
from os.path import isfile

import requests
from requests.exceptions import HTTPError


class InfobloxNetMRI(object):
    def __init__(self, host, username, password, api_version="auto",
                 use_ssl=True, ssl_verify=False, http_pool_connections=5,
                 http_pool_maxsize=10, max_retries=5):

        # Process ssl parameters
        if use_ssl:
            self.protocol = "https"
            if isinstance(ssl_verify, bool):
                self.ssl_verify = ssl_verify
            else:
                opt = str(ssl_verify).lower()
                if opt in ['yes', 'on', 'true']:
                    self.ssl_verify = True
                elif opt in ['no', 'off', 'false']:
                    self.ssl_verify = False
                elif isfile(ssl_verify):
                    self.ssl_verify = ssl_verify
                else:
                    raise ValueError("ssl_verify is not a valid boolean value,"
                                     "nor a valid path to a CA bundle file")
        else:
            self.protocol = "http"
            self.ssl_verify = False

        # Process host
        if re.match(r"^[\w.-]+$", host):
            self.host = host
        else:
            raise ValueError("Hostname is not a valid hostname")

        # Authentication parameters
        self.username = username
        self.password = password
        self._is_authenticated = False

        # HTTP session settings
        self.session = requests.Session()
        adapter = requests.adapters.HTTPAdapter(
            max_retries=max_retries,
            pool_connections=http_pool_connections,
            pool_maxsize=http_pool_maxsize)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
        self.session.verify = self.ssl_verify

        # API version
        if re.match('^[0-9.]$', api_version):
            self.api_version = api_version
        elif api_version.lower() == "auto":
            self.api_version = self._get_api_version()
        else:
            raise ValueError("Incorrect API version")

    def _make_request(self, url, method="get", data=None, extra_headers=None):
        """Prepares the request, checks for authentication and retries in case of issues

        Args:
            url (str): URL of the request
            method (str): Any of "get", "post", "delete"
            data (any): Possible extra data to send with the request
            extra_headers (dict): Possible extra headers to send along in the request
        Returns:
            dict
        """
        attempts = 0

        while attempts < 1:
            # Authenticate first if not authenticated already
            if not self._is_authenticated:
                self._authenticate()
            # Make the request and check for authentication errors
            # This allows us to catch session timeouts for long standing connections
            try:
                return self._send_request(url, method, data, extra_headers)
            except HTTPError as e:
                if e.response.status_code == 403:
                    self._is_authenticated = False
                    attempts += 1
                else:
                    # re-raise other HTTP errors
                    raise

    def _send_request(self, url, method="get", data=None, extra_headers=None):
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
        """Fetches the most recent API version

        Returns:
            str
        """
        url = "{base_url}/api/server_info".format(base_url=self._base_url())
        server_info = self._make_request(url=url, method="get")
        return server_info["latest_api_version"]

    def _authenticate(self):
        """ Perform an authentication against NetMRI"""
        url = "{base_url}/api/authenticate".format(base_url=self._base_url())
        data = json.dumps({'username': self.username, "password": self.password})
        # Bypass authentication check in make_request by using _send_request
        self._send_request(url, method="post", data=data)
        self._is_authenticated = True

    def _controller_name(self, objtype):
        """Determines the controller name for the object's type

        Args:
            objtype (str): The object type

        Returns:
            A string with the controller name
        """
        # would be better to use inflect.pluralize here, but would add a dependency
        if objtype.endswith('y'):
            return objtype[:-1] + 'ies'

        if objtype[-1] in 'sx' or objtype[-2:] in ['sh', 'ch']:
            return objtype + 'es'

        if objtype.endswith('an'):
            return objtype[:-2] + 'en'

        return objtype + 's'

    def _base_url(self):
        """Generate the base URL for the connection with NetMRI

        Returns:
            A string containing the base URL
        """
        return "{proto}://{host}".format(
            proto=self.protocol,
            host=self.host
        )

    def _object_url(self, objtype, objid):
        """Generate the URL for the specified object

        Args:
            objtype (str): The object's type
            objid (int): The objects ID

        Returns:
            A string containing the URL of the object
        """
        return "{base_url}/api/{api_version}/{controller}/{obj_id}".format(
            base_url=self._base_url(),
            api_version=self.api_version,
            controller=self._controller_name(objtype),
            obj_id=objid
        )

    def _method_url(self, method_name):
        """Generate the URL for the requested method

        Args:
            method_name (str): Name of the method

        Returns:
            A string containing the URL of the method
        """
        return "{base_url}/api/{api}/{method}".format(
            base_url=self._base_url(),
            api=self.api_version,
            method=method_name
        )

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
