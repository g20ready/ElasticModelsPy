from elasticpymodels.analysis.base import AnalysisSerializable

class Analyzer(AnalysisSerializable):
    def __init__(self, name, tokenizer, filters):
        super(Analyzer, self).__init__(name)
