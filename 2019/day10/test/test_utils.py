import os

from day10.utils import *

def test_max_los():
    a = get_array('input1.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    assert max_los(los) == 8

def test_max_los2():
    a = get_array('input2.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    assert max_los(los) == 35

def test_max_los3():
    a = get_array('input3.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    assert max_los(los) == 41

def test_max_los4():
    a = get_array('input4.txt')
    asteroids = get_asteroids(a)
    los = count_los(asteroids)
    assert max_los(los) == 210
