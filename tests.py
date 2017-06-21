import pytest
from format_price import get_format_price


class TestClass:
    pass


@pytest.mark.parametrize('test_input,expected', [
    ('123', '123'),
    ('1234', '1 234'),
    ('1234.00000', '1 234'),
    ('1234.00999', '1 234.01'),
    ('3245.000000', '3 245'),
])
def test_formatting(test_input, expected):
    assert get_format_price(test_input) == expected


@pytest.mark.parametrize('test_input,exception', [
    (set(), TypeError),
    (list(), TypeError),
    (dict(), TypeError),
    (None, TypeError),
    (TestClass(), TypeError),
])
def test_exceptions(test_input, exception):
    with pytest.raises(exception):
        get_format_price(test_input)
