import argparse

from infoblox_netmri.client import InfobloxNetMRI

parser = argparse.ArgumentParser(description='run jobs for specific devices')
parser.add_argument('script_name', help="script name")
parser.add_argument('pattern', help="name pattern")
parser.add_argument('command', help="value of the Script-Variable $command")
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

# get Script broker
broker = client.get_broker('Device')

# get devices
devices = broker.find(
    op_DeviceName='like',
    val_c_DeviceName=args.pattern,
    select=['DeviceID']
)

# get Script broker
script_broker = client.get_broker('Script')

# submit the job to the NetMRI
job_id = script_broker.run(**{
    'name': args.script_name,
    'device_ids': [x.DeviceID for x in devices],
    '$command': args.command
})

# let the user know how many devices the script is run on.
print("{} run on {} devices".format(args.script_name, [x.DeviceID for x in devices]))
