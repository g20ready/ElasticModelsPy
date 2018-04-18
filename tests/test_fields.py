#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 13/12/2017.
"""
import pytest

from elasticmodelspy.index import BaseField

def test_field_without_type():
    try:
        class FieldWithoutType(BaseField):
            pass
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert "Subclasses of BaseField must provide a value for 'field_type'." == ex.args[0]

def test_field_without_available_props():
    try:
        class FieldWithoutAvailableProps(BaseField):
            field_type = 'what'
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert "Subclasses of BaseField must provide a value for 'field_attributes'." == ex.args[0]

class SimpleField(BaseField):
    field_type = 'simple'
    field_attributes = ['index']

def test_field_with_error_attributes():
    try:
        SimpleField(name='simple', random='random')
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert "'random' is not a valid attribute." == ex.args[0]

def test_field_type():
    assert SimpleField(name='simple', index=False).serialize_data() == {
        'type': 'simple',
        'index': False
    }

def test_text_field():
    from elasticmodelspy.index import TextField
    from elasticmodelspy.analysis.analyzers import StandardAnalyzer

    # text field with standard analyzer class
    standard_analyzer = StandardAnalyzer('standard')
    text_field = TextField(name='analyzer_class_text_field',
                           analyzer=standard_analyzer)
    assert text_field.__getattribute__('analyzer') == 'standard'

    # text field with string analyzer
    text_field = TextField(name='analyzer_class_text_field',
                           analyzer=standard_analyzer.name)
    assert text_field.__getattribute__('analyzer') == 'standard'

    # text field with error analyzer
    try:
        text_field = TextField(name='analyzer_class_text_field', analyzer=123)
    except Exception as ex:
        assert isinstance(ex, ValueError)
        assert "Property 'analyzer' must be an instance of elasticmodelspy.analysis.Analyzer " \
               "or an instance of string type." == ex.args[0]




