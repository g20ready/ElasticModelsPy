#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Created by Marsel Tzatzo on 03/11/2017.
"""

from elasticmodelspy.analysis.analyzers import Analyzer, StandardAnalyzer, SimpleAnalyzer, WhiteSpaceAnalyzer, \
    StopAnalyzer, KeywordAnalyzer, PatternAnalyzer, CustomAnalyzer

def test_analyzer():
    analyzer = Analyzer('name', 'type')
    assert analyzer.serialize() == {
        'name': {
            'type': 'type'
        }
    }

def test_standard_analyzer():
    standard_analyzer = StandardAnalyzer('standard_analyzer',
                                         max_token_length=10,
                                         stopwords=['a', 'b', 'c'])
    assert standard_analyzer.serialize() == {
        'standard_analyzer': {
            'type': 'standard',
            'max_token_length': 10,
            'stopwords': ['a', 'b', 'c']
        }
    }

    standard_analyzer = StandardAnalyzer('standard_analyzer',
                                         stopwords_path='stopwords.txt')
    assert standard_analyzer.serialize() == {
        'standard_analyzer': {
            'type': 'standard',
            'stopwords_path': 'stopwords.txt'
        }
    }

def test_simple_analyzer():
    simple_analyzer = SimpleAnalyzer('simple_analyzer')
    assert simple_analyzer.serialize() == {
        'simple_analyzer': {
            'type': 'simple'
        }
    }

def test_white_space_analyzer():
    white_space_analyzer = WhiteSpaceAnalyzer('white_space_analyzer')
    assert white_space_analyzer.serialize() == {
        'white_space_analyzer': {
            'type': 'whitespace'
        }
    }

def test_stop_analyzer():
    stop_analyzer = StopAnalyzer('stop_analyzer',
                                 stopwords=['this', 'that', 'them'],
                                 stopwords_path='stopwords.txt')
    assert stop_analyzer.serialize() == {
        'stop_analyzer': {
            'type': 'stop',
            'stopwords': ['this', 'that', 'them']
        }
    }

    stop_analyzer = StopAnalyzer('stop_analyzer', stopwords_path='stopwords.txt')
    assert stop_analyzer.serialize() == {
        'stop_analyzer': {
            'type': 'stop',
            'stopwords_path': 'stopwords.txt'
        }
    }

def test_keyword_analyzer():
    keyword_analyzer = KeywordAnalyzer('keyword_analyzer')
    assert keyword_analyzer.serialize() == {
        'keyword_analyzer': {
            'type': 'keyword'
        }
    }

def test_pattern_analyzer():
    pattern_analyzer = PatternAnalyzer('pattern_analyzer',
                                       "\\W|_",
                                       stopwords=['this', 'that', 'them'])
    assert pattern_analyzer.serialize() == {
        'pattern_analyzer': {
            'type': 'pattern',
            'pattern': "\\W|_",
            'lowercase': True,
            'stopwords': ['this', 'that', 'them']
        }
    }

    pattern_analyzer = PatternAnalyzer('pattern_analyzer',
                                       "\\W|_",
                                       lowercase=False,
                                       stopwords_path='stopwords.txt')
    assert pattern_analyzer.serialize() == {
        'pattern_analyzer': {
            'type': 'pattern',
            'pattern': "\\W|_",
            'lowercase': False,
            'stopwords_path': 'stopwords.txt'
        }
    }

def test_custom_analyzer():
    from elasticmodelspy.analysis.tokenizers import StandardTokenizer
    from elasticmodelspy.analysis.char_filters import HtmlCharFilter
    from elasticmodelspy.analysis.token_filters import LowercaseTokenFilter

    standard_tokenizer = StandardTokenizer('standard_tokenizer')
    html_char_filter = HtmlCharFilter('html_char_filter')
    language_token_filter = LowercaseTokenFilter('language_token_filter', 'greek')

    custom_analyzer = CustomAnalyzer('custom_analyzer',
                                     tokenizer=standard_tokenizer,
                                     char_filters=html_char_filter,
                                     token_filters=language_token_filter)

    assert custom_analyzer.serialize() == {
        'custom_analyzer': {
            'type': 'custom',
            'tokenizer': 'standard_tokenizer',
            'char_filter': ['html_char_filter'],
            'token_filter': ['language_token_filter'],
            'position_increment_gap': 100
        }
    }

    assert custom_analyzer.char_filter_data() == {
        'html_char_filter': html_char_filter.serialize_data()
    }

    assert custom_analyzer.token_filter_data() == {
        'language_token_filter': language_token_filter.serialize_data()
    }

    assert custom_analyzer.tokenizer_data() == standard_tokenizer.serialize()


