import numpy as np

from day07.utils import *

def test_get_modes():
    ans = get_modes(4, np.array([1,0]))
    expected = np.array([0,1,0,0])
    assert np.array_equal(ans, expected)


def test_parse_op_code():
    op_code1, nargs1, modes1 = parse_op_code(1002)
    op_code2, nargs2, modes2 = (2, 3, np.array([0,1,0,]))
    assert op_code1 == op_code2
    assert nargs1 == nargs2
    assert np.array_equal(modes1, modes2)


def test_parse_op_code2():
    op_code1, nargs1, modes1 = parse_op_code(99)
    op_code2, nargs2, modes2 = (99, 0, np.array([]))
    assert op_code1 == op_code2
    assert nargs1 == nargs2
    assert np.array_equal(modes1, modes2)


def test_get_param_position():
    addr = 3
    mode = 0
    prog = [0,23,1,4,5]
    assert get_param(addr, mode, prog) == 5


def test_get_param_immediate():
    addr = 3
    mode = 1
    prog = [0,23,1,4,5]
    assert get_param(addr, mode, prog) == 4


def test_get_thruster_input():
    prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    phases = [4,3,2,1,0]
    ans = get_thruster_input(phases, prog)
    expected = 43210
    assert ans == expected


def test_get_thruster_input_2():
    prog = [3,23,3,24,1002,24,10,24,1002,23,-1,23,
            101,5,23,23,1,24,23,23,4,23,99,0,0]
    phases = [0,1,2,3,4]
    ans = get_thruster_input(phases, prog)
    expected = 54321
    assert ans == expected
