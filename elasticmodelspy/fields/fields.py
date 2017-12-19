#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 03/11/2017.
"""
from six import with_metaclass, string_types

from weakref import WeakKeyDictionary

from elasticmodelspy.base import Serializable
from elasticmodelspy.analysis import Analyzer

from .mixins import FieldTypeMixin, FieldAttributesMixin


class FieldMeta(type):
    def __new__(meta, name, bases, class_dict):
        # Don't validate Base Field
        if name != 'BaseField':
            if not class_dict.get('field_type'):
                raise ValueError("Subclasses of BaseField must provide a value for 'field_type'.")
            if not class_dict.get('field_attributes'):
                raise ValueError("Subclasses of BaseField must provide a value for 'field_attributes'.")
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class BaseField(with_metaclass(FieldMeta, FieldTypeMixin, FieldAttributesMixin, Serializable)):
    def __init__(self, name=None, **kwargs):
        super(BaseField, self).__init__(name)
        self._values = WeakKeyDictionary()
        for key in kwargs:
            # Validate that the current value is in field attributes.
            if not key in self.field_attributes:
                raise ValueError("'%s' is not a valid attribute." % key)

            # if validate function is defined for the given key
            # the value returned is assigned.
            if hasattr(self, 'validate_%s' % key):
                value = getattr(self, 'validate_%s' % key)(kwargs.get(key))
            else:
                value = kwargs.get(key)
            setattr(self, key, value)

    def serialize_data(self):
        data = dict(
            type=self.field_type
        )
        data.update({
            key: getattr(self, key, None)
            for key in self.field_attributes
            if hasattr(self, key)
        })
        return data

    def __get__(self, instance, owner):
        if instance is None: return self
        return self._values.get(instance)

    def __set__(self, instance, value):
        self._validate_(value)
        self._values[instance] = value

    def __delete__(self, instance):
        del self._values[instance]

    def _validate_(self, value):
        """
        Raise value error if value is invalid for custom field.
        """
        pass


class TextField(BaseField):
    field_type = 'text'
    field_attributes = [
        'analyzer',
        'boost',
        'eager_global_ordinals',
        'fielddata',
        'fielddata_frequency_filter',
        'fields',
        'index',
        'index_options',
        'norms',
        'position_increment_gap',
        'store',
        'search_analyzer',
        'search_quote_analyzer',
        'similarity',
        'term_vector'
    ]
    def __init__(self, name=None, **kwargs):
        super(TextField, self).__init__(name, **kwargs)

    def validate_analyzer(self, value):
        if isinstance(value, Analyzer):
            return value.name
        elif isinstance(value, string_types):
            return value
        raise ValueError("Property 'analyzer' must be an instance of elasticmodelspy.analysis.Analyzer "
                         "or an instance of string type.")


class KeywordField(BaseField):
    field_type = 'keyword'
    field_attributes = [
        'boost',
        'doc_values',
        'eager_global_ordinals',
        'fields',
        'ignore_above',
        'index',
        'index_options',
        'norms',
        'null_value',
        'store',
        'similarity',
        'normalizer'
    ]
    def __init__(self, name=None, **kwargs):
        super(KeywordField, self).__init__(name)

    def _serialize_field_data(self):
        return self.__dict__
