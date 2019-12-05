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
    arr = filter_order_rule(arr)
    arr = filter_adjacent_double_rule(arr)
    return arr


def filter_order_rule(arr):
    width = arr.shape[1]
    for i in range(width-1):
        arr = arr[arr[:,i] <= arr[:,i+1]]
    return arr


def filter_adjacent_double_rule(arr):
    # Get booleans of if adjacent element have a absolute
    # different that is non-zero
    bools = np.diff(arr, axis=1) == 0
    mask = np.apply_along_axis(np.logical_or.reduce, 1, bools)
    return arr[mask]

def updated_filter_adjacent_double_rule(arr):
    # Get booleans of if adjacent element have a absolute
    # different that is non-zero
    bools = np.diff(arr, axis=1) == 0
    mask = np.apply_along_axis(reduce_bool_row, 1, bools)
    return arr[mask]


def reduce_bool_row(bool_row):
    for i, p in enumerate(bool_row):
        if i == 0:
            prev = False
        else:
            prev = bool_row[i-1]
        if i == (len(bool_row) - 1):
            next = False
        else:
            next = bool_row[i+1]
        if p and not prev and not next:
            return True
    return False
