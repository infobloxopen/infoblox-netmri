#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'requests>=2.5.2',
]

test_requirements = [
    'mock>=1.2',
    'httmock>=1.2.4'
]


setup(
    name='infoblox-netmri',
    version="3.7.0.0",
    description="A simple client for the Infoblox NetMRI RESTful API.",
    long_description=readme,
    author="Infoblox, Inc.",
    author_email='narslanova@infoblox.com',
    url='https://netmri_ip/api/dist',
    packages=find_packages(exclude='infoblox_netmri.tests'),
    package_dir={'infoblox_netmri':
                 'infoblox_netmri'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache",
    zip_safe=False,
    keywords='infoblox_netmri netmri infoblox network automation',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    test_suite='infoblox_netmri.tests',
    tests_require=test_requirements
)
