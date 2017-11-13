#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 13/11/2017.
"""

def test_document_metaclass():
    from elasticmodelspy.index import Document
    from elasticmodelspy.fields.core import BaseField

    class SimpleDocument(Document):
        first_name = BaseField()
        sname = BaseField(name='last_name')

    doc = SimpleDocument()
    assert doc.first_name.name == 'first_name'
    assert doc.sname.name == 'last_name'
