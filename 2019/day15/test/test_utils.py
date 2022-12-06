import numpy as np

from day15.utils import *
from day15.amplifier import Amplifier

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


def test_amplifer():
    prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,
            27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    prog_copy = prog.copy()
    output, _, _ = run_prog(0, prog_copy, phase=0, input_=0)
    amp = Amplifier(name='a', prog=prog, phase=0)
    assert amp.run(0) == output


def test_defaultlist():
    l = defaultlist([1,2,3])
    l[5] = 5
    assert l == [1,2,3,0,0,5]
    assert l[10] == 0
