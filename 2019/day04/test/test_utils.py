import numpy as np
from day04.utils import *

def test_get_digits():
    ans = get_digits(1234)
    expected = np.array([1,2,3,4])
    assert np.array_equal(ans, expected)

def test_get_digits2():
    ans = get_digits(1)
    expected = np.array([1])
    assert np.array_equal(ans, expected)

def test_get_digits3():
    ans = get_digits(0)
    expected = np.array([0])
    assert np.array_equal(ans, expected)

def test_get_array():
    ans = get_array(39,41)
    expected = np.array([[3,9], [4,0], [4,1]])
    assert np.array_equal(ans, expected)

def test_reduce_bool_row():
    n = 112233
    a = get_digits(n)
    b = np.diff(a) == 0
    assert reduce_bool_row(b)

def test_reduce_bool_row2():
    n = 123444
    a = get_digits(n)
    b = np.diff(a) == 0
    assert not reduce_bool_row(b)

def test_reduce_bool_row3():
    n = 111122
    a = get_digits(n)
    b = np.diff(a) == 0
    assert reduce_bool_row(b)
