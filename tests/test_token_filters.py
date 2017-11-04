#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticmodelspy.analysis`"""

import pytest

# from elasticpymodels.analysis.token_filters import TokenFilter, AsciiFoldTokenFilter\
#     , StopwordsTokenFilter, LanguageTokenFilter, LengthTokenFilter, LowercaseTokenFilter\
#     , UppercaseTokenFilter, NgramTokenFilter, StopTokenFilter, EdgeNgramTokenFilter

from elasticmodelspy.analysis.token_filters import *

def test_filter():
    token_filter = TokenFilter('simple_lowercase', 'lowercase')
    assert token_filter.serialize() == {
        'simple_lowercase': {
            'type': 'lowercase'
        }
    }

def test_ascii_folding_token_filter():
    ascii_fold_filter = AsciiFoldTokenFilter('my_ascii_fold', True)
    assert ascii_fold_filter.serialize() == {
        'my_ascii_fold': {
            'type': 'asciifolding',
            'preserve_original': True
        }
    }

def test_stopwords_token_filter():
    stopwords_filter = StopwordsTokenFilter('simple_stopwords', '_greek_')
    assert stopwords_filter.serialize() == {
        'simple_stopwords': {
            'type': 'stopwords',
            'stopwords': '_greek_'
        }
    }

def test_language_token_filter():
    language_filter = LanguageTokenFilter('greek_lowercase', 'lowercase', 'greek')
    assert language_filter.serialize() == {
        'greek_lowercase': {
            'type': 'lowercase',
            'language': 'greek'
        }
    }

def test_length_token_filter():
    length_token_filter = LengthTokenFilter('length_token_filter', 5, 20)
    assert length_token_filter.serialize() == {
        'length_token_filter': {
            'type': 'length',
            'min': 5,
            'max': 20
        }
    }

def test_lowercase_token_filter():
    lowercase_token_filter = LowercaseTokenFilter('greek_lowercase', 'greek')
    assert lowercase_token_filter.serialize() == {
        'greek_lowercase': {
            'type': 'lowercase',
            'language': 'greek'
        }
    }

def test_uppercase_token_filter():
    uppercase_token_filter = UppercaseTokenFilter('greek_uppercase', 'greek')
    assert uppercase_token_filter.serialize() == {
        'greek_uppercase': {
            'type': 'uppercase',
            'language': 'greek'
        }
    }


def test_ngram_token_filter():
    ngram_token_filter = NgramTokenFilter('ngram_token_filter', 1, 2)
    assert ngram_token_filter.serialize() == {
        'ngram_token_filter' : {
            'type': 'nGram',
            'min_gram': 1,
            'max_gram': 2
        }
    }


