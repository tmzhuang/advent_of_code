from collections import deque

import numpy as np

def get_array(min_, max_):
    numbers = []
    for i in range(min_, max_+1):
        numbers.append(get_digits(i))
    return np.array(numbers)


def get_digits(number):
    number, digit = divmod(number, 10)
    digits = deque([digit])
    while number > 0:
        number, digit = divmod(number, 10)
        digits.appendleft(digit)
    return np.array(digits)


def get_valid_passwords(arr):
    pass
