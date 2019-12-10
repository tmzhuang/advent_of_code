from operator import add, mul, lt, eq
from collections import deque

import numpy as np

from .opcode import ADD, MUL, GET, PUT, JNZ, JZ, LT, EQ, REL, END
from .addr_mode import POSITION, IMMEDIATE, RELATIVE
from .iostream import IOStream

op_map = {
        ADD: add,
        MUL: mul,
        LT: lt,
        EQ: eq,
        }

def run_prog(prog, ip=0, rel=0, in_=None, in_arr=[], out=None, out_arr=[], breaks=[], step=False,
        verbose=False):
    if not in_:
        in_ = IOStream(in_='stdin', arr=in_arr)
    if not out:
        out = IOStream(out='stdout', arr=out_arr)
    while True:
        op_code, nargs, modes = parse_op_code(prog[ip])
        if op_code == END:
            return 0
        if (ip in breaks) or step:
            breakpoint()
        params = get_params(ip, nargs, modes, prog, rel)
        if verbose:
            print(f'{ip=}, {rel=}')
            print(prog[ip], params)
        if op_code in [ADD, MUL, LT, EQ]:
            operands, addr, mode = params
            func = op_map[op_code]
            result = int(func(*operands))
            store(prog, result, addr, mode, rel)
        elif op_code == GET:
            _, addr, mode = params
            store(prog, in_.read(), addr, mode, rel)
        elif op_code == PUT:
            _, value, mode = params
            item = resolve(prog, value, mode, rel)
            out.write(item)
        elif op_code == REL:
            _, value, mode = params
            offset = resolve(prog, value, mode, rel)
            rel += offset
        if op_code in [JNZ, JZ]:
            # print(prog[ip])
            operands, value, mode = params
            operand, = operands
            if (((op_code == JNZ) and operand != 0) or
                    ((op_code == JZ) and operand == 0)):
                addr = resolve(prog, value, mode, rel)
                ip = addr
                continue
        ip += nargs + 1


def get_digits(number):
    number, digit = divmod(number, 10)
    digits = deque([digit])
    while number > 0:
        number, digit = divmod(number, 10)
        digits.appendleft(digit)
    return np.array(digits)


def resolve(prog, value, mode, rel):
    if mode == POSITION:
        return prog[value]
    elif mode == RELATIVE:
        return prog[value + rel]
    else:
        return value


def store(prog, value, addr, mode, rel):
    if mode == RELATIVE:
        addr += rel
    if mode not in [POSITION, RELATIVE]:
        raise ValueError(f'Writing with mode {mode} is unsupported.')
    prog[addr] = value


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
    elif op_code in [GET, PUT, REL]:
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


def get_params(base, nargs, modes, prog, rel=0):
    values = [prog[base+i+1] for i in range(nargs)]
    raw_operands = values[:-1]
    operands = []
    for value, mode in zip(raw_operands, modes[:-1]):
        if mode == POSITION:
            value = prog[value]
        elif mode == RELATIVE:
            value = prog[rel+value]
        operands.append(value)
    dest = values[-1]
    addr_mode = modes[-1]
    return operands, dest, addr_mode


class defaultlist(list):
    def _fill(self, index):
        while len(self) <= index:
            self.append(int())

    def __setitem__(self, index, value):
        self._fill(index)
        list.__setitem__(self, index, value)

    def __getitem__(self, index):
        self._fill(index)
        return list.__getitem__(self, index)

    def copy(self):
        return defaultlist(self)
