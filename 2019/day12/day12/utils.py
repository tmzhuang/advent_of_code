import re
import logging

import numpy as np


logger = logging.getLogger()
LINE_REGEX = r'^\s*<x=(?P<x>[-]?\d+),\s*y=(?P<y>[-]?\d+),\s*z=(?P<z>[-]?\d+)>\s*$'


def advance(position, velocity):
    diff = np.empty_like(velocity)
    breakpoint()
    for i in range(position.shape[0]):
        p = position[i]
        others = np.delete(position, i, axis=0)
        add = np.less(p, others).sum(axis=0)
        sub = np.greater(p, others).sum(axis=0)
        diff[i] = add - sub
    velocity += diff
    position += velocity
    return position, velocity


def run_simulation(position, velocity=None, steps=1, capture_state=False):
    if not velocity:
        velocity = np.zeros(position.shape, dtype=int)
    if capture_state:
        init_state = get_state(position, velocity)
    i = 1
    while True:
        if steps and (i > steps):
            break
        logger.debug(f'{i=}')
        position, velocity = advance(position, velocity)
        if capture_state:
            state = get_state(position, velocity)
            if state == init_state:
                logger.info(f'Found matching state.')
                logger.info(f'{i=}')
                break
        logger.debug(f'{position=}')
        logger.debug(f'{velocity=}\n\n')
        i += 1
    return position, velocity


def calc_energy(position, velocity):
    p = np.abs(position).sum(axis=1)
    v = np.abs(velocity).sum(axis=1)
    return np.dot(p,v)


def get_position(filename):
    position = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            m = re.match(LINE_REGEX, line)
            position.append(np.array([int(m['x']), int(m['y']), int(m['z'])]))
    return np.array(position)


def get_state(position, velocity):
    return position.tobytes() + velocity.tobytes()
