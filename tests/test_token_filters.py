#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticpymodels.analysis`"""

import pytest

from elasticpymodels.analysis.token_filters import TokenFilter, AsciiFoldTokenFilter\
    , StopwordsTokenFilter, LanguageTokenFilter, LengthTokenFilter, LowercaseTokenFilter

def test_filter():
    token_filter = TokenFilter('simple_lowercase', 'lowercase')
    assert token_filter.name == 'simple_lowercase'
    assert token_filter.type == 'lowercase'

    serialized = token_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'lowercase'

def test_ascii_folding_token_filter():
    ascii_fold_filter = AsciiFoldTokenFilter('my_ascii_fold', True)
    assert ascii_fold_filter.name == 'my_ascii_fold'
    assert ascii_fold_filter.preserve_original

    serialized = ascii_fold_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'asciifolding'
    assert serialized_data.get('preserve_original')

def test_stopwords_token_filter():
    stopwords_filter = StopwordsTokenFilter('simple_stopwords', '_greek_')
    assert stopwords_filter.name == 'simple_stopwords'
    assert stopwords_filter.type == 'stopwords'
    assert stopwords_filter.stopwords == '_greek_'

    serialized = stopwords_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'stopwords'
    assert serialized_data.get('stopwords') == '_greek_'

def test_language_token_filter():
    language_filter = LanguageTokenFilter('greek_lowercase', 'lowercase', 'greek')
    assert language_filter.name == 'greek_lowercase'
    assert language_filter.type == 'lowercase'
    assert language_filter.language == 'greek'

    serialized = language_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'lowercase'
    assert serialized_data.get('language') == 'greek'

def test_length_token_filter():
    length_token_filter = LengthTokenFilter('length_token_filter', 5, 20)
    assert length_token_filter.name == 'length_token_filter'
    assert length_token_filter.type == 'length'
    assert length_token_filter.min == 5
    assert length_token_filter.max == 20

    serialized = length_token_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'length'
    assert serialized_data.get('min') == 5
    assert serialized_data.get('max') == 20

def test_lowercase_token_filter():
    lowercase_token_filter = LowercaseTokenFilter('greek_lowercase', 'greek')
    assert lowercase_token_filter.name == 'greek_lowercase'
    assert lowercase_token_filter.type == 'lowercase'
    assert lowercase_token_filter.language == 'greek'

    serialized = lowercase_token_filter.__serialize__()
    assert isinstance(serialized, dict)
    assert 'name' in serialized.keys()

    serialized_data = serialized.get('name')
    assert serialized_data.get('type') == 'lowercase'
    assert serialized_data.get('language') == 'greek'


