from intcode.utils import *

def test_run_prog():
    prog = [1,9,10,3, 2,3,11,0, 99, 30,40,50]
    result = [3500,9,10,70, 2,3,11,0, 99, 30,40,50]
    assert run_prog(0, prog) == result
