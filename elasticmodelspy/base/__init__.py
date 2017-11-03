#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Serializable(object):
    def __init__(self):
        pass

    def serialize(self):
        """
        :return:        dict repr of the object.
        """
        raise NotImplemented()
