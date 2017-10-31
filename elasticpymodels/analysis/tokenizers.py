from elasticpymodels.analysis.base import AnalysisSerializable

class Tokenizer(AnalysisSerializable):
    def __init__(self, name):
        super(Tokenizer, self).__init__(name)
