#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.base import Serializable

class CharFilter(Serializable):
    def __init__(self, name, type):
        super(CharFilter, self).__init__(name)
        self.type = type

    def serialize_data(self):
        data = dict(
            type=self.type
        )
        data.update(self._serialize_char_filter_data())
        return data

    def _serialize_char_filter_data(self):
        return dict()

class HtmlCharFilter(CharFilter):
    """
    The html_strip character filter strips HTML elements from the text and replaces HTML entities with their decoded
    value (e.g. replacing &amp; with &).
    """
    def __init__(self, name, escaped_tags=list()):
        super(HtmlCharFilter, self).__init__(name, 'html_strip')
        self.escaped_tags = escaped_tags

    def _serialize_char_filter_data(self):
        return dict(
            escaped_tags=self.escaped_tags
        )


class MappingCharFilter(CharFilter):
    """
    The mapping character filter accepts a map of keys and values. Whenever it encounters a string of characters that
    is the same as a key, it replaces them with the value associated with that key.

    Matching is greedy; the longest pattern matching at a given point wins. Replacements are allowed to be the empty
    string.
    """
    def __init__(self, name, mappings=list(), mappings_path=None):
        """
        Either mapping
        :param name:
        :param mappings:        A array of mappings, with each element having the form key => value.
        :param mappings_path:   A path, either absolute or relative to the config directory, to a UTF-8 encoded text
                                mappings file containing a key => value mapping per line. If both specified mappings
                                path has priority.
        """
        super(MappingCharFilter, self).__init__(name, 'mapping')
        self.mappings = mappings
        self.mappings_path = mappings_path

    def _serialize_char_filter_data(self):
        if self.mappings_path:
            return dict(
                mappings_path=self.mappings_path
            )
        return dict(
            mappings=self.mappings
        )



class PatternReplaceCharFilter(CharFilter):
    """
    The pattern_replace character filter uses a regular expression to match characters which should be replaced with
    the specified replacement string. The replacement string can refer to capture groups in the regular expression.
    """
    def __init__(self, name, pattern, replacement, flags=None):
        super(PatternReplaceCharFilter, self).__init__(name, 'pattern_replace')
        self.pattern = pattern
        self.replacement = replacement
        self.flag = flags

    def _serialize_char_filter_data(self):
        data = dict(
            pattern = self.pattern,
            replacement = self.replacement
        )
        if self.flag:
            data['flag'] = self.flag
        return data


