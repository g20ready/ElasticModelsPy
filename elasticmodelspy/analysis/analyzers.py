#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.analysis.base import AnalysisSerializable

from elasticmodelspy.analysis.tokenizers import Tokenizer

class Analyzer(AnalysisSerializable):
    def __init__(self, name, type):
        super(Analyzer, self).__init__(name)
        self.type = type

    def __serialize__(self):
        data = dict(
            type=self.type
        )
        data.update(self.__analyzer_data__())
        return data

    def __analyzer_data__(self):
        return dict()


class StandardAnalyzer(Analyzer):
    """
    The standard analyzer is the default analyzer which is used if none is specified. It provides grammar based
    tokenization (based on the Unicode Text Segmentation algorithm, as specified in Unicode Standard Annex #29) and
    works well for most languages.
    """
    def __init__(self, name, max_token_length=None, stopwords=None, stopwords_path=None):
        """

        :param name:                    Name of the analyzer

        :param max_token_length:        The maximum token length. If a token is seen that exceeds this length then it
                                        is split at max_token_length intervals. Defaults to 255.

        :param stopwords:               A pre-defined stop words list like _english_ or an array containing a list of
                                        stop words. Defaults to _none_.

        :param stopwords_path:          The path to a file containing stop words.
        """
        super(StandardAnalyzer, self).__init__(name, 'standard')
        self.max_token_length = max_token_length
        self.stopwords = stopwords
        self.stopwords_path = stopwords_path

    def __analyzer_data__(self):
        data = dict()
        if self.max_token_length:
            data['max_token_length'] = self.max_token_length
        if self.stopwords:
            data['stopwords'] = self.stopwords
        elif self.stopwords_path:
            data['stopwords_path'] = self.stopwords_path
        return data


class SimpleAnalyzer(Analyzer):
    """
    The simple analyzer breaks text into terms whenever it encounters a character which is not a letter. All terms are
    lower cased.
    """
    def __init__(self, name):
        """
        :param name:            Name of the analyzer.
        """
        super(SimpleAnalyzer, self).__init__(name, 'simple')


class WhiteSpaceAnalyzer(Analyzer):
    """
    The whitespace analyzer breaks text into terms whenever it encounters a whitespace character.
    """
    def __init__(self, name):
        """
        :param name:            Name of the analyzer.
        """
        super(WhiteSpaceAnalyzer, self).__init__(name, 'whitespace')


class StopAnalyzer(Analyzer):
    """
    The stop analyzer is the same as the simple analyzer but adds support for removing stop words. It defaults to using
    the _english_ stop words.
    """
    def __init__(self, name, stopwords=None, stopwords_path=None):
        super(StopAnalyzer, self).__init__(name, 'stop')
        self.stopwords = stopwords
        self.stopwords_path = stopwords_path

    def __analyzer_data__(self):
        data = dict()
        if self.stopwords:
            data['stopwords'] = self.stopwords
        elif self.stopwords_path:
            data['stopwords_path'] = self.stopwords_path
        return data


class KeywordAnalyzer(Analyzer):
    """
    The keyword analyzer is a “noop” analyzer which returns the entire input string as a single token.
    """
    def __init__(self, name):
        super(KeywordAnalyzer, self).__init__(name, 'keyword')


class PatternAnalyzer(Analyzer):
    """
    The pattern analyzer uses a regular expression to split the text into terms. The regular expression should match the
    token separators not the tokens themselves. The regular expression defaults to \W+ (or all non-word characters).
    """
    def __init__(self, name, pattern, flags=None, lowercase=True, stopwords=None, stopwords_path=None):
        """

        :param name:            Name of the analyzer
        :param pattern:         A Java regular expression, defaults to \W+.
        :param flags:           Java regular expression flags. Flags should be pipe-separated, eg
                                "CASE_INSENSITIVE|COMMENTS".
        :param lowercase:       Should terms be lowercased or not. Defaults to true.
        :param stopwords:       A pre-defined stop words list like _english_ or an array containing a list of stop
                                words. Defaults to _none_.
        :param stopwords_path:  The path to a file containing stop words.
        """
        super(PatternAnalyzer, self).__init__(name, 'pattern')
        self.pattern = pattern
        self.flags = flags
        self.lowercase = lowercase
        self.stopwords = stopwords
        self.stopwords_path = stopwords_path

    def __analyzer_data__(self):
        data = dict(
            pattern=self.pattern,
            lowercase=self.lowercase
        )
        if self.flags:
            data['flags'] = self.flags
        if self.stopwords:
            data['stopwords'] = self.stopwords
        elif self.stopwords_path:
            data['stopwords_path'] = self.stopwords_path
        return data


class CustomAnalyzer(Analyzer):
    """
    When the built-in analyzers do not fulfill your needs, you can create a custom analyzer which uses the appropriate
    combination of:

    * zero or more character filters
    * a tokenizer
    * zero or more token filters.
    """
    def __init__(self, name, tokenizer, char_filters, token_filters):
        """

        :param name:
        :param tokenizer:
        :param char_filters:
        :param token_filters:
        """
        super(CustomAnalyzer, self).__init__(name, 'custom')
        self.tokenizer = self.__validate_tokenizer__(tokenizer)
        self.char_filters = self.__validate_char_filters__(char_filters)
        self.token_filters = self.__validate_token_filters__(token_filters)

    def __validate_tokenizer__(self, tokenizer):
        if not isinstance(tokenizer, str) and not isinstance(tokenizer, Tokenizer):
            raise ValueError('Argument tokenizer should be of class str or elasticmodelspy.analysis.tokenizers.Tokenizer.')
        return tokenizer

    def __validate_char_filters__(self, char_filters):
        return None

    def __validate_token_filters__(self, token_filters):
        return None


    # def __get_char_filters__(self):
    #     """
    #     Char filter settings this analyzer references.
    #
    #     :return:        Dictionary mapping char filter names to char filter settings.
    #     """
    #     return dict()
    #
    # def __get_token_filters__(self):
    #     """
    #     Token filter settings this analyzer references.
    #
    #     :return:        Dictionary mapping token filter names to token filter settings.
    #     """
    #     return dict()
    #
    # def __get_tokenizers__(self):
    #     """
    #     Returns the tokenizer settings this analyzer references.
    #
    #     :return:        Dictionary mapping tokenizer names to tokenizer settings.
    #     """
    #     return dict()
