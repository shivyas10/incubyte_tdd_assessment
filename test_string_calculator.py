import pytest
from calculator import Calculator

def test_empty_string():
    assert Calculator.add('') == 0

def test_single_number():
    assert Calculator.add('1') == 1

def test_two_numbers():
    assert Calculator.add('1,2') == 3

def test_unknown_amount_of_numbers():
    assert Calculator.add('1,2,3,4,5') == 15

def test_newline_delimiter():
    assert Calculator.add('1\n2,3') == 6

def test_custom_delimiter():
    assert Calculator.add('//;\n1;2') == 3

def test_negative_number_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed -2"):
        Calculator().add("1,-2")

def test_multiple_negative_numbers_exception():
    with pytest.raises(ValueError, match="negative numbers not allowed -2, -3"):
        Calculator.add("//;\n1;-2;-3")
