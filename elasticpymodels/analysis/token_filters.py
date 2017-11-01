import sys

from elasticpymodels.analysis.base import AnalysisSerializable


class TokenFilter(AnalysisSerializable):
    def __init__(self, name, type):
        super(TokenFilter, self).__init__(name)
        self.type = type

    def __analysis_data__(self):
        data = dict(
            type=self.type
        )
        data.update(self.__token_filter_data__())
        return data

    def __token_filter_data__(self):
        return dict()


class AsciiFoldTokenFilter(TokenFilter):
    def __init__(self, name, preserve_original=False):
        super(AsciiFoldTokenFilter, self).__init__(name, 'asciifolding')
        self.preserve_original=preserve_original

    def __token_filter_data__(self):
        return dict(
            preserve_original=self.preserve_original
        )


class LengthTokenFilter(TokenFilter):
    def __init__(self, name, min=0, max=sys.maxsize):
        # TODO sys.maxsize is not the best possible value but it will do the job
        super(LengthTokenFilter, self).__init__(name, 'length')
        self.min = min
        self.max = max

    def __token_filter_data__(self):
        return dict(
            min=self.min,
            max=self.max
        )


class LanguageTokenFilter(TokenFilter):
    def __init__(self, name, type, language):
        super(LanguageTokenFilter, self).__init__(name, type)
        self.language = language

    def __token_filter_data__(self):
        return dict(
            language=self.language
        )


class LowercaseTokenFilter(LanguageTokenFilter):
    def __init__(self, name, language):
        super(LowercaseTokenFilter, self).__init__(name, 'lowercase', language)


class StopwordsTokenFilter(TokenFilter):
    def __init__(self, name, stopwords):
        super(StopwordsTokenFilter, self).__init__(name, 'stopwords')
        self.stopwords = stopwords

    def __token_filter_data__(self):
        return dict(
            stopwords=self.stopwords
        )


