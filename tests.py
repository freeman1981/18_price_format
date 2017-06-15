import pytest
from format_price import get_format_price


@pytest.mark.parametrize('test_input,expected', [
    ('123', '123'),
    ('1234', '1 234'),
    ('1234.00000', '1 234'),
    ('1234.00999', '1 234.01'),
    ('3245.000000', '3 245'),
])
def test_formatting(test_input, expected):
    assert get_format_price(test_input) == expected
