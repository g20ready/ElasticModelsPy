#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticmodelspy.analysis.base import Serializable

class ElasticBaseType(Serializable):
    def __init__(self, name):
        super(ElasticBaseType, self).__init__(name)

    def __analysis_data__(self):
        return dict()


class Text(ElasticBaseType):

    field_data = False
    index = True
    analyzer = None

    def __init__(self, field_data, index, analyzer):
        super(Text, self).__init__()
        self.field_data = field_data
        self.index = self.__validate_index(index)
        self.analyzer = self.__validate_analyzer(analyzer)

    def __validate_index(self, index):
        # TODO validate index
        return index

    def __validate_analyzer(self, analyzer):
        if not (isinstance(self.analyzer, BaseAnalyzer) or isinstance(self.analyzer, str)):
            raise TypeError('Analyzer ({0}) can only be of type elasticmodelspy.analyzers.BaseAnalyzer or str.'.format(analyzer))
        return analyzer


    def __repr__(self):
        return "[ field_data : {0}, index : {1}, analyzer : {2} ]".format(self.field_data, self.index, self.analyzer)


class Keyword(ElasticBaseType):
    pass

class Numeric(ElasticBaseType):
    pass

class Date(ElasticBaseType):
    pass

class Boolean(ElasticBaseType):
    pass

class Binary(ElasticBaseType):
    pass

class Range(ElasticBaseType):
    pass

class Array(ElasticBaseType):
    pass

class Nested(ElasticBaseType):
    pass

class GeoPoint(ElasticBaseType):
    pass

class GeoShape(ElasticBaseType):
    pass

class Completion(ElasticBaseType):
    pass

