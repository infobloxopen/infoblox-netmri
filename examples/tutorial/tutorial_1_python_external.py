#!/usr/bin/env python

import argparse

from infoblox_netmri.client import InfobloxNetMRI

parser = argparse.ArgumentParser(description='get device ip')
parser.add_argument('device_id', help="device id")
args = parser.parse_args()

defaults = {
    "host": "1.2.3.4",
    "username": "your_username",
    "password": "your_password",
}

client = InfobloxNetMRI(
    defaults.get("host"),
    defaults.get("username"),
    defaults.get("password"),
)

# get broker for specific API Object
broker = client.get_broker("Device")

device = broker.show(DeviceID=args.device_id)
print(device.DeviceIPDotted)
