#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_infoblox_netmri
----------------------------------

Tests for `infoblox_netmri` module.
"""

import json
import mock
import unittest

import infoblox_netmri


class TestInfoblox_netmri(unittest.TestCase):

    def setUp(self):
        self.netmri = infoblox_netmri.InfobloxNetMRI({
            'url': 'http://localhost/api/3',
            'username': 'admin',
            'password': 'admin'
        })
        self.session = mock.Mock()
        self.netmri.session = self.session

    def _mock_response(self, content):
        response = mock.Mock()
        response.raise_for_status.return_value = None
        response.content = json.dumps(content)
        return response

    def tearDown(self):
        pass

    def test_init_valid(self):
        self.assertEqual(type(self.netmri), infoblox_netmri.InfobloxNetMRI)

    def test_show(self):
        self.session.get.return_value = self._mock_response({'job': {}})
        self.netmri.show('job', 123)
        self.session.get.assert_called_with(
            'http://localhost/api/3/jobs/123',
            headers={'Content-type': 'application/json'}, verify=True)

    def test_show_with_string(self):
        self.session.get.return_value = self._mock_response({'job': {}})
        self.netmri.show('job', '232')
        self.session.get.assert_called_with(
            'http://localhost/api/3/jobs/232',
            headers={'Content-type': 'application/json'}, verify=True)

    def test_delete(self):
        self.session.delete.return_value = self._mock_response({'job': {}})
        self.netmri.delete('job', 123)
        self.session.delete.assert_called_with(
            'http://localhost/api/3/jobs/123',
            headers={'Content-type': 'application/json'}, verify=True)

    def test_delete_with_string(self):
        self.session.delete.return_value = self._mock_response({'job': {}})
        self.netmri.delete('job', '321')
        self.session.delete.assert_called_with(
            'http://localhost/api/3/jobs/321',
            headers={'Content-type': 'application/json'}, verify=True)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
