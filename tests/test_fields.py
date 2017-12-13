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
        assert 'Subclasses of BaseField must provide a value for type.' == ex.args[0]

def test_field_type():
    class SimpleField(BaseField):
        field_type = 'simple'

    assert SimpleField().serialize_data() == {
        'type': 'simple'
    }
