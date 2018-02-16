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
import collections
import logging


"""
Miscellaneous modules for Odoo, consisting in decorator and other
methods for general purposes, including localization constraint
"""
__author__ = "Blanco Martín & Asociados (info@blancomartin.cl)"
__copyright__ = "Copyright (C) 2018 Blanco Martín y Asoc. EIRL - BMyA S.A."
__license__ = "LGPL 3.0"

_logger = logging.getLogger(__name__)


def localization(country_loc, call_super=False):
    """
    Decorator method to prevent execution of methods inherent to localization
    @author: Blanco Martín & Asociados.
    @version: 2018-02
    :param country_loc: two-digit code for country (e.g.: 'cl', 'ar')
    :return: execution of decorated method
    """
    _logger.info('Entering main decorator: localization')

    def inner(method):
        _logger.info('Entering inner inside decorator: inner')

        def wrapper(self, *args, **kwargs):
            _logger.info('Entering inside inner: wrapper')
            if self.env.ref(
                    'base.'+country_loc) == self.env.user.company_id.country_id:
                _logger.info(
                    'country_loc is ok: %s. executing decorated method'
                    % country_loc)
                method(self, *args, **kwargs)
            elif call_super:
                _logger.info('######----CALL SUPER---########')
                _logger.info(method)
                _logger.info(method.__name__)
                _logger.info(self.__class__)
                values = getattr(super(self.__class__, self), fnct.__name__)
            else:
                _logger.info(
                    'country_loc is not %s, function is overriden'
                    % country_loc)
        return wrapper
    return inner


def to_json(col_names, rows):
    """
    Method used inside db_handler decorator, to deliver dataset in JSON format
    @author: Blanco Martín & Asociados.
    @version: 2018-02
    :param col_names:
    :param rows:
    :return:
    """
    all_data = []
    for row in rows:
        each_row = collections.OrderedDict()
        i = 0
        for col_name in col_names:
            each_row[col_name] = row[i]
            i += 1
        all_data.append(each_row)
    return all_data


def db_handler(method):
    """
    Decorator db_handler used to deliver query execution, and in JSON format
    Usage: decorate a method that returns your desired query in Odoo
    @author: Blanco Martín & Asociados.
    @version: 2018-02
    :param method:
    :return:
    """
    def call(self, *args, **kwargs):
        _logger.info(args)
        query = method(self, *args, **kwargs)
        cursor = self.env.cr
        try:
            cursor.execute(query)
        except:
            return False
        rows = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        _logger.info('col_names: {}'.format(col_names))
        _logger.info('rows: {}'.format(rows))
        return to_json(col_names, rows)
    return call
