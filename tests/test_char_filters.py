from elasticmodelspy.analysis.char_filters import CharFilter, HtmlCharFilter, MappingCharFilter, PatternReplaceCharFilter

def test_char_filter():
    char_filter = CharFilter('char_filter', 'some_type')
    assert char_filter.serialize() == {
        'char_filter': {
            'type': 'some_type'
        }
    }

def test_html_char_filter():
    html_char_filter = HtmlCharFilter('html_char_filter', ['a', 'p', 'b'])
    assert html_char_filter.serialize() == {
        'html_char_filter': {
            'type': 'html_strip',
            'escaped_tags': ['a', 'p', 'b']
        }
    }

def test_mapping_char_filter():
    mapping_char_filter = MappingCharFilter('mapping_char_filter', mappings=['I => 1', 'II => 2'])
    assert mapping_char_filter.serialize() == {
        'mapping_char_filter': {
            'type': 'mapping',
            'mappings': ['I => 1', 'II => 2']
        }
    }

    mapping_path_char_filter = MappingCharFilter('mapping_path_char_filter', mappings_path='/elastic/mappings.txt')
    assert mapping_path_char_filter.serialize() == {
        'mapping_path_char_filter': {
            'type': 'mapping',
            'mappings_path': '/elastic/mappings.txt'
        }
    }

def test_pattern_replace_char_filter():
    pattern_replace_char_filter = PatternReplaceCharFilter('pattern_replace_char_filter',
                                                           '(?<=\\p{Lower})(?=\\p{Upper})',
                                                           ' ')
    assert pattern_replace_char_filter.serialize() == {
        'pattern_replace_char_filter': {
            'type': 'pattern_replace',
            'replacement': ' ',
            'pattern': '(?<=\\p{Lower})(?=\\p{Upper})'
        }
    }

