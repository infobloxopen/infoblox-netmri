Infoblox NetMRI Client
======================

.. image:: https://codecov.io/github/infobloxopen/infoblox-netmri/coverage.svg?branch=master
    :target: https://codecov.io/github/infobloxopen/infoblox-netmri?branch=master

.. image:: https://img.shields.io/travis/infobloxopen/infoblox-netmri.svg
        :target: https://travis-ci.org/infobloxopen/infoblox-netmri

.. image:: https://img.shields.io/pypi/v/infoblox-netmri.svg
        :target: https://pypi.python.org/pypi/infoblox-netmri


A simple client for the Infoblox NetMRI RESTful API.

* Free software: Apache license
* Homepage: https://github.com/infobloxopen/infoblox-netmri
* Documentation: https://infoblox-netmri.readthedocs.org

Features
--------

* Enables execution of RESTful API calls on the NetMRI via Python.
* HTTP and HTTPS

Installation
------------

Install infoblox-netmri using pip:

::

  pip install infoblox-netmri


Usage
-----

It's simple to use. Just create an ``InfobloxNetMRI`` object and then call the
``api_request`` method. Almost every API request will return a dictionary. It
will contain the outputs documented in the online API documentation.

::

  from infoblox_netmri import InfobloxNetMRI

  c = InfobloxNetMRI(host="netmri",
                     username="admin",
                     password="password")

  devices = c.api_request('devices/index', {'limit': 10})

Now, ``devices`` contains a dictionary of the API call outputs. In this case,
it contains the standard keys returned by "list" style methods (index, search,
find - see the docs): ``current``, ``start``, ``limit``, and the plural form
of the model, ``devices``. This last is an array of dictionaries with the
device details, while the others describe the "paging" information of the
result. So, we really want to loop through ``devices['devices']``:

::

  FORMAT='%30s %16s %10s'
  print FORMAT % ('Device Name', 'IP Address', 'Vendor')
  for d in devices['devices']:
      print FORMAT % (d['DeviceName'], d['DeviceIPDotted'], d['DeviceVendor'])


NetMRI Documentation
--------------------

To see documentation on the calls available, visit the page /api/docs on
your NetMRI.

Please also see https://github.com/infobloxopen/netmri-toolkit for examples.
