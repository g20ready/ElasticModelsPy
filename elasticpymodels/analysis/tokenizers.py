from elasticpymodels.analysis.base import AnalysisSerializable

class Tokenizer(AnalysisSerializable):
    def __init__(self, name, type):
        super(Tokenizer, self).__init__(name)
        self.type = type

    def __analysis_data__(self):
        return dict(
            type=self.type
        )


class StandardTokenizer(Tokenizer):
    """
    The standard tokenizer provides grammar based tokenization (based on the Unicode Text Segmentation algorithm,
    as specified in Unicode Standard Annex #29) and works well for most languages.
    """
    def __init__(self, name, max_token_length=255):
        super(StandardTokenizer, self).__init__(name, 'standard')
        self.max_token_length = max_token_length

    def __tokenizer_data__(self):
        return dict(
            max_token_length=5
        )
