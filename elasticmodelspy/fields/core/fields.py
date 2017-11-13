#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 04/11/2017.
"""
from elasticmodelspy.base import Serializable


class BaseField(Serializable):
    def __init__(self, name=None):
        super(BaseField, self).__init__(name)

    def serialize_data(self):
        return dict()

    def _serialize_field_data(self):
        return dict()
