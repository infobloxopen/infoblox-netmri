#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_infoblox_netmri
----------------------------------

Tests for `infoblox_netmri` module.
"""

import unittest

import infoblox_netmri


class TestInfoblox_netmri(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init_valid(self):
        c = infoblox_netmri.InfobloxNetMRI({
            'url': 'http://localhost/api/3',
            'username': 'admin',
            'password': 'admin'
        })
        self.assertEqual(type(c), infoblox_netmri.InfobloxNetMRI)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
