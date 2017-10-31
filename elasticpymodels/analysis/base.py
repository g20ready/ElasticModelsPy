from elasticpymodels.base import Serializable

class AnalysisSerializable(Serializable):
    def __init__(self, name):
        super(AnalysisSerializable, self).__init__()
        self.name = name

    def __serialize__(self):
        return {
            self.name: self.__analysis_data__()
        }

    def __analysis_data__(self):
        raise NotImplemented()
