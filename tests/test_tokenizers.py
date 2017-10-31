from elasticpymodels.analysis.tokenizers import Tokenizer, StandardTokenizer

def test_tokenizer():
    tokenizer = Tokenizer('standard_tokenizer', 'standard')
    assert tokenizer.name == 'standard_tokenizer'
    assert  tokenizer.type == 'standard'

    serialized = tokenizer.__serialize__()
    assert 'standard_tokenizer' in serialized.keys()

    serialized_data = serialized.get('standard_tokenizer')
    assert len(serialized_data.keys()) == 1
    assert serialized_data.get('type') == 'standard'


def test_standard_tokenizer():
    standard_tokenizer = StandardTokenizer('s', )

