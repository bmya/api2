#!/usr/bin/python
# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

"""
Utility for api2 installation
"""
__author__ = "Blanco Martín & Asociados (info@blancomartin.cl)"
__copyright__ = "Copyright (C) 2018 Blanco Martín y Asoc. EIRL - BMyA S.A."
__license__ = "LGPL 3.0"


from setuptools import find_packages, setup

setup(
    name='api2',
    version='0.2',
    url='https://github.com/bmya/api2',
    license='LGPL-3',
    author='Blanco Martín & Asociados',
    author_email='info@blancomartin.cl',
    description='Utilities to make your life better in Odoo',
    long_description=open('README.md').read(),
    install_requires=[
    ],
    extras_require={
        ':python_version == "2.7"': ['enum34 >= 1.0.4'],
        ':python_version == "3.3"': ['enum34 >= 1.0.4']
    },
    # packages=find_packages(exclude=['test']),
    # packages=['api2'],
    py_modules=['api2'],
    platforms=['MacOS X', 'Posix'],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: LGPL-3',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
