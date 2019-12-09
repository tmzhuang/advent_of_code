from day09.utils import *
from day09.amplifier import Amplifier
from itertools import permutations

original_prog = defaultlist([1102,34915192,34915192,7,4,7,99,0])
# original_prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

def main1():
    prog = original_prog.copy()
    run_prog(0, prog, output='stdout')

def main2():
    pass


if __name__ == '__main__':
    main1()
