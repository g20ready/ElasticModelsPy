#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""
from six import with_metaclass
from elasticmodelspy.fields.core import BaseField

class DocumentMeta(type):
    def __new__(meta, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, BaseField) and not value.name:
                value.name = key
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class Document(with_metaclass(DocumentMeta, object)):

    def mapping(self):
        mapping = dict()
        for key, value in self.__dict__.items():
            if isinstance(value, BaseField) and value:
                mapping.update(value.serialize())
        return mapping


