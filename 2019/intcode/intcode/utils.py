from operator import add, mul
from .opcode import ADD, MUL, END

op_map = {
        ADD: add,
        MUL: mul,
        }

def run_prog(ip, prog):
    try:
        op_code = prog[ip]
    except IndexError as e:
        raise ValueError(f'Program executing out of bounds.')
    if op_code == END:
        return prog
    else:
        param1 = prog[prog[ip+1]]
        param2 = prog[prog[ip+2]]
        dest = prog[ip+3]
        ip += 4
        try:
            func = op_map[op_code]
        except KeyError as e:
            raise ValueError(f'Invalid opcode found: {op_code}.')
        prog[dest] = func(param1, param2)
        return run_prog(ip, prog)
