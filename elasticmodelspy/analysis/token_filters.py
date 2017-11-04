#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from elasticmodelspy.analysis.base import AnalysisSerializable


class TokenFilter(AnalysisSerializable):
    def __init__(self, name, type):
        super(TokenFilter, self).__init__(name)
        self.type = type

    def serialize_data(self):
        data = dict(
            type=self.type
        )
        data.update(self._serialize_token_filter_data())
        return data

    def _serialize_token_filter_data(self):
        return dict()


class AsciiFoldTokenFilter(TokenFilter):
    def __init__(self, name, preserve_original=False):
        super(AsciiFoldTokenFilter, self).__init__(name, 'asciifolding')
        self.preserve_original=preserve_original

    def _serialize_token_filter_data(self):
        return dict(
            preserve_original=self.preserve_original
        )


class LengthTokenFilter(TokenFilter):
    def __init__(self, name, min=0, max=sys.maxsize):
        # TODO sys.maxsize is not the best possible value but it will do the job
        super(LengthTokenFilter, self).__init__(name, 'length')
        self.min = min
        self.max = max

    def _serialize_token_filter_data(self):
        return dict(
            min=self.min,
            max=self.max
        )


class LanguageTokenFilter(TokenFilter):
    def __init__(self, name, type, language):
        super(LanguageTokenFilter, self).__init__(name, type)
        self.language = language

    def _serialize_token_filter_data(self):
        return dict(
            language=self.language
        )


class LowercaseTokenFilter(LanguageTokenFilter):
    def __init__(self, name, language):
        super(LowercaseTokenFilter, self).__init__(name, 'lowercase', language)


class UppercaseTokenFilter(LanguageTokenFilter):
    def __init__(self, name, language):
        super(UppercaseTokenFilter, self).__init__(name, 'uppercase', language)


class StopwordsTokenFilter(TokenFilter):
    def __init__(self, name, stopwords):
        super(StopwordsTokenFilter, self).__init__(name, 'stopwords')
        self.stopwords = stopwords

    def _serialize_token_filter_data(self):
        return dict(
            stopwords=self.stopwords
        )


class NgramTokenFilter(TokenFilter):
    def __init__(self, name, min_gram=1, max_gram=2):
        super(NgramTokenFilter, self).__init__(name, 'nGram')
        self.min_gram = min_gram
        self.max_gram = max_gram

    def __filter_data__(self):
        return dict(
            min_gram=self.min_gram,
            max_gram=self.max_gram
        )


class EdgeNgramTokenFilter(TokenFilter):
    def __init__(self, name, min_gram=1, max_gram=2, side='front'):
        super(EdgeNgramTokenFilter, self).__init__(name, 'edgeNGram')
        self.side = side
        self.min_gram = min_gram
        self.max_gram = max_gram

    def __filter_data__(self):
        return dict(
            min_gram=self.min_gram,
            max_gram=self.max_gram,
            side=self.side
        )


class StopTokenFilter(TokenFilter):
    def __init__(self, name, stopwords, stopwords_path,
                 ignore_case=False, remove_trailing=True):
        super(StopTokenFilter, self).__init__(name, 'stop')
        self.stopwords = stopwords
        self.stopwords_path = stopwords_path
        self.ignore_case = ignore_case
        self.remove_trailing = remove_trailing

    def __filter_data__(self):
        return dict(
            stopwords = self.stopwords,
            stopwords_path = self.stopwords_path,
            ignore_case = self.ignore_case,
            remove_trailing = self.remove_trailing
        )


class BaseWordDelimiterTokenFilter(TokenFilter):
    def __init__(self, name, type, protected_words, generate_word_parts=True, generate_number_parts=True,
                 catenate_words=False, catenate_numbers=False, catenate_all=False,
                 split_on_case_change=True, preserve_original =False,
                 split_on_numerics=True, stem_english_possessive=True,
                 protected_words_path='config/' ):

        super(BaseWordDelimiterTokenFilter, self).__init__(name, type)
        self.generate_word_parts = generate_word_parts
        self.generate_number_parts = generate_number_parts
        self.catenate_words = catenate_words
        self.catenate_numbers = catenate_numbers
        self.catenate_all = catenate_all
        self.split_on_case_change = split_on_case_change
        self.preserve_original = preserve_original
        self.split_on_numerics = split_on_numerics
        self.stem_english_possessive = stem_english_possessive

        if protected_words:
            assert isinstance(protected_words, list)
            self.protected_words = protected_words
            self.protected_words_path = None
        else:
            self.protected_words_path = protected_words_path

    def __filter_data__(self):
        return dict(
            generate_word_parts = self.generate_word_parts,
            generate_number_parts = self.generate_number_parts,
            catenate_words = self.catenate_words,
            catenate_numbers = self.catenate_numbers,
            catenate_all = self.catenate_all,
            split_on_case_change = self.split_on_case_change,
            preserve_original = self.preserve_original,
            split_on_numerics = self.split_on_numerics,
            stem_english_possessive = self.stem_english_possessive,
            protected_words_path = self.protected_words_path,
            protected_words = self.protected_words
        )

class WordDelimiterTokenFilter(BaseWordDelimiterTokenFilter):
    def __init__(self, name, **kwargs):
        super(WordDelimiterTokenFilter, self).__init__(name, 'word_delimiter', **kwargs)


class WordDelimeterGraphTokenFilter(BaseWordDelimiterTokenFilter):
    def __init__(self, name, **kwargs):
        super(WordDelimeterGraphTokenFilter, self).__init__(name, 'word_delimiter_graph',
                                                            preserve_original=True,
                                                            catenate_words=True,
                                                            catenate_numbers=True,
                                                            catenate_all=True, **kwargs)


class SynonymTokenFilter(TokenFilter):
    def __init__(self, name, synonyms_path='analysis/synonym.txt', tokenizer='whitespace', ignore_case=False):
        super(SynonymTokenFilter, self).__init__(name, 'synonym')
        self.synonyms_path = synonyms_path
        self.tokenizer = tokenizer
        self.ignore_case = ignore_case

    def __filter_data__(self):
        return dict(
            synonyms_path = self.synonyms_path,
            tokenizer = self.tokenizer,
            ignore_case = self.ignore_case
        )
