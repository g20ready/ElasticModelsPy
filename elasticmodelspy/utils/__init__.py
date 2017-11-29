#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 24/11/2017.
"""
from six import iteritems

class IterMixin(object):
    def __iter__(self):
        for attr, value in iteritems(self.__dict__):
            yield attr, value
