import pytest
from format_price import get_format_price

@pytest.mark.parametrize('test_input,expected', [
    ('123', '42'),
    ('123', '42'),
    ('123', '42'),
    ('123', '42'),
])
def test_formatting(test_input, expected):
    assert get_format_price(test_input) == expected
