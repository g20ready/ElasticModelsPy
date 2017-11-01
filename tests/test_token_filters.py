#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticmodelspy.analysis`"""

import pytest

from elasticmodelspy.analysis.token_filters import TokenFilter, AsciiFoldTokenFilter\
    , StopwordsTokenFilter, LanguageTokenFilter, LengthTokenFilter, LowercaseTokenFilter

def test_filter():
    token_filter = TokenFilter('simple_lowercase', 'lowercase')
    assert token_filter.__serialize__() == {
        'simple_lowercase': {
            'type': 'lowercase'
        }
    }

def test_ascii_folding_token_filter():
    ascii_fold_filter = AsciiFoldTokenFilter('my_ascii_fold', True)
    assert ascii_fold_filter.__serialize__() == {
        'my_ascii_fold': {
            'type': 'asciifolding',
            'preserve_original': True
        }
    }

def test_stopwords_token_filter():
    stopwords_filter = StopwordsTokenFilter('simple_stopwords', '_greek_')
    assert stopwords_filter.__serialize__() == {
        'simple_stopwords': {
            'type': 'stopwords',
            'stopwords': '_greek_'
        }
    }

def test_language_token_filter():
    language_filter = LanguageTokenFilter('greek_lowercase', 'lowercase', 'greek')
    assert language_filter.__serialize__() == {
        'greek_lowercase': {
            'type': 'lowercase',
            'language': 'greek'
        }
    }

def test_length_token_filter():
    length_token_filter = LengthTokenFilter('length_token_filter', 5, 20)
    assert length_token_filter.__serialize__() == {
        'length_token_filter': {
            'type': 'length',
            'min': 5,
            'max': 20
        }
    }

def test_lowercase_token_filter():
    lowercase_token_filter = LowercaseTokenFilter('greek_lowercase', 'greek')
    assert lowercase_token_filter.__serialize__() == {
        'greek_lowercase': {
            'type': 'lowercase',
            'language': 'greek'
        }
    }


