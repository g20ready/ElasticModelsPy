#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 13/12/2017.
"""
import pytest

from elasticmodelspy.fields import BaseField

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
        assert "Subclasses of BaseField must provide a value for 'available_props'." == ex.args[0]

def test_field_type():
    class SimpleField(BaseField):
        field_type = 'simple'
        available_props = ['index']

    assert SimpleField(name='simple', index=False).serialize_data() == {
        'type': 'simple',
        'index': False
    }
