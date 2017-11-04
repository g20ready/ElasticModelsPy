#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.base import Serializable

class AnalysisSerializable(Serializable):
    def __init__(self, name):
        super(AnalysisSerializable, self).__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            self.name: self.serialize_data()
        }

    def serialize_data(self):
        raise NotImplemented()
