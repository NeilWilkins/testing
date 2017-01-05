from mean import *

def test_ints():
    input = [1, 2, 3, 4, 5]
    calculated_value = mean(input)
    expected_value = 3
    assert calculated_value == expected_value, "Calculated value did not equal expected value"

def test_floats():
    input = [1.0, 2.0, 3.0]
    calculated_value = mean(input)
    expected_value = 2.0
    assert calculated_value == expected_value, "Calculated value did not equal expected value"

def test_empty():
    input = []
    calculated_value = mean(input)
    expected_value = 0
    assert calculated_value == expected_value, "Calculated value did not equal expected value"

def test_not_numbers():
    input = ['a', 'b', 'c']
    calculated_value = mean(input)
    expected_value = 0
    assert calculated_value == expected_value, "Calculated value did not equal expected value"
