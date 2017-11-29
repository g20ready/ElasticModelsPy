#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""
from weakref import WeakKeyDictionary

from elasticmodelspy.base import Serializable

class BaseField(Serializable):
    def __init__(self, name=None):
        super(BaseField, self).__init__(name)
        self._values = WeakKeyDictionary()

    def serialize_data(self):
        return dict()

    def _serialize_field_data(self):
        return dict()

    def __get__(self, instance, owner):
        if instance is None: return self
        return self._values.get(instance)

    def __set__(self, instance, value):
        self._validate_(value)
        self._values[instance] = value

    def _validate_(self, value):
        """
        Raise value error if value is invalid for custom field.
        """
        pass
