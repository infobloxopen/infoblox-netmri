#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_infoblox_netmri
----------------------------------

Tests for `infoblox_netmri` module.
"""

import unittest
import json
from requests import Session

from httmock import with_httmock, urlmatch
from mock import patch

from infoblox_netmri.client import InfobloxNetMRI
from infoblox_netmri.easy import NetMRIEasy


class MockResponse:

    def __init__(self, status_code=200, content=b"{}", data=None, is_headers=False):
        self.status_code = status_code
        self.content = content
        self.headers = self._json_headers() if is_headers else self._empty_headers()
        self.data = {} if data is None else data

    @staticmethod
    def _empty_headers():
        return {'content-type': []}

    @staticmethod
    def _json_headers():
        return {'content-type': ['application/json']}

    def json(self):
        return json.dumps(self.data)

    def iter_content(self):
        if self.data:
            temp = []
            for symbol in json.dumps(self.data):
                temp.append(symbol.encode())
            return temp
        return []


@urlmatch(path=r"^/api/authenticate$")
def authenticate_response(_url, _request):
    return {'status_code': 200, 'content': b"{}", 'headers': {'content-type': []}}


@urlmatch(path=r"^/api/3.1/dis_sessions/open")
def open_dis_session(_url, _request):
    return {'status_code': 200,
            'headers': {'content-type': json.dumps(['application/json'])},
            'content': b'{"dis_session": {"JobID": 4, "SessionID": "149088011782626-7348", "RemoteUsername": "admin", '
                       b'"RemoteIPAddress": "1.2.3.4", "Timestamp": "1855-01-30 06:21:57", "UnitIDList": [0], '
                       b'"_class": "DisSession"}}'}


@urlmatch(path=r'/api/3.1/dis_sessions/close')
def close_session(_url, _request):
    return {'status_code': 200, 'content': b'{}', 'headers': {'content-type': []}}


@urlmatch(path=r"^/api/3.1/cli_connections/open")
def open_cli_session(_url, _request):
    return {'status_code': 200, 'content': b"{}", 'headers': {'content-type': []}}


@urlmatch(path=r"^/api/3.1/jobs/[0-9]+$")
def job_response(_url, _request):
    return {'status_code': 200, 'content': b'{"job": {}}', 'headers': {'content-type': []}}


@urlmatch(path=r"^/api/3.1/devices/index$")
def devices_list_response(_url, _request):
    return {'status_code': 200, 'content': b'{}', 'headers': {'content-type': []}}


device = {'DeviceType': 'unknown', 'InfraDeviceInd': False,
          'MgmtServerDeviceID': 0, 'DeviceStartTime': '2016-11-16 04:10:12',
          'DeviceMAC': '', 'DeviceAssurance': 0,
          'DeviceTimestamp': '2016-11-16 04:10:12', 'DeviceModel': None, 'DeviceSysDescr': None,
          'DeviceSysContact': None, 'DeviceID': 1, 'DeviceName': 'unknown',
          'DataSourceID': 0, 'NetworkDeviceInd': False, 'DeviceEndTime': None,
          'VirtualNetworkID': 1, 'DeviceIPDotted': '60.1.200.180', 'VirtualInd': False,
          'DeviceVersion': None, 'DeviceVendor': None, 'DeviceIPNumeric': 1006749876, 'DeviceOUI': None,
          'DeviceDNSName': None, 'DeviceChangedCols': None, 'DeviceSysName': None,
          'DeviceFirstOccurrenceTime': '2016-11-16 04:10:12', 'DeviceNetBIOSName': None,
          'DeviceSysLocation': None, 'DeviceUniqueKey': None, 'ParentDeviceID': 0, '_class':
              'Device', 'DeviceAddlInfo': None}


def devices_list(*_, **__):
    global device
    device2 = device.copy()
    device2.update({'DeviceID': 2})
    devices = [device, device2]

    return {'devices': devices}


def single_device(*_, **__):
    global device
    return {'device': device}


def send_command_result(*_, **__):
    return {'command_response': "OK"}


class TestInfobloxNetmri(unittest.TestCase):
    opts = {"host": "localhost",
            "username": "admin",
            "password": "admin",
            "api_version": "3.1"}

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
    @patch('infoblox_netmri.client.isfile')
    def test_init_ssl_verify_file(self, mock_isfile):
        mock_isfile.return_value = True
        netmri = InfobloxNetMRI(ssl_verify='/some/path.crt', **self.opts)
        self.assertEqual('/some/path.crt', netmri.ssl_verify)

        mock_isfile.return_value = False
        self.assertRaises(ValueError, InfobloxNetMRI, ssl_verify='/some/path.crt', **self.opts)

    @with_httmock(authenticate_response, job_response)
    def test_show(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            netmri.show('job', 123)
            mock_request.assert_called_with("get",
                                            'https://localhost/api/3.1/jobs/123',
                                            headers={'Content-type': 'application/json'},
                                            data=None,
                                            stream=True)

    @with_httmock(authenticate_response, job_response)
    def test_show_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            netmri.show('job', '232')
            mock_request.assert_called_with("get",
                                            'https://localhost/api/3.1/jobs/232',
                                            headers={'Content-type': 'application/json'},
                                            data=None,
                                            stream=True)

    @with_httmock(authenticate_response, job_response)
    def test_delete(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            netmri.delete('job', 123)
            mock_request.assert_called_with("delete",
                                            'https://localhost/api/3.1/jobs/123',
                                            headers={'Content-type': 'application/json'},
                                            data=None,
                                            stream=True)

    @with_httmock(authenticate_response, job_response)
    def test_delete_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            netmri.delete('job', '321')
            mock_request.assert_called_with("delete",
                                            'https://localhost/api/3.1/jobs/321',
                                            headers={'Content-type': 'application/json'},
                                            data=None,
                                            stream=True)

    @with_httmock(authenticate_response)
    def test_get_device_broker(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        self.assertEqual(broker.__class__.__name__, 'DeviceBroker', "Device broker import error")

        broker = netmri.get_broker('AccessChange')
        self.assertEqual(broker.__class__.__name__, 'AccessChangeBroker', "AccessChangeBroker broker import error")

    @with_httmock(authenticate_response, devices_list_response)
    def test_get_devices_list(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            broker.index()
            mock_request.assert_called_with("post",
                                            'https://localhost/api/3.1/devices/index',
                                            headers={'Content-type': 'application/json'},
                                            data='{}',
                                            stream=True)

    @with_httmock(authenticate_response, devices_list_response)
    def test_get_device(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(Session, 'request', return_value=MockResponse()) as mock_request:
            broker.show(DeviceID=2)
            mock_request.assert_called_with("post",
                                            'https://localhost/api/3.1/devices/show',
                                            headers={'Content-type': 'application/json'},
                                            data='{"DeviceID": 2}',
                                            stream=True)

    @with_httmock(authenticate_response)
    def test_package_creation(self):
        netmri = InfobloxNetMRI(**self.opts)
        package = "infoblox_netmri.api.broker.v3_1_0.device_broker.DeviceBroker"
        self.assertEqual(package, netmri._get_broker_package("Device"))

    @with_httmock(authenticate_response)
    def test_check_return_values(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri.session, 'request', return_value=MockResponse(data=devices_list(), is_headers=True)):
            res = broker.index()
            self.assertEqual(res[0].DeviceID, 1, "Wrong id device 1")
            self.assertEqual(res[1].DeviceID, 2, "Wrong id device 2")

    @with_httmock(authenticate_response)
    def test_check_single_device(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri.session, 'request', return_value=MockResponse(data=single_device(), is_headers=True)):
            res = broker.show(DeviceID=1)
            self.assertEqual(res.DeviceID, 1, "Wrong id")

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy(self):
        init_data = {'device_id': 1, 'job_id': 1, 'batch_id': 1}
        init_data.update(
            {'api_url': 'https://localhost',
             'http_username': 'admin',
             'http_password': 'admin',
             'api_version': '3.1'}
        )
        with NetMRIEasy(**init_data) as easy:
            self.assertEqual(easy.device_id, 1)
            self.assertEqual(easy.job_id, 1)
            self.assertEqual(easy.batch_id, 1)
            self.assertIsNotNone(easy.dis_session)
            self.assertIsNotNone(easy.cli_connection)

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy_send_command(self):
        init_data = {'device_id': 1, 'job_id': 1, 'batch_id': 1}
        init_data.update(
            {'api_url': 'http://localhost',
             'http_username': 'admin',
             'http_password': 'admin',
             'api_version': '3.1'}
        )
        with NetMRIEasy(**init_data) as easy:
            with patch.object(easy.client.session, 'request',
                              return_value=MockResponse(data=send_command_result(), is_headers=True)):
                res = easy.send_command("show info")
                self.assertEqual(res, "OK")

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy_empty_params(self):
        # empty constructor test
        self.assertRaises(RuntimeError, NetMRIEasy)


if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
