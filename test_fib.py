# test_fib.py
# Testing module for fib.py

from fib import *

def test_zero():
    input = 0
    expected_value = 1
    calculated_value = fib(input)
    assert (calculated_value == expected_value)

def test_one():
    input = 1
    expected_value = 1
    calculated_value = fib(input)
    assert (calculated_value == expected_value)

def test_three():
    input = 3
    expected_value = 3
    calculated_value = fib(input)
    assert (calculated_value == expected_value)

def test_float():
    input = 2.0
    expected_value = 2
    calculated_value = fib(input)
    assert (calculated_value == expected_value)
