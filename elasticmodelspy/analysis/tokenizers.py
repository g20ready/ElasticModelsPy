#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.analysis.base import AnalysisSerializable

class Tokenizer(AnalysisSerializable):
    def __init__(self, name, type):
        super(Tokenizer, self).__init__(name)
        self.type = type

    def serialize_data(self):
        data = dict(
            type=self.type
        )
        data.update(self._serialize_tokenizer_data())
        return data

    def _serialize_tokenizer_data(self):
        return dict()


class StandardTokenizer(Tokenizer):
    """
    The standard tokenizer provides grammar based tokenization (based on the Unicode Text Segmentation algorithm,
    as specified in Unicode Standard Annex #29) and works well for most languages.
    """
    def __init__(self, name, max_token_length=255):
        super(StandardTokenizer, self).__init__(name, 'standard')
        self.max_token_length = max_token_length

    def _serialize_tokenizer_data(self):
        return dict(
            max_token_length=self.max_token_length
        )


class NGramTokenizer(Tokenizer):
    """
    The ngram tokenizer first breaks text down into words whenever it encounters one of a list of specified characters,
    then it emits N-grams of each word of the specified length.

    N-grams are like a sliding window that moves across the word - a continuous sequence of characters of
    the specified length. They are useful for querying languages that don’t use spaces or that have long compound words,
    like German.
    """
    def __init__(self, name, min_gram, max_gram, token_chars=list()):
        super(NGramTokenizer, self).__init__(name, 'ngram')
        self.min_gram = min_gram
        self.max_gram = max_gram
        self.token_chars = token_chars

    def _serialize_tokenizer_data(self):
        return dict(
            min_gram=self.min_gram,
            max_gram=self.max_gram,
            token_chars=self.token_chars
        )

class EdgeNGramTokenizer(Tokenizer):
    """
    The edge_ngram tokenizer first breaks text down into words whenever it encounters one of a list of specified
    characters, then it emits N-grams of each word where the start of the N-gram is anchored to the beginning of the
    word.

    Edge N-Grams are useful for search-as-you-type queries.
    """
    def __init__(self, name, min_gram, max_gram, token_chars=list()):
        super(EdgeNGramTokenizer, self).__init__(name, 'edge_ngram')
        self.min_gram = min_gram
        self.max_gram = max_gram
        self.token_chars = token_chars

    def _serialize_tokenizer_data(self):
        return dict(
            min_gram=self.min_gram,
            max_gram=self.max_gram,
            token_chars=self.token_chars
        )

