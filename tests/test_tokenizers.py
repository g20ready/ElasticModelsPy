#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `elasticmodelspy.analysis`"""

from elasticmodelspy.analysis.tokenizers import Tokenizer, StandardTokenizer, NGramTokenizer, EdgeNGramTokenizer

def test_tokenizer():
    tokenizer = Tokenizer('tokenizer', 'standard')
    assert tokenizer.__serialize__() == {
        'tokenizer': {
            'type': 'standard'
        }
    }

def test_standard_tokenizer():
    standard_tokenizer = StandardTokenizer('standard_tokenizer', max_token_length=200)
    assert standard_tokenizer.__serialize__() == {
        'standard_tokenizer': {
            'type': 'standard',
            'max_token_length': 200
        }
    }

def test_ngram_tokenizer():
    ngram_tokenizer = NGramTokenizer('ngram', 2, 10)
    assert ngram_tokenizer.__serialize__() == {
        'ngram': {
            'type': 'ngram',
            'min_gram': 2,
            'max_gram': 10,
            'token_chars': []
        }
    }

def test_edge_ngram_tokenizer():
    edge_ngram_tokenizer = EdgeNGramTokenizer('edge_ngram', 2, 12)
    assert edge_ngram_tokenizer.__serialize__() == {
        'edge_ngram': {
            'type': 'edge_ngram',
            'min_gram': 2,
            'max_gram': 12,
            'token_chars': []
        }
    }

