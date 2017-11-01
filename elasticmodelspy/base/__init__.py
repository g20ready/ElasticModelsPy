#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Serializable(object):
    def __init__(self):
        pass

    def __serialize__(self):
        raise NotImplemented()
