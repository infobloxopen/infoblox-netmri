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
    # return result of command execution
    result = easy.send_command('show version')
    print(result)
    print(20 * "=")
    # send async command. As result return TrakingID. If flag wait_until_finished=True, will work as send_command
    result = easy.send_async_command('show version', 60, '', wait_until_finished=False)
    print(result)
