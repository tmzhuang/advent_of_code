import numpy as np

from day03.utils2 import *


def test_intersect():
    s1 = (np.array([0,3]), np.array([3,0]))
    s2 = (np.array([2,1]), np.array([0,4]))
    expected = np.array([2,3])
    ans = intersect(s1,s2)
    assert np.array_equal(ans, expected)


def test_intersect_no_intersect():
    s1 = (np.array([0,8]), np.array([3,0]))
    s2 = (np.array([2,1]), np.array([0,4]))
    expected = np.array([2,3])
    ans = intersect(s1,s2)
    assert ans is None
