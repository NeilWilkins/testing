# test_sinc2d.py
from sinc2d import *
from numpy import sin

def test_00():
    x = 0
    y = 0
    expected_value = 1.0
    calculated_value = sinc2d(x, y)
    assert calculated_value == expected_value

def test_01():
    x = 0
    y = 1
    expected_value = sin(1)
    calculated_value = sinc2d(x, y)
    assert calculated_value == expected_value

def test_10():
    x = 1
    y = 0
    expected_value = sin(1)
    calculated_value = sinc2d(x, y)
    assert calculated_value == expected_value

def test_11():
    x = 1
    y = 1
    expected_value = sin(1) ** 2
    calculated_value = sinc2d(x, y)
    assert calculated_value == expected_value
