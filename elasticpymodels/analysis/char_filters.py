from elasticpymodels.analysis.base import AnalysisSerializable

class CharFilter(AnalysisSerializable):

    def __init__(self, name):
        super(CharFilter, self).__init__(name)


class HtmlCharFilter(CharFilter):
    """
    The html_strip character filter strips HTML elements from the text and replaces HTML entities with their decoded
    value (e.g. replacing &amp; with &).
    """
    pass


class MappingCharFilter(CharFilter):
    """
    The mapping character filter accepts a map of keys and values. Whenever it encounters a string of characters that
    is the same as a key, it replaces them with the value associated with that key.

    Matching is greedy; the longest pattern matching at a given point wins. Replacements are allowed to be the empty
    string.
    """
    pass


class PatternReplaceCharFilter(CharFilter):
    """
    The pattern_replace character filter uses a regular expression to match characters which should be replaced with
    the specified replacement string. The replacement string can refer to capture groups in the regular expression.
    """
    pass
