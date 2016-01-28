Usage
=====

To use Infoblox NetMRI Client in a project::

  from infoblox_netmri import InfobloxNetMRI

  c = InfobloxNetMRI(host="netmri",
                     username="admin",
                     password="password")

  devices = c.api_request('devices/index', {'limit': 10})
