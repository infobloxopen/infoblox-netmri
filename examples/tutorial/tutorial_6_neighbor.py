import argparse

from infoblox_netmri.client import InfobloxNetMRI

parser = argparse.ArgumentParser(description='run jobs for specific devices')
parser.add_argument('device_name', help="script name")
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

devices_broker = client.get_broker('Device')
device = devices_broker.index(
    DeviceName=args.device_name,
    select=['DeviceID', 'DeviceName']
)[0]

print(device.DeviceName)

# find the neighbor relationships where our device
# is the source
source_relations = client.get_broker('Neighbor').index(
    DeviceID=device.DeviceID,
    select=['NeighborDeviceID']
)

# find the neighbor relationships where our device
# is the destination.
destination_relations = client.get_broker('Neighbor').index(
    NeighborDeviceID=device.DeviceID,
    select=['DeviceID', ]
)

source_relations_ids = [x.NeighborDeviceID for x in source_relations]
for s_id in source_relations_ids:
    neighbor_device = devices_broker.index(
        DeviceID=s_id,
        select=['DeviceID', 'DeviceName', 'DeviceType']
    )
    print(" ->  {}  {}\n".format(neighbor_device.DeviceType, neighbor_device.DeviceName))


destination_ids = [x.DeviceID for x in destination_relations]
for d_id in destination_ids:
    neighbor_device = devices_broker.index(
        DeviceID=s_id,
        select=['DeviceID', 'DeviceName', 'DeviceType']
    )
    print(" ->  {}  {}\n".format(neighbor_device.DeviceType, neighbor_device.DeviceName))
