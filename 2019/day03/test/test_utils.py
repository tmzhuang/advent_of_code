from day03.utils import *


def test_attach_R3():
    init = [(1,1),(2,2)]
    move = 'R3'
    expected = [(1,1),(2,2),(3,2),(4,2),(5,2)]
    res = attach(move, init)
    assert res == expected

def test_attach_D2():
    init = [(1,1),(2,-2)]
    move = 'D2'
    expected = [(1,1),(2,-2),(2,-3),(2,-4)]
    res = attach(move, init)
    assert res == expected

def test_get_points():
    init = [(1,1),(2,-2)]
    move_str = 'D2,R3'
    expected = [(1,1),(2,-2),(2,-3),(2,-4),(3,-4),(4,-4),(5,-4)]


def test_intersects():
    w1 = [(0,0),(0,1),(3,3)]
    w2 = [(0,0),(1,0),(2,0),(3,3)]
    common = intersects(w1, w2)
    assert (0,0) in common
    assert (3,3) in common


def test_closest_point_1():
    m1 = 'R8,U5,L5,D3'
    m2 = 'U7,R6,D4,L4'
    assert closes_point(m1, m2) == 6


def test_closest_point_2():
    m1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
    m2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
    assert closes_point(m1, m2) == 159


def test_closest_point_2():
    m1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
    m2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
    assert closes_point(m1, m2) == 135
