#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticpymodels.analysis`"""

import pytest

from elasticpymodels.analysis.token_filters import TokenFilter, AsciiFoldTokenFilter\
    , StopwordsTokenFilter, LanguageTokenFilter, LengthTokenFilter, LowercaseTokenFilter\
    , UppercaseTokenFilter, NgramTokenFilter, StopTokenFilter

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

def test_uppercase_token_filter():
    uppercase_token_filter = UppercaseTokenFilter('greek_uppercase', 'greek')
    assert uppercase_token_filter.__serialize__() == {
        'greek_uppercase': {
            'type': 'uppercase',
            'language': 'greek'
        }
    }


def test_ngram_token_filter():
    ngram_token_filter = NgramTokenFilter('ngram_token_filter', 1, 20)
    assert ngram_token_filter.__serialize__() == {
        'ngram_token_filter' : {
            'type': 'nGram',
            'min_gram': 1,
            'max_gram': 20
        }
    }


def test_stop_token_filter():
    test_stop_filter = StopTokenFilter('stop_token_filter', ['is', 'the', 'and'],
                                       '/home/tester/stepwords_path.txt', False , True)
    assert test_stop_filter.__serialize__() == {
        'stop_token_filter': {
            'type': 'stop',
            'stopwords':  ['is', 'the', 'and'],
            'stopwords_path': '/home/tester/stepwords_path.txt',
            'ignore_case': False,
            'remove_trailing': True
        }
    }