def test_edge_ngram_token_filter():
    test_edge_ngram_filter = EdgeNgramTokenFilter('edge_ngram_filter', 1, 2, 'front')
    assert test_edge_ngram_filter.serialize() == {
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
    assert test_stop_filter.serialize() == {
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
    assert test_word_delimeter_filter.serialize() == {
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
    assert test_word_delimeter_graph_filter.serialize() == {
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

def test_stemmer_token_filter():
    test_stemmer_token_filter = StemmerTokenFilter('stemmer_token_filter', 'greek')
    assert test_stemmer_token_filter.serialize() == {
        'stemmer_token_filter' : {
            'type': 'stemmer',
            'language': 'greek'
        }
    }

def test_stemmer_override_token_filter():
    test_stemmer_rules = ["running => run", "stemmer => stemmer"]
    test_stemmer_rules_path = "analysis/stemmer_override.txt"

    test_stemmer_override_token_filter = StemmerOverrideTokenFilter('stemmer_override_token_filter',
                                                                    test_stemmer_rules,
                                                                    test_stemmer_rules_path)
    assert test_stemmer_override_token_filter.serialize() == {
        'stemmer_override_token_filter' : {
            'type': 'stemmer_override',
            'rules': [],
            'rules_path': test_stemmer_rules_path
        }
    }

def test_keyword_marker_token_filter():
    test_keywords =["cats"]
    test_keywords_path= "analysis/keyword_marker.txt"
    test_keywords_pattern =  "(\\w+)"
    test_keyword_marker_token_filter = KeywordMarkerTokenFilter('keyword_marker_token_filter',
                                                                    test_keywords,
                                                                    test_keywords_path,
                                                                    test_keywords_pattern)
    assert test_keyword_marker_token_filter.serialize() == {
        'keyword_marker_token_filter' : {
            'type': 'keyword_marker',
            'keywords': [],
            'keywords_path': test_keywords_path,
            'keywords_pattern': test_keywords_pattern,
            'ignore_case': False
       }
    }

def test_kstem_token_filter():
    test_kstem_filter = KStemTokenFiltrer('kstem_token_filter')
    assert test_kstem_filter.serialize() == {
        'kstem_token_filter': {
            'type': 'kstem'
        }
    }


def test_synonym_token_filter():
    test_synonym_filter = SynonymTokenFilter('synonym_token_filter', 'analysis/synonym.txt')
    assert test_synonym_filter.serialize() == {
        'synonym_token_filter' : {
            'type': 'synonym',
            'synonyms_path' : 'analysis/synonym.txt',
            'tokenizer': 'whitespace',
            'ignore_case': False
        }
    }

def test_reverse_token_filter():
    test_reverse_filter = ReverseTokenFiltrer('reverse_token_filter')
    assert test_reverse_filter.serialize() == {
        'reverse_token_filter': {
            'type' : 'reverse'
        }
    }

def test_elision_token_filter():
    test_elision_filter = ElisionTokenFilter('elision_token_filter', ["l", "m", "t", "qu", "n", "s", "j"])
    assert test_elision_filter.serialize() == {
        'elision_token_filter' : {
            'type': 'elision',
            'articles': ["l", "m", "t", "qu", "n", "s", "j"]
        }
    }

def test_truncate_token_filter():
    test_truncate_filter = TruncateTokenFilter('truncate_token_filter')
    assert test_truncate_filter.serialize() == {
        'truncate_token_filter': {
            'type': 'truncate',
            'length': 10
        }
    }

def test_unique_token_filter():
    test_unique_filter = UniqueTokenFilters('unique_token_filter')
    assert  test_unique_filter.serialize() == {
        'unique_token_filter': {
            'type': 'unique',
            'only_on_same_position': False
        }
    }

def test_pattern_capture_token_filter():
    test_patterns = ["(\\p{Ll}+|\\p{Lu}\\p{Ll}+|\\p{Lu}+)", "(\\d+)"]
    test_pattern_capture_filter = PatternCaptureTokenFilter('pattern_capture_filter', test_patterns)
    test_pattern_capture_filter.serialize() == {
        'pattern_capture_filter': {
            'type': 'pattern_capture',
            'patterns': test_patterns,
            'preserve_original': True
        }
    }

def test_pattern_replace_token_filter():
    test_pattern = "(\\p{Ll}+|\\p{Lu}\\p{Ll}+|\\p{Lu}+)"
    test_pattern_replace_filter = PatternReplaceTokenFilter('pattern_capture_filter', test_pattern)
    test_pattern_replace_filter.serialize() == {
        'pattern_capture_filter': {
            'type': 'pattern_capture',
            'patterns': test_pattern,
            'replacement': u''
        }
    }

def test_trim_token_filter():
    test_trim_filter = TrimTokenFilter('trim_token_filter')
    assert test_trim_filter.serialize() == {
        'trim_token_filter': {
            'type' : 'trim'
        }
    }

def test_limit_token_count_token_filter():
    test_limit_token_count_filter = LimitTokenCountTokenFilter('limit_token_count_filter')
    assert test_limit_token_count_filter.serialize() == {
        'limit_token_count_filter': {
            'type': 'limit',
            'max_token_count': 1,
            'consume_all_tokens': False
        }
    }

def test_common_grams_token_filter():
    test_common_grams_filter = CommonGramsTokenFilter('common_grams_filter', ["a", "an", "the"])
    assert test_common_grams_filter.serialize() == {
        'common_grams_filter' : {
            'type': 'common_grams',
            'common_words':  ["a", "an", "the"],
            'common_words_path': 'config/',
            'ignore_case': False,
            'query_mode': False
        }
    }

def test_delimited_payload_filter_token_filter():
    test_delimited_payload_filter = DelimitedPayloadTokenFilter('delimited_payload_filter')
    assert test_delimited_payload_filter.serialize() == {
        'delimited_payload_filter': {
            'type': 'delimited_payload_filter',
            'delimiter': '|',
            'encoding': 'float'
        }
    }

def test_keep_words_filter_token_filter():
    test_keep_words = [ "one", "two", "three"]
    test_keep_words_path = 'config/test_keep_words_file.txt'
    test_keep_words_filter = KeepWordsTokenFilter('keep_words_filter', test_keep_words, test_keep_words_path)
    assert test_keep_words_filter.serialize() == {
        'keep_words_filter': {
            'type': 'keep',
            'keep_words': test_keep_words,
            'keep_words_path': test_keep_words_path,
            'keep_words_case': False
        }
    }

def test_keep_types_filter_token_filter():
    test_keep_types = [ "<NUM>"]
    test_keep_types_filter = KeepTypesTokenFilter('keep_types_filter', test_keep_types)
    assert test_keep_types_filter.serialize() == {
        'keep_types_filter': {
            'type': 'keep_types',
            'types': test_keep_types,
        }
    }

def test_classic_token_filter():
    test_classic_filter = ClassicTokenFilter('classic_token_filter')
    assert test_classic_filter.serialize() == {
        'classic_token_filter': {
            'type' : 'classic'
        }
    }

def test_apostrophe_token_filter():
    test_apostrophe_filter = ApostropheTokenFilter('apostrophe_token_filter')
    assert test_apostrophe_filter.serialize() == {
        'apostrophe_token_filter': {
            'type' : 'apostrophe'
        }
    }


def test_decimal_digit_token_filter():
    test_decimal_digit_filter = DecimalDigitTokenFilter('decimal_digit_token_filter')
    assert test_decimal_digit_filter.serialize() == {
        'decimal_digit_token_filter': {
            'type' : 'decimal_digit'
        }
    }


def test_fingerprint_token_filter():
    test_fingerprint_filter = FingerprintTokenFilter('fingerprint_token_filter')
    assert test_fingerprint_filter.serialize() == {
        'fingerprint_token_filter': {
            'type' : 'fingerprint',
            'separator' : u' ',
            'max_output_size': 255
        }
    }

def test_minhash_token_filter():
    test_minhash_filter = MinhashTokenFilter('minhash_token_filter',)
    assert test_minhash_filter.serialize() == {
        'minhash_token_filter': {
            'type' : 'min_hash',
            'hash_count': 1,
            'bucket_count': 512,
            'hash_set_size' : 1,
            'with_rotation' : True
        }
    }
