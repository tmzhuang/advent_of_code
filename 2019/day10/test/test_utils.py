import os

from day10.utils import *

def test_count_los():
    a = get_array('input1.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    breakpoint()
