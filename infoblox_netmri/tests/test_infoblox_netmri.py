#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_infoblox_netmri
----------------------------------

Tests for `infoblox_netmri` module.
"""

import unittest

from httmock import with_httmock, urlmatch
from mock import patch

from infoblox_netmri.client import InfobloxNetMRI
from infoblox_netmri.easy import NetMRIEasy


@urlmatch(path=r"^/api/authenticate$")
def authenticate_response(url, request):
    return {'status_code': 200, 'content': b"{}"}


@urlmatch(path=r"^/api/3/dis_sessions/open")
def open_dis_session(url, request):
    return {'status_code': 200,
            'content': b'{"dis_session": {"JobID": 4, "SessionID": "149088011782626-7348", "RemoteUsername": "admin", '
                       b'"RemoteIPAddress": "1.2.3.4", "Timestamp": "1855-01-30 06:21:57", "UnitIDList": [0], '
                       b'"_class": "DisSession"}}'}


@urlmatch(path=r'/api/3/dis_sessions/close')
def close_session(url, request):
    return {'status_code': 200, 'content': b'{}'}


@urlmatch(path=r"^/api/3/cli_connections/open")
def open_cli_session(url, request):
    return {'status_code': 200, 'content': b"{}"}


@urlmatch(path=r"^/api/3.1/jobs/[0-9]+$")
def job_response(url, request):
    return {'status_code': 200, 'content': b'{"job": {}}'}


@urlmatch(path=r"^/api/3/devices/index$")
def devices_list_response(url, request):
    return {'status_code': 200, 'content': b'{}'}


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


class MockResult(object):
    data = None

    def __init__(self, key, data):
        self.data = {key: data}

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


def devices_list(*args, **kwargs):
    global device
    device2 = device.copy()
    device2.update({'DeviceID': 2})
    devices = [device, device2]

    return MockResult('devices', devices)


def single_device(*args, **kwargs):
    global device
    return MockResult('device', device)


def send_command_result(*args, **kwargs):
    return MockResult('command_response', "OK")


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
        with patch.object(netmri, 'session') as mock_request:
            netmri.show('job', 123)
            mock_request.request.assert_called_with("get",
                                                    'https://localhost/api/3.1/jobs/123',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_show_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.show('job', '232')
            mock_request.request.assert_called_with("get",
                                                    'https://localhost/api/3.1/jobs/232',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_delete(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.delete('job', 123)
            mock_request.request.assert_called_with("delete",
                                                    'https://localhost/api/3.1/jobs/123',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response, job_response)
    def test_delete_with_string(self):
        netmri = InfobloxNetMRI(**self.opts)
        with patch.object(netmri, 'session') as mock_request:
            netmri.delete('job', '321')
            mock_request.request.assert_called_with("delete",
                                                    'https://localhost/api/3.1/jobs/321',
                                                    headers={'Content-type': 'application/json'},
                                                    data=None)

    @with_httmock(authenticate_response)
    def test_get_device_broker(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        self.assertEquals(broker.__class__.__name__, 'DeviceBroker', "Device broker import error")

        broker = netmri.get_broker('AccessChange')
        self.assertEquals(broker.__class__.__name__, 'AccessChangeBroker', "AccessChangeBroker broker import error")

        broker = netmri.get_broker('ChangedPortNetExplorerInvSummaryGrid')
        self.assertEquals(broker.__class__.__name__, 'ChangedPortNetExplorerInvSummaryGridBroker',
                          'ChangedPortNetExplorerInvSummaryGridBroker broker import error ')

    @with_httmock(authenticate_response, devices_list_response)
    def test_get_devices_list(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri, 'session') as mock_request:
            broker.index()
            mock_request.request.assert_called_with("post",
                                                    'https://localhost/api/3/devices/index',
                                                    headers={'Content-type': 'application/json'},
                                                    data='{}')

    @with_httmock(authenticate_response, devices_list_response)
    def test_get_device(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri, 'session') as mock_request:
            broker.show(DeviceID=2)
            mock_request.request.assert_called_with("post",
                                                    'https://localhost/api/3/devices/show',
                                                    headers={'Content-type': 'application/json'},
                                                    data='{"DeviceID": 2}')

    @with_httmock(authenticate_response)
    def test_package_creation(self):
        netmri = InfobloxNetMRI(**self.opts)
        package = "infoblox_netmri.api.broker.v3_0_0.device_broker.DeviceBroker"
        self.assertEquals(package, netmri._get_broker_package("Device"))

    @with_httmock(authenticate_response)
    def test_check_return_values(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri.session, 'request', side_effect=devices_list):
            res = broker.index()
            self.assertEquals(res[0].DeviceID, 1, "Wrong id device 1")
            self.assertEquals(res[1].DeviceID, 2, "Wrong id device 2")

    @with_httmock(authenticate_response)
    def test_check_single_device(self):
        netmri = InfobloxNetMRI(**self.opts)
        broker = netmri.get_broker('Device')
        with patch.object(netmri.session, 'request', side_effect=single_device):
            res = broker.show(DeviceID=1)
            self.assertEquals(res.DeviceID, 1, "Wrong id")

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy(self):
        init_data = {'device_id': 1, 'job_id': 1, 'batch_id': 1}
        init_data.update(self.opts)
        with NetMRIEasy(**init_data) as easy:
            self.assertEquals(easy.device_id, 1)
            self.assertEquals(easy.job_id, 1)
            self.assertEquals(easy.batch_id, 1)
            self.assertIsNotNone(easy.dis_session)
            self.assertIsNotNone(easy.cli_connection)

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy_send_command(self):
        init_data = {'device_id': 1, 'job_id': 1, 'batch_id': 1}
        init_data.update(self.opts)
        with NetMRIEasy(**init_data) as easy:
            with patch.object(easy.client.session, 'request', side_effect=send_command_result) as mock_request:
                res = easy.send_command("show info")
                self.assertEquals(res, "OK")

    @with_httmock(authenticate_response, open_dis_session, open_cli_session, close_session)
    def test_easy_empty_params(self):
        # empty constructor test
        self.assertRaises(RuntimeError, NetMRIEasy)


if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
