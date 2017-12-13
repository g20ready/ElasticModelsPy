#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""
from six import with_metaclass, iteritems

from elasticmodelspy.fields import BaseField

class DocumentMeta(type):
    def __new__(meta, name, bases, class_dict):
        class_dict['__document_attr'] = DocumentAttr(class_dict)
        cls = type.__new__(meta, name, bases, class_dict)
        return cls


class DocumentAttr(object):
    def __init__(self, class_dict):
        self.fields = {}
        for key, value in iteritems(class_dict):
            if isinstance(value, BaseField):
                if not value.name:
                    value.name = key
                self.fields[key] = value.name
        self.inverted_fields = { v: k for k, v in iteritems(self.fields) }


class Document(with_metaclass(DocumentMeta, object)):
    def __init__(self, **kwargs):
        for key, value in iteritems(kwargs):
            if key in self.document_atrr_inv_fields:
                setattr(self, self.document_atrr_inv_fields[key], value)

    @property
    def document_attr(self):
        return getattr(self, '__document_attr')

    @property
    def document_attr_fields(self):
        return self.document_attr.fields

    @property
    def document_atrr_inv_fields(self):
        return self.document_attr.inverted_fields

    def document(self):
        document = dict()
        for key, value in iteritems(self.document_attr_fields):
            document.update({
                value: getattr(self, key)
            })
        return document

    @classmethod
    def mapping(cls):
        mapping = dict()
        for key, value in iteritems(cls.__dict__):
            if isinstance(value, BaseField) and value:
                mapping.update(value.serialize())
        return mapping



