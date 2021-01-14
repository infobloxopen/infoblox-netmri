import re
from infoblox_netmri.easy import NetMRIEasy

# This values will be provided by NetMRI before execution


defaults = {
    "api_url": 'api_url',
    "http_username": 'http_username',
    "http_password": 'http_password',
    "job_id": 'job_id',
    "device_id": 'device_id',
    "batch_id": 'batch_id'
}

# Create NetMRI context manager. It will close session after execution
with NetMRIEasy(**defaults) as easy:
    field_name = "chasis_serial_number"
    # custom field creation
    broker = easy.client.get_broker('CustomFields')
    broker.create_field(
        model='Device',
        name=field_name,
        type='string'
    )
    # get device
    device = easy.get_device()
    # The method for retrieving the serial number via the
    # CLI depends on the type of device.
    if device.DeviceType == 'Router':
        inventory = easy.send_command('show inventory')
        serial = re.search('(?<=SN: ).*$', inventory).group()
    else:
        info = easy.send_command('show version')
        serial = re.search('(?<=System serial number: ).*$').group()

    if serial:
        # Custom field creation
        # all custom fields should start with 'custom_'
        device_broker = easy.client.get_broker('Device')
        field_name = "custom_{}".format(field_name)
        params = {
            'DeviceID': device.DeviceID,
            field_name: serial
        }
        result = device_broker.update(**params)
        print(result.custom_chasis_serial_number)
