#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""

class FielddataMixin(object):
    fielddata = False
    # fielddata_frequency_filter =


class IndexMixin(object):
    index = True
    index_options = 'positions'
