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
