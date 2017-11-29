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

    def _serialize_token_filter_data(self):
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

    def _serialize_token_filter_data(self):
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

    def _serialize_token_filter_data(self):
        return dict(
            stopwords = self.stopwords,
            stopwords_path = self.stopwords_path,
            ignore_case = self.ignore_case,
            remove_trailing = self.remove_trailing
        )


class BaseWordDelimiterTokenFilter(TokenFilter):
    def __init__(self, name, type, protected_words, protected_words_path,
                 generate_word_parts=True, generate_number_parts=True,
                 catenate_words=False, catenate_numbers=False, catenate_all=False,
                 split_on_case_change=True, preserve_original =False,
                 split_on_numerics=True, stem_english_possessive=True):

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

        if protected_words_path:
            self.protected_words = []
            self.protected_words_path = protected_words_path
        else:
            assert isinstance(protected_words, list)
            self.protected_words = protected_words
            self.protected_words_path = u""

    def _serialize_token_filter_data(self):
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


class StemmerTokenFilter(TokenFilter):
    def __init__(self, name , language):
        super(StemmerTokenFilter, self).__init__(name, 'stemmer')
        self.languague = language

    def _serialize_token_filter_data(self):
        return dict(
            language = self.languague
        )


class StemmerOverrideTokenFilter(TokenFilter):
    def __init__(self, name , rules, rules_path):
        super(StemmerOverrideTokenFilter, self).__init__(name, 'stemmer_override')

        if rules_path:
            self.rules = []
            self.rules_path = rules_path
        else:
            assert isinstance(rules, list)
            self.rules = rules
            self.rules_path = u''

    def _serialize_token_filter_data(self):
        return dict(
            rules = self.rules,
            rules_path = self.rules_path
        )


class KeywordMarkerTokenFilter(TokenFilter):
    def __init__(self,name, keywords , keywords_path, keywords_pattern, ignore_case=False):
        super(KeywordMarkerTokenFilter, self).__init__(name, 'keyword_marker')

        if keywords_path:
            self.keywords = []
            self.keywords_path = keywords_path
        else:
            assert isinstance(keywords, list)
            self.keywords = keywords
            self.keywords_path = u''
        self.keywords_pattern = keywords_pattern
        self.ignore_case = ignore_case

    def _serialize_token_filter_data(self):
        return dict(
            keywords = self.keywords,
            keywords_path = self.keywords_path,
            keywords_pattern = self.keywords_pattern,
            ignore_case = self.ignore_case
        )


class ShingleMarkerTokenFilter(TokenFilter):
    def __init__(self,name, max_shingle_size=2, min_shingle_size=2,
                 output_unigrams=True, output_unigrams_if_no_shingles=False,
                 token_separator=u" ", filler_token=u"_"):
        super(ShingleMarkerTokenFilter, self).__init__(name, 'shingle')


        self.max_shingle_size= max_shingle_size
        self.min_shingle_size = min_shingle_size
        self.output_unigrams = output_unigrams
        self.output_unigrams_if_no_shingles = output_unigrams_if_no_shingles
        self.token_separator = token_separator
        self.filler_token = filler_token

    def _serialize_token_filter_data(self):
        return dict(
            max_shingle_size = self.max_shingle_size,
            min_shingle_size = self.min_shingle_size,
            output_unigrams = self.output_unigrams,
            output_unigrams_if_no_shingles = self.output_unigrams_if_no_shingles,
            token_separator = self.token_separator,
            filler_token = self.filler_token
        )

class KStemTokenFiltrer(TokenFilter):
    def __init__(self, name):
        super(KStemTokenFiltrer, self).__init__(name, 'kstem')


class SynonymTokenFilter(TokenFilter):
    def __init__(self, name, synonyms_path, tokenizer='whitespace', ignore_case=False):
        super(SynonymTokenFilter, self).__init__(name, 'synonym')
        self.synonyms_path = synonyms_path
        self.tokenizer = tokenizer
        self.ignore_case = ignore_case

    def _serialize_token_filter_data(self):
        return dict(
            synonyms_path = self.synonyms_path,
            tokenizer = self.tokenizer,
            ignore_case = self.ignore_case
        )

class ReverseTokenFiltrer(TokenFilter):
    def __init__(self, name):
        super(ReverseTokenFiltrer, self).__init__(name, 'reverse')


class ElisionTokenFilter(TokenFilter):
    def __init__(self, name, articles):
        super(ElisionTokenFilter, self).__init__(name, 'elision')
        self.articles = articles

    def _serialize_token_filter_data(self):
        return dict(
            articles = self.articles,
        )


class TruncateTokenFilter(TokenFilter):
    def __init__(self, name, length=10):
        super(TruncateTokenFilter, self).__init__(name, 'truncate')
        self.length = length

    def _serialize_token_filter_data(self):
        return dict(
            length = self.length
        )


