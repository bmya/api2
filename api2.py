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
from __future__ import print_function
import logging


"""
Miscelaneous auxiliar modules for Odoo, consisting in decorator and other
methods for general purposes, including localization constriaint
"""
__author__ = "Blanco Martín & Asociados (info@blancomartin.cl)"
__copyright__ = "Copyright (C) 2018 Blanco Martín y Asoc. EIRL - BMyA S.A."
__license__ = "LGPL 3.0"

_logger = logging.getLogger(__name__)


def localization(country_loc):
    _logger.info('Entering main decorator: localization')

    def inner(method):
        _logger.info('Entering inner inside decorator: inner')

        def wrapper(self, *args, **kwargs):
            _logger.info('Entering inside inner: wrapper')
            if self.env.ref(
                    'base.'+country_loc) == self.env.user.company_id.country_id:
                # if country_loc == 'cl':
                _logger.info(
                    'country_loc is ok: %s. executing decorated method %s'
                    % country_loc, method.__name__)
                method(self, *args, **kwargs)
            else:
                _logger.info(
                    'country_loc is not %s, function %s overriden'
                    % country_loc, method.__name__)
        return wrapper
    return inner
