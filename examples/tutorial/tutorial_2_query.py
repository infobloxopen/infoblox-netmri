from infoblox_netmri.client import InfobloxNetMRI

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

# get broker for interface addr
broker = client.get_broker('IfAddr')

# query interfaces which device id is greater than 20
addrs = broker.find(op_DeviceID=">",
                    val_c_DeviceID='20',
                    select=['DeviceID', 'DeviceName', 'InterfaceID', 'ifIPDotted'])

# get broker for interface remote model
interface_broker = client.get_broker('Interface')
for addr in addrs:
    interface = interface_broker.show(InterfaceID=addr.InterfaceID)
    print("{}    {}".format(addr.ifIPDotted, interface.ifName))
