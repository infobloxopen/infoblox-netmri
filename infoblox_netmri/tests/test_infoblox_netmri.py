#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_infoblox_netmri
----------------------------------

Tests for `infoblox_netmri` module.
"""

from mock import patch
from httmock import with_httmock, urlmatch
import unittest

from infoblox_netmri import InfobloxNetMRI


@urlmatch(path=r"^/api/authenticate$")
def authenticate_response(url, request):
    return {'status_code': 200, 'content': b"{}"}


@urlmatch(path=r"^/api/3/jobs/[0-9]+$")
def job_response(url, request):
    return {'status_code': 200, 'content': b'{"job": {}}'}


class TestInfobloxNetmri(unittest.TestCase):
    opts = {"host": "localhost",
            "username": "admin",
            "password": "admin",
            "api_version": "3"}

    def tearDown(self):
        pass

    @with_httmock(authenticate_response)
    def test_init_valid(self):
        netmri = InfobloxNetMRI(**self.opts)
        self.assertEqual(type(netmri), InfobloxNetMRI)

    @with_httmock(authenticate_response)
    def test_init_missing(self):
        self.assertRaises(TypeError, InfobloxNetMRI,
                          host="localhost",
                          user="admin")

        self.assertRaises(TypeError, InfobloxNetMRI,
                          host="localhost",
                          password="admin")

        self.assertRaises(TypeError, InfobloxNetMRI,
                          user="admin",
                          password="admin")

    @with_httmock(authenticate_response)
    def test_init_ssl_verify_bool(self):
        netmri = InfobloxNetMRI(**self.opts)
        self.assertEqual(False, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify="no", **self.opts)
        self.assertEqual(False, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify="off", **self.opts)
        self.assertEqual(False, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify=False, **self.opts)
        self.assertEqual(False, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify="false", **self.opts)
        self.assertEqual(False, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify="true", **self.opts)
        self.assertEqual(True, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify='yes', **self.opts)
        self.assertEqual(True, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify='on', **self.opts)
        self.assertEqual(True, netmri.ssl_verify)

        netmri = InfobloxNetMRI(ssl_verify=True, **self.opts)
        self.assertEqual(True, netmri.ssl_verify)

    @with_httmock(authenticate_response)
    @patch('infoblox_netmri.isfile')
    def test_init_ssl_verify_file(self, mock_isfile):
        mock_isfile.return_value = True
        netmri = InfobloxNetMRI(ssl_verify='/some/path.crt', **self.opts)
        self.assertEqual('/some/path.crt', netmri.ssl_verify)

        mock_isfile.return_value = False
        self.assertRaises(ValueError, InfobloxNetMRI, ssl_verify='/some/path.crt', **self.opts)

    @with_httmock(authenticate_response, job_response)
    def test_show(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.show('job', 123)
            mock_request.request.assert_called_with("get",
                                                    'https://localhost/api/3/jobs/123',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_show_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.show('job', '232')
            mock_request.request.assert_called_with("get",
                                                    'https://localhost/api/3/jobs/232',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_delete(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.delete('job', 123)
            mock_request.request.assert_called_with("delete",
                                                    'https://localhost/api/3/jobs/123',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_delete_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.delete('job', '321')
            mock_request.request.assert_called_with("delete",
                                                    'https://localhost/api/3/jobs/321',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
