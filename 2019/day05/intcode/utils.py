from operator import add, mul
from .opcode import ADD, MUL, END

op_map = {
        ADD: add,
        MUL: mul,
        }

def run_prog(ip, prog):
    try:
        encoded_op_code = prog[ip]
    except IndexError as e:
        raise ValueError(f'Program executing out of bounds.')
    if op_code == END:
        return prog
    else:
        digits = get_digits(encoded_op_code)
        op_code = digits[-2]*10 + digits[-1]
        # modes provided
        given_modes = digits[:-2]
        if op_code == ADD or op_code == MUL:
            nargs = 4
            # empty modes
            modes = np.zeros(nargs)
            missing_digits = nargs - modes.shape[0]
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



def get_digits(number):
    number, digit = divmod(number, 10)
    digits = deque([digit])
    while number > 0:
        number, digit = divmod(number, 10)
        digits.appendleft(digit)
    return np.array(digits)

