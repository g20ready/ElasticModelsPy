#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 03/11/2017.
"""
from six import with_metaclass

from weakref import WeakKeyDictionary

from elasticmodelspy.base import Serializable

from .mixins import TypeMixin, IndexMixin, FielddataMixin


class FieldMeta(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate Base Field
        if bases != (Serializable, TypeMixin,):
            if not class_dict.get('field_type'):
                raise ValueError('Subclasses of BaseField must provide a value for type.')
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class BaseField(with_metaclass(FieldMeta, TypeMixin, Serializable)):
    field_type = 'base'
    def __init__(self, name=None):
        super(BaseField, self).__init__(name)
        self._values = WeakKeyDictionary()

    def serialize_data(self):
        data = dict(
            type=self.field_type
        )
        dict.update(self._serialize_field_data())
        return data

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

class TextField(IndexMixin, FielddataMixin, BaseField):
    field_type = 'text'
    def __init__(self, name=None, fielddata=False, index=True, index_options='positions', **kwargs):
        super(TextField, self).__init__('text', name)
        self.fielddata = fielddata
        self.index = index
        self.index_options = index_options

    def _serialize_field_data(self):
        return dict(
            fielddata=self.fielddata,
            index=self.index,
            index_options=self.index_options
        )

class KeywordField(BaseField):
    field_type = 'keyword'
    def __init__(self, name=None):
        super(KeywordField, self).__init__(name)

    def _serialize_field_data(self):
        return self.__dict__