class UniqueTokenFilters(TokenFilter):
    def __init__(self, name, only_on_same_position=False):
        super(UniqueTokenFilters, self).__init__(name, 'unique')
        self.only_on_same_position = only_on_same_position

    def _serialize_token_filter_data(self):
        return dict(
            only_on_same_position = self.only_on_same_position
        )


class PatternCaptureTokenFilter(TokenFilter):
    def __init__(self, name, patterns, preserve_original=True):
        super(PatternCaptureTokenFilter, self).__init__(name, 'pattern_capture')
        self.patterns = patterns
        self.preserve_original = preserve_original

    def _serialize_token_filter_data(self):
        return dict(
            patterns = self.patterns,
            preserve_original = self.preserve_original
        )


class PatternReplaceTokenFilter(TokenFilter):
    def __init__(self, name, pattern, replacement=None):
        super(PatternReplaceTokenFilter, self).__init__(name, 'pattern_replace')
        self.pattern = pattern,
        self.replacement = replacement

    def _serialize_token_filter_data(self):
        return dict(
            pattern = self.pattern,
            replacement = self.replacement or u''
        )


class TrimTokenFilter(TokenFilter):
    def __init__(self, name):
        super(TrimTokenFilter, self).__init__(name, 'trim')


class LimitTokenCountTokenFilter(TokenFilter):
    def __init__(self, name, max_token_count=1, consume_all_tokens=False):
        super(LimitTokenCountTokenFilter, self).__init__(name, 'limit')
        self.max_token_count = max_token_count
        self.consume_all_tokens = consume_all_tokens

    def _serialize_token_filter_data(self):
        return dict(
            max_token_count = self.max_token_count,
            consume_all_tokens = self.consume_all_tokens
        )

class CommonGramsTokenFilter(TokenFilter):
    def __init__(self, name, common_words, common_words_path,
                 ignore_case=False, query_mode=False):
        super(CommonGramsTokenFilter, self).__init__(name, 'common_grams')
        if common_words_path:
            self.common_words = []
            self.common_words_path = common_words_path
        else:
            assert isinstance(common_words, list)
            self.common_words = common_words
            self.common_words_path = u""

        self.ignore_case = ignore_case
        self.query_mode = query_mode

    def _serialize_token_filter_data(self):
        return dict(
            common_words = self.common_words,
            common_words_path = self.common_words_path,
            ignore_case = self.ignore_case,
            query_mode = self.query_mode
        )


class DelimitedPayloadTokenFilter(TokenFilter):
    def __init__(self, name, delimiter='|', encoding='float'):
        super(DelimitedPayloadTokenFilter, self).__init__(name, 'delimited_payload_filter')
        self.delimiter = delimiter
        self.encoding = encoding

    def _serialize_token_filter_data(self):
        return dict(
            delimiter = self.delimiter,
            encoding = self.encoding
        )

class KeepWordsTokenFilter(TokenFilter):
    def __init__(self, name, keep_words, keep_words_path, keep_words_case=False):
        super(KeepWordsTokenFilter, self).__init__(name, 'keep')
        self.keep_words = keep_words
        self.keep_words_path = keep_words_path
        self.keep_words_case = keep_words_case

    def _serialize_token_filter_data(self):
        return dict(
            keep_words = self.keep_words,
            keep_words_path = self.keep_words_path,
            keep_words_case = self.keep_words_case
        )


class KeepTypesTokenFilter(TokenFilter):
    def __init__(self, name, types):
        super(KeepTypesTokenFilter, self).__init__(name, 'keep_types')
        self.types = types

    def _serialize_token_filter_data(self):
        return dict(
            types = self.types,
        )

class ClassicTokenFilter(TokenFilter):
    def __init__(self, name):
        super(ClassicTokenFilter, self).__init__(name, 'classic')


class ApostropheTokenFilter(TokenFilter):
    def __init__(self, name):
        super(ApostropheTokenFilter, self).__init__(name, 'apostrophe')


class DecimalDigitTokenFilter(TokenFilter):
    def __init__(self, name):
        super(DecimalDigitTokenFilter, self).__init__(name, 'decimal_digit')


class FingerprintTokenFilter(TokenFilter):
    def __init__(self, name, separator= u' ', max_output_size=255):
        super(FingerprintTokenFilter, self).__init__(name, 'fingerprint')
        self.separator = separator
        self.max_output_size= max_output_size

    def _serialize_token_filter_data(self):
        return dict(
            separator = self.separator,
            max_output_size = self.max_output_size
        )


class MinhashTokenFilter(TokenFilter):
    def __init__(self, name, hash_count=1, bucket_count=512,
                 hash_set_size=1):
        super(MinhashTokenFilter, self).__init__(name, 'min_hash')
        self.hash_count = hash_count
        self.bucket_count= bucket_count
        self.hash_set_size= hash_set_size
        self.with_rotation= True if self.hash_set_size == 1 else False


    def _serialize_token_filter_data(self):
        return dict(
            hash_count = self.hash_count,
            bucket_count = self.bucket_count,
            hash_set_size = self.hash_set_size,
            with_rotation = self.with_rotation
        )
