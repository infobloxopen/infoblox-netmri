.. :changelog:

History
=======

0.1.6 (2018-06-04)
----------------------
* Implement debug logging of HTTP requests to NetMRI.
  You can activate it by adding a `logger <https://docs.python.org/3/howto/logging.html#configuring-logging>`_
  named ``infoblox_netmri`` with level ``DEBUG``.

0.1.5 (2017-08-09)
----------------------
* Fix issue #11, where an API versions numbers with a minor part were not seen as valid.

0.1.4 (2017-03-22)
------------------
* Fix issue #7, where an expired session is never renewed.
* Cleanup and make more Pythonic

0.1.3 (2016-02-19)
------------------
* Implement authentication caching

0.1.2 (2016-01-07)
------------------
* Fix issue passing strings to show and delete methods
* Add Python 3 compatibility

0.1.1 (2015-11-11)
------------------
* Fix module naming issue

0.1.0 (2015-11-09)
------------------
* First release on PyPI.
