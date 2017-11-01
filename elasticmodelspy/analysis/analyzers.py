#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.analysis.base import AnalysisSerializable

class Analyzer(AnalysisSerializable):
    def __init__(self, name, tokenizer, token_filters, char_filters):
        super(Analyzer, self).__init__(name)


    def __serialize__(self):
        data = dict(

        )
        return dict()

    def __get_char_filters__(self):
        """
        Char filter settings this analyzer references.

        :return:        Dictionary mapping char filter names to char filter settings.
        """
        return dict()

    def __get_token_filters__(self):
        """
        Token filter settings this analyzer references.

        :return:        Dictionary mapping token filter names to token filter settings.
        """
        return dict()

    def __get_tokenizers__(self):
        """
        Returns the tokenizer settings this analyzer references.

        :return:        Dictionary mapping tokenizer names to tokenizer settings.
        """
        return dict()
