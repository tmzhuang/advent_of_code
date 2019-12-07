from operator import add, mul, lt, eq
from collections import deque

import numpy as np

from .opcode import ADD, MUL, GET, PUT, JNZ, JZ, LT, EQ, END
from .addr_mode import POSITION, IMMEDIATE

op_map = {
        ADD: add,
        MUL: mul,
        LT: lt,
        EQ: eq,
        }

def run_prog(ip, prog, phase=None, input_=None, phase_set=False, input_set=False, output=None):
    try:
        encoded_op_code = prog[ip]
    except IndexError as e:
        raise ValueError(f'Program executing out of bounds.')
    op_code, nargs, modes = parse_op_code(encoded_op_code)
    if op_code == END:
        return prog
    else:
        if op_code in [ADD, MUL, LT, EQ]:
            # print(prog[ip:ip+4])
            param1 = get_param(ip+1, modes[0], prog)
            param2 = get_param(ip+2, modes[1], prog)
            dest = prog[ip+3]
            try:
                func = op_map[op_code]
                result = func(param1, param2)
                prog[dest] = result
            except KeyError as e:
                raise ValueError(f'Invalid opcode found: {op_code}.')
        elif op_code == GET:
            # print(prog[ip:ip+2])
            dest = prog[ip+1]
            if not phase_set:
                result = phase
                phase_set = True
            elif not input_set:
                result = input_
                input_set = True
            else:
                result = int(input('Enter input:'))
            try:
                prog[dest] = result
                # print(f'Storing {result} at {dest}')
            except ValueError:
                raise ValueError(f'Invalid input {result}.')
        elif op_code == PUT:
            # print(prog[ip:ip+2])
            dest = prog[ip+1]
            if modes and modes[0] == IMMEDIATE:
                print(dest)
            # print(f'Printing data at {dest}')
            else:
                if output == 'stdout':
                    print(prog[dest])
                else:
                    return prog[dest]
        if op_code in [JNZ, JZ]:
            param1 = get_param(ip+1, modes[0], prog)
            param2 = get_param(ip+2, modes[1], prog)
            if (((op_code == JNZ) and param1 != 0) or
                    ((op_code == JZ) and param1 == 0)):
                ip = param2
                return run_prog(ip, prog, phase=phase, input_=input_, phase_set=phase_set, input_set=input_set, output=output)
        ip += nargs + 1
        return run_prog(ip, prog, phase=phase, input_=input_, phase_set=phase_set, input_set=input_set, output=output)


def get_digits(number):
    number, digit = divmod(number, 10)
    digits = deque([digit])
    while number > 0:
        number, digit = divmod(number, 10)
        digits.appendleft(digit)
    return np.array(digits)


def parse_op_code(encoded_op_code):
    '''
    Given enocded_op_code, returns the real opcode, number of params for the op code,
    and the modes for those params.
    eg. 1002 -> (2, 4, (0,1,0,0))
    '''
    digits = get_digits(encoded_op_code)
    if digits.shape[0] < 2:
        op_code = digits[0]
    else:
        op_code = digits[-2]*10 + digits[-1]
    nargs = get_nargs(op_code)
    # modes encoded in the op code
    given_modes = digits[:-2]
    # eg modes = [0,1,0] indicates modes 0 for param1, 1 for param2, 0 for param3 etc.
    modes = get_modes(nargs, given_modes)
    return op_code, nargs, modes


def get_nargs(op_code):
    if op_code in [ADD, MUL, LT, EQ]:
        return 3
    if op_code in [JNZ, JZ]:
        return 2
    elif op_code in [GET, PUT]:
        return 1
    elif op_code in [END]:
        return 0
    else:
        raise ValueError(f'Could not get nargs for unsupported opcode: {op_code}.')


def get_modes(nargs, modes_arr):
    modes = np.zeros(nargs)
    len_ = modes_arr.shape[0]
    if len_ > nargs:
        raise(f'Given {len_} modes in the op code but the operator only takes {nargs} parameters.')
    start = nargs - len_
    modes[start:] = modes_arr
    # modes are encoded right to left in the op code
    # return modes as left to right
    return np.flip(modes)


def get_param(addr, mode, prog):
    value = prog[addr]
    if mode == POSITION:
        return prog[value]
    elif mode == IMMEDIATE:
        return value
    else:
        raise ValueError(f'Unrecognized addressing mode {mode}.')


def get_thruster_input(phases, prog, input_=0):
    for phase, amp in zip(phases, list('abcde')):
        prog_copy = prog.copy()
        # print(f'INPUT: ({phase}, {input_})')
        # print(amp)
        input_ = run_prog(0, prog_copy, phase=phase, input_=input_)
        # print(f'OUTPUT: {input_}')
    return input_
