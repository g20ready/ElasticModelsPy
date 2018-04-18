#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""
from abc import abstractmethod, abstractproperty


class FieldTypeMixin(object):
    @abstractmethod
    def field_type(self):
        return 'field_type'


class FieldAttributesMixin(object):
    @abstractmethod
    def field_attributes(self):
        return []
