#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Serializable(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'BaseField(name=%s)' % self.name or ''

    def serialize(self):
        """
        :return:        dict repr of the object.
        """
        return {
            self.name: self.serialize_data()
        }

    def serialize_data(self):
        raise NotImplemented()
