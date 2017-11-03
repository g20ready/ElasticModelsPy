#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticmodelspy.analysis`"""

import pytest

# from elasticpymodels.analysis.token_filters import TokenFilter, AsciiFoldTokenFilter\
#     , StopwordsTokenFilter, LanguageTokenFilter, LengthTokenFilter, LowercaseTokenFilter\
#     , UppercaseTokenFilter, NgramTokenFilter, StopTokenFilter, EdgeNgramTokenFilter

from elasticpymodels.analysis.token_filters import *

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
    ngram_token_filter = NgramTokenFilter('ngram_token_filter', 1, 2)
    assert ngram_token_filter.__serialize__() == {
        'ngram_token_filter' : {
            'type': 'nGram',
            'min_gram': 1,
            'max_gram': 2
        }
    }


def test_edge_ngram_token_filter():
    test_edge_ngram_filter = EdgeNgramTokenFilter('edge_ngram_filter', 1, 2, 'front')
    assert test_edge_ngram_filter.__serialize__() == {
        'edge_ngram_filter': {
            'type': 'edgeNGram',
            'min_gram' : 1,
            'max_gram': 2,
            'side': 'front'
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


def test_word_delimeter_token_filter():
    test_word_delimeter_filter = WordDelimiterTokenFilter(name='word_delimiter_filter',
                                                          protected_words=['test', 'word', 'delimiter', 'filter'])
    assert test_word_delimeter_filter.__serialize__() == {
        'word_delimiter_filter' : {
            'type': 'word_delimiter',
            'generate_word_parts': True,
            'generate_number_parts': True,
            'catenate_words': False,
            'catenate_numbers': False,
            'catenate_all': False,
            'split_on_case_change': True,
            'preserve_original': False,
            'split_on_numerics': True,
            'stem_english_possessive': True,
            'protected_words_path': None,
            'protected_words': ['test', 'word', 'delimiter', 'filter']
        }
    }

def test_word_delimeter_graph_token_filter():
    test_word_delimeter_graph_filter = WordDelimeterGraphTokenFilter('word_delimiter_graph_filter',
                                                                     protected_words=['test', 'word', 'delimiter', 'filter'])
    assert test_word_delimeter_graph_filter.__serialize__() == {
        'word_delimiter_graph_filter' : {
            'type': 'word_delimiter_graph',
            'generate_word_parts': True,
            'generate_number_parts': True,
            'catenate_words': True,
            'catenate_numbers': True,
            'catenate_all': True,
            'split_on_case_change': True,
            'preserve_original': True,
            'split_on_numerics': True,
            'stem_english_possessive': True,
            'protected_words_path': None,
            'protected_words': ['test', 'word', 'delimiter', 'filter']
        }
    }

def tes_synonym_token_filter():
    test_synonym_filter = SynonymTokenFilter('synonym_token_filter')
    assert test_synonym_filter.__serialize__() == {
        'synonym_token_filter' : {
            'type': 'synonym',
            'synonyms_path' : 'analysis/synonym.txt',
            'tokenizer': 'whitespace',
            'ignore_case': False
        }
    }
