#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 03/11/2017.
"""
from .core import BaseField
from .core import IndexMixin, FielddataMixin


class TextField(IndexMixin, FielddataMixin, BaseField):
    def __init__(self, name, fielddata=False, index=True, index_options='positions'):
        super(TextField, self).__init__(name)
        self.fielddata = fielddata
        self.index = index
        self.index_options = index_options

